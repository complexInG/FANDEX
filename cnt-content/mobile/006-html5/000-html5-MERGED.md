---
order: 10
title: html5 模块文档合集
module: 'html5'
category: 前端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：006-html5/001-HTML5FormValidation.md ============ -->

# 表单与验证 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 表单容器

**form 元素**
`<form action="<URL>" [method="get|post"] [enctype="<编码>"] [autocomplete="on|off"] [novalidate] [target]></form>`
```html
<!-- 基础表单 -->
<form action="/submit" method="post">
  <input type="text" name="username" />
  <button type="submit">提交</button>
</form>

<!-- 文件上传表单 -->
<form action="/upload" method="post" enctype="multipart/form-data">
  <input type="file" name="avatar" />
</form>

<!-- 禁用原生验证 -->
<form action="/api" method="post" novalidate>...</form>
```

| 属性           | 作用                                |
| -------------- | ----------------------------------- |
| `action`       | 提交目标 URL                        |
| `method`       | HTTP 方法 get/post/dialog           |
| `enctype`      | 编码方式 application/x-www-form-urlencoded / multipart/form-data / text/plain |
| `autocomplete` | 自动补全 on/off                     |
| `novalidate`   | 禁用浏览器原生验证                  |
| `target`       | 提交后响应显示位置                  |
| `accept-charset` | 字符编码                          |

---

## input 输入类型

**文本输入框**
`<input type="text" name="<名称>" [placeholder="<提示>"] [required] [maxlength] [minlength] />`
```html
<!-- 用户名输入框,必填 -->
<input type="text" name="username" placeholder="请输入用户名" required />
```

**密码输入框**
`<input type="password" name="<名称>" [required] [minlength] [pattern] />`
```html
<input type="password" name="password" required minlength="8" />
```

**邮箱输入框**
`<input type="email" name="<名称>" [multiple] [required] />`
```html
<!-- 支持多个邮箱(逗号分隔) -->
<input type="email" name="email" multiple required />
```

**URL 输入框**
`<input type="url" name="<名称>" [required] />`
```html
<input type="url" name="website" placeholder="https://" />
```

**数字输入框**
`<input type="number" name="<名称>" [min] [max] [step] [required] />`
```html
<input type="number" name="age" min="1" max="120" step="1" />
```

**滑块输入**
`<input type="range" name="<名称>" min="<最小>" max="<最大>" [step] [value] />`
```html
<input type="range" name="volume" min="0" max="100" value="50" />
```

**日期时间类型**

| 类型             | 描述               | 示例                                        |
| ---------------- | ------------------ | ------------------------------------------- |
| `date`           | 日期选择器         | `<input type="date" name="birthday">`       |
| `month`          | 月份选择器         | `<input type="month" name="expiry">`        |
| `week`           | 周选择器           | `<input type="week" name="week">`           |
| `time`           | 时间选择器         | `<input type="time" name="meeting">`        |
| `datetime-local` | 本地日期时间       | `<input type="datetime-local" name="event">`|

**其他类型**

| 类型      | 描述               | 示例                                       |
| --------- | ------------------ | ------------------------------------------ |
| `color`   | 颜色选择器         | `<input type="color" name="color">`        |
| `search`  | 搜索框(带清除)     | `<input type="search" name="q">`           |
| `tel`     | 电话(移动端数字键) | `<input type="tel" name="phone">`          |
| `file`    | 文件上传           | `<input type="file" name="avatar">`        |
| `hidden`  | 隐藏字段           | `<input type="hidden" name="id">`          |
| `checkbox`| 复选框             | `<input type="checkbox" name="agree">`     |
| `radio`   | 单选框             | `<input type="radio" name="gender">`       |
| `submit`  | 提交按钮           | `<input type="submit" value="提交">`       |
| `reset`   | 重置按钮           | `<input type="reset" value="重置">`        |
| `button`  | 普通按钮           | `<input type="button" value="点击">`       |
| `image`   | 图像提交按钮       | `<input type="image" src="btn.png">`       |

```html
<!-- 文件上传(限制类型和多选) -->
<input type="file" name="photos" accept="image/*" multiple />

<!-- 颜色选择器 -->
<input type="color" name="favorite" value="#ff0000" />

<!-- 复选框 -->
<label>
  <input type="checkbox" name="subscribe" checked /> 订阅 newsletter
</label>

<!-- 单选框组 -->
<label><input type="radio" name="gender" value="male" /> 男</label>
<label><input type="radio" name="gender" value="female" /> 女</label>
```

---

## 表单增强属性

**input 通用属性**

| 属性           | 作用                       | 示例                                |
| -------------- | -------------------------- | ----------------------------------- |
| `placeholder`  | 占位提示文本               | `placeholder="请输入"`              |
| `required`     | 必填                        | `required`                          |
| `autofocus`    | 自动聚焦                   | `autofocus`                         |
| `autocomplete` | 自动补全                   | `autocomplete="off"`                |
| `pattern`      | 正则验证                   | `pattern="[0-9]{6}"`                |
| `min` / `max`  | 数值/日期范围              | `min="1" max="100"`                 |
| `step`         | 步长                       | `step="0.5"`                        |
| `multiple`     | 多选(email/file)           | `multiple`                          |
| `size`         | 宽度(字符数)               | `size="30"`                         |
| `maxlength`    | 最大字符数                 | `maxlength="50"`                    |
| `minlength`    | 最小字符数                 | `minlength="6"`                     |
| `readonly`     | 只读                       | `readonly`                          |
| `disabled`     | 禁用                       | `disabled`                          |
| `value`        | 默认值                     | `value="default"`                   |
| `list`         | 关联 datalist              | `list="browsers"`                   |
| `form`         | 指定所属表单              | `form="formId"`                     |

```html
<!-- 综合验证属性 -->
<input
  type="text"
  name="username"
  placeholder="请输入用户名"
  required
  minlength="6"
  maxlength="20"
  pattern="^[a-zA-Z0-9_]+$"
  autofocus
  autocomplete="username"
/>
```

---

## 表单元素

**label 标签**
`<label for="<控件ID>">[文本]</label>` 或 `<label>[控件 + 文本]</label>`
```html
<!-- 显式关联 -->
<label for="username">用户名:</label>
<input type="text" id="username" name="username" />

<!-- 隐式关联 -->
<label>
  <input type="checkbox" name="agree" /> 我同意条款
</label>
```

**select 下拉框**
`<select name="<名称>" [multiple] [size="<可见行数>"] [required]>...<option>...</select>`
```html
<select name="country" required>
  <option value="">请选择</option>
  <option value="cn">中国</option>
  <option value="us" selected>美国</option>
</select>

<!-- 分组 -->
<select name="city">
  <optgroup label="华东">
    <option value="sh">上海</option>
    <option value="hz">杭州</option>
  </optgroup>
  <optgroup label="华北">
    <option value="bj">北京</option>
  </optgroup>
</select>

<!-- 多选 -->
<select name="hobbies" multiple size="4">
  <option value="reading">阅读</option>
  <option value="music">音乐</option>
</select>
```

**option 选项**
`<option value="<值>" [selected] [disabled]>[文本]</option>`

**textarea 多行文本**
`<textarea name="<名称>" [rows="<行数>"] [cols="<列数>"] [maxlength] [required] [placeholder]></textarea>`
```html
<textarea name="message" rows="4" cols="50" placeholder="请输入留言" maxlength="500"></textarea>
```

**button 按钮**
`<button type="submit|reset|button" [name] [value]>[内容]</button>`
```html
<button type="submit">提交</button>
<button type="reset">重置</button>
<button type="button" onclick="alert('hi')">点击</button>
```

**fieldset 与 legend 分组**
`<fieldset [disabled]><legend>[标题]</legend>...</fieldset>`
```html
<fieldset>
  <legend>个人信息</legend>
  <label>姓名:<input type="text" name="name" /></label>
  <label>年龄:<input type="number" name="age" /></label>
</fieldset>
```

**datalist 输入建议**
`<input list="<ID>" />` + `<datalist id="<ID>">...<option>...</datalist>`
```html
<input type="text" list="browsers" name="browser" />
<datalist id="browsers">
  <option value="Chrome"></option>
  <option value="Firefox"></option>
  <option value="Safari"></option>
</datalist>
```

**output 输出结果**
`<output for="<关联ID>" name="<名称>">[结果]</output>`
```html
<form oninput="result.value=parseInt(a.value)+parseInt(b.value)">
  <input type="number" id="a" value="10" />
  +<input type="number" id="b" value="20" />
  =<output name="result" for="a b">30</output>
</form>
```

---

## 客户端验证

**内置验证类型**

| 验证类型     | 触发属性                    | 示例                              |
| ------------ | --------------------------- | --------------------------------- |
| 必填         | `required`                  | `<input required>`                |
| 邮箱格式     | `type="email"`              | `<input type="email">`            |
| URL 格式     | `type="url"`                | `<input type="url">`              |
| 数值范围     | `min` / `max`               | `<input min="1" max="100">`       |
| 长度限制     | `minlength` / `maxlength`   | `<input minlength="6">`           |
| 正则模式     | `pattern`                   | `<input pattern="[0-9]{6}">`      |
| 步长         | `step`                      | `<input step="0.5">`              |

**ValidityState API**
```javascript
const input = document.querySelector('input');

// 验证状态对象
const validity = input.validity;
console.log(validity.valid);           // 是否有效
console.log(validity.valueMissing);    // required 未填
console.log(validity.typeMismatch);    // 类型不匹配(email/url)
console.log(validity.patternMismatch); // pattern 不匹配
console.log(validity.tooShort);        // 长度小于 minlength
console.log(validity.tooLong);         // 长度大于 maxlength
console.log(validity.rangeUnderflow);  // 小于 min
console.log(validity.rangeOverflow);   // 大于 max
console.log(validity.stepMismatch);    // 步长不匹配
console.log(validity.badInput);        // 输入无效(如 number 中输入字母)
console.log(validity.customError);     // 自定义错误

// 验证方法
input.checkValidity();     // 触发验证,返回布尔值
input.reportValidity();    // 触发验证并显示错误
input.setCustomValidity('错误消息'); // 设置自定义错误
input.setCustomValidity('');         // 清除自定义错误

// 错误消息
console.log(input.validationMessage);
```

**自定义验证示例**
```javascript
// 密码确认验证
const password = document.getElementById('password');
const confirm = document.getElementById('confirmPassword');

confirm.addEventListener('input', () => {
  if (password.value !== confirm.value) {
    confirm.setCustomValidity('两次输入的密码不一致');
  } else {
    confirm.setCustomValidity('');
  }
});
```

---

## 表单事件

**表单相关事件**
```javascript
const form = document.querySelector('form');
const input = document.querySelector('input');

// 表单提交
form.addEventListener('submit', (e) => {
  if (!form.checkValidity()) {
    e.preventDefault();
  }
});

// 输入变化(实时)
input.addEventListener('input', (e) => {
  console.log(e.target.value);
});

// 值变化(失焦后)
input.addEventListener('change', (e) => {
  console.log(e.target.value);
});

// 无效字段
input.addEventListener('invalid', (e) => {
  e.target.setCustomValidity('请填写此字段');
});

// 表单重置
form.addEventListener('reset', () => {
  console.log('表单已重置');
});
```

| 事件      | 触发时机                |
| --------- | ----------------------- |
| `submit`  | 表单提交                |
| `reset`   | 表单重置                |
| `input`   | 输入变化(实时)         |
| `change`  | 值变化且失焦            |
| `invalid` | 验证失败                |
| `focus`   | 获得焦点                |
| `blur`    | 失去焦点                |

---

## FormData API

**表单数据收集**
```javascript
const form = document.querySelector('form');

// 从表单创建 FormData
const formData = new FormData(form);

// 读取字段
console.log(formData.get('username'));
console.log(formData.getAll('hobbies'));

// 添加字段
formData.append('key', 'value');
formData.append('file', fileInput.files[0]);

// 修改字段
formData.set('key', 'new-value');

// 删除字段
formData.delete('key');

// 遍历
for (const [key, value] of formData.entries()) {
  console.log(key, value);
}

// 通过 fetch 提交
fetch('/api/submit', {
  method: 'POST',
  body: formData
});
```



<!-- ============ 文档分隔线：006-html5/002-Geolocation.md ============ -->

# 地理位置定位 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数 | `{ }` 分组 | `|` 或 | `...` 重复

---

## Geolocation API 检测与获取

**API 存在性检测**
`'geolocation' in navigator`

```javascript
// 检测浏览器是否支持 Geolocation API
if ('geolocation' in navigator) {
  // 支持,可调用相关 API
} else {
  // 不支持,需降级处理
}
```

**获取当前位置**
`navigator.geolocation.getCurrentPosition(<success>, [error], [options])`

```javascript
// 异步获取设备当前位置(经纬度)
navigator.geolocation.getCurrentPosition(
  (position) => {
    console.log('纬度:', position.coords.latitude);   // 纬度(-180 ~ 180)
    console.log('经度:', position.coords.longitude);  // 经度(-90 ~ 90)
    console.log('精度:', position.coords.accuracy);   // 精度(米)
  },
  (error) => {
    console.error('错误码:', error.code, '消息:', error.message);
  },
  {
    enableHighAccuracy: true, // 是否启用高精度模式
    timeout: 10000,           // 超时时间(毫秒)
    maximumAge: 0             // 缓存位置最大有效期(毫秒),0 表示不使用缓存
  }
);
```

---

## 位置监听

**持续监听位置变化**
`const watchId = navigator.geolocation.watchPosition(<success>, [error], [options])`

```javascript
// 持续监听位置变化(适用于导航、运动追踪等场景)
const watchId = navigator.geolocation.watchPosition(
  (pos) => {
    console.log(`当前位置: ${pos.coords.latitude}, ${pos.coords.longitude}`);
  },
  (err) => {
    console.error('监听失败:', err.message);
  },
  {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
  }
);
```

**停止位置监听**
`navigator.geolocation.clearWatch(<watchId>)`

```javascript
// 停止位置监听,释放资源
navigator.geolocation.clearWatch(watchId);
```

---

## Position 对象属性

**coords 属性表**

| 属性                      | 类型   | 说明                              |
| ------------------------- | ------ | --------------------------------- |
| `coords.latitude`         | Double | 纬度(十进制度,范围 -90 ~ 90)     |
| `coords.longitude`        | Double | 经度(十进制度,范围 -180 ~ 180)   |
| `coords.accuracy`         | Double | 位置精度(米)                     |
| `coords.altitude`         | Double | 海拔高度(米,null 表示不可用)     |
| `coords.altitudeAccuracy` | Double | 海拔精度(米)                     |
| `coords.heading`          | Double | 方向(度,正北顺时针,null 表示静止)|
| `coords.speed`            | Double | 速度(米/秒,null 表示不可用)      |
| `timestamp`               | Long   | 获取位置的时间戳(DOMTimeStamp)   |

---

## 错误处理

**PositionError 错误码表**

| 错误码 | 常量名                  | 说明               |
| ------ | ----------------------- | ------------------ |
| 1      | `PERMISSION_DENIED`     | 用户拒绝了位置请求 |
| 2      | `POSITION_UNAVAILABLE`  | 位置信息不可用     |
| 3      | `TIMEOUT`               | 请求超时           |
| 0      | `UNKNOWN_ERROR`         | 未知错误           |

```javascript
// 错误处理示例
navigator.geolocation.getCurrentPosition(
  (pos) => console.log(pos.coords),
  (error) => {
    switch (error.code) {
      case error.PERMISSION_DENIED:
        console.error('用户拒绝授权');
        break;
      case error.POSITION_UNAVAILABLE:
        console.error('位置不可用');
        break;
      case error.TIMEOUT:
        console.error('请求超时');
        break;
      default:
        console.error('未知错误:', error.message);
    }
  }
);
```

---

## Permissions API 权限查询

**查询地理定位权限状态**
`navigator.permissions.query({ name: 'geolocation' })`

```javascript
// 查询当前地理位置权限状态
navigator.permissions.query({ name: 'geolocation' }).then((result) => {
  console.log('权限状态:', result.state); // granted | denied | prompt
  result.onchange = () => {
    console.log('权限变更:', result.state);
  };
});
```

---

## Haversine 距离计算

**计算两点间球面距离**
`haversineDistance(<lat1>, <lon1>, <lat2>, <lon2>)`

```javascript
// 使用 Haversine 公式计算地球表面两点间最短距离(千米)
function haversineDistance(lat1, lon1, lat2, lon2) {
  const R = 6371; // 地球半径(千米)
  const toRad = (deg) => (deg * Math.PI) / 180;
  const dLat = toRad(lat2 - lat1);
  const dLon = toRad(lon2 - lon1);
  const a =
    Math.sin(dLat / 2) ** 2 +
    Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLon / 2) ** 2;
  return R * 2 * Math.asin(Math.sqrt(a));
}

// 示例:北京到上海的距离
const distance = haversineDistance(39.9042, 116.4074, 31.2304, 121.4737);
console.log(`距离: ${distance.toFixed(2)} 千米`);
```

---

## 地理围栏

**Geofence 类实现**
`new Geofence(<centerLat>, <centerLng>, <radiusMeters>)`

```javascript
// 地理围栏:判断设备是否进入指定圆形区域
class Geofence {
  constructor(centerLat, centerLng, radiusMeters) {
    this.center = { lat: centerLat, lng: centerLng };
    this.radius = radiusMeters; // 半径(米)
  }

  // 判断指定坐标是否在围栏内
  contains(lat, lng) {
    const distanceKm = haversineDistance(this.center.lat, this.center.lng, lat, lng);
    return distanceKm * 1000 <= this.radius;
  }
}

// 使用示例
const fence = new Geofence(39.9042, 116.4074, 500); // 北京中心 500 米范围
console.log(fence.contains(39.9050, 116.4080)); // true/false
```

---

## 注意事项

- **HTTPS 要求**:Geolocation API 仅在安全上下文(HTTPS 或 localhost)中可用
- **用户授权**:首次调用会弹出权限请求,用户拒绝后返回 `PERMISSION_DENIED`
- **精度限制**:`enableHighAccuracy: true` 会消耗更多电量(使用 GPS)
- **移动设备**:结合 `watchPosition` 可实现导航功能,但需注意电池消耗
- **隐私保护**:不得在未经用户同意的情况下收集或上传位置数据



<!-- ============ 文档分隔线：006-html5/003-HTML5MultimediaCanvasDrawing.md ============ -->

# 多媒体与 Canvas 绘图 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Canvas 元素

**canvas 标签**
`<canvas id="<ID>" width="<宽>" height="<高>" [style]></canvas>`
```html
<!-- 画布元素 -->
<canvas id="myCanvas" width="400" height="300" style="border:1px solid #000;">
  您的浏览器不支持 Canvas。
</canvas>
```

**获取绘图上下文**
```javascript
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

// WebGL 上下文
const gl = canvas.getContext('webgl');
// 或 webgl2
const gl2 = canvas.getContext('webgl2');
```

---

## Canvas 2D 矩形

**矩形绘制**
`ctx.fillRect(x, y, width, height)` | `ctx.strokeRect(...)` | `ctx.clearRect(...)`
```javascript
// 填充矩形
ctx.fillStyle = '#FF0000';
ctx.fillRect(10, 10, 150, 75);

// 描边矩形
ctx.strokeStyle = '#0000FF';
ctx.lineWidth = 2;
ctx.strokeRect(200, 10, 150, 75);

// 清除矩形区域
ctx.clearRect(50, 25, 50, 30);

// 圆角矩形(新 API)
ctx.beginPath();
ctx.roundRect(10, 10, 100, 50, 8);
ctx.fill();
```

---

## Canvas 路径

**路径绘制**
```javascript
// 三角形
ctx.beginPath();
ctx.moveTo(50, 150);       // 移动到起点
ctx.lineTo(150, 150);      // 画线到
ctx.lineTo(100, 50);
ctx.closePath();           // 闭合路径
ctx.fillStyle = '#FFFF00';
ctx.fill();                // 填充
ctx.stroke();              // 描边
```

**圆形与弧线**
`ctx.arc(x, y, radius, startAngle, endAngle, [anticlockwise])`
```javascript
// 完整圆
ctx.beginPath();
ctx.arc(250, 100, 50, 0, Math.PI * 2);
ctx.fillStyle = '#00FF00';
ctx.fill();

// 半圆弧
ctx.beginPath();
ctx.arc(250, 200, 50, 0, Math.PI);
ctx.strokeStyle = '#FF00FF';
ctx.lineWidth = 3;
ctx.stroke();

// 椭圆
ctx.beginPath();
ctx.ellipse(100, 200, 50, 30, 0, 0, Math.PI * 2);
ctx.stroke();
```

**贝塞尔曲线**
```javascript
// 二次贝塞尔
ctx.beginPath();
ctx.moveTo(0, 100);
ctx.quadraticCurveTo(50, 0, 100, 100); // 控制点,终点
ctx.stroke();

// 三次贝塞尔
ctx.beginPath();
ctx.moveTo(0, 200);
ctx.bezierCurveTo(30, 150, 70, 250, 100, 200); // 控制点1,控制点2,终点
ctx.stroke();
```

---

## Canvas 文本

**文本绘制**
`ctx.fillText(text, x, y, [maxWidth])` | `ctx.strokeText(...)`
```javascript
// 填充文本
ctx.font = '30px Arial';
ctx.fillStyle = '#000000';
ctx.textAlign = 'start';  // start/end/left/right/center
ctx.textBaseline = 'alphabetic'; // top/hanging/middle/alphabetic/ideographic/bottom
ctx.fillText('Hello Canvas', 50, 250);

// 描边文本
ctx.font = '24px Times New Roman';
ctx.strokeStyle = '#FF0000';
ctx.strokeText('Hello Canvas', 50, 290);

// 测量文本
const metrics = ctx.measureText('Hello');
console.log(metrics.width);
```

---

## Canvas 图像

**图像绘制**
`ctx.drawImage(image, x, y, [width, height])` | `ctx.drawImage(image, sx, sy, sw, sh, dx, dy, dw, dh)`
```javascript
const img = new Image();
img.src = 'image.jpg';
img.onload = function () {
  // 完整绘制
  ctx.drawImage(img, 0, 0);

  // 缩放绘制
  ctx.drawImage(img, 0, 0, 100, 80);

  // 裁剪绘制(源 x,y,w,h,目标 x,y,w,h)
  ctx.drawImage(img, 100, 100, 50, 50, 200, 200, 50, 50);
};
```

---

## Canvas 样式

**填充与描边**
```javascript
// 纯色
ctx.fillStyle = 'red';
ctx.fillStyle = '#FF0000';
ctx.fillStyle = 'rgb(255, 0, 0)';
ctx.fillStyle = 'rgba(255, 0, 0, 0.5)';

// 线性渐变
const linearGradient = ctx.createLinearGradient(0, 0, 200, 0);
linearGradient.addColorStop(0, 'red');
linearGradient.addColorStop(0.5, 'yellow');
linearGradient.addColorStop(1, 'blue');
ctx.fillStyle = linearGradient;

// 径向渐变
const radialGradient = ctx.createRadialGradient(100, 100, 10, 100, 100, 100);
radialGradient.addColorStop(0, 'white');
radialGradient.addColorStop(1, 'black');
ctx.fillStyle = radialGradient;

// 图案
const pattern = ctx.createPattern(img, 'repeat'); // repeat/repeat-x/repeat-y/no-repeat
ctx.fillStyle = pattern;
```

**线样式**
```javascript
ctx.lineWidth = 2;            // 线宽
ctx.lineCap = 'round';        // butt/round/square
ctx.lineJoin = 'round';       // miter/round/bevel
ctx.miterLimit = 10;          // 斜接限制
ctx.setLineDash([5, 5]);      // 虚线
ctx.lineDashOffset = 0;       // 虚线偏移
```

**阴影**
```javascript
ctx.shadowColor = 'rgba(0, 0, 0, 0.5)';
ctx.shadowBlur = 10;
ctx.shadowOffsetX = 5;
ctx.shadowOffsetY = 5;
```

**透明度与合成**
```javascript
ctx.globalAlpha = 0.5;            // 全局透明度
ctx.globalCompositeOperation = 'source-over'; // 合成模式
// source-over / destination-over / multiply / screen / overlay 等
```

---

## Canvas 变换

**坐标变换**
```javascript
ctx.save();                       // 保存状态
ctx.translate(100, 50);           // 平移
ctx.rotate(Math.PI / 4);          // 旋转(弧度)
ctx.scale(1.5, 0.8);              // 缩放
ctx.transform(a, b, c, d, e, f);  // 矩阵变换
ctx.setTransform(1, 0, 0, 1, 0, 0); // 重置变换
ctx.restore();                    // 恢复状态
```

**示例:旋转矩形**
```javascript
ctx.save();
ctx.translate(200, 100);          // 移到旋转中心
ctx.rotate(Math.PI / 4);          // 旋转 45 度
ctx.fillStyle = '#00FF00';
ctx.fillRect(-50, -25, 100, 50);  // 以新原点为基准
ctx.restore();
```

---

## Canvas 动画

**requestAnimationFrame**
```javascript
let x = 0;
const speed = 2;

function animate() {
  // 清除画布
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // 绘制
  ctx.fillStyle = '#FF0000';
  ctx.fillRect(x, 100, 50, 50);

  // 更新位置
  x += speed;
  if (x > canvas.width - 50 || x < 0) {
    speed = -speed; // 反弹
  }

  // 请求下一帧
  requestAnimationFrame(animate);
}

animate();

// 取消动画
const animationId = requestAnimationFrame(animate);
cancelAnimationFrame(animationId);
```

---

## Canvas 交互

**鼠标绘制**
```javascript
let isDrawing = false;
let lastX = 0;
let lastY = 0;

canvas.addEventListener('mousedown', (e) => {
  isDrawing = true;
  [lastX, lastY] = [e.offsetX, e.offsetY];
});

canvas.addEventListener('mousemove', (e) => {
  if (!isDrawing) return;
  ctx.beginPath();
  ctx.moveTo(lastX, lastY);
  ctx.lineTo(e.offsetX, e.offsetY);
  ctx.strokeStyle = '#000';
  ctx.lineWidth = 2;
  ctx.lineCap = 'round';
  ctx.stroke();
  [lastX, lastY] = [e.offsetX, e.offsetY];
});

canvas.addEventListener('mouseup', () => isDrawing = false);
canvas.addEventListener('mouseout', () => isDrawing = false);
```

**触摸事件**
```javascript
canvas.addEventListener('touchstart', (e) => {
  e.preventDefault();
  const touch = e.touches[0];
  const rect = canvas.getBoundingClientRect();
  lastX = touch.clientX - rect.left;
  lastY = touch.clientY - rect.top;
  isDrawing = true;
});

canvas.addEventListener('touchmove', (e) => {
  e.preventDefault();
  if (!isDrawing) return;
  const touch = e.touches[0];
  const rect = canvas.getBoundingClientRect();
  const x = touch.clientX - rect.left;
  const y = touch.clientY - rect.top;
  ctx.beginPath();
  ctx.moveTo(lastX, lastY);
  ctx.lineTo(x, y);
  ctx.stroke();
  [lastX, lastY] = [x, y];
});
```

---

## Canvas 图像导出

**toDataURL 与 toBlob**
```javascript
// 转为 data URL
const dataURL = canvas.toDataURL('image/png');
const dataURL2 = canvas.toDataURL('image/jpeg', 0.9); // 质量

// 转为 Blob
canvas.toBlob((blob) => {
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'canvas.png';
  a.click();
  URL.revokeObjectURL(url);
}, 'image/png');
```

---

## Canvas vs SVG

| 特性     | Canvas                         | SVG                     |
| -------- | ------------------------------ | ----------------------- |
| 绘图方式 | 基于像素,JavaScript 绘制       | 基于矢量,XML 标记       |
| 缩放     | 缩放会失真                     | 缩放不失真              |
| 性能     | 适合大量图形和动画             | 适合少量静态图形        |
| 事件处理 | 需手动实现                     | 支持元素级事件          |
| DOM      | 单一元素                       | 每个图形是 DOM 元素     |
| 适用场景 | 游戏、复杂动画、数据可视化     | 图标、图表、标志        |

---

## Web Audio API

**音频上下文**
```javascript
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

// 创建振荡器
const oscillator = audioCtx.createOscillator();
oscillator.type = 'sine'; // sine/square/sawtooth/triangle
oscillator.frequency.value = 440; // 频率 Hz

// 创建增益(音量)
const gainNode = audioCtx.createGain();
gainNode.gain.value = 0.5;

// 连接节点
oscillator.connect(gainNode);
gainNode.connect(audioCtx.destination);

// 播放
oscillator.start();
oscillator.stop(audioCtx.currentTime + 2); // 2 秒后停止
```



<!-- ============ 文档分隔线：006-html5/004-HTML5OverviewCoreFeature.md ============ -->

# HTML5 全局属性与文档结构 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数 | `{ }` 分组 | `|` 或 | `...` 重复

---

## HTML5 文档基本结构

**最小 HTML5 文档**
`<!DOCTYPE html> <html lang="..."> <head>...</head> <body>...</body> </html>`

```html
<!DOCTYPE html>
<!-- HTML5 文档类型声明 -->
<html lang="zh-CN">
  <!-- lang 属性指定文档语言 -->
  <head>
    <meta charset="UTF-8" />
    <!-- 字符编码声明 -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- 移动端视口配置 -->
    <title>页面标题</title>
    <!-- 文档标题(必填) -->
  </head>
  <body>
    <!-- 页面内容 -->
  </body>
</html>
```

**head 头部元数据元素**

| 元素                    | 作用                           | 示例                                                |
| ----------------------- | ------------------------------ | --------------------------------------------------- |
| `<title>`               | 文档标题(必填)               | `<title>页面标题</title>`                           |
| `<meta charset>`        | 字符编码                       | `<meta charset="UTF-8" />`                          |
| `<meta name="viewport">`| 移动端视口                     | `<meta name="viewport" content="width=device-width, initial-scale=1.0">` |
| `<meta name="description">` | 页面描述(SEO)            | `<meta name="description" content="页面描述">`      |
| `<meta name="keywords">`    | 关键词(SEO,已废弃)       | `<meta name="keywords" content="HTML5, CSS3">`      |
| `<meta name="author">`      | 作者                       | `<meta name="author" content="张三">`               |
| `<meta http-equiv="refresh">` | 自动刷新                  | `<meta http-equiv="refresh" content="30">`          |
| `<link rel="stylesheet">`   | 外部样式表                 | `<link rel="stylesheet" href="style.css">`          |
| `<link rel="icon">`         | 网站图标                   | `<link rel="icon" href="favicon.ico">`              |
| `<link rel="canonical">`    | 规范链接(SEO)            | `<link rel="canonical" href="https://...">`         |
| `<link rel="preconnect">`   | 预连接                    | `<link rel="preconnect" href="https://cdn.example.com">` |
| `<link rel="preload">`      | 预加载                    | `<link rel="preload" href="font.woff2" as="font">`  |
| `<script>`                  | 脚本                      | `<script src="app.js" defer></script>`              |
| `<style>`                   | 内联样式                  | `<style>body{margin:0}</style>`                     |
| `<base>`                    | 基准 URL                  | `<base href="https://example.com/" target="_blank">`|

---

## 语义化文档结构

**完整文档骨架**

```html
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>语义化页面结构</title>
  </head>
  <body>
    <header><!-- 页面头部 --></header>
    <nav><!-- 导航 --></nav>
    <main>
      <article><!-- 独立内容 --></article>
      <section><!-- 区块 --></section>
      <aside><!-- 侧边栏 --></aside>
    </main>
    <footer><!-- 页脚 --></footer>
  </body>
</html>
```

**语义化结构元素表**

