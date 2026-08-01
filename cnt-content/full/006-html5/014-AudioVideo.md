---
order: 56
title: 音频与视频
module: html5
category: HTML5
difficulty: intermediate
description: audio、video、source、track字幕
author: fanquanpp
updated: '2026-08-01'
related:
  - html5/链接与锚点
  - html5/图像与响应式图片
  - html5/SVG矢量图形
  - html5/嵌入式内容
prerequisites:
  - html5/概述与核心特性
---

# 音频与视频 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 1. audio 元素

```html
<audio src="music.mp3" controls></audio>
<audio controls>
  <source src="music.mp3" type="audio/mpeg" />
  <source src="music.ogg" type="audio/ogg" />
</audio>
```

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

## 2. video 元素

```html
<video controls width="640" height="360" poster="cover.jpg" playsinline>
  <source src="movie.mp4" type="video/mp4" />
  <source src="movie.webm" type="video/webm" />
</video>
```

```javascript
const video = document.querySelector('video');
await video.play();
video.requestFullscreen();
await video.requestPictureInPicture();
```

## 3. track 字幕

```vtt
WEBVTT

00:00:01.000 --> 00:00:04.000
欢迎观看本教程

00:00:05.000 --> 00:00:08.000
今天我们学习 HTML5 视频
```

```html
<video controls>
  <source src="movie.mp4" type="video/mp4" />
  <track kind="subtitles" src="subs/zh.vtt" srclang="zh" label="中文" />
  <track kind="subtitles" src="subs/en.vtt" srclang="en" label="English" default />
</video>
```

| kind 值     | 说明             |
| ----------- | ---------------- |
| `subtitles` | 字幕（翻译）     |
| `captions`  | 说明文字（听障） |
| `chapters`  | 章节标题         |

## 4. 自动播放策略

| 条件       | 是否允许自动播放 |
| ---------- | ---------------- |
| 有声视频   |                  |
| 静音视频   |                  |
| 用户已交互 |                  |
## audio 音频元素

**音频基础**
`<audio src="<URL>" [controls] [autoplay] [loop] [muted] [preload]>[回退内容]</audio>`
```html
<!-- 简单音频 -->
<audio src="music.mp3" controls></audio>

<!-- 多格式回退 -->
<audio controls>
  <source src="music.mp3" type="audio/mpeg" />
  <source src="music.ogg" type="audio/ogg" />
  您的浏览器不支持音频元素。
</audio>
```

| 属性       | 说明                     | 示例                       |
| ---------- | ------------------------ | -------------------------- |
| `src`      | 音频源 URL               | `src="music.mp3"`          |
| `controls` | 显示播放控件             | `controls`                 |
| `autoplay` | 自动播放(需配合 muted)   | `autoplay muted`           |
| `loop`     | 循环播放                 | `loop`                     |
| `muted`    | 静音                     | `muted`                    |
| `preload`  | 预加载 none/metadata/auto| `preload="metadata"`       |

**音频格式**

| 格式   | MIME 类型       | 浏览器支持            |
| ------ | --------------- | --------------------- |
| MP3    | audio/mpeg      | 全部                  |
| OGG    | audio/ogg       | 除 Safari iOS 外      |
| WAV    | audio/wav       | 全部(文件较大)        |
| AAC    | audio/aac       | 全部                  |
| FLAC   | audio/flac      | 除 IE 外              |

---

## video 视频元素

**视频基础**
`<video src="<URL>" [controls] [autoplay] [loop] [muted] [poster="<封面>"] [width] [height] [preload] [playsinline]>[回退内容]</video>`
```html
<!-- 基础视频 -->
<video src="movie.mp4" controls width="640" height="360"></video>

<!-- 完整配置 -->
<video
  controls
  autoplay
  muted
  loop
  poster="cover.jpg"
  width="640"
  height="360"
  playsinline
  preload="metadata"
>
  <source src="movie.mp4" type="video/mp4" />
  <source src="movie.webm" type="video/webm" />
  <track kind="subtitles" src="subs.vtt" srclang="zh" label="中文" default />
  您的浏览器不支持视频元素。
</video>
```

| 属性         | 说明                   | 示例                          |
| ------------ | ---------------------- | ----------------------------- |
| `src`        | 视频源 URL             | `src="movie.mp4"`             |
| `controls`   | 显示控制条             | `controls`                    |
| `autoplay`   | 自动播放               | `autoplay muted`              |
| `muted`      | 静音                   | `muted`                       |
| `loop`       | 循环播放               | `loop`                        |
| `poster`     | 封面图 URL             | `poster="cover.jpg"`          |
| `preload`    | 预加载 none/metadata/auto | `preload="auto"`           |
| `width`      | 宽度                   | `width="640"`                 |
| `height`     | 高度                   | `height="360"`                |
| `playsinline`| 内联播放(防 iOS 全屏)  | `playsinline`                 |
| `controlslist` | 控制条按钮定制       | `controlslist="nodownload"`   |
| `disablepictureinpicture` | 禁用画中画  | `disablepictureinpicture`     |
| `crossorigin`| 跨域设置              | `crossorigin="anonymous"`     |

