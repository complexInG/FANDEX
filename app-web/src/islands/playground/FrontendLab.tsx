/**
 * 前端实验沙箱（CodePen 风格编辑器）
 *
 * 功能概述：
 *   - 三栏编辑器（HTML/CSS/JS）+ 实时预览 iframe + 控制台面板
 *   - 支持顶部/左右两种布局、面板显隐切换、拖拽调整预览区比例
 *   - 编辑内容自动保存到浏览器 IndexedDB，刷新不丢失
 *   - 本地作品库：另存为新作品、打开历史作品、删除作品
 *
 * 安全与性能：
 *   - 预览 iframe 使用 sandbox 隔离，用户代码运行在独立不透明源
 *   - 自动运行采用防抖（600ms），避免每次按键都重建 iframe
 *   - 控制台日志上限 200 条，防止长期运行撑爆内存
 *   - 所有数据仅存本地，不提供分享/上传/导出功能
 */

import {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
  type CSSProperties,
  type PointerEvent as ReactPointerEvent,
} from 'react';
import CodeMirrorBox from './CodeMirrorBox';
import { PgIcon } from './pg-icons';
import { buildPreviewDoc, estimatePenBytes, parsePreviewMessage } from './pg-frontend-runtime';
import {
  deletePen,
  getStorageUsage,
  loadPenDraft,
  loadPens,
  savePen,
  savePenDraft,
} from './pg-storage';
import type { ConsoleEntry, FrontendPen } from './types';

/** 默认草稿模板 */
const DEFAULT_TEMPLATE: FrontendPen = {
  id: 'draft',
  title: '未命名作品',
  html: '<h1>你好，FANDEX</h1>\n<button id="demo">点我</button>\n<p id="tip">打开控制台查看输出</p>',
  css: 'body {\n  font-family: var(--font-body, sans-serif);\n  text-align: center;\n  padding: 40px 16px;\n}\nbutton {\n  padding: 8px 20px;\n  border-radius: 8px;\n  border: 1px solid #0B6E7E;\n  background: #E6FBFC;\n  color: #0B6E7E;\n  cursor: pointer;\n}',
  js: "const tip = document.getElementById('tip');\nconst btn = document.getElementById('demo');\nbtn.addEventListener('click', () => {\n  tip.textContent = '点击次数 +1';\n  console.log('按钮被点击');\n});\nconsole.log('预览已就绪');",
  autoRun: true,
  layout: 'left',
  showHtml: true,
  showCss: true,
  showJs: true,
  showConsole: true,
  createdAt: 0,
  updatedAt: 0,
  lastOpenedAt: 0,
};

/** 编辑器区域占预览区的比例范围 */
const SPLIT_MIN = 0.2;
const SPLIT_MAX = 0.8;
/** 自动保存防抖时长（毫秒） */
const AUTOSAVE_MS = 800;
/** 自动运行防抖时长（毫秒） */
const AUTORUN_MS = 600;
/** 控制台日志条数上限 */
const CONSOLE_LIMIT = 200;
/** 存储用量预警阈值（占比） */
const STORAGE_WARN_RATIO = 0.85;

/** 保存状态文案 */
type SaveState = 'saved' | 'saving';

/**
 * 格式化时间戳为本地时间字符串
 * @param ts - 时间戳（毫秒）
 */
