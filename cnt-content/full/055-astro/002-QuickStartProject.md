---
order: 2
title: Astro 项目创建与目录结构
module: astro
category: Astro
difficulty: beginner
description: 'Astro 项目初始化：create astro、目录结构与配置文件'
author: fanquanpp
updated: '2026-08-01'
related:
  - astro/003-PagesRouting
  - astro/004-ComponentsProps
prerequisites:
  - html5/003-SemanticTag
---
## 1. 环境准备

开始前需要安装 Node.js 20.14 及以上版本（Astro 6+ 要求 Node.js 22 及以上）。安装完成后在终端验证：

```bash
node -v
npm -v
```

讲解：`node -v` 输出 Node.js 版本号（如 v22.x），`npm -v` 输出包管理器版本。两者都正常输出即环境就绪。npm 随 Node.js 一同安装，不需要单独配置。

## 2. 创建项目：npm create astro

### 2.1 交互式创建

在空目录中执行创建命令：

```bash
npm create astro@latest
```

讲解：`npm create astro` 是 `npm init astro` 的简写，`@latest` 保证拉取最新版本（当前为 Astro 7）。命令会进入交互流程：填写项目名、选择模板（Baseline 空白模板 / Blog 博客模板 / Docs 文档站模板等）、询问是否安装依赖、是否初始化 Git。

### 2.2 自动化创建（跳过交互）

```bash
npm create astro@latest my-site -- --template minimal --yes
```

讲解：`--template minimal` 指定最小模板，`--yes` 跳过全部交互提示，适合脚本与 CI 场景。常用模板：`baseline`（空白）、`minimal`（最小）、`blog`（博客）、`docs`（文档站）、`portfolio`（作品集）。

### 2.3 启动开发服务器

```bash
cd my-site
npm install
npm run dev
```

讲解：`npm install` 安装依赖，`npm run dev` 启动开发服务器，默认监听 `http://localhost:4321`。开发模式具备热更新：修改 `src` 下的文件，浏览器即时刷新。`Ctrl+C` 停止服务器。

## 3. 目录结构

创建完成后项目结构如下：

```text
my-site/
  src/
    pages/          # 路由目录：每个 .astro/.md 文件生成一个页面
      index.astro   # 对应首页 /
    components/     # 组件目录（可自行创建）
    layouts/        # 布局组件目录（可自行创建）
    styles/         # 全局样式目录（可自行创建）
    content.config.ts  # 内容集合配置（用到内容集合时创建）
  public/           # 静态资源：favicon.svg、robots.txt 等，原样拷贝到 dist
  astro.config.mjs  # Astro 配置文件
  package.json      # 依赖与脚本
  tsconfig.json     # TypeScript 配置（Astro 提供严格模式扩展）
  README.md
```

讲解：`src/` 是源码目录，只有 `pages/` 是必须的，其余目录按需创建。`public/` 中的文件不经过任何处理，直接拷贝到构建输出目录的根路径下（如 `public/favicon.svg` 通过 `/favicon.svg` 访问）。

## 4. 核心配置文件

### 4.1 astro.config.mjs

```js
// astro.config.mjs
import { defineConfig } from 'astro/config'

export default defineConfig({
  site: 'https://example.com',   // 站点最终部署地址，生成 sitemap 必需
  output: 'static',              // 输出模式：static（默认）/ server（SSR）/ hybrid
  compressHTML: true,            // 构建时压缩 HTML 空白
  markdown: {
    shikiConfig: { theme: 'github-dark' }, // 代码高亮主题
  },
})
```

讲解：`defineConfig` 提供类型提示与配置校验。`site` 影响规范链接、sitemap 与 OG 图片的生成；`output` 决定静态构建还是服务端渲染，本文按默认 `static` 理解即可。

### 4.2 package.json 脚本

```json
{
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro"
  }
}
```

讲解：四个脚本对应四个核心命令：`astro dev` 开发服务器；`astro build` 生产构建，输出到 `dist/`；`astro preview` 本地预览构建产物；`astro` 暴露 CLI 供 `npx astro add` 添加集成、`npx astro check` 类型检查等使用。

## 5. 第一个页面

打开 `src/pages/index.astro`：

```astro
---
// frontmatter：构建期执行的服务端代码
const title = '我的第一个 Astro 站点'
---

<html lang="zh-CN">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title}</title>
  </head>
  <body>
    <h1>{title}</h1>
    <p>这段内容会被直接渲染为静态 HTML，无需任何客户端 JavaScript。</p>
  </body>
</html>
```

讲解：`---` 包裹的部分称为 frontmatter，在构建期于服务端执行，可写变量、导入模块、读取文件，但不会发送到浏览器；模板部分用 `{表达式}` 语法输出变量的值。这是 Astro 组件最核心的语法，后续所有文档都建立在这一结构之上。

## 6. 常用命令速查

| 命令 | 作用 |
| --- | --- |
| `npm run dev` | 启动开发服务器（HMR 热更新） |
| `npm run build` | 生产构建，输出 `dist/` |
| `npm run preview` | 本地预览构建产物 |
| `npx astro add react` | 添加官方集成（React、Tailwind、MDX 等） |
| `npx astro check` | 运行类型与语法检查 |
| `npx astro info` | 输出环境诊断信息 |

## 7. 参考资源

Astro 安装指南：https://docs.astro.build/zh-cn/install-and-setup/

Astro 配置参考：https://docs.astro.build/zh-cn/reference/configuration-reference/

Astro 项目结构说明：https://docs.astro.build/zh-cn/basics/project-structure/

Astro 模板市场：https://astro.build/themes/
