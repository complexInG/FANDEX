---
order: 570
title: ES2023/2024/2025 新特性
module: 'javascript'
category: 前端技术
difficulty: beginner
description: ES2023/2024/2025 新特性 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## ES2023 数组非破坏方法

**基本写法：返回排序副本**
`<数组>.toSorted([比较函数])`
```javascript
// 不修改原数组，返回新排序数组
const arr = [3, 1, 2];
const sorted = arr.toSorted(); // [1, 2, 3]，arr 保持 [3, 1, 2]
```

---

**基本写法：返回反转副本**
`<数组>.toReversed()`
```javascript
// 返回反转后的新数组
const a = [1, 2, 3];
const r = a.toReversed(); // [3, 2, 1]
```

---

**基本写法：返回替换副本**
`<数组>.with(<索引>, <值>)`
```javascript
// 返回替换指定索引后的新数组
const a = [1, 2, 3];
const b = a.with(0, 9); // [9, 2, 3]
```

---

**基本写法：从末尾查找**
`<数组>.findLast(<回调>)`
```javascript
// 从尾部向前查找第一个满足条件的元素
const nums = [1, 2, 3, 4];
const lastEven = nums.findLast(x => x % 2 === 0); // 4
```

---

**基本写法：从末尾查找索引**
`<数组>.findLastIndex(<回调>)`
```javascript
// 返回从末尾查找的索引，未找到返回 -1
const idx = [1, 2, 3, 4].findLastIndex(x => x % 2 === 0); // 3
```

---

## ES2024 分组与原子等待

**基本写法：按键分组（数组方法）**
`<数组>.groupBy(<回调>)`
```javascript
// 按回调返回值分组，返回普通对象
const list = [6.1, 4.2, 6.3];
const grouped = Object.groupBy(list, Math.floor);
// { '4': [4.2], '6': [6.1, 6.3] }
```

---

**基本写法：按键分组（Map 版）**
`<数组>.groupByToMap(<回调>)`
```javascript
// 返回 Map，键可为任意类型
const data = [{ type: 'a' }, { type: 'b' }];
const m = Map.groupBy(data, x => x.type);
```

---

**基本写法：原子等待通知**
`Atomics.wait(<数组>, <索引>, <值>)`
```javascript
// 在共享内存上阻塞等待值变化，用于 Worker 同步
Atomics.wait(int32, 0, 0);
```

---

**基本写法：原子通知**
`Atomics.notify(<数组>, <索引>, <数量>)`
```javascript
// 唤醒等待的代理
Atomics.notify(int32, 0, 1);
```

---

## ES2024 Promise.withResolvers

**基本写法：创建可控 Promise**
`Promise.withResolvers()`
```javascript
// 返回 { promise, resolve, reject }，无需在执行器内捕获
const { promise, resolve, reject } = Promise.withResolvers();

stream.on('data', resolve);
stream.on('error', reject);
await promise;
```

---

## ES2025 Iterator Helpers

**基本写法：迭代器 map**
`<迭代器>.map(<回调>)`
```javascript
// 惰性求值，不生成中间数组
const it = [1, 2, 3].values().map(x => x * 2);
for (const v of it) console.log(v); // 2, 4, 6
```

---

**基本写法：迭代器 filter**
`<迭代器>.filter(<回调>)`
```javascript
// 过滤后仍为迭代器
const evens = [1, 2, 3, 4].values().filter(x => x % 2 === 0);
console.log(evens.toArray()); // [2, 4]
```

---

**基本写法：迭代器 take/drop**
`<迭代器>.take(<数量>)`
```javascript
// 取前 N 个或跳过前 N 个
const first3 = gen().take(3);
const rest = gen().drop(2);
```

---

**基本写法：迭代器归约**
`<迭代器>.reduce(<回调>, <初始值>)`
```javascript
// 直接对迭代器求和
const sum = [1, 2, 3].values().reduce((a, b) => a + b, 0); // 6
```

---

**基本写法：迭代器转数组**
`<迭代器>.toArray()`
```javascript
// 收集为真实数组
const arr = [1, 2, 3].values().map(x => x + 1).toArray(); // [2, 3, 4]
```

---

## ES2025 Set 集合运算

**基本写法：并集**
`<集合>.union(<其他集合>)`
```javascript
// 返回新 Set，包含两者全部元素
const u = new Set([1, 2]).union(new Set([2, 3])); // {1, 2, 3}
```

---

**基本写法：交集**
`<集合>.intersection(<其他集合>)`
```javascript
// 返回共同元素的新 Set
const i = new Set([1, 2, 3]).intersection(new Set([2, 3, 4])); // {2, 3}
```

---

**基本写法：差集**
`<集合>.difference(<其他集合>)`
```javascript
// 返回当前集合有而另一集合没有的元素
const d = new Set([1, 2, 3]).difference(new Set([2])); // {1, 3}
```

---

