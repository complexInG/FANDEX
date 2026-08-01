/**
 * 思维导图连线原子组件
 * -----------------------------------------------------------------------------
 * 根据布局计算出的锚点渲染贝塞尔曲线；根节点到阶段的连线带箭头标记。
 */
import { edgePath, type LayoutEdge } from './map-layout';

interface Props {
  /** 连线定义 */
  edge: LayoutEdge;
  /** 阶段主题色（箭头与连线着色） */
  color: string;
}

/** 连线组件：纯展示，无状态 */
export default function MapEdge({ edge, color }: Props) {
  const isRootEdge = edge.kind === 'root-stage';
  const markerId = `lp-arrow-${edge.stageId}`;
  return (
    <path
      d={edgePath(edge)}
      className="lp-edge"
      stroke={isRootEdge ? color : undefined}
      markerEnd={isRootEdge ? `url(#${markerId})` : undefined}
    />
  );
}
