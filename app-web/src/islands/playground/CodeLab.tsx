/**
 * 编程与算法练习实验室
 *
 * 功能概述：
 *   - 内置算法题目目录，支持 JavaScript/TypeScript/Python/C/C++ 五种语言
 *   - 运行时会自动拼接测试脚手架，逐条执行用例并输出 PASS/FAIL 汇总
 *   - 代码草稿与练习记录保存在浏览器 IndexedDB，刷新不丢失
 *
 * 性能设计：
 *   - 编辑器仅保留当前题目的一个实例，切换题目时懒加载对应记录
 *   - Python/C/C++ 首次运行需加载运行时（Pyodide/JSCPP），超时放宽至 20 秒
 *   - 自动保存防抖 800ms，避免高频写入
 */

import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import CodeMirrorBox from './CodeMirrorBox';
import { PgIcon } from './pg-icons';
import { DIFFICULTY_CLASS, EXERCISES, getExercise, getStarter, LAB_LANGUAGES, LAB_LANGUAGE_LABELS } from './exercises';
import { buildHarness, parseRunSummary } from './pg-harness';
import { labDraftKey, loadLabDraft, loadLabRecord, saveLabDraft, saveLabRecord } from './pg-storage';
import { runCode, type CodeLanguage, type RunResult } from '@/services';
import type { LabLanguage, LabRecord } from './types';

/** 自动保存防抖时长（毫秒） */
const AUTOSAVE_MS = 800;
/** JS/TS 运行超时（毫秒） */
const JS_TIMEOUT_MS = 8000;
/** Python/C/C++ 运行超时（毫秒，含首次运行时下载） */
const WASM_TIMEOUT_MS = 20000;

/** 输出区域运行结果状态 */
interface LabOutput {
  /** 运行结果 */
  result: RunResult;
  /** 解析出的用例汇总（无汇总行时为 null） */
  summary: { passed: number; failed: number; total: number } | null;
}

/**
 * 格式化耗时文本
 * @param ms - 毫秒数
 */
function formatDuration(ms: number): string {
  if (ms < 1000) return `${ms} ms`;
  return `${(ms / 1000).toFixed(1)} s`;
}

