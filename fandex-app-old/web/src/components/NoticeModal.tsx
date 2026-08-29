/**
 * 全局公告弹窗组件
 * 用途:展示 FANDEX 体系整合与重构的维护调整公告
 * 交互:支持 ESC/遮罩/按钮关闭
 * 持久化:由父组件(App)基于 sessionStorage 控制是否自动弹出
 * 美术:对齐 FANDEX-Web 设计系统(Sky 主色 + Amber 强调 + Slate 中性)
 */
import { useEffect, useCallback } from 'react';

interface NoticeModalProps {
  open: boolean;
  onClose: () => void;
}

export function NoticeModal({ open, onClose }: NoticeModalProps) {
  // ESC 键关闭 + 锁定 body 滚动
  useEffect(() => {
    if (!open) return;
    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    document.addEventListener('keydown', onKeyDown);
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    return () => {
      document.removeEventListener('keydown', onKeyDown);
      document.body.style.overflow = prevOverflow;
    };
  }, [open, onClose]);

  const handleMaskClick = useCallback(
    (e: React.MouseEvent<HTMLDivElement>) => {
      // 仅点击遮罩层本身时关闭,点击弹窗内容不关闭
      if (e.target === e.currentTarget) onClose();
    },
    [onClose],
  );

  if (!open) return null;

  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-labelledby="notice-title"
      onClick={handleMaskClick}
      className="fixed inset-0 z-[100] flex items-center justify-center p-5"
      style={{
        backgroundColor:
          'color-mix(in oklab, var(--color-neutral-950) 55%, transparent)',
        backdropFilter: 'blur(6px)',
        WebkitBackdropFilter: 'blur(6px)',
      }}
    >
      <div
        className="relative w-full max-w-[540px] max-h-[85vh] overflow-y-auto"
        style={{
          backgroundColor: 'var(--color-bg)',
          border: '1px solid var(--color-border)',
          borderRadius: '4px',
          boxShadow:
            '0 12px 40px -8px rgba(2, 6, 23, 0.4), 0 4px 12px -4px rgba(2, 6, 23, 0.2)',
        }}
      >
        {/* 头部 */}
        <div className="relative px-7 pt-6">
          <span
            className="inline-flex items-center gap-2 px-3 py-1 text-xs font-bold tracking-wide"
            style={{
              backgroundColor: 'var(--color-accent-100)',
              color: 'var(--color-accent-700)',
              borderRadius: '2px',
            }}
          >
            <span
              className="inline-block w-1.5 h-1.5 rounded-full"
              style={{ backgroundColor: 'var(--color-accent)' }}
            />
            重要通知
          </span>
          <h2
            id="notice-title"
            className="mt-3 mb-1 pr-9 text-xl font-extrabold tracking-tight"
            style={{ color: 'var(--color-text)' }}
          >
            项目维护调整公告
          </h2>
          <p
            className="m-0 text-xs"
            style={{ color: 'var(--color-text-tertiary)' }}
          >
            2026 年 7 月 24 日 · FANDEX 体系整合通知
          </p>
          <button
            type="button"
            onClick={onClose}
            aria-label="关闭通知"
            className="absolute top-5 right-5 inline-flex items-center justify-center w-8 h-8 transition-colors"
            style={{
              border: '1px solid var(--color-border)',
              borderRadius: '2px',
              backgroundColor: 'var(--color-bg-hover)',
              color: 'var(--color-text-secondary)',
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.color = 'var(--color-text)';
              e.currentTarget.style.borderColor =
                'var(--color-border-strong)';
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.color = 'var(--color-text-secondary)';
              e.currentTarget.style.borderColor = 'var(--color-border)';
            }}
          >
            <svg
              width="14"
              height="14"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2.4"
              strokeLinecap="round"
              strokeLinejoin="round"
              aria-hidden="true"
            >
              <line x1="18" y1="6" x2="6" y2="18" />
              <line x1="6" y1="6" x2="18" y2="18" />
            </svg>
          </button>
        </div>

        {/* 正文 */}
        <div
          className="px-7 pt-4 pb-2 text-sm leading-relaxed"
          style={{ color: 'var(--color-text)' }}
        >
          <p className="m-0 mb-3">尊敬的用户:</p>
          <p className="m-0 mb-3">
            感谢您一直以来对 FANDEX 项目的关注与支持。
          </p>
          <p className="m-0 mb-3">
            为推进 FANDEX 体系的长期演进,我们正在对整体项目进行
            <Highlight>整合与重构</Highlight>
            ,后续将以全新仓库
            <a
              href="https://github.com/fanquanpp/FANDEX"
              target="_blank"
              rel="noreferrer"
              style={{ color: 'var(--color-primary)', textDecoration: 'underline' }}
            >
              fanquanpp/FANDEX
            </a>
            作为唯一维护主体重新发布,预计
            <Highlight>2026 年 8 月下旬</Highlight>
            正式完成。
          </p>
          <p className="m-0 mb-3">
            据此,本仓库内容及站内文档自即日起
            <Highlight>暂停更新</Highlight>
            ,但仍会围绕美术风格、交互体验(UI/UX)等方向持续探索。新仓库正式发布后,本仓库将进入
            <Highlight>只读归档状态</Highlight>
            ,现有源码与历史 Release 仍可自由获取与使用;如需 fork 或二次开发,请遵循
            <Highlight>MIT 许可证</Highlight>
            条款自行处理,作者不再对使用过程中的任何问题提供支持。
          </p>
          <p className="m-0 mb-3">
            敬请留意后续公告,感谢您的理解与支持。
          </p>
          <hr
            className="my-4 border-0"
            style={{
              height: '1px',
              backgroundColor: 'var(--color-border)',
            }}
          />
          <p
            className="m-0 text-xs text-right"
            style={{ color: 'var(--color-text-tertiary)' }}
          >
            <strong style={{ color: 'var(--color-text-secondary)' }}>
              FANDEX 维护者
            </strong>
            <br />
            2026 年 7 月 24 日
          </p>
        </div>

        {/* 底部操作栏 */}
        <div
          className="flex flex-col-reverse sm:flex-row items-stretch sm:items-center justify-end gap-3 px-7 py-5 mt-2"
          style={{ borderTop: '1px solid var(--color-border)' }}
        >
          <span
            className="sm:mr-auto text-xs text-center sm:text-left"
            style={{ color: 'var(--color-text-tertiary)' }}
          >
            关闭后可通过顶部铃铛图标再次查看
          </span>
          <button
            type="button"
            onClick={onClose}
            className="inline-flex items-center justify-center gap-2 px-5 py-2.5 text-sm font-semibold transition-colors"
            style={{
              backgroundColor: 'var(--color-primary)',
              color: 'var(--color-text-inverse)',
              borderRadius: '2px',
              border: '1px solid var(--color-primary)',
            }}
            onMouseEnter={(e) => {
              e.currentTarget.style.backgroundColor =
                'var(--color-primary-600)';
              e.currentTarget.style.borderColor =
                'var(--color-primary-600)';
            }}
            onMouseLeave={(e) => {
              e.currentTarget.style.backgroundColor = 'var(--color-primary)';
              e.currentTarget.style.borderColor = 'var(--color-primary)';
            }}
          >
            我已知晓
          </button>
        </div>
      </div>
    </div>
  );
}

/** 关键信息高亮:Amber 强调色 + 浅色背景 */
function Highlight({ children }: { children: React.ReactNode }) {
  return (
    <span
      style={{
        backgroundColor: 'var(--color-accent-100)',
        color: 'var(--color-accent-700)',
        padding: '1px 5px',
        borderRadius: '2px',
        fontWeight: 600,
      }}
    >
      {children}
    </span>
  );
}
