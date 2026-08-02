---
order: 160
title: 嵌入式内容
module: 'html5'
category: 前端技术
difficulty: intermediate
description: iframe、embed、object
author: fanquanpp
updated: '2026-06-14'
related:
  - 'html5/014-AudioVideo'
  - 'html5/015-SVG'
  - 'html5/017-ProgressMeter'
  - 'html5/018-WebComponentsPWADevelopment'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 直觉：网页里的“网页”

你见过网页里嵌着的地图、视频、支付页面吗？那很可能就是 `<iframe>`——在一个网页里开一个“小窗口”，嵌入另一个网页。

典型场景：嵌入 YouTube 视频、Google 地图、第三方支付、社交推文、CodePen 代码演示。这节课学会三件事：怎么嵌（`iframe`）、怎么限制它的权限（`sandbox`）、怎么注意安全与性能。

## 1. 一句话了解历史

1997 年微软 IE 提出 `<iframe>`（内联框架），用来在页面中嵌入另一个文档。早期还有更激进的 `<frameset>` 整页分框方案，因为对 SEO、可访问性和导航都不友好，HTML5 已将其废弃。`iframe` 一直保留到今天，并演进出 `sandbox`（沙箱）、`srcdoc`（内嵌文档）、`loading="lazy"`（懒加载）等能力。你只需要记住：iframe 功能强大，但也必须管好它的权限。

## 2. iframe 核心速览

### 2.1 基础用法

```html
<iframe
  src="https://example.com"
  width="800"
  height="600"
  title="嵌入页面"
></iframe>
```

**讲解：**

- `src` 指定嵌入的地址，`width`/`height` 定义窗口尺寸；
- `title` 是给读屏用户的名字，每个 `iframe` 都应提供；
- 嵌入第三方内容前，先确认对方允许被嵌入（有些站点通过响应头禁止）。

### 2.2 常用属性

| 属性 | 作用 | 示例 |
| --- | --- | --- |
| `src` | 嵌入地址 | `src="https://example.com"` |
| `srcdoc` | 直接嵌入 HTML 字符串 | `srcdoc="<p>你好</p>"` |
| `sandbox` | 限制脚本、表单等能力 | `sandbox="allow-scripts"` |
| `allow` | 授权摄像头、麦克风等 | `allow="camera; microphone"` |
| `loading` | 懒加载 | `loading="lazy"` |
| `title` | 无障碍名称 | `title="地图"` |

### 2.3 sandbox 入门

```html
<!-- 最安全：什么能力都不给 -->
<iframe src="https://example.com" sandbox></iframe>

<!-- 按需开放：允许脚本，但不允许弹窗与表单提交 -->
<iframe
  src="https://example.com"
  sandbox="allow-scripts allow-same-origin"
></iframe>
```

**讲解：**

- `sandbox` 空值表示启用全部限制：脚本、表单、弹窗、同源访问全部禁止；
- 令牌（token）按需放开：`allow-scripts` 允许脚本、`allow-same-origin` 允许同源访问、`allow-forms` 允许表单提交、`allow-popups` 允许弹窗；
- 注意：`allow-scripts` 与 `allow-same-origin` 同时使用时，嵌入内容可以移除自己的沙箱，只对可信内容这样配置。

## 3. 安全与性能速览

### 3.1 安全三原则

1. 默认加 `sandbox`，按需放权；
2. 不信任的第三方内容，尽量用 `sandbox="allow-scripts allow-same-origin"` 之外的最小权限；
3. 配合 CSP 的 `frame-src` 限制可嵌入的来源白名单。

### 3.2 性能注意

- 每个 `iframe` 都是一个独立的文档与进程，数量过多会显著消耗内存；
- 非首屏 `iframe` 使用 `loading="lazy"`；
- 通信优先使用 `postMessage` 白名单校验，不要用 `window.parent` 直接操作。

### 3.3 与父页面通信

```javascript
// 父页面发送消息
iframe.contentWindow.postMessage({ type: 'hello' }, 'https://example.com');

// 父页面接收消息（必须校验来源）
window.addEventListener('message', (event) => {
  if (event.origin !== 'https://example.com') return;
  console.log(event.data);
});
```

**讲解：**

- `postMessage` 是跨窗口通信的标准方式，第二个参数限定目标来源；
- 接收消息时必须校验 `event.origin`，否则任何页面都能伪造消息；
- 详细用法见 `html5/028-CrossDocumentCommunication`。
## 4. 代码示例

### 4.1 完整 HTML5 文档结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>嵌入式内容示例</title>
    <!-- 样式将在后续 CSS 课程中学习，本示例只保留结构与交互逻辑 -->
  </head>
  <body>
    <!-- 1. 基础 iframe -->
    <iframe src="https://example.com" width="800" height="600" title="嵌入页面"></iframe>

    <!-- 2. sandbox 最小授权 -->
    <iframe
      src="widget.html"
      sandbox="allow-scripts allow-forms"
      allow="geolocation"
      referrerpolicy="no-referrer"
      loading="lazy"
      title="第三方小组件"
    ></iframe>

    <!-- 3. srcdoc 内联内容 -->
    <iframe
      srcdoc="<h1>内联内容</h1><p>无需 HTTP 请求</p>"
      sandbox="allow-scripts"
      title="内联示例"
    ></iframe>

    <!-- 4. 全屏视频嵌入 -->
    <iframe
      src="https://www.youtube.com/embed/dQw4w9WgXcQ"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
      class="widget"
      title="视频嵌入"
    ></iframe>

    <!-- 5. 广告 iframe（懒加载 + 凭据隔离） -->
    <iframe
      src="https://ads.example.com/banner"
      sandbox="allow-scripts allow-popups"
      credentialless
      loading="lazy"
      importance="low"
      class="ad"
      title="广告"
    ></iframe>

    <!-- 6. PDF 嵌入（object 回退） -->
    <object data="document.pdf" type="application/pdf" width="800" height="600">
      <param name="view" value="FitH" />
      <param name="toolbar" value="1" />
      <p>您的浏览器不支持 PDF 预览，<a href="document.pdf">点击下载</a></p>
    </object>

    <!-- 7. embed 嵌入（Flash 退役后少用） -->
    <embed src="animation.svg" type="image/svg+xml" width="400" height="300" />

    <!-- 8. 门户预渲染（实验性） -->
    <portal src="https://preview.example.com" id="portal"></portal>
  </body>
