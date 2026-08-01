/**
 * 思维导图详情面板
 * -----------------------------------------------------------------------------
 * 展示当前悬停/选中知识点的说明、难度、文档状态与跳转入口；
 * 待补充节点提供官方资料兜底与"定位到节点"操作。
 */
import type { CSSProperties } from 'react';
import type { NodeVM } from './types';

interface Props {
  /** 当前节点（null 时显示引导提示） */
  node: NodeVM | null;
  /** 技术标题 */
  techTitle: string;
  /** 技术主题色 */
  color: string;
  /** 关闭选中 */
  onClose: () => void;
  /** 定位到节点（画布居中） */
  onFocus: () => void;
}

/** 难度中文标签 */
const DIFFICULTY_LABEL: Record<string, string> = {
  beginner: '入门',
  intermediate: '中级',
  advanced: '进阶',
};

/** 详情面板：无节点时展示引导，有节点时展示完整信息 */
export default function MapDetailPanel({ node, techTitle, color, onClose, onFocus }: Props) {
  if (!node) {
    return (
      <aside className="lp-panel lp-panel--empty">
        <div className="lp-panel__icon" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8">
            <circle cx="11" cy="11" r="7" />
            <line x1="21" y1="21" x2="16.5" y2="16.5" />
          </svg>
        </div>
        <p className="lp-panel__hint">
          悬停或点击知识点节点，查看该知识点的说明与文档入口。
        </p>
        <p className="lp-panel__sub">虚线节点表示文档待补充，可先参考官方资料。</p>
      </aside>
    );
  }

  const planned = !node.href;
  return (
    <aside className="lp-panel" style={{ '--lp-panel-color': color } as CSSProperties}>
      <div className="lp-panel__head">
        <span className="lp-panel__stage">{node.stageTitle}</span>
        <button type="button" className="fndx-icon-btn" onClick={onClose} aria-label="关闭详情">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <line x1="18" y1="6" x2="6" y2="18" />
            <line x1="6" y1="6" x2="18" y2="18" />
          </svg>
        </button>
      </div>
      <h3 className="lp-panel__title">{node.title}</h3>
      <div className="lp-panel__meta">
        {node.difficulty && (
          <span className={`lp-panel__difficulty diff-${node.difficulty}`}>
            {DIFFICULTY_LABEL[node.difficulty] ?? node.difficulty}
          </span>
        )}
        <span className={`lp-panel__status${planned ? ' lp-panel__status--planned' : ''}`}>
          {planned ? '文档待补充' : '已发布'}
        </span>
      </div>
      {node.desc && <p className="lp-panel__desc">{node.desc}</p>}

      {node.href ? (
        <a className="lp-panel__doc-link" href={node.href}>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
            <polyline points="14 2 14 8 20 8" />
            <line x1="16" y1="13" x2="8" y2="13" />
            <line x1="16" y1="17" x2="8" y2="17" />
          </svg>
          {node.docTitle ? `阅读：${node.docTitle}` : '阅读专项文档'}
        </a>
      ) : (
        <div className="lp-panel__notice">
          该知识点暂未发布专项文档，可先通过官方资料学习。
        </div>
      )}

      {node.official && (
        <a
          className="lp-panel__official"
          href={node.official.url}
          target="_blank"
          rel="noopener noreferrer"
        >
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
            <polyline points="15 3 21 3 21 9" />
            <line x1="10" y1="14" x2="21" y2="3" />
          </svg>
          {node.official.label}
        </a>
      )}

      <button type="button" className="lp-panel__locate" onClick={onFocus}>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <circle cx="12" cy="12" r="3" />
          <circle cx="12" cy="12" r="9" />
        </svg>
        在地图中定位
      </button>
      <p className="lp-panel__footer">{techTitle} 学习路线</p>
    </aside>
  );
}
