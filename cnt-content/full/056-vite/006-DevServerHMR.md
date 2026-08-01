---
order: 6
title: Vite 开发服务器与 HMR
module: vite
category: Vite
difficulty: intermediate
description: 'Vite dev server：server 配置、代理、host 端口与 HMR 原理及 API'
author: fanquanpp
updated: '2026-08-01'
related:
  - vite/003-ConfigFile
  - vite/002-QuickStart
prerequisites:
  - vite/003-ConfigFile
---
## 1. server 配置总览

`server` 选项控制开发服务器行为，全部通过 `vite.config.ts` 配置：

```ts
// vite.config.ts
import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    port: 5173,           // 指定端口，被占用时自动加 1
    strictPort: false,    // true 时端口被占用直接报错
    host: 'localhost',    // 监听地址，见第 2 节
    open: true,           // 启动后自动打开浏览器
    cors: true,           // 允许跨域访问开发资源
    https: false,         // 需要 https 时配置证书对象
  },
})
```

| 选项 | 默认值 | 说明 |
| --- | --- | --- |
| `port` | `5173` | 开发服务器端口 |
| `strictPort` | `false` | 端口被占用时是否直接失败 |
| `host` | `localhost` | 监听的主机名或 IP |
| `open` | `false` | 启动后自动打开浏览器 |
| `proxy` | 无 | 开发期请求代理（第 3 节） |

讲解：`vite preview`（预览构建产物）使用独立的 `preview` 配置块，语法与 `server` 相同但互不影响，例如 `preview.port` 默认 4173。

## 2. host 与端口

`host` 决定开发服务器监听在哪张网卡上，直接影响局域网内的其他设备能否访问：

```bash
# 仅本机可访问（默认）
pnpm dev --host localhost
# 暴露到局域网，手机/同事可访问
pnpm dev --host 0.0.0.0
```

讲解：默认 `localhost` 下，同一局域网的其他设备访问你的 IP 会失败。改用 `0.0.0.0` 或具体网卡 IP 后，Vite 终端会输出 `Network: http://192.168.x.x:5173/`，其他设备即可访问。注意浏览器对局域网 HTTP 环境的敏感 API（摄像头等）可能要求 HTTPS，可用 `server.https` 自签证书。

## 3. 代理 proxy：解决开发跨域

前后端分离开发时，前端页面访问后端接口必然面临跨域。推荐方案是**开发代理**而不是改后端 CORS：

```ts
// vite.config.ts
export default defineConfig({
  server: {
    proxy: {
      // 前端请求 /api/xxx -> 转发到 http://localhost:8080/xxx
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
      // 简写形式：无 rewrite 需求
      '/socket': 'ws://localhost:3000',
    },
  },
})
```

讲解：`/api` 开头的请求由 dev server 转发到目标地址，浏览器看到的仍是同源请求，从而绕过跨域。`changeOrigin: true` 会把请求头中的 Host 改为目标地址（后端按 Host 鉴权时需要）；`rewrite` 用于路径改写（去掉 `/api` 前缀等）。代理配置基于 http-proxy，支持 ws（WebSocket）。

代理适用的典型场景：

| 场景 | 配置要点 |
| --- | --- |
| 转发 REST API | `target` + `changeOrigin` + `rewrite` |
| 转发 WebSocket | `target` 用 `ws://` 协议 |
| 转发到 HTTPS 后端 | `target` 填 https 地址 + `secure: false`（自签证书时） |

## 4. HMR 原理

HMR（Hot Module Replacement，模块热替换）是 Vite 开发体验的核心：修改代码后**不刷新页面**，只更新被改动的模块。

```text
修改文件 -> dev server 计算受影响模块 -> WebSocket 推送更新消息
         -> 浏览器端执行对应模块的更新逻辑 -> 页面状态保留
```

讲解：关键点在最后一步——框架插件（如 `@vitejs/plugin-react`、`@vitejs/plugin-vue`）实现了组件级的更新逻辑：React 使用 Fast Refresh 保留组件 state，Vue 直接重渲染受影响的组件。没有插件支持的模块会退化为整页刷新（reload）。

模块与 HMR 的关系：

| 模块类型 | 更新方式 |
| --- | --- |
| CSS / SCSS | 样式热替换，无需刷新 |
| React / Vue 组件 | 组件级热更新，状态保留 |
| 普通 JS 模块 | 递归更新依赖它的模块，必要时整页刷新 |

## 5. HMR API：import.meta.hot

不依赖框架时，可在业务模块中手动接入 HMR：

```ts
// counter.ts
let count = 0
export function inc() {
  return ++count
}

// 模块自身声明热更新边界
if (import.meta.hot) {
  import.meta.hot.accept((newModule) => {
    // 新模块加载完成后的处理（可选）
    console.log('counter.ts 已热更新')
  })
}
```

讲解：`import.meta.hot.accept()` 表示"本模块可接受热更新"，接受后模块变化只更新自身。若某模块**不可接受**热更新，Vite 会向上冒泡到最近的 accept 边界，否则整页刷新。常用 API：

| API | 作用 |
| --- | --- |
| `import.meta.hot.accept(deps, cb)` | 接受自身或指定依赖的热更新 |
| `import.meta.hot.dispose(cb)` | 模块被替换前清理副作用（定时器、事件监听） |
| `import.meta.hot.invalidate()` | 使当前模块失效并强制整页刷新 |
| `import.meta.hot.data` | 跨热更新保存模块数据（持久化状态） |

```ts
// 使用 data 保存状态 + dispose 清理资源的完整示例
import.meta.hot.data.count = (import.meta.hot.data.count ?? 0) + 1

if (import.meta.hot) {
  const timer = setInterval(() => {
    console.log('tick', import.meta.hot.data.count)
  }, 1000)

  import.meta.hot.dispose(() => {
    clearInterval(timer)   // 热更新前清理，防止内存泄漏
  })
}
```

讲解：`dispose` 里清理旧模块创建的副作用是防泄漏的关键。框架插件的 HMR 内部正是基于这套 API 实现，日常业务开发几乎不需要手写。

## 6. forwardConsole：日志转发

Vite 8 新增的 `server.forwardConsole`（默认为 `'js'`）会把**浏览器控制台日志转发到终端**，开发调试时无需切换窗口：

```ts
// vite.config.ts
export default defineConfig({
  server: {
    // 'js' | 'all' | 'none'
    // js：转发 console.log/warn/error 等 JS 日志（默认）
    // all：额外转发网络请求等浏览器日志
    // none：关闭转发
    forwardConsole: 'all',
  },
})
```

讲解：开启后，浏览器里 `console.log` 的输出会同步出现在 dev server 的终端，适合排查移动端调试、iframe 内日志等难以直接打开 DevTools 的场景。设为 `'none'` 可关闭，避免日志刷屏。

## 7. 常见陷阱

陷阱一：修改 `vite.config.ts` 或新增插件后 HMR 失效。重启 dev server 即可。

陷阱二：代理不生效。检查请求是否走了代理前缀（`/api`），以及 `rewrite` 是否误删了路径。

陷阱三：端口被占用且 `strictPort: true`。启动报错，换端口或关闭占用进程。

陷阱四：热更新后页面状态丢失。React 组件需安装 `@vitejs/plugin-react` 才能获得 Fast Refresh。

## 8. 参考资源

Vite 服务器选项：https://vite.dev/config/server-options

Vite HMR API：https://vite.dev/guide/api-hmr

Vite 中文文档：https://cn.vite.dev/