</html>
```

**代码结构解析：**

（1）基础嵌入：普通 `iframe` 直接引入第三方页面，`title` 提供无障碍名称；

（2）最小授权：`sandbox` 空值最安全，按需添加 `allow-scripts` 等令牌；

（3）通信：父页面用 `postMessage` 发送消息，接收时校验 `event.origin`；

（4）展示：广告位等固定尺寸内容用 `iframe` 承载，响应式场景配合 CSS 控制显示尺寸。

### 4.2 父子 iframe 双向通信

```html
<!-- parent.html -->
<!DOCTYPE html>
<html lang="zh-CN">
  <head><meta charset="UTF-8" /><title>父文档</title></head>
  <body>
    <iframe id="widget" src="https://widget.example.com" sandbox="allow-scripts"></iframe>
    <script>
      const widget = document.getElementById('widget');

      // 父 → iframe
      function sendToWidget(type, payload) {
        widget.contentWindow.postMessage({ type, payload }, 'https://widget.example.com');
      }

      // 接收 iframe 响应
      window.addEventListener('message', (event) => {
        if (event.origin !== 'https://widget.example.com') return;
        console.log('收到 iframe 消息:', event.data);
      });

      // 等待 iframe 就绪后发送
      widget.addEventListener('load', () => {
        sendToWidget('init', { userId: 123, theme: 'dark' });
      });
    </script>
  </body>
</html>
```

```html
<!-- widget.html -->
<!DOCTYPE html>
<html lang="zh-CN">
  <head><meta charset="UTF-8" /><title>Widget</title></head>
  <body>
    <script>
      const PARENT_ORIGIN = 'https://parent.example.com';

      window.addEventListener('message', (event) => {
        if (event.origin !== PARENT_ORIGIN) return;
        const { type, payload } = event.data;
        if (type === 'init') {
          console.log('收到父文档初始化:', payload);
          // 处理后回传
          event.source.postMessage(
            { type: 'ready', payload: { status: 'ok' } },
            PARENT_ORIGIN
          );
        }
      });
    </script>
  </body>
</html>
```

### 4.3 MessageChannel 私有通信管道

```javascript
// 父文档
const iframe = document.createElement('iframe');
iframe.src = 'https://widget.example.com';
iframe.sandbox = 'allow-scripts';
document.body.appendChild(iframe);

iframe.addEventListener('load', () => {
  const channel = new MessageChannel();
  
  // port1 留给父文档
  channel.port1.onmessage = (e) => console.log('父收到:', e.data);
  
  // port2 转移给 iframe
  iframe.contentWindow.postMessage(
    { type: 'init-channel' },
    'https://widget.example.com',
    [channel.port2]
  );
  
  // 通过 port1 发送
  channel.port1.postMessage({ cmd: 'getData' });
});
```

```javascript
// iframe 内
window.addEventListener('message', (e) => {
  if (e.data.type === 'init-channel' && e.ports.length > 0) {
    const port = e.ports[0];
    port.onmessage = (ev) => {
      console.log('iframe 收到:', ev.data);
      port.postMessage({ reply: 'done' });
    };
    port.start();
  }
});
```

### 4.4 srcdoc 富文本编辑器沙箱

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <title>沙箱富文本编辑器</title>
    <!-- 样式将在后续 CSS 课程中学习，本示例只保留结构与交互逻辑 -->
  </head>
  <body>
    <div class="editor-container">
      <div class="toolbar">
        <button data-cmd="bold">B</button>
        <button data-cmd="italic">I</button>
        <button data-cmd="underline">U</button>
        <button data-cmd="insertUnorderedList">UL</button>
        <button data-cmd="formatBlock" data-value="h1">H1</button>
        <button data-cmd="formatBlock" data-value="p">P</button>
      </div>
      <iframe id="editor" sandbox="allow-scripts"></iframe>
    </div>

    <script>
      const editor = document.getElementById('editor');
      const initialContent = `<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><style>
body { font-family: sans-serif; padding: 12px; }
</style></head>
<body contenteditable="true">
<h1>欢迎使用沙箱编辑器</h1>
<p>开始输入...</p>
</body>
</html>`;
      
      editor.srcdoc = initialContent;
      
      editor.addEventListener('load', () => {
        editor.contentDocument.designMode = 'on';
      });
      
      document.querySelector('.toolbar').addEventListener('click', (e) => {
        const btn = e.target.closest('button');
        if (!btn) return;
        const cmd = btn.dataset.cmd;
        const value = btn.dataset.value || null;
        editor.contentDocument.execCommand(cmd, false, value);
        editor.contentWindow.focus();
      });
    </script>
  </body>
</html>
```

### 4.5 PDF 嵌入完整方案

```html
<!-- 主路径：object + iframe 回退 -->
<object data="report.pdf#view=FitH&toolbar=1" type="application/pdf" width="100%" height="800">
  <param name="view" value="FitH" />
  <param name="toolbar" value="1" />
  <param name="statusbar" value="1" />
  <param name="messages" value="1" />
  <param name="navpanes" value="1" />
  
  <!-- 浏览器不支持 PDF 时回退到 iframe -->
  <iframe src="report.pdf#view=FitH" width="100%" height="800" title="PDF 预览">
    <!-- 仍不支持时提供下载链接 -->
    <p>
      您的浏览器不支持 PDF 内嵌预览。
      <a href="report.pdf" download>点击下载 PDF</a>
    </p>
  </iframe>
</object>

<!-- 使用 PDF.js（跨浏览器一致体验） -->
<iframe
  src="pdfjs/web/viewer.html?file=report.pdf"
  width="100%"
  height="800"
  sandbox="allow-scripts allow-same-origin"
  title="PDF.js 预览"
></iframe>
```

