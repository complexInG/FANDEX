/**
 * 思维导图 SVG 画布
 * -----------------------------------------------------------------------------
 * 职责：
 * - 渲染根节点、阶段列、连线与知识点节点（全部自绘 SVG，无第三方图形库）
 * - 提供平移（拖拽）、缩放（滚轮/按钮/键盘）、适应视口与节点定位能力
 *
 * 性能设计：
 * - 变换矩阵存放在 ref 中，直接修改 DOM transform 属性，避免拖动/滚轮时触发 React 重渲染
 * - 缩放读数通过 rAF 节流回传，面板状态更新频率受限
 * - 布局由父组件 useMemo 计算，画布内不做重复计算
 */
import {
  forwardRef,
  useCallback,
  useEffect,
  useImperativeHandle,
  useLayoutEffect,
  useRef,
} from 'react';
import type { TechVM } from './types';
import {
  LAYOUT,
  getNodeCenters,
  type LayoutEdge,
  type MapLayout,
} from './map-layout';
import MapEdge from './MapEdge';
import MapNode from './MapNode';
import MapStage from './MapStage';

/** 画布对外能力（供主岛调用） */
export interface MapCanvasHandle {
  /** 以画布中心为锚点缩放 */
  zoomBy: (factor: number) => void;
  /** 适应视口 */
  fit: () => void;
  /** 复位到 100% */
  reset: () => void;
  /** 将指定节点居中 */
  focusNode: (id: string) => void;
}

interface Props {
  /** 技术视图模型 */
  tech: TechVM;
  /** 站点基础路径 */
  base: string;
  /** 布局结果 */
  layout: MapLayout;
  /** 折叠的阶段 ID 集合 */
  collapsedStageIds: ReadonlySet<string>;
  /** 选中节点 ID */
  selectedId: string | null;
  /** 悬停节点 ID */
  hoverId: string | null;
  /** 选中节点 */
  onSelectNode: (id: string) => void;
  /** 悬停/移出节点 */
  onHoverNode: (id: string | null) => void;
  /** 折叠/展开阶段 */
  onToggleStage: (id: string) => void;
  /** 缩放百分比回传（rAF 节流） */
  onScaleChange?: (percent: number) => void;
}

/** 缩放范围 */
const MIN_SCALE = 0.3;
const MAX_SCALE = 2.5;
/** 拖拽与点击的位移阈值（超过则视为拖拽） */
const DRAG_THRESHOLD = 4;

/**
 * 计算视口可用尺寸（容器减去留白）
 */
function viewportSize(container: HTMLElement): { width: number; height: number } {
  const rect = container.getBoundingClientRect();
  return { width: Math.max(rect.width, 120), height: Math.max(rect.height, 120) };
}

/**
 * SVG 画布组件
 * 通过 forwardRef 暴露缩放/定位命令式接口
 */