| 元素          | 作用                  | 使用场景                  |
| ------------- | --------------------- | ------------------------- |
| `<header>`    | 页面或区块的头部      | 网站标题、Logo、导航栏    |
| `<nav>`       | 导航链接区域          | 主导航、面包屑导航        |
| `<main>`      | 主要内容(每页唯一)   | 唯一的主要内容区域        |
| `<article>`   | 独立完整的内容        | 文章、新闻、评论、产品卡  |
| `<section>`   | 主题相关的内容区块    | 章节、章节分组            |
| `<aside>`     | 侧边栏或附属信息      | 相关链接、广告、引用      |
| `<footer>`    | 页面或区块的底部      | 版权信息、联系方式        |
| `<figure>`    | 独立的媒体内容        | 图片、图表、代码块        |
| `<figcaption>`| figure 的标题         | 图片说明、图表标题        |
| `<details>`   | 可折叠的详细信息      | FAQ、技术详情             |
| `<summary>`   | details 的标题        | 折叠区域的标题            |
| `<dialog>`    | 对话框/模态框         | 模态对话框                |
| `<search>`    | 搜索区域(HTML Living Standard) | 站点搜索表单    |

---

## HTML5 全局属性

**核心全局属性表**

| 属性            | 作用                          | 示例                              |
| --------------- | ----------------------------- | --------------------------------- |
| `id`            | 元素唯一标识                  | `<div id="header">`               |
| `class`         | 类名(可多个,空格分隔)      | `<div class="box active">`        |
| `style`         | 内联样式                      | `<div style="color:red">`         |
| `title`         | 鼠标悬停提示                  | `<a title="点击查看详情">`        |
| `lang`          | 元素内容语言                  | `<p lang="en">Hello</p>`          |
| `dir`           | 文本方向                      | `<p dir="rtl">...</p>` (ltr/rtl/auto) |
| `tabindex`      | Tab 键焦点顺序                | `<div tabindex="0">`              |
| `accesskey`     | 快捷键                        | `<button accesskey="s">`          |
| `hidden`        | 隐藏元素                     | `<div hidden>...</div>`           |
| `draggable`     | 是否可拖拽                    | `<div draggable="true">`          |
| `spellcheck`    | 拼写检查                      | `<input spellcheck="true">`       |
| `translate`     | 是否翻译                     | `<p translate="no">Brand</p>`     |
| `contenteditable`| 内容可编辑                  | `<div contenteditable="true">`    |
| `contextmenu`   | 上下文菜单(已废弃)         | -                                 |
| `tabindex`      | 焦点顺序                     | `<div tabindex="0">`              |

**data-* 自定义数据属性**
`data-<name>="<value>"`

```html
<!-- 存储自定义数据(详见"自定义数据属性"章节) -->
<div data-user-id="123" data-role="admin">用户信息</div>
```

---

## ARIA 无障碍属性

**常用 ARIA 属性(详见"无障碍访问"章节)**

```html
<!-- 主要 ARIA 属性 -->
<div
  role="button"
  aria-label="关闭"
  aria-hidden="false"
  aria-disabled="false"
  aria-expanded="true"
  aria-controls="menu"
  aria-live="polite"
  aria-current="page"
>
  ...
</div>
```

---

## 事件处理属性

**HTML 事件属性表**

| 事件属性          | 触发时机              | 应用元素              |
| ----------------- | --------------------- | --------------------- |
| `onclick`         | 点击                  | 几乎所有元素          |
| `ondblclick`      | 双击                  | 几乎所有元素          |
| `onmousedown`     | 鼠标按下              | 几乎所有元素          |
| `onmouseup`       | 鼠标释放              | 几乎所有元素          |
| `onmouseover`     | 鼠标移入              | 几乎所有元素          |
| `onmouseout`      | 鼠标移出              | 几乎所有元素          |
| `onmousemove`     | 鼠标移动              | 几乎所有元素          |
| `onkeydown`       | 键盘按下              | 表单元素、可聚焦元素  |
| `onkeyup`         | 键盘释放              | 表单元素、可聚焦元素  |
| `onkeypress`      | 键盘按住(已废弃)    | 表单元素、可聚焦元素  |
| `onfocus`         | 获得焦点              | 表单元素、可聚焦元素  |
| `onblur`          | 失去焦点              | 表单元素、可聚焦元素  |
| `onchange`        | 值改变并失焦          | input、select、textarea |
| `oninput`         | 值改变(实时)        | input、textarea       |
| `onsubmit`        | 表单提交              | `<form>`              |
| `onreset`         | 表单重置              | `<form>`              |
| `onload`          | 加载完成              | `<body>`、`<img>`、`<iframe>` |
| `onunload`        | 卸载(已废弃)        | `<body>`              |
| `onresize`        | 窗口大小改变          | `<body>`              |
| `onscroll`        | 滚动                  | 可滚动元素            |
| `oncontextmenu`   | 右键菜单              | 几乎所有元素          |
| `ondrag`          | 拖拽中                | 可拖拽元素            |
| `ondrop`          | 放置                  | 放置目标              |
| `oncopy`          | 复制                  | 可选中文本元素        |
| `onpaste`         | 粘贴                  | 表单元素              |

---

## 字符编码与 viewport

**字符编码声明**
`<meta charset="<encoding>">`

```html
<!-- UTF-8 是 HTML5 推荐编码,必须放在 <head> 的最前面 -->
<meta charset="UTF-8" />

<!-- 其他常用编码 -->
<meta charset="UTF-16" />
<meta charset="ISO-8859-1" />
```

**viewport 视口配置(移动端必填)**
`<meta name="viewport" content="<key>=<value>, <key>=<value>, ...">`

```html
<!-- 标准移动端视口配置 -->
<meta
  name="viewport"
  content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=5.0, user-scalable=yes"
/>
```

**viewport 属性表**

| 属性                | 作用                          | 示例值              |
| ------------------- | ----------------------------- | ------------------- |
| `width`             | 视口宽度                      | `device-width` 或数字 |
| `height`            | 视口高度                      | `device-height` 或数字 |
| `initial-scale`     | 初始缩放比例                  | `1.0`               |
| `minimum-scale`     | 最小缩放比例                  | `1.0`               |
| `maximum-scale`     | 最大缩放比例                  | `5.0`               |
| `user-scalable`     | 是否允许用户缩放              | `yes` 或 `no`       |
| `viewport-fit`      | 视口形状(刘海屏适配)        | `auto` / `contain` / `cover` |

---

## 资源预加载

**link rel 预加载类型**
`<link rel="<type>" href="<url>" as="<resource-type>">`

```html
<!-- 预连接(提前建立连接) -->
<link rel="preconnect" href="https://cdn.example.com" crossorigin />

<!-- DNS 预解析 -->
<link rel="dns-prefetch" href="//cdn.example.com" />

<!-- 预加载关键资源 -->
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin />
<link rel="preload" href="critical.css" as="style" />
<link rel="preload" href="hero.jpg" as="image" />

<!-- 预获取(空闲时获取) -->
<link rel="prefetch" href="next-page.html" />

<!-- 预渲染(已废弃,改用 prefetch) -->
<link rel="prerender" href="next-page.html" />
```

**as 属性值表**

| 值              | 资源类型         |
| --------------- | ---------------- |
| `audio`         | 音频文件         |
| `document`      | HTML 文档        |
| `embed`         | 嵌入资源         |
| `fetch`         | fetch/XHR 请求   |
| `font`          | 字体文件         |
| `image`         | 图片             |
| `object`        | 插件资源         |
| `script`        | JavaScript       |
| `style`         | CSS 样式表       |
| `track`         | WebVTT 文件      |
| `video`         | 视频文件         |
| `worker`        | Web Worker       |

---

## script 标签属性

**script 加载策略**
`<script src="..." defer | async></script>`

```html
<!-- 普通加载:阻塞 HTML 解析,立即下载执行 -->
<script src="script.js"></script>

<!-- async:异步下载,下载完立即执行(不保证顺序) -->
<script src="analytics.js" async></script>

<!-- defer:异步下载,HTML 解析完成后按顺序执行 -->
<script src="app.js" defer></script>

<!-- 内联模块(默认 defer) -->
<script type="module">
  import { greet } from './utils.js';
  greet();
</script>

<!-- 指定 MIME 类型 -->
<script type="text/javascript" src="script.js"></script>
<script type="module" src="app.js"></script>
<script type="application/json">{"key":"value"}</script>
```

**async vs defer 对比**

| 属性     | 下载     | 执行时机                  | 执行顺序      | 适用场景            |
| -------- | -------- | ------------------------- | ------------- | ------------------- |
| 无       | 阻塞     | 下载完立即执行            | 源顺序        | 关键脚本            |
| `async`  | 不阻塞   | 下载完立即执行            | 不保证顺序    | 独立第三方脚本      |
| `defer`  | 不阻塞   | HTML 解析完成后执行       | 源顺序        | 依赖 DOM 的脚本     |

---

## HTML5 新增特性元素

**HTML Living Standard 2025 新增**

```html
<!-- <dialog> 原生对话框元素 -->
<dialog id="modal">
  <form method="dialog">
    <p>确认操作?</p>
    <button>取消</button>
    <button value="confirm">确认</button>
  </form>
</dialog>

<!-- popover 属性(原生弹出层) -->
<button popovertarget="mypopover">打开弹出</button>
<div id="mypopover" popover>
  <p>这是一个弹出层</p>
</div>

<!-- <search> 搜索区域 -->
<search>
  <form action="/search">
    <input type="search" name="q" />
    <button>搜索</button>
  </form>
</search>

<!-- <details> 可折叠区域 -->
<details>
  <summary>更多详情</summary>
  <p>这里是详细内容</p>
</details>

<!-- loading="lazy" 懒加载 -->
<img src="image.jpg" loading="lazy" alt="..." />

<!-- <template> 内容模板 -->
<template id="card-template">
  <div class="card">
    <h3></h3>
    <p></p>
  </div>
</template>
```

---

## 注意事项

- **DOCTYPE 必填**:HTML5 文档必须以 `<!DOCTYPE html>` 开头(不区分大小写)
- **charset 位置**:`<meta charset>` 必须放在 `<head>` 的最前面,前 1024 字节内
- **viewport 必填**:移动端页面必须配置 viewport,否则会以桌面宽度渲染
- **lang 属性**:应为 `<html>` 指定 `lang` 属性,有助于 SEO 和无障碍访问
- **title 必填**:每个页面必须有唯一的 `<title>`,长度建议 30-60 字符
- **语义化优先**:使用语义化标签(header、nav、main)替代无意义 div
- **script 位置**:推荐 `<script defer>` 放在 `<head>` 中,而非 `<body>` 末尾
- **preconnect 跨域**:跨域资源预加载需添加 `crossorigin` 属性



<!-- ============ 文档分隔线：006-html5/005-HTML5BasicTagGlobalAttribute.md ============ -->

# 基础标签与全局属性 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 标题标签

**六级标题**
`<h1>...</h1>` | `<h2>...</h2>` | `<h3>...</h3>` | `<h4>...</h4>` | `<h5>...</h5>` | `<h6>...</h6>`
```html
<!-- 标题层级递减,每页建议仅一个 h1 -->
<h1>网站主标题</h1>
<h2>章节标题</h2>
<h3>子章节标题</h3>
<h4>子子章节标题</h4>
```

| 标签   | 语义               |
| ------ | ------------------ |
| `<h1>` | 一级标题,页面主标题 |
| `<h2>` | 二级标题,章节标题   |
| `<h3>` | 三级标题,子章节     |
| `<h4>` | 四级标题            |
| `<h5>` | 五级标题            |
| `<h6>` | 六级标题            |

---

## 段落与行内容器

**段落标签**
`<p>[内容]</p>`
```html
<!-- 段落自动添加上下空白 -->
<p>这是一个段落。段落是网页中最基本的文本单位。</p>
<p>这是另一个段落。</p>
```

**行内文本容器**
`<span>[内容]</span>`
```html
<!-- 用于对局部文本应用样式 -->
<p>这是一段文本,其中 <span style="color: red;">红色部分</span> 被标记。</p>
```

---

## 文本语义标签

**强调与标记标签**

| 标签        | 描述       | 语义             |
| ----------- | ---------- | ---------------- |
| `<strong>`  | 加粗       | 重要内容         |
| `<em>`      | 倾斜       | 强调内容         |
| `<mark>`    | 标记       | 突出显示         |
| `<small>`   | 小号字体   | 辅助性内容       |
| `<del>`     | 删除线     | 已删除内容       |
| `<ins>`     | 下划线     | 已插入内容       |
| `<sub>`     | 下标       | 下标文本         |
| `<sup>`     | 上标       | 上标文本         |
| `<abbr>`    | 缩写       | 带标题的缩写     |
| `<cite>`    | 引用标题   | 作品标题         |
| `<dfn>`     | 定义术语   | 术语定义         |
| `<address>` | 联系方式   | 作者/联系方式    |
| `<time>`    | 时间       | 机器可读时间     |

```html
<!-- 文本语义综合示例 -->
<p>这是 <strong>重要内容</strong>,这是 <em>强调内容</em>。</p>
<p>这是 <mark>突出显示</mark> 的内容。</p>
<p>这是 <del>已删除</del> 的内容,这是 <ins>已插入</ins> 的内容。</p>
<p>水的化学式是 H<sub>2</sub>O,2 的平方是 2<sup>2</sup>。</p>
<p><abbr title="HyperText Markup Language">HTML</abbr> 是 Web 的基础。</p>
```

---

## 换行与分割线

**换行与水平线**
`<br>` | `<hr>`
```html
<!-- br 强制换行,hr 主题分割 -->
<p>这是第一行<br />这是第二行</p>
<hr />
<p>这是分割线下面的内容</p>
```

---

## 列表标签

**无序列表**
`<ul>...<li>[项]</li>...</ul>`
```html
<!-- 默认圆点标记 -->
<ul>
  <li>苹果</li>
  <li>香蕉</li>
  <li>橙子</li>
</ul>
```

**有序列表**
`<ol [start="<起始>"] [reversed] [type="1|A|a|I|i"]>...<li>[项]</li>...</ol>`
```html
<!-- 数字编号列表 -->
<ol>
  <li>准备材料</li>
  <li>混合原料</li>
  <li>加热</li>
</ol>

<!-- 倒序列表 -->
<ol reversed>
  <li>第四步</li>
  <li>第三步</li>
</ol>

<!-- 字母编号列表 -->
<ol type="A">
  <li>选项 A</li>
  <li>选项 B</li>
</ol>
```

**定义列表**
`<dl><dt>[术语]</dt><dd>[描述]</dd>...</dl>`
```html
<!-- 术语-描述成对出现 -->
<dl>
  <dt>HTML</dt>
  <dd>超文本标记语言</dd>
  <dt>CSS</dt>
  <dd>层叠样式表</dd>
</dl>
```

**嵌套列表**
```html
<!-- 列表可多层嵌套 -->
<ul>
  <li>HTML 基础
    <ul>
      <li>标签语法</li>
      <li>语义化标签</li>
    </ul>
  </li>
  <li>CSS 基础
    <ul>
      <li>选择器</li>
      <li>盒模型</li>
    </ul>
  </li>
</ul>
```

---

## 超链接

**锚点链接**
`<a href="<URL>" [target="_self|_blank|_parent|_top"] [rel="<关系>"] [title="<提示>"]>[文本]</a>`
```html
<!-- 外部链接,新窗口打开 -->
<a href="https://www.example.com" target="_blank" rel="noopener">访问示例网站</a>

<!-- 内部页面 -->
<a href="about.html">关于我们</a>

<!-- 页面锚点 -->
<a href="#section1">跳转到第一部分</a>

<!-- 邮件链接 -->
<a href="mailto:info@example.com">发送邮件</a>

<!-- 电话链接 -->
<a href="tel:+1234567890">拨打电话</a>
```

| target 值  | 行为           |
| ---------- | -------------- |
| `_self`    | 当前窗口(默认) |
| `_blank`   | 新窗口         |
| `_parent`  | 父框架         |
| `_top`     | 整个窗口       |

---

## 图像标签

**图像**
`<img src="<URL>" alt="<替代文本>" [width="<宽>"] [height="<高>"] [loading="lazy|eager"] [title="<提示>"] />`
```html
<!-- 基本图像 -->
<img src="images/photo.jpg" alt="美丽的风景" width="400" height="300" />

<!-- 延迟加载 -->
<img src="images/large-image.jpg" alt="大型图像" loading="lazy" />
```

---

## 全局属性

**基础全局属性**

| 属性              | 描述                       | 示例                       |
| ----------------- | -------------------------- | -------------------------- |
| `id`              | 唯一标识符                 | `id="header"`              |
| `class`           | 样式类名(可多个空格分隔)   | `class="container main"`   |
| `style`           | 行内样式                   | `style="color: red;"`      |
| `title`           | 悬停提示文字               | `title="提示"`             |
| `hidden`          | 隐藏元素                   | `hidden`                   |
| `contenteditable` | 内容可编辑                 | `contenteditable="true"`   |
| `spellcheck`      | 拼写检查                   | `spellcheck="true"`        |
| `tabindex`        | Tab 键顺序                 | `tabindex="1"`             |
| `accesskey`       | 快捷键                     | `accesskey="k"`            |
| `dir`             | 文本方向                   | `dir="ltr"` / `dir="rtl"`  |
| `lang`            | 内容语言                   | `lang="zh-CN"`             |
| `translate`       | 是否翻译                   | `translate="no"`           |
| `draggable`       | 是否可拖动                 | `draggable="true"`         |

```html
<!-- id 与 class -->
<div id="header" class="container">
  <h1>网站标题</h1>
</div>

<!-- 行内样式 -->
<p style="color: blue; font-weight: bold;">蓝色粗体文本</p>

<!-- hidden 隐藏 -->
<div hidden>这个元素是隐藏的</div>

<!-- contenteditable 可编辑 -->
<div contenteditable="true">点击此处编辑内容</div>
```

---

## 自定义数据属性

**data-* 数据存储**
`data-<名称>="<值>"`
```html
<!-- 存储产品信息 -->
<div class="product" data-id="123" data-name="iPhone 13" data-price="799">
  <h3>iPhone 13</h3>
</div>

<!-- JavaScript 读取 -->
<script>
  const product = document.querySelector('.product');
  const productId = product.dataset.id;
  const productName = product.dataset.name;
  const productPrice = product.dataset.price;
  console.log(`产品 ID: ${productId}, 名称: ${productName}, 价格: $${productPrice}`);
</script>
```

---

## 语义化结构标签

**页面结构标签**

| 标签           | 描述                  |
| -------------- | --------------------- |
| `<header>`     | 页面或 section 的头部 |
| `<nav>`        | 导航链接区域          |
| `<main>`       | 页面主要内容(唯一)    |
| `<section>`    | 文档中的主题节        |
| `<article>`    | 独立、可复用的内容块  |
| `<aside>`      | 侧边栏或附加内容      |
| `<footer>`     | 页面或 section 的底部 |
| `<figure>`     | 图表、图像等独立单元  |
| `<figcaption>` | figure 的标题         |
| `<search>`     | 搜索区域(HTML 2023)   |
| `<dialog>`     | 对话框(HTML 2021)     |

```html
<!-- 语义化页面结构 -->
<header>
  <h1>网站标题</h1>
  <nav>
    <ul>
      <li><a href="#">首页</a></li>
      <li><a href="#">关于</a></li>
    </ul>
  </nav>
</header>
<main>
  <article>
    <h2>文章标题</h2>
    <p>文章内容...</p>
  </article>
  <aside>
    <h3>侧边栏</h3>
  </aside>
</main>
<footer>
  <p>&copy; 2026 网站名称</p>
</footer>
```

---

## 可折叠内容

**details 与 summary**
`<details [open]><summary>[标题]</summary>[内容]</details>`
```html
<!-- 默认折叠 -->
<details>
  <summary>常见问题:如何重置密码?</summary>
  <p>请访问登录页面,点击"忘记密码"链接。</p>
</details>

<!-- 默认展开 -->
<details open>
  <summary>使用说明</summary>
  <p>这是默认展开的说明内容。</p>
</details>
```

---

## 弹出对话框(HTML 2021+)

**dialog 元素**
`<dialog [open]>[内容]</dialog>`
```html
<!-- 模态对话框 -->
<dialog id="myDialog">
  <form method="dialog">
    <p>请确认操作</p>
    <button>取消</button>
    <button value="confirm">确认</button>
  </form>
</dialog>

<script>
  const dialog = document.getElementById('myDialog');
  dialog.showModal(); // 显示模态
  dialog.close();     // 关闭
</script>
```

---

## Popover 弹出层(HTML 2024+)

**popover 属性**
`<div popover [="auto|manual"]>[内容]</div>`
```html
<!-- 声明式弹出层 -->
<button popovertarget="my-popover">打开弹出层</button>

<div id="my-popover" popover>
  <p>这是一个弹出层内容</p>
  <button popovertarget="my-popover" popovertargetaction="hide">关闭</button>
</div>
```



<!-- ============ 文档分隔线：006-html5/006-CrossDocumentCommunication.md ============ -->

# 跨文档通信 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数 | `{ }` 分组 | `|` 或 | `...` 重复

---

## postMessage 基础

**发送消息**
`targetWindow.postMessage(<message>, <targetOrigin>, [transfer])`

```javascript
// 向 iframe 发送消息
const iframe = document.getElementById('myIframe');
iframe.contentWindow.postMessage(
  { type: 'GREETING', text: 'Hello' },
  'https://example.com' // 必须指定确切的目标源
);

// 向父窗口发送消息
window.parent.postMessage({ type: 'RESULT' }, 'https://parent.com');

// 向打开的弹窗发送消息
const popup = window.open('https://example.com/popup');
popup.postMessage({ type: 'INIT' }, 'https://example.com');
```

**接收消息**
`window.addEventListener('message', handler)`

```javascript
// 监听 message 事件
window.addEventListener('message', (event) => {
  // 始终验证消息来源
  if (event.origin !== 'https://example.com') return;

  console.log('来源:', event.origin);
  console.log('数据:', event.data);
  console.log('源窗口:', event.source);
});
```

**postMessage 参数表**

| 参数            | 类型           | 说明                                  |
| --------------- | -------------- | ------------------------------------- |
| `message`       | any            | 发送的数据(结构化克隆算法传递)       |
| `targetOrigin`  | string         | 目标源(`'*'` 不安全,应指定确切源)   |
| `transfer`      | Transferable[] | 可转移对象(如 MessagePort、ArrayBuffer)|

---

## MessageEvent 属性

**MessageEvent 对象表**

| 属性             | 类型     | 说明                            |
| ---------------- | -------- | ------------------------------- |
| `data`           | any      | 传递的数据                      |
| `origin`         | string   | 发送方的源(协议+域名+端口)    |
| `source`         | Window   | 发送方的 window 引用(可回复)  |
| `lastEventId`    | string   | 事件 ID(用于 Server-Sent Events) |
| `ports`          | array    | MessagePort 数组                |
| `isTrusted`      | boolean  | 是否由用户行为触发              |

---

## targetWindow 获取方式

**获取目标 window 引用**

```javascript
// 1. iframe 的 contentWindow
const iframeWindow = document.getElementById('myIframe').contentWindow;

// 2. 父窗口
const parentWindow = window.parent;

// 3. 顶层窗口
const topWindow = window.top;

// 4. window.open 返回的引用
const popupWindow = window.open('https://example.com');

// 5. 命名的 window(通过 window.name 获取)
// 已打开的 window 可通过 window.frames 访问
const frameWindow = window.frames[0]; // 按索引
const namedWindow = window.frames['frameName']; // 按名称
```

---

## 安全实践

**验证来源(必须)**
`if (event.origin !== '<expected-origin>') return;`

```javascript
// 接收消息时必须验证来源
window.addEventListener('message', (event) => {
  // 1. 验证来源
  const trustedOrigins = [
    'https://example.com',
    'https://sub.example.com'
  ];
  if (!trustedOrigins.includes(event.origin)) return;

  // 2. 验证数据格式
  if (typeof event.data !== 'object' || !event.data.type) return;

  // 3. 处理消息
  handleMessage(event.data);
});
```

**始终指定 targetOrigin**
`postMessage(<data>, '<确切源>')`

```javascript
// 安全:指定确切的目标源
iframe.contentWindow.postMessage(data, 'https://specific-domain.com');

// 危险:使用通配符(任何窗口都可拦截)
iframe.contentWindow.postMessage(data, '*'); // 不推荐!

// 危险:使用 '/'(仅同源,但易被误解)
iframe.contentWindow.postMessage(data, '/'); // 仅同源时使用
```

**回复消息**
`event.source.postMessage(<reply>, event.origin)`

```javascript
// 接收方回复发送方
window.addEventListener('message', (event) => {
  if (event.origin !== 'https://trusted.com') return;

  // 处理消息后回复
  const reply = { type: 'REPLY', result: 'success' };
  event.source.postMessage(reply, event.origin);
});
```

---

## Channel Messaging API

**MessageChannel 创建**
`const channel = new MessageChannel()`

```javascript
// 创建双向通信通道
const channel = new MessageChannel();

// port1 留在当前窗口
channel.port1.onmessage = (e) => {
  console.log('收到回复:', e.data);
};

// port2 传递给 iframe
iframe.contentWindow.postMessage(
  { type: 'INIT_PORT' },
  'https://example.com',
  [channel.port2] // 转移 port2 的所有权
);
```

**iframe 接收端口并回复**
`event.ports[0].postMessage(<data>)`

```javascript
// iframe 内部接收并使用 port
window.addEventListener('message', (event) => {
  if (event.origin !== 'https://parent.com') return;
  if (event.data.type !== 'INIT_PORT') return;

  // 获取传递过来的 port
  const port = event.ports[0];
  port.onmessage = (e) => {
    console.log('收到:', e.data);
  };

  // 通过 port 回复消息
  port.postMessage({ type: 'PORT_READY' });
});
```

**MessagePort 方法表**

| 方法                    | 说明                          |
| ----------------------- | ----------------------------- |
| `port.postMessage(d)`   | 发送消息                      |
| `port.onmessage`        | 监听消息                      |
| `port.start()`          | 启用消息分发(显式)          |
| `port.close()`          | 关闭端口                      |
| `port.onmessageerror`   | 监听消息错误                  |

---

## BroadcastChannel API

**广播通道(同源多标签页通信)**
`const channel = new BroadcastChannel('<name>')`

```javascript
// 创建广播通道(同源的所有标签页共享)
const channel = new BroadcastChannel('app_updates');

// 发送广播消息(所有监听同一通道的标签页都会收到)
channel.postMessage({ type: 'LOGOUT' });

// 接收广播消息
channel.onmessage = (event) => {
  console.log('收到广播:', event.data);
};

// 关闭通道
channel.close();
```

**BroadcastChannel 应用场景**

```javascript
// 示例:多标签页同步登录状态
const authChannel = new BroadcastChannel('auth');

// 标签页 A 中登出
function logout() {
  localStorage.removeItem('token');
  authChannel.postMessage({ type: 'LOGOUT' });
  window.location.href = '/login';
}

// 标签页 B、C 监听并同步登出
authChannel.onmessage = (event) => {
  if (event.data.type === 'LOGOUT') {
    window.location.href = '/login';
  }
};
```

---

## 跨源 iframe 通信

**父窗口 → iframe**
`iframe.contentWindow.postMessage(<data>, <origin>)`

```html
<!-- 父页面 -->
<iframe id="embed" src="https://embed.example.com/widget"></iframe>
<script>
  const iframe = document.getElementById('embed');
  iframe.addEventListener('load', () => {
    iframe.contentWindow.postMessage(
      { type: 'CONFIG', theme: 'dark' },
      'https://embed.example.com'
    );
  });
</script>
```

**iframe → 父窗口**
`window.parent.postMessage(<data>, <origin>)`

```javascript
// iframe 内部
window.addEventListener('message', (event) => {
  if (event.origin !== 'https://parent.com') return;
  if (event.data.type === 'CONFIG') {
    applyConfig(event.data);
    // 通知父窗口配置已应用
    window.parent.postMessage({ type: 'CONFIG_APPLIED' }, 'https://parent.com');
  }
});
```

---

## 注意事项

- **origin 验证必须**:`message` 事件中必须验证 `event.origin`,否则会有 XSS 风险
- **targetOrigin 指定**:发送时必须指定确切目标源,避免使用 `'*'`
- **结构化克隆**:`postMessage` 数据通过结构化克隆算法传递,支持对象、数组、Map、Set 等
- **不可传递对象**:Function、DOM 节点、Window 等不能直接传递
- **Transferable Objects**:MessagePort、ArrayBuffer 等可通过 `transfer` 参数转移所有权
- **同源策略**:`BroadcastChannel` 仅在同源标签页之间工作
- **性能**:大对象通过 `postMessage` 传递时建议使用 Transferable Objects 避免拷贝



<!-- ============ 文档分隔线：006-html5/007-HTML5OfflineStorageWebAPI.md ============ -->

# 离线存储与WebAPI 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数 | `{ }` 分组 | `|` 或 | `...` 重复

---

## Web Storage API

**localStorage 永久存储**
`localStorage.setItem(<key>, <value>)` / `localStorage.getItem(<key>)`

```javascript
// 存储数据(键值对,值必须为字符串)
localStorage.setItem('name', 'Alice');
localStorage.setItem('age', '30');

// 读取数据
const name = localStorage.getItem('name');  // 'Alice'
const age = localStorage.getItem('age');    // '30'

// 删除指定键
localStorage.removeItem('age');

// 清除所有数据
localStorage.clear();

// 遍历所有键
for (let i = 0; i < localStorage.length; i++) {
  const key = localStorage.key(i);
  console.log(`${key}: ${localStorage.getItem(key)}`);
}
```

**存储对象(序列化)**
`localStorage.setItem(<key>, JSON.stringify(<obj>))`

```javascript
// localStorage 只能存储字符串,对象需先序列化
const user = { name: 'Bob', age: 25, email: 'bob@example.com' };
localStorage.setItem('user', JSON.stringify(user));

// 读取后反序列化
const storedUser = JSON.parse(localStorage.getItem('user'));
console.log(storedUser.name); // 'Bob'
```

**sessionStorage 会话存储**
`sessionStorage.setItem(<key>, <value>)`

```javascript
// 数据仅在当前标签页会话内有效,关闭标签页即清除
sessionStorage.setItem('token', 'abc123');
const token = sessionStorage.getItem('token');
sessionStorage.removeItem('token');
sessionStorage.clear();
```

**Web Storage 方法表**

| 方法/属性          | 说明                       |
| ------------------ | -------------------------- |
| `setItem(k, v)`    | 存储键值                   |
| `getItem(k)`       | 读取键值                   |
| `removeItem(k)`    | 删除指定键                 |
| `clear()`          | 清除所有键值               |
| `key(index)`       | 根据索引获取键名           |
| `length`           | 已存储键值对数量           |

**Web Storage 与 Cookie 对比**

| 特性       | localStorage | sessionStorage | Cookie          |
| ---------- | ------------ | -------------- | --------------- |
| 存储容量   | 约 5MB       | 约 5MB         | 约 4KB          |
| 存储时间   | 永久         | 会话期间       | 可设置过期时间  |
| 服务器发送 | 否           | 否             | 是(随请求发送) |
| 作用域     | 同一域名     | 同一标签页     | 可设置路径      |
| API 复杂度 | 简单         | 简单           | 复杂            |

---

## Storage 事件

**跨标签页监听 Storage 变化**
`window.addEventListener('storage', handler)`

```javascript
// 当其他标签页修改 localStorage 时触发
window.addEventListener('storage', (event) => {
  console.log('变更的键:', event.key);
  console.log('旧值:', event.oldValue);
  console.log('新值:', event.newValue);
  console.log('URL:', event.url);
  console.log('存储区域:', event.storageArea);
});
```

**StorageEvent 属性表**