**视频格式**

| 格式  | MIME 类型   | 视频编码    | 浏览器支持            |
| ----- | ----------- | ----------- | --------------------- |
| MP4   | video/mp4   | H.264       | 全部                  |
| WebM  | video/webm  | VP8/VP9     | 除 Safari 外          |
| OGG   | video/ogg   | Theora      | 除 Safari 外          |
| AV1   | video/mp4   | AV1         | Chrome、Firefox       |
| HLS   | application/vnd.apple.mpegurl | H.264 | Safari 原生,其他需 hls.js |

---

## source 元素

**多源回退**
`<source src="<URL>" type="<MIME>" [media="<媒体查询>"] [sizes] [srcset] />`
```html
<video controls>
  <source src="movie.av1.mp4" type="video/mp4; codecs=av01.0.05M.08" />
  <source src="movie.webm" type="video/webm; codecs=vp9" />
  <source src="movie.h264.mp4" type="video/mp4; codecs=avc1.4d401e" />
  您的浏览器不支持视频。
</video>
```

---

## track 字幕元素

**文本轨道**
`<track kind="<类型>" src="<VTT文件>" srclang="<语言>" label="<标签>" [default] />`
```html
<video controls>
  <source src="movie.mp4" type="video/mp4" />
  <track kind="subtitles" src="subs/zh.vtt" srclang="zh" label="中文" default />
  <track kind="subtitles" src="subs/en.vtt" srclang="en" label="English" />
  <track kind="captions" src="caps/en.vtt" srclang="en" label="English Captions" />
  <track kind="chapters" src="chapters.vtt" srclang="en" label="章节" />
</video>
```

| kind 值       | 说明                       |
| ------------- | -------------------------- |
| `subtitles`   | 字幕(翻译)                 |
| `captions`    | 说明文字(听障,含音效)      |
| `descriptions`| 视频描述(视障)             |
| `chapters`    | 章节标题                   |
| `metadata`    | 元数据(脚本用)             |

**WebVTT 文件格式**
```vtt
WEBVTT

00:00:01.000 --> 00:00:04.000
欢迎观看本教程

00:00:05.000 --> 00:00:08.000
今天我们学习 HTML5 视频

NOTE 这是注释

00:00:09.000 --> 00:00:12.000 align=start position:10%
带样式的字幕
```

---

## JavaScript 控制 API

**HTMLMediaElement API**
```javascript
const video = document.querySelector('video');
const audio = document.querySelector('audio');

// 播放控制
video.play();              // 播放(返回 Promise)
video.pause();             // 暂停
video.load();              // 重新加载

// 属性
video.currentTime;         // 当前播放时间(秒)
video.duration;            // 总时长(秒)
video.volume;              // 音量 0-1
video.muted;               // 是否静音
video.playbackRate;        // 播放速度(1.0 正常)
video.preservesPitch;      // 保持音调
video.loop;                // 是否循环
video.autoplay;            // 是否自动播放
video.controls;            // 是否显示控件
video.paused;              // 是否暂停
video.ended;               // 是否播放结束
video.seeking;             // 是否在跳转
video.buffered;            // 已缓冲区间
video.readyState;          // 就绪状态 0-4
video.networkState;        // 网络状态
video.error;               // 错误对象

// 设置
video.currentTime = 30;    // 跳转到 30 秒
video.volume = 0.5;        // 音量 50%
video.playbackRate = 1.5;  // 1.5 倍速
video.muted = true;        // 静音
```

**特殊 API**
```javascript
// 全屏
await video.requestFullscreen();
await document.exitFullscreen();

// 画中画
await video.requestPictureInPicture();
await document.exitPictureInPicture();

// 截图(需同源或 crossorigin)
const canvas = document.createElement('canvas');
canvas.width = video.videoWidth;
canvas.height = video.videoHeight;
canvas.getContext('2d').drawImage(video, 0, 0);
const dataURL = canvas.toDataURL('image/png');

// 录制(MediaRecorder)
const stream = video.captureStream();
const recorder = new MediaRecorder(stream, { mimeType: 'video/webm' });
```

---

## 媒体事件

**媒体事件监听**
`element.addEventListener('<事件>', handler)`
```javascript
video.addEventListener('loadstart', () => console.log('开始加载'));
video.addEventListener('loadedmetadata', () => console.log('元数据已加载'));
video.addEventListener('loadeddata', () => console.log('数据已加载'));
video.addEventListener('canplay', () => console.log('可以播放'));
video.addEventListener('canplaythrough', () => console.log('可流畅播放'));
video.addEventListener('play', () => console.log('开始播放'));
video.addEventListener('playing', () => console.log('播放中'));
video.addEventListener('pause', () => console.log('已暂停'));
video.addEventListener('ended', () => console.log('播放结束'));
video.addEventListener('timeupdate', () => console.log(video.currentTime));
video.addEventListener('progress', () => console.log('加载进度'));
video.addEventListener('volumechange', () => console.log('音量变化'));
video.addEventListener('ratechange', () => console.log('速度变化'));
video.addEventListener('seeking', () => console.log('跳转中'));
video.addEventListener('seeked', () => console.log('跳转完成'));
video.addEventListener('waiting', () => console.log('缓冲中'));
video.addEventListener('error', (e) => console.log('错误', video.error));
```

