/**
 * 在线编程沙箱（自由编辑 + 多语言运行）
 *
 * 功能概述：
 *   - 面向"用户自己写代码练习"的轻量在线编辑器，非答题/问答区
 *   - 支持站点全部主流语言编辑与语法高亮（JS/TS/Python/C/C++/Go/Java/Kotlin/
 *     Rust/C#/Lua/SQL/Shell）
 *   - JS/TS/Python/C/C++/Lua 可在浏览器沙箱内直接运行，其余语言如实提示本地运行
 *   - 代码草稿按语言自动保存到浏览器 IndexedDB，刷新不丢失
 *
 * 性能设计：
 *   - 编辑器仅保留当前语言的一个实例，切换语言时懒加载对应草稿
 *   - Python/C/C++/Lua 首次运行需加载运行时（Pyodide/JSCPP/Fengari），超时放宽
 *   - 自动保存防抖 800ms，避免高频写入
 */

import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import CodeMirrorBox from './CodeMirrorBox';
import { PgIcon } from './pg-icons';
import { formatCode } from './pg-formatter';
import {
  getStarter,
  getUnsupportedRunMessage,
  LAB_LANGUAGE_EXT,
  LAB_LANGUAGE_LABELS,
  LAB_LANGUAGES,
  LAB_LANGUAGE_RUNNABLE,
  toEditorLanguage,
} from './languages';
import { loadLabDraft, saveLabDraft } from './pg-storage';
import { runCode, type CodeLanguage, type RunResult } from '@/services/code-runner-service';
import type { LabLanguage } from './types';

/** 自动保存防抖时长（毫秒） */
const AUTOSAVE_MS = 800;
/** JS/TS 运行超时（毫秒） */
const JS_TIMEOUT_MS = 8000;
/** Python/C/C++/Lua 运行超时（毫秒，含首次运行时下载） */
const WASM_TIMEOUT_MS = 20000;

/** 草稿 key 前缀（按语言独立保存） */
function draftKey(language: LabLanguage): string {
  return `lab:${language}`;
}

/**
 * 格式化耗时文本
 * @param ms - 毫秒数
 */
function formatDuration(ms: number): string {
  if (ms < 1000) return `${ms} ms`;
  return `${(ms / 1000).toFixed(1)} s`;
}