| 属性             | 说明                       |
| ---------------- | -------------------------- |
| `key`            | 变更的键(null 表示 clear)|
| `newValue`       | 新值(null 表示删除)      |
| `oldValue`       | 旧值(null 表示新增)      |
| `url`            | 触发变更的页面 URL         |
| `storageArea`    | 受影响的存储对象           |

---

## Geolocation API

**获取当前位置**
`navigator.geolocation.getCurrentPosition(<success>, [error], [options])`

```javascript
navigator.geolocation.getCurrentPosition(
  (position) => {
    console.log('纬度:', position.coords.latitude);
    console.log('经度:', position.coords.longitude);
    console.log('精度:', position.coords.accuracy + ' 米');
  },
  (error) => {
    console.error('获取位置失败:', error.message);
  },
  {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
  }
);
```

**Position 对象属性表**

| 属性                      | 说明                            |
| ------------------------- | ------------------------------- |
| `coords.latitude`         | 纬度                            |
| `coords.longitude`        | 经度                            |
| `coords.accuracy`         | 位置精度(米)                   |
| `coords.altitude`         | 海拔高度(米)                   |
| `coords.altitudeAccuracy` | 海拔精度(米)                   |
| `coords.heading`          | 方向(度)                       |
| `coords.speed`            | 速度(米/秒)                    |
| `timestamp`               | 获取位置的时间戳                |

---

## Web Workers

**创建专用 Worker**
`const worker = new Worker(<url>, [options])`

```javascript
// 主线程创建 Worker
const worker = new Worker('worker.js');

// 发送消息给 Worker
worker.postMessage({ type: 'calculate', data: 1000000 });

// 接收 Worker 返回的消息
worker.onmessage = function (event) {
  console.log('计算结果:', event.data);
};

// 处理错误
worker.onerror = function (error) {
  console.error('Worker 错误:', error);
};
```

**Worker 脚本(worker.js)**
`self.onmessage = (event) => { ... }; self.postMessage(<data>)`

```javascript
// Worker 内部接收并处理消息
self.onmessage = function (event) {
  const { type, data } = event.data;
  if (type === 'calculate') {
    let result = 0;
    for (let i = 0; i < data; i++) {
      result += i;
    }
    // 发送结果回主线程
    self.postMessage(result);
  }
};
```

**Worker 方法表**

| 方法/属性                | 说明                          |
| ------------------------ | ----------------------------- |
| `worker.postMessage(d)`  | 向 Worker 发送消息            |
| `worker.onmessage`       | 监听 Worker 消息              |
| `worker.onerror`         | 监听 Worker 错误              |
| `worker.terminate()`     | 终止 Worker(主线程调用)      |
| `self.postMessage(d)`    | Worker 向主线程发送消息       |
| `self.onmessage`         | Worker 监听主线程消息         |
| `self.close()`           | Worker 主动关闭自身           |

**Worker 类型表**

| 类型                | 作用域                | 创建方式                  |
| ------------------- | --------------------- | ------------------------- |
| Dedicated Worker    | 仅创建脚本可用        | `new Worker('url')`       |
| Shared Worker       | 多脚本共享            | `new SharedWorker('url')` |
| Service Worker      | 离线缓存/推送         | `navigator.serviceWorker.register()` |

---

## Service Worker

**注册 Service Worker**
`navigator.serviceWorker.register(<url>, [options])`

```javascript
// 注册 Service Worker(必须在 HTTPS 环境下)
if ('serviceWorker' in navigator) {
  window.addEventListener('load', async () => {
    try {
      const registration = await navigator.serviceWorker.register('/sw.js', {
        scope: '/' // 控制范围
      });
      console.log('注册成功:', registration.scope);
    } catch (error) {
      console.error('注册失败:', error);
    }
  });
}
```

**Service Worker 生命周期事件**
`self.addEventListener('install' | 'activate' | 'fetch', handler)`

```javascript
// sw.js 内部:Service Worker 生命周期事件
const CACHE_NAME = 'my-cache-v1';
const urlsToCache = ['/', '/index.html', '/styles.css', '/script.js'];

// 安装:预缓存资源
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(urlsToCache))
  );
});

// 激活:清理旧缓存
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((name) => {
          if (name !== CACHE_NAME) return caches.delete(name);
        })
      );
    })
  );
});

// 拦截网络请求
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});
```

**缓存策略表**

| 策略                     | 说明                                  | 适用场景          |
| ------------------------ | ------------------------------------- | ----------------- |
| **Cache First**          | 优先缓存,缓存无则请求网络            | 静态资源          |
| **Network First**        | 优先网络,网络失败则使用缓存          | 动态内容          |
| **Cache Only**           | 仅从缓存读取                          | 离线页面          |
| **Network Only**         | 仅从网络获取                          | 实时数据          |
| **Stale While Revalidate** | 先返回缓存,同时请求网络更新缓存    | 可容忍短暂过期的数据 |

---

## Cache Storage API

**CacheStorage 方法表**

| 方法                              | 说明                       |
| --------------------------------- | -------------------------- |
| `caches.open(name)`               | 打开(或创建)命名缓存      |
| `caches.match(request)`           | 在所有缓存中查找匹配       |
| `caches.has(name)`                | 检查缓存是否存在           |
| `caches.delete(name)`             | 删除指定缓存               |
| `caches.keys()`                   | 获取所有缓存名称           |

**Cache 对象方法表**

| 方法                              | 说明                       |
| --------------------------------- | -------------------------- |
| `cache.put(request, response)`    | 存储请求-响应映射          |
| `cache.add(request)`              | fetch + put 的快捷方式     |
| `cache.addAll([requests])`        | 批量 add                   |
| `cache.match(request)`            | 查找匹配的响应             |
| `cache.matchAll([request])`       | 查找所有匹配的响应         |
| `cache.delete(request)`           | 删除指定条目               |
| `cache.keys()`                    | 获取所有请求键              |

```javascript
// Cache First 策略示例
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => {
      return cached || fetch(event.request).then((response) => {
        // 克隆响应(因为响应只能消费一次)
        const responseClone = response.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, responseClone);
        });
        return response;
      });
    })
  );
});
```

---

## Fetch API

**GET 请求**
`fetch(<url>, [options]).then(<handler>)`

```javascript
// 基础 GET 请求
fetch('https://api.example.com/data')
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    return response.json();
  })
  .then((data) => console.log('数据:', data))
  .catch((error) => console.error('错误:', error));
```

**POST 请求**
`fetch(<url>, { method: 'POST', body, headers })`

```javascript
// POST 请求(发送 JSON 数据)
fetch('https://api.example.com/users', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'John', email: 'john@example.com' })
})
  .then((response) => response.json())
  .then((data) => console.log('创建成功:', data))
  .catch((error) => console.error('错误:', error));
```

**fetch 请求选项**
`fetch(<url>, { method, headers, body, mode, credentials, ... })`

```javascript
const options = {
  method: 'GET',                         // GET | POST | PUT | DELETE | PATCH
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token123'
  },
  body: JSON.stringify(data),            // POST/PUT 请求体
  mode: 'cors',                          // cors | no-cors | same-origin
  credentials: 'include',                // include | same-origin | omit
  cache: 'default',                      // default | no-store | reload | no-cache | force-cache
  redirect: 'follow',                    // follow | error | manual
  referrer: 'no-referrer',               // no-referrer | client | <url>
  referrerPolicy: 'no-referrer',         // no-referrer | same-origin | strict-origin
  integrity: 'sha256-abc123',            // 子资源完整性
  keepalive: false,                      // 是否保持请求(页面卸载后)
  signal: abortController.signal         // 用于取消请求
};
```

**取消请求**
`const controller = new AbortController()`

```javascript
// 使用 AbortController 取消 fetch 请求
const controller = new AbortController();

fetch('https://api.example.com/data', { signal: controller.signal })
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => {
    if (error.name === 'AbortError') {
      console.log('请求已取消');
    } else {
      console.error('错误:', error);
    }
  });

// 5 秒后取消请求
setTimeout(() => controller.abort(), 5000);
```

**async/await 用法**
`const response = await fetch(<url>, [options])`

```javascript
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('错误:', error);
    throw error;
  }
}
```

**Response 对象方法表**

| 方法/属性                | 说明                       |
| ------------------------ | -------------------------- |
| `response.ok`            | 状态码 200-299 时为 true   |
| `response.status`        | HTTP 状态码                |
| `response.statusText`    | 状态文本                   |
| `response.headers`       | 响应头对象                 |
| `response.json()`        | 解析为 JSON                 |
| `response.text()`        | 解析为文本                  |
| `response.blob()`        | 解析为 Blob                 |
| `response.arrayBuffer()` | 解析为 ArrayBuffer          |
| `response.formData()`    | 解析为 FormData             |
| `response.clone()`       | 克隆响应                    |

---

## Notification API

**请求通知权限**
`Notification.requestPermission()`

```javascript
// 请求用户授权通知
if ('Notification' in window) {
  Notification.requestPermission().then((permission) => {
    console.log('权限状态:', permission); // granted | denied | default
  });
}
```

**显示通知**
`new Notification(<title>, [options])`

```javascript
// 显示桌面通知
const notification = new Notification('通知标题', {
  body: '通知正文内容',
  icon: '/images/icon.png',
  badge: '/images/badge.png',
  tag: 'unique-tag',          // 用于替换相同标签的通知
  requireInteraction: false,  // 是否需要用户手动关闭
  silent: false               // 是否静默(无声)
});

// 点击通知
notification.onclick = () => {
  window.focus();
  notification.close();
};

// 通知关闭
notification.onclose = () => console.log('通知已关闭');
```

---

## Intersection Observer API

**创建观察器**
`new IntersectionObserver(<callback>, [options])`

```javascript
// 创建视口观察器
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        console.log('元素进入视口:', entry.target);
        entry.target.classList.add('visible');
      } else {
        entry.target.classList.remove('visible');
      }
    });
  },
  {
    root: null,                  // 观察视口(null 表示浏览器视口)
    rootMargin: '0px',           // 根元素边距
    threshold: 0.1               // 目标可见度达到 10% 时触发
  }
);

// 观察元素
const target = document.querySelector('.target');
observer.observe(target);

// 停止观察
observer.unobserve(target);
observer.disconnect(); // 停止所有观察
```

---

## File API

**文件输入**
`<input type="file" accept="image/*" multiple>`

```html
<!-- 单文件选择 -->
<input type="file" id="singleFile" accept="image/*" />

<!-- 多文件选择 -->
<input type="file" id="multiFiles" multiple accept="image/png, image/jpeg" />
```

**FileReader 读取文件**
`new FileReader(); reader.readAsDataURL(<file>)`

```javascript
const fileInput = document.querySelector('input[type="file"]');

fileInput.addEventListener('change', (event) => {
  const file = event.target.files[0]; // File 对象
  console.log('文件名:', file.name);
  console.log('大小:', file.size, 'bytes');
  console.log('类型:', file.type);
  console.log('修改时间:', new Date(file.lastModified).toLocaleString());

  // 使用 FileReader 读取文件
  const reader = new FileReader();
  reader.onload = (e) => {
    const img = document.createElement('img');
    img.src = e.target.result; // Data URL
    document.body.appendChild(img);
  };
  reader.readAsDataURL(file);
});
```

**FileReader 方法表**

| 方法                            | 说明                       |
| ------------------------------- | -------------------------- |
| `readAsText(file, [encoding])`  | 读取为文本                 |
| `readAsDataURL(file)`           | 读取为 Data URL(Base64)   |
| `readAsArrayBuffer(file)`       | 读取为 ArrayBuffer         |
| `readAsBinaryString(file)`      | 读取为二进制字符串         |
| `abort()`                       | 中断读取                   |

**File 对象属性表**

| 属性             | 说明                          |
| ---------------- | ----------------------------- |
| `name`           | 文件名                        |
| `size`           | 文件大小(字节)              |
| `type`           | MIME 类型                     |
| `lastModified`   | 最后修改时间戳(毫秒)        |
| `lastModifiedDate` | 最后修改 Date 对象(已废弃)|

---

## Canvas API

**获取绘图上下文**
`canvas.getContext('2d' | 'webgl')`

```javascript
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d'); // 2D 上下文

// 绘制矩形
ctx.fillStyle = 'red';
ctx.fillRect(10, 10, 100, 50);

// 绘制圆形
ctx.beginPath();
ctx.arc(150, 100, 30, 0, Math.PI * 2);
ctx.fillStyle = 'blue';
ctx.fill();
```

**Canvas 2D 上下文方法表**

| 方法                                | 说明                  |
| ----------------------------------- | --------------------- |
| `fillRect(x, y, w, h)`              | 填充矩形              |
| `strokeRect(x, y, w, h)`            | 描边矩形              |
| `clearRect(x, y, w, h)`             | 清除矩形区域          |
| `beginPath()`                       | 开始路径              |
| `moveTo(x, y)`                      | 移动画笔              |
| `lineTo(x, y)`                      | 画线                  |
| `arc(x, y, r, start, end)`          | 画弧                  |
| `fill()`                            | 填充路径              |
| `stroke()`                          | 描边路径              |
| `drawImage(img, x, y, [w, h])`      | 绘制图像              |
| `fillText(text, x, y)`              | 绘制文本              |

---

## 注意事项

- **HTTPS 要求**:Service Worker、Geolocation、Notification 等 API 仅在安全上下文中可用
- **localStorage 容量**:约 5MB,超出会抛出 `QuotaExceededError`
- **localStorage 同步**:读写操作是同步阻塞主线程的,大数据请用 IndexedDB
- **Worker 限制**:Worker 中无法操作 DOM、window、document,可用 `self`、`navigator`、`fetch` 等
- **Fetch 默认不带 Cookie**:`credentials: 'include'` 才会跨域携带
- **Notification 权限**:必须用户主动触发(如点击)后才能请求
- **Canvas 性能**:大量绘图操作建议使用 `requestAnimationFrame` 优化性能



<!-- ============ 文档分隔线：006-html5/008-HistoryAPI.md ============ -->

# 历史记录 API 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## History 对象属性

**history 属性**
```javascript
history.length;                 // 历史栈中的条目数
history.state;                  // 当前条目的状态对象
history.scrollRestoration;      // 滚动恢复策略 'auto' | 'manual'
```

**scrollRestoration 设置**
```javascript
// 自动恢复滚动位置(默认)
history.scrollRestoration = 'auto';

// 手动管理滚动
history.scrollRestoration = 'manual';

// 查询
if (history.scrollRestoration === 'manual') {
  // 手动恢复
  window.scrollTo(0, savedScrollY);
}
```

---

## 导航方法

**back / forward / go**
```javascript
history.back();       // 后退一页
history.forward();    // 前进一页
history.go(-2);       // 后退 2 步
history.go(1);        // 前进 1 步
history.go(0);        // 刷新当前页
```

| 方法         | 说明               |
| ------------ | ------------------ |
| `back()`     | 等价于 `go(-1)`    |
| `forward()`  | 等价于 `go(1)`     |
| `go(n)`      | 前进/后退 n 步     |

---

## pushState 与 replaceState

**pushState 添加历史条目**
`history.pushState([state], [unused], [url])`
```javascript
// 添加新历史条目
history.pushState({ page: 'about' }, '', '/about');

// 不修改 URL
history.pushState({ page: 'about' }, '');

// 带 state 对象
history.pushState(
  { userId: 123, section: 'profile' },
  '',
  '/users/123/profile'
);

// 查询参数
history.pushState(null, '', '?page=2&sort=desc');

// 锚点
history.pushState(null, '', '#section1');
```

**replaceState 修改当前条目**
`history.replaceState([state], [unused], [url])`
```javascript
// 修改当前历史条目(不新增)
history.replaceState({ page: 'home' }, '', '/home');

// 更新 state 但保留 URL
history.replaceState({ updated: true }, '');
```

**参数说明**

| 参数      | 说明                                              |
| --------- | ------------------------------------------------- |
| `state`   | 状态对象(任意可序列化数据,最大约 640KB)         |
| `unused`  | 历史保留参数,建议传 `''`                          |
| `url`     | 新 URL(必须同源,可相对路径)                     |

> **注意**:`pushState` 和 `replaceState` 不会触发 `popstate` 事件,也不会加载新页面。

---

## popstate 事件

**监听前进/后退**
```javascript
window.addEventListener('popstate', (event) => {
  console.log('state:', event.state); // 历史条目的 state 对象
  if (event.state) {
    renderPage(event.state.page);
  }
});
```

**触发 popstate 的操作**
- 浏览器后退按钮
- 浏览器前进按钮
- `history.back()` / `history.forward()` / `history.go()`
- 点击带 `#` 锚点链接(同源)

**手动触发(测试用)**
```javascript
// 不会触发 popstate
history.pushState({ page: 'test' }, '', '/test');

// 触发 popstate 事件
window.dispatchEvent(new PopStateEvent('popstate', { state: history.state }));
```

---

## hashchange 事件

**URL 锚点变化**
```javascript
window.addEventListener('hashchange', (event) => {
  console.log('旧 hash:', event.oldURL);
  console.log('新 hash:', event.newURL);
  console.log('当前 hash:', location.hash);
});

// 通过修改 hash 触发
location.hash = 'section2';
```

---

## SPA 路由实现

**HashRouter 哈希路由**
```javascript
class HashRouter {
  constructor() {
    this.routes = {};
    window.addEventListener('hashchange', () => this.resolve());
    window.addEventListener('load', () => this.resolve());
  }

  addRoute(path, handler) {
    this.routes[path] = handler;
    return this;
  }

  navigate(path) {
    location.hash = path;
  }

  resolve() {
    const path = location.hash.slice(1) || '/';
    (this.routes[path] || this.routes['*'])?.();
  }
}

// 使用
const router = new HashRouter();
router
  .addRoute('/', () => renderHome())
  .addRoute('/about', () => renderAbout())
  .addRoute('/contact', () => renderContact());

// 导航
router.navigate('/about'); // URL 变为 #/about
```

**HistoryRouter History API 路由**
```javascript
class HistoryRouter {
  constructor() {
    this.routes = {};
    window.addEventListener('popstate', () => this.resolve());

    // 拦截链接点击
    document.addEventListener('click', (e) => {
      const link = e.target.closest('a[href]');
      if (link && link.origin === location.origin) {
        e.preventDefault();
        this.navigate(link.pathname);
      }
    });
  }

  addRoute(path, handler) {
    this.routes[path] = handler;
    return this;
  }

  navigate(path, state = {}) {
    history.pushState(state, '', path);
    this.resolve();
  }

  resolve() {
    const path = location.pathname;
    (this.routes[path] || this.routes['*'])?.(history.state);
  }
}

// 使用
const router = new HistoryRouter();
router
  .addRoute('/', () => renderHome())
  .addRoute('/users', () => renderUsers())
  .addRoute('/users/:id', () => renderUserDetail());
```

---

## URL 对象操作

**URL 解析**
```javascript
const url = new URL('https://example.com/path?name=Alice&age=30#section');

url.protocol; // 'https:'
url.host;     // 'example.com'
url.hostname; // 'example.com'
url.port;     // ''
url.pathname; // '/path'
url.search;   // '?name=Alice&age=30'
url.hash;     // '#section'
url.origin;   // 'https://example.com'
```

**URLSearchParams 查询参数**
```javascript
const params = new URLSearchParams('?name=Alice&age=30');

params.get('name');      // 'Alice'
params.getAll('tag');    // 数组
params.has('age');       // true
params.set('age', '25'); // 修改
params.append('tag', 'a'); // 添加
params.delete('name');   // 删除
params.toString();       // 'age=25&tag=a'

// 遍历
for (const [key, value] of params) {
  console.log(key, value);
}
```

**修改当前 URL 参数**
```javascript
const url = new URL(location.href);
url.searchParams.set('page', '2');
url.searchParams.delete('filter');
history.pushState(null, '', url.toString());
```

---

## 注意事项

**同源策略**
```javascript
// 错误:跨域 URL
history.pushState(null, '', 'https://other.com/page'); // 抛出 SecurityError

// 正确:同源 URL
history.pushState(null, '', '/page');
history.pushState(null, '', location.origin + '/page');
```

**state 大小限制**
```javascript
// 状态对象最大约 640KB(序列化后)
history.pushState({ data: 'large data...' }, '', '/page');

// 推荐用 sessionStorage / IndexedDB 存储大对象
sessionStorage.setItem('pageState', JSON.stringify(largeData));
history.pushState({ storageKey: 'pageState' }, '', '/page');
```

**服务端配置**
```javascript
// SPA 所有路由需服务端返回 index.html
// Nginx 配置示例:
// location / {
//   try_files $uri $uri/ /index.html;
// }
```



<!-- ============ 文档分隔线：006-html5/009-LinkageAnchor.md ============ -->

# 链接与锚点 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 超链接基础

**a 锚点元素**
`<a href="<URL>" [target="<目标>"] [rel="<关系>"] [download[="<文件名>"]] [type="<MIME>"]>[文本]</a>`
```html
<!-- 外部网站 -->
<a href="https://example.com">访问示例网站</a>

<!-- 邮件链接(带主题) -->
<a href="mailto:contact@example.com?subject=Hello">发送邮件</a>

<!-- 电话链接 -->
<a href="tel:+861012345678">拨打电话</a>

<!-- 短信链接 -->
<a href="sms:+861012345678?body=你好">发送短信</a>

<!-- 下载文件 -->
<a href="document.pdf" download="自定义文件名.pdf">下载文件</a>
```

| href 协议 | 用途         | 示例                              |
| --------- | ------------ | --------------------------------- |
| `http(s)` | 网页         | `https://example.com`             |
| `mailto`  | 邮件         | `mailto:user@example.com`         |
| `tel`     | 电话         | `tel:+861012345678`               |
| `sms`     | 短信         | `sms:+861012345678`               |
| `#`       | 锚点         | `#section1`                       |
| `javascript` | 脚本(不推荐) | `javascript:void(0)`           |

---

## target 属性

**链接打开方式**

| 值        | 行为                 |
| --------- | -------------------- |
| `_self`   | 当前窗口打开(默认)   |
| `_blank`  | 新窗口/标签页打开    |
| `_parent` | 父框架中打开         |
| `_top`    | 顶层窗口中打开       |
| `<名称>`  | 指定名称的窗口/框架  |

```html
<!-- 新窗口打开(安全写法) -->
<a href="https://example.com" target="_blank" rel="noopener noreferrer">外部链接</a>
```

> 安全提示:使用 `target="_blank"` 时务必添加 `rel="noopener noreferrer"`,防止新窗口通过 `window.opener` 操纵原窗口。

---

## rel 属性

**链接关系**

| rel 值        | 作用                              |
| ------------- | --------------------------------- |
| `noopener`    | 新窗口无法访问 window.opener      |
| `noreferrer`  | 不发送 Referer 头                 |
| `nofollow`    | 搜索引擎不传递权重                |
| `ugc`         | 用户生成内容                      |
| `sponsored`   | 付费链接                          |
| `bookmark`    | 永久书签                          |
| `next`        | 下一页                            |
| `prev`        | 上一页                            |
| `canonical`   | 规范化 URL                        |
| `alternate`   | 替代版本(如 RSS、其他语言)        |
| `license`     | 版权信息                          |
| `help`        | 帮助文档                          |

```html
<!-- 综合示例 -->
<a rel="noopener noreferrer">无 opener 不发送 Referer</a>
<a rel="nofollow">不传递权重</a>
<a rel="ugc">用户生成内容</a>
<a rel="sponsored">广告链接</a>
```

---

## 锚点与页面内导航

**页面内跳转**
`<a href="#<ID>">[文本]</a>` + `<[元素] id="<ID>">`
```html
<!-- 跳转到指定 ID -->
<h2 id="section1">第一节</h2>
<a href="#section1">跳转到第一节</a>

<!-- 跳回顶部 -->
<a href="#">回到顶部</a>

<!-- 跨页面锚点 -->
<a href="page.html#section1">跳到其他页面的第一节</a>
```

**平滑滚动**
```css
html {
  scroll-behavior: smooth;
}

/* 锚点偏移(避免被固定头部遮挡) */
[id] {
  scroll-margin-top: 80px;
}
```

**JavaScript 滚动**
```javascript
// 平滑滚动到元素
document.getElementById('section1').scrollIntoView({
  behavior: 'smooth',
  block: 'start'
});

// 滚动到顶部
window.scrollTo({ top: 0, behavior: 'smooth' });
```

---

## 路径系统

**绝对路径**
```html
<!-- 完整 URL -->
<a href="https://example.com/page.html">完整 URL</a>

<!-- 根目录开始 -->
<a href="/about/index.html">根目录开始</a>
```

**相对路径**
```html
<!-- 同目录 -->
<a href="page.html">同目录</a>

<!-- 子目录 -->
<a href="sub/page.html">子目录</a>

<!-- 父目录 -->
<a href="../page.html">父目录</a>

<!-- 上两级 -->
<a href="../../page.html">上两级</a>
```

| 路径         | 含义               |
| ------------ | ------------------ |
| `/path`      | 根目录绝对路径     |
| `./page`     | 当前目录(可省略)   |
| `../page`    | 上级目录           |
| `page.html`  | 相对当前页面       |
| `//host/path`| 协议相对路径       |

---

## 链接可访问性

**描述性链接文本**
```html
<!-- 正确:描述性文本 -->
<a href="report.pdf">查看2026年度报告</a>

<!-- 错误:无意义文本 -->
<a href="report.pdf">点击这里</a>
```

**跳过导航链接**
```html
<!-- 键盘用户跳过重复导航 -->
<body>
  <a href="#main-content" class="skip-link">跳到主要内容</a>
  <header>...</header>
  <main id="main-content">...</main>
</body>

<style>
  .skip-link {
    position: absolute;
    left: -9999px;
  }
  .skip-link:focus {
    left: 0;
    top: 0;
    background: #fff;
    padding: 1rem;
  }
</style>
```

---

## 链接状态 CSS

**链接伪类**
```css
a:link    { color: blue; }       /* 未访问 */
a:visited { color: purple; }     /* 已访问 */
a:hover   { color: red; }        /* 悬停 */
a:focus   { outline: 2px solid; } /* 聚焦 */
a:active  { color: orange; }     /* 点击时 */
```

---

## Ping 追踪

**ping 属性**
`<a href="<URL>" ping="<追踪URL>">[文本]</a>`
```html
<!-- 浏览器会向 ping 指定的 URL 发送 POST 请求 -->
<a href="https://example.com" ping="https://track.example.com/click">链接</a>
```



<!-- ============ 文档分隔线：006-html5/010-List.md ============ -->

# 列表 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 无序列表

**ul 无序列表**
`<ul [type="disc|circle|square|none"]>...<li>[项]</li>...</ul>`
```html
<!-- 默认实心圆 -->
<ul>
  <li>苹果</li>
  <li>香蕉</li>
  <li>橙子</li>
</ul>
```

**CSS 列表样式**
```css
ul { list-style-type: disc; }    /* 实心圆(默认) */
ul { list-style-type: circle; }  /* 空心圆 */
ul { list-style-type: square; }  /* 实心方块 */
ul { list-style-type: none; }    /* 无标记 */
```

---

## 有序列表

**ol 有序列表**
`<ol [start="<起始>"] [reversed] [type="1|A|a|I|i"]>...<li>[项]</li>...</ol>`
```html
<!-- 默认数字编号 -->
<ol>
  <li>第一步</li>
  <li>第二步</li>
</ol>

<!-- 从 5 开始 -->
<ol start="5">
  <li>第五项</li>
  <li>第六项</li>
</ol>

<!-- 倒序 -->
<ol reversed>
  <li>第三项</li>
  <li>第二项</li>
</ol>

<!-- 字母编号 -->
<ol type="A">
  <li>选项 A</li>
  <li>选项 B</li>
</ol>
```

| type 值 | 编号样式     | 示例       |
| ------- | ------------ | ---------- |
| `1`     | 数字(默认)   | 1, 2, 3    |
| `A`     | 大写字母     | A, B, C    |
| `a`     | 小写字母     | a, b, c    |
| `I`     | 大写罗马数字 | I, II, III |
| `i`     | 小写罗马数字 | i, ii, iii |

**CSS 列表样式**
```css
ol { list-style-type: decimal; }            /* 1, 2, 3 */
ol { list-style-type: lower-roman; }        /* i, ii, iii */
ol { list-style-type: upper-roman; }        /* I, II, III */
ol { list-style-type: cjk-ideographic; }    /* 一, 二, 三 */
```

**li 元素**
`<li [value="<数值>"]>[内容]</li>`
```html
<!-- value 改变当前项编号 -->
<ol>
  <li>第一项</li>
  <li value="5">第五项</li>
  <li>第六项</li>
</ol>
```

---

## CSS 自定义计数器

**计数器实现复杂编号**
```css
ol.custom {
  counter-reset: section;
  list-style: none;
}
ol.custom li {
  counter-increment: section;
}
ol.custom li::before {
  content: '第' counter(section) '章:';
  font-weight: bold;
  margin-right: 0.5em;
}
```

```html
<ol class="custom">
  <li>入门</li>
  <li>进阶</li>
  <li>高级</li>
</ol>
```

---

## 定义列表

**dl 定义列表**
`<dl>...<dt>[术语]</dt><dd>[描述]</dd>...</dl>`
```html
<!-- 术语-描述成对 -->
<dl>
  <dt>HTML</dt>
  <dd>超文本标记语言</dd>
  <dt>CSS</dt>
  <dd>层叠样式表</dd>
</dl>
```

**多对多关系**
```html
<!-- 一个术语多个定义 -->
<dl>
  <dt>Java</dt>
  <dd>一种编程语言</dd>
  <dd>一种咖啡</dd>
</dl>

<!-- 多个术语一个定义 -->
<dl>
  <dt>JS</dt>
  <dt>JavaScript</dt>
  <dd>一种脚本语言</dd>
</dl>
```

---

## 嵌套列表

**列表嵌套**
```html
<!-- 多层嵌套无序列表 -->
<ul>
  <li>HTML 基础
    <ul>
      <li>标签语法</li>
      <li>语义化标签</li>
    </ul>
  </li>
  <li>CSS 基础
    <ol>
      <li>选择器</li>
      <li>盒模型</li>
    </ol>
  </li>
</ul>
```

---

## 列表布局技巧

**导航栏布局**
```css
/* 重置列表样式 */
ul, ol {
  list-style: none;
  margin: 0;
  padding: 0;
}

/* 横向导航 */
ul.nav {
  display: flex;
  gap: 1rem;
}
```

**自定义标记**
```css
ul.custom-mark li {
  position: relative;
  padding-left: 1.5em;
}
ul.custom-mark li::before {
  content: '►';
  position: absolute;
  left: 0;
  color: green;
}
```

---

## menu 元素

**menu 菜单列表(HTML 2023)**
`<menu>...<li>[项]</li>...</menu>`
```html
<!-- 工具栏/命令列表 -->
<menu>
  <li><button onclick="save()">保存</button></li>
  <li><button onclick="open()">打开</button></li>
  <li><button onclick="exit()">退出</button></li>
</menu>
```



<!-- ============ 文档分隔线：006-html5/011-EmbeddedContent.md ============ -->

# 嵌入式内容 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## iframe 内联框架

**iframe 元素**
`<iframe src="<URL>" [width="<宽>"] [height="<高>"] [title="<标题>"] [sandbox="<策略>"] [allow="<功能>"] [loading="lazy|eager"]></iframe>`
```html
<!-- 基础 iframe -->
<iframe src="https://example.com" width="800" height="600" title="嵌入页面"></iframe>

<!-- 完整安全配置 -->
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

**iframe 属性**

| 属性             | 作用                          |
| ---------------- | ----------------------------- |
| `src`            | 嵌入页面 URL                  |
| `srcdoc`         | 内联 HTML 内容                |
| `name`           | 框架名称(target 用)          |
| `sandbox`        | 沙箱安全策略                  |
| `allow`          | 权限策略(摄像头、麦克风等)   |
| `loading`        | 懒加载 lazy / eager           |
| `referrerpolicy` | Referer 策略                  |
| `title`          | 无障碍标题(必填)             |

---

## sandbox 沙箱策略

**安全沙箱**
`<iframe src="<URL>" sandbox="<策略列表>">`
```html
<!-- 完全沙箱(禁用所有功能) -->
<iframe src="untrusted.html" sandbox></iframe>

