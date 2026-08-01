/**
 * Playground 首页岛组件
 *
 * 功能概述：
 *   - 展示前端实验与编程练习两个功能入口
 *   - 汇总本地数据：作品数、练习记录、存储用量（全部来自浏览器本地）
 *   - 展示最近作品与最近练习，支持一键打开继续编辑
 *
 * 数据原则：
 *   - 所有数据仅存用户浏览器（IndexedDB/localStorage），不对外分享
 *   - 清空数据操作必须由用户显式确认，程序不做自动清理
 */

import { useCallback, useEffect, useState } from 'react';
import { PgIcon } from './pg-icons';
import { clearAllPlaygroundData, getPlaygroundStats, loadLabRecords, loadPens } from './pg-storage';
import { getExercise } from './exercises';
import type { FrontendPen, LabRecord, PlaygroundStats } from './types';

/** 格式化时间戳 */
function formatTime(ts: number): string {
  const d = new Date(ts);
  const pad = (n: number) => String(n).padStart(2, '0');
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}`;
}

/** 格式化字节数 */
function formatBytes(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
  return `${(bytes / 1024 / 1024).toFixed(1)} MB`;
}

/** Playground 首页组件 */
function PlaygroundHub() {
  /** 本地统计数据 */
  const [stats, setStats] = useState<PlaygroundStats | null>(null);
  /** 最近前端作品 */
  const [pens, setPens] = useState<FrontendPen[]>([]);
  /** 最近练习记录 */
  const [records, setRecords] = useState<LabRecord[]>([]);

  /**
   * 刷新本地统计与最近记录
   */
  const refresh = useCallback(async () => {
    const [nextStats, nextPens, nextRecords] = await Promise.all([
      getPlaygroundStats(),
      loadPens(),
      loadLabRecords(),
    ]);
    setStats(nextStats);
    setPens(nextPens.slice(0, 5));
    setRecords(
      nextRecords
        .slice()
        .sort((a, b) => b.lastRunAt - a.lastRunAt)
        .slice(0, 5),
    );
  }, []);

  useEffect(() => {
    void refresh();
  }, [refresh]);

  /**
   * 用户主动清空全部本地数据（双重确认）
   */
  const handleClearAll = useCallback(async () => {
    if (!window.confirm('清空 Playground 全部本地数据？包括作品库、草稿与练习记录。')) return;
    if (!window.confirm('此操作不可恢复，确定继续？')) return;
    await clearAllPlaygroundData();
    await refresh();
  }, [refresh]);

  /** 存储用量占比（用于进度条） */
  const usageRatio = stats && stats.quotaBytes > 0 ? Math.min(1, stats.usageBytes / stats.quotaBytes) : 0;

  return (
    <div className="pg-hub">
      {/* 顶部介绍 */}
      <section className="pg-hub-hero">
        <span className="pg-hub-kicker">FANDEX PLAYGROUND</span>
        <h1 className="pg-hub-title">在线编程实验场</h1>
        <p className="pg-hub-subtitle">
          两个实验入口：前端效果实验与编程算法练习。所有作品和记录只保存在当前浏览器本地，刷新不丢失。
        </p>
      </section>

      {/* 功能入口卡片 */}
      <section className="pg-hub-cards">
        <a className="pg-hub-card pg-hub-card--frontend" href={`${import.meta.env.BASE_URL}playground/frontend/`}>
          <div className="pg-hub-card-icon">
            <PgIcon name="code" size={26} />
          </div>
          <h2>前端效果实验</h2>
          <p>仿 CodePen 的三栏编辑器：同时编写 HTML、CSS 与 JavaScript，实时预览各种前端效果。</p>
          <ul className="pg-hub-card-features">
            <li>实时预览与自动运行</li>
            <li>内置控制台输出捕获</li>
            <li>左右/上下布局切换</li>
            <li>本地作品库自动保存</li>
          </ul>
          <span className="pg-hub-card-action">
            进入实验
            <PgIcon name="arrow-left" size={14} />
          </span>
        </a>

        <a className="pg-hub-card pg-hub-card--lab" href={`${import.meta.env.BASE_URL}playground/lab/`}>
          <div className="pg-hub-card-icon">
            <PgIcon name="cpu" size={26} />
          </div>
          <h2>编程与算法练习</h2>
          <p>内置经典算法题目，支持 JavaScript、TypeScript、Python、C、C++ 五种语言，浏览器内直接运行测试。</p>
          <ul className="pg-hub-card-features">
            <li>自动用例测试与结果汇总</li>
            <li>五种语言起始模板</li>
            <li>练习记录与通过统计</li>
            <li>代码草稿自动保存</li>
          </ul>
          <span className="pg-hub-card-action">
            进入练习
            <PgIcon name="arrow-left" size={14} />
          </span>
        </a>
      </section>

      {/* 本地数据统计 */}
      <section className="pg-hub-local">
        <div className="pg-hub-section-head">
          <h2>本地数据</h2>
          <span className="pg-hub-section-note">仅保存在当前浏览器，由你自行管理</span>
        </div>
        <div className="pg-hub-stats">
          <div className="pg-stat">
            <span className="pg-stat-num">{stats?.penCount ?? '-'}</span>
            <span className="pg-stat-label">前端作品</span>
          </div>
          <div className="pg-stat">
            <span className="pg-stat-num">{stats?.labCount ?? '-'}</span>
            <span className="pg-stat-label">练习组合</span>
          </div>
          <div className="pg-stat">
            <span className="pg-stat-num">{stats?.solvedCount ?? '-'}</span>
            <span className="pg-stat-label">已通过题目</span>
          </div>
          <div className="pg-stat">
            <span className="pg-stat-num">{stats?.totalAttempts ?? '-'}</span>
            <span className="pg-stat-label">累计运行</span>
          </div>
        </div>

        <div className="pg-hub-storage">
          <div className="pg-hub-storage-head">
            <span>
              <PgIcon name="alert" size={13} />
              浏览器本地存储
            </span>
            <span>
              {stats && stats.quotaBytes > 0
                ? `${formatBytes(stats.usageBytes)} / ${formatBytes(stats.quotaBytes)}`
                : '浏览器未提供配额信息'}
            </span>
          </div>
          <div className="pg-hub-storage-bar" role="progressbar" aria-valuenow={Math.round(usageRatio * 100)} aria-valuemin={0} aria-valuemax={100}>
            <i style={{ width: `${usageRatio * 100}%` }} />
          </div>
          <p className="pg-hub-storage-note">
            自动保存只写入用户代码文本，占用极小。如需释放空间，可删除不需要的作品，或点击下方按钮清空全部本地数据。
          </p>
          <button type="button" className="pg-btn pg-btn--danger" onClick={handleClearAll}>
            <PgIcon name="trash" size={14} />
            清空全部本地数据
          </button>
        </div>
      </section>

      {/* 最近作品与练习 */}
      <section className="pg-hub-recent">
        <div className="pg-hub-recent-col">
          <div className="pg-hub-section-head">
            <h2>最近作品</h2>
          </div>
          {pens.length === 0 ? (
            <p className="pg-hub-empty">暂无保存的前端作品</p>
          ) : (
            <ul className="pg-hub-list">
              {pens.map((pen) => (
                <li key={pen.id}>
                  <a href={`${import.meta.env.BASE_URL}playground/frontend/?pen=${encodeURIComponent(pen.id)}`}>
                    <span className="pg-hub-list-title">{pen.title || '未命名作品'}</span>
                    <span className="pg-hub-list-meta">{formatTime(pen.updatedAt)}</span>
                  </a>
                </li>
              ))}
            </ul>
          )}
        </div>
        <div className="pg-hub-recent-col">
          <div className="pg-hub-section-head">
            <h2>最近练习</h2>
          </div>
          {records.length === 0 ? (
            <p className="pg-hub-empty">暂无练习记录</p>
          ) : (
            <ul className="pg-hub-list">
              {records.map((record) => (
                <li key={record.id}>
                  <a href={`${import.meta.env.BASE_URL}playground/lab/?exercise=${encodeURIComponent(record.exerciseId)}&lang=${encodeURIComponent(record.language)}`}>
                    <span className="pg-hub-list-title">
                      {getExercise(record.exerciseId).title}
                      <em className={`pg-hub-list-status ${record.status === 'solved' ? 'pg-text-ok' : 'pg-text-fail'}`}>
                        {record.status === 'solved' ? '已通过' : '未通过'}
                      </em>
                    </span>
                    <span className="pg-hub-list-meta">{formatTime(record.lastRunAt)}</span>
                  </a>
                </li>
              ))}
            </ul>
          )}
        </div>
      </section>
    </div>
  );
}

export default PlaygroundHub;
