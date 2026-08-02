---
order: 59
title: progress与meter
module: html5
category: HTML5
difficulty: beginner
description: progress与meter
author: fanquanpp
updated: '2026-08-01'
related:
  - html5/SVG矢量图形
  - html5/嵌入式内容
  - html5/WebComponents与PWA开发
  - html5/拖拽API
prerequisites:
  - html5/概述与核心特性
---
## 1. progress 元素

```html
<progress>加载中...</progress> <progress value="70" max="100">70%</progress>
```

| 属性    | 说明   | 默认值 |
| ------- | ------ | ------ |
| `value` | 当前值 | 0      |
| `max`   | 最大值 | 1      |

```javascript
const progress = document.querySelector('progress');
progress.value = 0.5;
console.log(progress.position); // 0.5
```

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

## 2. meter 元素

```html
<meter value="0.7" min="0" max="1">70%</meter>
<meter value="85" min="0" max="100" low="60" high="90" optimum="80">85分</meter>
```

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
## progress 进度条

**progress 元素**
`<progress [value="<当前值>"] [max="<最大值>"]>[回退内容]</progress>`
```html
<!-- 不确定进度(加载中) -->
<progress>加载中...</progress>

<!-- 确定进度 -->
<progress value="70" max="100">70%</progress>

<!-- 默认 max=1 -->
<progress value="0.5"></progress>
```

| 属性    | 说明     | 默认值 |
| ------- | -------- | ------ |
| `value` | 当前值   | 0      |
| `max`   | 最大值   | 1      |

**JavaScript 操作**
```javascript
const progress = document.querySelector('progress');

// 设置值
progress.value = 0.5;
progress.max = 200;

// 读取属性
console.log(progress.value);     // 当前值
console.log(progress.max);       // 最大值
console.log(progress.position);  // 比例(value/max)

// 模拟加载
let value = 0;
const timer = setInterval(() => {
  value += 0.1;
  progress.value = value;
  if (value >= 1) {
    clearInterval(timer);
    console.log('加载完成');
  }
}, 100);
```

---

## progress 自定义样式

**CSS 伪元素样式**
```css
/* WebKit 内核(Chrome、Safari) */
progress::-webkit-progress-bar {
  background: #e0e0e0;
  border-radius: 10px;
  height: 20px;
}

progress::-webkit-progress-value {
  background: linear-gradient(to right, #4caf50, #8bc34a);
  border-radius: 10px;
  transition: width 0.3s;
}

/* Firefox */
progress::-moz-progress-bar {
  background: #4caf50;
  border-radius: 10px;
}

/* 进度条本身 */
progress {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 20px;
  border: none;
}
```

---

## meter 度量条

**meter 元素**
`<meter value="<当前值>" [min] [max] [low] [high] [optimum]>[回退内容]</meter>`
```html
<!-- 简单度量 -->
<meter value="0.7" min="0" max="1">70%</meter>

<!-- 带区间划分 -->
<meter value="85" min="0" max="100" low="60" high="90" optimum="80">85 分</meter>

<!-- 磁盘使用量 -->
<meter value="650" min="0" max="1000" low="500" high="800" optimum="300">
  650 GB / 1000 GB
</meter>
```

| 属性      | 说明           | 默认值 |
| --------- | -------------- | ------ |
| `value`   | 当前值(必需)   | 0      |
| `min`     | 最小值         | 0      |
| `max`     | 最大值         | 1      |
| `low`     | 低值区间边界   | min    |
| `high`    | 高值区间边界   | max    |
| `optimum` | 最优值         | -      |

**区间划分规则**
```
min          low          high          max
 |-----------|------------|-------------|
   低值区间     中值区间       高值区间
```

颜色规则:optimum 所在区间为绿色,远离 optimum 为黄色/红色。

| optimum 位置 | value 在低区间 | value 在中区间 | value 在高区间 |
| ------------ | -------------- | -------------- | -------------- |
| 低区间       | 绿色           | 黄色           | 红色           |
| 中区间       | 黄色           | 绿色           | 黄色           |
| 高区间       | 红色           | 黄色           | 绿色           |

---

## meter 自定义样式

**CSS 伪元素样式**
```css
meter {
  -webkit-appearance: none;
  appearance: none;
  width: 100%;
  height: 20px;
}

/* WebKit 内核 */
meter::-webkit-meter-bar {
  background: #e0e0e0;
  border-radius: 10px;
}

/* 最优值(绿色) */
meter::-webkit-meter-optimum-value {
  background: #4caf50;
  border-radius: 10px;
}

/* 次优值(黄色) */
meter::-webkit-meter-suboptimum-value {
  background: #ff9800;
  border-radius: 10px;
}

/* 较差值(红色) */
meter::-webkit-meter-even-less-good-value {
  background: #f44336;
  border-radius: 10px;
}

/* Firefox */
meter::-moz-meter-bar {
  background: #4caf50;
}
```

---

## JavaScript 操作 meter

**属性读写**
```javascript
const meter = document.querySelector('meter');

// 读取
console.log(meter.value);     // 当前值
console.log(meter.min);       // 最小值
console.log(meter.max);       // 最大值
console.log(meter.low);       // 低值边界
console.log(meter.high);      // 高值边界
console.log(meter.optimum);   // 最优值

// 设置
meter.value = 75;
meter.min = 0;
meter.max = 100;
meter.low = 40;
meter.high = 80;
meter.optimum = 60;
```

---

## 应用场景示例

**文件上传进度**
```html
<progress id="uploadProgress" value="0" max="100">0%</progress>
<span id="progressText">0%</span>

<script>
  const progress = document.getElementById('uploadProgress');
  const progressText = document.getElementById('progressText');

  function uploadFile(file) {
    const xhr = new XMLHttpRequest();
    xhr.upload.addEventListener('progress', (e) => {
      if (e.lengthComputable) {
        const percent = (e.loaded / e.total) * 100;
        progress.value = percent;
        progressText.textContent = Math.round(percent) + '%';
      }
    });
    xhr.open('POST', '/upload');
    xhr.send(file);
  }
</script>
```

**评分显示**
```html
<!-- 评分 -->
<meter value="4.5" min="0" max="5" low="2" high="4" optimum="5">4.5 / 5</meter>

<!-- 密码强度 -->
<meter id="passwordStrength" value="0" min="0" max="100" low="40" high="70" optimum="100"></meter>

<script>
  function checkStrength(password) {
    let score = 0;
    if (password.length >= 8) score += 25;
    if (/[A-Z]/.test(password)) score += 25;
    if (/[0-9]/.test(password)) score += 25;
    if (/[^a-zA-Z0-9]/.test(password)) score += 25;
    document.getElementById('passwordStrength').value = score;
  }
</script>
```

**电池电量**
```html
<!-- 电池电量(配合 Battery API) -->
<meter id="battery" value="0.75" min="0" max="1" low="0.2" high="0.5" optimum="1">
  75%
</meter>

<script>
  navigator.getBattery().then((battery) => {
    const meter = document.getElementById('battery');
    function update() {
      meter.value = battery.level;
    }
    update();
    battery.addEventListener('levelchange', update);
  });
</script>
```

## 延伸阅读
HTML 列表与链接精讲，见 006-html5/011-List 与 012-LinkageAnchor 文档。
CSS 样式与布局，见 007-css 模块。
JavaScript DOM 操作，见 008-javascript 模块。
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