<!-- 部分启用 -->
<iframe src="widget.html" sandbox="allow-scripts allow-forms allow-same-origin"></iframe>
```

| sandbox 值                   | 允许的功能                |
| ---------------------------- | ------------------------- |
| (空)                         | 禁止所有                  |
| `allow-scripts`              | 执行脚本                  |
| `allow-same-origin`          | 同源请求                  |
| `allow-forms`                | 提交表单                  |
| `allow-popups`               | 弹窗(window.open)        |
| `allow-modals`               | 模态对话框(alert/confirm)|
| `allow-orientation-lock`     | 屏幕方向锁定              |
| `allow-pointer-lock`         | 鼠标锁定                  |
| `allow-presentation`         | 全屏演示                  |
| `allow-top-navigation`       | 顶层窗口导航              |
| `allow-downloads`            | 下载                      |

> 安全警告:同时使用 `allow-scripts` 和 `allow-same-origin` 可能导致沙箱被绕过。

---

## allow 权限策略

**Permissions Policy**
`<iframe src="<URL>" allow="<功能列表>">`
```html
<!-- 允许摄像头和麦克风 -->
<iframe src="video.html" allow="camera; microphone"></iframe>

<!-- 允许全屏和地理位置 -->
<iframe src="map.html" allow="fullscreen; geolocation"></iframe>

<!-- 限定来源 -->
<iframe
  src="https://example.com"
  allow="camera https://example.com; microphone https://example.com"
></iframe>
```

| 权限           | 说明          |
| -------------- | ------------- |
| `camera`       | 摄像头        |
| `microphone`   | 麦克风        |
| `geolocation`  | 地理位置      |
| `fullscreen`   | 全屏          |
| `autoplay`     | 自动播放      |
| `clipboard-read` | 剪贴板读取  |
| `clipboard-write` | 剪贴板写入 |
| `payment`      | 支付          |
| `usb`          | USB 设备      |

---

## srcdoc 内联内容

**内联 HTML**
`<iframe srcdoc="<HTML字符串>" [sandbox]></iframe>`
```html
<!-- 直接嵌入 HTML -->
<iframe srcdoc="<h1>内联内容</h1><p>Hello</p>" sandbox="allow-scripts"></iframe>

<!-- 配合 JavaScript 动态内容 -->
<iframe id="frame" sandbox="allow-scripts"></iframe>
<script>
  const html = `
    <h1>动态内容</h1>
    <p>当前时间:${new Date().toLocaleString()}</p>
  `;
  document.getElementById('frame').srcdoc = html;
</script>
```

---

## embed 与 object

**embed 元素**
`<embed src="<URL>" [type="<MIME>"] [width] [height] />`
```html
<!-- 嵌入 PDF -->
<embed src="document.pdf" type="application/pdf" width="800" height="600" />

<!-- 嵌入 Flash(已废弃) -->
<embed src="animation.swf" type="application/x-shockwave-flash" />
```

**object 元素**
`<object data="<URL>" [type="<MIME>"] [width] [height]>[回退内容]</object>`
```html
<!-- 嵌入 PDF(带回退) -->
<object data="document.pdf" type="application/pdf" width="800" height="600">
  <p>您的浏览器不支持 PDF 预览,请<a href="document.pdf">下载查看</a></p>
</object>

<!-- 嵌入图像 -->
<object data="chart.svg" type="image/svg+xml" width="400" height="300">
  <img src="chart.png" alt="图表" />
</object>
```

**embed vs object**

| 特性       | embed            | object                  |
| ---------- | ---------------- | ----------------------- |
| 自闭合     | 是               | 否                      |
| 回退内容   | 不支持           | 支持                    |
| 参数传递   | 通过属性         | 通过 `<param>` 子元素   |
| 使用场景   | 简单嵌入         | 需要回退的复杂嵌入      |

**param 参数**
`<param name="<名称>" value="<值>" />`
```html
<object data="game.swf" type="application/x-shockwave-flash">
  <param name="quality" value="high" />
  <param name="wmode" value="transparent" />
  <p>需要安装 Flash 插件</p>
</object>
```

---

## iframe 跨文档通信

**postMessage API**
```javascript
// 父页面 → iframe
const iframe = document.getElementById('myFrame');
iframe.contentWindow.postMessage(
  { type: 'DATA', payload: 'hello' },
  'https://example.com' // 必须指定目标源
);

// iframe → 父页面
window.parent.postMessage({ type: 'CHILD_READY' }, 'https://parent.com');

// 接收消息
window.addEventListener('message', (event) => {
  // 校验来源(防 XSS)
  if (event.origin !== 'https://example.com') return;
  console.log('收到消息:', event.data);
  console.log('来源:', event.origin);
  console.log('来源窗口:', event.source);
});
```

---

## video 与 audio 嵌入

**通过 iframe 嵌入视频**
```html
<!-- YouTube 嵌入 -->
<iframe
  src="https://www.youtube.com/embed/VIDEO_ID"
  width="560" height="315"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen
></iframe>

<!-- Bilibili 嵌入 -->
<iframe src="//player.bilibili.com/player.html?bvid=BVxxxx" width="100%" height="500" allowfullscreen></iframe>
```

---

## picture 与 source

**source 元素**
`<source src="<URL>" [type="<MIME>"] [media="<媒体查询>"] [srcset="<URL>"] />`
```html
<!-- 多格式图像回退 -->
<picture>
  <source srcset="photo.avif" type="image/avif" />
  <source srcset="photo.webp" type="image/webp" />
  <img src="photo.jpg" alt="照片" />
</picture>

<!-- 视频多格式 -->
<video controls>
  <source src="movie.webm" type="video/webm" />
  <source src="movie.mp4" type="video/mp4" />
  您的浏览器不支持视频。
</video>
```

---

## 嵌入地图

**iframe 嵌入地图**
```html
<!-- 高德地图 -->
<iframe
  src="https://uri.amap.com/marker?position=经度,纬度&name=位置名称"
  width="600" height="450"
  style="border:0;"
  loading="lazy"
  title="地图"
></iframe>

<!-- Google Maps -->
<iframe
  src="https://www.google.com/maps/embed?pb=..."
  width="600" height="450"
  style="border:0;"
  allowfullscreen=""
  loading="lazy"
  referrerpolicy="no-referrer-when-downgrade"
></iframe>
```



<!-- ============ 文档分隔线：006-html5/012-WebSocket.md ============ -->

# 全双工通信 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## WebSocket 创建

**创建 WebSocket 连接**
`const ws = new WebSocket(<url>, [protocols])`
```javascript
// 基础连接
const ws = new WebSocket('wss://example.com/chat');

// 带子协议
const ws = new WebSocket('wss://example.com/chat', ['chat-v1', 'chat-v2']);

// 事件监听
ws.onopen = () => {
  console.log('连接已建立');
  ws.send('Hello!');
};

ws.onmessage = (e) => {
  console.log('收到消息:', e.data);
};

ws.onclose = (e) => {
  console.log('连接关闭:', e.code, e.reason);
};

ws.onerror = () => {
  console.error('WebSocket 错误');
};
```

**protocols 参数**
```javascript
// 字符串数组,客户端支持的子协议
const ws = new WebSocket('wss://example.com', ['protocol1', 'protocol2']);

// 服务端选择的协议
console.log(ws.protocol); // 'protocol1' 或 'protocol2'
```

---

## WebSocket 状态

**readyState 状态**

| readyState | 常量       | 说明       |
| ---------- | ---------- | ---------- |
| 0          | CONNECTING | 正在连接   |
| 1          | OPEN       | 连接已建立 |
| 2          | CLOSING    | 正在关闭   |
| 3          | CLOSED     | 已关闭     |

```javascript
// 检查连接状态
if (ws.readyState === WebSocket.OPEN) {
  ws.send('消息');
}

// 常量访问
console.log(WebSocket.CONNECTING); // 0
console.log(WebSocket.OPEN);       // 1
console.log(WebSocket.CLOSING);    // 2
console.log(WebSocket.CLOSED);     // 3
```

---

## 发送消息

**send 方法**
`ws.send(<data>)`
```javascript
// 发送文本
ws.send('文本消息');

// 发送 JSON
ws.send(JSON.stringify({ type: 'chat', content: '你好' }));

// 发送 ArrayBuffer
const buffer = new ArrayBuffer(4);
const view = new Uint8Array(buffer);
view[0] = 1;
ws.send(buffer);

// 发送 Blob
const blob = new Blob(['二进制数据'], { type: 'application/octet-stream' });
ws.send(blob);
```

**发送数据类型**

| 数据类型      | 说明                  |
| ------------- | --------------------- |
| `string`      | 文本消息              |
| `ArrayBuffer` | 二进制数据            |
| `Blob`        | 二进制大对象          |
| `TypedArray`  | 类型化数组            |
| `DataView`    | 数据视图              |

**bufferedAmount 缓冲检查**
```javascript
// 检查未发送的数据量
if (ws.bufferedAmount < 1024 * 1024) {
  ws.send(data);
} else {
  console.log('缓冲区已满,等待...');
}
```

---

## 接收消息

**onmessage 事件**
```javascript
ws.onmessage = (e) => {
  // e.data 类型:string / ArrayBuffer / Blob
  console.log('收到:', e.data);
  console.log('来源:', e.origin);
};

// 二进制模式
ws.binaryType = 'arraybuffer'; // 默认 'blob'
ws.onmessage = (e) => {
  if (typeof e.data === 'string') {
    console.log('文本消息:', e.data);
  } else {
    const view = new Uint8Array(e.data);
    console.log('二进制数据:', view);
  }
};
```

---

## 关闭连接

**close 方法**
`ws.close([code], [reason])`
```javascript
// 正常关闭
ws.close();

// 带关闭码和原因
ws.close(1000, '正常关闭');
ws.close(4001, '用户退出');
```

**关闭码规范**

| code  | 说明                       |
| ----- | -------------------------- |
| 1000  | 正常关闭                   |
| 1001  | 端点离开(关闭页面)         |
| 1002  | 协议错误                   |
| 1003  | 不支持的数据类型           |
| 1006  | 异常关闭(无 close 帧)      |
| 1009  | 消息过大                   |
| 1011  | 服务器遇到意外情况         |
| 4000-4999 | 应用自定义范围          |

**close 事件**
```javascript
ws.onclose = (e) => {
  console.log('code:', e.code);       // 关闭码
  console.log('reason:', e.reason);   // 关闭原因
  console.log('wasClean:', e.wasClean); // 是否干净关闭
};
```

---

## 断线重连

**自动重连封装**
```javascript
class ReconnectingWebSocket {
  constructor(url, options = {}) {
    this.url = url;
    this.retries = 0;
    this.options = {
      reconnectInterval: 1000,
      maxRetries: Infinity,
      ...options,
    };
    this.connect();
  }

  connect() {
    this.ws = new WebSocket(this.url);
    this.ws.onopen = (e) => {
      this.retries = 0;
      this.onopen?.(e);
    };
    this.ws.onmessage = (e) => this.onmessage?.(e);
    this.ws.onclose = (e) => {
      this.onclose?.(e);
      if (this.retries < this.options.maxRetries) {
        // 指数退避
        const delay = Math.min(
          this.options.reconnectInterval * Math.pow(1.5, this.retries),
          30000
        );
        this.retries++;
        setTimeout(() => this.connect(), delay);
      }
    };
    this.ws.onerror = (e) => this.onerror?.(e);
  }

  send(data) {
    if (this.ws?.readyState === WebSocket.OPEN) {
      this.ws.send(data);
    }
  }

  close() {
    this.retries = Infinity; // 阻止重连
    this.ws?.close();
  }
}

// 使用
const ws = new ReconnectingWebSocket('wss://example.com/chat');
ws.onmessage = (e) => console.log(e.data);
```

---

## 心跳机制

**心跳检测实现**
```javascript
const HEARTBEAT_INTERVAL = 30000;
const HEARTBEAT_TIMEOUT = 10000;

let heartbeatTimer;
let timeoutTimer;

function startHeartbeat() {
  heartbeatTimer = setInterval(() => {
    if (ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify({ type: 'ping', timestamp: Date.now() }));

      // 等待 pong 响应
      timeoutTimer = setTimeout(() => {
        console.log('心跳超时,重连...');
        ws.close();
      }, HEARTBEAT_TIMEOUT);
    }
  }, HEARTBEAT_INTERVAL);
}

ws.onmessage = (e) => {
  const msg = JSON.parse(e.data);
  if (msg.type === 'pong') {
    clearTimeout(timeoutTimer); // 收到 pong,清除超时
    return;
  }
  // 处理业务消息
};

ws.onopen = startHeartbeat;
ws.onclose = () => clearInterval(heartbeatTimer);
```

---

## HTTP 与 WebSocket 对比

| 特性       | HTTP                | WebSocket       |
| ---------- | ------------------- | --------------- |
| 通信模式   | 请求-响应           | 全双工          |
| 连接       | 短连接(Keep-Alive)  | 持久连接        |
| 服务器推送 | 需轮询或 SSE        | 原生支持        |
| 协议       | HTTP/1.1、HTTP/2、HTTP/3 | ws/wss        |
| 头部开销   | 每次请求带 header   | 连接后无 header |
| 数据格式   | 文本为主            | 文本 + 二进制   |
| 适用场景   | 普通 API 请求       | 实时通信        |

---

## WebSocket vs SSE

**Server-Sent Events (SSE) 单向推送**
```javascript
// SSE 仅服务器→客户端
const eventSource = new EventSource('/api/events');
eventSource.onmessage = (e) => {
  console.log('收到事件:', e.data);
};
eventSource.addEventListener('update', (e) => {
  console.log('自定义事件:', e.data);
});
eventSource.close();
```

| 特性       | WebSocket          | SSE                    |
| ---------- | ------------------ | ---------------------- |
| 通信方向   | 双向               | 服务器→客户端          |
| 协议       | ws/wss             | HTTP                   |
| 自动重连   | 需手动实现         | 内置                   |
| 二进制     | 支持               | 不支持                 |
| 浏览器兼容| 主流               | 除 IE 外主流           |
| 适用场景   | 聊天、游戏、协作   | 通知、股票、日志推送   |

---

## 服务器端握手响应

**WebSocket 握手响应头**
```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
Sec-WebSocket-Protocol: chat-v1
```

**JavaScript 中无直接 API**
握手由浏览器自动处理,开发者只需调用 `new WebSocket()`。
- `ws.url` - 连接 URL
- `ws.protocol` - 选定的子协议
- `ws.extensions` - 使用的扩展

---

## 客户端示例

**简单聊天客户端**
```javascript
class ChatClient {
  constructor(url) {
    this.ws = new WebSocket(url);
    this.ws.onopen = () => console.log('已连接');
    this.ws.onmessage = (e) => {
      const msg = JSON.parse(e.data);
      this.display(msg);
    };
    this.ws.onclose = () => console.log('已断开');
  }

  send(text) {
    this.ws.send(JSON.stringify({
      type: 'message',
      text,
      time: Date.now(),
    }));
  }

  display(msg) {
    console.log(`[${msg.time}] ${msg.text}`);
  }
}

const chat = new ChatClient('wss://chat.example.com');
chat.send('Hello!');
```



<!-- ============ 文档分隔线：006-html5/013-WebRTC.md ============ -->

# 实时通信 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数 | `{ }` 分组 | `|` 或 | `...` 重复

---

## WebRTC 核心组件

**WebRTC 三大组件表**

| 组件                      | 作用                       | 主要对象/方法                |
| ------------------------- | -------------------------- | ---------------------------- |
| **getUserMedia**          | 获取本地媒体流(摄像头/麦克风) | `navigator.mediaDevices.getUserMedia()` |
| **RTCPeerConnection**     | 建立点对点连接             | `new RTCPeerConnection()`    |
| **RTCDataChannel**        | 传输任意数据               | `pc.createDataChannel()`     |

---

## getUserMedia 媒体捕获

**获取本地媒体流**
`const stream = await navigator.mediaDevices.getUserMedia(<constraints>)`

```javascript
// 获取摄像头和麦克风媒体流
const stream = await navigator.mediaDevices.getUserMedia({
  video: true,   // 启用视频
  audio: true    // 启用音频
});

// 将媒体流绑定到 video 元素
const video = document.querySelector('#localVideo');
video.srcObject = stream;
await video.play();
```

**媒体约束条件**
`{ video: { width, height, facingMode }, audio: { echoCancellation, noiseSuppression } }`

```javascript
// 精细化约束视频和音频参数
const stream = await navigator.mediaDevices.getUserMedia({
  video: {
    width: { ideal: 1280 },      // 理想宽度
    height: { ideal: 720 },      // 理想高度
    frameRate: { ideal: 30 },    // 理想帧率
    facingMode: 'user'           // 前置摄像头(user | environment)
  },
  audio: {
    echoCancellation: true,      // 回声消除
    noiseSuppression: true,      // 降噪
    autoGainControl: true        // 自动增益
  }
});
```

**屏幕共享**
`const stream = await navigator.mediaDevices.getDisplayMedia(<constraints>)`

```javascript
// 捕获屏幕、窗口或浏览器标签页(需用户选择)
const stream = await navigator.mediaDevices.getDisplayMedia({
  video: { cursor: 'always' },  // 始终显示鼠标
  audio: false                   // 是否捕获系统音频
});
```

---

## 媒体轨道操作

**MediaStreamTrack 方法表**

| 方法                       | 说明                       |
| -------------------------- | -------------------------- |
| `track.stop()`             | 停止轨道                   |
| `track.enabled = false`    | 静音/禁用轨道              |
| `track.getSettings()`      | 获取当前轨道配置           |
| `track.getCapabilities()`  | 获取设备支持的配置范围     |
| `track.applyConstraints()` | 动态修改约束               |

```javascript
// 遍历并操作媒体轨道
stream.getTracks().forEach((track) => {
  console.log(`轨道类型: ${track.kind}, 状态: ${track.readyState}`);
  // track.stop();        // 停止
  // track.enabled = false; // 禁用
});

// 动态切换摄像头
async function switchCamera() {
  const videoTrack = stream.getVideoTracks()[0];
  const newConstraints = { facingMode: 'environment' };
  await videoTrack.applyConstraints(newConstraints);
}
```

---

## RTCPeerConnection 点对点连接

**创建 PeerConnection**
`const pc = new RTCPeerConnection(<configuration>)`

```javascript
// 创建点对点连接,配置 ICE 服务器(STUN/TURN)
const pc = new RTCPeerConnection({
  iceServers: [
    { urls: 'stun:stun.l.google.com:19302' },                        // STUN 服务器
    { urls: 'turn:turn.example.com', username: 'user', credential: 'pass' } // TURN 服务器
  ],
  iceTransportPolicy: 'all' // all | relay
});
```

**添加本地媒体流**
`stream.getTracks().forEach(track => pc.addTrack(track, stream))`

```javascript
// 将本地媒体轨道添加到连接中
const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
stream.getTracks().forEach((track) => {
  pc.addTrack(track, stream);
});
```

**接收远端媒体流**
`pc.ontrack = (event) => { event.streams[0] }`

```javascript
// 监听远端媒体流到达
pc.ontrack = (event) => {
  console.log('收到远端轨道:', event.track.kind);
  const remoteVideo = document.getElementById('remote');
  remoteVideo.srcObject = event.streams[0];
};
```

---

## ICE 候选交换

**监听 ICE 候选**
`pc.onicecandidate = (event) => { event.candidate }`

```javascript
// 监听本地 ICE 候选,通过信令服务器发送给对端
pc.onicecandidate = (event) => {
  if (event.candidate) {
    // 将候选发送给对端
    sendSignal({ type: 'candidate', candidate: event.candidate });
  } else {
    console.log('ICE 候选收集完成');
  }
};

// 接收对端 ICE 候选
function handleRemoteCandidate(candidate) {
  pc.addIceCandidate(new RTCIceCandidate(candidate));
}
```

**ICE 连接状态**
`pc.oniceconnectionstatechange = () => { pc.iceConnectionState }`

```javascript
// 监听 ICE 连接状态变化
pc.oniceconnectionstatechange = () => {
  const state = pc.iceConnectionState;
  console.log('ICE 状态:', state);
  // checking | connected | completed | disconnected | failed | closed
};
```

---

## SDP 信令交换

**创建并设置 Offer**
`const offer = await pc.createOffer([options])`

```javascript
// 主叫方创建 Offer
const offer = await pc.createOffer({
  offerToReceiveAudio: true,
  offerToReceiveVideo: true
});
await pc.setLocalDescription(offer);
// 通过信令服务器发送 offer 给被叫方
sendSignal({ type: 'offer', sdp: offer });
```

**接收并应答 Offer**
`const answer = await pc.createAnswer()`

```javascript
// 被叫方处理 Offer 并创建 Answer
async function handleOffer(offer) {
  await pc.setRemoteDescription(offer);
  const answer = await pc.createAnswer();
  await pc.setLocalDescription(answer);
  sendSignal({ type: 'answer', sdp: answer });
}

// 主叫方接收 Answer
async function handleAnswer(answer) {
  await pc.setRemoteDescription(answer);
}
```

---

## RTCDataChannel 数据通道

**创建数据通道**
`const channel = pc.createDataChannel(<label>, [options])`

```javascript
// 创建有序数据通道
const channel = pc.createDataChannel('chat', {
  ordered: true,           // 保证送达顺序
  maxRetransmits: 3,       // 最大重传次数
  // maxPacketLifeTime: 3000  // 最大生存时间(毫秒,与 maxRetransmits 二选一)
});

channel.onopen = () => {
  console.log('通道已打开');
  channel.send('Hello!');
};

channel.onmessage = (event) => {
  console.log('收到:', event.data);
};

channel.onclose = () => console.log('通道已关闭');
channel.onerror = (err) => console.error('通道错误:', err);
```

**接收对端数据通道**
`pc.ondatachannel = (event) => { event.channel }`

```javascript
// 被叫方监听对端创建的数据通道
pc.ondatachannel = (event) => {
  const channel = event.channel;
  channel.onmessage = (e) => console.log('收到:', e.data);
  channel.onopen = () => channel.send('已连接');
};
```

---

## 连接关闭与状态

**关闭连接**
`pc.close()`

```javascript
// 关闭点对点连接,释放资源
pc.close();
```

**RTCPeerConnection 状态表**

| 属性                    | 值                                                  |
| ----------------------- | --------------------------------------------------- |
| `connectionState`       | new \| connecting \| connected \| disconnected \| failed \| closed |
| `iceConnectionState`    | new \| checking \| connected \| completed \| disconnected \| failed \| closed |
| `iceGatheringState`     | new \| gathering \| complete                        |
| `signalingState`        | stable \| have-local-offer \| have-remote-offer \| have-local-pranswer \| have-remote-pranswer \| closed |

---

## 安全与权限

- **HTTPS 要求**:WebRTC API 仅在安全上下文(HTTPS 或 localhost)中可用
- **用户授权**:`getUserMedia` 首次调用会弹出权限请求
- **权限查询**:`navigator.permissions.query({ name: 'camera' })` 或 `'microphone'`
- **加密传输**:WebRTC 所有的媒体流和数据通道均强制使用 SRTP/DTLS 加密
- **隐私保护**:摄像头/麦克风指示灯会亮起,提醒用户媒体正在被捕获



<!-- ============ 文档分隔线：006-html5/014-ViewportConfigMobileFirst.md ============ -->

# 视口配置与移动优先 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 视口类型

| 视口类型     | 说明                          |
| ------------ | ----------------------------- |
| 布局视口     | 浏览器用于计算 CSS 布局的视口 |
| 视觉视口     | 用户实际看到的区域            |
| 理想视口     | 设备屏幕的理想尺寸            |

**JavaScript 获取视口尺寸**
```javascript
// 布局视口
console.log(document.documentElement.clientWidth);

// 视觉视口
console.log(window.visualViewport.width);
console.log(window.visualViewport.height);
console.log(window.visualViewport.scale);
```

---

## viewport meta 标签

**视口配置**
`<meta name="viewport" content="<键>=<值>, <键>=<值>, ..." />`
```html
<!-- 标准移动端配置 -->
<meta name="viewport" content="width=device-width, initial-scale=1.0" />

<!-- 完整配置 -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=5.0, user-scalable=yes" />

<!-- 刘海屏适配 -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
```

| 属性            | 值                       | 说明             |
| --------------- | ------------------------ | ---------------- |
| `width`         | device-width / 数值      | 布局视口宽度     |
| `height`        | device-height / 数值     | 布局视口高度     |
| `initial-scale` | 0.1 ~ 10.0               | 初始缩放比例     |
| `minimum-scale` | 0.1 ~ 10.0               | 最小缩放比例     |
| `maximum-scale` | 0.1 ~ 10.0               | 最大缩放比例     |
| `user-scalable` | yes / no                 | 是否允许用户缩放 |
| `viewport-fit`  | auto / contain / cover   | 适配刘海屏       |

---

## 设备像素比(DPR)

**DPR 计算公式**
`DPR = 物理像素 / CSS 像素`

**JavaScript 读取 DPR**
```javascript
// 设备像素比,常见值 1、2、3
console.log(window.devicePixelRatio);

// 监听 DPR 变化
window.matchMedia(`(resolution: ${window.devicePixelRatio}dppx)`).addEventListener('change', () => {
  console.log('DPR 变化');
});
```

---

## 移动优先响应式断点

**响应式断点对照**

| 断点 | 宽度      | 设备     |
| ---- | --------- | -------- |
| xs   | < 576px   | 手机     |
| sm   | ≥ 576px   | 大手机   |
| md   | ≥ 768px   | 平板     |
| lg   | ≥ 992px   | 小桌面   |
| xl   | ≥ 1200px  | 桌面     |
| xxl  | ≥ 1400px  | 大桌面   |

**移动优先 CSS 媒体查询**
```css
/* 移动优先:基础样式优先 */
.container {
  padding: 1rem;
  display: flex;
  flex-direction: column;
}

/* 平板及以上 */
@media (min-width: 768px) {
  .container {
    padding: 2rem;
    flex-direction: row;
  }
}

/* 桌面及以上 */
@media (min-width: 1024px) {
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
}
```

---

## 安全区域适配

**env() 适配刘海屏**
```css
/* 适配顶部刘海 */
.header {
  padding-top: env(safe-area-inset-top);
}

/* 适配底部 Home 指示条 */
.footer {
  padding-bottom: env(safe-area-inset-bottom);
}

/* 左右安全区 */
.sidebar-left {
  padding-left: env(safe-area-inset-left);
}

/* 同时设置 fallback */
.container {
  padding-top: 20px;
  padding-top: env(safe-area-inset-top);
}
```

---

## CSS 媒体查询语法

**媒体查询基础**
`@media <媒体类型> [and (<特性>)] { ... }`
```css
/* 屏幕宽度大于 768px */
@media screen and (min-width: 768px) { ... }

/* 横屏 */
@media screen and (orientation: landscape) { ... }

/* 高分辨率屏幕(Retina) */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) { ... }

/* 暗色模式 */
@media (prefers-color-scheme: dark) {
  body { background: #000; color: #fff; }
}

/* 减少动画 */
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}
```

---

## Picture 元素响应式图片

**响应式图片**
```html
<picture>
  <!-- 大屏加载大图 -->
  <source media="(min-width: 1200px)" srcset="large.jpg" />
  <source media="(min-width: 768px)" srcset="medium.jpg" />
  <!-- 默认小图 -->
  <img src="small.jpg" alt="响应式图片" />
</picture>
```

**srcset 与 sizes**
`<img src="<默认>" srcset="<URL> <宽度>w, <URL> <宽度>w" sizes="<媒体查询> <尺寸>, ..." />`
```html
<img
  src="small.jpg"
  srcset="small.jpg 480w, medium.jpg 768w, large.jpg 1200w"
  sizes="(max-width: 600px) 100vw, 50vw"
  alt="响应式图片"
/>
```

---

## VisualViewport API

**视觉视口 API**
```javascript
// 获取视觉视口
const vv = window.visualViewport;

console.log(vv.width);   // 视觉视口宽度
console.log(vv.height);  // 视觉视口高度
console.log(vv.offsetLeft); // 相对布局视口的 X 偏移
console.log(vv.offsetTop);  // 相对布局视口的 Y 偏移
console.log(vv.scale);   // 缩放比例

// 监听视觉视口变化(键盘弹出等)
vv.addEventListener('resize', () => {
  console.log('视觉视口大小变化');
});

vv.addEventListener('scroll', () => {
  console.log('视觉视口滚动');
});
```

---

## 触摸事件

**触摸事件监听**
`element.addEventListener('<事件>', handler)`
```javascript
const el = document.getElementById('touch-area');

el.addEventListener('touchstart', (e) => {
  console.log('触摸开始', e.touches.length);
});

el.addEventListener('touchmove', (e) => {
  e.preventDefault(); // 阻止默认滚动
  const touch = e.touches[0];
  console.log(`X: ${touch.clientX}, Y: ${touch.clientY}`);
});

el.addEventListener('touchend', (e) => {
  console.log('触摸结束');
});

// 多点触控
el.addEventListener('gesturechange', (e) => {
  console.log('缩放:', e.scale, '旋转:', e.rotation);
});
```

| 触摸事件        | 触发时机       |
| --------------- | -------------- |
| `touchstart`    | 手指触摸屏幕   |
| `touchmove`     | 手指在屏幕移动 |
| `touchend`      | 手指离开屏幕   |
| `touchcancel`   | 触摸被打断     |



<!-- ============ 文档分隔线：006-html5/015-ImageResponsiveImage.md ============ -->

# 图像与响应式图片 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## img 元素

**图像标签**
`<img src="<URL>" alt="<替代文本>" [width="<宽>"] [height="<高>"] [loading="lazy|eager"] [decoding="async|sync|auto"] [srcset] [sizes] />`
```html
<!-- 基础图像 -->
<img src="photo.jpg" alt="美丽的风景" width="800" height="600" />

<!-- 延迟加载 -->
<img src="photo.jpg" alt="照片" loading="lazy" />

<!-- 异步解码 -->
<img src="large.jpg" alt="大图" decoding="async" />

<!-- 错误回退 -->
<img src="photo.jpg" alt="照片" onerror="this.src='fallback.jpg'" />
```

| 属性         | 作用                          |
| ------------ | ----------------------------- |
| `src`        | 图像 URL                      |
| `alt`        | 替代文本(必填,无障碍)         |
| `width`      | 宽度(像素)                   |
| `height`     | 高度(像素)                   |
| `loading`    | lazy 懒加载 / eager 立即加载  |
| `decoding`   | 解码方式 async/sync/auto      |
| `srcset`     | 多源图像列表                  |
| `sizes`      | 不同视口下的显示尺寸          |
| `referrerpolicy` | Referer 策略              |
| `usemap`     | 关联 image map                |

---

## 响应式图片 srcset

**宽度描述符**
`<img srcset="<URL> <宽度>w, <URL> <宽度>w, ..." />`
```html
<!-- 浏览器根据视口自动选择合适尺寸 -->
<img
  src="small.jpg"
  srcset="small.jpg 400w, medium.jpg 800w, large.jpg 1200w"
  alt="响应式图片"
/>
```

**像素密度描述符**
`<img srcset="<URL> 1x, <URL> 2x, <URL> 3x" />`
```html
<!-- Retina 屏适配 -->
<img
  src="photo.jpg"
  srcset="photo.jpg 1x, photo@2x.jpg 2x, photo@3x.jpg 3x"
  alt="高分辨率图片"
