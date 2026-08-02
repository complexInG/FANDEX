/**
 * 思维导图知识点节点原子组件
 * -----------------------------------------------------------------------------
 * - 已发布节点渲染为 SVG 链接（整卡可点，支持新标签打开）
 * - 待补充节点渲染为按钮（点击选中并查看详情）
 * - 标题自动换行（最多两行），尾部显示难度竖条与状态
 */
import type { NodeVM } from './types';

interface Props {
  /** 节点视图模型 */
  node: NodeVM;
  /** 节点左上角 x */
  x: number;
  /** 节点左上角 y */
  y: number;
  /** 阶段内序号（从 1 开始） */
  index: number;
  /** 节点宽度 */
  width: number;
  /** 节点高度 */
  height: number;
  /** 是否选中 */
  selected: boolean;
  /** 是否悬停 */
  hovered: boolean;
  /** 点击待补充节点 */
  onSelect: (id: string) => void;
  /** 悬停/移出节点 */
  onHover: (id: string | null) => void;
}

/** 标题单行最大字符数（CJK 字符约等于字号宽度） */
const LINE_CHARS = 17;

/**
 * 标题换行：按字符数拆分为最多两行，超出部分省略
 * @param title - 原始标题
 * @returns 行数组（1-2 行）
 */
function wrapTitle(title: string): string[] {
  if (title.length <= LINE_CHARS) return [title];
  const first = title.slice(0, LINE_CHARS);
  const rest = title.slice(LINE_CHARS);
  return [first, rest.length > LINE_CHARS ? `${rest.slice(0, LINE_CHARS - 1)}…` : rest];
}

/** 节点内容（矩形 + 文本 + 元信息） */
function NodeBody({ node, index, width, height }: Props) {
  const lines = wrapTitle(node.title);
  const planned = !node.href;
  return (
    <>
      <rect
        className={`lp-node__rect${planned ? ' lp-node__rect--planned' : ''}`}
        x={0}
        y={0}
        width={width}
        height={height}
        rx={2}
      />
      {/* 序号 */}
      <text className="lp-node__seq" x={width - 10} y={16} textAnchor="end">
        {String(index).padStart(2, '0')}
      </text>
      {/* 标题（1-2 行） */}
      {lines.map((line, i) => (
        <text
          key={i}
          className="lp-node__title"
          x={12}
          y={i === 0 ? 20 : 37}
        >
          {line}
        </text>
      ))}
      {/* 元信息：难度竖条 + 状态 + 序号 */}
      <rect
        className={`lp-node__bar lp-node__bar--${node.difficulty ?? 'intermediate'}`}
        x={10}
        y={height - 19}
        width={4}
        height={10}
        rx={1}
      />
      <text className="lp-node__status" x={21} y={height - 11}>
        {planned ? '文档待补充' : '已发布'}
      </text>
    </>
  );
}

/** 知识点节点 */
export default function MapNode(props: Props) {
  const { node, x, y, selected, hovered, onSelect, onHover } = props;
  const commonProps = {
    transform: `translate(${x} ${y})`,
    className: `lp-node${selected ? ' lp-node--selected' : ''}${
      hovered ? ' lp-node--hovered' : ''
    }`,
    onPointerEnter: () => onHover(node.id),
    onPointerLeave: () => onHover(null),
  };

  if (node.href) {
    return (
      <a
        href={node.href}
        {...commonProps}
        aria-label={`${node.title}（阅读专项文档）`}
      >
        <NodeBody {...props} />
      </a>
    );
  }

  return (
    <g
      role="button"
      tabIndex={0}
      aria-label={`${node.title}（文档待补充）`}
      onClick={() => onSelect(node.id)}
      onKeyDown={(event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          onSelect(node.id);
        }
      }}
      {...commonProps}
    >
      <NodeBody {...props} />
    </g>
  );
}
