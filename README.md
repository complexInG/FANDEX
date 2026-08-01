# FANDEX

FANDEX 是一个面向零基础学习者的计算机科学自学平台，内容覆盖工具链、前端、后端、数据库、计算机科学、数学与云基础设施等领域，以 Markdown 教材库为核心，静态生成多端应用。

## 技术栈

- monorepo：pnpm 11 workspace（catalog 统一依赖版本）
- web：Astro 7 + React 19 + TypeScript + Tailwind CSS 4，SSG 部署至 GitHub Pages
- desktop / android：占位目录，规划中（Tauri 2 / 原生）

## 目录结构

- `app-web`：Web 端应用（Astro 页面、React 岛屿、样式、服务层）
- `app-desktop` / `app-android`：桌面端与移动端占位目录
- `cnt-content`：内容库（`full` 为全量内容源，`mobile` 为归档子集）
- `shd-shared`：共享层（模块元数据、设计令牌、工具函数、统一资产）
- `tls-tools`：工具链（manifest 生成、ID 注册表、内容扫描、命名校验）
- `thd-third-party`：第三方组件/插件占位目录
- `tools`：本地工作笔记（非 workspace 包）

## 常用命令

```bash
pnpm install                # 安装全部 workspace 依赖
pnpm dev:web                # 启动 Web 开发服务器（端口 3000）
pnpm build:web              # 构建 Web 端并清理中间产物
pnpm typecheck              # 全仓类型检查
pnpm --filter @fandex/web qa  # 发布前质量门禁检查
pnpm generate-manifest      # 生成内容索引 manifest
pnpm allocate-id            # 分配模块/文档 ID
```

## 内容约定

- 文档存放于 `cnt-content/full`，目录命名 `NNN-module-id`，文档命名 `NNN-EnglishName.md`
- frontmatter 必须包含 `title` / `module` / `order` 等字段，由 `content.config.ts` 的 Zod schema 严格校验
- 站内链接禁止使用根路径形式（`/xxx/`），示例路径一律写成行内代码
- 模块元数据统一维护在 `shd-shared/metadata/modules.json`，新增模块需同步 ID 注册表

## 许可

MIT License