/>
```

---

## sizes 属性

**显示尺寸声明**
`<img srcset="..." sizes="<媒体查询> <尺寸>, ... <默认尺寸>" />`
```html
<img
  src="photo.jpg"
  srcset="small.jpg 400w, medium.jpg 800w, large.jpg 1200w"
  sizes="(max-width: 600px) 100vw, (max-width: 1200px) 50vw, 33vw"
  alt="响应式图片"
/>
```

**选择宽度计算**
`选择宽度 = sizes 计算值 × 设备像素比`

```javascript
// JavaScript 读取当前显示的图片
const img = document.querySelector('img');
console.log(img.currentSrc); // 当前加载的 URL
```

---

## picture 元素

**多格式回退**
`<picture><source srcset="<URL>" type="<MIME>" />...<img src="<URL>" alt="<替代>" /></picture>`
```html
<!-- 按格式优先级回退 -->
<picture>
  <source srcset="photo.avif" type="image/avif" />
  <source srcset="photo.webp" type="image/webp" />
  <img src="photo.jpg" alt="照片" width="800" height="600" />
</picture>
```

**按媒体查询切换**
`<source media="<媒体查询>" srcset="<URL>" />`
```html
<!-- 不同视口加载不同图片 -->
<picture>
  <source media="(min-width: 1200px)" srcset="wide.jpg" />
  <source media="(min-width: 768px)" srcset="medium.jpg" />
  <img src="small.jpg" alt="响应式图片" />
</picture>

<!-- 同时指定宽度和格式 -->
<picture>
  <source
    media="(min-width: 1200px)"
    srcset="large.avif 1200w"
    type="image/avif"
  />
  <source
    media="(min-width: 768px)"
    srcset="medium.webp 768w"
    type="image/webp"
  />
  <img src="small.jpg" alt="照片" />
</picture>
```

---

## 图片格式对照

| 格式 | 压缩类型  | 透明度 | 动画 | 压缩率 | 浏览器支持 |
| ---- | --------- | ------ | ---- | ------ | ---------- |
| JPEG | 有损      | 不支持 | 不支持 | 中等 | 全部       |
| PNG  | 无损      | 支持   | 不支持 | 较低 | 全部       |
| WebP | 有损/无损 | 支持   | 支持 | 高   | 97%+       |
| AVIF | 有损/无损 | 支持   | 支持 | 最高 | 92%+       |
| SVG  | 矢量      | 支持   | 支持 | —    | 全部       |
| GIF  | 无损      | 支持   | 支持 | 低   | 全部       |
| APNG | 无损      | 支持   | 支持 | 中等 | 95%+       |

---

## 图片预加载

**link preload**
`<link rel="preload" as="image" href="<URL>" [type="<MIME>"] [imagesrcset] [imagesizes] />`
```html
<!-- 预加载关键图片 -->
<link rel="preload" as="image" href="hero.webp" type="image/webp" />

<!-- 预加载响应式图片 -->
<link
  rel="preload"
  as="image"
  href="small.webp"
  imagesrcset="small.webp 400w, medium.webp 800w, large.webp 1200w"
  imagesizes="100vw"
/>
```

---

## image map 图像映射

**usemap 关联映射**
`<img src="<URL>" usemap="#<map名称>" alt="<替代>" />` + `<map name="<名称>">...<area>...</map>`
```html
<img src="map.png" alt="地图" usemap="#workmap" width="400" height="300" />

<map name="workmap">
  <area shape="rect" coords="34,44,270,350" alt="区域1" href="area1.html" />
  <area shape="circle" coords="337,300,44" alt="区域2" href="area2.html" />
  <area shape="poly" coords="140,21,180,40,150,80" alt="区域3" href="area3.html" />
</map>
```

| shape 值 | coords 含义              |
| -------- | ------------------------ |
| `rect`   | x1,y1,x2,y2              |
| `circle` | center-x,center-y,radius |
| `poly`   | x1,y1,x2,y2,...,xn,yn    |
| `default`| 整个区域                 |

---

## 性能优化技巧

**宽高属性防止布局跳动**
```html
<!-- 指定 width/height,CSS 用比例缩放 -->
<img
  src="photo.jpg"
  alt="照片"
  width="800" height="600"
  style="width: 100%; height: auto;"
/>
```

**fetchpriority 优先级**
```html
<!-- 关键首屏图片 -->
<img src="hero.jpg" alt="主图" fetchpriority="high" />

<!-- 非关键图片 -->
<img src="icon.png" alt="图标" fetchpriority="low" loading="lazy" />
```

**figure 与 figcaption**
```html
<figure>
  <img src="chart.png" alt="销售数据图表" />
  <figcaption>图1:2026年上半年销售数据</figcaption>
</figure>
```



<!-- ============ 文档分隔线：006-html5/016-DragAPI.md ============ -->

# 拖拽API 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数 | `{ }` 分组 | `|` 或 | `...` 重复

---

## draggable 属性

**启用元素拖拽**
`<element draggable="true | false">`

```html
<!-- 将元素标记为可拖拽 -->
<div id="draggable" draggable="true">拖拽我</div>
<div id="dropzone">放置区域</div>

<!-- 图片和带 href 的链接默认可拖拽,无需设置 -->
<img src="logo.png" alt="Logo" />
<a href="/page">链接</a>
```

---

## 拖拽事件

**事件触发顺序表**

| 事件        | 触发对象   | 触发时机             | 用途                    |
| ----------- | ---------- | -------------------- | ----------------------- |
| `dragstart` | 拖拽元素   | 开始拖拽             | 设置拖拽数据            |
| `drag`      | 拖拽元素   | 拖拽过程中持续触发   | 更新状态                |
| `dragend`   | 拖拽元素   | 拖拽结束             | 清理状态                |
| `dragenter` | 放置目标   | 拖拽进入目标         | 高亮放置区域            |
| `dragover`  | 放置目标   | 拖拽在目标上方移动   | **必须 preventDefault** |
| `dragleave` | 放置目标   | 拖拽离开目标         | 取消高亮                |
| `drop`      | 放置目标   | 在目标上释放         | 处理放置逻辑            |

---

## 基本拖拽实现

**HTML 结构**
`<div draggable="true">源</div> <div>目标</div>`

```html
<!-- 拖拽源与放置目标 -->
<div id="draggable" draggable="true">拖拽我</div>
<div id="dropzone">放置区域</div>
```

**JavaScript 事件绑定**
`element.addEventListener('dragstart' | 'dragover' | 'drop', handler)`

```javascript
const draggable = document.getElementById('draggable');
const dropzone = document.getElementById('dropzone');

// 拖拽开始:设置数据与效果
draggable.addEventListener('dragstart', (e) => {
  e.dataTransfer.setData('text/plain', e.target.id); // 设置拖拽数据
  e.dataTransfer.effectAllowed = 'move';             // 允许的效果:copy | move | link
});

// 拖拽悬停:必须阻止默认行为,否则无法触发 drop
dropzone.addEventListener('dragover', (e) => {
  e.preventDefault();
  e.dataTransfer.dropEffect = 'move'; // 设置放置效果
});

// 拖拽进入:高亮目标
dropzone.addEventListener('dragenter', (e) => {
  e.preventDefault();
  dropzone.classList.add('drag-over');
});

// 拖拽离开:取消高亮
dropzone.addEventListener('dragleave', () => {
  dropzone.classList.remove('drag-over');
});

// 放置:处理数据
dropzone.addEventListener('drop', (e) => {
  e.preventDefault();
  dropzone.classList.remove('drag-over');
  const id = e.dataTransfer.getData('text/plain'); // 获取拖拽数据
  const draggedEl = document.getElementById(id);
  dropzone.appendChild(draggedEl);
});
```

---

## DataTransfer 对象

**DataTransfer 方法表**

| 方法                              | 说明                          |
| --------------------------------- | ----------------------------- |
| `setData(format, data)`           | 设置指定格式的数据            |
| `getData(format)`                 | 读取指定格式的数据            |
| `clearData([format])`             | 清除数据                      |
| `setDragImage(img, x, y)`         | 设置自定义拖拽图像            |
| `types`                           | 只读属性,数据格式数组        |
| `files`                           | 只读属性,FileList 对象       |
| `items`                           | 只读属性,DataTransferItemList |

**常用数据格式**
`e.dataTransfer.setData('text/plain' | 'text/uri-list' | 'text/html', data)`

```javascript
// 设置多种格式的数据
e.dataTransfer.setData('text/plain', '纯文本数据');
e.dataTransfer.setData('text/uri-list', 'https://example.com');
e.dataTransfer.setData('text/html', '<strong>HTML 数据</strong>');
e.dataTransfer.setData('application/json', JSON.stringify({ id: 1, name: '张三' }));

// 读取数据(在 drop 事件中)
const text = e.dataTransfer.getData('text/plain');
const json = JSON.parse(e.dataTransfer.getData('application/json'));
```

**拖拽效果设置**
`e.dataTransfer.effectAllowed = 'copy | move | link | copyMove | all | none'`

```javascript
// 设置允许的效果
e.dataTransfer.effectAllowed = 'copy';   // 仅复制
e.dataTransfer.effectAllowed = 'move';   // 仅移动
e.dataTransfer.effectAllowed = 'link';   // 仅链接
e.dataTransfer.effectAllowed = 'copyMove'; // 复制或移动

// 设置放置效果(在 dragover 事件中)
e.dataTransfer.dropEffect = 'copy'; // copy | move | link | none
```

**自定义拖拽图像**
`e.dataTransfer.setDragImage(<element>, <offsetX>, <offsetY>)`

```javascript
// 使用自定义图像作为拖拽预览
draggable.addEventListener('dragstart', (e) => {
  const img = new Image();
  img.src = 'drag-icon.png';
  e.dataTransfer.setDragImage(img, 10, 10); // 偏移量(像素)
});
```

---

## 文件拖拽

**获取拖入的文件**
`e.dataTransfer.files` 或 `e.dataTransfer.items`

```javascript
// 处理拖拽上传的文件
dropzone.addEventListener('drop', (e) => {
  e.preventDefault();
  const files = e.dataTransfer.files; // FileList 对象
  for (const file of files) {
    console.log(`文件名: ${file.name}`);
    console.log(`大小: ${file.size} bytes`);
    console.log(`类型: ${file.type}`);
    console.log(`最后修改: ${new Date(file.lastModified).toLocaleString()}`);
  }
});
```

**异步读取文件内容**
`file.text() | file.arrayBuffer() | reader.readAsDataURL(file)`

```javascript
// 读取文本文件
const text = await file.text();

// 读取为 ArrayBuffer
const buffer = await file.arrayBuffer();

// 使用 FileReader 读取为 Data URL(图片预览)
const reader = new FileReader();
reader.onload = (e) => {
  const img = document.createElement('img');
  img.src = e.target.result;
  document.body.appendChild(img);
};
reader.readAsDataURL(file);
```

---

## 拖拽方向控制

**仅允许垂直/水平拖拽**
`if (Math.abs(dx) > Math.abs(dy)) { ... }`

```javascript
// 限制为水平拖拽
let isDragging = false;
let startX, startY;

element.addEventListener('mousedown', (e) => {
  isDragging = true;
  startX = e.clientX;
  startY = e.clientY;
});

document.addEventListener('mousemove', (e) => {
  if (!isDragging) return;
  const dx = e.clientX - startX;
  const dy = e.clientY - startY;
  // 仅水平方向有效
  if (Math.abs(dx) > Math.abs(dy)) {
    element.style.left = `${dx}px`;
  }
});

document.addEventListener('mouseup', () => {
  isDragging = false;
});
```

---

## 注意事项

- **dragover 必须 preventDefault**:否则 `drop` 事件不会触发
- **数据类型一致性**:`setData` 和 `getData` 的 format 参数必须完全一致
- **安全性**:拖拽内容来源不可信时,需进行数据校验,防止 XSS
- **触摸设备**:原生 HTML5 拖拽 API 在移动端支持有限,需使用 polyfill 或自定义实现
- **可访问性**:拖拽操作对屏幕阅读器不友好,需提供等价的非拖拽操作方式(如按钮)
- **DataTransfer 生命周期**:`getData` 仅在 `drop` 事件中可读取,`dragstart` 中设置的数据在 `dragover` 中无法读取



<!-- ============ 文档分隔线：006-html5/017-MicrodataJSONLD.md ============ -->

# 微数据与JSON-LD 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数 | `{ }` 分组 | `|` 或 | `...` 重复

---

## 结构化数据格式对比

**Microdata 与 JSON-LD 对比表**

| 格式          | 嵌入方式           | 优点                    | 缺点       |
| ------------- | ------------------ | ----------------------- | ---------- |
| **Microdata** | HTML 属性          | 与内容一体,无需额外标签 | HTML 冗余  |
| **JSON-LD**   | `<script>` 标签    | 独立于内容,Google 推荐  | 需额外维护 |
| **RDFa**      | HTML 属性          | 表达力强                | 语法复杂   |

---

## Microdata 微数据

**基本语法**
`<div itemscope itemtype="<schema-url>"> <span itemprop="<property>">值</span> </div>`

```html
<!-- 描述一个 Person 类型对象 -->
<div itemscope itemtype="https://schema.org/Person">
  <span itemprop="name">张三</span>
  <span itemprop="jobTitle">软件工程师</span>
  <span itemprop="email">mailto:zhangsan@example.com</span>
</div>
```

**Microdata 属性表**

| 属性          | 说明                              |
| ------------- | --------------------------------- |
| `itemscope`   | 声明一个项目(对象)               |
| `itemtype`    | 项目类型(Schema.org URL)         |
| `itemprop`    | 项目属性名                        |
| `itemid`      | 项目全局标识符(如 URL)           |
| `itemref`     | 引用其他元素作为项目属性          |
| `itemlist`    | 列表容器                          |

**嵌套对象**
`<div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">`

```html
<!-- 嵌套对象:Person 包含 PostalAddress -->
<div itemscope itemtype="https://schema.org/Person">
  <span itemprop="name">张三</span>
  <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
    <span itemprop="addressLocality">北京</span>
    <span itemprop="postalCode">100000</span>
  </div>
</div>
```

**多值属性**
`<span itemprop="keyword">关键词1</span> <span itemprop="keyword">关键词2</span>`

```html
<!-- 同一属性出现多次表示多值 -->
<div itemscope itemtype="https://schema.org/Article">
  <span itemprop="headline">HTML5 微数据指南</span>
  <span itemprop="keywords">HTML5</span>
  <span itemprop="keywords">Microdata</span>
  <span itemprop="keywords">SEO</span>
</div>
```

---

## JSON-LD 嵌入

**基础语法**
`<script type="application/ld+json"> { ... } </script>`

```html
<!-- 使用 script 标签嵌入 JSON-LD 结构化数据 -->
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "深入理解 HTML5",
    "author": {
      "@type": "Person",
      "name": "张三"
    },
    "datePublished": "2026-06-14",
    "image": "https://example.com/cover.jpg",
    "publisher": {
      "@type": "Organization",
      "name": "示例出版社"
    }
  }
</script>
```

**@graph 多对象嵌入**
`{ "@context": "...", "@graph": [ {obj1}, {obj2} ] }`

```html
<!-- 一次嵌入多个相关对象 -->
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "WebSite",
        "@id": "https://example.com",
        "name": "示例网站",
        "url": "https://example.com"
      },
      {
        "@type": "Organization",
        "@id": "https://example.com/org",
        "name": "示例公司",
        "logo": "https://example.com/logo.png"
      }
    ]
  }
</script>
```

---

## 常用 Schema.org 类型

**Product 产品类型**
`{ "@type": "Product", "name", "offers", "aggregateRating" }`

```html
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "无线蓝牙耳机",
    "image": "https://example.com/earbuds.jpg",
    "description": "降噪蓝牙耳机,续航 24 小时",
    "sku": "SKU-001",
    "brand": {
      "@type": "Brand",
      "name": "ExampleBrand"
    },
    "offers": {
      "@type": "Offer",
      "url": "https://example.com/buy",
      "price": "299.00",
      "priceCurrency": "CNY",
      "availability": "https://schema.org/InStock"
    },
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.5",
      "reviewCount": "128"
    }
  }
</script>
```

**FAQPage 常见问题类型**
`{ "@type": "FAQPage", "mainEntity": [ { "@type": "Question" } ] }`

```html
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "什么是 HTML5?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "HTML5 是超文本标记语言的最新标准,于 2014 年正式发布。"
        }
      },
      {
        "@type": "Question",
        "name": "什么是 Service Worker?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Service Worker 是一种在浏览器后台运行的脚本,可用于实现离线缓存和推送通知。"
        }
      }
    ]
  }
</script>
```

**BreadcrumbList 面包屑导航**
`{ "@type": "BreadcrumbList", "itemListElement": [ { "@type": "ListItem", "position" } ] }`

```html
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "首页",
        "item": "https://example.com"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "产品",
        "item": "https://example.com/products"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "无线耳机"
      }
    ]
  }
</script>
```

**Event 事件类型**
`{ "@type": "Event", "name", "startDate", "location", "offers" }`

```html
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Event",
    "name": "前端技术大会 2026",
    "startDate": "2026-09-15T09:00:00+08:00",
    "endDate": "2026-09-15T18:00:00+08:00",
    "eventStatus": "https://schema.org/EventScheduled",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
    "location": {
      "@type": "Place",
      "name": "北京国际会议中心",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "北京",
        "streetAddress": "朝阳区北辰东路 8 号"
      }
    },
    "image": ["https://example.com/event.jpg"],
    "offers": {
      "@type": "Offer",
      "price": "199.00",
      "priceCurrency": "CNY",
      "availability": "https://schema.org/InStock"
    }
  }
</script>
```

---

## 常用 Schema 类型清单

**Schema.org 主要类型表**

| 类型             | 用途             | 关键属性                                   |
| ---------------- | ---------------- | ------------------------------------------ |
| `Article`        | 文章             | headline, author, datePublished            |
| `Product`        | 产品             | name, offers, brand, aggregateRating       |
| `Offer`          | 商品报价         | price, priceCurrency, availability         |
| `Organization`   | 组织/公司        | name, logo, url, contactPoint              |
| `Person`         | 个人             | name, jobTitle, email, address             |
| `Event`          | 事件             | name, startDate, endDate, location         |
| `FAQPage`        | 常见问题页       | mainEntity                                 |
| `Recipe`         | 食谱             | name, recipeIngredient, cookTime           |
| `Review`         | 评论             | reviewRating, author, itemReviewed         |
| `BreadcrumbList` | 面包屑导航       | itemListElement                            |
| `WebSite`        | 网站             | name, url, potentialAction                 |
| `VideoObject`    | 视频内容         | name, uploadDate, thumbnailUrl, contentUrl |
| `HowTo`          | 教程/操作指南    | step, totalTime, supply                    |

---

## 验证与测试

**官方验证工具**

| 工具                          | 用途                              |
| ----------------------------- | --------------------------------- |
| Google 富摘要测试             | 检测 Google 富摘要支持情况        |
| Schema.org 验证器             | 验证 Schema.org 标记语法          |
| Google Search Console         | 监控结构化数据错误与点击          |
| Bing Webmaster Tools          | Bing 结构化数据报告               |

**验证 URL**

- 富摘要测试: `https://search.google.com/test/rich-results`
- Schema.org 验证器: `https://validator.schema.org/`
- 结构化数据检测: `https://search.google.com/structured-data/testing-tool`

---

## 注意事项

- **JSON-LD 首选**:Google 官方推荐使用 JSON-LD,而非 Microdata
- **数据真实性**:结构化数据必须与页面可见内容一致,否则可能被判定为垃圾信息
- **@context 必填**:JSON-LD 必须包含 `@context: "https://schema.org"`
- **类型一致性**:`@type` 必须是 Schema.org 中定义的合法类型
- **富摘要审核**:部分类型(如 JobPosting、Event)需额外审核才能在搜索结果中显示



<!-- ============ 文档分隔线：006-html5/018-TextSemantic.md ============ -->

# 文本语义 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 标题元素

**六级标题**
`<h1>...</h1>` ~ `<h6>...</h6>`
```html
<!-- 标题用于语义结构,不用于控制字号 -->
<h1>网站主标题</h1>
<h2>章节标题</h2>
<h3>小节标题</h3>
<h4>更小的子节标题</h4>
<h5>五级标题</h5>
<h6>六级标题</h6>
```

---

## 段落与换行

**段落**
`<p>[内容]</p>`
```html
<!-- 段落自动添加上下边距 -->
<p>这是一个段落。</p>
```

**换行**
`<br>` | `<wbr>`
```html
<!-- br 强制换行,wbr 建议换行点(长单词) -->
<p>第一行<br />第二行</p>
<p>超长单词<wbr />可以在<wbr />此处<wbr />断行</p>
```

---

## 强调元素

**文本强调标签**

| 元素       | 语义       | 默认样式 | 使用场景       |
| ---------- | ---------- | -------- | -------------- |
| `<em>`     | 语气强调   | 斜体     | 语音阅读时加重 |
| `<strong>` | 重要性强调 | 粗体     | 标记重要内容   |
| `<mark>`   | 相关性标记 | 黄色高亮 | 搜索结果高亮   |
| `<b>`      | 吸引注意   | 粗体     | 关键词、产品名 |
| `<i>`      | 不同语态   | 斜体     | 术语、外文     |
| `<small>`  | 附属细则   | 小字     | 免责声明       |

```html
<!-- 强调标签综合 -->
<p><em>不要</em>在走廊奔跑</p>
<p><strong>警告:</strong>高压危险</p>
<p>搜索"<mark>HTML5</mark>"的结果</p>
<p>这是 <b>关键词</b>,这是 <i>术语</i>。</p>
<p><small>本活动最终解释权归本公司所有</small></p>
```

---

## 术语与引用

**定义与缩写**
`<dfn>[术语]</dfn>` | `<abbr title="<全称>">[缩写]</abbr>`
```html
<dfn>HTML</dfn>是超文本标记语言
<abbr title="HyperText Markup Language">HTML</abbr>
```

**引用**
`<blockquote cite="<URL>">[内容]</blockquote>` | `<q cite="<URL>">[内容]</q>` | `<cite>[作品名]</cite>`
```html
<!-- 块级引用 -->
<blockquote cite="https://example.com">
  <p>引用文字</p>
</blockquote>

<!-- 行内引用 -->
<p>他说:<q>你好</q></p>

<!-- 作品标题 -->
参考:<cite>JavaScript高级程序设计</cite>
```

---

## 上下标与代码

**上下标**
`<sub>[下标]</sub>` | `<sup>[上标]</sup>`
```html
<!-- 数学公式与化学式 -->
H<sub>2</sub>O
E=mc<sup>2</sup>
```

**代码与键盘**
`<code>[代码]</code>` | `<pre>[预格式化]</pre>` | `<kbd>[按键]</kbd>` | `<samp>[输出]</samp>` | `<var>[变量]</var>`
```html
<!-- 行内代码 -->
<code>console.log()</code>

<!-- 代码块 -->
<pre><code>function hello() {
  console.log('Hello');
}</code></pre>

<!-- 键盘按键 -->
按 <kbd>Ctrl</kbd> + <kbd>C</kbd> 复制

<!-- 程序输出 -->
<samp>Compilation successful</samp>

<!-- 变量 -->
<var>x</var> = 10
```

---

## 修改记录

**删除与插入**
`<del [datetime="<日期>"]>[内容]</del>` | `<ins [datetime="<日期>"]>[内容]</ins>`
```html
<!-- 价格变更 -->
<p>价格:<del datetime="2026-01-01">¥99</del> <ins>¥79</ins></p>
```

---

## 隔离与方向

**双向隔离**
`<bdi>[文本]</bdi>` | `<bdo dir="ltr|rtl">[文本]</bdo>`
```html
<!-- bdi 隔离方向不明的文本(如用户名) -->
<p>用户 <bdi>إبراهيم</bdi> 发表了评论</p>

<!-- bdo 强制文本方向 -->
<bdo dir="rtl">这段文字从右到左显示</bdo>
```

---

## 时间元素

**time 元素**
`<time datetime="<ISO日期>" [pubdate]>[显示文本]</time>`
```html
<!-- 日期 -->
<time datetime="2026-06-14">2026年6月14日</time>

<!-- 日期时间(带时区) -->
<time datetime="2026-06-14T10:30:00+08:00">上午10:30</time>

<!-- 持续时间 -->
<time datetime="PT2H30M">2小时30分钟</time>

<!-- 发布日期 -->
<time datetime="2026-06-14" pubdate>发布于 2026-06-14</time>
```

| 类型     | 格式                | 示例                |
| -------- | ------------------- | ------------------- |
| 日期     | YYYY-MM-DD          | 2026-06-14          |
| 日期时间 | YYYY-MM-DDThh:mm:ss | 2026-06-14T10:30:00 |
| 带时区   | YYYY-MM-DDThh:mm:ssTZD | 2026-06-14T10:30:00+08:00 |
| 持续时间 | PnYnMnDTnHnMnS      | PT2H30M             |

---

## 联系信息

**address 元素**
`<address>...[a|br|文本]...</address>`
```html
<!-- 用于文档作者/文章作者的联系信息 -->
<address>
  <a href="mailto:contact@example.com">contact@example.com</a><br />
  北京市朝阳区某某路123号
</address>
```

---

## 高亮与注音

**ruby 注音**
`<ruby>[字]<rt>[拼音]</rt></ruby>`
```html
<!-- 中日韩文字注音 -->
<ruby>汉<rt>hàn</rt></ruby>字
<ruby>日本<rt>にほん</rt></ruby>
```

**rp 注音回退**
```html
<ruby>
  汉<rp>(</rp><rt>hàn</rt><rp>)</rp>
</ruby>
```



<!-- ============ 文档分隔线：006-html5/019-DocTypeDeclaration.md ============ -->

# 文档类型声明 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## DOCTYPE 声明

**HTML5 文档类型声明**
`<!DOCTYPE html>`
```html
<!-- 文档首行声明,触发标准模式 -->
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="UTF-8" />
    <title>文档类型声明示例</title>
  </head>
  <body>
    <p>这是一个 HTML5 文档</p>
  </body>
</html>
```

**DOCTYPE 历史版本对照**

| 版本             | DOCTYPE 声明                                                    |
| ---------------- | --------------------------------------------------------------- |
| HTML 2.0         | `<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">`            |
| HTML 4.01 Strict | `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "...">`      |
| XHTML 1.0        | `<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "...">` |
| HTML5            | `<!DOCTYPE html>`                                               |

---

## 渲染模式检测

**渲染模式分类**

| 模式             | 触发条件            | 特点                         |
| ---------------- | ------------------- | ---------------------------- |
| 标准模式         | 存在有效的 DOCTYPE  | 按 W3C 标准渲染              |
| 怪异模式         | 缺少 DOCTYPE 或无效 | 模拟旧浏览器行为             |
| 几乎标准模式     | 某些过渡型 DOCTYPE  | 除表格单元格高度外按标准渲染 |

**JavaScript 检测当前模式**
`document.compatMode`
```javascript
// 检测当前渲染模式
if (document.compatMode === 'CSS1Compat') {
  console.log('标准模式');
} else {
  console.log('怪异模式');
}
```

---

## HTML Living Standard 新特性时间线

| 年份 | 新增特性                              |
| ---- | ------------------------------------- |
| 2020 | `loading="lazy"`                      |
| 2021 | `<dialog>` 元素、`popover` 属性       |
| 2022 | Container Queries、`:has()` 选择器    |
| 2023 | View Transitions API、`<search>` 元素 |
| 2024 | CSS Anchor Positioning                |
| 2025 | Declarative Shadow DOM                |



<!-- ============ 文档分隔线：006-html5/020-Accessibility.md ============ -->

# 无障碍访问 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数 | `{ }` 分组 | `|` 或 | `...` 重复

---

## WCAG 标准原则

**WCAG 四大原则表**

| 原则                         | 含义         | 实现示例                      |
| ---------------------------- | ------------ | ----------------------------- |
| **可感知(Perceivable)**      | 信息可被感知 | 图片有 alt 文本、视频有字幕   |
| **可操作(Operable)**         | 界面可操作   | 键盘可访问、有足够操作时间    |
| **可理解(Understandable)**   | 内容可理解   | 清晰语言、一致的导航          |
| **健壮性(Robust)**           | 兼容辅助技术 | 语义化 HTML、ARIA 属性        |

**WCAG 对比度要求表**

| 文本类型                   | WCAG AA | WCAG AAA |
| -------------------------- | ------- | -------- |
| 正文文本(<18px)           | 4.5:1   | 7:1      |
| 大文本(≥18px 或 14px 粗体)| 3:1     | 4.5:1    |
| UI 组件和图形对象          | 3:1     | -        |

---

## 语义化 HTML 与无障碍

**原生元素优先**

```html
<!-- 错误:用 div 模拟按钮,不可键盘聚焦 -->
<div class="btn" onclick="submit()">提交</div>

<!-- 正确:使用原生 button,可键盘聚焦、回车触发 -->
<button type="submit">提交</button>

<!-- 错误:用 div 模拟链接 -->
<div class="link" onclick="navigate()">点击这里</div>

<!-- 正确:使用原生 a 标签 -->
<a href="/page">点击这里</a>
```

**图片无障碍**
`<img src="..." alt="<描述>" | role="presentation" />`

```html
<!-- 有意义的图片:提供 alt 描述 -->
<img src="chart.png" alt="2026年Q1销售额增长15%的柱状图" />

<!-- 装饰性图片:alt 留空 -->
<img src="decorative-line.png" alt="" role="presentation" />

<!-- 图标字体:对辅助技术隐藏 -->
<span class="icon-search" aria-hidden="true"></span>
<span class="sr-only">搜索</span>
```

---

## ARIA 角色

**常用 ARIA role 角色表**

| 角色             | 用途                 | 应用元素示例                |
| ---------------- | -------------------- | --------------------------- |
| `navigation`     | 导航区域             | `<nav role="navigation">`   |
| `main`           | 主要内容             | `<main role="main">`        |
| `banner`         | 页面头部             | `<header role="banner">`    |
| `contentinfo`    | 页面底部             | `<footer role="contentinfo">|
| `alert`          | 警告/通知            | `<div role="alert">`        |
| `dialog`         | 对话框               | `<div role="dialog">`       |
| `alertdialog`    | 警告对话框           | `<div role="alertdialog">`  |
| `tablist`        | 标签列表容器         | `<div role="tablist">`      |
| `tab`            | 标签项               | `<button role="tab">`       |
| `tabpanel`       | 标签面板             | `<div role="tabpanel">`     |
| `progressbar`    | 进度条               | `<div role="progressbar">`  |
| `tooltip`        | 工具提示             | `<div role="tooltip">`      |
| `menu`           | 菜单容器             | `<ul role="menu">`          |
| `menuitem`       | 菜单项               | `<li role="menuitem">`      |
| `listbox`        | 列表选择框           | `<ul role="listbox">`       |
| `option`         | 选项                 | `<li role="option">`        |
| `combobox`       | 组合框               | `<div role="combobox">`     |
| `switch`         | 开关组件             | `<div role="switch">`       |
| `slider`         | 滑块                 | `<div role="slider">`       |

**role 角色应用示例**

```html
<!-- 导航角色 -->
<nav role="navigation" aria-label="主导航">
  <ul>
    <li><a href="/" role="menuitem">首页</a></li>
    <li><a href="/about" role="menuitem">关于</a></li>
  </ul>
</nav>

<!-- 警告通知 -->
<div role="alert">操作成功!</div>

<!-- 模态对话框 -->
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">确认删除</h2>
  <p>确定要删除这条记录吗?</p>