### 4.6 微前端容器示例

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <title>微前端容器</title>
    <!-- 样式将在后续 CSS 课程中学习，本示例只保留结构与交互逻辑 -->
  </head>
  <body>
    <div class="mfe-container">
      <header class="mfe-header">
        <div class="mfe-tabs">
          <button data-app="dashboard" class="active">仪表盘</button>
          <button data-app="orders">订单</button>
          <button data-app="users">用户</button>
        </div>
      </header>
      <iframe id="mfe-frame" sandbox="allow-scripts allow-forms allow-popups"></iframe>
    </div>

    <script>
      const frame = document.getElementById('mfe-frame');
      const apps = {
        dashboard: 'https://dashboard.mfe.example.com',
        orders: 'https://orders.mfe.example.com',
        users: 'https://users.mfe.example.com',
      };
      const channel = new MessageChannel();
      channel.port1.onmessage = (e) => {
        if (e.data.type === 'route-change') {
          console.log('子应用路由变更:', e.data.path);
        }
      };

      function switchApp(name) {
        document.querySelectorAll('.mfe-tabs button').forEach((b) => {
          b.classList.toggle('active', b.dataset.app === name);
        });
        frame.src = apps[name];
        frame.addEventListener('load', () => {
          frame.contentWindow.postMessage({ type: 'handshake' }, apps[name], [channel.port2]);
        }, { once: true });
      }

      document.querySelector('.mfe-tabs').addEventListener('click', (e) => {
        const btn = e.target.closest('button');
        if (btn) switchApp(btn.dataset.app);
      });

      switchApp('dashboard');
    </script>
  </body>
</html>
```

---

## 5. 对比分析

### 5.1 嵌入元素横向对比

| 特性 | `<iframe>` | `<embed>` | `<object>` | `<portal>` |
| ---- | ---------- | --------- | ---------- | ---------- |
| 元素类型 | 嵌入式 | 嵌入式 | 嵌入式 | 嵌入式（实验） |
| 闭合方式 | 显式 `</iframe>` | 自闭合 | 显式 `</object>` | 显式 `</portal>` |
| 回退内容 | 支持 | 不支持 | 支持 | 不支持 |
| DOM 访问 | `contentDocument` | 无 | `contentDocument` | `contentWindow`（受限） |
| 沙箱 | `sandbox` 属性 | 无 | 无 | 天然沙箱 |
| 跨源通信 | `postMessage` | 受限 | `postMessage` | 受限 |
| 语义 | 嵌入 HTML 文档 | 嵌入插件内容 | 通用嵌入 | 预渲染页面 |
| HTML5 状态 | 推荐 | 推荐（受限） | 推荐 | 实验 |
| 典型用途 | widget、广告、微前端 | SVG、视频（已少用） | PDF、回退 | 跨站预渲染 |
| 进程隔离 | 支持（站点隔离） | 不支持 | 不支持 | 强制隔离 |
| 懒加载 | `loading="lazy"` | 不支持 | 不支持 | 支持 |
| Permissions Policy | `allow` 属性 | 不支持 | 不支持 | 支持 |

### 5.2 iframe 沙箱令牌对比

| 令牌 | 默认 | 启用后 | 风险等级 |
| ---- | ---- | ------ | -------- |
| `allow-scripts` | 禁止 | 允许 JS 执行 | 中 |
| `allow-same-origin` | 禁止 | 保留原始源 | 高（与 scripts 同用危险） |
| `allow-forms` | 禁止 | 允许表单提交 | 低 |
| `allow-popups` | 禁止 | 允许 `window.open` | 中 |
| `allow-popups-to-escape-sandbox` | 禁止 | 弹出窗口脱离沙箱 | 高 |
| `allow-top-navigation` | 禁止 | 允许导航父窗口 | 高 |
| `allow-top-navigation-by-user-activation` | 禁止 | 用户激活下导航父 | 中 |
| `allow-modals` | 禁止 | 允许 `alert`/`confirm` | 低 |
| `allow-pointer-lock` | 禁止 | 允许鼠标锁定 | 低 |
| `allow-presentation` | 禁止 | 允许 Presentation API | 低 |
| `allow-orientation-lock` | 禁止 | 允许屏幕方向锁定 | 低 |
| `allow-downloads` | 禁止 | 允许下载文件 | 低 |
| `allow-storage-access-by-user-activation` | 禁止 | 用户激活下访问存储 | 中 |
| `allow-fullscreen` | 禁用 | 允许全屏 API | 低 |

### 5.3 嵌入式内容 vs Web Components

| 维度 | `<iframe>` | Web Components (Shadow DOM) |
| ---- | ---------- | --------------------------- |
| CSS 隔离 | 完全隔离 | Shadow DOM 隔离 |
| JS 隔离 | 完全独立 | 共享主文档 |
| 资源加载 | 独立请求 | 共享主文档 |
| 通信 | `postMessage` | 直接函数调用 / 事件 |
| 性能 | 进程开销 | 轻量 |
| SEO | 不索引（默认） | 索引 |
| 可访问性 | 需 `title` | 原生支持 |
| 跨源 | 支持 | 不支持 |
| 第三方库 | 完美隔离 | 样式冲突 |
| 适用场景 | 第三方 widget、广告、微前端 | UI 组件、设计系统 |

### 5.4 src vs srcdoc 选择

| 维度 | `src` | `srcdoc` |
| ---- | ----- | -------- |
| 内容来源 | HTTP 请求 | 内联字符串 |
| 加载延迟 | RTT + 解析 | 仅解析 |
| 缓存 | 可缓存（HTTP） | 不可缓存（随主文档） |
| 大小限制 | 无 | 受 HTML 属性大小限制 |
| 语义清晰度 | 高 | 低（内容混在属性中） |
| 工具链支持 | 完善 | 较弱 |
| 适用场景 | 第三方页面、大型内容 | 小型沙箱、富文本编辑器、邮件预览 |

### 5.5 PDF 嵌入方案对比

| 方案 | 浏览器支持 | 体验一致性 | 文件保护 | 实现复杂度 |
| ---- | ---------- | ---------- | -------- | ---------- |
| `<object data>` | Chrome/Firefox 原生 | 不一致 | 弱 | 低 |
| `<iframe src>` | Chrome/Firefox 原生 | 不一致 | 弱 | 低 |
| `<embed src>` | Chrome 原生 | 不一致 | 弱 | 低 |
| PDF.js (`<iframe>` 包装) | 全平台 | 一致 | 中 | 中 |
| 服务端转图片 | 全平台 | 一致 | 强 | 高 |
| 商业 SDK（Adobe PDF Embed API） | 全平台 | 一致 | 中 | 中 |

---

## 6. 常见陷阱与反模式

### 6.1 类型与语义陷阱

**陷阱 7.1.1**：`<iframe>` 缺少 `title` 属性。

```html
<!-- 反模式 -->
<iframe src="widget.html"></iframe>