---

## 自动播放策略

| 条件               | 是否允许自动播放 |
| ------------------ | ---------------- |
| 有声视频(默认)     | 通常被禁止       |
| 静音视频 muted     | 允许             |
| 用户已与页面交互   | 允许             |
| 已被用户授权       | 允许             |

```javascript
// 安全的自动播放
const video = document.querySelector('video');
video.muted = true;
video.play().then(() => {
  console.log('自动播放成功');
}).catch((err) => {
  console.log('自动播放被拒绝,需要用户交互');
  document.body.addEventListener('click', () => {
    video.play();
  }, { once: true });
});
```

## 参考文献



WHATWG HTML Living Standard：https://html.spec.whatwg.org/
MDN HTML 文档：https://developer.mozilla.org/zh-CN/docs/Web/HTML
W3C Markup Validation Service：https://validator.w3.org/
WebAIM 可访问性指南：https://webaim.org/

## 延伸阅读



HTML 列表与链接精讲，见 006-html5/011-List 与 012-LinkageAnchor 文档。
CSS 样式与布局，见 007-css 模块。
JavaScript DOM 操作，见 008-javascript 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 HTML/CSS 课程。

## 深度专题扩展


以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 HTML 解析与 DOM 树

浏览器解析 HTML 时先 tokenize 再建树；解析器对错误标记有容错规则（错误恢复算法）。
DOM 是内存中的树结构：元素节点、文本节点、属性；document.querySelector 沿树查找。
渲染流程：HTML -> DOM，CSS -> CSSOM，合并为渲染树，布局与绘制；理解流程可定位性能瓶颈。
脚本与解析：defer 延后执行，async 异步执行，模块脚本默认 defer 语义。

### 13.2 表单校验与无障碍

原生校验：required、pattern、min/max、type 约束；novalidate 可关闭，交由 JS 自定义。
校验 UI：:invalid/:valid 伪类样式；aria-invalid 标记错误；错误信息用 aria-describedby 关联。
键盘可达：所有交互元素可 Tab 聚焦，焦点可见，弹层焦点管理（trap）。
屏幕阅读器测试：NVDA/VoiceOver 实际朗读验证语义。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| HTML5 概述与核心特性 | 001-HTML5OverviewCoreFeature | 本文的前置基础 |
| HTML5 基础标签与全局属性 | 002-HTML5BasicTagGlobalAttribute | 本文的前置基础 |
| 语义化标签 | 003-SemanticTag | 本文的并列主题 |
| 无障碍访问 | 004-Accessibility | 本文的并列主题 |
| HTML5 表单与验证 | 005-HTML5FormValidation | 本文的并列主题 |
| HTML5 多媒体与 Canvas 绘图 | 006-HTML5MultimediaCanvasDrawing | 本文的并列主题 |
| 文档类型声明 | 007-DocTypeDeclaration | 本文的并列主题 |
| HTML5 离线存储与 Web API | 008-HTML5OfflineStorageWebAPI | 本文的并列主题 |
| 元数据与字符编码 | 009-MetadataCharacterEncoding | 本文的并列主题 |
| 文本语义 | 010-TextSemantic | 本文的并列主题 |
| 列表 | 011-List | 本文的并列主题 |
| 链接与锚点 | 012-LinkageAnchor | 本文的并列主题 |
| 图像与响应式图片 | 013-ImageResponsiveImage | 本文的并列主题 |
| 音频与视频 | 014-AudioVideo | 本文自身 |
| SVG | 015-SVG | 本文的并列主题 |
| 嵌入式内容 | 016-EmbeddedContent | 本文的并列主题 |
| progress与meter | 017-ProgressMeter | 本文的并列主题 |
| Web Components 与 PWA 开发 | 018-WebComponentsPWADevelopment | 本文的并列主题 |
| 拖拽API | 019-DragAPI | 本文的并列主题 |
| 地理位置定位 | 020-Geolocation | 本文的并列主题 |
| Web-Workers | 021-WebWorkers | 本文的并列主题 |
| Service-Worker与PWA | 022-ServiceWorkerPWA | 本文的并列主题 |
| History-API | 023-HistoryAPI | 本文的并列主题 |
| WebSocket | 024-WebSocket | 本文的并列主题 |
| WebRTC | 025-WebRTC | 本文的并列主题 |
| 微数据与JSON-LD | 026-MicrodataJSONLD | 本文的并列主题 |
| 自定义数据属性 | 027-CustomDataAttribute | 本文的并列主题 |
| 跨文档通信 | 028-CrossDocumentCommunication | 本文的并列主题 |
| 视口配置与移动优先 | 029-ViewportConfigMobileFirst | 本文的并列主题 |
| HTML5 项目示例：交互式表单应用 | 030-HTML5ProjectExampleInteractiveFormApplication | 本文的综合应用 |