**基本写法：对称差集**
`<集合>.symmetricDifference(<其他集合>)`
```javascript
// 返回只在其中一个集合出现的元素
const s = new Set([1, 2]).symmetricDifference(new Set([2, 3])); // {1, 3}
```

---

**基本写法：子集判断**
`<集合>.isSubsetOf(<其他集合>)`
```javascript
// 判断当前集合是否为另一集合的子集
new Set([1, 2]).isSubsetOf(new Set([1, 2, 3])); // true
```

---

**基本写法：超集判断**
`<集合>.isSupersetOf(<其他集合>)`
```javascript
// 判断当前集合是否为另一集合的超集
new Set([1, 2, 3]).isSupersetOf(new Set([1, 2])); // true
```

---

**基本写法：无交集判断**
`<集合>.isDisjointFrom(<其他集合>)`
```javascript
// 判断两集合是否无共同元素
new Set([1, 2]).isDisjointFrom(new Set([3, 4])); // true
```

---

## ES2025 Promise.try

**基本写法：统一捕获同步异常**
`Promise.try(<函数>)`
```javascript
// 同步抛错也转为 rejected Promise，避免微任务延迟
Promise.try(() => {
  if (Math.random() > 0.5) throw new Error('boom');
  return fetchData();
}).catch(console.error);
```

---

## ES2025 Import Attributes

**基本写法：导入 JSON 模块**
`import <名> from <路径> with { type: 'json' }`
```javascript
// 用 with 显式声明模块类型
import config from './config.json' with { type: 'json' };
console.log(config.port);
```

---

**基本写法：动态导入带属性**
`import(<路径>, { with: { type: '<类型>' } })`
```javascript
// 动态导入同样支持属性声明
const mod = await import('./data.json', { with: { type: 'json' } });
```

---

## ES2025 正则增强

**基本写法：转义正则特殊字符**
`RegExp.escape(<字符串>)`
```javascript
// 安全转义字符串用于正则匹配
const re = new RegExp(RegExp.escape('file.(txt)'));
re.test('file.(txt)'); // true
```

---

**基本写法：正则内联标志**
`/(?<标志>:<子模式>)/`
```javascript
// 局部启用忽略大小写
/HELLO(?i: World)/.test('HELLO world'); // true
```

---

**基本写法：重复命名捕获组**
`/分支1(?<名>)|分支2(?<名>)/`
```javascript
// 不同分支可复用同名捕获组
const r = /ECMAScript(?<v>[0-9]{4})|ES(?<v>[0-9]{2})/;
'ECMAScript2025'.match(r).groups.v; // '2025'
```

---

## ES2025 Float16Array

**基本写法：半精度浮点数组**
`new Float16Array(<长度>)`
```javascript
// 16 位浮点 TypedArray，节省显存与带宽
const f16 = new Float16Array(4);
f16[0] = 1.5;
```

---

**基本写法：DataView 读写半精度**
`<DataView>.getFloat16(<偏移>)`
```javascript
// DataView 新增半精度读写方法
const dv = new DataView(new ArrayBuffer(2));
dv.setFloat16(0, 1.5);
dv.getFloat16(0); // 1.5
```

---

**基本写法：半精度舍入**
`Math.f16round(<数值>)`
```javascript
// 返回最接近的半精度浮点数
Math.f16round(1.337); // 按 float16 精度舍入
```

## 核心知识点

> 一句话记住新特性：数组新增非破坏方法（toSorted/toReversed/with/findLast），`Object.groupBy` 分组，Promise 新增 `withResolvers`，正则支持 `v` 标志。

- `toSorted()`/`toReversed()`/`toSpliced()`/`with()`：不修改原数组，返回副本；
- `findLast()`/`findLastIndex()`：从末尾查找；
- `Object.groupBy()`：按键分组为普通对象；`Map.groupBy()` 返回 Map；
- `Promise.withResolvers()`：一次拿到 resolve/reject；
- `RegExp v` 标志：增强字符类与集合运算；
- `ArrayBuffer` 新方法：`resize()`/`transfer()`。

## 动手试试

1. 用 `toSorted` 排序一组数据，确认原数组不变；
2. 用 `Object.groupBy` 把商品按分类分组；
3. 用 `Promise.withResolvers` 改写一个手动 resolve 的场景；
4. 进阶挑战：用 `with()` 实现不可变更新（配合 React 状态）。

## 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 环境不支持 | 新特性需要新版运行时 | 确认目标环境或引入 polyfill |
| 把新方法当旧方法 | 破坏性/非破坏性混淆 | 阅读返回值与副作用 |
| groupBy 键为对象 | 普通对象键会转字符串 | 用 Map.groupBy |

## 扩展学习

- 数组方法：`javascript/009-ArrayHigherOrderMethod`；
- Promise：`javascript/027-PromiseStaticMethod`；
- 正则：`javascript/011-Regex`。