<!-- 正确 -->
<iframe src="widget.html" title="用户评论组件"></iframe>
```

**后果**：屏幕阅读器无法识别 iframe 用途，可访问性扣分（Lighthouse 检测项）。

**陷阱 7.1.2**：混淆 `name` 与 `id`。

```html
<!-- 反模式：用 name 作为 CSS 选择器 -->
<iframe name="widget"></iframe>
<style>iframe[name=widget] { ... }</style>

<!-- 正确：用 id 作为选择器，name 用于 target -->
<iframe id="widget-frame" name="widget"></iframe>
```

**陷阱 7.1.3**：误用 `<embed>` 嵌入 HTML。

```html
<!-- 反模式 -->
<embed src="page.html" type="text/html">

<!-- 正确 -->
<iframe src="page.html"></iframe>
```

### 6.2 安全反模式

**反模式 7.2.1**：`sandbox="allow-scripts allow-same-origin"` 同时使用。

```html
<!-- 危险：沙箱可被绕过 -->
<iframe src="untrusted.html" sandbox="allow-scripts allow-same-origin"></iframe>
```

**修复**：若必须同源，使用 CSP 限制；若必须脚本，使用 `credentialless` 或跨源部署。

**反模式 7.2.2**：`postMessage` 使用 `*` 通配符。

```javascript
// 反模式：任意源可接收
iframe.contentWindow.postMessage(secret, '*');

// 正确：指定目标源
iframe.contentWindow.postMessage(secret, 'https://widget.example.com');
```

**反模式 7.2.3**：未校验 `event.origin`。

```javascript
// 反模式
window.addEventListener('message', (e) => {
  doSomething(e.data);  // 任意源可触发
});

// 正确
window.addEventListener('message', (e) => {
  if (e.origin !== 'https://trusted.example.com') return;
  doSomething(e.data);
});
```

**反模式 7.2.4**：`<iframe src="javascript:...">`。

```html
<!-- 反模式：现代浏览器已禁止 -->
<iframe src="javascript:alert(1)"></iframe>
```

**修复**：使用 `srcdoc` 或 `about:blank` + JS 写入。

### 6.3 性能反模式

**反模式 7.3.1**：首屏可视区 iframe 不加 `loading="lazy"`，但非首屏也不加。

```html
<!-- 反模式：所有 iframe 立即加载 -->
<iframe src="ad1.html"></iframe>
<iframe src="ad2.html"></iframe>
<!-- ... 50 个 iframe ... -->

<!-- 正确：非首屏使用 lazy -->
<iframe src="ad1.html"></iframe>  <!-- 首屏 -->
<iframe src="ad2.html" loading="lazy"></iframe>  <!-- 非首屏 -->
```

**反模式 7.3.2**：iframe 缺少 `width`/`height` 导致 CLS。

```html
<!-- 反模式：无尺寸声明 -->
<iframe src="video.html"></iframe>

<!-- 正确：声明尺寸或 aspect-ratio -->
<iframe src="video.html" width="560" height="315"></iframe>
<!-- 或 CSS -->
<iframe src="video.html" style="aspect-ratio: 16/9; width: 100%;"></iframe>
```

**反模式 7.3.3**：嵌套 iframe 过深。

```html
<!-- 反模式：5 层嵌套 -->
<iframe src="a.html"><iframe src="b.html"><iframe src="c.html">...</iframe></iframe></iframe>
```

**后果**：性能急剧下降，部分浏览器限制最大嵌套深度。

### 6.4 可访问性陷阱

**陷阱 7.4.1**：iframe 内容无键盘焦点管理。

```html
<!-- 反模式：iframe 内按钮无法通过 Tab 访问 -->
<iframe src="modal.html" tabindex="-1"></iframe>
```

**修复**：iframe 默认可聚焦，移除 `tabindex="-1"`，并在 iframe 内部管理焦点。

**陷阱 7.4.2**：iframe 内 `title` 与外层 `aria-label` 冲突。

```html
<!-- 反模式 -->
<div role="dialog" aria-label="登录对话框">
  <iframe src="login.html" title="登录表单"></iframe>
</div>
```

**修复**：外层不设 `aria-label`，依赖 iframe `title`。

### 6.5 SEO 陷阱

**陷阱 7.5.1**：核心内容放入 iframe。

```html
<!-- 反模式：正文内容在 iframe 中 -->
<iframe src="article.html"></iframe>
```

**后果**：搜索引擎可能不索引 iframe 内容（Google 索引部分 iframe，但不保证）。

**修复**：核心内容直接写在主文档；iframe 仅用于辅助内容（评论、广告）。

**陷阱 7.5.2**：`srcdoc` 内容不被索引。

```html
<!-- 反模式：关键 SEO 内容在 srcdoc -->
<iframe srcdoc="<h1>核心关键词</h1><p>...</p>"></iframe>
```

**后果**：`srcdoc` 内容作为属性，搜索引擎通常不索引。

---

## 7. 工程实践

### 7.1 TypeScript 类型定义

```typescript
// iframe-secure.ts
interface SandboxToken {
  readonly value:
    | 'allow-downloads'
    | 'allow-forms'
    | 'allow-modals'
    | 'allow-orientation-lock'
    | 'allow-pointer-lock'
    | 'allow-popups'
    | 'allow-popups-to-escape-sandbox'
    | 'allow-presentation'
    | 'allow-same-origin'
    | 'allow-scripts'
    | 'allow-storage-access-by-user-activation'
    | 'allow-top-navigation'
    | 'allow-top-navigation-by-user-activation';
}

interface SecureIframeOptions {
  src: string;
  sandbox?: SandboxToken['value'][];
  allow?: string[];  // Permissions Policy
  loading?: 'lazy' | 'eager';
  referrerPolicy?: ReferrerPolicy;
  credentialless?: boolean;
  title: string;  // 强制必填
  width?: number | string;
  height?: number | string;
  className?: string;
  onLoad?: () => void;
}

class IframeSecurityError extends Error {}

function validateSandbox(tokens: SandboxToken['value'][]): void {
  if (tokens.includes('allow-scripts') && tokens.includes('allow-same-origin')) {
    console.warn(
      '[security] sandbox 同时启用 allow-scripts 与 allow-same-origin 可能被绕过'
    );
  }
}

