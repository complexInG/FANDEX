/**
 * 背景装饰预览服务器
 * ==================
 * 独立运行的 HTTP 服务器，用于预览 GeoBgDecor 组件的所有变体。
 * 不依赖 Astro 构建流程，直接读取源 CSS 文件并内联到 HTML 中。
 *
 * 功能：
 * - 渲染全部 7 个变体（home/docs/list/minimal/loading/error/info）
 * - 支持亮色/暗色主题实时切换
 * - 每个变体在独立卡片中展示，配有标题和装饰元素列表
 * - 端口 3001，与 dev 服务器（3000）隔离
 *
 * 启动方式：node scripts/bg-decor-preview.mjs
 * 访问地址：http://localhost:3001
 *
 * 设计原则：
 * - 零依赖：仅使用 Node.js 内置模块（http/fs/path/url）
 * - 零构建：直接读取源 CSS 文件，无需预编译
 * - 独立运行：不影响主项目的 dev/build 流程
 */

import { createServer } from 'node:http';
import { readFileSync, existsSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const projectRoot = resolve(__dirname, '..');
const stylesRoot = join(projectRoot, 'src', 'styles');

/** 预览服务器端口（与 dev 服务器 3000 隔离） */
const PORT = 3001;

/**
 * GeoBgDecor 变体配置
 * 与 GeoBgDecor.astro 中的 GEO_DECOR_CONFIG 保持同步
 */
const GEO_DECOR_CONFIG = {
  home: [
    'geo-curve-s',
    'geo-ripple-tr',
    'geo-triangle-rt',
    'geo-cross-marks',
    'geo-spiral-ccw',
    'geo-pulse-ring',
    'geo-float-block',
  ],
  docs: [
    'geo-bg-grid',
    'geo-curve-s',
    'geo-cross-marks',
    'geo-dots-radial',
    'geo-bezier-flow',
    'geo-pulse-ring',
    'geo-float-block',
  ],
  list: [
    'geo-bg-grid',
    'geo-parallel-lines',
    'geo-cross-marks',
    { className: 'geo-hatch-block', style: 'top:12%;right:4%' },
    'geo-dots-radial',
    'geo-chevron-stack',
    'geo-bezier-flow',
  ],
  minimal: ['geo-bg-grid', 'geo-dots-sm'],
  loading: ['geo-bg-grid', 'geo-dots-sm'],
  error: ['geo-bg-grid', 'geo-dots-lg'],
  info: [
    'geo-bg-grid',
    'geo-curve-s',
    'geo-cross-marks',
    'geo-dots-radial',
    'geo-pulse-ring',
    'geo-float-block',
  ],
};

/** 变体中文描述映射 */
const VARIANT_LABELS = {
  home: { title: '首页（home）', desc: 'Hero 区 S 曲线 + 涟漪环 + 三角切片等 7 项装饰' },
  docs: { title: '文档详情页（docs）', desc: '网格底纹 + 几何线条 + 动态元素，克制 7 项' },
  list: { title: '列表页（list）', desc: '网格底纹 + 平行斜线 + 十字坐标点 + 动态元素' },
  minimal: { title: '轻量变体（minimal）', desc: '仅网格底纹 + 小点阵，用于搜索/404 等辅助页' },
  loading: { title: '加载态（loading）', desc: '网格底纹 + 小点阵，保持克制不分散注意力' },
  error: { title: '错误态（error）', desc: '网格底纹 + 大点阵，疏点阵传达空旷感' },
  info: { title: '信息页（info）', desc: '类似 docs 但更克制，用于 about/privacy 等信息页' },
};

/**
 * 读取 CSS 文件内容
 * @param {string} relativePath - 相对于 src/styles 的路径
 * @returns {string} 文件内容，文件不存在时返回空字符串
 */
function readCss(relativePath) {
  const fullPath = join(stylesRoot, relativePath);
  if (!existsSync(fullPath)) {
    console.warn(`[warn] CSS 文件不存在: ${fullPath}`);
    return '';
  }
  return readFileSync(fullPath, 'utf-8');
}

/**
 * 渲染单个变体的装饰层 HTML
 * @param {string} variantName - 变体名称
 * @returns {string} 装饰层 div 的 HTML 字符串
 */
function renderDecorItems(variantName) {
  const items = GEO_DECOR_CONFIG[variantName];
  return items
    .map((item) => {
      const className = typeof item === 'string' ? item : item.className;
      const style = typeof item === 'string' ? '' : item.style || '';
      return `      <div class="${className}"${style ? ` style="${style}"` : ''}></div>`;
    })
    .join('\n');
}

/**
 * 生成变体预览卡片 HTML
 * @param {string} variantName - 变体名称
 * @returns {string} 卡片 HTML
 */
function renderVariantCard(variantName) {
  const label = VARIANT_LABELS[variantName];
  const decorHtml = renderDecorItems(variantName);
  const itemCount = GEO_DECOR_CONFIG[variantName].length;

  return `
    <section class="variant-card">
      <header class="variant-header">
        <h2>${label.title}</h2>
        <span class="variant-badge">${itemCount} 项装饰</span>
      </header>
      <p class="variant-desc">${label.desc}</p>
      <div class="variant-preview">
        <div class="geo-bg-decor" aria-hidden="true">
${decorHtml}
        </div>
        <div class="variant-content-placeholder">
          <span>内容区域占位</span>
        </div>
      </div>
    </section>`;
}

/**
 * 生成完整的预览页面 HTML
 * @returns {string} 完整 HTML 文档
 */
function renderPreviewPage() {
  // 读取所需的 CSS 文件
  const variablesCss = readCss('variables.css');
  const geoDecorCss = readCss('geo-decor.css');
  const tokensCss = readCss('shared/tokens.css');

  // 渲染所有变体卡片
  const variantCards = Object.keys(GEO_DECOR_CONFIG)
    .map(renderVariantCard)
    .join('\n');

  return `<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>FANDEX 背景装饰预览</title>
  <style>
    /* ===== 内联源 CSS（variables + tokens + geo-decor） ===== */
    ${variablesCss}

    ${tokensCss}

    ${geoDecorCss}

    /* ===== 预览页面专属样式 ===== */
    :root {
      --preview-bg: #FAF9F6;
      --preview-fg: #1a1a1a;
      --preview-card-bg: #ffffff;
      --preview-border: rgba(0, 0, 0, 0.1);
      --preview-accent: #00838F;
    }

    [data-theme='dark'] {
      --preview-bg: #0a0e14;
      --preview-fg: #e5e5e5;
      --preview-card-bg: #141414;
      --preview-border: rgba(255, 255, 255, 0.1);
      --preview-accent: #00E5FF;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI',
        'PingFang SC', 'Microsoft YaHei', sans-serif;
      background: var(--preview-bg);
      color: var(--preview-fg);
      transition: background-color 0.25s ease, color 0.25s ease;
      min-height: 100vh;
      padding: 32px 24px 64px;
    }

    .preview-header {
      max-width: 1200px;
      margin: 0 auto 32px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
    }

    .preview-header h1 {
      font-size: 1.75rem;
      font-weight: 600;
      letter-spacing: -0.02em;
    }

    .preview-header p {
      font-size: 0.875rem;
      opacity: 0.7;
      margin-top: 4px;
    }

    .theme-toggle {
      padding: 8px 16px;
      border: 1px solid var(--preview-border);
      border-radius: 6px;
      background: var(--preview-card-bg);
      color: var(--preview-fg);
      cursor: pointer;
      font-size: 0.875rem;
      font-weight: 500;
      transition: all 0.2s ease;
    }

    .theme-toggle:hover {
      border-color: var(--preview-accent);
      color: var(--preview-accent);
    }

    .variants-grid {
      max-width: 1200px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1fr;
      gap: 32px;
    }

    @media (min-width: 900px) {
      .variants-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    .variant-card {
      background: var(--preview-card-bg);
      border: 1px solid var(--preview-border);
      border-radius: 12px;
      overflow: hidden;
      transition: border-color 0.2s ease;
    }

    .variant-card:hover {
      border-color: var(--preview-accent);
    }

    .variant-header {
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--preview-border);
    }

    .variant-header h2 {
      font-size: 1rem;
      font-weight: 600;
      font-family: 'JetBrains Mono', 'Cascadia Code', Consolas, monospace;
    }

    .variant-badge {
      font-size: 0.75rem;
      padding: 2px 8px;
      border-radius: 4px;
      background: var(--preview-accent);
      color: var(--preview-bg);
      font-weight: 500;
    }

    .variant-desc {
      padding: 8px 20px 12px;
      font-size: 0.8125rem;
      opacity: 0.7;
    }

    .variant-preview {
      position: relative;
      height: 280px;
      overflow: hidden;
      background: var(--preview-bg);
      border-top: 1px solid var(--preview-border);
    }

    /* 覆盖 .geo-bg-decor 的 fixed 定位，改为 absolute 适配预览卡片 */
    .variant-preview .geo-bg-decor {
      position: absolute;
      inset: 0;
    }

    .variant-content-placeholder {
      position: relative;
      z-index: 1;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      pointer-events: none;
    }

    .variant-content-placeholder span {
      padding: 8px 20px;
      background: var(--preview-card-bg);
      border: 1px solid var(--preview-border);
      border-radius: 6px;
      font-size: 0.8125rem;
      opacity: 0.5;
      font-family: 'JetBrains Mono', monospace;
    }

    .preview-footer {
      max-width: 1200px;
      margin: 48px auto 0;
      padding-top: 24px;
      border-top: 1px solid var(--preview-border);
      font-size: 0.8125rem;
      opacity: 0.5;
      text-align: center;
    }
  </style>
</head>
<body>
  <header class="preview-header">
    <div>
      <h1>FANDEX 背景装饰预览</h1>
      <p>GeoBgDecor 组件全部变体可视化预览 · 共 ${Object.keys(GEO_DECOR_CONFIG).length} 个变体</p>
    </div>
    <button class="theme-toggle" id="theme-toggle" type="button">
      切换暗色模式
    </button>
  </header>

  <main class="variants-grid">
${variantCards}
  </main>

  <footer class="preview-footer">
    <p>此页面为独立预览工具，不依赖 Astro 构建 · 端口 ${PORT}</p>
  </footer>

  <script>
    // 主题切换逻辑
    (function() {
      var btn = document.getElementById('theme-toggle');
      var root = document.documentElement;
      btn.addEventListener('click', function() {
        var current = root.getAttribute('data-theme');
        var next = current === 'dark' ? 'light' : 'dark';
        root.setAttribute('data-theme', next);
        btn.textContent = next === 'dark' ? '切换亮色模式' : '切换暗色模式';
      });
    })();
  </script>
</body>
</html>`;
}

/**
 * HTTP 请求处理器
 * @param {import('node:http').IncomingMessage} req
 * @param {import('node:http').ServerResponse} res
 */
function handleRequest(req, res) {
  if (req.url === '/' || req.url === '/index.html') {
    const html = renderPreviewPage();
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(html);
    return;
  }

  // 健康检查端点
  if (req.url === '/health') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ status: 'ok', service: 'bg-decor-preview' }));
    return;
  }

  res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
  res.end('404 Not Found');
}

// 启动服务器
const server = createServer(handleRequest);

server.listen(PORT, () => {
  console.log('');
  console.log('  ┌──────────────────────────────────────────────┐');
  console.log('  │  FANDEX 背景装饰预览服务器                    │');
  console.log('  │                                              │');
  console.log(`  │  地址: http://localhost:${PORT}                │`);
  console.log(`  │  变体: ${Object.keys(GEO_DECOR_CONFIG).length} 个（home/docs/list/minimal/loading/error/info）│`);
  console.log('  │                                              │');
  console.log('  │  按 Ctrl+C 停止                               │');
  console.log('  └──────────────────────────────────────────────┘');
  console.log('');
});

// 优雅退出
process.on('SIGINT', () => {
  console.log('\n正在关闭预览服务器...');
  server.close(() => process.exit(0));
});

process.on('SIGTERM', () => {
  server.close(() => process.exit(0));
});