function formatTime(ts: number): string {
  if (!ts) return '未保存';
  const d = new Date(ts);
  const pad = (n: number) => String(n).padStart(2, '0');
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}`;
}

/**
 * 格式化字节数为可读文本
 * @param bytes - 字节数
 */
function formatBytes(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
  return `${(bytes / 1024 / 1024).toFixed(1)} MB`;
}

/** 前端实验沙箱主组件 */
function FrontendLab() {
  /** 当前编辑中的作品 */
  const [pen, setPen] = useState<FrontendPen>(DEFAULT_TEMPLATE);
  /** 自动保存状态 */
  const [saveState, setSaveState] = useState<SaveState>('saved');
  /** 预览文档（srcdoc 内容） */
  const [previewDoc, setPreviewDoc] = useState<string>(() => buildPreviewDoc(DEFAULT_TEMPLATE));
  /** 手动运行计数（作为 iframe key 强制刷新） */
  const [runId, setRunId] = useState(0);
  /** 控制台日志 */
  const [consoleEntries, setConsoleEntries] = useState<ConsoleEntry[]>([]);
  /** 是否打开作品库面板 */
  const [showLibrary, setShowLibrary] = useState(false);
  /** 作品库列表 */
  const [library, setLibrary] = useState<FrontendPen[]>([]);
  /** 编辑器区域占比（0-1） */
  const [split, setSplit] = useState(0.5);
  /** 是否正在拖拽分隔条 */
  const [dragging, setDragging] = useState(false);
  /** 存储用量提示 */
  const [storageWarning, setStorageWarning] = useState<string>('');
  /** 当前作品字节数（用于本地占用提示） */
  const [penBytes, setPenBytes] = useState(0);
  /** iframe 引用（用于控制台消息来源校验） */
  const iframeRef = useRef<HTMLIFrameElement | null>(null);
  /** 拖拽起始信息 */
  const dragRef = useRef<{ start: number; value: number } | null>(null);

  /**
   * 挂载时读取本地草稿与存储用量
   */
  useEffect(() => {
    let cancelled = false;
    (async () => {
      // 优先打开首页跳转指定的作品（?pen=ID），否则恢复草稿
      const penId = new URLSearchParams(window.location.search).get('pen');
      let target: FrontendPen | null = null;
      if (penId) {
        const pens = await loadPens();
        target = pens.find((p) => p.id === penId) ?? null;
      }
      if (!target) {
        target = await loadPenDraft();
      }
      if (!cancelled && target) {
        const opened = { ...target, lastOpenedAt: target.lastOpenedAt || Date.now() };
        setPen(opened);
        setPreviewDoc(buildPreviewDoc(opened));
      }
      setLibrary(await loadPens());
      const usage = await getStorageUsage();
      if (!cancelled && usage.quotaBytes > 0 && usage.usageBytes / usage.quotaBytes > STORAGE_WARN_RATIO) {
        setStorageWarning(
          `本地存储已使用 ${formatBytes(usage.usageBytes)} / ${formatBytes(usage.quotaBytes)}，建议整理作品库`,
        );
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);

  /**
   * 同步当前作品字节估算（用于本地占用提示）
   */
  useEffect(() => {
    setPenBytes(estimatePenBytes(pen));
  }, [pen]);

  /**
   * 自动保存（防抖）：草稿与作品库记录都实时落盘
   */
  useEffect(() => {
    const timer = setTimeout(async () => {
      setSaveState('saving');
      const now = Date.now();
      const payload: FrontendPen = {
        ...pen,
        updatedAt: now,
        lastOpenedAt: pen.lastOpenedAt || now,
      };
      if (pen.id === 'draft') {
        await savePenDraft(payload);
      } else {
        await savePen(payload);
      }
      setSaveState('saved');
    }, AUTOSAVE_MS);
    return () => clearTimeout(timer);
  }, [pen]);

  /**
   * 自动运行（防抖）：内容变化后延迟重建预览
   */
  useEffect(() => {
    if (!pen.autoRun) return;
    const timer = setTimeout(() => {
      setPreviewDoc(buildPreviewDoc(pen));
      setRunId((n) => n + 1);
    }, AUTORUN_MS);
    return () => clearTimeout(timer);
  }, [pen.html, pen.css, pen.js, pen.autoRun]);

  /**
   * 监听预览 iframe 回传的控制台消息
   */
  useEffect(() => {
    const onMessage = (e: MessageEvent) => {
      const entry = parsePreviewMessage(e, iframeRef.current?.contentWindow ?? null);
      if (!entry) return;
      setConsoleEntries((prev) => [...prev.slice(-(CONSOLE_LIMIT - 1)), entry]);
    };
    window.addEventListener('message', onMessage);
    return () => window.removeEventListener('message', onMessage);
  }, []);

  /**
   * 更新作品内容的通用入口
   * 字节估算由上方独立 effect 随 pen 变化同步，无需在此处重复计算
   */
  const updatePen = useCallback((patch: Partial<FrontendPen>) => {
    setPen((prev) => ({ ...prev, ...patch }));
  }, []);

  /**
   * 手动运行：立即重建预览并强制刷新 iframe
   */
  const handleRun = useCallback(() => {
    setPreviewDoc(buildPreviewDoc(pen));
    setRunId((n) => n + 1);
  }, [pen]);

  /**
   * 将当前作品另存为新作品（复制到作品库）
   */
  const handleSaveAsNew = useCallback(async () => {
    const now = Date.now();
    const newId =
      typeof crypto !== 'undefined' && typeof crypto.randomUUID === 'function'
        ? crypto.randomUUID()
        : `pen-${now}-${Math.random().toString(36).slice(2, 10)}`;
    const newPen: FrontendPen = {
      ...pen,
      id: newId,
      title: pen.title.trim() || '未命名作品',
      createdAt: now,
      updatedAt: now,
      lastOpenedAt: now,
    };
    await savePen(newPen);
    setPen(newPen);
    setSaveState('saved');
  }, [pen]);

  /**
   * 新建空白草稿（会覆盖当前未另存的编辑内容，需用户确认）
   */
  const handleNewDraft = useCallback(() => {
    const isTemplate =
      pen.html === DEFAULT_TEMPLATE.html && pen.css === DEFAULT_TEMPLATE.css && pen.js === DEFAULT_TEMPLATE.js;
    const needsConfirm =
      pen.id !== 'draft'
        ? '当前正在编辑作品库中的作品，新建草稿不会影响已保存的作品，是否继续？'
        : !isTemplate
          ? '当前草稿尚未另存为作品，新建会覆盖草稿内容，是否继续？'
          : '';
    if (needsConfirm && !window.confirm(needsConfirm)) return;
    setPen({ ...DEFAULT_TEMPLATE, lastOpenedAt: Date.now() });
    setPreviewDoc(buildPreviewDoc(DEFAULT_TEMPLATE));
    setRunId((n) => n + 1);
    setConsoleEntries([]);
  }, [pen]);

  /**
   * 打开作品库面板并刷新列表
   */
  const handleOpenLibrary = useCallback(async () => {
    setLibrary(await loadPens());
    setShowLibrary(true);
  }, []);

  /**
   * 打开作品库中的某条作品
   */
  const handleOpenPen = useCallback(
    async (item: FrontendPen) => {
      const now = Date.now();
      const opened = { ...item, lastOpenedAt: now };
      await savePen(opened);
      setPen(opened);
      setPreviewDoc(buildPreviewDoc(opened));
      setRunId((n) => n + 1);
      setConsoleEntries([]);
      setShowLibrary(false);
    },
    [],
  );

  /**
   * 删除作品库中的一条作品（用户主动操作，带确认）
   */
  const handleDeletePen = useCallback(async (item: FrontendPen) => {
    if (!window.confirm(`确定删除作品「${item.title}」？删除后无法恢复。`)) return;
    await deletePen(item.id);
    setLibrary(await loadPens());
  }, []);

  /**
   * 开始拖拽分隔条
   */
  const handleSplitStart = useCallback(
    (e: ReactPointerEvent<HTMLDivElement>) => {
      e.preventDefault();
      // 捕获指针，保证拖拽移出分隔条后仍能持续更新比例
      e.currentTarget.setPointerCapture(e.pointerId);
      dragRef.current = {
        start: pen.layout === 'left' ? e.clientX : e.clientY,
        value: split,
      };
      setDragging(true);
    },
    [pen.layout, split],
  );

  /**
   * 拖拽过程中更新分隔比例
   */
  const handleSplitMove = useCallback(
    (e: ReactPointerEvent<HTMLDivElement>) => {
      if (!dragRef.current) return;
      const total = pen.layout === 'left' ? window.innerWidth : window.innerHeight;
      const delta = (pen.layout === 'left' ? e.clientX : e.clientY) - dragRef.current.start;
      const next = Math.min(SPLIT_MAX, Math.max(SPLIT_MIN, dragRef.current.value + delta / total));
      setSplit(next);
    },
    [pen.layout],
  );

  /**
   * 结束拖拽
   */
  const handleSplitEnd = useCallback(() => {
    dragRef.current = null;
    setDragging(false);
  }, []);

  /** 编辑器区域网格模板（按布局方向生成） */
  const workspaceStyle = useMemo<CSSProperties>(() => {
    const ratio = `${split * 100}%`;
    return pen.layout === 'left'
      ? { gridTemplateColumns: `${ratio} 6px 1fr`, gridTemplateRows: '100%' }
      : { gridTemplateColumns: '100%', gridTemplateRows: `${ratio} 6px 1fr` };
  }, [pen.layout, split]);

  /** 当前打开的编辑器语言映射 */
  const editors = useMemo(
    () =>
      [
        { key: 'html', label: 'HTML', visible: pen.showHtml },
        { key: 'css', label: 'CSS', visible: pen.showCss },
        { key: 'js', label: 'JS', visible: pen.showJs },
      ] as const,
    [pen.showHtml, pen.showCss, pen.showJs],
  );

  return (
    <div className={`pg-frontend ${dragging ? 'pg-dragging' : ''}`}>
      {/* 顶部工具栏 */}
      <header className="pg-toolbar">
        <a className="pg-back" href={`${import.meta.env.BASE_URL}playground/`} aria-label="返回实验首页">
          <PgIcon name="arrow-left" size={15} />
          <span>实验</span>
        </a>
        <input
          className="pg-title-input"
          value={pen.title}
          placeholder="作品标题"
          onChange={(e) => updatePen({ title: e.target.value })}
          aria-label="作品标题"
        />
        <div className="pg-toolbar-group">
          <button
            type="button"
            className="pg-btn pg-btn--ghost"
            onClick={() => updatePen({ autoRun: !pen.autoRun })}
            aria-pressed={pen.autoRun}
            title="自动运行预览"
          >
            <PgIcon name="refresh" size={14} />
            <span>自动</span>
          </button>
          <button
            type="button"
            className="pg-btn pg-btn--ghost"
            onClick={() => updatePen({ layout: pen.layout === 'left' ? 'top' : 'left' })}
            title="切换编辑区布局"
          >
            <PgIcon name={pen.layout === 'left' ? 'layout-left' : 'layout-top'} size={14} />
            <span>{pen.layout === 'left' ? '左右' : '上下'}</span>
          </button>
          <button
            type="button"
            className="pg-btn pg-btn--ghost"
            onClick={() => updatePen({ showConsole: !pen.showConsole })}
            aria-pressed={pen.showConsole}
            title="控制台"
          >
            <PgIcon name="terminal" size={14} />
            <span>控制台</span>
          </button>
        </div>
        <div className="pg-toolbar-group">
          <button type="button" className="pg-btn pg-btn--ghost" onClick={handleNewDraft} title="新建草稿">
            <PgIcon name="plus" size={14} />
            <span>新建</span>
          </button>
          <button type="button" className="pg-btn pg-btn--ghost" onClick={handleSaveAsNew} title="另存为新作品">
            <PgIcon name="copy" size={14} />
            <span>另存</span>
          </button>
          <button type="button" className="pg-btn pg-btn--ghost pg-btn--library" onClick={handleOpenLibrary} title="本地作品库">
            <PgIcon name="folder" size={14} />
            <span>作品库</span>
            {library.length > 0 && <em className="pg-count">{library.length}</em>}
          </button>
          <button type="button" className="pg-btn pg-btn--primary" onClick={handleRun} title="运行">
            <PgIcon name="play" size={14} />
            <span>运行</span>
          </button>
        </div>
        <span className={`pg-save-state pg-save-state--${saveState}`}>
          {saveState === 'saved' ? '已保存到本地' : '保存中'}
        </span>
      </header>

      {/* 存储用量预警 */}
      {storageWarning && (
        <div className="pg-warning-bar">
          <PgIcon name="alert" size={14} />
          <span>{storageWarning}</span>
        </div>
      )}

      {/* 主工作区 */}
      <div className="pg-workspace" style={workspaceStyle}>
        {/* 编辑器区域 */}
        <section className="pg-editors" aria-label="代码编辑器">
          {editors.map((editor) => {
            if (!editor.visible) return null;
            const value = editor.key === 'html' ? pen.html : editor.key === 'css' ? pen.css : pen.js;
            const language = editor.key === 'html' ? 'html' : editor.key === 'css' ? 'css' : 'javascript';
            return (
              <div className="pg-pane" key={editor.key}>
                <div className="pg-pane-head">
                  <span className="pg-pane-title">{editor.label}</span>
                  <button
                    type="button"
                    className="pg-pane-toggle"
                    onClick={() =>
                      updatePen(
                        editor.key === 'html'
                          ? { showHtml: false }
                          : editor.key === 'css'
                            ? { showCss: false }
                            : { showJs: false },
                      )
                    }
                    title={`收起 ${editor.label}`}
                  >
                    <PgIcon name="close" size={12} />
                  </button>
                </div>
                <div className="pg-pane-body">
                  <CodeMirrorBox
                    value={value}
                    language={language as 'html' | 'css' | 'javascript'}
                    onChange={(next) =>
                      updatePen(editor.key === 'html' ? { html: next } : editor.key === 'css' ? { css: next } : { js: next })
                    }
                    ariaLabel={`${editor.label} 编辑器`}
                  />
                </div>
              </div>
            );
          })}
          {!pen.showHtml && !pen.showCss && !pen.showJs && (
            <div className="pg-pane-empty">全部编辑器已收起，请从工具栏打开</div>
          )}
        </section>

        {/* 分隔条 */}
        <div
          className={`pg-splitter pg-splitter--${pen.layout}`}
          onPointerDown={handleSplitStart}
          onPointerMove={handleSplitMove}
          onPointerUp={handleSplitEnd}
          onPointerCancel={handleSplitEnd}
          role="separator"
          aria-orientation={pen.layout === 'left' ? 'vertical' : 'horizontal'}
          aria-label="调整编辑区与预览区比例"
        />

        {/* 预览区域 */}
        <section className="pg-preview">
          <div className="pg-preview-head">
            <span className="pg-preview-title">
              <PgIcon name="spark" size={13} />
              实时预览
            </span>
            <div className="pg-preview-actions">
              <span className="pg-preview-size">{formatBytes(penBytes)}</span>
              <button
                type="button"
                className="pg-btn pg-btn--ghost pg-btn--sm"
                onClick={handleRun}
                title="重新运行预览"
              >
                <PgIcon name="refresh" size={12} />
              </button>
            </div>
          </div>
          <iframe
            ref={iframeRef}
            key={runId}
            className="pg-frame"
            sandbox="allow-scripts allow-modals allow-forms allow-popups allow-pointer-lock"
            srcDoc={previewDoc}
            title="前端效果预览"
          />
          {pen.showConsole && (
            <div className="pg-console">
              <div className="pg-console-head">
                <span className="pg-console-title">
                  <PgIcon name="terminal" size={12} />
                  控制台
                </span>
                <div className="pg-console-actions">
                  {consoleEntries.length > 0 && (
                    <button
                      type="button"
                      className="pg-btn pg-btn--ghost pg-btn--sm"
                      onClick={() => setConsoleEntries([])}
                    >
                      清空
                    </button>
                  )}
                  <button
                    type="button"
                    className="pg-btn pg-btn--ghost pg-btn--sm"
                    onClick={() => updatePen({ showConsole: false })}
                    title="收起控制台"
                  >
                    <PgIcon name="close" size={12} />
                  </button>
                </div>
              </div>
              <div className="pg-console-body">
                {consoleEntries.length === 0 ? (
                  <div className="pg-console-empty">暂无输出，运行预览后 console 内容会显示在这里</div>
                ) : (
                  consoleEntries.map((entry, index) => (
                    <div className={`pg-console-line pg-console-line--${entry.kind}`} key={`${entry.time}-${index}`}>
                      <span className="pg-console-kind">{entry.kind}</span>
                      <pre className="pg-console-text">{entry.text}</pre>
                    </div>
                  ))
                )}
              </div>
            </div>
          )}
        </section>
      </div>

      {/* 本地作品库面板 */}
      {showLibrary && (
        <div className="pg-drawer-mask" onClick={() => setShowLibrary(false)}>
          <aside className="pg-drawer" onClick={(e) => e.stopPropagation()}>
            <div className="pg-drawer-head">
              <span className="pg-drawer-title">
                <PgIcon name="folder" size={15} />
                本地作品库
              </span>
              <button type="button" className="pg-btn pg-btn--ghost pg-btn--sm" onClick={() => setShowLibrary(false)}>
                <PgIcon name="close" size={14} />
              </button>
            </div>
            <div className="pg-drawer-body">
              {library.length === 0 ? (
                <div className="pg-drawer-empty">
                  暂无保存的作品。编辑完成后点击「另存」即可保存在当前浏览器。
                </div>
              ) : (
                library.map((item) => (
                  <div className={`pg-lib-item ${item.id === pen.id ? 'pg-lib-item--active' : ''}`} key={item.id}>
                    <div className="pg-lib-info">
                      <span className="pg-lib-title">{item.title || '未命名作品'}</span>
                      <span className="pg-lib-meta">
                        {formatTime(item.updatedAt)} · {formatBytes(estimatePenBytes(item))}
                      </span>
                    </div>
                    <div className="pg-lib-actions">
                      <button type="button" className="pg-btn pg-btn--ghost pg-btn--sm" onClick={() => handleOpenPen(item)}>
                        打开
                      </button>
                      <button
                        type="button"
                        className="pg-btn pg-btn--ghost pg-btn--sm pg-btn--danger"
                        onClick={() => handleDeletePen(item)}
                      >
                        删除
                      </button>
                    </div>
                  </div>
                ))
              )}
            </div>
          </aside>
        </div>
      )}
    </div>
  );
}

export default FrontendLab;