function createSecureIframe(options: SecureIframeOptions): HTMLIFrameElement {
  const { sandbox = [], allow = [], title, ...rest } = options;
  
  if (!title) {
    throw new IframeSecurityError('iframe 必须提供 title 属性以满足可访问性');
  }
  
  validateSandbox(sandbox);
  
  const iframe = document.createElement('iframe');
  iframe.src = rest.src;
  iframe.title = title;
  iframe.sandbox.value = sandbox.join(' ');
  if (allow.length > 0) {
    iframe.allow = allow.join('; ');
  }
  if (rest.loading) iframe.loading = rest.loading;
  if (rest.referrerPolicy) iframe.referrerPolicy = rest.referrerPolicy;
  if (rest.credentialless) iframe.setAttribute('credentialless', '');
  if (rest.width) iframe.width = String(rest.width);
  if (rest.height) iframe.height = String(rest.height);
  if (rest.className) iframe.className = rest.className;
  if (rest.onLoad) iframe.addEventListener('load', rest.onLoad);
  
  return iframe;
}

// 使用
const widget = createSecureIframe({
  src: 'https://widget.example.com',
  sandbox: ['allow-scripts', 'allow-forms'],
  allow: ['geolocation', 'camera'],
  loading: 'lazy',
  referrerPolicy: 'no-referrer',
  title: '用户头像编辑器',
  width: 400,
  height: 300,
});
document.body.appendChild(widget);
```

### 7.2 React 封装

```tsx
// SecureIframe.tsx
import React, { iframeHTMLAttributes, useCallback, useEffect, useRef } from 'react';

type SandboxToken =
  | 'allow-downloads' | 'allow-forms' | 'allow-modals'
  | 'allow-orientation-lock' | 'allow-pointer-lock' | 'allow-popups'
  | 'allow-popups-to-escape-sandbox' | 'allow-presentation'
  | 'allow-same-origin' | 'allow-scripts'
  | 'allow-storage-access-by-user-activation'
  | 'allow-top-navigation' | 'allow-top-navigation-by-user-activation';

interface SecureIframeProps
  extends Omit<iframeHTMLAttributes<HTMLIFrameElement>, 'sandbox' | 'allow'> {
  sandbox?: SandboxToken[];
  allow?: string[];
  onMessage?: (data: unknown, origin: string) => void;
  allowedOrigins?: string[];
  rpcHandlers?: Record<string, (payload: unknown) => Promise<unknown>>;
}

export const SecureIframe: React.FC<SecureIframeProps> = ({
  sandbox = ['allow-scripts'],
  allow = [],
  src,
  srcdoc,
  title,
  loading = 'lazy',
  onMessage,
  allowedOrigins = [],
  rpcHandlers = {},
  ...rest
}) => {
  const iframeRef = useRef<HTMLIFrameElement>(null);

  // 安全校验：避免 allow-scripts + allow-same-origin 同时使用
  useEffect(() => {
    if (sandbox.includes('allow-scripts') && sandbox.includes('allow-same-origin')) {
      console.warn(
        '[SecureIframe] 同时启用 allow-scripts 与 allow-same-origin 存在沙箱绕过风险'
      );
    }
  }, [sandbox]);

  // 消息处理
  useEffect(() => {
    if (!onMessage && Object.keys(rpcHandlers).length === 0) return;
    
    const handler = async (event: MessageEvent) => {
      const iframeOrigin = new URL(src || '', window.location.href).origin;
      if (!allowedOrigins.includes(event.origin)) return;
      
      if (onMessage) onMessage(event.data, event.origin);
      
      // RPC 模式
      const { id, method, payload } = event.data || {};
      if (method && rpcHandlers[method]) {
        try {
          const result = await rpcHandlers[method](payload);
          iframeRef.current?.contentWindow?.postMessage(
            { id, result },
            event.origin
          );
        } catch (err) {
          iframeRef.current?.contentWindow?.postMessage(
            { id, error: String(err) },
            event.origin
          );
        }
      }
    };
    
    window.addEventListener('message', handler);
    return () => window.removeEventListener('message', handler);
  }, [onMessage, rpcHandlers, allowedOrigins, src]);

  return (
    <iframe
      ref={iframeRef}
      src={src}
      srcDoc={srcdoc}
      title={title}
      sandbox={sandbox.join(' ')}
      allow={allow.join('; ')}
      loading={loading}
      {...rest}
    />
  );
};

// 使用示例
const App: React.FC = () => {
  return (
    <SecureIframe
      src="https://widget.example.com"
      title="用户评论"
      sandbox={['allow-scripts', 'allow-forms']}
      allow={['geolocation']}
      allowedOrigins={['https://widget.example.com']}
      rpcHandlers={{
        getUser: async () => ({ id: 1, name: '张三' }),
      }}
      style={{ width: '100%', aspectRatio: '16/9' }}
    />
  );
};
```

### 7.3 Vue 封装

```vue
<!-- SecureIframe.vue -->
<script setup lang="ts">
import { ref, watch, onMounted, onUnmounted } from 'vue';

type SandboxToken =
  | 'allow-downloads' | 'allow-forms' | 'allow-modals'
  | 'allow-scripts' | 'allow-same-origin' | 'allow-popups';

interface Props {
  src?: string;
  srcdoc?: string;
  title: string;
  sandbox?: SandboxToken[];
  allow?: string[];
  loading?: 'lazy' | 'eager';
  allowedOrigins?: string[];
}

const props = withDefaults(defineProps<Props>(), {
  sandbox: () => ['allow-scripts'],
  allow: () => [],
  loading: 'lazy',
  allowedOrigins: () => [],
});

const emit = defineEmits<{
  (e: 'message', data: unknown, origin: string): void;
  (e: 'load'): void;
}>();

const iframeRef = ref<HTMLIFrameElement>(null);

// 安全校验
watch(
  () => props.sandbox,
  (tokens) => {
    if (tokens.includes('allow-scripts') && tokens.includes('allow-same-origin')) {
      console.warn('[SecureIframe] 同时启用 allow-scripts 与 allow-same-origin 存在风险');
    }
  },
  { immediate: true }
);

// 消息监听
const handleMessage = (event: MessageEvent) => {
  if (props.allowedOrigins.length > 0 && !props.allowedOrigins.includes(event.origin)) {
    return;
  }
  emit('message', event.data, event.origin);
};

