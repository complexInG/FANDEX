---
order: 170
title: progress与meter
module: 'html5'
category: 前端技术
difficulty: beginner
description: progress与meter
author: fanquanpp
updated: '2026-08-02'
related:
  - 'html5/015-SVG'
  - 'html5/016-EmbeddedContent'
  - 'html5/018-WebComponentsPWADevelopment'
  - 'html5/019-DragAPI'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 直觉：进度条和度量条不是一回事

- `<progress>` 是“任务进度”：下载到 70%，加载完成 100%——它回答“完成了多少”；
- `<meter>` 是“数值位置”：电量 70%、评分 85 分——它回答“这个值处于什么水平”。

一个看“过程”，一个看“状态”。写代码前先想清楚语义，选错标签会让读屏用户听到错误含义。

## 1. progress 元素

```html
<progress>加载中...</progress> <progress value="70" max="100">70%</progress>
```

**讲解：**

- 不写 `value` 时是“不确定进度”，显示为流动动画（如“加载中”）；
- 写了 `value`/`max` 就变成确定进度，`value / max` 是完成比例；
- 标签之间的文字是给旧浏览器与读屏用户的回退内容。

| 属性    | 说明   | 默认值 |
| ------- | ------ | ------ |
| `value` | 当前值 | 0      |
| `max`   | 最大值 | 1      |

```javascript
const progress = document.querySelector('progress');
progress.value = 0.5;
console.log(progress.position); // 0.5
```

**讲解：**

- `value`/`max` 是数字属性，直接赋值即可更新进度条；
- `position` 是只读属性，返回 `value / max` 的比例；
- 模拟加载时用 `setInterval` 逐步递增 `value`，完成后 `clearInterval` 停止。

### 自定义样式

```css
progress::-webkit-progress-bar {
  background: #e0e0e0;
  border-radius: 10px;
}
progress::-webkit-progress-value {
  background: #4caf50;
  border-radius: 10px;
}
progress::-moz-progress-bar {
  background: #4caf50;
}
```

**讲解：**

- WebKit/Blink 浏览器用 `::-webkit-progress-bar` 与 `::-webkit-progress-value` 定制轨道和填充；
- Firefox 用 `::-moz-progress-bar`；
- 两条规则都要写，否则 Firefox 或 Chrome 中会有一边不生效。

## 2. meter 元素

```html
<meter value="0.7" min="0" max="1">70%</meter>
<meter value="85" min="0" max="100" low="60" high="90" optimum="80">85分</meter>
```

**讲解：**

- `value` 是当前值，`min`/`max` 定义刻度范围；
- `low`/`high` 划分低、中、高三个区间，`optimum` 声明“最佳值”在哪；
- 浏览器根据值与最优值的距离自动显示绿/黄/红，无需写脚本。

| 属性      | 说明           | 默认值 |
| --------- | -------------- | ------ |
| `value`   | 当前值（必需） | 0      |
| `min`     | 最小值         | 0      |
| `max`     | 最大值         | 1      |
| `low`     | 低值区间边界   | min    |
| `high`    | 高值区间边界   | max    |
| `optimum` | 最优值         | —      |

### 区间划分

```
min          low          high          max
 |-----------|------------|-------------|
   低值区间     中值区间       高值区间
```

颜色规则基于 optimum 所在区间：optimum 所在区间为绿色，远离为黄色/红色。

**讲解：** 颜色是“自动语义”：`optimum` 所在的区间显示绿色，越远离越偏黄、红。注意 `meter` 只适合“已知范围”的数值（电量、评分），任务进度请用 `progress`。

```css
meter::-webkit-meter-optimum-value {
  background: #4caf50;
}
meter::-webkit-meter-suboptimum-value {
  background: #ff9800;
}
meter::-webkit-meter-even-less-good-value {
  background: #f44336;
}
```

**讲解：**

- `::-webkit-meter-optimum-value` 控制绿色段（最优区间）；
- `::-webkit-meter-suboptimum-value` 控制黄色段，`::-webkit-meter-even-less-good-value` 控制红色段；
- 自定义样式时不要覆盖掉颜色的“语义”，否则用户会失去直观判断。

## 3. 动手试试

### 入门版（必做）

1. 用 `<progress>` 做一个“文件下载”进度条，用 JS 定时把 `value` 从 0 递增到 `max`；
2. 用 `<meter>` 显示“当前电量 70%”，并配置 `low`/`high`/`optimum` 观察颜色变化；
3. 用浏览器检查两个元素的语义：右键查看无障碍树中的角色与名称。

### 进阶版（选做）

1. 给进度条加自定义样式：圆角轨道 + 绿色填充；
2. 做一个“上传中”的不确定进度条（不写 `value`），完成后切换为确定进度；
3. 用 `aria-label` 给进度条补充“下载第 2/5 个文件”等动态描述。

## 4. 核心知识点

> 一句话记住 progress/meter：任务进度用 `progress`，数值状态用 `meter`；`value`/`max` 定比例，`low`/`high`/`optimum` 管颜色。

- `progress` 表示任务完成度：无 `value` 为不确定进度，有 `value`/`max` 为确定进度；
- `meter` 表示数值在刻度区间的位置：`min`/`max`/`low`/`high`/`optimum` 共同决定语义颜色；
- 两者都可被 JavaScript 直接赋值更新，`position` 返回比例；
- 自定义样式需同时覆盖 WebKit 与 Firefox 的伪元素；
- 语义别混用：进度用 `progress`，状态用 `meter`。

## 5. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 用 `meter` 显示进度 | 语义错误，读屏播报成“仪表” | 任务进度改用 `progress` |
| 用 `progress` 显示电量 | 语义错误 | 数值状态改用 `meter` |
| 样式只写 WebKit | Firefox 中样式不生效 | 同时写 `::-moz-*` 伪元素 |
| 覆盖颜色语义 | 用户失去直观判断 | 保留绿/黄/红含义或另加文字说明 |
| 忘记回退文字 | 旧环境无法理解数值 | 标签内写可读文本 |

## 6. 扩展学习

- 无障碍：`html5/004-Accessibility` 中 ARIA 的 `progressbar`/`meter` 角色；
- 动画：`css/017-CSSAnimationTransition` 让进度变化更平滑；
- 组件化：`html5/018-WebComponentsPWADevelopment` 封装自定义进度条；
- 实时更新：`html5/024-WebSocket` 中上传/下载进度的真实数据来源。