</div>
```

---

## ARIA 属性

**常用 ARIA 属性表**

| 属性                  | 作用                   | 取值示例                          |
| --------------------- | ---------------------- | --------------------------------- |
| `aria-label`          | 不可见标签             | `aria-label="关闭菜单"`           |
| `aria-labelledby`     | 引用其他元素 ID 作为标签 | `aria-labelledby="title-id"`     |
| `aria-describedby`    | 引用其他元素 ID 作为描述 | `aria-describedby="hint-id"`     |
| `aria-hidden`         | 对辅助技术隐藏         | `aria-hidden="true"`              |
| `aria-expanded`       | 展开/折叠状态          | `aria-expanded="true | false"`    |
| `aria-controls`       | 控制的元素 ID          | `aria-controls="menu-id"`         |
| `aria-current`        | 当前项                 | `aria-current="page | step"`      |
| `aria-live`           | 动态内容更新通告       | `aria-live="polite | assertive"`  |
| `aria-atomic`         | 区域整体更新           | `aria-atomic="true"`              |
| `aria-disabled`       | 禁用状态               | `aria-disabled="true"`            |
| `aria-required`       | 必填字段               | `aria-required="true"`            |
| `aria-invalid`        | 校验失败               | `aria-invalid="true"`             |
| `aria-checked`        | 选中状态(switch/checkbox) | `aria-checked="true | false"`  |
| `aria-selected`       | 选中状态(option/tab) | `aria-selected="true"`            |
| `aria-pressed`        | 按下状态(toggle button) | `aria-pressed="true"`           |
| `aria-modal`          | 模态对话框             | `aria-modal="true"`               |
| `aria-haspopup`       | 弹出元素               | `aria-haspopup="menu | dialog"`   |
| `aria-roledescription`| 自定义角色描述         | `aria-roledescription="幻灯片"`   |

**aria-label 与 aria-labelledby**
`aria-label="<文本>"` | `aria-labelledby="<element-id>"`

```html
<!-- aria-label:提供不可见标签 -->
<button aria-label="关闭菜单" class="close-btn">
  <span aria-hidden="true">×</span>
</button>

<!-- aria-labelledby:引用其他元素作为标签 -->
<div id="dialog-title">确认删除</div>
<div role="dialog" aria-labelledby="dialog-title">
  <p>确定要删除这条记录吗?</p>
</div>
```

**aria-expanded 与 aria-controls**
`aria-expanded="true | false"` `aria-controls="<element-id>"`

```html
<!-- 折叠菜单 -->
<button aria-expanded="false" aria-controls="menu">菜单</button>
<ul id="menu" role="menu" hidden>
  <li role="menuitem">选项1</li>
  <li role="menuitem">选项2</li>
</ul>
```

**aria-current 当前页**
`aria-current="page | step | location | date | time | true | false"`

```html
<!-- 面包屑导航 -->
<nav aria-label="面包屑">
  <a href="/">首页</a>
  <a href="/products" aria-current="page">产品</a>
</nav>
```

**aria-live 动态内容通告**
`aria-live="polite | assertive | off"`

```html
<!-- polite:等待用户空闲后通告 -->
<div aria-live="polite" aria-atomic="true" id="status">
  <!-- 动态更新的内容 -->
</div>

<!-- assertive:立即通告(打断当前操作) -->
<div aria-live="assertive" role="alert" id="errors">
  <!-- 错误消息 -->
</div>
```

---

## 表单无障碍

**label 关联**
`<label for="<input-id>">` 或 `<label><input></label>`

```html
<form>
  <!-- 方式1:label 包裹输入框 -->
  <label>
    用户名:
    <input type="text" name="username" required />
  </label>

  <!-- 方式2:label 的 for 属性关联 -->
  <label for="email">邮箱:</label>
  <input type="email" id="email" name="email" required aria-describedby="email-hint" />
  <span id="email-hint" class="hint">请输入有效的邮箱地址</span>

  <!-- 必填字段提示 -->
  <label for="phone">电话:<span aria-label="必填">*</span></label>
  <input type="tel" id="phone" name="phone" required aria-required="true" />

  <!-- 错误提示 -->
  <label for="password">密码:</label>
  <input type="password" id="password" aria-describedby="password-error" aria-invalid="true" />
  <span id="password-error" role="alert" class="error">密码至少需要8个字符</span>

  <!-- 分组表单 -->
  <fieldset>
    <legend>联系方式偏好</legend>
    <label><input type="radio" name="contact" value="email" /> 邮件</label>
    <label><input type="radio" name="contact" value="phone" /> 电话</label>
  </fieldset>
</form>
```

---

## 键盘导航

**tabindex 属性**
`tabindex="0 | -1 | 1+"`

```html
<!-- tabindex="0":可聚焦,按文档顺序 -->
<div class="custom-widget" tabindex="0" role="button">自定义按钮</div>

<!-- tabindex="-1":可编程聚焦,不在 Tab 序列中(适用于模态对话框) -->
<div class="modal" tabindex="-1">...</div>

<!-- 跳过导航链接(放在页面顶部) -->
<a href="#main-content" class="skip-link">跳到主要内容</a>
```

**accesskey 快捷键**
`accesskey="<key>"`

```html
<!-- 通过 Alt+键 触发(浏览器不同组合键不同) -->
<button accesskey="s">保存</button>
<a href="/" accesskey="h">首页</a>
```

**模态对话框焦点陷阱**
`element.addEventListener('keydown', focusTrapHandler)`

```javascript
// 在模态对话框中循环焦点,防止 Tab 跳到外部
function trapFocus(element) {
  const focusableSelectors = [
    'a[href]',
    'button:not([disabled])',
    'input:not([disabled])',
    'select:not([disabled])',
    'textarea:not([disabled])',
    '[tabindex]:not([tabindex="-1"])'
  ];

  const focusableElements = element.querySelectorAll(focusableSelectors.join(','));
  const first = focusableElements[0];
  const last = focusableElements[focusableElements.length - 1];

  element.addEventListener('keydown', (e) => {
    if (e.key !== 'Tab') return;
    if (e.shiftKey) {
      if (document.activeElement === first) {
        last.focus();
        e.preventDefault();
      }
    } else {
      if (document.activeElement === last) {
        first.focus();
        e.preventDefault();
      }
    }
  });

  first.focus(); // 打开时聚焦第一个元素
}
```

---

## 视觉隐藏文本

**sr-only 样式**
`.sr-only { position: absolute; ... }`

```css
/* 视觉隐藏但屏幕阅读器可读取 */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

```html
<!-- 图标按钮添加视觉隐藏文本 -->
<button>
  <i class="fa fa-search" aria-hidden="true"></i>
  <span class="sr-only">搜索</span>
</button>
```

---

## 标签页组件

**Tab 组件完整结构**
`role="tablist" > role="tab" + aria-selected / role="tabpanel" + aria-labelledby`

```html
<div class="tabs">
  <div role="tablist" aria-label="账户设置">
    <button role="tab" id="tab-profile" aria-selected="true" aria-controls="panel-profile">
      个人资料
    </button>
    <button role="tab" id="tab-security" aria-selected="false" aria-controls="panel-security" tabindex="-1">
      安全设置
    </button>
  </div>

  <div role="tabpanel" id="panel-profile" aria-labelledby="tab-profile">
    <h3>个人资料</h3>
    <p>编辑你的个人信息...</p>
  </div>

  <div role="tabpanel" id="panel-security" aria-labelledby="tab-security" hidden>
    <h3>安全设置</h3>
    <p>修改密码和安全选项...</p>
  </div>
</div>
```

---

## 自定义开关组件

**Switch 组件**
`role="switch" aria-checked="true | false" tabindex="0"`

```html
<div class="switch" role="switch" aria-checked="false" aria-label="深色模式" tabindex="0">
  <span class="switch-thumb"></span>
</div>

<script>
  const switchEl = document.querySelector('.switch');
  switchEl.addEventListener('keydown', (e) => {
    if (e.key === ' ' || e.key === 'Enter') {
      e.preventDefault();
      toggleSwitch();
    }
  });

  function toggleSwitch() {
    const isChecked = switchEl.getAttribute('aria-checked') === 'true';
    switchEl.setAttribute('aria-checked', !isChecked);
  }
</script>
```

---

## 颜色与对比度

**对比度示例**

```css
/* AA 通过:深灰文字 #333 在白色 #fff 背景,对比度 12.6:1 */
.text-aa {
  color: #333333;
  background-color: #ffffff;
}

/* AA 未通过:浅灰文字 #999 在白色背景,对比度 2.8:1 */
.text-fail {
  color: #999999;
}

/* 修正:使用更深的灰色,对比度 4.5:1 */
.text-fixed {
  color: #767676;
}
```

**不仅依赖颜色传达信息**

```html
<!-- 错误:仅用颜色区分 -->
<p>请填写 <span style="color:red">红色</span> 标记的字段</p>

<!-- 正确:颜色 + 文字/图标 -->
<p>请填写带 <span class="required"><span aria-hidden="true">*</span>星号</span> 的字段</p>
```

---

## 注意事项

- **原生优先**:使用语义化 HTML 标签(`<button>`、`<nav>`、`<main>`)优先于 ARIA
- **键盘可访问**:所有交互元素必须可通过键盘(Tab/Enter/Space)操作
- **测试工具**:Lighthouse、axe DevTools、NVDA、VoiceOver
- **不滥用 ARIA**:ARIA 用于增强语义,不能替代正确的 HTML 结构
- **aria-hidden 慎用**:对聚焦元素使用 `aria-hidden="true"` 会导致键盘仍可聚焦但屏幕阅读器不可见
- **动态内容**:AJAX 更新内容后,使用 `aria-live` 通告屏幕阅读器



<!-- ============ 文档分隔线：006-html5/021-HTML5ProjectExampleInteractiveFormApplication.md ============ -->

# HTML5 表单与交互 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数 | `{ }` 分组 | `|` 或 | `...` 重复

---

## form 表单容器

**form 元素**
`<form action="<url>" method="GET|POST" [target] [enctype] [autocomplete] [novalidate]></form>`

```html
<!-- 基础表单 -->
<form action="/submit" method="POST">
  <!-- 表单控件 -->
</form>

<!-- 文件上传表单(必须指定 enctype) -->
<form action="/upload" method="POST" enctype="multipart/form-data">
  <input type="file" name="avatar" />
</form>

<!-- 禁用浏览器自动验证 -->
<form action="/submit" method="POST" novalidate>
  <!-- 表单控件 -->
</form>

<!-- 自动填充提示 -->
<form action="/submit" method="POST" autocomplete="on">
  <!-- 表单控件 -->
</form>
```

**form 属性表**

| 属性            | 作用                              | 取值示例                            |
| --------------- | --------------------------------- | ----------------------------------- |
| `action`        | 提交目标 URL                       | `"/submit"`                         |
| `method`        | 提交方法                           | `GET` 或 `POST`                     |
| `enctype`       | 编码类型(POST 时有效)             | `application/x-www-form-urlencoded` |
|                 |                                    | `multipart/form-data`(文件上传)    |
|                 |                                    | `text/plain`                        |
| `target`        | 提交后跳转位置                     | `_self` / `_blank`                  |
| `autocomplete`  | 自动填充                           | `on` / `off`                        |
| `novalidate`    | 禁用浏览器验证                     | 布尔属性                            |
| `accept-charset`| 字符编码                           | `UTF-8`                             |
| `name`          | 表单名称                           | `"loginForm"`                       |

---

## input 输入控件

**input 类型表**

| `type` 值        | 作用                   | 示例                                       |
| ---------------- | ---------------------- | ------------------------------------------ |
| `text`           | 单行文本               | `<input type="text">`                      |
| `password`       | 密码(隐藏字符)        | `<input type="password">`                  |
| `email`          | 邮箱(自带验证)        | `<input type="email">`                     |
| `url`            | URL(自带验证)         | `<input type="url">`                       |
| `tel`            | 电话号码               | `<input type="tel">`                       |
| `number`         | 数字输入               | `<input type="number" min="0" max="100">`  |
| `search`         | 搜索框                 | `<input type="search">`                    |
| `date`           | 日期选择               | `<input type="date">`                      |
| `time`           | 时间选择               | `<input type="time">`                      |
| `datetime-local` | 本地日期时间           | `<input type="datetime-local">`            |
| `month`          | 月份选择               | `<input type="month">`                     |
| `week`           | 周选择                 | `<input type="week">`                      |
| `color`          | 颜色选择器             | `<input type="color" value="#ff0000">`     |
| `range`          | 范围滑块               | `<input type="range" min="0" max="100">`   |
| `file`           | 文件上传               | `<input type="file" accept="image/*">`     |
| `checkbox`       | 复选框                 | `<input type="checkbox" checked>`          |
| `radio`          | 单选框                 | `<input type="radio" name="gender">`       |
| `submit`         | 提交按钮               | `<input type="submit" value="提交">`       |
| `reset`          | 重置按钮               | `<input type="reset">`                     |
| `button`         | 普通按钮               | `<input type="button" value="点击">`       |
| `image`          | 图像提交按钮           | `<input type="image" src="btn.png">`       |
| `hidden`         | 隐藏字段               | `<input type="hidden" name="id">`          |

**input 通用属性表**

| 属性            | 作用                          | 示例                              |
| --------------- | ----------------------------- | --------------------------------- |
| `name`          | 字段名(提交时的键)           | `name="username"`                 |
| `value`         | 字段值                         | `value="default"`                 |
| `placeholder`   | 占位提示文本                  | `placeholder="请输入"`            |
| `required`      | 必填字段                       | 布尔属性                          |
| `disabled`      | 禁用字段                       | 布尔属性                          |
| `readonly`      | 只读字段                       | 布尔属性                          |
| `autofocus`     | 自动聚焦                       | 布尔属性                          |
| `autocomplete`  | 自动填充提示                  | `autocomplete="email"`            |
| `min` / `max`   | 数值/日期范围                  | `min="0" max="100"`               |
| `step`          | 步长                           | `step="0.01"`                     |
| `minlength`     | 最小字符数                    | `minlength="6"`                   |
| `maxlength`     | 最大字符数                    | `maxlength="20"`                  |
| `pattern`       | 正则验证模式                  | `pattern="[0-9]{11}"`             |
| `multiple`      | 允许多选(file/email)         | 布尔属性                          |
| `accept`        | 文件类型过滤(file 专用)      | `accept="image/png, image/jpeg"`  |
| `capture`       | 调用设备摄像头(file 专用)    | `capture="user"`                  |
| `list`          | 关联 datalist                 | `list="browsers"`                 |
| `form`          | 指定所属表单(无需嵌套)      | `form="myForm"`                   |

**常用 input 组合**

```html
<!-- 必填邮箱 -->
<input
  type="email"
  name="email"
  required
  placeholder="example@domain.com"
  autocomplete="email"
/>

<!-- 密码(最少 8 位) -->
<input
  type="password"
  name="password"
  required
  minlength="8"
  maxlength="32"
  placeholder="至少 8 位字符"
/>

<!-- 手机号(中国大陆 11 位) -->
<input
  type="tel"
  name="phone"
  pattern="1[3-9]\d{9}"
  placeholder="请输入手机号"
  autocomplete="tel"
/>

<!-- 数字范围(0-100,步长 5) -->
<input type="number" name="score" min="0" max="100" step="5" value="60" />

<!-- 日期范围限制 -->
<input type="date" name="birthday" min="1920-01-01" max="2010-12-31" />

<!-- 文件上传(限制类型和大小由 JS 处理) -->
<input type="file" name="avatar" accept="image/png, image/jpeg" />

<!-- 多文件上传 -->
<input type="file" name="photos" multiple accept="image/*" />

<!-- 范围滑块 -->
<input type="range" name="volume" min="0" max="100" step="1" value="50" />

<!-- 颜色选择器 -->
<input type="color" name="theme" value="#4361ee" />
```

---

## textarea 多行文本

**textarea 元素**
`<textarea name="<name>" [rows] [cols] [maxlength] [placeholder] [required]></textarea>`

```html
<!-- 基础多行文本 -->
<textarea
  name="address"
  rows="3"
  cols="40"
  placeholder="请输入详细地址"
  maxlength="200"
  required
></textarea>

<!-- 字符计数(配合 JavaScript) -->
<textarea name="comment" id="comment" rows="4" maxlength="500"></textarea>
<div class="char-count"><span id="commentCount">0</span>/500</div>
```

**textarea 属性表**

| 属性          | 作用                | 示例                |
| ------------- | ------------------- | ------------------- |
| `rows`        | 可见行数            | `rows="5"`          |
| `cols`        | 可见列数            | `cols="40"`         |
| `maxlength`   | 最大字符数          | `maxlength="500"`   |
| `minlength`   | 最小字符数          | `minlength="10"`    |
| `wrap`        | 换行模式            | `soft` / `hard`     |
| `placeholder` | 占位文本            | `placeholder="..."` |
| `required`    | 必填                | 布尔属性            |
| `readonly`    | 只读                | 布尔属性            |
| `disabled`    | 禁用                | 布尔属性            |

---

## select 与 option

**select 下拉选择**
`<select name="<name>" [multiple] [size] [required]></select>`

```html
<!-- 基础下拉框 -->
<select name="country" required>
  <option value="">请选择国家</option>
  <option value="CN">中国</option>
  <option value="US">美国</option>
  <option value="JP">日本</option>
</select>

<!-- 分组下拉框 -->
<select name="city">
  <optgroup label="一线城市">
    <option value="beijing">北京</option>
    <option value="shanghai">上海</option>
  </optgroup>
  <optgroup label="二线城市">
    <option value="hangzhou">杭州</option>
    <option value="chengdu">成都</option>
  </optgroup>
</select>

<!-- 多选下拉框 -->
<select name="languages" multiple size="5">
  <option value="js">JavaScript</option>
  <option value="py">Python</option>
  <option value="java">Java</option>
</select>
```

**select 属性表**

| 属性          | 作用                  | 示例              |
| ------------- | --------------------- | ----------------- |
| `name`        | 字段名                | `name="country"`  |
| `multiple`    | 允许多选              | 布尔属性          |
| `size`        | 可见选项数            | `size="5"`        |
| `required`    | 必填                  | 布尔属性          |
| `disabled`    | 禁用                  | 布尔属性          |
| `autofocus`   | 自动聚焦              | 布尔属性          |

**option 属性表**

| 属性        | 作用                | 示例             |
| ----------- | ------------------- | ---------------- |
| `value`     | 提交值              | `value="CN"`     |
| `selected`  | 默认选中            | 布尔属性         |
| `disabled`  | 禁用选项            | 布尔属性         |
| `label`     | 选项显示文本        | `label="中国"`   |

---

## button 按钮

**button 元素**
`<button type="submit | reset | button" [name] [value] [disabled]></button>`

```html
<!-- 提交按钮(默认 type) -->
<button type="submit">提交</button>

<!-- 重置按钮 -->
<button type="reset">重置</button>

<!-- 普通按钮(配合 JavaScript) -->
<button type="button" onclick="handleClick()">点击</button>

<!-- 带图标的按钮 -->
<button type="submit">
  <i class="fa fa-search" aria-hidden="true"></i>
  <span>搜索</span>
</button>

<!-- 禁用按钮 -->
<button type="submit" disabled>提交中...</button>

<!-- 表单外提交按钮(通过 form 属性关联) -->
<button type="submit" form="myForm" value="save">保存</button>
```

**button 属性表**

| 属性        | 作用                           | 示例             |
| ----------- | ------------------------------ | ---------------- |
| `type`      | 按钮类型                       | `submit`/`reset`/`button` |
| `name`      | 按钮名(提交时作为键)         | `name="action"`  |
| `value`     | 按钮值                         | `value="save"`   |
| `disabled`  | 禁用按钮                       | 布尔属性         |
| `autofocus` | 自动聚焦                       | 布尔属性         |
| `form`      | 关联表单 ID                    | `form="loginForm"`|

---

## label 标签关联

**label 元素**
`<label for="<input-id>">文本</label>` 或 `<label><input> 文本</label>`

```html
<!-- 方式1:label 包裹输入框 -->
<label>
  用户名:
  <input type="text" name="username" required />
</label>

<!-- 方式2:label 的 for 属性关联 -->
<label for="email">邮箱:</label>
<input type="email" id="email" name="email" required />

<!-- 必填字段提示 -->
<label for="phone">
  电话:<span aria-label="必填">*</span>
</label>
<input type="tel" id="phone" name="phone" required />

<!-- 单选框/复选框包裹 -->
<label class="radio-label">
  <input type="radio" name="gender" value="male" /> 男
</label>
<label class="radio-label">
  <input type="radio" name="gender" value="female" /> 女
</label>
```

---

## fieldset 与 legend

**字段分组**
`<fieldset [disabled]><legend>分组标题</legend>...</fieldset>`

```html
<!-- 表单字段分组 -->
<form>
  <fieldset>
    <legend>个人信息</legend>
    <label>姓名:<input type="text" name="name" /></label>
    <label>年龄:<input type="number" name="age" /></label>
  </fieldset>

  <fieldset>
    <legend>联系方式</legend>
    <label>邮箱:<input type="email" name="email" /></label>
    <label>电话:<input type="tel" name="phone" /></label>
  </fieldset>

  <!-- 禁用整个分组 -->
  <fieldset disabled>
    <legend>已禁用分组</legend>
    <input type="text" name="readonly-field" />
  </fieldset>
</form>
```

---

## datalist 预定义选项

**输入框联想**
`<input list="<datalist-id>">` + `<datalist id="..."><option></datalist>`

```html
<!-- 输入框带联想选项 -->
<label for="browser">浏览器:</label>
<input list="browsers" id="browser" name="browser" />
<datalist id="browsers">
  <option value="Chrome"></option>
  <option value="Firefox"></option>
  <option value="Safari"></option>
  <option value="Edge"></option>
</datalist>

<!-- 邮箱联想 -->
<input type="email" list="common-emails" name="email" />
<datalist id="common-emails">
  <option value="@gmail.com"></option>
  <option value="@outlook.com"></option>
  <option value="@qq.com"></option>
</datalist>
```

---

## output 与 progress

**output 输出元素**
`<output name="<name>" for="<input-ids>">值</output>`

```html
<!-- 实时显示计算结果 -->
<form oninput="result.value=parseInt(a.value)+parseInt(b.value)">
  <input type="number" name="a" value="10" /> +
  <input type="number" name="b" value="20" /> =
  <output name="result">30</output>
</form>
```

**progress 进度条**
`<progress value="<current>" max="<total>"></progress>`

```html
<!-- 任务进度 -->
<label>上传进度:</label>
<progress id="uploadProgress" value="70" max="100">70%</progress>

<!-- 不确定进度(加载中) -->
<progress>加载中...</progress>
```

**meter 度量条**
`<meter value="<value>" [min] [max] [low] [high] [optimum]></meter>`

```html
<!-- 磁盘使用率 -->
<label>磁盘占用:</label>
<meter value="0.6" min="0" max="1" low="0.3" high="0.7" optimum="0.2">60%</meter>

<!-- 分数评估 -->
<meter value="85" min="0" max="100" low="40" high="80" optimum="100">85 分</meter>
```

---

## 表单验证 API

**HTML5 内置验证属性**

```html
<!-- 必填 -->
<input type="text" required />

<!-- 类型验证(邮箱/URL/数字等) -->
<input type="email" required />
<input type="url" required />
<input type="number" min="0" max="100" />

<!-- 长度验证 -->
<input type="text" minlength="2" maxlength="50" />

<!-- 正则验证 -->
<input type="text" pattern="[A-Za-z]{3,}" title="至少3个字母" />

<!-- 自定义验证消息 -->
<input type="text" required oninput="setCustomValidity('')" 
       oninvalid="setCustomValidity('请输入有效值')" />
```

**ValidityState 对象属性表**

```javascript
// 检查单个输入框的验证状态
const input = document.getElementById('email');
input.checkValidity();              // 返回 true/false
input.reportValidity();             // 验证并显示错误消息
input.setCustomValidity('msg');     // 设置自定义错误消息
input.validationMessage;            // 浏览器默认错误消息

// ValidityState 属性
input.validity.valid;               // 是否通过所有验证
input.validity.valueMissing;        // required 但为空
input.validity.typeMismatch;        // 类型不匹配(email/url)
input.validity.patternMismatch;     // pattern 不匹配
input.validity.tooShort;            // 长度小于 minlength
input.validity.tooLong;             // 长度大于 maxlength
input.validity.rangeUnderflow;      // 值小于 min
input.validity.rangeOverflow;       // 值大于 max
input.validity.stepMismatch;        // 不符合 step 要求
input.validity.badInput;            // 浏览器无法转换输入
input.validity.customError;         // 已设置自定义错误
```

**表单验证流程**

```javascript
// 验证整个表单
const form = document.getElementById('myForm');
const isValid = form.checkValidity();   // 返回是否全部通过
form.reportValidity();                  // 显示所有错误

// 验证单个字段并显示错误
function validateField(input) {
  const errorEl = document.getElementById(`${input.id}Error`);
  if (!input.checkValidity()) {
    input.classList.add('invalid');
    if (errorEl) {
      if (input.validity.valueMissing) {
        errorEl.textContent = '该字段必填';
      } else if (input.validity.typeMismatch) {
        errorEl.textContent = `请输入有效的${input.type}格式`;
      } else if (input.validity.tooShort) {
        errorEl.textContent = `至少 ${input.minLength} 个字符`;
      } else if (input.validity.patternMismatch) {
        errorEl.textContent = '格式不正确';
      } else {
        errorEl.textContent = input.validationMessage;
      }
    }
    return false;
  }
  input.classList.remove('invalid');
  if (errorEl) errorEl.textContent = '';
  return true;
}

// 表单提交前验证
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
  let valid = true;
  inputs.forEach((input) => {
    if (!validateField(input)) valid = false;
  });
  if (valid) {
    // 提交表单
    form.submit();
  }
});
```

---

## 表单事件

**表单相关事件表**

| 事件         | 触发时机                    | 应用元素               |
| ------------ | --------------------------- | ---------------------- |
| `submit`     | 表单提交时                  | `<form>`               |
| `reset`      | 表单重置时                  | `<form>`               |
| `input`      | 输入值改变(实时)          | input、textarea、select |
| `change`     | 值改变并失焦时              | input、select、textarea |
| `focus`      | 获得焦点                    | 所有表单元素           |
| `blur`       | 失去焦点                    | 所有表单元素           |
| `invalid`    | 验证失败                    | 表单控件               |
| `valid`      | 验证通过(自定义)          | 表单控件               |

```javascript
// 实时验证(input 事件)
form.addEventListener('input', (e) => {
  const input = e.target;
  if (input.tagName === 'INPUT' || input.tagName === 'TEXTAREA') {
    validateField(input);
  }
});

// 表单提交
form.addEventListener('submit', (e) => {
  e.preventDefault();
  if (form.checkValidity()) {
    const formData = new FormData(form);
    // 提交数据
  }
});

// 阻止无效提交
form.addEventListener('invalid', (e) => {
  e.preventDefault();
  validateField(e.target);
}, true);
```

---

## FormData 数据提交

**FormData 对象**
`const formData = new FormData([form])`

```javascript
// 从表单创建 FormData
const form = document.getElementById('myForm');
const formData = new FormData(form);

// 遍历所有字段
for (const [key, value] of formData.entries()) {
  console.log(`${key}: ${value}`);
}

// 获取单个字段
const name = formData.get('name');
const files = formData.getAll('photos');  // 多值字段

// 添加/修改字段
formData.append('key', 'value');
formData.set('key', 'new-value');
formData.delete('key');

// 转为普通对象
const data = Object.fromEntries(formData.entries());

// 通过 fetch 提交
fetch('/api/submit', {
  method: 'POST',
  body: formData  // 自动设置 multipart/form-data
})
  .then((response) => response.json())
  .then((data) => console.log(data));
```

**FormData 方法表**

| 方法                    | 说明                       |
| ----------------------- | -------------------------- |
| `append(name, value)`   | 添加字段                   |
| `set(name, value)`      | 设置(覆盖)字段           |
| `get(name)`             | 获取第一个值               |
| `getAll(name)`          | 获取所有值(多选)        |
| `has(name)`             | 是否存在字段               |
| `delete(name)`          | 删除字段                   |
| `entries()`             | 遍历所有键值对             |
| `keys()`                | 遍历所有键名               |
| `values()`              | 遍历所有值                 |

---

## autocomplete 自动填充

**autocomplete 值表**

| 值             | 作用                  | 应用字段            |
| -------------- | --------------------- | ------------------- |
| `on`           | 启用自动填充          | 通用                |
| `off`          | 禁用自动填充          | 敏感字段            |
| `name`         | 全名                  | `<input type="text">` |
| `given-name`   | 名字                  | 文本输入            |
| `family-name`  | 姓氏                  | 文本输入            |
| `email`        | 邮箱                  | `<input type="email">` |
| `tel`          | 电话                  | `<input type="tel">` |
| `address-line1`| 地址行 1              | 文本输入            |
| `address-line2`| 地址行 2              | 文本输入            |
| `country`      | 国家                  | 文本/select         |
| `postal-code`  | 邮政编码              | 文本输入            |
| `username`     | 用户名                | 文本输入            |
| `current-password` | 当前密码          | `<input type="password">` |
| `new-password` | 新密码                | `<input type="password">` |
| `cc-number`    | 信用卡号              | 文本输入            |
| `cc-exp`       | 信用卡有效期          | 文本输入            |
| `cc-csc`       | 信用卡安全码          | 文本输入            |
| `bday`          | 生日                  | `<input type="date">` |

```html
<!-- 启用自动填充(浏览器记住用户信息) -->
<form autocomplete="on">
  <input type="text" name="name" autocomplete="name" />
  <input type="email" name="email" autocomplete="email" />
  <input type="tel" name="phone" autocomplete="tel" />
  <input type="password" name="password" autocomplete="current-password" />
</form>

<!-- 禁用自动填充(敏感字段) -->
<input type="text" name="captcha" autocomplete="off" />
<input type="password" name="new-password" autocomplete="new-password" />
```

---

## 文件上传

**file 输入与 FileReader**

```html
<!-- 单文件上传 -->
<input type="file" id="avatar" name="avatar" accept="image/png, image/jpeg" />

<!-- 多文件上传 -->
<input type="file" id="photos" name="photos" multiple accept="image/*" />

<!-- 调用摄像头 -->
<input type="file" accept="image/*" capture="user" />
<!-- 调用麦克风 -->
<input type="file" accept="audio/*" capture />
```

```javascript
// 监听文件选择
const fileInput = document.getElementById('avatar');
fileInput.addEventListener('change', () => {
  const file = fileInput.files[0];
  if (!file) return;

  // 文件信息
  console.log('文件名:', file.name);
  console.log('文件大小:', file.size, 'bytes');
  console.log('文件类型:', file.type);
  console.log('最后修改:', file.lastModified);

  // 文件大小校验(限制 5MB)
  if (file.size > 5 * 1024 * 1024) {
    alert('文件大小不能超过 5MB');
    return;
  }

  // 读取为 Data URL(图片预览)
  const reader = new FileReader();
  reader.onload = (e) => {
    const img = document.getElementById('preview');
    img.src = e.target.result;
  };
  reader.readAsDataURL(file);
});

// 拖拽上传
const dropZone = document.getElementById('dropZone');
dropZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropZone.classList.add('dragover');
});
dropZone.addEventListener('dragleave', () => {
  dropZone.classList.remove('dragover');
});
dropZone.addEventListener('drop', (e) => {
  e.preventDefault();
  dropZone.classList.remove('dragover');
  const file = e.dataTransfer.files[0];
  if (file && file.type.startsWith('image/')) {
    handleImageFile(file);
  }
});
```

**FileReader 方法表**

| 方法                       | 说明                       |
| -------------------------- | -------------------------- |
| `readAsDataURL(file)`      | 读取为 Base64 Data URL     |
| `readAsText(file, [enc])`  | 读取为文本                 |
| `readAsArrayBuffer(file)`  | 读取为 ArrayBuffer         |
| `readAsBinaryString(file)` | 读取为二进制字符串         |
| `abort()`                  | 中断读取                   |