onMounted(() => window.addEventListener('message', handleMessage));
onUnmounted(() => window.removeEventListener('message', handleMessage));
</script>

<template>
  <iframe
    ref="iframeRef"
    :src="src"
    :srcdoc="srcdoc"
    :title="title"
    :sandbox="sandbox.join(' ')"
    :allow="allow.join('; ')"
    :loading="loading"
    @load="emit('load')"
  />
</template>
```

### 7.4 CSP 配置实践

```http
# 父文档 HTTP 头
Content-Security-Policy:
  default-src 'self';
  frame-src 'self' https://widget.example.com https://www.youtube.com;
  frame-ancestors 'none';  # 防止被嵌入

# iframe 文档 HTTP 头
Content-Security-Policy:
  default-src 'self';
  script-src 'self';
  frame-ancestors https://parent.example.com;
Cross-Origin-Resource-Policy: same-site;
Cross-Origin-Opener-Policy: same-origin;
```

### 7.5 性能监控

```typescript
// iframe-performance-monitor.ts
interface IframeMetrics {
  src: string;
  loadTime: number;        // 加载耗时
  ttfb: number;            // 首字节时间
  domContentLoaded: number;
  transferSize: number;    // 传输字节数
  layoutShift: number;     // 布局偏移
}

class IframePerformanceMonitor {
  private observer: PerformanceObserver;
  private metrics: Map<string, IframeMetrics> = new Map();

  constructor() {
    this.observer = new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        if (entry.entryType === 'resource' && entry.initiatorType === 'iframe') {
          this.recordResource(entry);
        }
      }
    });
    this.observer.observe({ entryTypes: ['resource', 'LCP'] });
  }

  private recordResource(entry: PerformanceResourceTiming) {
    const metric: IframeMetrics = {
      src: entry.name,
      loadTime: entry.responseEnd - entry.startTime,
      ttfb: entry.responseStart - entry.startTime,
      domContentLoaded: entry.domainLookupEnd - entry.domainLookupStart,
      transferSize: entry.transferSize,
      layoutShift: 0,
    };
    this.metrics.set(entry.name, metric);
    this.report(metric);
  }

  private report(metric: IframeMetrics) {
    // 上报到监控平台
    if (metric.loadTime > 3000) {
      console.warn(`[iframe] 加载缓慢: ${metric.src} (${metric.loadTime}ms)`);
    }
    navigator.sendBeacon('/api/iframe-metrics', JSON.stringify(metric));
  }

  disconnect() {
    this.observer.disconnect();
  }
}
```

### 7.6 自动化测试

```typescript
// iframe.test.ts
import { test, expect } from '@playwright/test';

test.describe('嵌入式 iframe', () => {
  test('安全配置正确', async ({ page }) => {
    await page.goto('/embed-demo');
    const iframe = page.frameLocator('iframe[title="用户评论"]');
    
    // 验证 sandbox 属性
    const sandbox = await page.locator('iframe[title="用户评论"]').getAttribute('sandbox');
    expect(sandbox).toContain('allow-scripts');
    expect(sandbox).not.toContain('allow-same-origin');
    
    // 验证 allow 属性
    const allow = await page.locator('iframe[title="用户评论"]').getAttribute('allow');
    expect(allow).toContain('geolocation');
  });

  test('postMessage 通信正常', async ({ page }) => {
    await page.goto('/embed-demo');
    const iframe = page.frameLocator('iframe[title="测试组件"]');
    
    // 监听父文档消息
    const messagePromise = page.evaluate(() => {
      return new Promise((resolve) => {
        window.addEventListener('message', (e) => {
          if (e.data.type === 'ready') resolve(e.data);
        });
      });
    });
    
    // 触发 iframe 内事件
    await iframe.locator('button#init').click();
    
    const message = await messagePromise;
    expect(message).toEqual({ type: 'ready', payload: { status: 'ok' } });
  });

  test('懒加载生效', async ({ page }) => {
    await page.goto('/embed-demo');
    
    // 验证非首屏 iframe 未加载
    const lazyIframe = page.locator('iframe[loading="lazy"]').last();
    const src = await lazyIframe.getAttribute('src');
    
    // 滚动到视口
    await lazyIframe.scrollIntoViewIfNeeded();
    await page.waitForTimeout(500);
    
    // 验证已加载
    const contentWindow = await lazyIframe.evaluate((el) => el.contentWindow);
    expect(contentWindow).not.toBeNull();
  });
});
```

---

## 8. 案例研究

### 8.1 YouTube 嵌入式播放器

YouTube 提供官方 `<iframe>` 嵌入 API：

```html
<iframe
  src="https://www.youtube.com/embed/VIDEO_ID?enablejsapi=1&origin=https://yoursite.com"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen
  width="560"
  height="315"
  title="YouTube 视频"
></iframe>
```

**安全设计要点**：

1. `origin` 参数限制 postMessage 来源。
2. `allow` 列表精确授权所需能力。
3. `allowfullscreen` 单独声明。
4. YouTube 服务端设置 `X-Frame-Options: ALLOWALL` 允许任意嵌入。

**性能优化**：使用 `lite-youtube-embed` 替代原生 iframe，首屏延迟加载真实 iframe，节省 500KB+ 资源。

### 8.2 Google Maps 嵌入

```html
<iframe
  src="https://www.google.com/maps/embed?pb=..."
  width="600"
  height="450"
  style="border:0"
  allowfullscreen
  loading="lazy"
  referrerpolicy="no-referrer-when-downgrade"
  title="地图位置"
></iframe>
```

**关键属性**：

- `loading="lazy"`：地图在视口外不加载，节省资源。
- `referrerpolicy`：控制 referrer 泄露。
- `allowfullscreen`：支持全屏地图视图。

### 8.3 Stripe 支付组件

Stripe Elements 使用 `<iframe>` 隔离支付字段，符合 PCI DSS 要求：

```javascript
const stripe = Stripe('pk_test_xxx');
const elements = stripe.elements();
const card = elements.create('card');
card.mount('#card-element');
```

**内部机制**：

1. Stripe JS SDK 在 `#card-element` 内创建多个 `<iframe>`。
2. 每个 iframe 加载 `js.stripe.com` 的支付字段。
3. 用户输入的卡号仅在 iframe 内处理，主文档无法访问。
4. 通过 `postMessage` 与主文档通信（仅传递 token，不传递原始卡号）。
5. 满足 PCI DSS SAQ-A 范围（主文档不接触敏感数据）。