/** 编程练习实验室主组件 */
function CodeLab() {
  /** 从首页跳转链接解析初始参数（?exercise=&lang=） */
  const initialParams = useMemo(() => {
    if (typeof window === 'undefined') return null;
    return new URLSearchParams(window.location.search);
  }, []);
  /** 当前题目 ID */
  const [exerciseId, setExerciseId] = useState<string>(() => {
    const id = initialParams?.get('exercise');
    return id && EXERCISES.some((e) => e.id === id) ? id : EXERCISES[0]!.id;
  });
  /** 当前语言 */
  const [language, setLanguage] = useState<LabLanguage>(() => {
    const lang = initialParams?.get('lang');
    return lang && (LAB_LANGUAGES as string[]).includes(lang) ? (lang as LabLanguage) : 'javascript';
  });
  /** 编辑器代码 */
  const [code, setCode] = useState<string>('');
  /** 练习记录（来自 IndexedDB） */
  const [record, setRecord] = useState<LabRecord | null>(null);
  /** 是否正在运行 */
  const [running, setRunning] = useState(false);
  /** 运行时加载提示（Pyodide/JSCPP 首次加载） */
  const [loadingMessage, setLoadingMessage] = useState('');
  /** 最近一次运行输出 */
  const [output, setOutput] = useState<LabOutput | null>(null);
  /** 是否展开提示 */
  const [showHints, setShowHints] = useState(false);
  /** 保存状态 */
  const [saveState, setSaveState] = useState<'saved' | 'saving'>('saved');
  /** 题目切换过程中避免旧异步结果覆盖新状态 */
  const loadTokenRef = useRef(0);

  /** 当前题目对象 */
  const exercise = useMemo(() => getExercise(exerciseId), [exerciseId]);

  /**
   * 切换题目或语言时，加载对应记录/草稿/起始模板
   */
  useEffect(() => {
    const token = ++loadTokenRef.current;
    let cancelled = false;
    (async () => {
      const current = getExercise(exerciseId);
      const existing = await loadLabRecord(exerciseId, language);
      if (cancelled || token !== loadTokenRef.current) return;
      setRecord(existing);
      if (existing?.code) {
        setCode(existing.code);
        return;
      }
      const draft = await loadLabDraft(labDraftKey(exerciseId, language));
      if (cancelled || token !== loadTokenRef.current) return;
      setCode(draft ?? getStarter(current, language));
    })();
    return () => {
      cancelled = true;
    };
  }, [exerciseId, language]);

  /**
   * 代码自动保存（防抖）：练习草稿按 题目+语言 独立保存
   */
  useEffect(() => {
    const timer = setTimeout(async () => {
      setSaveState('saving');
      await saveLabDraft(labDraftKey(exerciseId, language), code);
      setSaveState('saved');
    }, AUTOSAVE_MS);
    return () => clearTimeout(timer);
  }, [code, exerciseId, language]);

  /**
   * 运行当前代码：拼接测试脚手架后交给 Worker 执行
   */
  const handleRun = useCallback(async () => {
    if (running || !code.trim()) return;
    setRunning(true);
    setLoadingMessage('');
    setOutput(null);

    const harness = buildHarness(exercise, language);
    const fullCode = `${code}\n${harness}`;
    const timeout = language === 'javascript' || language === 'typescript' ? JS_TIMEOUT_MS : WASM_TIMEOUT_MS;

    try {
      const result = await runCode({
        language: language as CodeLanguage,
        code: fullCode,
        timeout,
      });
      const summary = parseRunSummary(result.stdout);
      const status: LabRecord['status'] = summary && summary.failed === 0 && !result.timedOut ? 'solved' : 'failed';
      const now = Date.now();
      const nextRecord: LabRecord = {
        id: `${exerciseId}:${language}`,
        exerciseId,
        language,
        code,
        status,
        attempts: (record?.attempts ?? 0) + 1,
        solvedCount: (record?.solvedCount ?? 0) + (status === 'solved' ? 1 : 0),
        lastDurationMs: result.durationMs,
        lastPassed: summary?.passed ?? 0,
        lastFailed: summary?.failed ?? (result.exitCode !== 0 || result.timedOut ? 1 : 0),
        lastRunAt: now,
        createdAt: record?.createdAt ?? now,
      };
      setRecord(nextRecord);
      setOutput({ result, summary });
      await saveLabRecord(nextRecord);
      await saveLabDraft(labDraftKey(exerciseId, language), code);
    } catch (err) {
      // runCode 服务层通常 resolve，此处兜底
      setOutput({
        result: {
          stdout: '',
          stderr: err instanceof Error ? err.message : String(err),
          exitCode: 1,
          durationMs: 0,
          timedOut: false,
        },
        summary: null,
      });
    } finally {
      setRunning(false);
      setLoadingMessage('');
    }
  }, [code, exercise, exerciseId, language, record, running]);

  /**
   * 重置为题目起始模板（带确认，避免误触丢失草稿）
   */
  const handleReset = useCallback(() => {
    if (!window.confirm('确定重置为题目模板？当前编辑内容将保留在草稿中，不会被删除。')) return;
    setCode(getStarter(exercise, language));
  }, [exercise, language]);

  /** 运行状态文案 */
  const statusText = useMemo(() => {
    if (running) return loadingMessage || '运行中';
    if (!output) return '尚未运行';
    const { result, summary } = output;
    if (result.timedOut) return `运行超时（超过 ${formatDuration(result.durationMs)}）`;
    if (summary) {
      return summary.failed === 0
        ? `全部通过 ${summary.passed}/${summary.total} · ${formatDuration(result.durationMs)}`
        : `失败 ${summary.failed}/${summary.total} · ${formatDuration(result.durationMs)}`;
    }
    return result.exitCode === 0 ? `运行完成 · ${formatDuration(result.durationMs)}` : '运行出错';
  }, [running, output, loadingMessage]);

  /** 运行状态样式类 */
  const statusClass = useMemo(() => {
    if (running) return 'pg-run-state--running';
    if (!output) return '';
    const { result, summary } = output;
    if (result.timedOut) return 'pg-run-state--timeout';
    if (summary && summary.failed === 0) return 'pg-run-state--ok';
    return 'pg-run-state--fail';
  }, [running, output]);

  return (
    <div className="pg-codelab">
      {/* 顶部工具栏 */}
      <header className="pg-toolbar">
        <a className="pg-back" href={`${import.meta.env.BASE_URL}playground/`} aria-label="返回实验首页">
          <PgIcon name="arrow-left" size={15} />
          <span>练习</span>
        </a>
        <select
          className="pg-select"
          value={exerciseId}
          onChange={(e) => {
            setExerciseId(e.target.value);
            setOutput(null);
            setShowHints(false);
          }}
          aria-label="选择题目"
        >
          {EXERCISES.map((item) => (
            <option key={item.id} value={item.id}>
              {item.title}（{item.difficulty}）
            </option>
          ))}
        </select>
        <div className="pg-toolbar-group pg-lang-switch" role="group" aria-label="选择语言">
          {LAB_LANGUAGES.map((lang) => (
            <button
              key={lang}
              type="button"
              className={`pg-lang-pill ${language === lang ? 'pg-lang-pill--active' : ''}`}
              onClick={() => {
                setLanguage(lang);
                setOutput(null);
              }}
            >
              {LAB_LANGUAGE_LABELS[lang]}
            </button>
          ))}
        </div>
        <div className="pg-toolbar-group">
          <button type="button" className="pg-btn pg-btn--ghost" onClick={handleReset} title="重置为题目模板">
            <PgIcon name="refresh" size={14} />
            <span>重置</span>
          </button>
          <button
            type="button"
            className="pg-btn pg-btn--primary"
            onClick={handleRun}
            disabled={running}
            title="运行并测试"
          >
            <PgIcon name={running ? 'stop' : 'play'} size={14} />
            <span>{running ? '运行中' : '运行'}</span>
          </button>
        </div>
        <span className={`pg-save-state pg-save-state--${saveState}`}>
          {saveState === 'saved' ? '已保存到本地' : '保存中'}
        </span>
      </header>

      {/* 主区域：题目说明 | 编辑器 + 输出 */}
      <div className="pg-lab-main">
        <aside className="pg-lab-desc">
          <div className="pg-lab-desc-head">
            <span className={`pg-badge ${DIFFICULTY_CLASS[exercise.difficulty]}`}>{exercise.difficulty}</span>
            <div className="pg-tags">
              {exercise.tags.map((tag) => (
                <span className="pg-tag" key={tag}>
                  {tag}
                </span>
              ))}
            </div>
          </div>
          <h2 className="pg-lab-title">{exercise.title}</h2>
          <p className="pg-lab-desc-text">{exercise.description}</p>
          <div className="pg-lab-example">
            <div className="pg-lab-example-head">示例</div>
            <pre>{exercise.example}</pre>
          </div>

          <button
            type="button"
            className="pg-hints-toggle"
            onClick={() => setShowHints((v) => !v)}
            aria-expanded={showHints}
          >
            <span>解题提示</span>
            <PgIcon name="chevron-down" size={14} className={showHints ? 'pg-hints-icon--open' : ''} />
          </button>
          {showHints && (
            <ul className="pg-hints">
              {exercise.hints.map((hint, index) => (
                <li key={index}>{hint}</li>
              ))}
            </ul>
          )}

          <div className="pg-record">
            <div className="pg-record-head">
              <PgIcon name="clock" size={13} />
              练习记录
            </div>
            {record ? (
              <dl className="pg-record-grid">
                <div>
                  <dt>状态</dt>
                  <dd className={record.status === 'solved' ? 'pg-text-ok' : 'pg-text-fail'}>
                    {record.status === 'solved' ? '已通过' : '未通过'}
                  </dd>
                </div>
                <div>
                  <dt>尝试</dt>
                  <dd>{record.attempts} 次</dd>
                </div>
                <div>
                  <dt>通过</dt>
                  <dd>{record.solvedCount} 次</dd>
                </div>
                <div>
                  <dt>最近耗时</dt>
                  <dd>{formatDuration(record.lastDurationMs)}</dd>
                </div>
              </dl>
            ) : (
              <p className="pg-record-empty">本题尚未运行过，运行后记录会保存在当前浏览器</p>
            )}
          </div>
        </aside>

        <section className="pg-lab-work">
          <div className="pg-pane">
            <div className="pg-pane-head">
              <span className="pg-pane-title">
                {exercise.functionName}.{language === 'python' ? 'py' : language === 'c' ? 'c' : language === 'cpp' ? 'cpp' : language === 'typescript' ? 'ts' : 'js'}
              </span>
              <span className="pg-pane-note">测试用例会自动追加在代码末尾</span>
            </div>
            <div className="pg-pane-body">
              <CodeMirrorBox
                value={code}
                onChange={setCode}
                language={language === 'typescript' ? 'typescript' : language === 'python' ? 'python' : language === 'c' || language === 'cpp' ? 'cpp' : 'javascript'}
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
                  退出码 {output.result.exitCode} · 用例 {output.summary ? `${output.summary.passed + output.summary.failed}/${output.summary.total}` : '-'}
                </span>
              )}
            </div>
            <div className="pg-run-body">
              {!output && !running && <div className="pg-run-empty">点击「运行」开始测试</div>}
              {output && output.result.stdout.length > 0 && (
                <pre className="pg-run-stdout">{output.result.stdout}</pre>
              )}
              {output && output.result.stderr.length > 0 && (
                <pre className="pg-run-stderr">{output.result.stderr}</pre>
              )}
              {output && output.result.stdout.length === 0 && output.result.stderr.length === 0 && (
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
