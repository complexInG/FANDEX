---
order: 140
title: 音频与视频
module: 'html5'
category: 前端技术
difficulty: intermediate
description: audio、video、source、track字幕
author: fanquanpp
updated: '2026-08-02'
related:
  - 'html5/012-LinkageAnchor'
  - 'html5/013-ImageResponsiveImage'
  - 'html5/015-SVG'
  - 'html5/016-EmbeddedContent'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 直觉：网页里的“播放器”从哪来？

在网页上听歌、看视频，不需要安装任何插件——`<audio>` 和 `<video>` 就是浏览器自带的播放器。它们像一个“插座”，`src` 或 `<source>` 是插头，格式选对了就能播。

为什么要写多个 `<source>`？因为不同浏览器支持的格式不同：MP4 覆盖最广（所有浏览器都能播），WebM 体积更小（Chrome/Firefox 优先），OGG 是 Firefox 的备选。写多个 `<source>` 就是让浏览器自己挑一个它能播的，保证所有用户都能正常播放。

## 1. audio 元素

```html
<audio src="music.mp3" controls></audio>
<audio controls>
  <source src="music.mp3" type="audio/mpeg" />
  <source src="music.ogg" type="audio/ogg" />
</audio>
```

**讲解：**

- `controls` 显示原生控制条，不写则页面静默播放（需脚本控制）；
- `autoplay` 通常会被浏览器拦截，静音（`muted`）或用户手势后才允许；
- 推荐写 `<source>` 多格式降级，而不是只写 `src`。

| 属性       | 说明                     |
| ---------- | ------------------------ |
| `controls` | 显示播放控件             |
| `autoplay` | 自动播放（需配合 muted） |
| `loop`     | 循环播放                 |
| `muted`    | 静音                     |
| `preload`  | none/metadata/auto       |

```javascript
const audio = document.querySelector('audio');
audio.play();
audio.pause();
audio.currentTime = 30;
audio.volume = 0.5;
```

**讲解：**

- `play()`/`pause()` 控制播放，`currentTime` 跳转位置（单位秒）；
- `volume` 取值 0-1，`muted` 是独立于音量的静音开关；
- 自动播放被拦截时，`play()` 返回的 Promise 会 reject，需用 `.catch` 处理。

## 2. video 元素

```html
<video controls width="640" height="360" poster="cover.jpg" playsinline>
  <source src="movie.mp4" type="video/mp4" />
  <source src="movie.webm" type="video/webm" />
</video>
```

**讲解：**

- `width`/`height` 预留布局空间，`poster` 是加载前的封面；
- `playsinline` 让视频在 iOS 上内联播放而不是全屏；
- 与音频相同，多个 `<source>` 提供格式降级。

```javascript
const video = document.querySelector('video');
await video.play();
video.requestFullscreen();
await video.requestPictureInPicture();
```

**讲解：**

- `requestFullscreen()` 进入全屏，返回 Promise；
- `requestPictureInPicture()` 开启画中画（小窗悬浮），同样返回 Promise；
- 两者都必须在用户手势（点击）触发，否则浏览器拒绝。

## 3. track 字幕

```vtt
WEBVTT

00:00:01.000 --> 00:00:04.000
欢迎观看本教程

00:00:05.000 --> 00:00:08.000
今天我们学习 HTML5 视频
```

**讲解：**

- WebVTT 的格式是“时间段 --> 时间段”加字幕文本，空行分隔；
- 时间格式为“时:分:秒.毫秒”，必须精确到毫秒；
- 这是纯文本字幕文件，不需要额外工具即可编写。

```html
<video controls>
  <source src="movie.mp4" type="video/mp4" />
  <track kind="subtitles" src="subs/zh.vtt" srclang="zh" label="中文" />
  <track kind="subtitles" src="subs/en.vtt" srclang="en" label="English" default />
</video>
```

**讲解：**

- `<track>` 必须放在 `<source>` 之后，`kind` 决定字幕类型；
- `srclang` 标注语言，`label` 是用户在字幕菜单里看到的名字；
- `default` 指定默认启用的字幕轨，多语言时通常默认母语。

