/**
 * 思维导图布局纯函数
 * -----------------------------------------------------------------------------
 * 布局模型（右向思维导图）：
 * - 根节点（技术）位于最左侧
 * - 每个阶段是一列分支，阶段标题位于列首
 * - 阶段内知识点自上而下纵向连接，形成知识链
 *
 * 设计要点：
 * - 纯函数、无 DOM 依赖，便于单测与复用
 * - 布局只计算一次（useMemo），折叠阶段时增量重算
 * - 坐标均为节点矩形左上角，连线锚点由调用方推导
 */
import type { StageVM } from './types';

/** 布局尺寸常量（与 CSS 中节点视觉尺寸保持一致） */
export const LAYOUT = {
  /** 根节点宽度 */
  rootWidth: 176,
  /** 根节点高度 */
  rootHeight: 56,
  /** 节点卡片宽度 */
  nodeWidth: 244,
  /** 节点卡片高度 */
  nodeHeight: 64,
  /** 阶段内节点垂直间距 */
  nodeGap: 18,
  /** 阶段标题高度 */
  headerHeight: 48,
  /** 阶段列水平间距 */
  stageGap: 56,
  /** 根节点与首列间距 */
  rootGap: 48,
  /** 画布内边距 */
  padding: 28,
} as const;

/** 节点放置结果 */
export interface PlacedNode {
  /** 节点 ID */
  id: string;
  /** 左上角 x */
  x: number;
  /** 左上角 y */
  y: number;
  /** 所属阶段 ID */
  stageId: string;
}

/** 阶段放置结果 */
export interface PlacedStage {
  /** 阶段 ID */
  id: string;
  /** 左上角 x */
  x: number;
  /** 阶段标题区 y */
  y: number;
  /** 阶段总高度（含标题与节点链） */
  height: number;
  /** 节点放置结果 */
  nodes: PlacedNode[];
}

/** 连线定义 */
export interface LayoutEdge {
  /** 起点（绝对坐标） */
  from: { x: number; y: number };
  /** 终点（绝对坐标） */
  to: { x: number; y: number };
  /** 所属阶段 ID（用于着色与折叠） */
  stageId: string;
  /** 连线类型 */
  kind: 'root-stage' | 'stage-node' | 'node-node';
}

/** 完整布局结果 */
export interface MapLayout {
  /** 画布宽 */
  width: number;
  /** 画布高 */
  height: number;
  /** 根节点位置 */
  root: { x: number; y: number; width: number; height: number };
  /** 阶段放置结果 */
  stages: PlacedStage[];
  /** 全部连线 */
  edges: LayoutEdge[];
}

/**
 * 计算阶段内节点纵向布局
 * @param nodes - 阶段内节点
 * @param x - 阶段列 x
 * @param y - 首节点 y
 * @returns 节点位置数组
 */
function layoutStageNodes(
  nodes: StageVM['nodes'],
  x: number,
  y: number,
): PlacedNode[] {
  return nodes.map((node, index) => ({
    id: node.id,
    x,
    y: y + index * (LAYOUT.nodeHeight + LAYOUT.nodeGap),
    stageId: node.stageId,
  }));
}

/**
 * 计算整张思维导图布局
 * @param stages - 阶段视图模型（已按顺序排列）
 * @param collapsedStageIds - 折叠的阶段 ID 集合（折叠后仅保留标题）
 * @returns 布局结果
 */
export function computeMapLayout(
  stages: StageVM[],
  collapsedStageIds: ReadonlySet<string>,
): MapLayout {
  const { padding, rootWidth, rootGap, stageGap, nodeWidth, headerHeight } = LAYOUT;

  // 根节点垂直居中于首列中心，先按首列高度估算（最终高度取最大值后不做二次居中，
  // 根节点固定在顶部标题对齐位置，视觉上更稳定）
  const rootY = padding;

  const placedStages: PlacedStage[] = [];
  const edges: LayoutEdge[] = [];

  stages.forEach((stage, index) => {
    const x = padding + rootWidth + rootGap + index * (nodeWidth + stageGap);
    const visibleNodes = collapsedStageIds.has(stage.id) ? [] : stage.nodes;
    const nodes = layoutStageNodes(visibleNodes, x, padding + headerHeight + 12);
    const height =
      headerHeight +
      (nodes.length > 0
        ? 12 + nodes.length * LAYOUT.nodeHeight + (nodes.length - 1) * LAYOUT.nodeGap
        : 0);

    placedStages.push({ id: stage.id, x, y: padding, height, nodes });

    // 根节点 -> 阶段标题（水平贝塞尔）
    const rootRight = padding + rootWidth;
    const rootCenterY = rootY + LAYOUT.rootHeight / 2;
    edges.push({
      from: { x: rootRight, y: rootCenterY },
      to: { x, y: padding + headerHeight / 2 },
      stageId: stage.id,
      kind: 'root-stage',
    });

    // 阶段标题 -> 首节点 / 节点 -> 下一节点（纵向贝塞尔）
    const headerBottom = padding + headerHeight;
    const headerCenterX = x + nodeWidth / 2;
    nodes.forEach((node, nodeIndex) => {
      const prevNode = nodeIndex === 0 ? undefined : nodes[nodeIndex - 1];
      const fromY =
        nodeIndex === 0 || !prevNode
          ? headerBottom
          : prevNode.y + LAYOUT.nodeHeight;
      edges.push({
        from: { x: headerCenterX, y: fromY },
        to: { x: headerCenterX, y: node.y },
        stageId: stage.id,
        kind: nodeIndex === 0 ? 'stage-node' : 'node-node',
      });
    });
  });

  // 画布尺寸 = 最后一列右边界 + 内边距；高度 = 最高列 + 内边距
  const lastStage = placedStages[placedStages.length - 1];
  const width = lastStage
    ? lastStage.x + nodeWidth + padding
    : padding + rootWidth + padding;
  const maxHeight = placedStages.reduce((max, stage) => Math.max(max, stage.height), 0);
  const height = maxHeight + padding * 2;

  return {
    width,
    height,
    root: { x: padding, y: rootY, width: rootWidth, height: LAYOUT.rootHeight },
    stages: placedStages,
    edges,
  };
}

/**
 * 生成节点 -> 坐标映射（供详情面板定位使用）
 * @param layout - 布局结果
 * @returns 节点 ID 到中心坐标的映射
 */
export function getNodeCenters(layout: MapLayout): Map<string, { x: number; y: number }> {
  const centers = new Map<string, { x: number; y: number }>();
  for (const stage of layout.stages) {
    for (const node of stage.nodes) {
      centers.set(node.id, {
        x: node.x + LAYOUT.nodeWidth / 2,
        y: node.y + LAYOUT.nodeHeight / 2,
      });
    }
  }
  return centers;
}

/**
 * 生成 SVG 路径（贝塞尔曲线）
 * 水平连线：二次控制点向中点收缩；纵向连线：直线化曲线过渡
 * @param edge - 连线定义
 * @returns path d 属性
 */
export function edgePath(edge: LayoutEdge): string {
  const { from, to } = edge;
  if (edge.kind === 'root-stage') {
    const dx = Math.max(24, Math.min(72, (to.x - from.x) / 2));
    return `M ${from.x} ${from.y} C ${from.x + dx} ${from.y}, ${to.x - dx} ${to.y}, ${to.x} ${to.y}`;
  }
  const dy = 14;
  return `M ${from.x} ${from.y} C ${from.x} ${from.y + dy}, ${to.x} ${to.y - dy}, ${to.x} ${to.y}`;
}