### 8.4 Twitter 嵌入推文

```html
<blockquote class="twitter-tweet">
  <p>推文内容...</p>
  <a href="https://twitter.com/user/status/123">— User (@user)</a>
</blockquote>
<script async src="https://platform.twitter.com/widgets.js"></script>
```

`widgets.js` 将 `<blockquote>` 替换为 `<iframe>`：

1. iframe 加载 `syndication.twitter.com`。
2. 推文内容在 iframe 内渲染，样式隔离。
3. 通过 `postMessage` 通知主文档高度变化（`tw-tweet-rendered` 事件）。
4. `sandbox="allow-popups allow-popups-to-escape-sandbox allow-scripts allow-same-origin"`（注意：此处允许同源是因为 Twitter 完全控制 iframe 内容）。

### 8.5 微前端架构：Single-SPA 与 iframe 模式

**Single-SPA 模式**：使用 JS 动态加载子应用 bundle，集成到主文档。优点是路由同步、状态共享，缺点是 CSS/JS 隔离弱。

**iframe 模式**：每个子应用在独立 `<iframe>` 中运行。优点是强隔离，缺点是通信开销大、UX 割裂（滚动、模态框）。

**混合模式**（推荐）：

1. 核心子应用使用 Single-SPA（同源、可信）。
2. 第三方子应用使用 `<iframe>`（跨源、不可信）。
3. 通过 `postMessage` + `MessageChannel` 统一通信层。
4. UI 统一：iframe 内子应用使用与主应用一致的设计系统。

### 8.6 GitHub Gist 嵌入

```html
<script src="https://gist.github.com/user/abc123.js"></script>
```

脚本动态创建 `<iframe>`：

1. iframe 加载 `gist.github.com`。
2. iframe 内渲染代码高亮（使用 Prism.js）。
3. 通过 `postMessage` 通知主文档高度，避免滚动条。
4. `sandbox="allow-scripts"`（最小权限）。
5. `style="width: 100%; height: <动态>px"`。

### 8.7 CodePen 嵌入

```html
<p class="codepen" data-height="300" data-default-tab="html,result">
  See the Pen <a href="...">...</a>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>
```

`ei.js` 将 `.codepen` 元素替换为 `<iframe>`：

1. iframe 加载 `codepen.io/user/pen/abc/embed`。
2. 内置 HTML/CSS/JS 编辑器与实时预览。
3. `sandbox="allow-scripts allow-forms allow-popups allow-modals"`。
4. `allow="accelerometer; camera; encrypted-media; geolocation; gyroscope; microphone; speaker"`（编辑场景需要）。

### 8.8 Adobe PDF Embed API

```html
<script src="https://documentcloud.adobe.com/view-sdk/main.js"></script>
<div id="pdf-viewer"></div>
<script>
  document.addEventListener('adobe-view-sdk-viewer-ready', () => {
    const view = new AdobeDC.View({ clientId: 'YOUR_ID', divId: 'pdf-viewer' });
    view.previewFile({ content: { location: { url: 'doc.pdf' } }, metaData: { fileName: 'doc.pdf' } });
  });
</script>
```

**内部机制**：

1. SDK 创建 `<iframe>` 加载 `documentcloud.adobe.com`。
2. iframe 内运行 PDF.js 修改版 + Adobe 高质量渲染引擎。
3. 通过 `postMessage` 与主文档同步注释、书签。
4. 支持工具栏定制、注释、表单填写、签名。

---

## 11. 扩展阅读

### 11.1 官方规范

- WHATWG HTML Living Standard: https://html.spec.whatwg.org/multipage/iframe-embed-object.html
- W3C HTML 5.3: https://www.w3.org/TR/html53/iframe-embed-object.html
- Permissions Policy: https://www.w3.org/TR/permissions-policy-1/
- Cross-Origin Embedder Policy: https://www.w3.org/TR/cross-origin-embedder-policy-1/

### 11.2 浏览器实现

- Chromium Iframe Rendering: https://chromium.googlesource.com/chromium/src/+/main/docs/security/iframe-pipeline.md
- Site Isolation in Chrome: https://www.chromium.org/Home/chromium-security/site-isolation/
- Firefox Fission (Site Isolation): https://wiki.mozilla.org/Project_Fission

### 11.3 安全研究

- HTML5 Security Cheatsheet: https://html5sec.org/
- OWASP Clickjacking Defense: https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html
- Subresource Integrity (SRI): https://www.w3.org/TR/SRI/

### 11.4 性能优化

- web.dev "Optimize iframe loading": https://web.dev/articles/iframe-lazy-loading
- Chrome Developers "Third-party embeds": https://developer.chrome.com/articles/third-party-embeds/
- LCP and iframes: https://web.dev/articles/lcp#how-to-optimize-embeds

### 11.5 工程实践

- Micro Frontends with iframes: https://martinfowler.com/articles/micro-frontends.html
- Single-SPA framework: https://single-spa.js.org/
- Stripe Elements architecture: https://stripe.com/docs/security
- Adobe PDF Embed API: https://developer.adobe.com/document-services/apis/pdf-embed/

### 11.6 浏览器兼容性矩阵

| 特性 | Chrome | Firefox | Safari | Edge |
| ---- | ------ | ------- | ------ | ---- |
| `<iframe>` 基础 | 全版本 | 全版本 | 全版本 | 全版本 |
| `sandbox` | 4+ | 17+ | 5+ | 12+ |
| `srcdoc` | 20+ | 25+ | 6+ | 79+ |
| `allow` (Permissions Policy) | 60+ | 74+ | 14.1+ | 79+ |
| `loading="lazy"` | 76+ | 121+ | 16.4+ | 79+ |
| `credentialless` | 96+ | 未支持 | 未支持 | 96+ |
| `importance` | 110+ | 未支持 | 未支持 | 110+ |
| `csp` 属性 | 122+ | 未支持 | 未支持 | 122+ |
| `<portal>` | 85+ (flag) | 未支持 | 未支持 | 85+ (flag) |
| `sandbox="allow-storage-access-by-user-activation"` | 119+ | 未支持 | 15.4+ | 119+ |

