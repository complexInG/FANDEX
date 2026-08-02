/**
 * Playground 首页岛组件
 *
 * 功能概述：
 *   - 展示前端实验与编程练习两个功能入口（紧凑卡片，自绘 SVG 几何装饰）
 *   - 汇总本地数据：作品数、练习记录、存储用量（全部来自浏览器本地）
 *   - 展示最近作品，支持一键打开继续编辑
 *
 * 数据原则：
 *   - 所有数据仅存用户浏览器（IndexedDB/localStorage），不对外分享
 *   - 清空数据操作必须由用户显式确认，程序不做自动清理
 */

import { useCallback, useEffect, useState } from 'react';
import { PgIcon } from './pg-icons';
import { clearAllPlaygroundData, getPlaygroundStats, loadPens } from './pg-storage';
import type { FrontendPen, PlaygroundStats } from './types';

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

/** 卡片右上角几何装饰（自绘 SVG，非位图） */
function CardDecor({ variant }: { variant: 'code' | 'cpu' }) {
  return (
    <svg className="pg-hub-card__decor" viewBox="0 0 120 72" aria-hidden="true">
      {/* 右上角坐标刻度 */}
      <path className="pg-hub-card__decor-bracket" d="M 104 8 H 112 V 16" />
      <path className="pg-hub-card__decor-bracket" d="M 104 64 H 112 V 56" />
      <path className="pg-hub-card__decor-bracket" d="M 8 8 H 16 V 16" />
      <path className="pg-hub-card__decor-bracket" d="M 8 64 H 16 V 56" />
      {variant === 'code' ? (
        <>
          <path className="pg-hub-card__decor-glyph" d="M 70 22 L 58 36 L 70 50" />
          <path className="pg-hub-card__decor-glyph" d="M 82 22 L 94 36 L 82 50" />
          <path className="pg-hub-card__decor-glyph" d="M 74 20 L 78 52" />
        </>
      ) : (
        <>
          <rect className="pg-hub-card__decor-glyph" x="62" y="22" width="28" height="28" />
          <path className="pg-hub-card__decor-glyph" d="M 70 30 h 12 M 70 42 h 12 M 76 26 v 20" />
          <path className="pg-hub-card__decor-glyph" d="M 70 18 V 22 M 82 18 V 22 M 70 50 V 54 M 82 50 V 54" />
        </>
      )}
    </svg>
  );
}

/** Playground 首页组件 */
function PlaygroundHub() {
  /** 本地统计数据 */
  const [stats, setStats] = useState<PlaygroundStats | null>(null);
  /** 最近前端作品 */
  const [pens, setPens] = useState<FrontendPen[]>([]);

  /**
   * 刷新本地统计与最近作品
   */
  const refresh = useCallback(async () => {
    const [nextStats, nextPens] = await Promise.all([getPlaygroundStats(), loadPens()]);
    setStats(nextStats);
    setPens(nextPens.slice(0, 5));
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
      {/* 功能入口卡片：紧凑双卡布局 */}
      <section className="pg-hub-cards">
        <a className="pg-hub-card pg-hub-card--frontend" href={`${import.meta.env.BASE_URL}playground/frontend/`}>
          <CardDecor variant="code" />
          <span className="pg-hub-card__index">01</span>
          <div className="pg-hub-card__head">
            <div className="pg-hub-card-icon">
              <PgIcon name="code" size={22} />
            </div>
            <div className="pg-hub-card__heading">
              <h2>前端效果实验</h2>
              <p className="pg-hub-card__brief">仿 CodePen 的三栏编辑器，HTML / CSS / JavaScript 实时预览</p>
            </div>
          </div>
          <ul className="pg-hub-card-features">
            <li>实时预览与自动运行</li>
            <li>内置控制台输出</li>
            <li>左右 / 上下布局切换</li>
            <li>本地作品库自动保存</li>
          </ul>
          <span className="pg-hub-card-action">
            进入实验
            <PgIcon name="arrow-left" size={13} />
          </span>
        </a>

        <a className="pg-hub-card pg-hub-card--lab" href={`${import.meta.env.BASE_URL}playground/lab/`}>
          <CardDecor variant="cpu" />
          <span className="pg-hub-card__index">02</span>
          <div className="pg-hub-card__head">
            <div className="pg-hub-card-icon">
              <PgIcon name="cpu" size={22} />
            </div>
            <div className="pg-hub-card__heading">
              <h2>编程与算法练习</h2>
              <p className="pg-hub-card__brief">内置经典算法题目，五种语言在浏览器内直接运行测试</p>
            </div>
          </div>
          <ul className="pg-hub-card-features">
            <li>自动用例测试与结果汇总</li>
            <li>五种语言起始模板</li>
            <li>练习记录与通过统计</li>
            <li>代码草稿自动保存</li>
          </ul>
          <span className="pg-hub-card-action">
            进入练习
            <PgIcon name="arrow-left" size={13} />
          </span>
        </a>
      </section>

      {/* 本地数据面板：统计 + 存储用量合并为单个紧凑区域 */}
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
          <div className="pg-hub-storage-main">
            <div className="pg-hub-storage-bar" role="progressbar" aria-valuenow={Math.round(usageRatio * 100)} aria-valuemin={0} aria-valuemax={100}>
              <i style={{ width: `${usageRatio * 100}%` }} />
            </div>
            <button type="button" className="pg-btn pg-btn--danger" onClick={handleClearAll}>
              <PgIcon name="trash" size={14} />
              清空全部本地数据
            </button>
          </div>
          <p className="pg-hub-storage-note">
            自动保存只写入用户代码文本，占用极小。如需释放空间，可删除不需要的作品，或点击上方按钮清空全部本地数据。
          </p>
        </div>
      </section>

      {/* 最近作品 */}
      <section className="pg-hub-recent">
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
      </section>
    </div>
  );
}

export default PlaygroundHub;
