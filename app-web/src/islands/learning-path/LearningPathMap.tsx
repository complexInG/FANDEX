/**
 * 学习路径思维导图主岛
 * -----------------------------------------------------------------------------
 * 组合层：持有选中/悬停/折叠状态，组装画布、控制条与详情面板。
 * 数据来源：由 Astro 页面注入的 TechVM（服务端组装，客户端不加载地图 JSON）。
 */
import { useCallback, useMemo, useRef, useState, type CSSProperties } from 'react';
import type { TechVM } from './types';
import { computeMapLayout } from './map-layout';
import MapCanvas, { type MapCanvasHandle } from './MapCanvas';
import MapControls from './MapControls';
import MapDetailPanel from './MapDetailPanel';

interface Props {
  /** 技术视图模型 */
  tech: TechVM;
  /** 站点基础路径 */
  base: string;
}

/** 学习路径思维导图 */
export default function LearningPathMap({ tech, base }: Props) {
  /** 选中节点 ID（点击待补充节点触发） */
  const [selectedId, setSelectedId] = useState<string | null>(null);
  /** 悬停节点 ID（优先于选中态展示） */
  const [hoverId, setHoverId] = useState<string | null>(null);
  /** 折叠的阶段 ID 集合 */
  const [collapsedStageIds, setCollapsedStageIds] = useState<ReadonlySet<string>>(
    () => new Set(),
  );
  /** 缩放百分比 */
  const [scale, setScale] = useState(100);
  /** 画布命令式接口 */
  const canvasRef = useRef<MapCanvasHandle>(null);

  /** 布局：阶段/节点/连线坐标（折叠变化时增量重算） */
  const layout = useMemo(
    () => computeMapLayout(tech.stages, collapsedStageIds),
    [tech.stages, collapsedStageIds],
  );

  /** 面板展示节点：优先悬停，其次选中 */
  const panelNode = useMemo(() => {
    const id = hoverId ?? selectedId;
    if (!id) return null;
    for (const stage of tech.stages) {
      const node = stage.nodes.find((n) => n.id === id);
      if (node) return node;
    }
    return null;
  }, [hoverId, selectedId, tech.stages]);

  /** 选中节点 */
  const handleSelectNode = useCallback((id: string) => {
    setSelectedId(id);
  }, []);

  /** 悬停节点 */
  const handleHoverNode = useCallback((id: string | null) => {
    setHoverId(id);
  }, []);

  /** 折叠/展开阶段 */
  const handleToggleStage = useCallback((id: string) => {
    setCollapsedStageIds((prev) => {
      const next = new Set(prev);
      if (next.has(id)) {
        next.delete(id);
      } else {
        next.add(id);
      }
      return next;
    });
  }, []);

  /** 在地图中定位当前节点 */
  const handleLocate = useCallback(() => {
    const id = hoverId ?? selectedId;
    if (id) canvasRef.current?.focusNode(id);
  }, [hoverId, selectedId]);

  return (
    <div className="lp-map" style={{ '--lp-color': tech.color } as CSSProperties}>
      {/* 顶部控制条（统计信息已上移至页面 Hero，与语法速览页布局一致） */}
      <div className="lp-map__toolbar">
        <MapControls
          scale={scale}
          onZoomOut={() => canvasRef.current?.zoomBy(1 / 1.25)}
          onZoomIn={() => canvasRef.current?.zoomBy(1.25)}
          onFit={() => canvasRef.current?.fit()}
          onReset={() => canvasRef.current?.reset()}
        />
      </div>

      {/* 画布 + 详情面板 */}
      <div className="lp-map__body">
        <MapCanvas
          ref={canvasRef}
          tech={tech}
          base={base}
          layout={layout}
          collapsedStageIds={collapsedStageIds}
          selectedId={selectedId}
          hoverId={hoverId}
          onSelectNode={handleSelectNode}
          onHoverNode={handleHoverNode}
          onToggleStage={handleToggleStage}
          onScaleChange={setScale}
        />
        <MapDetailPanel
          node={panelNode}
          techTitle={tech.title}
          color={tech.color}
          onClose={() => {
            setSelectedId(null);
            setHoverId(null);
          }}
          onFocus={handleLocate}
        />
      </div>

      {/* 图例 */}
      <div className="lp-map__legend" aria-label="图例">
        <span className="lp-legend-item">
          <i className="lp-legend-line" />
          已发布文档
        </span>
        <span className="lp-legend-item">
          <i className="lp-legend-line lp-legend-line--planned" />
          文档待补充
        </span>
        <span className="lp-legend-item">
          <i className="lp-legend-dot lp-legend-dot--beginner" />
          入门
        </span>
        <span className="lp-legend-item">
          <i className="lp-legend-dot lp-legend-dot--intermediate" />
          中级
        </span>
        <span className="lp-legend-item">
          <i className="lp-legend-dot lp-legend-dot--advanced" />
          进阶
        </span>
      </div>
    </div>
  );
}