| kind 值     | 说明             |
| ----------- | ---------------- |
| `subtitles` | 字幕（翻译）     |
| `captions`  | 说明文字（听障） |
| `chapters`  | 章节标题         |

## 4. 自动播放策略

| 条件       | 是否允许自动播放 |
| ---------- | ---------------- |
| 有声视频   | 不允许           |
| 静音视频   | 允许             |
| 用户已交互 | 允许             |

**讲解：** 自动播放限制的目的是防止网页“未经同意出声”。静音播放不打扰用户，所以允许；一旦用户点击过页面（有交互），浏览器也视为已授权。

## 5. 进阶知识点

### 5.1 媒体事件

```javascript
const video = document.querySelector('video');

video.addEventListener('loadedmetadata', () => {
  console.log('时长:', video.duration);
});

video.addEventListener('timeupdate', () => {
  console.log('播放位置:', video.currentTime);
});

video.addEventListener('ended', () => {
  console.log('播放结束');
});
```

**讲解：**

- `loadedmetadata` 在时长、尺寸等元数据就绪后触发，此时才能安全读取 `duration`；
- `timeupdate` 在播放过程中高频触发，适合同步进度条；
- `ended` 表示播放到结尾，可在这里实现“自动播放下一个”等逻辑。

| 事件 | 触发时机 |
| --- | --- |
| `loadedmetadata` | 元数据加载完成 |
| `timeupdate` | 播放位置更新 |
| `play`/`pause` | 开始/暂停播放 |
| `ended` | 播放结束 |
| `error` | 资源加载失败 |

## 6. 动手试试

### 入门版（必做）

1. 用 `<video controls>` 嵌入一段本地视频，加上 `poster` 封面；
2. 给页面加一段背景音乐，用 `<audio controls>` 播放；
3. 做一个中文字幕文件（WebVTT），用 `<track>` 挂到视频上并验证显示。

### 进阶版（选做）

1. 用 JS 实现自定义播放按钮：播放/暂停、进度条、音量；
2. 监听 `timeupdate` 把进度同步到页面上的进度条；
3. 给视频加“画中画”按钮，点击后 `requestPictureInPicture()`。

## 7. 核心知识点

> 一句话记住音视频：`audio` 听声、`video` 看画，多个 `source` 保兼容；`controls` 给控件，`autoplay` 需静音，字幕用 `track`。

- `<audio>`/`<video>` 是浏览器原生播放器，无需插件；
- 多个 `<source>` 按浏览器支持顺序降级（MP4 最稳）；
- `controls`/`autoplay`/`muted`/`loop`/`poster`/`preload` 是核心属性；
- 播放控制 API：`play()`/`pause()`/`currentTime`/`volume`；
- 自动播放规则：有声需要用户手势，静音允许；
- 字幕用 WebVTT + `<track>`，`kind` 区分字幕与说明文字。

## 8. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 自动播放被拦截 | 有声视频直接 `autoplay` 无效 | 静音播放或等用户手势再 `play()` |
| 只有一种格式 | 部分浏览器无法播放 | 提供 MP4 + WebM 多格式 |
| 缺少字幕 | 听障用户与嘈杂环境无法观看 | 添加 `<track kind="captions">` |
| 无 `poster` | 视频加载前一片黑 | 设置封面图并预留尺寸 |
| `play()` 未处理失败 | 拦截时出现未捕获的 Promise 错误 | `.catch()` 处理或 `try/catch` |
| 视频撑爆布局 | 宽高固定导致移动端溢出 | `max-width: 100%` 或按容器自适应 |

## 9. 扩展学习

- 完整控制：`html5/006-HTML5MultimediaCanvasDrawing` 中自定义播放器与媒体 API；
- 音频进阶：Web Audio API 节点图与音频可视化；
- 性能：`html5/031-CriticalRenderingPathAndResourceLoading` 媒体预加载策略；
- 无障碍：`html5/004-Accessibility` 中媒体替代文本与字幕规范；
- 直播流：`html5/024-WebSocket` 与 MSE（Media Source Extensions）。