### 11.7 术语表

| 术语 | 全称 | 说明 |
| ---- | ---- | ---- |
| SOP | Same-Origin Policy | 同源策略 |
| CORS | Cross-Origin Resource Sharing | 跨源资源共享 |
| COEP | Cross-Origin Embedder Policy | 跨源嵌入策略 |
| CORP | Cross-Origin Resource Policy | 跨源资源策略 |
| CSP | Content Security Policy | 内容安全策略 |
| IPC | Inter-Process Communication | 进程间通信 |
| RTT | Round-Trip Time | 网络往返时间 |
| LCP | Largest Contentful Paint | 最大内容渲染时间 |
| CLS | Cumulative Layout Shift | 累积布局偏移 |
| RPC | Remote Procedure Call | 远程过程调用 |
| SAQ | Self-Assessment Questionnaire | 自评估问卷（PCI DSS） |
| SRI | Subresource Integrity | 子资源完整性 |
| TTFB | Time to First Byte | 首字节时间 |

### 11.8 学习路径

**入门（1 周）**：

1. 阅读 WHATWG HTML Living Standard §4.8.5—4.8.7。
2. 完成 MDN "Iframe element" 教程。
3. 要点：基础 iframe 嵌入与 `postMessage` 通信。

**进阶（2 周）**：

1. 学习 `sandbox` 全部令牌，实践最小权限配置。
2. 要点： `MessageChannel` 双向 RPC。
3. 阅读 Chrome Site Isolation 文档。
4. 实践 COEP 与 `credentialless`。

**高级（1 月）**：

1. 要点：微前端容器框架（基于 iframe + Web Components 混合）。
2. 构建 iframe 安全审计工具。
3. 研究 `portal` 元素的预渲染机制。
4. 阅读 Chromium iframe 渲染管线源码。

**研究（持续）**：

1. 跟踪 WHATWG HTML Living Standard 更新。
2. 关注浏览器安全公告（Chrome、Firefox、Safari）。
3. 研究 Spectre 等侧信道攻击对 iframe 隔离的影响。
4. 探索 WebAssembly-based iframe 替代方案。

## 12. 进阶知识点

### 12.1 完整安全配置示例

```html
<iframe
  src="https://trusted-site.com/widget"
  width="800"
  height="600"
  title="第三方小组件"
  sandbox="allow-scripts allow-forms"
  allow="geolocation"
  referrerpolicy="no-referrer"
  loading="lazy"
></iframe>
```

**讲解：**

- `sandbox="allow-scripts allow-forms"` 只放开脚本与表单，弹窗、同源访问仍被禁止；
- `allow="geolocation"` 是权限策略（Permissions Policy），按需授权摄像头、麦克风、定位等；
- `referrerpolicy="no-referrer"` 隐藏来源地址，`loading="lazy"` 延迟加载非首屏组件。

| 属性 | 作用 |
| --- | --- |
| `src` | 嵌入页面 URL |
| `srcdoc` | 内联 HTML 内容 |
| `name` | 框架名称（target 用） |
| `sandbox` | 沙箱安全策略 |
| `allow` | 权限策略（摄像头、麦克风等） |
| `loading` | 懒加载 lazy / eager |
| `referrerpolicy` | Referer 策略 |
| `title` | 无障碍标题（必填） |

### 12.2 sandbox 令牌速查

| 令牌 | 作用 |
| --- | --- |
| `allow-scripts` | 允许执行脚本 |
| `allow-same-origin` | 允许同源访问（与脚本同开时慎用） |
| `allow-forms` | 允许表单提交 |
| `allow-popups` | 允许弹窗 |
| `allow-top-navigation` | 允许顶层导航 |
| `allow-modals` | 允许 alert/confirm 等模态 |

## 13. 动手试试

### 入门版（必做）

1. 用 `iframe` 嵌入一段公开视频（如 B 站分享代码），设置 `title`；
2. 给 `iframe` 加上空 `sandbox`，观察嵌入内容是否还能交互；
3. 对比 `sandbox="allow-scripts"` 与空 `sandbox` 的行为差异。

### 进阶版（选做）

1. 用 `srcdoc` 嵌入一段带样式的自包含 HTML；
2. 父子页面用 `postMessage` 实现“点击按钮同步计数”，并校验来源；
3. 给第三方嵌入配置 `loading="lazy"`，用网络面板确认滚动前不加载。

## 14. 核心知识点

> 一句话记住 iframe：`src` 嵌网页，`title` 不能少；`sandbox` 默认禁，令牌按需开；`postMessage` 通信，来源必须验。

- `iframe` 在页面中嵌入另一个文档，`width`/`height`/`title` 是基础属性；
- `sandbox` 默认禁用脚本、表单、弹窗与同源访问，令牌按需放开；
- `srcdoc` 直接嵌入 HTML 字符串，适合沙箱化的小工具；
- `postMessage` 跨窗口通信必须校验 `event.origin`；
- 每个 iframe 独立消耗资源，非首屏用 `loading="lazy"`；
- 嵌入第三方内容前确认对方允许，并用 CSP `frame-src` 限制来源。

## 15. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 无 `title` | 读屏无法识别框架用途 | 每个 iframe 都写 `title` |
| 完全不加 `sandbox` | 第三方内容拥有全部权限 | 默认 `sandbox`，按需加令牌 |
| `allow-scripts` + `allow-same-origin` 同开 | 嵌入内容可自行移除沙箱 | 只对可信内容这样配置 |
| 消息不校验来源 | 任意页面可伪造消息 | 接收时校验 `event.origin` 白名单 |
| iframe 数量过多 | 内存与进程开销大 | 尽量少用，非首屏懒加载 |
| 用 `<embed>` 嵌 HTML | 语义与安全控制缺失 | HTML 嵌入用 iframe |

## 16. 扩展学习

- 通信进阶：`html5/028-CrossDocumentCommunication` 全面掌握 `postMessage`；
- 安全：CSP 的 `frame-src` 与 `object-src` 指令（见 `css/` 或安全模块）；
- 微前端：`html5/018-WebComponentsPWADevelopment` 对比 iframe 与 Web Components；
- 性能：`html5/031-CriticalRenderingPathAndResourceLoading` 中第三方嵌入对 LCP 的影响；
- 权限策略：MDN Permissions Policy 文档了解 `allow` 的完整取值。