**FileReader 事件表**

| 事件          | 触发时机                |
| ------------- | ----------------------- |
| `onloadstart` | 开始读取                |
| `onprogress`  | 读取进度更新            |
| `onload`      | 读取完成                |
| `onerror`     | 读取错误                |
| `onabort`     | 读取中断                |
| `onloadend`   | 读取结束(无论成功失败)|

---

## 表单序列化

**序列化方法对比**

```javascript
// 方式1:FormData(推荐,支持文件)
const formData = new FormData(form);
fetch('/api/submit', { method: 'POST', body: formData });

// 方式2:URLSearchParams(适合 GET 请求或 x-www-form-urlencoded)
const params = new URLSearchParams();
params.append('name', 'Alice');
params.append('email', 'alice@example.com');
fetch('/api/submit', {
  method: 'POST',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  body: params
});

// 方式3:JSON 提交
const data = Object.fromEntries(new FormData(form).entries());
fetch('/api/submit', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(data)
});

// 方式4:直接获取表单值
const form = document.getElementById('myForm');
const data = {
  name: form.elements.name.value,
  email: form.elements.email.value,
  gender: form.elements.gender.value
};
```

---

## 注意事项

- **novalidate**:默认浏览器会在表单提交时自动验证,设置 `novalidate` 可禁用此行为
- **autocomplete**:推荐启用以提升用户体验,敏感字段(验证码、新密码)使用 `off` 或 `new-password`
- **type 优先**:使用正确的 `type`(email/url/number)可触发浏览器内置验证和移动端键盘适配
- **pattern 配合 title**:`pattern` 属性必须配合 `title` 提示用户正确的格式
- **maxlength**:`textarea` 早期不支持 `maxlength`,现代浏览器已支持
- **required**:`checkbox` 类型的 `required` 表示必须勾选,`radio` 同 name 组至少选一个
- **FormData**:直接作为 `fetch` 的 `body` 时不要手动设置 `Content-Type`,浏览器会自动添加 boundary
- **FileReader 异步**:`readAsDataURL` 等方法为异步,需在 `onload` 回调中处理结果
- **accept 仅提示**:`accept` 属性只是浏览器提示,用户仍可选择其他类型,服务端必须再次校验
- **大文件上传**:大文件建议分片上传,避免使用 FileReader 一次性读取



<!-- ============ 文档分隔线：006-html5/022-AudioVideo.md ============ -->

# 音频与视频 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

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



<!-- ============ 文档分隔线：006-html5/023-SemanticTag.md ============ -->

# 语义化标签 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 页面结构标签

**header 头部**
`<header>...[h1-h6|nav|form]...</header>`
```html
<!-- 页面级 header -->
<header>
  <h1>网站标题</h1>
  <nav>
    <ul>
      <li><a href="/">首页</a></li>
      <li><a href="/about">关于</a></li>
    </ul>
  </nav>
</header>

<!-- article 内的 header -->
<article>
  <header>
    <h2>文章标题</h2>
    <time datetime="2026-06-13">2026年6月13日</time>
  </header>
  <p>文章内容...</p>
</article>
```

**nav 导航**
`<nav [aria-label="<名称>"]>...[a|ul]...</nav>`
```html
<!-- 主导航 -->
<nav aria-label="主导航">
  <ul>
    <li><a href="/" aria-current="page">首页</a></li>
    <li><a href="/blog">博客</a></li>
  </ul>
</nav>

<!-- 面包屑 -->
<nav aria-label="面包屑">
  <ol>
    <li><a href="/">首页</a></li>
    <li><a href="/blog">博客</a></li>
    <li aria-current="page">当前文章</li>
  </ol>
</nav>

<!-- 分页 -->
<nav aria-label="分页">
  <ul>
    <li><a href="?page=1">1</a></li>
    <li><a href="?page=2" aria-current="page">2</a></li>
  </ul>
</nav>
```

**main 主内容**
`<main [id="<锚点ID>"]>...</main>`
```html
<!-- 每页只能有一个 main -->
<body>
  <a href="#main-content" class="skip-link">跳到主要内容</a>
  <header>...</header>
  <main id="main-content">
    <h1>页面主标题</h1>
    <p>主要内容区域...</p>
  </main>
  <footer>...</footer>
</body>
```

**footer 底部**
`<footer>...[address|nav|p]...</footer>`
```html
<footer>
  <section>
    <h3>联系方式</h3>
    <address>
      <a href="mailto:info@example.com">info@example.com</a><br />
      <a href="tel:+8612345678">+86 123-4567-8</a>
    </address>
  </section>
  <p><small>&copy; 2026 我的公司. 保留所有权利.</small></p>
</footer>
```

---

## 内容分区标签

**article 独立内容**
`<article>...[header|section|footer]...</article>`
```html
<!-- 博客文章 -->
<article>
  <header>
    <h2>深入理解HTML5语义化</h2>
    <p>由 <a href="/author/zhangsan">张三</a> 发布于
      <time datetime="2026-06-13">2026年6月13日</time>
    </p>
  </header>
  <p>文章正文内容...</p>
  <footer>
    <p>标签:<a href="/tag/html5">HTML5</a></p>
  </footer>
</article>

<!-- 嵌套评论 -->
<article>
  <header>
    <p>李四 评论于 <time datetime="2026-06-13T10:30">10:30</time></p>
  </header>
  <p>非常好的文章!</p>
</article>
```

**section 主题分组**
`<section>...[h2-h6]...</section>`
```html
<article>
  <h1>Web开发指南</h1>
  <section>
    <h2>HTML基础</h2>
    <p>HTML是Web的骨架...</p>
  </section>
  <section>
    <h2>CSS样式</h2>
    <p>CSS负责页面的视觉表现...</p>
  </section>
</article>
```

**aside 侧边栏**
`<aside [aria-label="<名称>"]>...</aside>`
```html
<main>
  <article>
    <h1>如何学习编程</h1>
    <p>学习编程的第一步是...</p>
  </article>

  <aside aria-label="相关文章">
    <h2>推荐阅读</h2>
    <ul>
      <li><a href="/post/2">编程语言选择指南</a></li>
    </ul>
  </aside>
</main>
```

---

## 文本级语义标签

**time 时间**
`<time datetime="<ISO日期>">[显示文本]</time>`
```html
<!-- 日期 -->
<time datetime="2026-06-13">2026年6月13日</time>

<!-- 日期和时间 -->
<time datetime="2026-06-13T14:30:00+08:00">下午2:30</time>

<!-- 时间段 -->
<time datetime="PT2H30M">2小时30分钟</time>

<!-- 可读性更好的日期 -->
<time datetime="2026-06-13">上周五</time>
```

**figure 与 figcaption**
`<figure>...[img|pre|blockquote]...[<figcaption>[说明]</figcaption>]</figure>`
```html
<!-- 图片说明 -->
<figure>
  <img src="chart.png" alt="2026年销售数据图表" />
  <figcaption>图1:2026年上半年销售数据趋势</figcaption>
</figure>

<!-- 代码示例 -->
<figure>
  <figcaption>示例:Hello World程序</figcaption>
  <pre><code>console.log("Hello, World!");</code></pre>
</figure>

<!-- 引用 -->
<figure>
  <blockquote>
    <p>任何足够先进的技术,都与魔法无异。</p>
  </blockquote>
  <figcaption>—— 亚瑟·克拉克,<cite>未来的轮廓</cite></figcaption>
</figure>
```

**mark 高亮**
`<mark>[文本]</mark>`
```html
<!-- 搜索结果高亮 -->
<p>搜索结果中 <mark>HTML5</mark> 语义化标签的使用...</p>
```

**abbr 缩写**
`<abbr title="<全称>">[缩写]</abbr>`
```html
<abbr title="HyperText Markup Language">HTML</abbr> 是Web的基础。
```

**cite 引用标题**
`<cite>[作品名]</cite>`
```html
参考书目:<cite>JavaScript高级程序设计</cite>
```

**dfn 定义术语**
`<dfn>[术语]</dfn>`
```html
<dfn>语义化</dfn>是指使用具有明确含义的标签来描述内容。
```

**address 联系方式**
`<address>...</address>`
```html
<address>
  作者:<a href="mailto:author@example.com">张三</a><br />
  地址:北京市朝阳区xxx
</address>
```

---

## 可折叠内容

**details 与 summary**
`<details [open]><summary>[标题]</summary>[内容]</details>`
```html
<!-- 默认折叠 -->
<details>
  <summary>常见问题:如何重置密码?</summary>
  <p>请访问登录页面,点击"忘记密码"链接。</p>
</details>

<!-- 默认展开 -->
<details open>
  <summary>使用说明</summary>
  <p>这是默认展开的说明内容。</p>
</details>
```

---

## 搜索区域(HTML 2023)

**search 元素**
`<search>...[form|input]...</search>`
```html
<!-- 站点搜索 -->
<search>
  <form action="/search" role="search">
    <label for="q">搜索</label>
    <input type="search" id="q" name="q" placeholder="搜索内容..." />
    <button type="submit">搜索</button>
  </form>
</search>
```

---

## 对话框(HTML 2021)

**dialog 元素**
`<dialog [open]>[内容]</dialog>`
```html
<dialog id="myDialog">
  <form method="dialog">
    <p>请确认操作</p>
    <button>取消</button>
    <button value="confirm">确认</button>
  </form>
</dialog>

<script>
  const dialog = document.getElementById('myDialog');
  dialog.showModal();
  dialog.close('cancel');
</script>
```

---

## 微数据增强语义

**itemscope 与 itemtype**
`<article itemscope itemtype="<Schema类型>">...[itemprop]...</article>`
```html
<article itemscope itemtype="https://schema.org/NewsArticle">
  <h2 itemprop="headline">重大新闻标题</h2>
  <meta itemprop="datePublished" content="2026-06-13" />
  <p itemprop="articleBody">新闻内容...</p>
</article>
```

---

## ARIA 增强可访问性

**常用 ARIA 属性**

| 属性              | 作用                |
| ----------------- | ------------------- |
| `aria-label`      | 元素的文本标签      |
| `aria-labelledby` | 引用其他元素作为标签 |
| `aria-current`    | 当前项(page/step等) |
| `aria-expanded`   | 展开/折叠状态       |
| `aria-hidden`     | 对辅助技术隐藏      |
| `role`            | 元素的角色          |

```html
<nav aria-label="主导航">
  <a href="/" aria-current="page">首页</a>
</nav>

<button aria-expanded="false" aria-controls="menu">菜单</button>
<ul id="menu" aria-hidden="true">...</ul>
```



<!-- ============ 文档分隔线：006-html5/024-MetadataCharacterEncoding.md ============ -->

# 元数据与字符编码 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## head 容器

**文档头部容器**
`<head>...[meta|title|link|style|script]...</head>`
```html
<!-- 文档头部基础结构 -->
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="页面描述" />
  <title>页面标题</title>
  <link rel="stylesheet" href="styles.css" />
</head>
```

| 类别     | 元素                | 作用                     |
| -------- | ------------------- | ------------------------ |
| 字符编码 | `<meta charset>`    | 声明文档编码             |
| 视口配置 | `<meta viewport>`   | 移动端适配               |
| SEO 相关 | `<meta name>`       | 描述、关键词、机器人指令 |
| 社交分享 | `<meta property>`   | Open Graph、Twitter Card |
| 安全策略 | `<meta http-equiv>` | CSP、CORS                |
| 资源关系 | `<link>`            | 样式表、图标、预加载     |

---

## meta 元素

**字符编码声明**
`<meta charset="<编码>" />`
```html
<!-- 必须在文档前 1024 字节内,title 之前 -->
<meta charset="UTF-8" />
```

**SEO 元数据**
`<meta name="<名称>" content="<内容>" />`
```html
<!-- 页面描述 -->
<meta name="description" content="深入讲解 HTML5 元数据与字符编码" />

<!-- 搜索引擎指令 -->
<meta name="robots" content="index, follow" />

<!-- 作者 -->
<meta name="author" content="fanquanpp" />

<!-- 关键词 -->
<meta name="keywords" content="HTML5,meta,字符编码" />
```

**Open Graph 社交分享**
`<meta property="og:<属性>" content="<值>" />`
```html
<!-- Facebook / 微博等社交平台分享 -->
<meta property="og:title" content="页面标题" />
<meta property="og:description" content="页面描述" />
<meta property="og:image" content="https://example.com/image.jpg" />
<meta property="og:url" content="https://example.com/page" />

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="页面标题" />
```

**安全相关元数据**
`<meta http-equiv="<HTTP头>" content="<值>" />`
```html
<!-- 内容安全策略 -->
<meta http-equiv="Content-Security-Policy" content="default-src 'self'" />

<!-- Referrer 策略 -->
<meta name="referrer" content="strict-origin-when-cross-origin" />

<!-- X-UA-Compatible -->
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
```

---

## viewport 视口配置

**移动端视口**
`<meta name="viewport" content="<键>=<值>, <键>=<值>" />`
```html
<!-- 标准移动端配置 -->
<meta name="viewport" content="width=device-width, initial-scale=1.0" />

<!-- 禁止用户缩放(不推荐,影响可访问性) -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />

<!-- 适配刘海屏 -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
```

| 属性            | 值                 | 说明             |
| --------------- | ------------------ | ---------------- |
| `width`         | device-width / 数值 | 布局视口宽度     |
| `height`        | device-height / 数值 | 布局视口高度     |
| `initial-scale` | 0.1 ~ 10.0         | 初始缩放比例     |
| `minimum-scale` | 0.1 ~ 10.0         | 最小缩放比例     |
| `maximum-scale` | 0.1 ~ 10.0         | 最大缩放比例     |
| `user-scalable` | yes / no           | 是否允许用户缩放 |
| `viewport-fit`  | auto / contain / cover | 适配刘海屏     |

---

## title 元素

**文档标题**
`<title>[标题文本]</title>`
```html
<!-- 浏览器标签页标题,SEO 重要字段 -->
<title>页面标题 - 网站名称</title>
```

---

## link 元素

**资源关系**
`<link rel="<关系>" [type="<MIME>"] [href="<URL>"] [media="<媒体查询>"] />`
```html
<!-- 样式表 -->
<link rel="stylesheet" href="styles.css" />

<!-- 网站图标 -->
<link rel="icon" type="image/png" href="/favicon.png" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png" />

<!-- 预连接(加速第三方资源) -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="dns-prefetch" href="https://fonts.googleapis.com" />

<!-- 预加载关键资源 -->
<link rel="preload" href="font.woff2" as="font" crossorigin />
<link rel="preload" href="hero.jpg" as="image" />

<!-- 规范化 URL -->
<link rel="canonical" href="https://example.com/page" />

<!-- 替代语言版本 -->
<link rel="alternate" hreflang="en" href="https://example.com/en/page" />
<link rel="alternate" hreflang="zh-CN" href="https://example.com/zh/page" />

<!-- manifest(PWA) -->
<link rel="manifest" href="/manifest.json" />
```

| rel 值          | 作用              |
| --------------- | ----------------- |
| `stylesheet`    | 样式表            |
| `icon`          | 网站图标          |
| `preconnect`    | 预连接域名        |
| `dns-prefetch`  | DNS 预解析        |
| `preload`       | 预加载资源        |
| `prefetch`      | 预获取下一页资源  |
| `canonical`     | 规范化 URL        |
| `alternate`     | 替代版本          |
| `manifest`      | PWA manifest      |

---

## style 与 script

**内联样式**
`<style [type="text/css"] [media="<媒体查询>"]>[CSS]</style>`
```html
<style>
  body { font-family: Arial, sans-serif; }
</style>
```

**脚本引入**
`<script src="<URL>" [type="<类型>"] [defer] [async] [crossorigin]></script>`
```html
<!-- 外部脚本,defer 等文档解析完后执行 -->
<script src="app.js" defer></script>

<!-- 异步加载 -->
<script src="analytics.js" async></script>

<!-- 模块脚本 -->
<script type="module" src="app.mjs"></script>

<!-- 内联脚本 -->
<script>
  console.log('页面加载完成');
</script>
```

| 属性     | 作用                              |
| -------- | --------------------------------- |
| `defer`  | 延迟执行(按顺序,DOMContentLoaded 前) |
| `async`  | 异步执行(下载完即执行,不保证顺序)  |
| `type="module"` | ES 模块                  |
| `crossorigin`   | 跨域脚本                |

---

## base 元素

**基准 URL**
`<base href="<URL>" [target="<目标>"] />`
```html
<!-- 文档内所有相对 URL 的基准 -->
<base href="https://www.example.com/" target="_blank" />
```

---

## UTF-8 字符编码

**UTF-8 编码原理**

| 码点范围           | 字节数 | 编码格式                              |
| ------------------ | ------ | ------------------------------------- |
| U+0000 ~ U+007F    | 1      | `0xxxxxxx`                            |
| U+0080 ~ U+07FF    | 2      | `110xxxxx 10xxxxxx`                   |
| U+0800 ~ U+FFFF    | 3      | `1110xxxx 10xxxxxx 10xxxxxx`          |
| U+10000 ~ U+10FFFF | 4      | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

**编码声明优先级**
`BOM > HTTP Content-Type 头 > meta charset 声明`

**JavaScript 检测编码**
```javascript
// 获取文档字符编码
console.log(document.characterSet); // 'UTF-8'
console.log(document.inputEncoding);
```



<!-- ============ 文档分隔线：006-html5/025-CustomDataAttribute.md ============ -->

# 自定义数据属性 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数 | `{ }` 分组 | `|` 或 | `...` 重复

---

## data-* 属性定义

**HTML 自定义数据属性**
`<element data-<name>="<value>">`

```html
<!-- 在 HTML 元素上存储自定义数据 -->
<div
  id="user"
  data-user-id="123"
  data-role="admin"
  data-login-count="42"
  data-last-active="2026-07-20"
>
  用户信息
</div>
```

**命名规则**

| 规则                       | 说明                                              |
| -------------------------- | ------------------------------------------------- |
| 必须以 `data-` 开头         | 前缀标识自定义属性                                |
| 仅允许小写字母、数字、连字符 | 不支持大写字母、下划线、特殊字符                  |
| 不能以连字符开头            | `data--name` 不合法                               |
| 不能以数字开头(连字符后)  | `data-1name` 不合法                               |
| XML 兼容                   | 名称必须符合 XML 规范                             |

---

## JavaScript 访问

**dataset 属性(驼峰命名)**
`element.dataset.<camelCaseName>`

```javascript
const el = document.getElementById('user');

// 读取 data-* 属性(连字符转驼峰)
console.log(el.dataset.userId);      // '123'(对应 data-user-id)
console.log(el.dataset.role);        // 'admin'
console.log(el.dataset.loginCount);  // '42'(对应 data-login-count)

// 设置 data-* 属性
el.dataset.active = 'true';          // 添加 data-active="true"
el.dataset.lastLogin = '2026-07-20'; // 添加 data-last-login

// 删除 data-* 属性
delete el.dataset.role;              // 移除 data-role
```

**getAttribute / setAttribute 方法**
`element.getAttribute('data-<name>')`

```javascript
const el = document.getElementById('user');

// 读取属性(原始连字符格式)
const userId = el.getAttribute('data-user-id'); // '123'

// 设置属性
el.setAttribute('data-user-id', '456');

// 判断属性是否存在
const hasRole = el.hasAttribute('data-role'); // true / false

// 删除属性
el.removeAttribute('data-role');
```

**dataset vs getAttribute 对比**

| 特性                | `dataset`                | `getAttribute / setAttribute` |
| ------------------- | ------------------------ | ----------------------------- |
| 属性名格式          | 驼峰(`userId`)          | 连字符(`data-user-id`)       |
| 性能                | 略慢                     | 略快                          |
| 类型                | DOMStringMap 对象        | 字符串                        |
| IE 支持             | IE11+                    | 所有版本                      |
| 推荐场景            | 现代 Web 应用            | 兼容旧浏览器                  |

---

## CSS 访问

**属性选择器**
`[data-<name>] | [data-<name>="<value>"]`

```css
/* 通过 data-* 属性选择元素 */
[data-role='admin'] {
  background-color: gold;
  font-weight: bold;
}

[data-role='user'] {
  background-color: #f0f0f0;
}

/* 仅判断属性存在性 */
[data-featured] {
  border: 2px solid blue;
}
```

**content 与 attr()**
`content: attr(data-<name>)`

```css
/* 使用 attr() 在 CSS 中读取 data-* 值 */
.tooltip::after {
  content: attr(data-tooltip);
  display: none;
  padding: 8px;
  background: #333;
  color: #fff;
  border-radius: 4px;
  position: absolute;
  top: 100%;
  left: 0;
}

.tooltip:hover::after {
  display: block;
}
```

```html
<!-- 配合 CSS 实现纯 CSS 提示框 -->
<button class="tooltip" data-tooltip="点击此处提交表单">提交</button>
```

**data-* 配合 CSS 状态切换**

```css
/* 通过 data-* 控制 Tab 切换 */
.tab-panel {
  display: none;
}

[data-active='true'].tab-panel {
  display: block;
}
```

```html
<div class="tab-panel" data-active="true">面板1</div>
<div class="tab-panel" data-active="false">面板2</div>
```

---

## 事件委托应用

**事件委托模式**
`container.addEventListener('click', handler)`

```html
<!-- 列表项通过 data-* 存储用户数据 -->
<ul id="user-list">
  <li data-user-id="1" data-name="张三" data-role="admin">张三</li>
  <li data-user-id="2" data-name="李四" data-role="user">李四</li>
  <li data-user-id="3" data-name="王五" data-role="user">王五</li>
</ul>
```

```javascript
// 事件委托:在父元素上监听,通过 data-* 获取数据
document.getElementById('user-list').addEventListener('click', (e) => {
  const li = e.target.closest('li');
  if (!li) return;

  console.log(`用户 ID: ${li.dataset.userId}`);
  console.log(`用户名: ${li.dataset.name}`);
  console.log(`角色: ${li.dataset.role}`);

  // 根据 data-* 执行不同操作
  if (li.dataset.role === 'admin') {
    showAdminPanel(li.dataset.userId);
  } else {
    showUserProfile(li.dataset.userId);
  }
});
```

---

## 类型转换

**手动类型转换**

```javascript
const el = document.getElementById('user');

// 字符串转数字
const userId = parseInt(el.dataset.userId, 10);      // 123
const loginCount = Number(el.dataset.loginCount);    // 42

// 字符串转布尔
const isActive = el.dataset.active === 'true';       // true

// 字符串转对象(需 JSON.parse)
const data = JSON.parse(el.dataset.config);          // 对象

// 存储对象需先序列化
el.dataset.user = JSON.stringify({ name: '张三', age: 25 });
const user = JSON.parse(el.dataset.user);
```

---

## 注意事项

- **字符串类型**:data-* 值始终是字符串,使用时需手动类型转换
- **大小限制**:不适合存储大量数据,大数据请用 `WeakMap` 或 `IndexedDB`
- **XSS 风险**:避免用 `innerHTML` 输出 data-* 值,防止 XSS 攻击
- **可读性**:data-* 会在 HTML 中可见,不要存储敏感信息(如 Token、密码)
- **语义化**:data-* 是自定义数据属性,不应替代 class、id 等语义化属性
- **性能优化**:大量元素访问 data-* 时,优先使用 `getAttribute`(略快于 `dataset`)
- **命名一致性**:全项目统一使用连字符命名(如 `data-user-id`),不要混用驼峰



<!-- ============ 文档分隔线：006-html5/026-ProgressMeter.md ============ -->

# progress 与 meter 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

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



<!-- ============ 文档分隔线：006-html5/027-ServiceWorkerPWA.md ============ -->

# Service Worker 与 PWA 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Service Worker 注册

**注册 Service Worker**
`navigator.serviceWorker.register(<scriptURL>, [options]).then(<回调>)`
```javascript
// 基础注册
if ('serviceWorker' in navigator) {
  navigator.serviceWorker
    .register('/sw.js', { scope: '/' })
    .then((reg) => console.log('注册成功,作用域:', reg.scope))
    .catch((err) => console.error('注册失败:', err));
}
```

| options 字段 | 说明                       | 示例                |
| ------------ | -------------------------- | ------------------- |
| `scope`      | 控制范围(子目录路径)       | `scope: '/'`        |
| `type`       | worker 类型 classic/module | `type: 'module'`    |
| `updateViaCache` | 缓存策略               | `updateViaCache: 'none'` |

**生命周期方法**
```javascript
// 获取注册对象
const reg = await navigator.serviceWorker.ready;

// 手动更新
await reg.update();

// 取消注册
await reg.unregister();

// 监听更新事件
reg.addEventListener('updatefound', () => {
  console.log('发现新版本');
});
```

---

## Service Worker 生命周期事件

**install 事件(安装阶段)**
`self.addEventListener('install', (event) => { event.waitUntil(<Promise>) })`
```javascript
const CACHE_NAME = 'app-v1';
const CACHE_URLS = ['/', '/index.html', '/styles.css', '/app.js'];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches
      .open(CACHE_NAME)
      .then((cache) => cache.addAll(CACHE_URLS))
      .then(() => self.skipWaiting()) // 跳过等待,立即激活
  );
});
```

**activate 事件(激活阶段)**
`self.addEventListener('activate', (event) => { event.waitUntil(<Promise>) })`
```javascript
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((names) =>
        Promise.all(
          names
            .filter((n) => n !== CACHE_NAME)
            .map((n) => caches.delete(n))
        )
      )
      .then(() => self.clients.claim()) // 立即接管所有客户端
  );
});
```

**生命周期阶段**

| 阶段       | 事件       | 说明                  |
| ---------- | ---------- | --------------------- |
| Installing | `install`  | 安装中,预缓存资源     |
| Waiting    | -          | 等待旧 SW 释放        |
| Activating | `activate` | 激活中,清理旧缓存     |
| Activated  | -          | 已激活,可拦截请求     |
| Redundant  | -          | 安装失败或被替换      |

---

## fetch 事件与缓存策略

**fetch 事件**
`self.addEventListener('fetch', (event) => { event.respondWith(<Response>) })`
```javascript
// Cache First 优先缓存
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => cached || fetch(event.request))
  );
});
```

**Cache First(适合静态资源)**
```javascript
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => {
      return cached || fetch(event.request);
    })
  );
});
```

**Network First(适合 API 请求)**
```javascript
self.addEventListener('fetch', (event) => {
  event.respondWith(
    fetch(event.request).catch(() => caches.match(event.request))
  );
});
```

**Stale While Revalidate(缓存即时响应,后台更新)**
```javascript
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.open(CACHE_NAME).then((cache) =>
      cache.match(event.request).then((cached) => {
        const fetchPromise = fetch(event.request).then((response) => {
          cache.put(event.request, response.clone());
          return response;
        });
        return cached || fetchPromise;
      })
    )
  );
});
```

**缓存策略对比**

| 策略                       | 说明                   | 适用场景     |
| -------------------------- | ---------------------- | ------------ |
| **Cache First**            | 优先缓存,无则请求网络  | 静态资源     |
| **Network First**          | 优先网络,失败用缓存    | API 请求     |
| **Stale While Revalidate** | 缓存即时响应,后台更新  | 非关键 API   |
| **Network Only**           | 仅网络                 | 实时数据     |
| **Cache Only**             | 仅缓存                 | 离线资源     |

---

## Cache Storage API

**缓存操作方法**
```javascript
// 打开缓存
const cache = await caches.open('my-cache-v1');

// 添加单个资源
await cache.add('/api/data');

// 批量添加
await cache.addAll(['/', '/styles.css', '/app.js']);

// 添加自定义响应
await cache.put('/api/custom', new Response('{"a":1}'));

// 匹配请求
const response = await cache.match('/api/data');

// 删除缓存项
await cache.delete('/api/data');

// 查询所有缓存名
const names = await caches.keys();

// 删除整个缓存
await caches.delete('my-cache-v1');
```

---

## Web App Manifest

**manifest.json 字段**
```json
{
  "name": "我的应用",
  "short_name": "我的App",
  "description": "应用描述",
  "start_url": "/",
  "scope": "/",
  "display": "standalone",
  "orientation": "portrait-primary",
  "background_color": "#ffffff",
  "theme_color": "#1976d2",
  "lang": "zh-CN",
  "dir": "ltr",
  "categories": ["productivity", "utilities"],
  "icons": [
    {
      "src": "/icons/192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/icons/512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "maskable"
    }
  ],
  "shortcuts": [
    {
      "name": "新消息",
      "url": "/messages/new",
      "icons": [{ "src": "/icons/msg.png", "sizes": "96x96" }]
    }
  ]
}
```

| 字段              | 说明                              | 示例值                          |
| ----------------- | --------------------------------- | ------------------------------- |
| `name`            | 应用全名                          | `"我的应用"`                    |
| `short_name`      | 短名(主屏图标)                    | `"我的App"`                     |
| `start_url`       | 启动 URL                          | `"/"`                           |
| `scope`           | 作用域                            | `"/"`                           |
| `display`         | 显示模式                          | `standalone` / `fullscreen` / `minimal-ui` / `browser` |
| `theme_color`     | 主题色                            | `"#1976d2"`                     |
| `background_color`| 启动背景色                        | `"#ffffff"`                     |
| `orientation`     | 屏幕方向                          | `portrait-primary` / `landscape` |
| `icons`           | 图标数组                          | `[{src, sizes, type, purpose}]` |

**HTML 中引用 manifest**
```html
<link rel="manifest" href="/manifest.json" />
<meta name="theme-color" content="#1976d2" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="default" />
<link rel="apple-touch-icon" href="/icons/apple-180.png" />
```

**display 显示模式检测**
```javascript
// 检测是否以 PWA 方式启动
const isStandalone = window.matchMedia('(display-mode: standalone)').matches
  || window.navigator.standalone;

window.matchMedia('(display-mode: standalone)').addEventListener('change', (e) => {
  console.log(e.matches ? 'PWA 模式' : '浏览器模式');
});
```

---

## 推送通知

**Notification API**
```javascript
// 请求通知权限
const permission = await Notification.requestPermission();
// permission: 'granted' | 'denied' | 'default'

// 显示通知
new Notification('标题', {
  body: '通知正文',
  icon: '/icons/192.png',
  badge: '/icons/badge.png',
  tag: 'unique-id', // 相同 tag 会替换
  data: { url: '/page' },
  vibrate: [100, 50, 100],
  requireInteraction: true, // 用户必须手动关闭
});
```

**Push API(服务端推送)**
```javascript
// 主线程:订阅推送
const reg = await navigator.serviceWorker.ready;
const subscription = await reg.pushManager.subscribe({
  userVisibleOnly: true,
  applicationServerKey: urlBase64ToUint8Array(VAPID_PUBLIC_KEY),
});
// 将 subscription 发送到服务端保存
await fetch('/api/subscribe', {
  method: 'POST',
  body: JSON.stringify(subscription),
  headers: { 'Content-Type': 'application/json' },
});
```

**Service Worker 处理推送**
```javascript
self.addEventListener('push', (event) => {
  const data = event.data?.json() ?? { title: '新消息', body: '' };
  event.waitUntil(
    self.registration.showNotification(data.title, {
      body: data.body,
      icon: '/icons/192.png',
      data: data.url,
    })
  );
});

// 通知点击
self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  event.waitUntil(clients.openWindow(event.notification.data || '/'));
});
```

---

## 后台同步

**注册后台同步**
```javascript
const reg = await navigator.serviceWorker.ready;
await reg.sync.register('sync-data');
```

**Service Worker 处理同步**
```javascript
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-data') {
    event.waitUntil(syncData());
  }
});

async function syncData() {
  try {
    await fetch('/api/sync', {
      method: 'POST',
      body: JSON.stringify({ data: 'sync data' }),
    });
  } catch (e) {
    throw e; // 抛出错误会自动重试
  }
}
```