const MapCanvas = forwardRef<MapCanvasHandle, Props>(function MapCanvas(
  {
    tech,
    base,
    layout,
    collapsedStageIds,
    selectedId,
    hoverId,
    onSelectNode,
    onHoverNode,
    onToggleStage,
    onScaleChange,
  },
  ref,
) {
  /** 容器（决定视口尺寸） */
  const containerRef = useRef<HTMLDivElement>(null);
  /** SVG 元素 */
  const svgRef = useRef<SVGSVGElement>(null);
  /** 内容组（transform 直接作用于此） */
  const contentRef = useRef<SVGGElement>(null);
  /** 当前变换：x/y 平移、k 缩放 */
  const transformRef = useRef({ x: 0, y: 0, k: 1 });
  /** 拖拽状态 */
  const dragRef = useRef({ active: false, moved: false, startX: 0, startY: 0, tx: 0, ty: 0 });
  /** 缩放读数 rAF 节流标志 */
  const scaleRafRef = useRef(0);

  /** 应用当前变换到内容组（直接改 DOM，不触发 React 重渲染） */
  const applyTransform = useCallback(() => {
    const { x, y, k } = transformRef.current;
    contentRef.current?.setAttribute('transform', `translate(${x} ${y}) scale(${k})`);
    if (onScaleChange && scaleRafRef.current === 0) {
      scaleRafRef.current = requestAnimationFrame(() => {
        scaleRafRef.current = 0;
        onScaleChange(k * 100);
      });
    }
  }, [onScaleChange]);

  /** 缩放（围绕锚点） */
  const zoomAt = useCallback(
    (cx: number, cy: number, factor: number) => {
      const t = transformRef.current;
      const nextK = Math.min(MAX_SCALE, Math.max(MIN_SCALE, t.k * factor));
      if (nextK === t.k) return;
      // 保持锚点（cx, cy）在缩放前后指向相同的内容坐标
      t.x = cx - ((cx - t.x) * nextK) / t.k;
      t.y = cy - ((cy - t.y) * nextK) / t.k;
      t.k = nextK;
      applyTransform();
    },
    [applyTransform],
  );

  /** 适应视口：整图缩放并居中 */
  const fit = useCallback(() => {
    const container = containerRef.current;
    if (!container) return;
    const { width: vw, height: vh } = viewportSize(container);
    const pad = 24;
    const k = Math.min(
      MAX_SCALE,
      Math.max(MIN_SCALE, Math.min((vw - pad * 2) / layout.width, (vh - pad * 2) / layout.height)),
    );
    const t = transformRef.current;
    t.k = k;
    t.x = (vw - layout.width * k) / 2;
    t.y = (vh - layout.height * k) / 2;
    applyTransform();
  }, [applyTransform, layout]);

  /** 复位：100% 并居中 */
  const reset = useCallback(() => {
    const container = containerRef.current;
    if (!container) return;
    const { width: vw, height: vh } = viewportSize(container);
    const t = transformRef.current;
    t.k = 1;
    t.x = (vw - layout.width) / 2;
    t.y = (vh - layout.height) / 2;
    applyTransform();
  }, [applyTransform, layout]);

  /** 将指定节点居中（保持当前缩放，至少放大到 100%） */
  const focusNode = useCallback(
    (id: string) => {
      const container = containerRef.current;
      const center = getNodeCenters(layout).get(id);
      if (!container || !center) return;
      const { width: vw, height: vh } = viewportSize(container);
      const t = transformRef.current;
      if (t.k < 1) t.k = 1;
      t.x = vw / 2 - center.x * t.k;
      t.y = vh / 2 - center.y * t.k;
      applyTransform();
    },
    [applyTransform, layout],
  );

  /** 对外暴露命令式接口 */
  useImperativeHandle(ref, () => ({
    zoomBy: (factor: number) => {
      const container = containerRef.current;
      if (!container) return;
      const { width: vw, height: vh } = viewportSize(container);
      zoomAt(vw / 2, vh / 2, factor);
    },
    fit,
    reset,
    focusNode,
  }));

  /** 首次渲染与布局变化后自适应 */
  useLayoutEffect(() => {
    const raf = requestAnimationFrame(fit);
    return () => cancelAnimationFrame(raf);
  }, [fit]);

  /** 容器尺寸变化时重新适应 */
  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;
    const observer = new ResizeObserver(() => fit());
    observer.observe(container);
    return () => observer.disconnect();
  }, [fit]);

  /** 滚轮缩放：原生监听以支持 preventDefault（React 的 wheel 为 passive） */
  useEffect(() => {
    const svg = svgRef.current;
    if (!svg) return;
    const onWheel = (event: WheelEvent) => {
      event.preventDefault();
      const rect = svg.getBoundingClientRect();
      zoomAt(event.clientX - rect.left, event.clientY - rect.top, Math.exp(-event.deltaY * 0.0012));
    };
    svg.addEventListener('wheel', onWheel, { passive: false });
    return () => svg.removeEventListener('wheel', onWheel);
  }, [zoomAt]);

  /** 拖拽平移 */
  const onPointerDown = (event: React.PointerEvent<SVGSVGElement>) => {
    if (event.button !== 0) return;
    // 仅在点击画布空白处时启动平移；
    // 若从节点按下，指针捕获会把后续 click 重定向到画布，导致节点链接无法打开
    if (event.target !== event.currentTarget) return;
    const t = transformRef.current;
    dragRef.current = {
      active: true,
      moved: false,
      startX: event.clientX,
      startY: event.clientY,
      tx: t.x,
      ty: t.y,
    };
    event.currentTarget.setPointerCapture(event.pointerId);
  };

  const onPointerMove = (event: React.PointerEvent<SVGSVGElement>) => {
    const drag = dragRef.current;
    if (!drag.active) return;
    const dx = event.clientX - drag.startX;
    const dy = event.clientY - drag.startY;
    if (!drag.moved && Math.hypot(dx, dy) > DRAG_THRESHOLD) drag.moved = true;
    if (drag.moved) {
      const t = transformRef.current;
      t.x = drag.tx + dx;
      t.y = drag.ty + dy;
      applyTransform();
    }
  };

  const onPointerUp = (event: React.PointerEvent<SVGSVGElement>) => {
    if (!dragRef.current.active) return;
    dragRef.current.active = false;
    event.currentTarget.releasePointerCapture(event.pointerId);
  };

  /** 拖拽结束后抑制一次点击（防止拖拽触发链接跳转） */
  const onClickCapture = (event: React.MouseEvent<SVGSVGElement>) => {
    if (dragRef.current.moved) {
      event.preventDefault();
      event.stopPropagation();
      dragRef.current.moved = false;
    }
  };

  /** 键盘操作：+/- 缩放、0 适应、方向键平移 */
  const onKeyDown = (event: React.KeyboardEvent<HTMLDivElement>) => {
    const t = transformRef.current;
    switch (event.key) {
      case '+':
      case '=':
        zoomAt(window.innerWidth / 2, window.innerHeight / 2, 1.2);
        break;
      case '-':
        zoomAt(window.innerWidth / 2, window.innerHeight / 2, 1 / 1.2);
        break;
      case '0':
        fit();
        break;
      case 'ArrowLeft':
        t.x += 48;
        applyTransform();
        break;
      case 'ArrowRight':
        t.x -= 48;
        applyTransform();
        break;
      case 'ArrowUp':
        t.y += 48;
        applyTransform();
        break;
      case 'ArrowDown':
        t.y -= 48;
        applyTransform();
        break;
      default:
        return;
    }
    event.preventDefault();
  };

  return (
    <div
      className="lp-canvas"
      ref={containerRef}
      tabIndex={0}
      role="application"
      aria-label={`${tech.title} 学习路线思维导图，支持拖拽平移与滚轮缩放`}
      onKeyDown={onKeyDown}
    >
      <svg
        className="lp-canvas__svg"
        ref={svgRef}
        onPointerDown={onPointerDown}
        onPointerMove={onPointerMove}
        onPointerUp={onPointerUp}
        onClickCapture={onClickCapture}
      >
        <defs>
          {/* 根节点到阶段连线的箭头标记（按阶段独立着色） */}
          {layout.stages.map((stage) => (
            <marker
              key={stage.id}
              id={`lp-arrow-${stage.id}`}
              viewBox="0 0 10 10"
              refX="9"
              refY="5"
              markerWidth="7"
              markerHeight="7"
              orient="auto-start-reverse"
            >
              <path d="M 0 0 L 10 5 L 0 10 z" fill={tech.color} />
            </marker>
          ))}
        </defs>
        <g ref={contentRef}>
          {/* 根节点：技术入口，点击进入模块文档列表 */}
          <g transform={`translate(${layout.root.x} ${layout.root.y})`}>
            <a href={`${base}${tech.module}/`} className="lp-root">
              <rect
                className="lp-root__rect"
                width={layout.root.width}
                height={layout.root.height}
                rx={2}
              />
              <text className="lp-root__icon" x={12} y={22}>
                {tech.icon}
              </text>
              <text className="lp-root__title" x={12} y={42}>
                {tech.title}
              </text>
              <text className="lp-root__count" x={layout.root.width - 12} y={20} textAnchor="end">
                {tech.stats.nodes} 知识点
              </text>
            </a>
          </g>

          {/* 连线层 */}
          {layout.edges.map((edge: LayoutEdge, index: number) => (
            <MapEdge key={`${edge.stageId}-${index}`} edge={edge} color={tech.color} />
          ))}

          {/* 阶段层：标题 + 节点链 */}
          {layout.stages.map((placedStage, stageIndex) => {
            const stage = tech.stages[stageIndex];
            if (!stage) return null;
            return (
              <MapStage
                key={stage.id}
                stage={stage}
                index={stageIndex + 1}
                x={placedStage.x}
                y={placedStage.y}
                color={tech.color}
                collapsed={collapsedStageIds.has(stage.id)}
                onToggle={onToggleStage}
              >
                {placedStage.nodes.map((placedNode, nodeIndex) => {
                  const node = stage.nodes.find((n) => n.id === placedNode.id);
                  if (!node) return null;
                  return (
                    <MapNode
                      key={node.id}
                      node={node}
                      x={placedNode.x - placedStage.x}
                      y={placedNode.y - placedStage.y}
                      index={nodeIndex + 1}
                      width={LAYOUT.nodeWidth}
                      height={LAYOUT.nodeHeight}
                      selected={selectedId === node.id}
                      hovered={hoverId === node.id}
                      onSelect={onSelectNode}
                      onHover={onHoverNode}
                    />
                  );
                })}
              </MapStage>
            );
          })}
        </g>
      </svg>
    </div>
  );
});

export default MapCanvas;