/** 在线编程沙箱主组件 */
function CodeLab() {
  /** 从首页跳转链接解析初始语言（?lang=） */
  const initialParams = useMemo(() => {
    if (typeof window === 'undefined') return null;
    return new URLSearchParams(window.location.search);
  }, []);
  /** 当前语言 */
  const [language, setLanguage] = useState<LabLanguage>(() => {
    const lang = initialParams?.get('lang');
    return lang && (LAB_LANGUAGES as readonly string[]).includes(lang)
      ? (lang as LabLanguage)
      : 'javascript';
  });
  /** 编辑器代码 */
  const [code, setCode] = useState<string>('');
  /** 是否正在运行 */
  const [running, setRunning] = useState(false);
  /** 运行时加载提示（Pyodide/JSCPP/Fengari 首次加载） */
  const [loadingMessage, setLoadingMessage] = useState('');
  /** 最近一次运行输出 */
  const [output, setOutput] = useState<RunResult | null>(null);
  /** 是否正在格式化 */
  const [formatting, setFormatting] = useState(false);
  /** 格式化/运行提示信息 */
  const [notice, setNotice] = useState('');
  /** 保存状态 */
  const [saveState, setSaveState] = useState<'saved' | 'saving'>('saved');
  /** 语言切换过程中避免旧异步结果覆盖新状态 */
  const loadTokenRef = useRef(0);

  /**
   * 切换语言时加载对应草稿（无草稿时使用起始模板）
   */
  useEffect(() => {
    const token = ++loadTokenRef.current;
    let cancelled = false;
    (async () => {
      const draft = await loadLabDraft(draftKey(language));
      if (cancelled || token !== loadTokenRef.current) return;
      setCode(draft ?? getStarter(language));
      setOutput(null);
      setNotice('');
    })();
    return () => {
      cancelled = true;
    };
  }, [language]);

  /**
   * 代码自动保存（防抖）：按语言独立保存草稿
   */
  useEffect(() => {
    const timer = setTimeout(async () => {
      setSaveState('saving');
      await saveLabDraft(draftKey(language), code);
      setSaveState('saved');
    }, AUTOSAVE_MS);
    return () => clearTimeout(timer);
  }, [code, language]);

  /**
   * 运行当前代码
   * - 支持运行的语言直接交给 Worker 沙箱
   * - 不支持运行的语言给出本地工具链提示
   */
  const handleRun = useCallback(async () => {
    if (running || !code.trim()) return;
    if (!LAB_LANGUAGE_RUNNABLE[language]) {
      setOutput({
        stdout: '',
        stderr: getUnsupportedRunMessage(language),
        exitCode: 1,
        durationMs: 0,
        timedOut: false,
      });
      return;
    }
    setRunning(true);
    setLoadingMessage('');
    setOutput(null);
    setNotice('');

    const timeout =
      language === 'javascript' || language === 'typescript'
        ? JS_TIMEOUT_MS
        : WASM_TIMEOUT_MS;

    try {
      const result = await runCode({
        language: language as CodeLanguage,
        code,
        timeout,
      });
      setOutput(result);
    } catch (err) {
      // runCode 服务层通常 resolve，此处兜底
      setOutput({
        stdout: '',
        stderr: err instanceof Error ? err.message : String(err),
        exitCode: 1,
        durationMs: 0,
        timedOut: false,
      });
    } finally {
      setRunning(false);
      setLoadingMessage('');
    }
  }, [code, language, running]);

  /**
   * 格式化当前代码（支持 JS/TS/Python/HTML/CSS；其余语言提示不支持）
   */
  const handleFormat = useCallback(async () => {
    if (formatting || !code.trim()) return;
    setFormatting(true);
    setNotice('');
    const result = await formatCode(language, code);
    if (result.code !== code) {
      setCode(result.code);
    }
    if (result.note) {
      setNotice(result.note);
    }
    setFormatting(false);
  }, [code, formatting, language]);

  /**
   * 重置为语言起始模板（带确认，避免误触丢失草稿）
   */
  const handleReset = useCallback(() => {
    if (!window.confirm('确定重置为起始模板？当前编辑内容将保留在草稿中，不会被删除。')) return;
    setCode(getStarter(language));
  }, [language]);

  /** 运行状态文案 */
  const statusText = useMemo(() => {
    if (running) return loadingMessage || '运行中';
    if (!output) return '尚未运行';
    if (output.timedOut) return `运行超时（超过 ${formatDuration(output.durationMs)}）`;
    return output.exitCode === 0
      ? `运行完成 · ${formatDuration(output.durationMs)}`
      : '运行出错';
  }, [running, output, loadingMessage]);

  /** 运行状态样式类 */
  const statusClass = useMemo(() => {
    if (running) return 'pg-run-state--running';
    if (!output) return '';
    if (output.timedOut) return 'pg-run-state--timeout';
    return output.exitCode === 0 ? 'pg-run-state--ok' : 'pg-run-state--fail';
  }, [running, output]);

  return (
    <div className="pg-codelab">
      {/* 顶部工具栏：返回 + 语言切换 + 操作按钮 */}
      <header className="pg-toolbar">
        <a className="pg-back" href={`${import.meta.env.BASE_URL}playground/`} aria-label="返回实验首页">
          <PgIcon name="arrow-left" size={15} />
          <span>编程</span>
        </a>
        <div className="pg-toolbar-group pg-lang-switch" role="group" aria-label="选择语言">
          {LAB_LANGUAGES.map((lang) => (
            <button
              key={lang}
              type="button"
              className={`pg-lang-pill ${language === lang ? 'pg-lang-pill--active' : ''}`}
              onClick={() => setLanguage(lang)}
              title={LAB_LANGUAGE_RUNNABLE[lang] ? '浏览器内可直接运行' : '编辑模式，运行需本地工具链'}
            >
              {LAB_LANGUAGE_LABELS[lang]}
            </button>
          ))}
        </div>
        <div className="pg-toolbar-group">
          <button
            type="button"
            className="pg-btn pg-btn--ghost"
            onClick={() => void handleFormat()}
            disabled={formatting}
            title="格式化代码（JS/TS/Python）"
          >
            <PgIcon name="spark" size={14} />
            <span>{formatting ? '格式化中' : '格式化'}</span>
          </button>
          <button type="button" className="pg-btn pg-btn--ghost" onClick={handleReset} title="重置为起始模板">
            <PgIcon name="refresh" size={14} />
            <span>重置</span>
          </button>
          <button
            type="button"
            className="pg-btn pg-btn--primary"
            onClick={() => void handleRun()}
            disabled={running}
            title="运行代码"
          >
            <PgIcon name={running ? 'stop' : 'play'} size={14} />
            <span>{running ? '运行中' : '运行'}</span>
          </button>
        </div>
        <span className={`pg-save-state pg-save-state--${saveState}`}>
          {saveState === 'saved' ? '已保存到本地' : '保存中'}
        </span>
      </header>

      {/* 主区域：编辑器 + 输出面板 */}
      <div className="pg-lab-main">
        <section className="pg-lab-work">
          <div className="pg-pane">
            <div className="pg-pane-head">
              <span className="pg-pane-title">
                main.{LAB_LANGUAGE_EXT[language]}
              </span>
              <span className="pg-pane-note">
                {LAB_LANGUAGE_RUNNABLE[language] ? '浏览器沙箱可直接运行' : '编辑模式 · 本地工具链运行'}
              </span>
            </div>
            <div className="pg-pane-body">
              <CodeMirrorBox
                value={code}
                onChange={setCode}
                language={toEditorLanguage(language)}
                ariaLabel={`${LAB_LANGUAGE_LABELS[language]} 代码编辑器`}
              />
            </div>
          </div>

          <div className="pg-run-panel">
            <div className="pg-run-head">
              <span className={`pg-run-state ${statusClass}`}>
                <PgIcon name={running ? 'clock' : 'terminal'} size={12} />
                {statusText}
              </span>
              {output && (
                <span className="pg-run-meta">
                  退出码 {output.exitCode} · {formatDuration(output.durationMs)}
                </span>
              )}
            </div>
            <div className="pg-run-body">
              {notice && <pre className="pg-run-notice">{notice}</pre>}
              {!output && !running && <div className="pg-run-empty">点击「运行」执行当前代码</div>}
              {output && output.stdout.length > 0 && (
                <pre className="pg-run-stdout">{output.stdout}</pre>
              )}
              {output && output.stderr.length > 0 && (
                <pre className="pg-run-stderr">{output.stderr}</pre>
              )}
              {output && output.stdout.length === 0 && output.stderr.length === 0 && (
                <div className="pg-run-empty">无输出</div>
              )}
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}

export default CodeLab;