**Periodic Sync(周期同步)**
```javascript
// 注册周期同步
const reg = await navigator.serviceWorker.ready;
const status = await navigator.permissions.query({ name: 'periodic-background-sync' });
if (status.state === 'granted') {
  await reg.periodicSync.register('update-content', {
    minInterval: 24 * 60 * 60 * 1000, // 24 小时
  });
}
```

---

## Clients API

**与客户端通信**
```javascript
// 获取所有客户端
const clients = await self.clients.matchAll({ includeUncontrolled: true, type: 'window' });

// 向所有客户端发送消息
clients.forEach((client) => client.postMessage({ type: 'UPDATE' }));

// 打开新窗口
await self.clients.openWindow('https://example.com');

// 获取当前客户端
const client = await self.clients.get(clientId);
```

---

## PWA 安装

**beforeinstallprompt 事件**
```javascript
let deferredPrompt;

window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  deferredPrompt = e;
  showInstallButton();
});

document.getElementById('installBtn').addEventListener('click', async () => {
  if (!deferredPrompt) return;
  deferredPrompt.prompt();
  const { outcome } = await deferredPrompt.userChoice;
  console.log(outcome); // 'accepted' | 'dismissed'
  deferredPrompt = null;
});

window.addEventListener('appinstalled', () => {
  console.log('应用已安装');
});
```



<!-- ============ 文档分隔线：006-html5/028-SVG.md ============ -->

# SVG 矢量图形 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## SVG 基础

**svg 元素**
`<svg [width] [height] [viewBox="<min-x> <min-y> <width> <height>"] [xmlns="http://www.w3.org/2000/svg"]>...</svg>`
```html
<!-- 基础 SVG -->
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
  <circle cx="100" cy="100" r="80" fill="blue" />
</svg>

<!-- 内联 SVG(HTML 中可直接使用) -->
<svg width="100" height="100">
  <rect width="100" height="100" fill="red" />
</svg>
```

---

## viewBox 坐标系统

**viewBox 详解**
`viewBox="<min-x> <min-y> <width> <height>"`
```html
<!-- 200x150 内部坐标,显示为 400x300 -->
<svg width="400" height="300" viewBox="0 0 200 150">
  <rect x="0" y="0" width="100" height="75" fill="blue" />
</svg>
```

**preserveAspectRatio 属性**
`preserveAspectRatio="[alignment] [meet|slice|none]"`
```html
<svg width="400" height="300" viewBox="0 0 200 150" preserveAspectRatio="xMidYMid meet">
  <rect width="200" height="150" fill="green" />
</svg>
```

| preserveAspectRatio 值 | 说明                   |
| ---------------------- | ---------------------- |
| `xMidYMid meet`        | 居中,完整显示(默认)   |
| `xMidYMid slice`       | 居中,裁剪填充          |
| `xMinYMin meet`        | 左上对齐,完整显示      |
| `none`                 | 不保持比例,拉伸填充    |

---

## 基本形状

**矩形 rect**
`<rect x="<X>" y="<Y>" width="<宽>" height="<高>" [rx="<圆角X>"] [ry="<圆角Y>"] [fill] [stroke] [stroke-width] />`
```html
<rect x="10" y="10" width="100" height="60" rx="10" ry="10" fill="blue" stroke="black" stroke-width="2" />
```

**圆形 circle**
`<circle cx="<圆心X>" cy="<圆心Y>" r="<半径>" [fill] [stroke] />`
```html
<circle cx="200" cy="80" r="50" fill="red" />
```

**椭圆 ellipse**
`<ellipse cx="<圆心X>" cy="<圆心Y>" rx="<X半径>" ry="<Y半径>" [fill] [stroke] />`
```html
<ellipse cx="320" cy="80" rx="60" ry="30" fill="green" />
```

**直线 line**
`<line x1="<起点X>" y1="<起点Y>" x2="<终点X>" y2="<终点Y>" stroke="<颜色>" [stroke-width] />`
```html
<line x1="10" y1="150" x2="390" y2="150" stroke="black" stroke-width="2" />
```

**折线 polyline**
`<polyline points="<x1>,<y1> <x2>,<y2> ..." [fill] [stroke] />`
```html
<polyline points="10,180 50,160 90,200 130,170" fill="none" stroke="purple" stroke-width="2" />
```

**多边形 polygon**
`<polygon points="<x1>,<y1> <x2>,<y2> ..." [fill] [stroke] />`
```html
<polygon points="200,180 240,220 160,220" fill="orange" stroke="black" />
```

---

## 路径 path

**path 元素**
`<path d="<路径命令>" [fill] [stroke] [stroke-width] />`
```html
<!-- 三角形 -->
<path d="M 100 100 L 200 100 L 150 50 Z" fill="yellow" stroke="black" />

<!-- 心形 -->
<path d="M 100 200 C 50 100, 0 200, 100 300 C 200 200, 150 100, 100 200 Z" fill="red" />
```

**路径命令**

| 命令 | 说明           | 示例                  |
| ---- | -------------- | --------------------- |
| `M`  | 移动到(绝对)   | `M 10 10`             |
| `m`  | 移动到(相对)   | `m 10 10`             |
| `L`  | 直线到(绝对)   | `L 100 100`           |
| `l`  | 直线到(相对)   | `l 10 10`             |
| `H`  | 水平线到       | `H 100`               |
| `V`  | 垂直线到       | `V 100`               |
| `C`  | 三次贝塞尔     | `C 20,20 40,20 50,10` |
| `S`  | 平滑三次贝塞尔 | `S 40,20 50,10`       |
| `Q`  | 二次贝塞尔     | `Q 50,0 100,50`       |
| `T`  | 平滑二次贝塞尔 | `T 100,50`            |
| `A`  | 弧线           | `A 25,25 0 0,1 50,25` |
| `Z`  | 闭合路径       | `Z`                   |

> 小写字母为相对坐标,大写字母为绝对坐标。

**A 弧线参数**
`A rx ry x-axis-rotation large-arc-flag sweep-flag x y`
```html
<!-- 半圆弧 -->
<path d="M 50 100 A 50 50 0 0 1 150 100" stroke="red" fill="none" />
```

---

## 文本

**text 元素**
`<text x="<X>" y="<Y>" [font-size] [font-family] [fill] [text-anchor] [dominant-baseline]>[文本]</text>`
```html
<text x="20" y="50" font-size="24" font-family="Arial" fill="black"
      text-anchor="start" dominant-baseline="alphabetic">
  Hello SVG
</text>
```

| text-anchor 值 | 对齐方式   |
| -------------- | ---------- |
| `start`        | 左对齐     |
| `middle`       | 居中       |
| `end`          | 右对齐     |

**tspan 子文本**
```html
<text x="10" y="50">
  <tspan font-weight="bold">Hello</tspan>
  <tspan fill="red">World</tspan>
</text>
```

**textPath 沿路径排版**
```html
<defs>
  <path id="curve" d="M 50 150 Q 200 50, 350 150" />
</defs>
<text font-size="20" fill="blue">
  <textPath href="#curve">沿曲线排列的文字</textPath>
</text>
```

---

## 渐变与滤镜

**线性渐变**
```html
<defs>
  <linearGradient id="lg" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="red" />
    <stop offset="50%" stop-color="yellow" />
    <stop offset="100%" stop-color="blue" />
  </linearGradient>
</defs>
<rect x="50" y="50" width="100" height="80" fill="url(#lg)" />
```

**径向渐变**
```html
<defs>
  <radialGradient id="rg" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="white" />
    <stop offset="100%" stop-color="black" />
  </radialGradient>
</defs>
<circle cx="100" cy="100" r="80" fill="url(#rg)" />
```

**滤镜**
```html
<defs>
  <!-- 高斯模糊 -->
  <filter id="blur">
    <feGaussianBlur stdDeviation="5" />
  </filter>

  <!-- 阴影 -->
  <filter id="shadow">
    <feDropShadow dx="4" dy="4" stdDeviation="3" flood-color="black" flood-opacity="0.5" />
  </filter>
</defs>

<rect x="50" y="50" width="100" height="80" fill="blue" filter="url(#shadow)" />
```

---

## g 分组与 use 引用

**g 分组**
`<g [transform] [fill] [stroke] [opacity]>...</g>`
```html
<g transform="translate(50, 50)" fill="red" stroke="black">
  <rect width="50" height="50" />
  <circle cx="80" cy="25" r="25" />
</g>
```

**defs 与 use**
```html
<defs>
  <symbol id="icon" viewBox="0 0 24 24">
    <circle cx="12" cy="12" r="10" />
  </symbol>
</defs>

<!-- 多次引用 -->
<use href="#icon" x="0" y="0" width="50" height="50" />
<use href="#icon" x="60" y="0" width="50" height="50" fill="red" />
```

---

## SVG 属性参考

**通用样式属性**

| 属性             | 作用              | 示例                  |
| ---------------- | ----------------- | --------------------- |
| `fill`           | 填充颜色          | `fill="red"`          |
| `fill-opacity`   | 填充透明度        | `fill-opacity="0.5"`  |
| `stroke`         | 描边颜色          | `stroke="black"`      |
| `stroke-width`   | 描边宽度          | `stroke-width="2"`    |
| `stroke-opacity` | 描边透明度        | `stroke-opacity="0.8"`|
| `stroke-linecap` | 线帽 butt/round/square | `stroke-linecap="round"` |
| `stroke-linejoin`| 连接 miter/round/bevel | `stroke-linejoin="round"` |
| `stroke-dasharray` | 虚线           | `stroke-dasharray="5,5"` |
| `opacity`        | 整体透明度        | `opacity="0.8"`       |
| `transform`      | 变换              | `transform="rotate(45)"` |

**transform 变换**
```html
<!-- translate/scale/rotate/skew -->
<g transform="translate(50,50) rotate(45) scale(1.5)">
  <rect width="100" height="100" />
</g>
```

---

## SVG 动画

**SMIL 动画(SVG 原生)**
```html
<rect x="0" y="0" width="50" height="50" fill="red">
  <animate attributeName="x" from="0" to="200" dur="2s" repeatCount="indefinite" />
</rect>

<circle cx="50" cy="50" r="20" fill="blue">
  <animate attributeName="r" values="20;40;20" dur="2s" repeatCount="indefinite" />
</circle>
```

**CSS 动画**
```html
<style>
  .box {
    animation: move 2s infinite alternate;
  }
  @keyframes move {
    from { transform: translateX(0); }
    to { transform: translateX(100px); }
  }
</style>

<svg>
  <rect class="box" width="50" height="50" fill="red" />
</svg>
```

---

## SVG 在 HTML 中的使用

**直接内联**
```html
<svg width="50" height="50">
  <circle cx="25" cy="25" r="20" fill="red" />
</svg>
```

**img 引用**
```html
<img src="icon.svg" alt="图标" width="50" height="50" />
```

**CSS 背景**
```css
.icon {
  background: url('icon.svg') no-repeat center;
  width: 50px;
  height: 50px;
}
```

**object 引用**
```html
<object data="icon.svg" type="image/svg+xml" width="50" height="50"></object>
```



<!-- ============ 文档分隔线：006-html5/029-WebWorkers.md ============ -->

# Web 工作线程 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Dedicated Worker 专用 Worker

**创建 Worker**
`const worker = new Worker(<scriptURL>, [options])`
```javascript
// 主线程
const worker = new Worker('worker.js');

// 发送消息给 Worker
worker.postMessage({ type: 'CALCULATE', data: [1, 2, 3, 4, 5] });

// 接收 Worker 消息
worker.onmessage = (e) => console.log('Worker 返回:', e.data);

// 错误处理
worker.onerror = (e) => console.error('Worker 错误:', e.message);

// 终止 Worker
worker.terminate();
```

**Worker 线程脚本**
```javascript
// worker.js
self.onmessage = (e) => {
  const { type, data } = e.data;
  if (type === 'CALCULATE') {
    const result = data.reduce((sum, n) => sum + n * n, 0);
    self.postMessage({ type: 'RESULT', data: result });
  }
};
```

**Worker options 选项**

| 字段          | 说明                                | 示例                 |
| ------------- | ----------------------------------- | -------------------- |
| `type`        | 模块类型 classic/module              | `{ type: 'module' }` |
| `name`        | Worker 名称(用于调试)              | `{ name: 'calc' }`   |
| `credentials` | 凭证 include/same-origin/omit       | `{ credentials: 'same-origin' }` |

**Worker 全局上下文**
```javascript
// worker.js 中
self.name;            // Worker 名称
self.location;        // Worker 脚本 URL
self.navigator;       // navigator 对象
self.importScripts(); // 同步引入脚本(仅 classic 模式)

// 关闭 Worker
self.close();
```

**importScripts 引入脚本**
```javascript
// worker.js
importScripts('lib.js', 'helper.js');

// module 模式使用 import
import { helper } from './helper.js';
```

---

## Worker 通信

**postMessage 基础通信**
```javascript
// 主线程
worker.postMessage('文本消息');
worker.postMessage({ type: 'task', payload: data });
worker.postMessage({ buffer }, [buffer]); // 转移所有权

// Worker
self.postMessage({ result: '完成' });
```

**结构化克隆与可转移对象**
```javascript
// 主线程:转移 ArrayBuffer 所有权(零拷贝)
const buffer = new ArrayBuffer(1024 * 1024);
worker.postMessage({ buffer }, [buffer]);
// 主线程的 buffer 此后不可用

// Worker 端接收
self.onmessage = (e) => {
  const { buffer } = e.data;
  const view = new Uint8Array(buffer);
  view[0] = 255;
  self.postMessage({ buffer }, [buffer]); // 再传回
};
```

**Transferable Objects 类型**

| 类型                | 说明                  |
| ------------------- | --------------------- |
| `ArrayBuffer`       | 二进制数据缓冲区      |
| `MessagePort`       | 消息端口              |
| `ImageBitmap`       | 图像位图              |
| `OffscreenCanvas`   | 离屏 Canvas           |
| `ReadableStream`    | 可读流                |
| `WritableStream`    | 可写流                |
| `TransformStream`   | 转换流                |
| `AudioData`         | 音频数据              |

---

## 内联 Worker

**通过 Blob 创建内联 Worker**
```javascript
const code = `
  self.onmessage = (e) => {
    const result = e.data.reduce((s, n) => s + n * n, 0);
    self.postMessage(result);
  };
`;
const blob = new Blob([code], { type: 'application/javascript' });
const worker = new Worker(URL.createObjectURL(blob));

worker.postMessage([1, 2, 3, 4, 5]);
worker.onmessage = (e) => console.log('结果:', e.data);
```

---

## Shared Worker 共享 Worker

**创建 SharedWorker**
`const worker = new SharedWorker(<scriptURL>, [name])`
```javascript
// 主线程(可被多个标签页共享)
const worker = new SharedWorker('shared-worker.js');

// 启动端口
worker.port.start();

// 通过 port 通信
worker.port.postMessage('Hello');
worker.port.onmessage = (e) => console.log('收到:', e.data);

// 关闭端口
worker.port.close();
```

**SharedWorker 脚本**
```javascript
// shared-worker.js
const connections = [];

self.onconnect = (e) => {
  const port = e.ports[0];
  connections.push(port);

  port.onmessage = (e) => {
    // 广播给所有连接
    connections.forEach((p) => p.postMessage(e.data));
  };

  port.start();
};
```

---

## Worker 池

**Worker 池实现**
```javascript
class WorkerPool {
  constructor(workerScript, poolSize = navigator.hardwareConcurrency) {
    this.workers = Array.from({ length: poolSize }, () => new Worker(workerScript));
  }

  execute(data) {
    return new Promise((resolve) => {
      const worker = this.workers.pop();
      worker.onmessage = (e) => {
        resolve(e.data);
        this.workers.push(worker);
      };
      worker.postMessage(data);
    });
  }

  terminate() {
    this.workers.forEach((w) => w.terminate());
  }
}

// 使用
const pool = new WorkerPool('worker.js', 4);
const results = await Promise.all([
  pool.execute([1, 2, 3]),
  pool.execute([4, 5, 6]),
  pool.execute([7, 8, 9]),
]);
```

---

## Worker 中可用 API

**可在 Worker 中使用的 API**
```javascript
// worker.js
// 网络
fetch('https://api.example.com/data');
const ws = new WebSocket('wss://example.com');

// IndexedDB
const db = indexedDB.open('mydb');

// Cache Storage
const cache = await caches.open('my-cache');

// setTimeout / setInterval
setTimeout(() => self.postMessage('done'), 1000);

// FileReader / Blob / URL
const reader = new FileReader();

// OffscreenCanvas(主线程 transferControlToOffscreen)
const ctx = offscreenCanvas.getContext('2d');
```

**不可在 Worker 中使用的 API**
- DOM 操作(document, window, parent)
- localStorage / sessionStorage
- XMLHttpRequest(部分旧版不支持)
- 某些 UI 相关 API

---

## OffscreenCanvas

**主线程转移控制权**
```javascript
const canvas = document.getElementById('canvas');
const offscreen = canvas.transferControlToOffscreen();

const worker = new Worker('canvas-worker.js');
worker.postMessage({ canvas: offscreen }, [offscreen]);
```

**Worker 中绘制**
```javascript
// canvas-worker.js
self.onmessage = (e) => {
  const canvas = e.data.canvas;
  const ctx = canvas.getContext('2d');

  ctx.fillStyle = 'red';
  ctx.fillRect(10, 10, 100, 50);

  // 动画循环
  let x = 0;
  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = 'blue';
    ctx.fillRect(x, 10, 50, 50);
    x = (x + 2) % canvas.width;
    requestAnimationFrame(animate);
  }
  animate();
};
```

---

## Worker 类型与场景

| Worker 类型       | 创建方式                        | 共享范围         | 适用场景               |
| ----------------- | ------------------------------- | ---------------- | ---------------------- |
| Dedicated Worker  | `new Worker()`                  | 单个页面         | 密集计算、数据处理     |
| Shared Worker     | `new SharedWorker()`            | 多个同源页面     | 共享状态、广播         |
| Service Worker    | `navigator.serviceWorker.register()` | 全域名(网络代理) | 离线缓存、推送通知     |
| Audio Worklet     | `audioContext.audioWorklet.addModule()` | 音频线程     | 音频处理               |

---

## MessageChannel 双向通信

**主线程创建通道**
```javascript
const channel = new MessageChannel();

const worker1 = new Worker('worker1.js');
const worker2 = new Worker('worker2.js');

// 将 port1 给 worker1,port2 给 worker2
worker1.postMessage({ port: channel.port1 }, [channel.port1]);
worker2.postMessage({ port: channel.port2 }, [channel.port2]);
```

**Worker 间通过端口通信**
```javascript
// worker1.js
self.onmessage = (e) => {
  const port = e.data.port;
  port.postMessage('来自 worker1');
  port.onmessage = (e) => console.log('收到:', e.data);
};

// worker2.js
self.onmessage = (e) => {
  const port = e.data.port;
  port.onmessage = (e) => {
    console.log('收到:', e.data);
    port.postMessage('来自 worker2');
  };
};
```

---

## BroadcastChannel 广播

**跨上下文广播**
```javascript
// 主线程或 Worker 中
const channel = new BroadcastChannel('app-events');

// 监听消息
channel.onmessage = (e) => {
  console.log('收到广播:', e.data);
};

// 发送广播(所有同源页面和 Worker 都能收到)
channel.postMessage({ type: 'UPDATE', data: '新数据' });

// 关闭
channel.close();
```

---

## 错误处理

**Worker 错误事件**
```javascript
worker.onerror = (e) => {
  console.error('错误信息:', e.message);
  console.error('文件:', e.filename);
  console.error('行号:', e.lineno);
  console.error('列号:', e.colno);
};
```

**Worker 内部错误捕获**
```javascript
// worker.js
self.onerror = (message, filename, lineno, colno, error) => {
  console.error('Worker 错误:', message);
  return true; // 阻止默认行为
};

try {
  // 可能出错的代码
} catch (e) {
  self.postMessage({ type: 'ERROR', error: e.message });
}
```



<!-- ============ 文档分隔线：006-html5/030-WebComponentsPWADevelopment.md ============ -->

# Web Components 与 PWA 开发 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Custom Elements 自定义元素

**定义自定义元素**
`customElements.define(<名称>, <类>, [options])`
```javascript
class MyElement extends HTMLElement {
  constructor() {
    super();
    // 元素初始化
  }

  // 当元素被添加到 DOM 时调用
  connectedCallback() {
    this.innerHTML = `<p>Hello, Web Components!</p>`;
  }

  // 当元素从 DOM 中移除时调用
  disconnectedCallback() {
    // 清理资源
  }

  // 当属性变化时调用
  attributeChangedCallback(name, oldValue, newValue) {
    // 处理属性变化
  }

  // 定义需要观察的属性
  static get observedAttributes() {
    return ['title'];
  }

  // 元素被移动到新文档时调用
  adoptedCallback() {}
}

// 注册自定义元素(名称必须包含连字符)
customElements.define('my-element', MyElement);
```

**使用自定义元素**
```html
<my-element title="Hello"></my-element>
```

**生命周期回调**

| 回调方法                                             | 触发时机             |
| :--------------------------------------------------- | :------------------- |
| `constructor()`                                      | 元素创建时           |
| `connectedCallback()`                                | 元素添加到 DOM 时    |
| `disconnectedCallback()`                             | 元素从 DOM 中移除时  |
| `attributeChangedCallback(name, oldValue, newValue)` | 属性变化时           |
| `adoptedCallback()`                                  | 元素被移动到新文档时 |

**CustomizedElement 内置扩展**
```javascript
class FancyButton extends HTMLButtonElement {
  constructor() {
    super();
    this.addEventListener('click', () => console.log('点击'));
  }
}

// 扩展内置元素
customElements.define('fancy-button', FancyButton, { extends: 'button' });
```

```html
<!-- 使用 is 属性 -->
<button is="fancy-button">点击</button>
```

**元素查询与升级**
```javascript
// 获取自定义元素引用
const el = customElements.get('my-element');

// 强制升级未定义的元素
await customElements.whenDefined('my-element');
console.log('my-element 已定义');
```

---

## Shadow DOM 影子 DOM

**attachShadow 创建 Shadow DOM**
`element.attachShadow({ mode: 'open' | 'closed' })`
```javascript
class MyElement extends HTMLElement {
  constructor() {
    super();
    // 创建 Shadow DOM
    const shadow = this.attachShadow({ mode: 'open' });

    // 创建样式
    const style = document.createElement('style');
    style.textContent = `
      p {
        color: blue;
        font-size: 18px;
      }
    `;

    // 创建内容
    const p = document.createElement('p');
    p.textContent = 'Hello from Shadow DOM!';

    shadow.appendChild(style);
    shadow.appendChild(p);
  }
}
customElements.define('my-shadow-element', MyElement);
```

| mode 值   | 说明                                  |
| --------- | ------------------------------------- |
| `'open'`  | 外部可通过 `element.shadowRoot` 访问   |
| `'closed'`| 拒绝外部访问 `element.shadowRoot` 为 null |

**Shadow DOM 模板化**
```javascript
class MyTemplateElement extends HTMLElement {
  constructor() {
    super();
    const shadow = this.attachShadow({ mode: 'open' });
    const template = document.getElementById('my-template');
    const content = template.content.cloneNode(true);

    content.querySelector('h3').textContent = this.getAttribute('title') || '默认标题';
    content.querySelector('p').textContent = this.getAttribute('message') || '默认内容';
    shadow.appendChild(content);
  }
}
customElements.define('my-template-element', MyTemplateElement);
```

**shadowRoot 操作**
```javascript
// 获取 shadowRoot(open 模式)
const shadow = element.shadowRoot;

// 在 shadow 中查询元素
const innerEl = shadow.querySelector('.inner');

// 在 shadow 中添加元素
shadow.appendChild(document.createElement('div'));
```

**Declarative Shadow DOM(声明式 Shadow DOM)**
```html
<host-element>
  <template shadowrootmode="open">
    <style>p { color: red; }</style>
    <p>声明式 Shadow DOM 内容</p>
  </template>
</host-element>
```

---

## HTML Templates 模板

**template 元素**
```html
<template id="my-template">
  <style>
    .container {
      padding: 20px;
      background: #f0f0f0;
      border-radius: 8px;
    }
    h3 {
      color: #333;
    }
  </style>
  <div class="container">
    <h3></h3>
    <p></p>
  </div>
</template>
```

**使用模板**
```javascript
class MyTemplateElement extends HTMLElement {
  constructor() {
    super();
    const shadow = this.attachShadow({ mode: 'open' });

    // 获取模板
    const template = document.getElementById('my-template');
    // 克隆模板内容
    const content = template.content.cloneNode(true);

    // 填充内容
    content.querySelector('h3').textContent = this.getAttribute('title') || 'Default';
    content.querySelector('p').textContent = this.getAttribute('message') || 'Message';

    shadow.appendChild(content);
  }
}
customElements.define('my-template-element', MyTemplateElement);
```

**slot 插槽**
```html
<!-- 组件定义 -->
<template id="card-template">
  <div class="card">
    <slot name="header">默认头部</slot>
    <hr />
    <slot>默认内容</slot>
  </div>
</template>
```

```html
<!-- 使用插槽 -->
<my-card>
  <span slot="header">自定义头部</span>
  <p>自定义内容</p>
</my-card>
```

**slotchange 事件**
```javascript
const slot = shadow.querySelector('slot');
slot.addEventListener('slotchange', (e) => {
  const assigned = e.target.assignedNodes();
  console.log('插槽内容变化', assigned);
});
```

---

## CSS Scoping 样式隔离

**CSS 自定义属性穿透**
```css
/* 外部定义变量 */
:host {
  --primary-color: #1976d2;
}

/* shadow 内部使用 */
.button {
  background: var(--primary-color);
}
```

**host 选择器**
```css
/* 选中宿主元素 */
:host {
  display: block;
}

/* 选中具有特定类的宿主 */
:host(.active) {
  opacity: 1;
}

/* 选中特定宿主标签 */
:host(my-button) {
  border-radius: 4px;
}
```

**:host-context 上下文选择器**
```css
/* 当祖先元素具有 .dark-theme 时 */
:host-context(.dark-theme) {
  background: #333;
  color: #fff;
}
```

**::part() 伪元素**
```javascript
// 组件内
shadow.innerHTML = `
  <div part="container">
    <span part="label">标签</span>
  </div>
`;
```

```css
/* 外部样式表选中 part */
my-element::part(container) {
  background: red;
}
my-element::part(label) {
  color: white;
}
```

---

## PWA Web App Manifest

**manifest.json 完整字段**
```json
{
  "name": "My PWA",
  "short_name": "PWA",
  "description": "A progressive web app",
  "start_url": "/",
  "scope": "/",
  "display": "standalone",
  "display_override": ["window-controls-overlay", "standalone"],
  "background_color": "#ffffff",
  "theme_color": "#4A90E2",
  "orientation": "any",
  "lang": "zh-CN",
  "dir": "ltr",
  "categories": ["productivity", "utilities"],
  "icons": [
    {
      "src": "/icons/icon-192.png",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any"
    },
    {
      "src": "/icons/icon-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "maskable"
    }
  ],
  "screenshots": [
    {
      "src": "/screenshots/home.png",
      "sizes": "1280x720",
      "type": "image/png",
      "form_factor": "wide"
    }
  ],
  "shortcuts": [
    {
      "name": "新消息",
      "short_name": "消息",
      "url": "/messages/new",
      "icons": [{ "src": "/icons/msg.png", "sizes": "96x96" }]
    }
  ],
  "file_handlers": [
    {
      "action": "/open-file",
      "accept": { "image/*": [".png", ".jpg"] }
    }
  ]
}
```

**HTML 中引用 manifest**
```html
<link rel="manifest" href="/manifest.json" />
<meta name="theme-color" content="#4A90E2" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-title" content="My PWA" />
<link rel="apple-touch-icon" href="/icons/apple-180.png" />
```

**display 显示模式**

| display 值      | 说明                              |
| --------------- | --------------------------------- |
| `fullscreen`    | 全屏(无 UI)                       |
| `standalone`    | 独立应用(无浏览器 UI)             |
| `minimal-ui`    | 最小 UI(部分浏览器控件)           |
| `browser`       | 标准浏览器(默认)                  |

---

## PWA 安装

**beforeinstallprompt 事件**
```javascript
let deferredPrompt;

window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  deferredPrompt = e;
  showInstallButton();
});

document.getElementById('installBtn').addEventListener('click', async () => {
  if (!deferredPrompt) return;
  deferredPrompt.prompt();
  const { outcome } = await deferredPrompt.userChoice;
  console.log(outcome); // 'accepted' | 'dismissed'
  deferredPrompt = null;
});

window.addEventListener('appinstalled', () => {
  console.log('应用已安装');
});
```

**Window Controls Overlay**
```javascript
// 检测支持
const supported = 'windowControlsOverlay' in navigator;

// 监听变化
navigator.windowControlsOverlay.addEventListener('geometrychange', (e) => {
  console.log('标题栏区域变化', e.titlebarAreaRect);
});
```

---

## Fetch 拦截(SW)

**fetch 事件处理**
`self.addEventListener('fetch', (event) => { event.respondWith(<Response>) })`
```javascript
// service-worker.js
const CACHE_NAME = 'my-pwa-cache-v1';
const ASSETS = ['/', '/index.html', '/styles.css', '/app.js'];

// 安装:预缓存
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
      .then(() => self.skipWaiting())
  );
});

// 激活:清理旧缓存
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((names) =>
      Promise.all(names.filter((n) => n !== CACHE_NAME).map((n) => caches.delete(n)))
    ).then(() => self.clients.claim())
  );
});

// 拦截请求
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => {
      if (cached) return cached;
      return fetch(event.request).then((response) => {
        if (response && response.status === 200 && response.type === 'basic') {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
        }
        return response;
      });
    })
  );
});
```

**缓存策略对比**

| 策略                       | 说明                   | 适用场景     |
| -------------------------- | ---------------------- | ------------ |
| **Cache First**            | 优先缓存,无则请求网络  | 静态资源     |
| **Network First**          | 优先网络,失败用缓存    | API 请求     |
| **Stale While Revalidate** | 缓存即时响应,后台更新  | 非关键 API   |
| **Network Only**           | 仅网络                 | 实时数据     |
| **Cache Only**             | 仅缓存                 | 离线资源     |

---

## 通知与推送

**请求通知权限**
```javascript
if ('Notification' in window) {
  Notification.requestPermission().then((permission) => {
    if (permission === 'granted') {
      console.log('通知权限已授予');
    }
  });
}
```

**显示通知**
```javascript
function sendNotification() {
  if ('serviceWorker' in navigator && 'PushManager' in window) {
    navigator.serviceWorker.ready.then((registration) => {
      registration.showNotification('Hello PWA!', {
        body: 'This is a push notification',
        icon: '/icons/icon-192.png',
        badge: '/icons/badge.png',
        vibrate: [100, 50, 100],
        data: { url: '/notifications' },
        actions: [
          { action: 'open', title: '打开' },
          { action: 'close', title: '关闭' },
        ],
      });
    });
  }
}
```

---

## 后台同步

**注册后台同步**
```javascript
if ('serviceWorker' in navigator && 'SyncManager' in window) {
  navigator.serviceWorker.ready
    .then((registration) => registration.sync.register('sync-data'))
    .then(() => console.log('已注册后台同步'))
    .catch((error) => console.error('注册失败:', error));
}
```

**Service Worker 处理同步**
```javascript
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-data') {
    event.waitUntil(syncData());
  }
});

async function syncData() {
  try {
    const response = await fetch('/api/sync', {
      method: 'POST',
      body: JSON.stringify({ data: 'sync data' }),
    });
    console.log('同步完成:', await response.json());
  } catch (error) {
    console.error('同步失败:', error);
    throw error;
  }
}
```
