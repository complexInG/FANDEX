---
order: 10
title: javascript 模块文档合集
module: 'javascript'
category: 前端技术
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：008-javascript/001-VariableDataType.md ============ -->

# JavaScript 变量与数据类型

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 变量声明

**基本写法：let 声明**
`let <变量名> = <值>;`
```javascript
// 声明可变变量
let age = 18;
```

---

**基本写法：const 声明**
`const <常量名> = <值>;`
```javascript
// 声明不可变常量
const PI = 3.14159;
```

---

**基本写法：var 声明**
`var <变量名> = <值>;`
```javascript
// 声明函数级作用域变量
var name = "Alice";
```

---

**基本写法：多变量声明**
`let <变量1> = <值1>, <变量2> = <值2>;`
```javascript
// 一次声明多个变量
let x = 1, y = 2, z = 3;
```

---

**基本写法：解构声明**
`let { <属性1>, <属性2> } = <对象>;`
```javascript
// 对象解构声明变量
let { name, age } = user;
```

---

**基本写法：数组解构声明**
`let [ <变量1>, <变量2> ] = <数组>;`
```javascript
// 数组解构声明变量
let [first, second] = numbers;
```

---

## 原始数据类型

**基本写法：Number 类型**
`let <变量> = <数字>;`
```javascript
// 声明数字类型
let count = 42;
```

---

**基本写法：浮点数**
`let <变量> = <浮点数>;`
```javascript
// 声明浮点数
let price = 9.99;
```

---

**基本写法：String 类型**
`let <变量> = "<字符串>";`
```javascript
// 声明字符串
let name = "Hello";
```

---

**基本写法：模板字符串**
`let <变量> = \`<模板>\`;`
```javascript
// 使用模板字符串嵌入变量
let greeting = `Hello, ${name}!`;
```

---

**基本写法：Boolean 类型**
`let <变量> = <true|false>;`
```javascript
// 声明布尔值
let isActive = true;
```

---

**基本写法：null 值**
`let <变量> = null;`
```javascript
// 声明空值
let data = null;
```

---

**基本写法：undefined 值**
`let <变量> = undefined;`
```javascript
// 声明未定义值
let value = undefined;
```

---

**基本写法：Symbol 类型**
`let <变量> = Symbol("<描述>");`
```javascript
// 创建唯一符号
let id = Symbol("id");
```

---

**基本写法：BigInt 类型**
`let <变量> = <大整数>n;`
```javascript
// 声明大整数
let big = 9007199254740991n;
```

---

## 引用数据类型

**基本写法：Object 类型**
`let <变量> = { <键>: <值> };`
```javascript
// 声明对象
let user = { name: "Alice", age: 25 };
```

---

**基本写法：Array 类型**
`let <变量> = [ <元素1>, <元素2> ];`
```javascript
// 声明数组
let numbers = [1, 2, 3];
```

---

**基本写法：Function 类型**
`let <变量> = function() { };`
```javascript
// 声明函数表达式
let greet = function() {
};
```

---

**基本写法：Date 类型**
`let <变量> = new Date();`
```javascript
// 创建日期对象
let now = new Date();
```

---

**基本写法：RegExp 类型**
`let <变量> = /<模式>/<标志>;`
```javascript
// 创建正则表达式
let pattern = /hello/gi;
```

---

## 类型检查

**基本写法：typeof 操作符**
`typeof <变量>`
```javascript
// 获取变量类型字符串
let type = typeof name;
```

---

**基本写法：instanceof 操作符**
`<对象> instanceof <构造函数>`
```javascript
// 检查对象是否为某构造函数的实例
let isArray = arr instanceof Array;
```

---

**基本写法：Array.isArray**
`Array.isArray(<变量>)`
```javascript
// 检查变量是否为数组
let isArray = Array.isArray(numbers);
```

---

**基本写法：Object.prototype.toString**
`Object.prototype.toString.call(<变量>)`
```javascript
// 获取对象精确类型
let type = Object.prototype.toString.call(obj);
```

---

## 类型转换

**基本写法：转字符串**
`String(<值>)`
```javascript
// 将值转换为字符串
let str = String(123);
```

---

**基本写法：toString 方法**
`<值>.toString()`
```javascript
// 调用 toString 方法转换
let str = (123).toString();
```

---

**基本写法：转数字**
`Number(<值>)`
```javascript
// 将字符串转换为数字
let num = Number("123");
```

---

**基本写法：parseInt**
`parseInt(<字符串>, <基数>)`
```javascript
// 解析整数
let num = parseInt("42px", 10);
```

---

**基本写法：parseFloat**
`parseFloat(<字符串>)`
```javascript
// 解析浮点数
let num = parseFloat("3.14abc");
```

---

**基本写法：转布尔**
`Boolean(<值>)`
```javascript
// 将值转换为布尔
let bool = Boolean(0);
```

---

**基本写法：双重否定转布尔**
`!!<值>`
```javascript
// 使用双重否定转换为布尔
let bool = !!value;
```

---

## 变量作用域

**基本写法：全局作用域**
`<变量名> = <值>;`
```javascript
// 不使用关键字声明为全局变量
globalVar = 10;
```

---

**基本写法：函数作用域**
`function <函数>() { var <变量> = <值>; }`
```javascript
// var 声明的变量为函数级作用域
function test() {
    var functionVar = 10;
}
```

---

**基本写法：块级作用域**
`{ let <变量> = <值>; }`
```javascript
// let 声明的变量为块级作用域
{
    let blockVar = 10;
}
```

---

## 变量提升

**基本写法：var 提升**
`console.log(<变量>); var <变量> = <值>;`
```javascript
// var 声明的变量会提升值为 undefined
console.log(x);
var x = 10;
```

---

**基本写法：let 暂时性死区**
`console.log(<变量>); let <变量> = <值>;`
```javascript
// let 声明的变量在声明前访问会报错
// console.log(y);
// let y = 10;
```

---

## 常量特性

**基本写法：const 不可重新赋值**
`const <常量> = <值>;`
```javascript
// const 声明的常量不能重新赋值
const MAX = 100;
```

---

**基本写法：const 对象属性可变**
`const <对象> = { }; <对象>.<属性> = <值>;`
```javascript
// const 对象的属性可以修改
const obj = {};
obj.name = "Alice";
```

---

**基本写法：冻结对象**
`Object.freeze(<对象>)`
```javascript
// 冻结对象使其属性不可变
const frozen = Object.freeze({});
```

---

## ES2025 新数据类型

**基本写法：Float16Array 半精度浮点数组**
`new Float16Array([<元素>])`
```javascript
// 创建半精度浮点数组节省内存适合机器学习场景
let arr = new Float16Array([1.0, 2.5, 3.14]);
```

---

**基本写法：Iterator 协议对象**
`<对象>[Symbol.iterator] = function() { return { next: () => ({ value, done }) }; }`
```javascript
// 自定义迭代器协议对象支持 for-of 与扩展运算符
let range = {
    [Symbol.iterator]() {
        let n = 0;
        return {
            next: () => ({ value: n++, done: n > 3 })
        };
    }
};
```



<!-- ============ 文档分隔线：008-javascript/002-ProgramStructureBasicSyntax.md ============ -->

# JavaScript 程序结构与基本语法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 语句与分号

**基本写法：语句结尾分号**
`<语句>;`
```javascript
// 语句以分号结尾
let x = 10;
```

---

**基本写法：无分号语句**
`<语句>`
```javascript
// 语句可省略分号
let x = 10
```

---

## 严格模式

**基本写法：启用严格模式**
`"use strict";`
```javascript
// 在脚本顶部启用严格模式
"use strict";
let x = 10;
```

---

**基本写法：函数级严格模式**
`function <函数名>() { "use strict"; }`
```javascript
// 在函数内部启用严格模式
function safeFunction() {
    "use strict";
}
```

---

## 注释

**基本写法：单行注释**
`// <注释内容>`
```javascript
// 这是一个单行注释
let x = 10;
```

---

**基本写法：多行注释**
`/* <注释内容> */`
```javascript
/* 这是一个多行注释 */
let x = 10;
```

---

**换行写法：多行注释**
`/* <注释内容> */`
```javascript
/*
 * 这是一个多行注释
 * 可以跨越多行
 */
let x = 10;
```

---

**基本写法：文档注释**
`/** <注释内容> */`
```javascript
/** 计算两个数的和 */
function add(a, b) {
    return a + b;
}
```

---

## 输出

**基本写法：控制台输出**
`console.log(<内容>);`
```javascript
// 输出到控制台
console.log("Hello, World!");
```

---

**基本写法：输出多个值**
`console.log(<值1>, <值2>);`
```javascript
// 输出多个值以空格分隔
console.log("Name:", name, "Age:", age);
```

---

**基本写法：错误输出**
`console.error(<内容>);`
```javascript
// 输出错误信息到控制台
console.error("Something went wrong");
```

---

**基本写法：警告输出**
`console.warn(<内容>);`
```javascript
// 输出警告信息到控制台
console.warn("This is a warning");
```

---

## 标识符命名

**基本写法：变量名命名**
`<lowerCamelCase>`
```javascript
// 变量名使用小驼峰命名法
userName
```

---

**基本写法：常量名命名**
`<UPPER_SNAKE_CASE>`
```javascript
// 常量名全大写使用下划线分隔
MAX_VALUE
```

---

**基本写法：函数名命名**
`<lowerCamelCase>`
```javascript
// 函数名使用小驼峰命名法
getUserName
```

---

**基本写法：类名命名**
`<UpperCamelCase>`
```javascript
// 类名使用大驼峰命名法
HelloWorld
```

---

## 输入

**基本写法：浏览器输入**
`prompt("<提示文本>")`
```javascript
// 弹出输入框获取用户输入
let name = prompt("请输入你的名字");
```

---

**基本写法：确认框**
`confirm("<提示文本>")`
```javascript
// 弹出确认框返回布尔值
let result = confirm("确定要删除吗");
```

---

**基本写法：警告框**
`alert("<消息>")`
```javascript
// 弹出警告框显示消息
alert("操作成功");
```

---

## 代码块

**基本写法：块级作用域**
`{ <语句> }`
```javascript
// 使用大括号创建块级作用域
{
    let blockVar = 10;
}
```

---

**基本写法：语句分组**
`{ <语句1> <语句2> }`
```javascript
// 多条语句分组
{
    let x = 1;
    let y = 2;
}
```



<!-- ============ 文档分隔线：008-javascript/003-ObjectArray.md ============ -->

# JavaScript 对象与数组

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 对象创建

**基本写法：对象字面量**
`let <变量> = { <键>: <值> };`
```javascript
// 使用字面量创建对象
let user = { name: "Alice", age: 25 };
```

---

**基本写法：new Object 创建**
`let <变量> = new Object();`
```javascript
// 使用 new Object 创建对象
let user = new Object();
```

---

**基本写法：构造函数创建**
`function <构造函数>(<参数>) { this.<属性> = <参数>; }`
```javascript
// 定义构造函数
function Person(name, age) {
    this.name = name;
    this.age = age;
}
```

---

**基本写法：使用构造函数**
`let <变量> = new <构造函数>(<参数>);`
```javascript
// 通过构造函数创建对象
let p = new Person("Alice", 25);
```

---

**基本写法：Object.create**
`let <变量> = Object.create(<原型>);`
```javascript
// 以指定原型创建对象
let child = Object.create(parent);
```

---

## 对象属性

**基本写法：点访问属性**
`<对象>.<属性>`
```javascript
// 使用点号访问属性
let name = user.name;
```

---

**基本写法：方括号访问属性**
`<对象>["<属性>"]`
```javascript
// 使用方括号访问属性
let name = user["name"];
```

---

**基本写法：设置属性**
`<对象>.<属性> = <值>;`
```javascript
// 设置对象属性值
user.age = 26;
```

---

**基本写法：删除属性**
`delete <对象>.<属性>`
```javascript
// 删除对象属性
delete user.age;
```

---

**基本写法：检查属性存在**
`"<属性>" in <对象>`
```javascript
// 检查属性是否存在于对象中
let has = "name" in user;
```

---

**基本写法：hasOwnProperty**
`<对象>.hasOwnProperty("<属性>")`
```javascript
// 检查对象自身是否包含属性
let has = user.hasOwnProperty("name");
```

---

## 对象方法

**基本写法：方法简写**
`let <对象> = { <方法名>() { } };`
```javascript
// 对象方法简写
let user = {
    greet() {
    }
};
```

---

**基本写法：计算属性名**
`let <对象> = { [<表达式>]: <值> };`
```javascript
// 使用表达式作为属性名
let key = "dynamic";
let obj = { [key]: "value" };
```

---

## 对象遍历

**基本写法：for-in 遍历**
`for (let <键> in <对象>) { }`
```javascript
// 遍历对象的可枚举属性
for (let key in user) {
}
```

---

**基本写法：Object.keys**
`Object.keys(<对象>)`
```javascript
// 获取对象所有键的数组
let keys = Object.keys(user);
```

---

**基本写法：Object.values**
`Object.values(<对象>)`
```javascript
// 获取对象所有值的数组
let values = Object.values(user);
```

---

**基本写法：Object.entries**
`Object.entries(<对象>)`
```javascript
// 获取对象键值对数组
let entries = Object.entries(user);
```

---

## 对象操作

**基本写法：Object.assign**
`Object.assign(<目标>, <源对象>)`
```javascript
// 合并对象到目标对象
Object.assign(target, source);
```

---

**基本写法：展开运算符合并**
`let <结果> = { ...<对象1>, ...<对象2> };`
```javascript
// 使用展开运算符合并对象
let merged = { ...obj1, ...obj2 };
```

---

**基本写法：对象解构**
`let { <属性1>, <属性2> } = <对象>;`
```javascript
// 解构对象属性到变量
let { name, age } = user;
```

---

**基本写法：重命名解构**
`let { <属性>: <新名> } = <对象>;`
```javascript
// 解构时重命名变量
let { name: userName } = user;
```

---

**基本写法：默认值解构**
`let { <属性> = <默认值> } = <对象>;`
```javascript
// 解构时设置默认值
let { name = "Unknown" } = user;
```

---

**基本写法：嵌套解构**
`let { <对象>: { <属性> } } = <对象>;`
```javascript
// 解构嵌套对象
let { address: { city } } = user;
```

---

## 对象保护

**基本写法：Object.freeze**
`Object.freeze(<对象>)`
```javascript
// 冻结对象不可修改
Object.freeze(user);
```

---

**基本写法：Object.seal**
`Object.seal(<对象>)`
```javascript
// 密封对象不可增删属性
Object.seal(user);
```

---

**基本写法：Object.preventExtensions**
`Object.preventExtensions(<对象>)`
```javascript
// 阻止对象扩展
Object.preventExtensions(user);
```

---

## 数组创建

**基本写法：数组字面量**
`let <变量> = [ <元素1>, <元素2> ];`
```javascript
// 使用字面量创建数组
let numbers = [1, 2, 3];
```

---

**基本写法：new Array 创建**
`let <变量> = new Array(<长度>);`
```javascript
// 创建指定长度的空数组
let arr = new Array(5);
```

---

**基本写法：Array.of**
`Array.of(<元素1>, <元素2>)`
```javascript
// 创建包含指定元素的数组
let arr = Array.of(1, 2, 3);
```

---

**基本写法：Array.from**
`Array.from(<可迭代对象>)`
```javascript
// 从可迭代对象创建数组
let arr = Array.from("hello");
```

---

## 数组访问

**基本写法：索引访问**
`<数组>[<索引>]`
```javascript
// 通过索引获取元素
let first = numbers[0];
```

---

**基本写法：修改元素**
`<数组>[<索引>] = <值>;`
```javascript
// 修改指定索引的元素
numbers[0] = 100;
```

---

**基本写法：获取长度**
`<数组>.length`
```javascript
// 获取数组长度
let len = numbers.length;
```

---

## 数组方法

**基本写法：push 添加末尾**
`<数组>.push(<元素>)`
```javascript
// 向数组末尾添加元素
numbers.push(4);
```

---

**基本写法：pop 删除末尾**
`<数组>.pop()`
```javascript
// 删除并返回数组末尾元素
let last = numbers.pop();
```

---

**基本写法：unshift 添加头部**
`<数组>.unshift(<元素>)`
```javascript
// 向数组头部添加元素
numbers.unshift(0);
```

---

**基本写法：shift 删除头部**
`<数组>.shift()`
```javascript
// 删除并返回数组头部元素
let first = numbers.shift();
```

---

**基本写法：splice 删除**
`<数组>.splice(<起始>, <数量>)`
```javascript
// 删除指定位置的元素
numbers.splice(1, 2);
```

---

**基本写法：splice 插入**
`<数组>.splice(<位置>, 0, <元素>)`
```javascript
// 在指定位置插入元素
numbers.splice(1, 0, "new");
```

---

**基本写法：slice 截取**
`<数组>.slice(<起始>, <结束>)`
```javascript
// 截取数组指定范围返回新数组
let part = numbers.slice(1, 3);
```

---

**基本写法：concat 合并**
`<数组>.concat(<其他数组>)`
```javascript
// 合并多个数组
let combined = arr1.concat(arr2);
```

---

**基本写法：indexOf 查找**
`<数组>.indexOf(<元素>)`
```javascript
// 查找元素首次出现的索引
let index = numbers.indexOf(3);
```

---

**基本写法：includes 包含**
`<数组>.includes(<元素>)`
```javascript
// 判断数组是否包含元素
let has = numbers.includes(3);
```

---

**基本写法：join 转字符串**
`<数组>.join("<分隔符>")`
```javascript
// 将数组元素连接为字符串
let str = numbers.join(",");
```

---

**基本写法：reverse 反转**
`<数组>.reverse()`
```javascript
// 反转数组元素顺序
numbers.reverse();
```

---

**基本写法：sort 排序**
`<数组>.sort()`
```javascript
// 对数组进行排序
numbers.sort();
```

---

**基本写法：自定义排序**
`<数组>.sort(<比较函数>)`
```javascript
// 使用比较函数排序
numbers.sort((a, b) => a - b);
```

---

## 数组遍历

**基本写法：for 循环遍历**
`for (let i = 0; i < <数组>.length; i++) { }`
```javascript
// 使用索引遍历数组
for (let i = 0; i < numbers.length; i++) {
}
```

---

**基本写法：for-of 遍历**
`for (let <元素> of <数组>) { }`
```javascript
// 遍历数组元素
for (let num of numbers) {
}
```

---

**基本写法：forEach 遍历**
`<数组>.forEach(<回调函数>)`
```javascript
// 使用 forEach 遍历数组
numbers.forEach((num) => {
});
```

---

## 数组解构

**基本写法：数组解构**
`let [ <变量1>, <变量2> ] = <数组>;`
```javascript
// 解构数组元素到变量
let [first, second] = numbers;
```

---

**基本写法：跳过元素**
`let [, <变量2>] = <数组>;`
```javascript
// 解构时跳过某些元素
let [, second] = numbers;
```

---

**基本写法：剩余元素**
`let [ <变量1>, ...<剩余> ] = <数组>;`
```javascript
// 解构剩余元素到数组
let [first, ...rest] = numbers;
```

---

**基本写法：默认值解构**
`let [ <变量> = <默认值> ] = <数组>;`
```javascript
// 解构时设置默认值
let [a = 0, b = 0] = numbers;
```

---

## 二维数组

**基本写法：创建二维数组**
`let <数组> = [[<元素>], [<元素>]];`
```javascript
// 创建二维数组
let matrix = [[1, 2], [3, 4]];
```

---

**基本写法：访问二维数组**
`<数组>[<行>][<列>]`
```javascript
// 获取二维数组元素
let element = matrix[0][1];
```

---

**基本写法：遍历二维数组**
`for (let i = 0; i < <数组>.length; i++) { for (let j = 0; j < <数组>[i].length; j++) { } }`
```javascript
// 嵌套循环遍历二维数组
for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
    }
}
```

---

## ES2024+ 对象数组新方法

**基本写法：Object.groupBy 分组**
`Object.groupBy(<数组>, <回调函数>)`
```javascript
// 按回调返回的键对数组分组返回普通对象
let grouped = Object.groupBy([1, 2, 3, 4], n => n % 2 === 0 ? "even" : "odd");
```

---

**基本写法：Map.groupBy 分组**
`Map.groupBy(<数组>, <回调函数>)`
```javascript
// 返回 Map 实例键可以是任意类型不只是字符串
let grouped = Map.groupBy(users, u => u.role);
```

---

**基本写法：Object.hasOwn 检查自身属性**
`Object.hasOwn(<对象>, "<属性>")`
```javascript
// ES2022 新增替代 hasOwnProperty 更安全不会被原型链覆盖
let has = Object.hasOwn(user, "name");
```

---

**基本写法：structuredClone 深拷贝**
`structuredClone(<对象>)`
```javascript
// 结构化克隆算法深拷贝支持循环引用与 Date 等内置类型
let copy = structuredClone(original);
```



<!-- ============ 文档分隔线：008-javascript/004-FunctionScopeClosure.md ============ -->

# JavaScript 函数-作用域与闭包

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 函数声明

**基本写法：函数声明**
`function <函数名>(<参数>) { }`
```javascript
// 声明一个函数
function greet(name) {
}
```

---

**基本写法：函数表达式**
`let <变量> = function(<参数>) { };`
```javascript
// 将函数赋值给变量
let greet = function(name) {
};
```

---

**基本写法：具名函数表达式**
`let <变量> = function <函数名>(<参数>) { };`
```javascript
// 函数表达式带名称用于内部递归
let factorial = function compute(n) {
};
```

---

## 箭头函数

**基本写法：箭头函数单参数**
`<参数> => <表达式>`
```javascript
// 单参数箭头函数直接返回
let square = x => x * x;
```

---

**基本写法：箭头函数多参数**
`(<参数1>, <参数2>) => <表达式>`
```javascript
// 多参数箭头函数直接返回
let add = (a, b) => a + b;
```

---

**基本写法：箭头函数带函数体**
`(<参数>) => { <语句> }`
```javascript
// 箭头函数带函数体需要 return
let greet = (name) => {
    return "Hello, " + name;
};
```

---

**基本写法：无参数箭头函数**
`() => <表达式>`
```javascript
// 无参数箭头函数
let getRandom = () => Math.random();
```

---

**基本写法：箭头函数返回对象**
`(<参数>) => ({ <属性>: <值> })`
```javascript
// 箭头函数直接返回对象字面量
let createUser = (name) => ({ name: name, age: 0 });
```

---

## 参数处理

**基本写法：默认参数**
`function <函数名>(<参数> = <默认值>) { }`
```javascript
// 参数默认值
function greet(name = "Guest") {
}
```

---

**基本写法：剩余参数**
`function <函数名>(...<参数名>) { }`
```javascript
// 收集剩余参数为数组
function sum(...numbers) {
}
```

---

**基本写法：arguments 对象**
`arguments[<索引>]`
```javascript
// 访问函数的所有参数
function logArgs() {
    console.log(arguments[0]);
}
```

---

## 函数调用

**基本写法：普通调用**
`<函数名>(<参数>)`
```javascript
// 直接调用函数
greet("Alice");
```

---

**基本写法：call 调用**
`<函数>.call(<this对象>, <参数1>, <参数2>)`
```javascript
// 指定 this 和参数调用函数
greet.call(obj, "Alice");
```

---

**基本写法：apply 调用**
`<函数>.apply(<this对象>, [<参数数组>])`
```javascript
// 指定 this 和参数数组调用函数
greet.apply(obj, ["Alice"]);
```

---

**基本写法：bind 绑定**
`<函数>.bind(<this对象>)`
```javascript
// 创建绑定了 this 的新函数
let boundGreet = greet.bind(obj);
```

---

## 作用域

**基本写法：全局作用域**
`let <变量> = <值>;`
```javascript
// 在全局声明的变量
let globalVar = 10;
```

---

**基本写法：函数作用域**
`function <函数>() { var <变量> = <值>; }`
```javascript
// var 声明的变量为函数级作用域
function test() {
    var functionVar = 10;
}
```

---

**基本写法：块级作用域**
`{ let <变量> = <值>; }`
```javascript
// let 声明的变量为块级作用域
{
    let blockVar = 10;
}
```

---

## 闭包

**基本写法：闭包基本结构**
`function <外部函数>() { let <变量>; return function() { }; }`
```javascript
// 内部函数访问外部函数的变量
function createCounter() {
    let count = 0;
    return function() {
        count++;
    };
}
```

---

**基本写法：使用闭包**
`let <变量> = <外部函数>();`
```javascript
// 创建闭包并使用
let counter = createCounter();
counter();
```

---

**基本写法：闭包工厂**
`function <工厂>(<配置>) { return function(<参数>) { }; }`
```javascript
// 闭包实现工厂函数
function createMultiplier(factor) {
    return function(number) {
        return number * factor;
    };
}
```

---

**基本写法：模块模式**
`const <模块> = (function() { let <私有变量>; return { <方法> }; })();`
```javascript
// 闭包实现模块模式
const counter = (function() {
    let count = 0;
    return {
        increment: function() { count++; }
    };
})();
```

---

## 递归

**基本写法：递归结构**
`function <函数名>(<参数>) { if (<基准条件>) return <基准值>; return <函数名>(<修改参数>); }`
```javascript
// 递归函数基本结构
function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
```

---

**基本写法：斐波那契递归**
`function fibonacci(<参数>)`
```javascript
// 斐波那契数列递归实现
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

---

## 高阶函数

**基本写法：函数作为参数**
`function <函数>(<回调函数>) { <回调函数>(); }`
```javascript
// 接受函数作为参数
function execute(callback) {
    callback();
}
```

---

**基本写法：函数作为返回值**
`function <函数>() { return function() { }; }`
```javascript
// 返回函数作为结果
function getHandler() {
    return function() {
    };
}
```

---

## 立即执行函数

**基本写法：IIFE**
`(function() { })();`
```javascript
// 立即执行函数表达式
(function() {
})();
```

---

**基本写法：带参数 IIFE**
`(function(<参数>) { })(<值>);`
```javascript
// 带参数的立即执行函数
(function(name) {
})( "Alice");
```

---

**基本写法：箭头函数 IIFE**
`(() => { })();`
```javascript
// 箭头函数立即执行
(() => {
})();
```

---

## this 关键字

**基本写法：方法中的 this**
`<对象>.<方法> = function() { this.<属性>; }`
```javascript
// 方法中 this 指向调用对象
let obj = {
    name: "Alice",
    getName: function() {
        return this.name;
    }
};
```

---

**基本写法：箭头函数中的 this**
`<对象>.<方法> = () => { }`
```javascript
// 箭头函数继承外层 this
let obj = {
    name: "Alice",
    getName: () => {
    }
};
```

---

## 函数属性

**基本写法：函数 length**
`<函数>.length`
```javascript
// 获取函数形参个数
let paramCount = greet.length;
```

---

**基本写法：函数 name**
`<函数>.name`
```javascript
// 获取函数名称
let funcName = greet.name;
```

---

## 生成器函数

**基本写法：生成器函数声明**
`function* <函数名>() { yield <值>; }`
```javascript
// 声明生成器函数
function* generator() {
    yield 1;
    yield 2;
}
```

---

**基本写法：使用生成器**
`let <迭代器> = <生成器函数>();`
```javascript
// 创建生成器迭代器
let gen = generator();
gen.next();
```



<!-- ============ 文档分隔线：008-javascript/005-ControlFlow.md ============ -->

# JavaScript 控制流

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## if-else 语句

**基本写法：if 语句**
`if (<条件>) { }`
```javascript
// 条件为真时执行
if (score >= 90) {
}
```

---

**基本写法：if-else 语句**
`if (<条件>) { } else { }`
```javascript
// 条件为真执行 if 块否则执行 else 块
if (score >= 60) {
} else {
}
```

---

**换行写法：if-else if-else 链**
`if (<条件>) { } else if (<条件>) { } else { }`
```javascript
// 多条件分支判断
if (score >= 90) {
} else if (score >= 80) {
} else if (score >= 60) {
} else {
}
```

---

**基本写法：嵌套 if**
`if (<条件>) { if (<条件>) { } else { } }`
```javascript
// if 语句内部嵌套 if
if (score >= 90) {
    if (score >= 95) {
    } else {
    }
}
```

---

**基本写法：卫语句提前返回**
`if (<条件>) { return; }`
```javascript
// 条件不满足时提前返回
if (order == null) {
    return;
}
```

---

## switch 语句

**基本写法：传统 switch**
`switch (<表达式>) { case <值>: break; default: }`
```javascript
// 传统 switch 多分支
switch (day) {
    case 1:
        break;
    case 2:
        break;
    default:
}
```

---

**基本写法：switch case 穿透**
`case <值1>: case <值2>: <语句>; break;`
```javascript
// 多个 case 共享同一处理
switch (day) {
    case 1:
    case 2:
    case 3:
        console.log("Weekday");
        break;
    default:
}
```

---

## for 循环

**基本写法：标准 for 循环**
`for (<初始化>; <条件>; <更新>) { }`
```javascript
// 已知次数的循环
for (let i = 0; i < 10; i++) {
}
```

---

**基本写法：for-in 遍历对象**
`for (let <键> in <对象>) { }`
```javascript
// 遍历对象的可枚举属性
for (let key in obj) {
}
```

---

**基本写法：for-of 遍历可迭代对象**
`for (let <元素> of <可迭代对象>) { }`
```javascript
// 遍历数组元素
for (let item of array) {
}
```

---

**基本写法：for-of 带索引**
`for (let [<索引>, <元素>] of <数组>.entries()) { }`
```javascript
// 遍历数组同时获取索引和元素
for (let [index, item] of array.entries()) {
}
```

---

## while 循环

**基本写法：while 循环**
`while (<条件>) { }`
```javascript
// 先判断后执行
let i = 0;
while (i < 10) {
    i++;
}
```

---

## do-while 循环

**基本写法：do-while 循环**
`do { } while (<条件>);`
```javascript
// 先执行后判断至少执行一次
let i = 0;
do {
    i++;
} while (i < 10);
```

---

## 循环控制

**基本写法：break 语句**
`break;`
```javascript
// 跳出当前循环
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        break;
    }
}
```

---

**基本写法：带标签的 break**
`<标签>: for (...) { break <标签>; }`
```javascript
// 跳出多层循环
outerLoop: for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
        if (i * j > 6) {
            break outerLoop;
        }
    }
}
```

---

**基本写法：continue 语句**
`continue;`
```javascript
// 跳过当前迭代
for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) {
        continue;
    }
}
```

---

**基本写法：带标签的 continue**
`<标签>: for (...) { continue <标签>; }`
```javascript
// 跳过外层循环的当前迭代
outer: for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        if (j === 1) {
            continue outer;
        }
    }
}
```

---

## 异常处理

**基本写法：try-catch**
`try { } catch (<错误>) { }`
```javascript
// 捕获异常
try {
    JSON.parse(invalidJson);
} catch (error) {
}
```

---

**基本写法：try-catch-finally**
`try { } catch (<错误>) { } finally { }`
```javascript
// finally 块无论是否异常都执行
try {
} catch (error) {
} finally {
}
```

---

**基本写法：throw 抛出错误**
`throw new Error("<消息>");`
```javascript
// 手动抛出错误
throw new Error("Invalid input");
```

---

**基本写法：throw 抛出对象**
`throw { <属性>: <值> };`
```javascript
// 抛出自定义错误对象
throw { code: 400, message: "Bad Request" };
```

---

## return 语句

**基本写法：返回值**
`return <值>;`
```javascript
// 返回计算结果
function add(a, b) {
    return a + b;
}
```

---

**基本写法：无返回值**
`return;`
```javascript
// 提前结束函数
function validate(value) {
    if (value < 0) {
        return;
    }
}
```



<!-- ============ 文档分隔线：008-javascript/006-JavaScriptModular.md ============ -->

# JavaScript 模块化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## export 导出

**基本写法：命名导出变量**
`export let <变量名> = <值>;`
```javascript
// 导出变量
export let name = "Alice";
```

---

**基本写法：命名导出函数**
`export function <函数名>() { }`
```javascript
// 导出函数
export function greet() {
}
```

---

**基本写法：命名导出类**
`export class <类名> { }`
```javascript
// 导出类
export class Person {
}
```

---

**基本写法：命名导出常量**
`export const <常量名> = <值>;`
```javascript
// 导出常量
export const PI = 3.14159;
```

---

**基本写法：统一导出**
`export { <标识符1>, <标识符2> };`
```javascript
// 统一导出多个标识符
export { name, greet, Person };
```

---

**基本写法：导出时重命名**
`export { <原名> as <新名> };`
```javascript
// 导出时重命名标识符
export { greet as sayHello };
```

---

**基本写法：默认导出**
`export default <表达式>`
```javascript
// 默认导出
export default function() {
}
```

---

**基本写法：默认导出命名函数**
`export default function <函数名>() { }`
```javascript
// 默认导出命名函数
export default function main() {
}
```

---

**基本写法：默认导出类**
`export default class <类名> { }`
```javascript
// 默认导出类
export default class App {
}
```

---

**基本写法：默认导出对象**
`export default { <属性> };`
```javascript
// 默认导出对象
export default {
    name: "Alice",
    age: 25
};
```

---

## import 导入

**基本写法：导入命名导出**
`import { <标识符> } from "<模块>";`
```javascript
// 导入指定的命名导出
import { name } from "./module.js";
```

---

**单行写法：导入多个命名导出**
`import { <标识符1>, <标识符2> } from "<模块>";`
```javascript
// 单行导入多个命名导出
import { name, greet, Person } from "./module.js";
```

---

**换行写法：导入多个命名导出**
`import { <标识符1>, <标识符2>, <标识符3> } from "<模块>";`
```javascript
// 换行导入多个命名导出
import {
    name,
    greet,
    Person
} from "./module.js";
```

---

**基本写法：导入时重命名**
`import { <原名> as <新名> } from "<模块>";`
```javascript
// 导入时重命名标识符
import { greet as sayHello } from "./module.js";
```

---

**基本写法：导入默认导出**
`import <名称> from "<模块>";`
```javascript
// 导入默认导出
import main from "./module.js";
```

---

**基本写法：混合导入**
`import <默认>, { <命名1>, <命名2> } from "<模块>";`
```javascript
// 同时导入默认导出和命名导出
import main, { name, greet } from "./module.js";
```

---

**基本写法：命名空间导入**
`import * as <命名空间> from "<模块>";`
```javascript
// 导入整个模块作为命名空间
import * as utils from "./module.js";
```

---

**基本写法：使用命名空间**
`<命名空间>.<标识符>`
```javascript
// 通过命名空间访问导出
utils.greet();
```

---

**基本写法：副作用导入**
`import "<模块>";`
```javascript
// 仅执行模块不导入内容
import "./polyfill.js";
```

---

**基本写法：动态导入**
`import("<模块>")`
```javascript
// 动态导入返回 Promise
import("./module.js").then(module => {
});
```

---

**基本写法：await 动态导入**
`const <模块> = await import("<模块>");`
```javascript
// 使用 await 等待动态导入
const module = await import("./module.js");
```

---

## re-export 重新导出

**基本写法：重新导出**
`export { <标识符> } from "<模块>";`
```javascript
// 从其他模块重新导出
export { name } from "./module.js";
```

---

**基本写法：重新导出全部**
`export * from "<模块>";`
```javascript
// 重新导出模块全部内容
export * from "./module.js";
```

---

**基本写法：重新导出默认**
`export { default } from "<模块>";`
```javascript
// 重新导出默认导出
export { default } from "./module.js";
```

---

**基本写法：重新导出并重命名**
`export { <原名> as <新名> } from "<模块>";`
```javascript
// 重新导出并重命名
export { greet as sayHello } from "./module.js";
```

---

## 模块模式

**基本写法：模块文件结构**
`// <导出> <导入>`
```javascript
// 模块文件包含导入和导出
import { helper } from "./helper.js";
export function main() {
}
```

---

**基本写法：具名导入与默认导入**
`import <默认>, * as <命名空间> from "<模块>";`
```javascript
// 同时导入默认和命名空间
import main, * as utils from "./module.js";
```

---

## CommonJS 模块

**基本写法：module.exports**
`module.exports = <值>;`
```javascript
// CommonJS 导出模块
module.exports = {
    name: "Alice"
};
```

---

**基本写法：exports 属性**
`exports.<属性> = <值>;`
```javascript
// CommonJS 导出属性
exports.greet = function() {
};
```

---

**基本写法：require 导入**
`const <模块> = require("<模块>");`
```javascript
// CommonJS 导入模块
const fs = require("fs");
```

---

**基本写法：require 解构导入**
`const { <属性> } = require("<模块>");`
```javascript
// CommonJS 解构导入
const { readFile } = require("fs");
```

---

## 模块路径

**基本写法：相对路径**
`import <模块> from "./<文件>";`
```javascript
// 使用相对路径导入
import { helper } from "./utils.js";
```

---

**基本写法：上级目录**
`import <模块> from "../<文件>";`
```javascript
// 使用上级目录路径
import { config } from "../config.js";
```

---

**基本写法：包名导入**
`import <模块> from "<包名>";`
```javascript
// 导入 npm 包
import React from "react";
```

---

**基本写法：子路径导入**
`import <模块> from "<包名>/<子路径>";`
```javascript
// 导入包的子路径
import { button } from "react-bootstrap";
```

---

## ES2025 Import Attributes

**基本写法：import json 模块**
`import <内容> from "<模块>" with { type: "json" }`
```javascript
// 使用 import attributes 显式声明模块类型
import config from "./config.json" with { type: "json" };
```

---

**基本写法：动态 import 断言**
`import("<模块>", { with: { type: "json" } })`
```javascript
// 动态导入时使用 with 选项声明模块类型
let mod = await import("./config.json", { with: { type: "json" } });
```

---

**基本写法：import attributes 与 import assertions 区别**
`// assert 已废弃改用 with 关键字`
```javascript
// 旧写法 import assertions 使用 assert 已废弃
// import x from "./a.json" assert { type: "json" };
// 新写法 import attributes 使用 with 关键字
import x from "./a.json" with { type: "json" };
```



<!-- ============ 文档分隔线：008-javascript/007-CoroutinesInJavaScript.md ============ -->

# JavaScript 生成器函数

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 生成器函数声明

**基本写法：生成器函数声明**
`function* <函数名>() { }`
```javascript
// 声明生成器函数
function* generator() {
}
```

---

**基本写法：生成器函数表达式**
`let <变量> = function*() { };`
```javascript
// 生成器函数表达式
let gen = function*() {
};
```

---

**基本写法：对象方法生成器**
`let <对象> = { *<方法名>() { } };`
```javascript
// 对象中的生成器方法
let obj = {
    *generator() {
    }
};
```

---

**基本写法：类方法生成器**
`class <类> { *<方法名>() { } }`
```javascript
// 类中的生成器方法
class Range {
    *iterator() {
    }
}
```

---

## yield 表达式

**基本写法：yield 单个值**
`yield <值>;`
```javascript
// 产出单个值
function* gen() {
    yield 1;
    yield 2;
}
```

---

**基本写法：yield 多个值**
`yield <值1>; yield <值2>;`
```javascript
// 产出多个值
function* gen() {
    yield "a";
    yield "b";
    yield "c";
}
```

---

**基本写法：yield 表达式**
`yield <表达式>;`
```javascript
// yield 表达式结果
function* gen() {
    yield 1 + 2;
}
```

---

**基本写法：yield 变量**
`yield <变量>;`
```javascript
// yield 变量值
function* gen() {
    let value = getValue();
    yield value;
}
```

---

## 生成器迭代

**基本写法：创建迭代器**
`let <迭代器> = <生成器函数>();`
```javascript
// 调用生成器函数创建迭代器
let it = generator();
```

---

**基本写法：next 方法**
`<迭代器>.next()`
```javascript
// 获取下一个 yield 的值
let result = it.next();
```

---

**基本写法：next 返回值**
`<迭代器>.next().value`
```javascript
// 获取 yield 产出的值
let value = it.next().value;
```

---

**基本写法：next done 检查**
`<迭代器>.next().done`
```javascript
// 检查迭代是否完成
let done = it.next().done;
```

---

**基本写法：for-of 遍历生成器**
`for (let <值> of <生成器>()) { }`
```javascript
// 使用 for-of 遍历生成器
for (let value of generator()) {
}
```

---

## yield 委托

**基本写法：yield 委托**
`yield* <可迭代对象>;`
```javascript
// 委托给另一个可迭代对象
function* gen() {
    yield* [1, 2, 3];
}
```

---

**基本写法：委托给另一个生成器**
`yield* <生成器函数>();`
```javascript
// 委托给另一个生成器函数
function* inner() {
    yield 1;
    yield 2;
}
function* outer() {
    yield* inner();
    yield 3;
}
```

---

**基本写法：委托返回值**
`let <结果> = yield* <生成器>();`
```javascript
// 获取委托生成器的返回值
function* inner() {
    yield 1;
    return "done";
}
function* outer() {
    let result = yield* inner();
}
```

---

## 生成器传值

**基本写法：next 传值**
`<迭代器>.next(<值>)`
```javascript
// 向生成器内部传递值
function* gen() {
    let input = yield;
}
let it = gen();
it.next();
it.next(42);
```

---

**基本写法：yield 接收值**
`let <变量> = yield <值>;`
```javascript
// yield 表达式接收外部传入的值
function* gen() {
    let received = yield "first";
}
```

---

## return 语句

**基本写法：生成器 return**
`return <值>;`
```javascript
// 生成器中 return 终止迭代
function* gen() {
    yield 1;
    return "finished";
    yield 2;
}
```

---

**基本写法：return 方法**
`<迭代器>.return(<值>)`
```javascript
// 提前终止生成器
let it = gen();
it.return("terminated");
```

---

## throw 方法

**基本写法：throw 注入错误**
`<迭代器>.throw(new Error("<消息>"))`
```javascript
// 向生成器内部抛出错误
let it = gen();
it.next();
it.throw(new Error("Error"));
```

---

**基本写法：生成器捕获错误**
`try { yield <值>; } catch (<错误>) { }`
```javascript
// 生成器内部捕获 throw 注入的错误
function* gen() {
    try {
        yield 1;
    } catch (error) {
    }
}
```

---

## 无限生成器

**基本写法：无限序列**
`while (true) { yield <值>; }`
```javascript
// 生成无限序列
function* counter() {
    let i = 0;
    while (true) {
        yield i++;
    }
}
```

---

**基本写法：斐波那契生成器**
`function* <函数>() { while (true) { yield <值>; } }`
```javascript
// 生成斐波那契数列
function* fibonacci() {
    let [a, b] = [0, 1];
    while (true) {
        yield a;
        [a, b] = [b, a + b];
    }
}
```

---

## 生成器应用

**基本写法：ID 生成器**
`function* <函数>() { let <变量> = <初始值>; while (true) { yield <变量>++; } }`
```javascript
// 生成唯一 ID
function* idGenerator() {
    let id = 1;
    while (true) {
        yield id++;
    }
}
```

---

**基本写法：状态机**
`function* <函数>() { while (true) { yield <状态1>; yield <状态2>; } }`
```javascript
// 生成器实现状态机
function* stateMachine() {
    while (true) {
        yield "ON";
        yield "OFF";
    }
}
```

---

**基本写法：惰性计算**
`function* <函数>(<数组>) { for (let <项> of <数组>) { yield <处理>(<项>); } }`
```javascript
// 惰性处理数据
function* process(items) {
    for (let item of items) {
        yield transform(item);
    }
}
```

---

## 异步生成器

**基本写法：异步生成器函数**
`async function* <函数名>() { }`
```javascript
// 声明异步生成器函数
async function* asyncGen() {
}
```

---

**基本写法：yield 异步值**
`yield await <Promise>;`
```javascript
// 异步生成器产出 Promise 结果
async function* fetchItems() {
    let data = await fetch("url");
    yield data;
}
```

---

**基本写法：for-await-of 遍历**
`for await (let <值> of <异步生成器>) { }`
```javascript
// 使用 for-await-of 遍历异步生成器
for await (let item of asyncGen()) {
}
```

---

**基本写法：异步生成器 next**
`await <异步迭代器>.next()`
```javascript
// 等待异步生成器下一个值
let it = asyncGen();
let result = await it.next();
```



<!-- ============ 文档分隔线：008-javascript/008-DataTypeOperator.md ============ -->

# JavaScript 数据类型与运算符

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 算术运算符

**基本写法：加法运算**
`<操作数1> + <操作数2>`
```javascript
// 两个数字相加
let sum = 10 + 3;
```

---

**基本写法：减法运算**
`<操作数1> - <操作数2>`
```javascript
// 两个数字相减
let diff = 10 - 3;
```

---

**基本写法：乘法运算**
`<操作数1> * <操作数2>`
```javascript
// 两个数字相乘
let product = 10 * 3;
```

---

**基本写法：除法运算**
`<操作数1> / <操作数2>`
```javascript
// 两个数字相除
let quotient = 10 / 3;
```

---

**基本写法：取模运算**
`<操作数1> % <操作数2>`
```javascript
// 取余数
let remainder = 10 % 3;
```

---

**基本写法：幂运算**
`<底数> ** <指数>`
```javascript
// 计算幂
let power = 2 ** 10;
```

---

## 自增自减

**基本写法：后置自增**
`<变量>++`
```javascript
// 先使用后加 1
let a = 5;
let b = a++;
```

---

**基本写法：前置自增**
`++<变量>`
```javascript
// 先加 1 后使用
let a = 5;
let b = ++a;
```

---

**基本写法：后置自减**
`<变量>--`
```javascript
// 先使用后减 1
let a = 5;
let b = a--;
```

---

**基本写法：前置自减**
`--<变量>`
```javascript
// 先减 1 后使用
let a = 5;
let b = --a;
```

---

## 赋值运算符

**基本写法：简单赋值**
`<变量> = <值>`
```javascript
// 给变量赋值
let a = 10;
```

---

**基本写法：加法复合赋值**
`<变量> += <值>`
```javascript
// 等价于 a = a + 5
let a = 10;
a += 5;
```

---

**基本写法：减法复合赋值**
`<变量> -= <值>`
```javascript
// 等价于 a = a - 3
let a = 10;
a -= 3;
```

---

**基本写法：乘法复合赋值**
`<变量> *= <值>`
```javascript
// 等价于 a = a * 2
let a = 10;
a *= 2;
```

---

**基本写法：除法复合赋值**
`<变量> /= <值>`
```javascript
// 等价于 a = a / 4
let a = 10;
a /= 4;
```

---

**基本写法：取模复合赋值**
`<变量> %= <值>`
```javascript
// 等价于 a = a % 3
let a = 10;
a %= 3;
```

---

**基本写法：幂运算复合赋值**
`<变量> **= <值>`
```javascript
// 等价于 a = a ** 2
let a = 10;
a **= 2;
```

---

## 比较运算符

**基本写法：抽象等于**
`<操作数1> == <操作数2>`
```javascript
// 比较值不比较类型会类型转换
let result = (10 == "10");
```

---

**基本写法：抽象不等于**
`<操作数1> != <操作数2>`
```javascript
// 比较值不比较类型
let result = (10 != "10");
```

---

**基本写法：严格等于**
`<操作数1> === <操作数2>`
```javascript
// 比较值和类型都不转换
let result = (10 === 10);
```

---

**基本写法：严格不等于**
`<操作数1> !== <操作数2>`
```javascript
// 比较值和类型是否不全等
let result = (10 !== "10");
```

---

**基本写法：大于比较**
`<操作数1> > <操作数2>`
```javascript
// 比较左边是否大于右边
let result = (10 > 3);
```

---

**基本写法：小于比较**
`<操作数1> < <操作数2>`
```javascript
// 比较左边是否小于右边
let result = (10 < 3);
```

---

**基本写法：大于等于比较**
`<操作数1> >= <操作数2>`
```javascript
// 比较左边是否大于等于右边
let result = (10 >= 3);
```

---

**基本写法：小于等于比较**
`<操作数1> <= <操作数2>`
```javascript
// 比较左边是否小于等于右边
let result = (10 <= 3);
```

---

## 逻辑运算符

**基本写法：逻辑与**
`<布尔表达式1> && <布尔表达式2>`
```javascript
// 两个条件都为真才为真
let result = (x > 0) && (x < 100);
```

---

**基本写法：逻辑或**
`<布尔表达式1> || <布尔表达式2>`
```javascript
// 任一条件为真即为真
let result = (x < 0) || (x > 100);
```

---

**基本写法：逻辑非**
`!<布尔表达式>`
```javascript
// 对布尔值取反
let result = !flag;
```

---

**基本写法：空值合并运算符**
`<值1> ?? <值2>`
```javascript
// 左侧为 null 或 undefined 时返回右侧
let value = a ?? b;
```

---

**基本写法：可选链操作符**
`<对象>?.<属性>`
```javascript
// 安全访问嵌套属性
let name = user?.name;
```

---

## 位运算符

**基本写法：按位与**
`<操作数1> & <操作数2>`
```javascript
// 二进制位与运算
let result = 6 & 3;
```

---

**基本写法：按位或**
`<操作数1> | <操作数2>`
```javascript
// 二进制位或运算
let result = 6 | 3;
```

---

**基本写法：按位异或**
`<操作数1> ^ <操作数2>`
```javascript
// 二进制位异或运算
let result = 6 ^ 3;
```

---

**基本写法：按位取反**
`~<操作数>`
```javascript
// 二进制位取反
let result = ~6;
```

---

**基本写法：左移**
`<操作数> << <位数>`
```javascript
// 二进制位左移
let result = 6 << 1;
```

---

**基本写法：右移**
`<操作数> >> <位数>`
```javascript
// 有符号右移
let result = 6 >> 1;
```

---

**基本写法：无符号右移**
`<操作数> >>> <位数>`
```javascript
// 无符号右移高位补 0
let result = -6 >>> 1;
```

---

## 字符串运算符

**基本写法：字符串拼接**
`<字符串1> + <字符串2>`
```javascript
// 拼接两个字符串
let result = "Hello" + " " + "World";
```

---

**基本写法：字符串复合赋值**
`<变量> += <字符串>`
```javascript
// 追加字符串到变量
let str = "Hello";
str += " World";
```

---

## 三元运算符

**基本写法：三元条件运算符**
`<条件> ? <表达式1> : <表达式2>`
```javascript
// 根据条件选择值
let max = (a > b) ? a : b;
```

---

**基本写法：嵌套三元运算符**
`<条件1> ? <值1> : (<条件2> ? <值2> : <值3>)`
```javascript
// 嵌套三元运算符
let grade = (score >= 90) ? "A" : (score >= 60) ? "B" : "C";
```

---

## 类型运算符

**基本写法：typeof**
`typeof <操作数>`
```javascript
// 获取操作数类型
let type = typeof "hello";
```

---

**基本写法：instanceof**
`<对象> instanceof <构造函数>`
```javascript
// 检查对象是否为某类型实例
let result = arr instanceof Array;
```

---

**基本写法：delete**
`delete <对象>.<属性>`
```javascript
// 删除对象属性
delete obj.name;
```

---

**基本写法：in**
`"<属性>" in <对象>`
```javascript
// 检查属性是否存在于对象中
let has = "name" in obj;
```

---

## 运算符优先级

**基本写法：使用括号明确顺序**
`(<表达式>)`
```javascript
// 使用括号改变运算顺序
let result = (a + b) * (c - d);
```

---

## 数值处理

**基本写法：Math.max**
`Math.max(<值1>, <值2>)`
```javascript
// 获取最大值
let max = Math.max(10, 20);
```

---

**基本写法：Math.min**
`Math.min(<值1>, <值2>)`
```javascript
// 获取最小值
let min = Math.min(10, 20);
```

---

**基本写法：Math.round**
`Math.round(<数字>)`
```javascript
// 四舍五入
let rounded = Math.round(3.7);
```

---

**基本写法：Math.floor**
`Math.floor(<数字>)`
```javascript
// 向下取整
let floored = Math.floor(3.7);
```

---

**基本写法：Math.ceil**
`Math.ceil(<数字>)`
```javascript
// 向上取整
let ceiled = Math.ceil(3.2);
```

---

**基本写法：Math.abs**
`Math.abs(<数字>)`
```javascript
// 取绝对值
let abs = Math.abs(-10);
```

---

**基本写法：Math.random**
`Math.random()`
```javascript
// 生成 0 到 1 之间的随机数
let random = Math.random();
```

---

**基本写法：Number.isInteger**
`Number.isInteger(<值>)`
```javascript
// 判断是否为整数
let isInt = Number.isInteger(42);
```

---

**基本写法：Number.isNaN**
`Number.isNaN(<值>)`
```javascript
// 判断是否为 NaN
let isNan = Number.isNaN(value);
```

---

**基本写法：toFixed**
`<数字>.toFixed(<小数位数>)`
```javascript
// 保留指定小数位
let fixed = (3.14159).toFixed(2);
```



<!-- ============ 文档分隔线：008-javascript/009-ArrayHigherOrderMethod.md ============ -->

# JavaScript 数组高阶方法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## map 方法

**基本写法：map 转换元素**
`<数组>.map(<回调函数>)`
```javascript
// 将数组元素转换为新值
let doubled = numbers.map(n => n * 2);
```

---

**基本写法：map 提取属性**
`<数组>.map(<回调函数>)`
```javascript
// 从对象数组提取属性
let names = users.map(user => user.name);
```

---

**基本写法：map 带索引**
`<数组>.map((<元素>, <索引>) => <表达式>)`
```javascript
// map 回调函数使用索引
let indexed = numbers.map((n, i) => `${i}: ${n}`);
```

---

## filter 方法

**基本写法：filter 过滤**
`<数组>.filter(<条件函数>)`
```javascript
// 过滤满足条件的元素
let evens = numbers.filter(n => n % 2 === 0);
```

---

**基本写法：filter 过滤对象**
`<数组>.filter(<条件函数>)`
```javascript
// 过滤对象数组
let adults = users.filter(user => user.age >= 18);
```

---

**基本写法：filter 去重**
`<数组>.filter((<元素>, <索引>, <数组>) => <条件>)`
```javascript
// 使用 filter 去重
let unique = arr.filter((item, index, array) => array.indexOf(item) === index);
```

---

## reduce 方法

**基本写法：reduce 求和**
`<数组>.reduce((<累加器>, <当前值>) => <表达式>, <初始值>)`
```javascript
// 计算数组元素总和
let sum = numbers.reduce((acc, n) => acc + n, 0);
```

---

**基本写法：reduce 求最大值**
`<数组>.reduce((<累加器>, <当前值>) => <表达式>)`
```javascript
// 查找数组最大值
let max = numbers.reduce((a, b) => Math.max(a, b));
```

---

**基本写法：reduce 计数**
`<数组>.reduce((<累加器>, <当前值>) => <表达式>, <初始值>)`
```javascript
// 统计元素出现次数
let count = words.reduce((acc, word) => {
    acc[word] = (acc[word] || 0) + 1;
    return acc;
}, {});
```

---

**基本写法：reduce 数组转对象**
`<数组>.reduce((<累加器>, <当前值>) => <表达式>, <初始值>)`
```javascript
// 将数组转换为对象
let obj = users.reduce((acc, user) => {
    acc[user.id] = user;
    return acc;
}, {});
```

---

## find 方法

**基本写法：find 查找元素**
`<数组>.find(<条件函数>)`
```javascript
// 查找第一个满足条件的元素
let user = users.find(u => u.age > 18);
```

---

**基本写法：findIndex 查找索引**
`<数组>.findIndex(<条件函数>)`
```javascript
// 查找第一个满足条件的元素索引
let index = users.findIndex(u => u.age > 18);
```

---

## some 方法

**基本写法：some 判断存在**
`<数组>.some(<条件函数>)`
```javascript
// 判断是否有元素满足条件
let hasAdult = users.some(u => u.age >= 18);
```

---

## every 方法

**基本写法：every 判断全部**
`<数组>.every(<条件函数>)`
```javascript
// 判断是否所有元素都满足条件
let allAdult = users.every(u => u.age >= 18);
```

---

## flat 方法

**基本写法：flat 展平一层**
`<数组>.flat()`
```javascript
// 展平数组一层
let flat = [1, [2, 3], [4]].flat();
```

---

**基本写法：flat 展平多层**
`<数组>.flat(<深度>)`
```javascript
// 展平数组指定深度
let flat = [1, [2, [3, [4]]]].flat(Infinity);
```

---

## flatMap 方法

**基本写法：flatMap 映射并展平**
`<数组>.flatMap(<回调函数>)`
```javascript
// 先映射再展平一层
let result = numbers.flatMap(n => [n, n * 2]);
```

---

## sort 方法

**基本写法：sort 数字升序**
`<数组>.sort((<a>, <b>) => <a> - <b>)`
```javascript
// 数字升序排序
numbers.sort((a, b) => a - b);
```

---

**基本写法：sort 数字降序**
`<数组>.sort((<a>, <b>) => <b> - <a>)`
```javascript
// 数字降序排序
numbers.sort((a, b) => b - a);
```

---

**基本写法：sort 对象数组**
`<数组>.sort((<a>, <b>) => <a>.<属性> - <b>.<属性>)`
```javascript
// 按对象属性排序
users.sort((a, b) => a.age - b.age);
```

---

## 链式调用

**基本写法：filter 链 map**
`<数组>.filter(<条件>).map(<映射>)`
```javascript
// 过滤后映射
let names = users.filter(u => u.age >= 18).map(u => u.name);
```

---

**基本写法：map 链 filter**
`<数组>.map(<映射>).filter(<条件>)`
```javascript
// 映射后过滤
let evens = numbers.map(n => n * 2).filter(n => n > 10);
```

---

**基本写法：filter 链 reduce**
`<数组>.filter(<条件>).reduce(<累加>, <初始值>)`
```javascript
// 过滤后求和
let sum = numbers.filter(n => n > 0).reduce((acc, n) => acc + n, 0);
```

---

**换行写法：多方法链式**
`<数组>.filter(<条件>).map(<映射>).reduce(<累加>, <初始值>)`
```javascript
// 多方法链式调用换行书写
let result = numbers
    .filter(n => n > 0)
    .map(n => n * 2)
    .reduce((acc, n) => acc + n, 0);
```

---

## 其他高阶方法

**基本写法：fill 填充**
`<数组>.fill(<值>, <起始>, <结束>)`
```javascript
// 用指定值填充数组
let arr = new Array(5).fill(0);
```

---

**基本写法：copyWithin**
`<数组>.copyWithin(<目标位置>, <起始>, <结束>)`
```javascript
// 数组内部复制
[1, 2, 3, 4, 5].copyWithin(0, 3);
```

---

**基本写法：at 访问**
`<数组>.at(<索引>)`
```javascript
// 使用 at 方法访问元素支持负索引
let last = numbers.at(-1);
```

---

## 数组判断

**基本写法：Array.isArray**
`Array.isArray(<变量>)`
```javascript
// 判断变量是否为数组
let isArray = Array.isArray(numbers);
```

---

**基本写法：includes 判断**
`<数组>.includes(<元素>)`
```javascript
// 判断数组是否包含元素
let has = numbers.includes(3);
```

---

## 数组转换

**基本写法：join 转字符串**
`<数组>.join("<分隔符>")`
```javascript
// 将数组连接为字符串
let str = numbers.join(", ");
```

---

**基本写法：toString**
`<数组>.toString()`
```javascript
// 数组转字符串默认逗号分隔
let str = numbers.toString();
```

---

**基本写法：entries 获取迭代器**
`<数组>.entries()`
```javascript
// 获取键值对迭代器
let entries = numbers.entries();
```

---

**基本写法：keys 获取键迭代器**
`<数组>.keys()`
```javascript
// 获取键索引迭代器
let keys = numbers.keys();
```

---

**基本写法：values 获取值迭代器**
`<数组>.values()`
```javascript
// 获取值迭代器
let values = numbers.values();
```

---

## ES2025 Iterator Helpers

**基本写法：Iterator.map 链式映射**
`<iterator>.map(<回调函数>)`
```javascript
// 迭代器映射元素不创建中间数组惰性求值
let iter = [1, 2, 3].values().map(x => x * 2);
```

---

**基本写法：Iterator.filter 链式过滤**
`<iterator>.filter(<条件函数>)`
```javascript
// 迭代器过滤满足条件的元素
let iter = [1, 2, 3, 4].values().filter(x => x % 2 === 0);
```

---

**基本写法：Iterator.take 取前 N 个**
`<iterator>.take(<数量>)`
```javascript
// 从迭代器取前 N 个元素后停止迭代
let iter = [1, 2, 3, 4].values().take(2);
```

---

**基本写法：Iterator.drop 跳过前 N 个**
`<iterator>.drop(<数量>)`
```javascript
// 跳过迭代器前 N 个元素返回剩余元素
let iter = [1, 2, 3, 4].values().drop(2);
```

---

**基本写法：Iterator.toArray 转数组**
`<iterator>.toArray()`
```javascript
// 将迭代器消费为数组终结链式操作
let arr = [1, 2, 3].values().map(x => x * 2).toArray();
```



<!-- ============ 文档分隔线：008-javascript/010-AsyncProgramming.md ============ -->

# JavaScript 异步编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 回调函数

**基本写法：回调函数**
`function <函数>(<参数>, <回调>) { <回调>(); }`
```javascript
// 使用回调函数处理异步
function fetchData(url, callback) {
    callback(data);
}
```

---

**基本写法：错误优先回调**
`function <回调>(<错误>, <数据>) { }`
```javascript
// Node.js 风格错误优先回调
function handler(err, data) {
    if (err) {
    }
}
```

---

**基本写法：回调地狱**
`<函数>(<参数>, function() { <函数>(<参数>, function() { }) })`
```javascript
// 嵌套回调
step1(function() {
    step2(function() {
    });
});
```

---

## Promise

**基本写法：创建 Promise**
`new Promise((<resolve>, <reject>) => { })`
```javascript
// 创建 Promise 对象
let promise = new Promise((resolve, reject) => {
});
```

---

**基本写法：Promise resolve**
`new Promise((resolve) => { resolve(<值>); })`
```javascript
// 创建已完成的 Promise
let p = Promise.resolve(42);
```

---

**基本写法：Promise reject**
`new Promise((_, reject) => { reject(<错误>); })`
```javascript
// 创建已拒绝的 Promise
let p = Promise.reject(new Error("Failed"));
```

---

**基本写法：then 处理成功**
`<promise>.then(<成功回调>)`
```javascript
// 处理 Promise 成功结果
promise.then(result => {
});
```

---

**基本写法：catch 处理失败**
`<promise>.catch(<失败回调>)`
```javascript
// 处理 Promise 失败错误
promise.catch(error => {
});
```

---

**基本写法：finally 最终处理**
`<promise>.finally(<回调>)`
```javascript
// 无论成功失败都执行
promise.finally(() => {
});
```

---

**基本写法：链式调用**
`<promise>.then(<回调1>).then(<回调2>)`
```javascript
// Promise 链式调用
promise.then(result => result * 2).then(doubled => {
});
```

---

## async-await

**基本写法：async 函数**
`async function <函数名>() { }`
```javascript
// 声明异步函数
async function fetchData() {
}
```

---

**基本写法：await 等待**
`await <Promise>`
```javascript
// 等待 Promise 完成获取结果
let data = await promise;
```

---

**基本写法：async 箭头函数**
`async (<参数>) => { }`
```javascript
// 异步箭头函数
let fetch = async (url) => {
};
```

---

**基本写法：await 错误处理**
`try { await <Promise> } catch (<错误>) { }`
```javascript
// 使用 try-catch 处理 await 错误
try {
    let data = await promise;
} catch (error) {
}
```

---

**基本写法：async 返回值**
`async function <函数>() { return <值>; }`
```javascript
// async 函数返回 Promise
async function getValue() {
    return 42;
}
```

---

## Promise 静态方法

**基本写法：Promise.all**
`Promise.all([<promise1>, <promise2>])`
```javascript
// 等待所有 Promise 完成
Promise.all([p1, p2, p3]).then(results => {
});
```

---

**基本写法：Promise.race**
`Promise.race([<promise1>, <promise2>])`
```javascript
// 返回第一个完成的 Promise
Promise.race([p1, p2]).then(result => {
});
```

---

**基本写法：Promise.allSettled**
`Promise.allSettled([<promise1>, <promise2>])`
```javascript
// 等待所有 Promise 落定无论成功失败
Promise.allSettled([p1, p2]).then(results => {
});
```

---

**基本写法：Promise.any**
`Promise.any([<promise1>, <promise2>])`
```javascript
// 返回第一个成功的 Promise
Promise.any([p1, p2]).then(result => {
});
```

---

## 定时器

**基本写法：setTimeout**
`setTimeout(<回调>, <毫秒>)`
```javascript
// 延迟执行一次
setTimeout(() => {
}, 1000);
```

---

**基本写法：setInterval**
`setInterval(<回调>, <毫秒>)`
```javascript
// 重复执行
setInterval(() => {
}, 1000);
```

---

**基本写法：clearTimeout**
`clearTimeout(<定时器ID>)`
```javascript
// 清除延迟定时器
clearTimeout(timerId);
```

---

**基本写法：clearInterval**
`clearInterval(<定时器ID>)`
```javascript
// 清除重复定时器
clearInterval(timerId);
```

---

## Promise 封装

**基本写法：Promise 封装 setTimeout**
`new Promise(<resolve> => setTimeout(<resolve>, <毫秒>))`
```javascript
// 将 setTimeout 封装为 Promise
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
```

---

**基本写法：Promise 封装回调函数**
`new Promise((<resolve>, <reject>) => { <回调函数>(<参数>, (<错误>, <数据>) => { }) })`
```javascript
// 将回调函数封装为 Promise
function promisify(fn) {
    return new Promise((resolve, reject) => {
        fn((err, data) => {
            if (err) reject(err);
            else resolve(data);
        });
    });
}
```

---

## 并发控制

**基本写法：async 并发执行**
`await Promise.all([<异步1>(), <异步2>()])`
```javascript
// 并发执行多个异步操作
let [a, b] = await Promise.all([fetchA(), fetchB()]);
```

---

**基本写法：async 顺序执行**
`let <结果1> = await <异步1>(); let <结果2> = await <异步2>();`
```javascript
// 顺序执行多个异步操作
let a = await fetchA();
let b = await fetchB();
```

---

**基本写法：async 循环处理**
`for (let <项> of <数组>) { await <异步>(<项>); }`
```javascript
// 顺序处理数组中的异步操作
for (let item of items) {
    await processItem(item);
}
```

---

## 事件循环

**基本写法：微任务 queueMicrotask**
`queueMicrotask(<回调>)`
```javascript
// 将任务添加到微任务队列
queueMicrotask(() => {
});
```

---

**基本写法：宏任务 setTimeout**
`setTimeout(<回调>, 0)`
```javascript
// 将任务添加到宏任务队列
setTimeout(() => {
}, 0);
```

---

## ES2025 异步新特性

**基本写法：using 显式资源管理**
`using <变量> = <资源>`
```javascript
// 同步资源在作用域结束时自动调用 Symbol.dispose
{
    using handle = createResource();
    handle.doWork();
} // 自动调用 handle[Symbol.dispose]()
```

---

**基本写法：await using 异步资源管理**
`await using <变量> = <异步资源>`
```javascript
// 异步资源在作用域结束时自动 await Symbol.asyncDispose
{
    await using conn = await getConnection();
    await conn.query("SELECT 1");
} // 自动 await conn[Symbol.asyncDispose]()
```

---

**基本写法：Promise.try 替代 async 函数包装**
`Promise.try(<函数>)`
```javascript
// 将同步或异步函数统一包装为 Promise 无需 async 关键字
let p = Promise.try(() => {
    if (cached) return cached;
    return fetch("/api");
});
```



<!-- ============ 文档分隔线：008-javascript/011-Regex.md ============ -->

# JavaScript 正则表达式

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 正则创建

**基本写法：字面量创建**
`/<模式>/<标志>`
```javascript
// 使用字面量创建正则表达式
let pattern = /hello/gi;
```

---

**基本写法：构造函数创建**
`new RegExp("<模式>", "<标志>")`
```javascript
// 使用构造函数创建正则表达式
let pattern = new RegExp("hello", "gi");
```

---

**基本写法：动态模式**
`new RegExp(<变量>)`
```javascript
// 使用变量构建动态模式
let word = "hello";
let pattern = new RegExp(word, "g");
```

---

## 标志

**基本写法：全局标志 g**
`/<模式>/g`
```javascript
// 全局匹配所有结果
let pattern = /hello/g;
```

---

**基本写法：忽略大小写 i**
`/<模式>/i`
```javascript
// 忽略大小写匹配
let pattern = /hello/i;
```

---

**基本写法：多行标志 m**
`/<模式>/m`
```javascript
// 多行模式下 ^ 和 $ 匹配每行
let pattern = /^hello/m;
```

---

**基本写法：组合标志**
`/<模式>/<标志组合>`
```javascript
// 组合多个标志
let pattern = /hello/gim;
```

---

## 字符类

**基本写法：任意字符**
`/.`
```javascript
// 匹配除换行符外的任意字符
let pattern = /a.c/;
```

---

**基本写法：字符集**
`/[<字符>]/`
```javascript
// 匹配方括号内的任意字符
let pattern = /[aeiou]/;
```

---

**基本写法：范围字符集**
`/[<起始>-<结束>]/`
```javascript
// 匹配指定范围的字符
let pattern = /[a-z]/;
```

---

**基本写法：否定字符集**
`/[^<字符>]/`
```javascript
// 匹配不在方括号内的字符
let pattern = /[^0-9]/;
```

---

## 预定义类

**基本写法：数字 \d**
`/\d/`
```javascript
// 匹配数字等价于 [0-9]
let pattern = /\d+/;
```

---

**基本写法：非数字 \D**
`/\D/`
```javascript
// 匹配非数字等价于 [^0-9]
let pattern = /\D+/;
```

---

**基本写法：单词字符 \w**
`/\w/`
```javascript
// 匹配单词字符等价于 [a-zA-Z0-9_]
let pattern = /\w+/;
```

---

**基本写法：非单词字符 \W**
`/\W/`
```javascript
// 匹配非单词字符
let pattern = /\W+/;
```

---

**基本写法：空白 \s**
`/\s/`
```javascript
// 匹配空白字符
let pattern = /\s+/;
```

---

**基本写法：非空白 \S**
`/\S/`
```javascript
// 匹配非空白字符
let pattern = /\S+/;
```

---

## 量词

**基本写法：零次或多次**
`/<字符>*`
```javascript
// 匹配前一个字符零次或多次
let pattern = /ab*c/;
```

---

**基本写法：一次或多次**
`/<字符>+`
```javascript
// 匹配前一个字符一次或多次
let pattern = /ab+c/;
```

---

**基本写法：零次或一次**
`/<字符>?`
```javascript
// 匹配前一个字符零次或一次
let pattern = /ab?c/;
```

---

**基本写法：精确次数**
`/<字符>{<次数>}`
```javascript
// 匹配前一个字符指定次数
let pattern = /a{3}/;
```

---

**基本写法：范围次数**
`/<字符>{<最小>, <最大>}`
```javascript
// 匹配前一个字符指定范围次数
let pattern = /a{2,4}/;
```

---

**基本写法：至少次数**
`/<字符>{<次数>,}`
```javascript
// 匹配前一个字符至少指定次数
let pattern = /a{2,}/;
```

---

## 锚点

**基本写法：行首 ^**
`/^<模式>`
```javascript
// 匹配字符串开头
let pattern = /^Hello/;
```

---

**基本写法：行尾 $**
`/<模式>$/`
```javascript
// 匹配字符串结尾
let pattern = /World$/;
```

---

**基本写法：单词边界 \b**
`/\b<单词>\b/`
```javascript
// 匹配完整单词
let pattern = /\bhello\b/;
```

---

## 分组

**基本写法：捕获组**
`/(<模式>)/`
```javascript
// 捕获匹配的内容
let pattern = /(\d+)-(\d+)/;
```

---

**基本写法：非捕获组**
`/(?:<模式>)/`
```javascript
// 非捕获分组不保存匹配
let pattern = /(?:\d+)-(\d+)/;
```

---

**基本写法：命名捕获组**
`/(?<<名称><模式>)/`
```javascript
// 命名捕获组
let pattern = /(?<year>\d{4})-(?<month>\d{2})/;
```

---

## 选择与引用

**基本写法：选择符**
`/<模式1>|<模式2>/`
```javascript
// 匹配多个模式之一
let pattern = /cat|dog/;
```

---

**基本写法：反向引用**
`/<字符>\1`
```javascript
// 引用第一个捕获组
let pattern = /(\w)\1/;
```

---

## 方法

**基本写法：test 测试**
`<正则>.test(<字符串>)`
```javascript
// 测试字符串是否匹配
let result = /hello/.test("hello world");
```

---

**基本写法：exec 执行**
`<正则>.exec(<字符串>)`
```javascript
// 执行匹配返回结果数组
let result = /(\d+)/.exec("abc123");
```

---

**基本写法：match 方法**
`<字符串>.match(<正则>)`
```javascript
// 字符串匹配正则
let result = "hello".match(/l/g);
```

---

**基本写法：matchAll 方法**
`<字符串>.matchAll(<正则>)`
```javascript
// 返回所有匹配的迭代器
let results = "a1b2c3".matchAll(/\d/g);
```

---

**基本写法：replace 替换**
`<字符串>.replace(<正则>, <替换>)`
```javascript
// 替换匹配的内容
let result = "hello".replace(/l/g, "L");
```

---

**基本写法：replace 回调**
`<字符串>.replace(<正则>, <回调>)`
```javascript
// 使用回调函数替换
let result = "hello".replace(/l/g, match => match.toUpperCase());
```

---

**基本写法：search 查找**
`<字符串>.search(<正则>)`
```javascript
// 查找匹配的索引
let index = "hello".search(/l/);
```

---

**基本写法：split 分割**
`<字符串>.split(<正则>)`
```javascript
// 使用正则分割字符串
let parts = "a,b;c".split(/[,;]/);
```

---

## 断言

**基本写法：正向先行断言**
`/<模式>(?=<断言>)`
```javascript
// 匹配后面跟着指定内容的位置
let pattern = /\d+(?=元)/;
```

---

**基本写法：负向先行断言**
`/<模式>(?!<断言>)`
```javascript
// 匹配后面不跟指定内容的位置
let pattern = /\d+(?!元)/;
```

---

**基本写法：正向后行断言**
`/(?<=<断言>)<模式>/`
```javascript
// 匹配前面是指定内容的位置
let pattern = /(?<=￥)\d+/;
```

---

**基本写法：负向后行断言**
`/(?<!<断言>)<模式>/`
```javascript
// 匹配前面不是指定内容的位置
let pattern = /(?<!\$)\d+/;
```

---

## 常用模式

**基本写法：邮箱匹配**
`/^[<字符>]+@[<字符>]+\.[<字符>]+$/`
```javascript
// 简单邮箱格式匹配
let pattern = /^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$/;
```

---

**基本写法：手机号匹配**
`/^1[3-9]\d{9}$/`
```javascript
// 中国手机号格式匹配
let pattern = /^1[3-9]\d{9}$/;
```

---

**基本写法：URL 匹配**
`/^https?:\/\/<域名>/`
```javascript
// HTTP URL 格式匹配
let pattern = /^https?:\/\/[^\s]+/;
```

---

**基本写法：IP 地址匹配**
`/^(\d{1,3}\.){3}\d{1,3}$/`
```javascript
// IPv4 地址格式匹配
let pattern = /^(\d{1,3}\.){3}\d{1,3}$/;
```

---

## ES2024+ 正则新特性

**基本写法：RegExp v 标志与集合操作**
`/<模式>/v`
```javascript
// v 标志支持集合操作交集 && 差集 -- 与 Unicode 属性
let pattern = /[\p{Letter}&&\p{ASCII}]/v;
```

---

**基本写法：String.prototype.isWellFormed 检查**
`<字符串>.isWellFormed()`
```javascript
// 检查字符串是否为合法 Unicode 无单独代理项
let ok = "hello".isWellFormed();
```

---

**基本写法：RegExp.escape 转义**
`RegExp.escape(<字符串>)`
```javascript
// 转义字符串中的正则特殊字符用于安全构建正则
let escaped = RegExp.escape("a.b*c");
```



<!-- ============ 文档分隔线：008-javascript/012-ErrorReferenceAndControlFlowAndErrorHandling.md ============ -->

# JavaScript 自定义 Error

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Error 基础

**基本写法：创建 Error**
`new Error("<消息>")`
```javascript
// 创建错误对象
let error = new Error("Something went wrong");
```

---

**基本写法：省略 new**
`Error("<消息>")`
```javascript
// 省略 new 创建错误对象
let error = Error("Something went wrong");
```

---

**基本写法：throw Error**
`throw new Error("<消息>")`
```javascript
// 抛出错误
throw new Error("Invalid input");
```

---

**基本写法：Error message 属性**
`<error>.message`
```javascript
// 获取错误消息
let message = error.message;
```

---

**基本写法：Error name 属性**
`<error>.name`
```javascript
// 获取错误名称
let name = error.name;
```

---

**基本写法：Error stack 属性**
`<error>.stack`
```javascript
// 获取错误堆栈信息
let stack = error.stack;
```

---

## 内置 Error 类型

**基本写法：TypeError**
`new TypeError("<消息>")`
```javascript
// 创建类型错误
throw new TypeError("Expected a number");
```

---

**基本写法：RangeError**
`new RangeError("<消息>")`
```javascript
// 创建范围错误
throw new RangeError("Value must be positive");
```

---

**基本写法：SyntaxError**
`new SyntaxError("<消息>")`
```javascript
// 创建语法错误
throw new SyntaxError("Invalid syntax");
```

---

**基本写法：ReferenceError**
`new ReferenceError("<消息>")`
```javascript
// 创建引用错误
throw new ReferenceError("Variable is not defined");
```

---

**基本写法：URIError**
`new URIError("<消息>")`
```javascript
// 创建 URI 错误
throw new URIError("Malformed URI");
```

---

**基本写法：EvalError**
`new EvalError("<消息>")`
```javascript
// 创建 eval 错误
throw new EvalError("Eval failed");
```

---

## 自定义 Error 类

**基本写法：继承 Error**
`class <自定义错误> extends Error { }`
```javascript
// 继承 Error 创建自定义错误
class CustomError extends Error {
}
```

---

**换行写法：带构造方法的自定义错误**
`class <自定义错误> extends Error { constructor(<参数>) { super(<参数>); this.name = <名称>; } }`
```javascript
// 自定义错误带构造方法
class ValidationError extends Error {
    constructor(message) {
        super(message);
        this.name = "ValidationError";
    }
}
```

---

**换行写法：带额外属性的自定义错误**
`class <自定义错误> extends Error { constructor(<参数1>, <参数2>) { super(<参数1>); this.<属性> = <参数2>; } }`
```javascript
// 自定义错误带额外属性
class ApiError extends Error {
    constructor(message, statusCode) {
        super(message);
        this.name = "ApiError";
        this.statusCode = statusCode;
    }
}
```

---

**基本写法：使用自定义错误**
`throw new <自定义错误>("<消息>")`
```javascript
// 抛出自定义错误
throw new ValidationError("Email is required");
```

---

## 错误处理

**基本写法：try-catch**
`try { } catch (<错误>) { }`
```javascript
// 捕获错误
try {
    riskyOperation();
} catch (error) {
}
```

---

**基本写法：try-catch-finally**
`try { } catch (<错误>) { } finally { }`
```javascript
// finally 块无论是否异常都执行
try {
} catch (error) {
} finally {
}
```

---

**基本写法：catch 无参数**
`try { } catch { }`
```javascript
// ES2019+ catch 可省略参数
try {
} catch {
}
```

---

**基本写法：捕获特定错误类型**
`catch (<错误>) { if (<错误> instanceof <类型>) { } }`
```javascript
// 捕获特定类型的错误
try {
} catch (error) {
    if (error instanceof TypeError) {
    }
}
```

---

**基本写法：重新抛出错误**
`catch (<错误>) { throw <错误>; }`
```javascript
// 捕获后重新抛出错误
try {
} catch (error) {
    throw error;
}
```

---

**基本写法：抛出新错误**
`catch (<错误>) { throw new <错误类型>("<消息>", { cause: <错误> }); }`
```javascript
// 抛出新错误并保留原始错误
try {
} catch (error) {
    throw new Error("Operation failed", { cause: error });
}
```

---

## Error.cause

**基本写法：Error cause 选项**
`new Error("<消息>", { cause: <原因> })`
```javascript
// ES2022+ 创建带原因的错误
let error = new Error("Failed", { cause: originalError });
```

---

**基本写法：访问 cause**
`<error>.cause`
```javascript
// 获取错误的原始原因
let cause = error.cause;
```

---

## AggregateError

**基本写法：创建 AggregateError**
`new AggregateError([<错误1>, <错误2>], "<消息>")`
```javascript
// 创建聚合错误
let error = new AggregateError([err1, err2], "Multiple errors");
```

---

**基本写法：访问 errors**
`<error>.errors`
```javascript
// 获取聚合错误中的所有错误
let errors = aggregateError.errors;
```

---

**基本写法：Promise.any 触发 AggregateError**
`Promise.any([<promise1>, <promise2>]).catch(<回调>)`
```javascript
// Promise.any 全部失败时抛出 AggregateError
Promise.any([p1, p2]).catch(error => {
    if (error instanceof AggregateError) {
    }
});
```

---

## 错误断言

**基本写法：自定义断言函数**
`function <断言>(<条件>, "<消息>") { if (!<条件>) throw new Error("<消息>"); }`
```javascript
// 实现断言函数
function assert(condition, message) {
    if (!condition) {
        throw new Error(message);
    }
}
```

---

**基本写法：console.assert**
`console.assert(<条件>, "<消息>")`
```javascript
// 条件为假时输出错误
console.assert(value > 0, "Value must be positive");
```

---

## 错误转换

**基本写法：错误转字符串**
`<error>.toString()`
```javascript
// 将错误转换为字符串
let str = error.toString();
```

---

**基本写法：JSON 序列化错误**
`JSON.stringify(<错误>, Object.getOwnPropertyNames(<错误>))`
```javascript
// 序列化错误对象包含所有属性
let json = JSON.stringify(error, Object.getOwnPropertyNames(error));
```

---

## 错误链

**基本写法：错误链模式**
`try { } catch (<错误>) { throw new <错误类型>("<消息>", { cause: <错误> }); }`
```javascript
// 错误链保留原始错误信息
try {
    operation();
} catch (error) {
    throw new AppError("Operation failed", { cause: error });
}
```

---

**基本写法：遍历错误链**
`let <当前> = <错误>; while (<当前>.cause) { <当前> = <当前>.cause; }`
```javascript
// 遍历错误链获取根本原因
let current = error;
while (current.cause) {
    current = current.cause;
}
```



<!-- ============ 文档分隔线：008-javascript/013-ES6NewFeatures.md ============ -->

# JavaScript ES6+ 新特性

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## let 与 const

**基本写法：let 声明**
`let <变量名> = <值>;`
```javascript
// 声明块级作用域变量
let count = 0;
```

---

**基本写法：const 声明**
`const <常量名> = <值>;`
```javascript
// 声明不可重新赋值的常量
const PI = 3.14159;
```

---

## 箭头函数

**基本写法：箭头函数**
`(<参数>) => <表达式>`
```javascript
// 箭头函数直接返回表达式
let square = x => x * x;
```

---

**基本写法：箭头函数带函数体**
`(<参数>) => { return <值>; }`
```javascript
// 箭头函数带函数体
let greet = (name) => {
    return "Hello, " + name;
};
```

---

## 模板字符串

**基本写法：模板字符串**
`` ` <文本> ` ``
```javascript
// 使用反引号创建字符串
let str = `Hello World`;
```

---

**基本写法：变量插值**
`` ` <文本> ${<变量>} ` ``
```javascript
// 在模板字符串中嵌入变量
let greeting = `Hello, ${name}!`;
```

---

**基本写法：多行字符串**
`` ` <行1> <行2> ` ``
```javascript
// 模板字符串支持多行
let text = `Line 1
Line 2`;
```

---

**基本写法：表达式插值**
`` ` <文本> ${<表达式>} ` ``
```javascript
// 在模板字符串中嵌入表达式
let result = `Sum: ${a + b}`;
```

---

## 解构赋值

**基本写法：数组解构**
`let [ <变量1>, <变量2> ] = <数组>;`
```javascript
// 解构数组元素
let [a, b] = [1, 2];
```

---

**基本写法：对象解构**
`let { <属性1>, <属性2> } = <对象>;`
```javascript
// 解构对象属性
let { name, age } = user;
```

---

**基本写法：默认值解构**
`let { <属性> = <默认值> } = <对象>;`
```javascript
// 解构时设置默认值
let { name = "Unknown" } = user;
```

---

**基本写法：重命名解构**
`let { <属性>: <新名> } = <对象>;`
```javascript
// 解构时重命名变量
let { name: userName } = user;
```

---

**基本写法：剩余元素解构**
`let [ <变量1>, ...<剩余> ] = <数组>;`
```javascript
// 解构剩余元素到数组
let [first, ...rest] = numbers;
```

---

## 展开运算符

**基本写法：数组展开**
`[...<数组1>, ...<数组2>]`
```javascript
// 合并数组
let combined = [...arr1, ...arr2];
```

---

**基本写法：对象展开**
`{ ...<对象1>, ...<对象2> }`
```javascript
// 合并对象
let merged = { ...obj1, ...obj2 };
```

---

**基本写法：函数参数展开**
`<函数>(...<数组>)`
```javascript
// 将数组展开为函数参数
Math.max(...numbers);
```

---

## 默认参数

**基本写法：默认参数**
`function <函数>(<参数> = <默认值>) { }`
```javascript
// 参数默认值
function greet(name = "Guest") {
}
```

---

## 剩余参数

**基本写法：剩余参数**
`function <函数>(...<参数名>) { }`
```javascript
// 收集剩余参数为数组
function sum(...numbers) {
}
```

---

## for-of 循环

**基本写法：for-of 遍历**
`for (let <元素> of <可迭代对象>) { }`
```javascript
// 遍历可迭代对象
for (let item of array) {
}
```

---

## Symbol

**基本写法：创建 Symbol**
`let <变量> = Symbol("<描述>");`
```javascript
// 创建唯一符号
let id = Symbol("id");
```

---

**基本写法：Symbol 作为属性键**
`{ [<Symbol>]: <值> }`
```javascript
// 使用 Symbol 作为对象属性键
let obj = { [id]: 123 };
```

---

## 类

**基本写法：类定义**
`class <类名> { }`
```javascript
// 定义类
class Person {
}
```

---

**基本写法：构造方法**
`constructor(<参数>) { }`
```javascript
// 类的构造方法
class Person {
    constructor(name) {
        this.name = name;
    }
}
```

---

**基本写法：类方法**
`<方法名>() { }`
```javascript
// 定义类方法
class Person {
    greet() {
    }
}
```

---

**基本写法：类继承**
`class <子类> extends <父类> { }`
```javascript
// 类继承
class Student extends Person {
}
```

---

**基本写法：super 调用**
`super.<方法>()`
```javascript
// 调用父类方法
class Student extends Person {
    greet() {
        super.greet();
    }
}
```

---

**基本写法：静态方法**
`static <方法名>() { }`
```javascript
// 定义静态方法
class Person {
    static create() {
    }
}
```

---

## Promise

**基本写法：创建 Promise**
`new Promise((<resolve>, <reject>) => { })`
```javascript
// 创建 Promise 对象
let p = new Promise((resolve, reject) => {
});
```

---

**基本写法：async-await**
`async function <函数>() { await <Promise>; }`
```javascript
// 使用 async-await 处理异步
async function fetchData() {
    let data = await promise;
}
```

---

## Map 与 Set

**基本写法：创建 Map**
`let <变量> = new Map();`
```javascript
// 创建 Map 对象
let map = new Map();
```

---

**基本写法：Map 设置**
`<map>.set(<键>, <值>);`
```javascript
// 设置 Map 键值对
map.set("name", "Alice");
```

---

**基本写法：Map 获取**
`<map>.get(<键>);`
```javascript
// 获取 Map 值
let name = map.get("name");
```

---

**基本写法：创建 Set**
`let <变量> = new Set();`
```javascript
// 创建 Set 对象
let set = new Set();
```

---

**基本写法：Set 添加**
`<set>.add(<值>);`
```javascript
// 向 Set 添加值
set.add(1);
```

---

## 模块化

**基本写法：命名导出**
`export <声明>`
```javascript
// 导出变量
export let name = "Alice";
```

---

**基本写法：默认导出**
`export default <表达式>`
```javascript
// 默认导出
export default function() {
}
```

---

**基本写法：导入**
`import { <标识符> } from "<模块>";`
```javascript
// 导入模块
import { name } from "./module.js";
```

---

## 可选链与空值合并

**基本写法：可选链**
`<对象>?.<属性>`
```javascript
// 安全访问嵌套属性
let name = user?.name;
```

---

**基本写法：可选链方法**
`<对象>?.<方法>()`
```javascript
// 安全调用方法
let result = obj?.method();
```

---

**基本写法：空值合并**
`<值1> ?? <值2>`
```javascript
// 左侧为 null 或 undefined 时返回右侧
let value = a ?? b;
```

---

## 其他特性

**基本写法：BigInt**
`<数字>n`
```javascript
// 创建大整数
let big = 9007199254740991n;
```

---

**基本写法：globalThis**
`globalThis`
```javascript
// 访问全局对象
globalThis.variable = 10;
```

---

**基本写法：数值分隔符**
`<数字>_<数字>`
```javascript
// 使用下划线分隔数字提高可读性
let num = 1_000_000;
```

---

**基本写法：Array.flat**
`<数组>.flat(<深度>)`
```javascript
// 展平嵌套数组
let flat = [1, [2, [3]]].flat(Infinity);
```

---

**基本写法：Object.fromEntries**
`Object.fromEntries(<键值对数组>)`
```javascript
// 将键值对数组转换为对象
let obj = Object.fromEntries([["a", 1], ["b", 2]]);
```

---

**基本写法：String.trimStart**
`<字符串>.trimStart()`
```javascript
// 去除字符串开头空白
let trimmed = " hello".trimStart();
```

---

**基本写法：String.trimEnd**
`<字符串>.trimEnd()`
```javascript
// 去除字符串结尾空白
let trimmed = "hello ".trimEnd();
```

---

## ES2024+ 新特性

**基本写法：Object.groupBy 分组**
`Object.groupBy(<数组>, <回调函数>)`
```javascript
// 按回调返回的键对数组元素分组返回普通对象
let grouped = Object.groupBy([6, 7, 8, 9], n => n % 2 === 0 ? "even" : "odd");
```

---

**基本写法：Map.groupBy 分组**
`Map.groupBy(<数组>, <回调函数>)`
```javascript
// 返回 Map 实例键可以是任意类型不只是字符串
let grouped = Map.groupBy(users, u => u.role);
```

---

**基本写法：Promise.withResolvers 构造器**
`Promise.withResolvers()`
```javascript
// ES2024 新增在外部获取 resolve 和 reject 函数
const { promise, resolve, reject } = Promise.withResolvers();
```

---

**基本写法：ArrayBuffer resize 调整大小**
`<buffer>.resize(<新长度>)`
```javascript
// 调整 ArrayBuffer 大小需 maxByteLength 配置
let buffer = new ArrayBuffer(8, { maxByteLength: 16 });
buffer.resize(12);
```

---

**基本写法：ArrayBuffer transfer 转移所有权**
`<buffer>.transfer([<新长度>])`
```javascript
// 转移 ArrayBuffer 所有权原对象变为 detached 状态
let detached = buffer.transfer(16);
```

---

**基本写法：Atomics.waitAsync 异步等待**
`Atomics.waitAsync(<Int32Array>, <索引>, <值>)`
```javascript
// 异步等待共享内存值变化不阻塞主线程
let result = Atomics.waitAsync(int32, 0, 0);
result.value.then(() => {});
```

---

**基本写法：RegExp v 标志与集合操作**
`/<模式>/v`
```javascript
// v 标志支持集合操作与 Unicode 属性字符串
let pattern = /[\p{Letter}&&\p{ASCII}]/v;
```

---

**基本写法：String.prototype.isWellFormed 检查**
`<字符串>.isWellFormed()`
```javascript
// 检查字符串是否为合法 Unicode 无单独代理项
let ok = "hello".isWellFormed();
```

---

**基本写法：Iterator.prototype.map/filter/take/drop 链式操作**
`<iterator>.map(<回调>).filter(<条件>).take(<数量>).drop(<数量>)`
```javascript
// 迭代器链式操作不创建中间数组惰性求值
let result = [1, 2, 3, 4, 5].values()
    .map(x => x * 2)
    .filter(x => x > 4)
    .drop(1)
    .take(2);
```

---

**基本写法：Iterator.prototype.toArray 转数组**
`<iterator>.toArray()`
```javascript
// 将迭代器消费为数组终结链式操作
let arr = [1, 2, 3].values().map(x => x * 2).toArray();
```

---

**基本写法：Set.prototype.union/intersection/difference 集合操作**
`<set>.union(<其他>) | <set>.intersection(<其他>) | <set>.difference(<其他>)`
```javascript
// 返回新 Set 不修改原 Set
let u = a.union(b);
let i = a.intersection(b);
let d = a.difference(b);
```

---

**基本写法：Set.prototype.isSubsetOf/isSupersetOf/isDisjointFrom**
`<set>.isSubsetOf(<其他>) | <set>.isSupersetOf(<其他>) | <set>.isDisjointFrom(<其他>)`
```javascript
// 返回布尔值判断 Set 间关系
let isSub = a.isSubsetOf(b);
let isSuper = a.isSupersetOf(b);
let isDisjoint = a.isDisjointFrom(b);
```

---

**基本写法：Promise.try 同步函数包装为 Promise**
`Promise.try(<函数>)`
```javascript
// 将同步或异步函数调用统一包装为 Promise
let p = Promise.try(() => fetch("/api"));
```

---

**基本写法：import attributes 加载 JSON 模块**
`import <内容> from "<模块>" with { type: "json" }`
```javascript
// 使用 import attributes 显式声明模块类型
import config from "./config.json" with { type: "json" };
```

---

**基本写法：Float16Array 半精度浮点数组**
`new Float16Array([<元素>])`
```javascript
// 创建半精度浮点数组节省内存适合机器学习
let arr = new Float16Array([1.0, 2.5, 3.14]);
```

---

**基本写法：using 与 await using 显式资源管理**
`using <变量> = <资源> | await using <变量> = <异步资源>`
```javascript
// 资源在作用域结束时自动调用 Symbol.dispose 或 Symbol.asyncDispose
{
    using handle = createResource();
    await using conn = await getConnection();
}
```

---

**基本写法：RegExp.escape 转义**
`RegExp.escape(<字符串>)`
```javascript
// 转义字符串中的正则特殊字符用于安全构建正则
let escaped = RegExp.escape("a.b*c");
```



<!-- ============ 文档分隔线：008-javascript/014-YouDonTKnowJSAsyncPerformance.md ============ -->

# JavaScript Promise 构造器

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Promise 创建

**基本写法：创建 Promise**
`new Promise((<resolve>, <reject>) => { })`
```javascript
// 创建 Promise 对象
let promise = new Promise((resolve, reject) => {
});
```

---

**基本写法：resolve 完成**
`new Promise((resolve) => { resolve(<值>); })`
```javascript
// 创建已完成的 Promise
let p = new Promise((resolve) => {
    resolve("success");
});
```

---

**基本写法：reject 拒绝**
`new Promise((_, reject) => { reject(<错误>); })`
```javascript
// 创建已拒绝的 Promise
let p = new Promise((_, reject) => {
    reject(new Error("failed"));
});
```

---

## Promise 状态

**基本写法：pending 状态**
`new Promise(() => { })`
```javascript
// 创建 pending 状态的 Promise 永不落定
let p = new Promise(() => {
});
```

---

**基本写法：fulfilled 状态**
`Promise.resolve(<值>)`
```javascript
// 创建 fulfilled 状态的 Promise
let p = Promise.resolve(42);
```

---

**基本写法：rejected 状态**
`Promise.reject(<错误>)`
```javascript
// 创建 rejected 状态的 Promise
let p = Promise.reject(new Error("error"));
```

---

## then 方法

**基本写法：then 成功回调**
`<promise>.then(<回调>)`
```javascript
// 处理 Promise 成功结果
promise.then(result => {
});
```

---

**基本写法：then 成功和失败回调**
`<promise>.then(<成功回调>, <失败回调>)`
```javascript
// 同时处理成功和失败
promise.then(
    result => {
    },
    error => {
    }
);
```

---

**基本写法：then 返回值**
`<promise>.then(<回调>).then(<回调>)`
```javascript
// then 返回值传递给下一个 then
promise.then(result => result * 2).then(doubled => {
});
```

---

**基本写法：then 返回 Promise**
`<promise>.then(() => <Promise>)`
```javascript
// then 返回 Promise 会等待完成
promise.then(result => {
    return anotherPromise;
});
```

---

## catch 方法

**基本写法：catch 错误处理**
`<promise>.catch(<错误回调>)`
```javascript
// 捕获 Promise 错误
promise.catch(error => {
});
```

---

**基本写法：catch 链式**
`<promise>.then(<回调>).catch(<回调>)`
```javascript
// then 后接 catch 捕获错误
promise.then(result => {
}).catch(error => {
});
```

---

**基本写法：catch 恢复**
`<promise>.catch(() => <恢复值>)`
```javascript
// catch 返回值可以恢复链
promise.catch(() => "default value").then(result => {
});
```

---

## finally 方法

**基本写法：finally 最终处理**
`<promise>.finally(<回调>)`
```javascript
// 无论成功失败都执行
promise.finally(() => {
});
```

---

**基本写法：finally 链式**
`<promise>.then(<回调>).catch(<回调>).finally(<回调>)`
```javascript
// 完整的 Promise 链
promise
    .then(result => {
    })
    .catch(error => {
    })
    .finally(() => {
    });
```

---

## Promise 链

**基本写法：链式调用**
`<promise>.then(<回调1>).then(<回调2>).then(<回调3>)`
```javascript
// 多个 then 链式调用
promise.then(step1).then(step2).then(step3);
```

---

**换行写法：长链式调用**
`<promise>.then(<回调>).then(<回调>).then(<回调>)`
```javascript
// 换行书写长链式调用
promise
    .then(result => process(result))
    .then(processed => transform(processed))
    .then(transformed => save(transformed));
```

---

**基本写法：链中抛出错误**
`<promise>.then(() => { throw new Error("<消息>"); })`
```javascript
// then 中抛出错误会被 catch 捕获
promise.then(() => {
    throw new Error("Something went wrong");
}).catch(error => {
});
```

---

## Promise 组合

**基本写法：Promise.all**
`Promise.all([<promise1>, <promise2>])`
```javascript
// 等待所有 Promise 完成
Promise.all([p1, p2]).then(results => {
});
```

---

**基本写法：Promise.race**
`Promise.race([<promise1>, <promise2>])`
```javascript
// 返回第一个完成的 Promise
Promise.race([p1, p2]).then(result => {
});
```

---

**基本写法：Promise.allSettled**
`Promise.allSettled([<promise1>, <promise2>])`
```javascript
// 等待所有 Promise 落定
Promise.allSettled([p1, p2]).then(results => {
});
```

---

**基本写法：Promise.any**
`Promise.any([<promise1>, <promise2>])`
```javascript
// 返回第一个成功的 Promise
Promise.any([p1, p2]).then(result => {
});
```

---

## Promise 静态方法

**基本写法：Promise.resolve**
`Promise.resolve(<值>)`
```javascript
// 创建已完成的 Promise
let p = Promise.resolve(42);
```

---

**基本写法：Promise.reject**
`Promise.reject(<错误>)`
```javascript
// 创建已拒绝的 Promise
let p = Promise.reject(new Error("error"));
```

---

**基本写法：Promise.resolve thenable**
`Promise.resolve(<thenable对象>)`
```javascript
// 将 thenable 对象转换为 Promise
let p = Promise.resolve({ then: (resolve) => resolve(42) });
```

---

## 错误处理

**基本写法：throw 错误**
`throw new Error("<消息>")`
```javascript
// 在 Promise 中抛出错误
new Promise(() => {
    throw new Error("Failed");
});
```

---

**基本写法：reject 错误**
`reject(new Error("<消息>"))`
```javascript
// 使用 reject 拒绝 Promise
new Promise((_, reject) => {
    reject(new Error("Failed"));
});
```

---

**基本写法：捕获特定错误**
`<promise>.catch(<错误> => { if (<错误> instanceof <类型>) { } })`
```javascript
// 捕获特定类型的错误
promise.catch(error => {
    if (error instanceof TypeError) {
    }
});
```

---

## Promise 实用模式

**基本写法：Promise 超时**
`Promise.race([<promise>, <超时Promise>])`
```javascript
// 实现 Promise 超时
Promise.race([
    fetchData(),
    new Promise((_, reject) => setTimeout(() => reject(new Error("timeout")), 5000))
]);
```

---

**基本写法：Promise 重试**
`function <重试函数>(<函数>, <次数>) { return <函数>().catch(() => <次数> > 0 ? <重试函数>(<函数>, <次数> - 1) : Promise.reject()); }`
```javascript
// 实现 Promise 重试机制
function retry(fn, times) {
    return fn().catch(() => times > 0 ? retry(fn, times - 1) : Promise.reject());
}
```

---

**基本写法：Promise 顺序执行**
`<数组>.reduce((<链>, <promise>) => <链>.then(() => <promise>()), Promise.resolve())`
```javascript
// 顺序执行 Promise 数组
promises.reduce((chain, promise) => chain.then(() => promise()), Promise.resolve());
```



<!-- ============ 文档分隔线：008-javascript/015-PromiseStaticMethod.md ============ -->

# JavaScript Promise 静态方法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Promise.resolve

**基本写法：resolve 值**
`Promise.resolve(<值>)`
```javascript
// 创建已完成的 Promise
let p = Promise.resolve(42);
```

---

**基本写法：resolve 对象**
`Promise.resolve(<对象>)`
```javascript
// 将对象包装为 Promise
let p = Promise.resolve({ name: "Alice" });
```

---

**基本写法：resolve 数组**
`Promise.resolve(<数组>)`
```javascript
// 将数组包装为 Promise
let p = Promise.resolve([1, 2, 3]);
```

---

**基本写法：resolve thenable**
`Promise.resolve(<thenable>)`
```javascript
// 将 thenable 对象转换为 Promise
let p = Promise.resolve({ then: (resolve) => resolve(42) });
```

---

**基本写法：resolve Promise**
`Promise.resolve(<promise>)`
```javascript
// 传入 Promise 原样返回
let original = Promise.resolve(1);
let p = Promise.resolve(original);
```

---

## Promise.reject

**基本写法：reject 错误**
`Promise.reject(new Error("<消息>"))`
```javascript
// 创建已拒绝的 Promise
let p = Promise.reject(new Error("failed"));
```

---

**基本写法：reject 字符串**
`Promise.reject("<消息>")`
```javascript
// 使用字符串作为拒绝原因
let p = Promise.reject("error occurred");
```

---

**基本写法：reject 对象**
`Promise.reject({ <属性>: <值> })`
```javascript
// 使用对象作为拒绝原因
let p = Promise.reject({ code: 500, message: "Server Error" });
```

---

## Promise.all

**基本写法：all 等待全部**
`Promise.all([<promise1>, <promise2>])`
```javascript
// 等待所有 Promise 完成
Promise.all([p1, p2]).then(results => {
});
```

---

**基本写法：all 结果顺序**
`Promise.all([<promise1>, <promise2>]).then(([<结果1>, <结果2>]) => { })`
```javascript
// 结果顺序与传入顺序一致
Promise.all([fetchA(), fetchB()]).then(([a, b]) => {
});
```

---

**基本写法：all 任一失败**
`Promise.all([<promise1>, <promise2>]).catch(<回调>)`
```javascript
// 任一 Promise 失败则整体失败
Promise.all([p1, p2]).catch(error => {
});
```

---

**基本写法：all 空数组**
`Promise.all([])`
```javascript
// 空数组立即完成
Promise.all([]).then(results => {
});
```

---

## Promise.allSettled

**基本写法：allSettled 等待全部落定**
`Promise.allSettled([<promise1>, <promise2>])`
```javascript
// 等待所有 Promise 落定无论成功失败
Promise.allSettled([p1, p2]).then(results => {
});
```

---

**基本写法：allSettled 结果处理**
`Promise.allSettled([<promise1>, <promise2>]).then(<回调>)`
```javascript
// 处理每个 Promise 的状态和值
Promise.allSettled([p1, p2]).then(results => {
    results.forEach(result => {
        if (result.status === "fulfilled") {
        }
    });
});
```

---

## Promise.race

**基本写法：race 竞速**
`Promise.race([<promise1>, <promise2>])`
```javascript
// 返回第一个落定的 Promise
Promise.race([p1, p2]).then(result => {
});
```

---

**基本写法：race 超时控制**
`Promise.race([<promise>, <超时Promise>])`
```javascript
// 使用 race 实现超时控制
Promise.race([
    fetchData(),
    new Promise((_, reject) => setTimeout(() => reject(new Error("timeout")), 5000))
]);
```

---

## Promise.any

**基本写法：any 第一个成功**
`Promise.any([<promise1>, <promise2>])`
```javascript
// 返回第一个成功的 Promise
Promise.any([p1, p2]).then(result => {
});
```

---

**基本写法：any 全部失败**
`Promise.any([<promise1>, <promise2>]).catch(<回调>)`
```javascript
// 所有 Promise 失败则抛出 AggregateError
Promise.any([p1, p2]).catch(error => {
});
```

---

## Promise.withResolvers

**基本写法：withResolvers**
`Promise.withResolvers()`
```javascript
// 获取 Promise 和 resolve reject 函数
const { promise, resolve, reject } = Promise.withResolvers();
```

---

## 实用模式

**基本写法：并行执行**
`Promise.all([<异步1>(), <异步2>(), <异步3>()])`
```javascript
// 并行执行多个异步操作
Promise.all([fetchUsers(), fetchPosts(), fetchComments()]);
```

---

**基本写法：容错执行**
`Promise.allSettled([<promise1>, <promise2>])`
```javascript
// 容错执行即使部分失败也继续
Promise.allSettled([fetchA(), fetchB()]).then(results => {
});
```

---

**基本写法：首个成功**
`Promise.any([<promise1>, <promise2>])`
```javascript
// 获取首个成功的响应
Promise.any([fetchPrimary(), fetchBackup()]);
```

---

**基本写法：超时控制**
`Promise.race([<promise>, <超时Promise>])`
```javascript
// 限制 Promise 执行时间
Promise.race([
    fetch(),
    new Promise((_, reject) => setTimeout(() => reject(new Error("timeout")), 3000))
]);
```

---

## 错误处理

**基本写法：all 错误处理**
`Promise.all([<promise1>, <promise2>]).catch(<回调>)`
```javascript
// Promise.all 任一失败触发 catch
Promise.all([p1, p2]).catch(error => {
});
```

---

**基本写法：any 错误处理**
`Promise.any([<promise1>, <promise2>]).catch(<回调>)`
```javascript
// Promise.any 全部失败触发 AggregateError
Promise.any([p1, p2]).catch(error => {
});
```

---

**基本写法：allSettled 错误处理**
`Promise.allSettled([<promise1>, <promise2>]).then(<回调>)`
```javascript
// allSettled 不会触发 catch 需在 then 中处理
Promise.allSettled([p1, p2]).then(results => {
    results.forEach(r => {
        if (r.status === "rejected") {
        }
    });
});
```

---

## 数组映射为 Promise

**基本写法：数组映射 Promise**
`Promise.all(<数组>.map(<异步函数>))`
```javascript
// 将数组元素映射为 Promise 并行执行
Promise.all(urls.map(url => fetch(url)));
```

---

**基本写法：数组顺序执行**
`<数组>.reduce(<链式回调>, Promise.resolve())`
```javascript
// 顺序执行数组中的异步操作
items.reduce((chain, item) => chain.then(() => process(item)), Promise.resolve());
```

---

## ES2024+ Promise 新增

**基本写法：ES2024 Promise.withResolvers**
`const { promise, resolve, reject } = Promise.withResolvers()`
```javascript
// ES2024 新增替代 new Promise 内部 resolve reject 模式
const { promise, resolve } = Promise.withResolvers();
setTimeout(() => resolve("done"), 1000);
let result = await promise;
```

---

**基本写法：ES2025 Promise.try**
`Promise.try(<函数>)`
```javascript
// 将同步或异步函数调用统一包装为 Promise 无需 async 关键字
let p = Promise.try(() => {
    if (invalid) throw new Error("bad");
    return fetch("/api");
});
```

---

**基本写法：withResolvers 与传统 Deferred 对比**
`Promise.withResolvers() // 替代 new Promise((resolve, reject) => { })`
```javascript
// 传统写法 resolve reject 受限于回调作用域
// withResolvers 在外部获取无需嵌套回调
const { promise, resolve, reject } = Promise.withResolvers();
// 可在外部任意位置调用 resolve reject
button.onclick = () => resolve("clicked");
```



<!-- ============ 文档分隔线：008-javascript/016-EventLoopDetailed.md ============ -->

# JavaScript 事件循环机制

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 调用栈与堆

**基本写法：调用栈执行同步代码**
`<函数调用>`
```javascript
// 同步代码按调用栈后进先出执行
function a() { b(); }
function b() { console.log("done"); }
a();
```

---

## 宏任务与微任务

**基本写法：微任务队列**
`queueMicrotask(<回调>)`
```javascript
// 微任务在当前宏任务结束后立即执行
queueMicrotask(() => console.log("micro"));
```

---

**基本写法：宏任务队列**
`setTimeout(<回调>, <延迟>)`
```javascript
// 宏任务在下一次事件循环执行
setTimeout(() => console.log("macro"), 0);
```

---

**基本写法：微任务优先于宏任务**
`Promise.resolve().then(<回调>)`
```javascript
// then 回调作为微任务先于 setTimeout 执行
Promise.resolve().then(() => console.log("micro"));
setTimeout(() => console.log("macro"), 0);
```

---

## 事件循环阶段

**基本写法：Node.js 事件循环阶段**
`timers -> pending -> poll -> check -> close callbacks`
```javascript
// timers 执行 setTimeout setInterval
// check 执行 setImmediate
// poll 执行 I/O 回调
setTimeout(() => {}, 0);     // timers 阶段
setImmediate(() => {});      // check 阶段
```

---

**基本写法：浏览器事件循环**
`执行脚本 -> 微任务 -> requestAnimationFrame -> 渲染 -> 宏任务`
```javascript
// 浏览器每个宏任务后清空微任务队列
console.log("script");
setTimeout(() => console.log("timeout"), 0);
Promise.resolve().then(() => console.log("promise"));
```

---

## process.nextTick

**基本写法：nextTick 优先级最高**
`process.nextTick(<回调>)`
```javascript
// Node.js 中 nextTick 早于微任务执行
process.nextTick(() => console.log("nextTick"));
Promise.resolve().then(() => console.log("promise"));
```

---

## async await 转换

**基本写法：await 转为 then 链**
`await <promise>`
```javascript
// await 之后的代码相当于 then 回调作为微任务
async function fn() {
    console.log(1);
    await Promise.resolve();
    console.log(3);
}
fn();
console.log(2);  // 输出顺序 1 2 3
```

---

## 任务队列实战

**基本写法：输出顺序判断**
`<同步> -> <微任务> -> <宏任务>`
```javascript
// 经典执行顺序示例
console.log("start");
setTimeout(() => console.log("timeout"));
Promise.resolve().then(() => console.log("promise"));
console.log("end");
// 输出顺序 start end promise timeout
```

---

**基本写法：嵌套微任务**
`<微任务>.then(<回调>)`
```javascript
// 微任务中产生的微任务在同一阶段清空
Promise.resolve()
    .then(() => Promise.resolve())
    .then(() => console.log("nested"));
```

---

**基本写法：宏任务嵌套**
`setTimeout(() => setTimeout(<回调>))`
```javascript
// 宏任务中产生的宏任务进入下一轮循环
setTimeout(() => {
    setTimeout(() => console.log("inner"));
}, 0);
```

---

## requestAnimationFrame

**基本写法：rAF 在渲染前执行**
`requestAnimationFrame(<回调>)`
```javascript
// rAF 在浏览器重绘前调用适合动画
requestAnimationFrame(() => console.log("rAF"));
```

---

**基本写法：rAF 与 setTimeout 区别**
`requestAnimationFrame(<回调>)`
```javascript
// rAF 同步浏览器刷新率通常 60fps
let start = performance.now();
requestAnimationFrame(t => console.log(t - start));
```

---

## 任务拆分

**基本写法：长任务拆分**
`setTimeout(<回调>, 0)`
```javascript
// 拆分长任务避免阻塞主线程
function chunk(tasks) {
    if (tasks.length === 0) return;
    const task = tasks.shift();
    task();
    setTimeout(() => chunk(tasks), 0);
}
```

---

**基本写法：使用 scheduler.yield**
`await scheduler.yield()`
```javascript
// ES2024+ 让出主线程继续执行后续代码
async function work() {
    for (const item of items) {
        process(item);
        await scheduler.yield();
    }
}
```

---

## MessageChannel

**基本写法：MessageChannel 创建宏任务**
`new MessageChannel()`
```javascript
// MessageChannel 端口通信是宏任务
const { port1, port2 } = new MessageChannel();
port1.onmessage = () => console.log("received");
port2.postMessage(null);
```

---

## 异步执行顺序

**基本写法：综合执行顺序**
`<script> -> <micro> -> <macro>`
```javascript
// 同步代码 -> 微任务 -> 宏任务 -> 渲染
console.log(1);
setTimeout(() => console.log(2));
Promise.resolve().then(() => console.log(3));
queueMicrotask(() => console.log(4));
console.log(5);
// 输出 1 5 3 4 2
```

---

## 浏览器渲染时机

**基本写法：渲染与任务交错**
`<宏任务> -> <微任务> -> <rAF> -> <渲染>`
```javascript
// 一帧内执行顺序宏任务清空微任务 rAF 渲染
setTimeout(() => console.log("task"));
requestAnimationFrame(() => console.log("rAF"));
Promise.resolve().then(() => console.log("micro"));
```

---

## 实用模式

**基本写法：nextTick 工具函数**
`Promise.resolve().then(<回调>)`
```javascript
// 浏览器实现 nextTick 等同微任务
const nextTick = fn => Promise.resolve().then(fn);
nextTick(() => console.log("next tick"));
```

---

**基本写法：立即 resolved Promise**
`Promise.resolve().then(<回调>)`
```javascript
// 已 resolved 的 then 仍是异步微任务
Promise.resolve().then(() => console.log("async"));
console.log("sync");
```



<!-- ============ 文档分隔线：008-javascript/017-DOMOperationEvent.md ============ -->

# JavaScript DOM 操作与事件 API

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 节点获取

**基本写法：getElementById**
`document.getElementById(<id>)`
```javascript
// 通过 ID 获取单个元素
let el = document.getElementById("app");
```

---

**基本写法：querySelector**
`document.querySelector(<选择器>)`
```javascript
// 通过 CSS 选择器获取首个匹配元素
let el = document.querySelector(".item");
```

---

**基本写法：querySelectorAll**
`document.querySelectorAll(<选择器>)`
```javascript
// 获取所有匹配元素返回 NodeList
let els = document.querySelectorAll(".item");
```

---

## 节点创建

**基本写法：createElement**
`document.createElement(<标签名>)`
```javascript
// 创建元素节点
let div = document.createElement("div");
```

---

**基本写法：createTextNode**
`document.createTextNode(<文本>)`
```javascript
// 创建文本节点
let text = document.createTextNode("hello");
```

---

**基本写法：DocumentFragment 批量插入**
`document.createDocumentFragment()`
```javascript
// 使用片段批量插入减少重排
let frag = document.createDocumentFragment();
items.forEach(item => {
    let li = document.createElement("li");
    li.textContent = item;
    frag.appendChild(li);
});
list.appendChild(frag);
```

---

## 节点插入与删除

**基本写法：appendChild**
`<父节点>.appendChild(<节点>)`
```javascript
// 在末尾追加子节点
document.body.appendChild(div);
```

---

**基本写法：insertBefore**
`<父节点>.insertBefore(<新节点>, <参考节点>)`
```javascript
// 在参考节点前插入
parent.insertBefore(newNode, refNode);
```

---

**基本写法：removeChild**
`<父节点>.removeChild(<节点>)`
```javascript
// 移除子节点
parent.removeChild(child);
```

---

**基本写法：replaceChild**
`<父节点>.replaceChild(<新节点>, <旧节点>)`
```javascript
// 替换子节点
parent.replaceChild(newNode, oldNode);
```

---

## 现代节点 API

**基本写法：append**
`<父节点>.append(<节点或文本>)`
```javascript
// 追加多个节点或文本字符串
parent.append(node1, "text", node2);
```

---

**基本写法：prepend**
`<父节点>.prepend(<节点或文本>)`
```javascript
// 在开头插入
parent.prepend(newNode);
```

---

**基本写法：before 与 after**
`<节点>.before(<节点>)`
```javascript
// 在节点前或后插入兄弟节点
el.before(newNode);
el.after(anotherNode);
```

---

**基本写法：remove**
`<节点>.remove()`
```javascript
// 节点自移除
el.remove();
```

---

**基本写法：replaceWith**
`<节点>.replaceWith(<新节点>)`
```javascript
// 节点自替换
oldEl.replaceWith(newEl);
```

---

## 属性操作

**基本写法：getAttribute setAttribute**
`<元素>.setAttribute(<名称>, <值>)`
```javascript
// 读写 HTML 属性
el.setAttribute("data-id", "1");
let id = el.getAttribute("data-id");
```

---

**基本写法：dataset 自定义属性**
`<元素>.dataset.<名称>`
```javascript
// 读写 data-* 自定义属性
el.dataset.userId = "42";
let id = el.dataset.userId;
```

---

**基本写法：hasAttribute removeAttribute**
`<元素>.removeAttribute(<名称>)`
```javascript
// 检查与移除属性
el.hasAttribute("disabled");
el.removeAttribute("disabled");
```

---

## classList 操作

**基本写法：add remove**
`<元素>.classList.add(<类名>)`
```javascript
// 添加移除类名
el.classList.add("active");
el.classList.remove("hidden");
```

---

**基本写法：toggle**
`<元素>.classList.toggle(<类名>)`
```javascript
// 切换类名存在则移除否则添加
el.classList.toggle("open");
```

---

**基本写法：contains**
`<元素>.classList.contains(<类名>)`
```javascript
// 判断是否包含类名
if (el.classList.contains("active")) {}
```

---

## 样式操作

**基本写法：内联样式**
`<元素>.style.<属性> = <值>`
```javascript
// 读写内联样式需用驼峰命名
el.style.backgroundColor = "#fff";
```

---

**基本写法：getComputedStyle**
`window.getComputedStyle(<元素>)`
```javascript
// 获取最终计算样式
let style = window.getComputedStyle(el);
let color = style.color;
```

---

**基本写法：cssText 批量设置**
`<元素>.style.cssText = "<样式字符串>"`
```javascript
// 批量设置内联样式
el.style.cssText = "color:red;font-size:14px;";
```

---

## 事件绑定

**基本写法：addEventListener**
`<元素>.addEventListener(<事件>, <回调>, [<选项>])`
```javascript
// 添加事件监听器
el.addEventListener("click", e => {});
```

---

**基本写法：removeEventListener**
`<元素>.removeEventListener(<事件>, <回调>)`
```javascript
// 移除事件监听需同一回调引用
el.removeEventListener("click", handler);
```

---

**基本写法：once 选项**
`<元素>.addEventListener(<事件>, <回调>, { once: true })`
```javascript
// once 表示只触发一次后自动移除
el.addEventListener("click", fn, { once: true });
```

---

**基本写法：capture 捕获阶段**
`<元素>.addEventListener(<事件>, <回调>, { capture: true })`
```javascript
// 在捕获阶段触发
el.addEventListener("click", fn, { capture: true });
```

---

**基本写法：passive 提升滚动性能**
`<元素>.addEventListener(<事件>, <回调>, { passive: true })`
```javascript
// passive 声明不调用 preventDefault 优化滚动
window.addEventListener("touchmove", fn, { passive: true });
```

---

## 事件对象

**基本写法：preventDefault**
`<事件>.preventDefault()`
```javascript
// 阻止默认行为如表单提交链接跳转
a.addEventListener("click", e => e.preventDefault());
```

---

**基本写法：stopPropagation**
`<事件>.stopPropagation()`
```javascript
// 阻止事件冒泡
el.addEventListener("click", e => e.stopPropagation());
```

---

**基本写法：stopImmediatePropagation**
`<事件>.stopImmediatePropagation()`
```javascript
// 阻止冒泡并阻止同元素其他监听器
el.addEventListener("click", e => e.stopImmediatePropagation());
```

---

## 事件委托

**基本写法：事件委托模式**
`<父节点>.addEventListener(<事件>, <回调>)`
```javascript
// 利用冒泡在父节点统一处理
list.addEventListener("click", e => {
    let item = e.target.closest(".item");
    if (item) handle(item);
});
```

---

**基本写法：closest 匹配祖先**
`<元素>.closest(<选择器>)`
```javascript
// 从当前元素向上查找匹配选择器的最近祖先
let card = e.target.closest(".card");
```

---

## 自定义事件

**基本写法：CustomEvent**
`new CustomEvent(<名称>, { detail: <数据> })`
```javascript
// 创建带数据的自定义事件
let evt = new CustomEvent("login", { detail: { user: "Tom" } });
el.dispatchEvent(evt);
```

---

**基本写法：dispatchEvent**
`<元素>.dispatchEvent(<事件>)`
```javascript
// 同步派发事件触发监听器
el.dispatchEvent(new Event("ready"));
```

---

## 遍历与查找

**基本写法：parentNode parentElement**
`<元素>.parentElement`
```javascript
// 获取父节点
let parent = el.parentElement;
```

---

**基本写法：children childNodes**
`<元素>.children`
```javascript
// children 返回元素集合 childNodes 含文本节点
let kids = el.children;
```

---

**基本写法：nextElementSibling**
`<元素>.nextElementSibling`
```javascript
// 获取下一个兄弟元素节点
let next = el.nextElementSibling;
```

---

## MutationObserver

**基本写法：观察 DOM 变化**
`new MutationObserver(<回调>)`
```javascript
// 监听子节点属性变化
let observer = new MutationObserver(muts => {});
observer.observe(el, { childList: true, subtree: true });
```

---

**基本写法：disconnect 断开**
`<observer>.disconnect()`
```javascript
// 停止观察
observer.disconnect();
```

---

## IntersectionObserver

**基本写法：可见性观察**
`new IntersectionObserver(<回调>, [<选项>])`
```javascript
// 监听元素进入视口用于懒加载
let io = new IntersectionObserver(entries => {
    entries.forEach(e => {
        if (e.isIntersecting) loadImage(e.target);
    });
});
io.observe(img);
```

---

**基本写法：rootMargin**
`new IntersectionObserver(<回调>, { rootMargin: "<边距>" })`
```javascript
// 提前预加载设置根边距
let io = new IntersectionObserver(fn, { rootMargin: "100px" });
```

---

## ResizeObserver

**基本写法：尺寸变化观察**
`new ResizeObserver(<回调>)`
```javascript
// 监听元素尺寸变化
let ro = new ResizeObserver(entries => {
    entries.forEach(e => console.log(e.contentRect.width));
});
ro.observe(el);
```

---

## 实用模式

**基本写法：事件委托结合 dataset**
`<父节点>.addEventListener(<事件>, <回调>)`
```javascript
// 通过 dataset 传递上下文数据
list.addEventListener("click", e => {
    let item = e.target.closest("[data-id]");
    if (item) console.log(item.dataset.id);
});
```

---

**基本写法：批量绑定事件**
`<元素列表>.forEach(<元素> => <元素>.addEventListener(<事件>, <回调>))`
```javascript
// 为多个元素绑定相同事件
document.querySelectorAll(".btn")
    .forEach(btn => btn.addEventListener("click", onClick));
```



<!-- ============ 文档分隔线：008-javascript/018-DebounceThrottle.md ============ -->

# JavaScript 防抖节流实现

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 防抖 debounce

**基本写法：防抖基本实现**
`function <防抖>(<函数>, <等待时间>) { }`
```javascript
// 防抖在停止触发后等待时间才执行
function debounce(fn, wait) {
    let timer;
    return function (...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn.apply(this, args), wait);
    };
}
```

---

**基本写法：立即执行防抖**
`function <防抖>(<函数>, <等待时间>, { leading: true })`
```javascript
// 首次触发立即执行后续等待
function debounce(fn, wait) {
    let timer, called = false;
    return function (...args) {
        if (!called) { fn.apply(this, args); called = true; }
        clearTimeout(timer);
        timer = setTimeout(() => called = false, wait);
    };
}
```

---

**基本写法：带 cancel 取消**
`<防抖函数>.cancel()`
```javascript
// 取消未执行的防抖调用
function debounce(fn, wait) {
    let timer;
    const debounced = (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => fn(...args), wait);
    };
    debounced.cancel = () => clearTimeout(timer);
    return debounced;
}
```

---

**基本写法：带 flush 立即执行**
`<防抖函数>.flush()`
```javascript
// 立即执行挂起的调用
function debounce(fn, wait) {
    let timer, lastArgs;
    const debounced = (...args) => {
        lastArgs = args;
        clearTimeout(timer);
        timer = setTimeout(() => fn(...lastArgs), wait);
    };
    debounced.flush = () => { clearTimeout(timer); if (lastArgs) fn(...lastArgs); };
    return debounced;
}
```

---

## 节流 throttle

**基本写法：节流定时器实现**
`function <节流>(<函数>, <等待时间>) { }`
```javascript
// 节流在间隔时间内最多执行一次
function throttle(fn, wait) {
    let timer = null;
    return function (...args) {
        if (timer) return;
        timer = setTimeout(() => { fn.apply(this, args); timer = null; }, wait);
    };
}
```

---

**基本写法：节流时间戳实现**
`function <节流>(<函数>, <等待时间>) { }`
```javascript
// 基于时间戳首次立即执行
function throttle(fn, wait) {
    let last = 0;
    return function (...args) {
        const now = Date.now();
        if (now - last >= wait) { fn.apply(this, args); last = now; }
    };
}
```

---

**基本写法：节流首次与尾调用**
`function <节流>(<函数>, <等待时间>) { }`
```javascript
// 首次立即执行并保留最后一次调用
function throttle(fn, wait) {
    let last = 0, timer, lastArgs;
    return function (...args) {
        const now = Date.now();
        const remaining = wait - (now - last);
        if (remaining <= 0) {
            clearTimeout(timer); timer = null;
            fn.apply(this, args); last = now;
        } else if (!timer) {
            lastArgs = args;
            timer = setTimeout(() => {
                fn.apply(this, lastArgs); last = Date.now(); timer = null;
            }, remaining);
        }
    };
}
```

---

**基本写法：节流带 cancel**
`<节流函数>.cancel()`
```javascript
// 取消节流并重置状态
function throttle(fn, wait) {
    let timer = null;
    const throttled = (...args) => {
        if (timer) return;
        timer = setTimeout(() => { fn(...args); timer = null; }, wait);
    };
    throttled.cancel = () => { clearTimeout(timer); timer = null; };
    return throttled;
}
```

---

## 应用场景

**基本写法：搜索输入防抖**
`<输入框>.addEventListener("input", <防抖>(<回调>, <等待>))`
```javascript
// 输入搜索时减少请求频率
input.addEventListener("input", debounce(e => {
    search(e.target.value);
}, 300));
```

---

**基本写法：窗口 resize 节流**
`window.addEventListener("resize", <节流>(<回调>, <等待>))`
```javascript
// 窗口尺寸变化时节流计算
window.addEventListener("resize", throttle(() => {
    layout();
}, 200));
```

---

**基本写法：滚动事件节流**
`window.addEventListener("scroll", <节流>(<回调>, <等待>))`
```javascript
// 滚动监听懒加载或吸顶
window.addEventListener("scroll", throttle(() => {
    checkInView();
}, 100));
```

---

**基本写法：按钮点击防抖**
`<按钮>.addEventListener("click", <防抖>(<回调>, <等待>))`
```javascript
// 防止按钮多次点击重复提交
btn.addEventListener("click", debounce(submit, 500));
```

---

**基本写法：拖拽节流**
`<元素>.addEventListener("mousemove", <节流>(<回调>, <等待>))`
```javascript
// 拖拽时降低 mousemove 触发频率
el.addEventListener("mousemove", throttle(update, 16));
```

---

## requestAnimationFrame 节流

**基本写法：rAF 节流**
`function <rAF节流>(<回调>) { }`
```javascript
// 基于刷新率节流适合动画场景
function rafThrottle(fn) {
    let locked = false;
    return function (...args) {
        if (locked) return;
        locked = true;
        requestAnimationFrame(() => { fn.apply(this, args); locked = false; });
    };
}
```

---

## 对象方法上下文

**基本写法：对象方法防抖**
`<对象>.<方法> = <防抖>(function () { }, <等待>)`
```javascript
// 保持 this 指向对象本身
const obj = {
    value: 1,
    log: debounce(function () { console.log(this.value); }, 300)
};
```

---

## 高级模式

**基本写法：返回 Promise 防抖**
`function <防抖异步>(<异步函数>, <等待>) { }`
```javascript
// 防抖并返回 Promise 支持异步
function debounceAsync(fn, wait) {
    let timer, rejectPrev;
    return (...args) => {
        clearTimeout(timer);
        if (rejectPrev) rejectPrev("cancelled");
        return new Promise((resolve, reject) => {
            rejectPrev = reject;
            timer = setTimeout(() => fn(...args).then(resolve, reject), wait);
        });
    };
}
```

---

**基本写法：组合防抖与节流**
`<节流>(<防抖>(<函数>, <短等待>), <长等待>)`
```javascript
// 既限制频率又保证停止后触发
const handler = throttle(debounce(save, 100), 1000);
```

---

## 实用工具

**基本写法：lodash 风格防抖**
`import { debounce } from "<lodash>"`
```javascript
// lodash 提供完整防抖实现
import { debounce } from "lodash";
const fn = debounce(search, 300, { leading: false, trailing: true });
```

---

**基本写法：lodash 风格节流**
`import { throttle } from "<lodash>"`
```javascript
// lodash 提供完整节流实现
import { throttle } from "lodash";
const fn = throttle(scroll, 100, { leading: true, trailing: true });
```

---

## 取消与挂起

**基本写法：组件卸载时取消**
`<防抖函数>.cancel()`
```javascript
// 防止组件卸载后回调执行
const handler = debounce(fetch, 300);
onUnmounted(() => handler.cancel());
```

---

**基本写法：Vue 中使用防抖**
`const <方法> = <防抖>(<回调>, <等待>)`
```javascript
// Vue 组合式 API 中防抖
import { onUnmounted } from "vue";
const search = debounce(q => fetch(q), 300);
onUnmounted(() => search.cancel());
```



<!-- ============ 文档分隔线：008-javascript/019-DeepShallowCopy.md ============ -->

# JavaScript 深浅拷贝方法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 浅拷贝

**基本写法：Object.assign**
`Object.assign({}, <源对象>)`
```javascript
// 浅拷贝一级属性嵌套仍引用
let copy = Object.assign({}, obj);
```

---

**基本写法：展开运算符**
`{ ...<对象> }`
```javascript
// 对象展开为浅拷贝
let copy = { ...obj };
```

---

**基本写法：数组展开**
`[ ...<数组> ]`
```javascript
// 数组展开为浅拷贝
let copy = [...arr];
```

---

**基本写法：slice 浅拷贝数组**
`<数组>.slice()`
```javascript
// slice 无参返回新数组
let copy = arr.slice();
```

---

**基本写法：concat 浅拷贝数组**
`<数组>.concat()`
```javascript
// concat 无参返回新数组
let copy = arr.concat();
```

---

**基本写法：Array.from**
`Array.from(<数组>)`
```javascript
// 从可迭代对象创建新数组
let copy = Array.from(arr);
```

---

## JSON 深拷贝

**基本写法：JSON 序列化**
`JSON.parse(JSON.stringify(<对象>))`
```javascript
// 简单深拷贝但无法处理函数 undefined 循环引用
let deep = JSON.parse(JSON.stringify(obj));
```

---

**基本写法：JSON 限制**
`JSON.parse(JSON.stringify(<含 Date 对象>))`
```javascript
// Date 会变成字符串 Map Set 丢失
let obj = { d: new Date() };
let copy = JSON.parse(JSON.stringify(obj));  // d 变为字符串
```

---

## 递归深拷贝

**基本写法：基础递归深拷贝**
`function <深拷贝>(<对象>) { }`
```javascript
// 递归处理对象和数组
function deepClone(obj) {
    if (obj === null || typeof obj !== "object") return obj;
    if (Array.isArray(obj)) return obj.map(deepClone);
    let copy = {};
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) copy[key] = deepClone(obj[key]);
    }
    return copy;
}
```

---

**基本写法：处理 Date RegExp**
`function <深拷贝>(<对象>) { }`
```javascript
// 处理特殊对象类型
function deepClone(obj) {
    if (obj instanceof Date) return new Date(obj);
    if (obj instanceof RegExp) return new RegExp(obj);
    if (obj === null || typeof obj !== "object") return obj;
    let copy = Array.isArray(obj) ? [] : {};
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) copy[key] = deepClone(obj[key]);
    }
    return copy;
}
```

---

## 循环引用处理

**基本写法：使用 WeakMap 解决循环引用**
`function <深拷贝>(<对象>, <hash>) { }`
```javascript
// WeakMap 记录已拷贝对象避免重复
function deepClone(obj, hash = new WeakMap()) {
    if (obj === null || typeof obj !== "object") return obj;
    if (hash.has(obj)) return hash.get(obj);
    let copy = Array.isArray(obj) ? [] : {};
    hash.set(obj, copy);
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) copy[key] = deepClone(obj[key], hash);
    }
    return copy;
}
```

---

## Map Set 拷贝

**基本写法：拷贝 Map**
`new Map(<源 Map>)`
```javascript
// Map 浅拷贝
let copy = new Map(map);
```

---

**基本写法：深拷贝 Map**
`function <深拷贝Map>(<源>) { }`
```javascript
// 递归拷贝 Map 值
function deepCloneMap(map, hash = new WeakMap()) {
    if (hash.has(map)) return hash.get(map);
    let copy = new Map();
    hash.set(map, copy);
    for (let [k, v] of map) copy.set(deepClone(k, hash), deepClone(v, hash));
    return copy;
}
```

---

**基本写法：拷贝 Set**
`new Set(<源 Set>)`
```javascript
// Set 浅拷贝
let copy = new Set(set);
```

---

## structuredClone

**基本写法：structuredClone**
`structuredClone(<对象>)`
```javascript
// 原生深拷贝支持循环引用 Date Map Set
let deep = structuredClone(obj);
```

---

**基本写法：transfer 转移**
`structuredClone(<对象>, { transfer: [<可转移对象>] })`
```javascript
// 转移 ArrayBuffer 提升性能源对象失效
let buf = new ArrayBuffer(8);
let copy = structuredClone(buf, { transfer: [buf] });
```

---

**基本写法：structuredClone 限制**
`structuredClone(<含函数对象>)`
```javascript
// 不支持函数 DOM 节点抛出异常
let obj = { fn: () => {} };
structuredClone(obj);  // 抛出 DataCloneError
```

---

## 特殊对象拷贝

**基本写法：拷贝 RegExp**
`new RegExp(<源>)`
```javascript
// 复制正则对象
let copy = new RegExp(regex);
```

---

**基本写法：拷贝 Date**
`new Date(<源>)`
```javascript
// 复制日期对象
let copy = new Date(date);
```

---

**基本写法：拷贝 Error**
`new <Error类型>(<源>.message)`
```javascript
// 复制错误对象
let copy = new Error(err.message);
```

---

## 自定义类拷贝

**基本写法：通过构造器重建**
`new <类>(<源对象>)`
```javascript
// 调用构造器重新创建实例
class Point {
    constructor(x, y) { this.x = x; this.y = y; }
    clone() { return new Point(this.x, this.y); }
}
```

---

## 性能对比

**基本写法：浅拷贝性能最优**
`{ ...<对象> }`
```javascript
// 浅拷贝最快但只复制一层
let copy = { ...obj };
```

---

**基本写法：structuredClone 平衡**
`structuredClone(<对象>)`
```javascript
// 原生 API 性能优于递归实现
let copy = structuredClone(obj);
```

---

**基本写法：JSON 适合纯数据**
`JSON.parse(JSON.stringify(<对象>))`
```javascript
// 纯数据场景 JSON 最快
let copy = JSON.parse(JSON.stringify(data));
```

---

## 实用工具函数

**基本写法：通用深拷贝工具**
`function <deepClone>(<对象>) { }`
```javascript
// 综合处理各种类型的深拷贝
function deepClone(obj, hash = new WeakMap()) {
    if (obj === null || typeof obj !== "object") return obj;
    if (obj instanceof Date) return new Date(obj);
    if (obj instanceof RegExp) return new RegExp(obj);
    if (obj instanceof Map) {
        let copy = new Map(); hash.set(obj, copy);
        for (let [k, v] of obj) copy.set(deepClone(k, hash), deepClone(v, hash));
        return copy;
    }
    if (obj instanceof Set) {
        let copy = new Set(); hash.set(obj, copy);
        for (let v of obj) copy.add(deepClone(v, hash));
        return copy;
    }
    if (hash.has(obj)) return hash.get(obj);
    let copy = Array.isArray(obj) ? [] : {};
    hash.set(obj, copy);
    for (let key of Reflect.ownKeys(obj)) copy[key] = deepClone(obj[key], hash);
    return copy;
}
```

---

## 引用关系

**基本写法：浅拷贝引用关系**
`let <副本> = { ...<对象> }`
```javascript
// 嵌套对象仍共享引用
let obj = { nested: { a: 1 } };
let copy = { ...obj };
copy.nested.a = 2;  // obj.nested.a 也变为 2
```

---

**基本写法：深拷贝独立**
`let <副本> = structuredClone(<对象>)`
```javascript
// 深拷贝完全独立互不影响
let obj = { nested: { a: 1 } };
let copy = structuredClone(obj);
copy.nested.a = 2;  // obj.nested.a 仍为 1
```



<!-- ============ 文档分隔线：008-javascript/020-ProxyReflectPractice.md ============ -->

# JavaScript Proxy 与 Reflect

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Proxy 基础

**基本写法：创建 Proxy**
`new Proxy(<目标对象>, <处理器>)`
```javascript
// Proxy 代理目标对象拦截操作
let proxy = new Proxy({}, { get(t, k) { return k in t ? t[k] : 42; } });
```

---

**基本写法：get 拦截**
`new Proxy(<目标>, { get(<target>, <prop>) { } })`
```javascript
// 拦截属性读取
let proxy = new Proxy(obj, {
    get(target, prop) {
        console.log(`read ${String(prop)}`);
        return Reflect.get(target, prop);
    }
});
```

---

**基本写法：set 拦截**
`new Proxy(<目标>, { set(<target>, <prop>, <value>) { } })`
```javascript
// 拦截属性设置做校验
let proxy = new Proxy(obj, {
    set(target, prop, value) {
        if (prop === "age" && value < 0) throw new Error("invalid");
        return Reflect.set(target, prop, value);
    }
});
```

---

**基本写法：has 拦截**
`new Proxy(<目标>, { has(<target>, <prop>) { } })`
```javascript
// 拦截 in 操作符
let proxy = new Proxy(obj, {
    has(target, prop) {
        return prop.startsWith("_") ? false : Reflect.has(target, prop);
    }
});
```

---

**基本写法：deleteProperty 拦截**
`new Proxy(<目标>, { deleteProperty(<target>, <prop>) { } })`
```javascript
// 拦截 delete 操作
let proxy = new Proxy(obj, {
    deleteProperty(target, prop) {
        console.log(`delete ${String(prop)}`);
        return Reflect.deleteProperty(target, prop);
    }
});
```

---

## 函数拦截

**基本写法：apply 拦截**
`new Proxy(<函数>, { apply(<target>, <thisArg>, <args>) { } })`
```javascript
// 拦截函数调用
let fn = new Proxy(function (x) { return x; }, {
    apply(target, thisArg, args) {
        return Reflect.apply(target, thisArg, args) * 2;
    }
});
fn(5);  // 10
```

---

**基本写法：construct 拦截**
`new Proxy(<构造器>, { construct(<target>, <args>) { } })`
```javascript
// 拦截 new 调用
let Klass = new Proxy(function () {}, {
    construct(target, args) {
        return Reflect.construct(target, args);
    }
});
new Klass();
```

---

## Reflect 静态方法

**基本写法：Reflect.get**
`Reflect.get(<目标>, <属性>, [<this>])`
```javascript
// 等同 target[key] 但可指定 this
let val = Reflect.get(obj, "name");
```

---

**基本写法：Reflect.set**
`Reflect.set(<目标>, <属性>, <值>, [<this>])`
```javascript
// 等同赋值返回布尔表示成功
let ok = Reflect.set(obj, "name", "Tom");
```

---

**基本写法：Reflect.has**
`Reflect.has(<目标>, <属性>)`
```javascript
// 等同 in 操作符
let exists = Reflect.has(obj, "name");
```

---

**基本写法：Reflect.ownKeys**
`Reflect.ownKeys(<目标>)`
```javascript
// 返回所有自有键含 Symbol
let keys = Reflect.ownKeys(obj);
```

---

**基本写法：Reflect.deleteProperty**
`Reflect.deleteProperty(<目标>, <属性>)`
```javascript
// 等同 delete 返回布尔
let ok = Reflect.deleteProperty(obj, "name");
```

---

**基本写法：Reflect.construct**
`Reflect.construct(<构造器>, <参数列表>)`
```javascript
// 等同 new 但可指定原型
let instance = Reflect.construct(Klass, [1, 2]);
```

---

**基本写法：Reflect.apply**
`Reflect.apply(<函数>, <this>, <参数列表>)`
```javascript
// 函数调用替代 fn.apply
let result = Reflect.apply(fn, thisArg, [1, 2]);
```

---

## 常见陷阱

**基本写法：响应式对象**
`new Proxy(<目标>, { get, set })`
```javascript
// 简易响应式系统
function reactive(obj) {
    return new Proxy(obj, {
        get(target, key, receiver) {
            track(target, key);
            return Reflect.get(target, key, receiver);
        },
        set(target, key, value, receiver) {
            const result = Reflect.set(target, key, value, receiver);
            trigger(target, key);
            return result;
        }
    });
}
```

---

**基本写法：私有属性保护**
`new Proxy(<目标>, { get, has })`
```javascript
// 禁止访问下划线开头属性
let proxy = new Proxy(obj, {
    get(target, prop) {
        if (prop[0] === "_") throw new Error("private");
        return Reflect.get(target, prop);
    }
});
```

---

**基本写法：默认值**
`new Proxy(<目标>, { get })`
```javascript
// 属性不存在时返回默认值
let proxy = new Proxy({}, {
    get(target, prop) {
        return prop in target ? target[prop] : "default";
    }
});
```

---

**基本写法：缓存代理**
`new Proxy(<函数>, { apply })`
```javascript
// 缓存函数结果
function memoize(fn) {
    let cache = new Map();
    return new Proxy(fn, {
        apply(target, thisArg, args) {
            let key = JSON.stringify(args);
            if (!cache.has(key)) cache.set(key, Reflect.apply(target, thisArg, args));
            return cache.get(key);
        }
    });
}
```

---

**基本写法：属性验证**
`new Proxy(<目标>, { set })`
```javascript
// 设置属性时做类型校验
let proxy = new Proxy({}, {
    set(target, prop, value) {
        if (prop === "age" && typeof value !== "number") return false;
        return Reflect.set(target, prop, value);
    }
});
```

---

**基本写法：日志代理**
`new Proxy(<目标>, { get, set })`
```javascript
// 记录属性访问与修改
let proxy = new Proxy(obj, {
    get(target, prop) {
        console.log(`get ${String(prop)}`);
        return Reflect.get(target, prop);
    },
    set(target, prop, value) {
        console.log(`set ${String(prop)} = ${value}`);
        return Reflect.set(target, prop, value);
    }
});
```

---

## receiver 参数

**基本写法：receiver 保持 this 指向**
`Reflect.get(<target>, <prop>, <receiver>)`
```javascript
// receiver 保证 getter 中的 this 正确
let proxy = new Proxy(obj, {
    get(target, prop, receiver) {
        return Reflect.get(target, prop, receiver);
    }
});
```

---

## 可撤销 Proxy

**基本写法：revoke 撤销**
`Proxy.revocable(<目标>, <处理器>)`
```javascript
// 创建可撤销代理
let { proxy, revoke } = Proxy.revocable(obj, {
    get(t, k) { return Reflect.get(t, k); }
});
revoke();  // 之后访问 proxy 抛出 TypeError
```

---

## 数组代理

**基本写法：数组索引拦截**
`new Proxy(<数组>, { get, set })`
```javascript
// 拦截数组读写触发更新
let arr = new Proxy([1, 2, 3], {
    set(target, prop, value, receiver) {
        if (!isNaN(prop)) console.log(`set index ${prop}`);
        return Reflect.set(target, prop, value, receiver);
    }
});
arr[0] = 99;
```

---

## 实用模式

**基本写法：观察者模式**
`function <observable>(<对象>, <回调>)`
```javascript
// 监听对象所有修改
function observable(obj, callback) {
    return new Proxy(obj, {
        set(target, prop, value, receiver) {
            const old = target[prop];
            const result = Reflect.set(target, prop, value, receiver);
            if (old !== value) callback(prop, value, old);
            return result;
        }
    });
}
```

---

**基本写法：单例代理**
`new Proxy(<构造器>, { construct })`
```javascript
// 限制只能创建一个实例
let Singleton = new Proxy(class {}, {
    construct(target, args) {
        if (!instance) instance = Reflect.construct(target, args);
        return instance;
    }
});
```

---

## Proxy 限制

**基本写法：不可代理的对象**
`new Proxy(<目标>, <处理器>)`
```javascript
// 一些内置对象不可代理如 Map 的内部槽
let proxy = new Proxy(new Map(), {});
proxy.set("a", 1);  // 抛出 TypeError
```

---

**基本写法：兼容性处理**
`Object.defineProperty(<对象>, <属性>, <描述>)`
```javascript
// Proxy 不支持时退回 defineProperty
function defineReactive(obj, key, val) {
    Object.defineProperty(obj, key, {
        get() { return val; },
        set(newVal) { val = newVal; }
    });
}
```



<!-- ============ 文档分隔线：008-javascript/021-StorageForTheWeb.md ============ -->

# JavaScript Web 存储 API

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## localStorage

**基本写法：setItem 存储**
`localStorage.setItem(<键>, <值>)`
```javascript
// 存储字符串值
localStorage.setItem("user", "Tom");
```

---

**基本写法：getItem 读取**
`localStorage.getItem(<键>)`
```javascript
// 读取存储的值不存在返回 null
let user = localStorage.getItem("user");
```

---

**基本写法：removeItem 删除**
`localStorage.removeItem(<键>)`
```javascript
// 删除指定键
localStorage.removeItem("user");
```

---

**基本写法：clear 清空**
`localStorage.clear()`
```javascript
// 清空当前域所有存储
localStorage.clear();
```

---

**基本写法：遍历键**
`localStorage.length` | `localStorage.key(<索引>)`
```javascript
// 遍历所有存储项
for (let i = 0; i < localStorage.length; i++) {
    let key = localStorage.key(i);
}
```

---

**基本写法：存储对象**
`localStorage.setItem(<键>, JSON.stringify(<对象>))`
```javascript
// 对象需序列化为字符串存储
localStorage.setItem("user", JSON.stringify({ name: "Tom" }));
```

---

**基本写法：读取对象**
`JSON.parse(localStorage.getItem(<键>))`
```javascript
// 读取后反序列化注意 null 处理
let user = JSON.parse(localStorage.getItem("user") || "null");
```

---

## sessionStorage

**基本写法：会话级存储**
`sessionStorage.setItem(<键>, <值>)`
```javascript
// 标签页关闭后清除
sessionStorage.setItem("token", "abc");
```

---

**基本写法：API 与 localStorage 一致**
`sessionStorage.getItem(<键>)`
```javascript
// API 完全相同生命周期不同
let token = sessionStorage.getItem("token");
```

---

## 存储事件

**基本写法：跨标签页通信**
`window.addEventListener("storage", <回调>)`
```javascript
// 同源其他标签页 storage 变化触发
window.addEventListener("storage", e => {
    console.log(e.key, e.newValue);
});
```

---

**基本写法：事件对象**
`{ key, newValue, oldValue, url }`
```javascript
// storage 事件包含变更详情
window.addEventListener("storage", e => {
    if (e.key === "cart") updateCart(e.newValue);
});
```

---

## IndexedDB 基础

**基本写法：打开数据库**
`indexedDB.open(<名称>, [<版本>])`
```javascript
// 打开或创建数据库返回请求
let req = indexedDB.open("myDB", 1);
```

---

**基本写法：监听事件**
`<请求>.onsuccess = <回调>` | `<请求>.onupgradeneeded = <回调>`
```javascript
// 升级时创建对象仓库
let req = indexedDB.open("myDB", 1);
req.onupgradeneeded = e => {
    let db = e.target.result;
    db.createObjectStore("users", { keyPath: "id" });
};
req.onsuccess = e => { let db = e.target.result; };
```

---

**基本写法：创建仓库与索引**
`<db>.createObjectStore(<名称>, { keyPath: <键> })`
```javascript
// 在 upgrade 时创建仓库
let store = db.createObjectStore("users", { keyPath: "id" });
store.createIndex("name", "name", { unique: false });
```

---

## IndexedDB 事务

**基本写法：开启事务**
`<db>.transaction(<仓库名>, <模式>)`
```javascript
// 事务读写数据
let tx = db.transaction("users", "readwrite");
let store = tx.objectStore("users");
```

---

**基本写法：添加数据**
`<store>.add(<对象>)`
```javascript
// 添加记录
let tx = db.transaction("users", "readwrite");
tx.objectStore("users").add({ id: 1, name: "Tom" });
```

---

**基本写法：读取数据**
`<store>.get(<键>)`
```javascript
// 按键读取
let req = db.transaction("users").objectStore("users").get(1);
req.onsuccess = e => console.log(e.target.result);
```

---

**基本写法：修改数据**
`<store>.put(<对象>)`
```javascript
// put 存在则更新不存在则添加
tx.objectStore("users").put({ id: 1, name: "Jerry" });
```

---

**基本写法：删除数据**
`<store>.delete(<键>)`
```javascript
// 按键删除记录
tx.objectStore("users").delete(1);
```

---

**基本写法：清空仓库**
`<store>.clear()`
```javascript
// 清空整个仓库
tx.objectStore("users").clear();
```

---

## IndexedDB 游标

**基本写法：遍历数据**
`<store>.openCursor()`
```javascript
// 使用游标遍历所有记录
let req = db.transaction("users").objectStore("users").openCursor();
req.onsuccess = e => {
    let cursor = e.target.result;
    if (cursor) { console.log(cursor.value); cursor.continue(); }
};
```

---

**基本写法：使用索引查询**
`<store>.index(<索引名>).get(<值>)`
```javascript
// 通过索引查询
let req = store.index("name").get("Tom");
```

---

## Promise 封装

**基本写法：Promise 封装 IndexedDB**
`function <open>(<名称>, <版本>, <升级回调>) { }`
```javascript
// 将请求 API 转为 Promise
function openDB(name, version, upgrade) {
    return new Promise((resolve, reject) => {
        let req = indexedDB.open(name, version);
        req.onupgradeneeded = e => upgrade(e.target.result);
        req.onsuccess = e => resolve(e.target.result);
        req.onerror = e => reject(e.target.error);
    });
}
```

---

**基本写法：async await 操作**
`await <封装的请求>`
```javascript
// 配合 async await 优雅操作
async function getUser(db, id) {
    return new Promise((resolve, reject) => {
        let req = db.transaction("users").objectStore("users").get(id);
        req.onsuccess = () => resolve(req.result);
        req.onerror = () => reject(req.error);
    });
}
```

---

## Cookie

**基本写法：写入 Cookie**
`document.cookie = "<键>=<值>; [expires=<日期>]; [path=<路径>]"`
```javascript
// 设置 cookie 默认会话级
document.cookie = "user=Tom; max-age=3600; path=/";
```

---

**基本写法：读取 Cookie**
`document.cookie`
```javascript
// 读取返回所有 cookie 字符串
let cookies = document.cookie;
```

---

**基本写法：删除 Cookie**
`document.cookie = "<键>=; expires=<过去时间>"`
```javascript
// 设置过期时间为过去删除
document.cookie = "user=; expires=Thu, 01 Jan 1970 00:00:00 GMT";
```

---

## Cache API

**基本写法：打开缓存**
`caches.open(<名称>)`
```javascript
// 用于 Service Worker 缓存
caches.open("v1").then(cache => {});
```

---

**基本写法：缓存请求**
`<cache>.put(<请求>, <响应>)`
```javascript
// 缓存 fetch 响应
caches.open("v1").then(cache => {
    fetch("/api").then(res => cache.put("/api", res.clone()));
});
```

---

**基本写法：读取缓存**
`<cache>.match(<请求>)`
```javascript
// 从缓存匹配请求
caches.open("v1").then(cache => cache.match("/api"))
    .then(res => {});
```

---

## 存储容量

**基本写法：查询存储估算**
`navigator.storage.estimate()`
```javascript
// 查询当前使用量与配额
navigator.storage.estimate().then(est => {
    console.log(est.usage, est.quota);
});
```

---

**基本写法：请求持久化存储**
`navigator.storage.persist()`
```javascript
// 请求持久化避免被自动清除
navigator.storage.persist().then(persisted => {});
```

---

## 工具函数

**基本写法：JSON 存储封装**
`const <storage> = { get, set, remove }`
```javascript
// 封装 localStorage JSON 操作
const storage = {
    get(key, def = null) {
        let val = localStorage.getItem(key);
        return val ? JSON.parse(val) : def;
    },
    set(key, value) { localStorage.setItem(key, JSON.stringify(value)); },
    remove(key) { localStorage.removeItem(key); }
};
```

---

**基本写法：带过期时间存储**
`<storage>.set(<键>, <值>, <过期毫秒>)`
```javascript
// 数据自动过期
const storage = {
    set(key, value, ttl) {
        localStorage.setItem(key, JSON.stringify({
            value, expire: Date.now() + ttl
        }));
    },
    get(key) {
        let data = JSON.parse(localStorage.getItem(key) || "null");
        if (!data) return null;
        if (data.expire < Date.now()) { localStorage.removeItem(key); return null; }
        return data.value;
    }
};
```

---

## 存储选择

**基本写法：选型对比**
| 存储 | 容量 | 同步 | 生命周期 |
|------|------|------|----------|
| localStorage | 5-10MB | 同步 | 永久 |
| sessionStorage | 5-10MB | 同步 | 会话 |
| IndexedDB | 数百MB+ | 异步 | 永久 |
| Cookie | 4KB | 同步 | 可配置 |
```javascript
// 小数据用 localStorage 大数据用 IndexedDB
```



<!-- ============ 文档分隔线：008-javascript/022-ModuleDynamicImportCodeSplitting.md ============ -->

# JavaScript 动态 import 与代码分割

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 静态 import 回顾

**基本写法：静态导入**
`import <名称> from "<模块>"`
```javascript
// 静态导入在编译期分析打包到主 bundle
import lodash from "lodash";
```

---

**基本写法：命名导入**
`import { <名称>, <名称> } from "<模块>"`
```javascript
// 按需导入命名导出
import { debounce, throttle } from "lodash-es";
```

---

## 动态 import

**基本写法：动态 import 返回 Promise**
`import("<模块>")`
```javascript
// 运行时加载模块返回 Promise
import("./module.js").then(mod => {
    mod.doSomething();
});
```

---

**基本写法：await 动态 import**
`const <模块> = await import("<模块>")`
```javascript
// 配合 async await 使用
async function loadFeature() {
    const mod = await import("./feature.js");
    mod.run();
}
```

---

**基本写法：按需加载组件**
`const <组件> = React.lazy(() => import("<路径>"))`
```javascript
// React 路由或组件按需加载
const Page = React.lazy(() => import("./Page"));
```

---

**基本写法：Vue 异步组件**
`() => import("<路径>")`
```javascript
// Vue 异步组件工厂函数
const Page = () => import("./Page.vue");
```

---

## 条件加载

**基本写法：按条件加载**
`if (<条件>) import("<模块>")`
```javascript
// 满足条件才加载减少初始体积
if (typeof IntersectionObserver === "undefined") {
    await import("intersection-observer");
}
```

---

**基本写法：特性检测加载**
`if (!<特性>) import("<polyfill>")`
```javascript
// 按需加载 polyfill
if (!Array.prototype.flat) {
    await import("core-js/modules/es.array.flat");
}
```

---

**基本写法：环境判断**
`if (<环境>) import("<模块>")`
```javascript
// 开发环境加载调试工具
if (process.env.NODE_ENV === "development") {
    const { inspect } = await import("./inspect");
    inspect();
}
```

---

## 事件触发加载

**基本写法：点击后加载**
`<元素>.addEventListener("click", async () => await import("<模块>"))`
```javascript
// 用户点击时才加载模块
btn.addEventListener("click", async () => {
    const { editor } = await import("./editor");
    editor.show();
});
```

---

**基本写法：路由切换加载**
`{ path: "<路径>", component: () => import("<文件>") }`
```javascript
// Vue Router 懒加载路由
const routes = [
    { path: "/about", component: () => import("./About.vue") }
];
```

---

## Webpack 魔法注释

**基本写法：指定 chunk 名称**
`import(/* webpackChunkName: "<名称>" */ "<模块>")`
```javascript
// 自定义 chunk 名称便于识别
import(/* webpackChunkName: "editor" */ "./editor");
```

---

**基本写法：预加载 prefetch**
`import(/* webpackPrefetch: true */ "<模块>")`
```javascript
// 空闲时预加载提升后续体验
import(/* webpackPrefetch: true */ "./next-page");
```

---

**基本写法：预加载 preload**
`import(/* webpackPreload: true */ "<模块>")`
```javascript
// 与父 chunk 并行加载优先级高
import(/* webpackPreload: true */ "./critical");
```

---

**基本写法：组合魔法注释**
`import(/* webpackChunkName: "<n>", webpackPrefetch: true */ "<模块>")`
```javascript
// 多个魔法注释组合使用
import(/* webpackChunkName: "chart", webpackPrefetch: true */ "./chart");
```

---

## Vite Rollup 分割

**基本写法：Vite 自动分割**
`import("<模块>")`
```javascript
// Vite 自动分割动态 import
const mod = await import("./heavy");
```

---

**基本写法：manualChunks 配置**
`build.rollupOptions.output.manualChunks`
```javascript
// 手动配置 chunk 分割
export default {
    build: {
        rollupOptions: {
            output: {
                manualChunks: {
                    vendor: ["react", "react-dom"],
                    utils: ["lodash-es"]
                }
            }
        }
    }
};
```

---

## 加载状态处理

**基本写法：加载中提示**
`<Suspense fallback={<Loading />}>`
```javascript
// React Suspense 配合 lazy 显示加载
const Page = React.lazy(() => import("./Page"));
<Suspense fallback={<Loading />}><Page /></Suspense>;
```

---

**基本写法：错误处理**
`import("<模块>").catch(<回调>)`
```javascript
// 捕获加载失败错误
import("./module").catch(err => {
    console.error("load failed", err);
});
```

---

**基本写法：加载超时**
`Promise.race([import("<模块>"), <超时Promise>])`
```javascript
// 控制加载超时
Promise.race([
    import("./module"),
    new Promise((_, rej) => setTimeout(() => rej("timeout"), 5000))
]);
```

---

**基本写法：重试机制**
`async function <loadWithRetry>(<模块>, <次数>)`
```javascript
// 加载失败自动重试
async function loadWithRetry(path, times = 3) {
    for (let i = 0; i < times; i++) {
        try { return await import(path); }
        catch (e) { if (i === times - 1) throw e; }
    }
}
```

---

## import.meta

**基本写法：获取模块 URL**
`import.meta.url`
```javascript
// 获取当前模块 URL
let url = new URL("./data.json", import.meta.url);
```

---

**基本写法：Vite 环境变量**
`import.meta.env`
```javascript
// Vite 注入的环境变量
if (import.meta.env.DEV) console.log("dev mode");
```

---

**基本写法：动态资源路径**
`new URL("<资源>", import.meta.url)`
```javascript
// 动态计算资源路径
let img = new URL("./assets/logo.png", import.meta.url).href;
```

---

## 命名导出处理

**基本写法：解构动态导入**
`const { <名称> } = await import("<模块>")`
```javascript
// 直接解构命名导出
const { debounce } = await import("lodash-es");
```

---

**基本写法：默认导出**
`const <模块> = (await import("<模块>")).default`
```javascript
// 访问 default 属性
const lodash = (await import("lodash")).default;
```

---

## 实用模式

**基本写法：路由懒加载工厂**
`function <lazy>(<路径>) { return () => import(<路径>); }`
```javascript
// 统一路由懒加载工厂
function lazy(path) {
    return () => import(/* webpackChunkName: "[request]" */ path);
}
```

---

**基本写法：模块缓存复用**
`const <缓存> = new Map(); async function <load>(<名称>)`
```javascript
// 复用已加载模块避免重复
const cache = new Map();
async function load(name) {
    if (!cache.has(name)) cache.set(name, await import(`./mods/${name}`));
    return cache.get(name);
}
```

---

**基本写法：插件系统**
`async function <loadPlugin>(<名称>)`
```javascript
// 动态加载插件
async function loadPlugin(name) {
    const plugin = await import(`./plugins/${name}.js`);
    plugin.install(app);
}
```

---

## 性能优化

**基本写法：首屏关键资源**
`import("<首屏模块>")`
```javascript
// 首屏代码打包主 bundle 非首屏动态加载
const Home = lazy(() => import("./Home"));
```

---

**基本写法：vendor 分割**
`manualChunks: { vendor: <依赖数组> }`
```javascript
// 第三方库单独打包长期缓存
manualChunks: { react: ["react", "react-dom"] }
```

---

**基本写法：资源预取**
`<link rel="prefetch" href="<资源>">`
```javascript
// 提示浏览器空闲时预取
let link = document.createElement("link");
link.rel = "prefetch";
link.href = "/chunk.js";
document.head.appendChild(link);
```



<!-- ============ 文档分隔线：008-javascript/023-DebugPerformanceOptimization.md ============ -->

# JavaScript 调试与性能优化 API

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## console API

**基本写法：分类输出**
`console.<方法>(<内容>)`
```javascript
// 不同级别日志
console.log("info"); console.warn("warn"); console.error("err");
```

---

**基本写法：分组输出**
`console.group(<标题>)` | `console.groupEnd()`
```javascript
// 折叠分组日志
console.group("user");
console.log("name", name);
console.groupEnd();
```

---

**基本写法：表格输出**
`console.table(<数据>)`
```javascript
// 以表格形式展示对象数组
console.table([{ id: 1, name: "Tom" }, { id: 2, name: "Jerry" }]);
```

---

**基本写法：计时**
`console.time(<标签>)` | `console.timeEnd(<标签>)`
```javascript
// 测量代码执行时间
console.time("loop");
for (let i = 0; i < 1000; i++) {}
console.timeEnd("loop");
```

---

**基本写法：计数**
`console.count(<标签>)`
```javascript
// 统计调用次数
function fn() { console.count("fn"); }
```

---

**基本写法：断言**
`console.assert(<条件>, <消息>)`
```javascript
// 条件为假才输出错误
console.assert(value > 0, "value must be positive");
```

---

**基本写法：堆栈追踪**
`console.trace(<消息>)`
```javascript
// 输出调用堆栈
function inner() { console.trace("here"); }
```

---

## debugger 断点

**基本写法：debugger 语句**
`debugger`
```javascript
// 代码中插入断点打开开发者工具时暂停
function fn() { debugger; }
```

---

## performance API

**基本写法：性能时间戳**
`performance.now()`
```javascript
// 高精度时间戳精确到微秒
let start = performance.now();
work();
console.log(performance.now() - start);
```

---

**基本写法：标记测量**
`performance.mark(<名称>)`
```javascript
// 标记时间点
performance.mark("start");
work();
performance.mark("end");
performance.measure("duration", "start", "end");
```

---

**基本写法：获取测量结果**
`performance.getEntriesByName(<名称>)`
```javascript
// 读取测量数据
let measures = performance.getEntriesByName("duration");
console.log(measures[0].duration);
```

---

**基本写法：清理条目**
`performance.clearMarks()` | `performance.clearMeasures()`
```javascript
// 清除标记和测量
performance.clearMarks();
performance.clearMeasures();
```

---

## 性能指标

**基本写法：页面加载性能**
`performance.timing`
```javascript
// 读取页面加载各阶段时间
let t = performance.timing;
let loadTime = t.loadEventEnd - t.navigationStart;
```

---

**基本写法：navigationEntry**
`performance.getEntriesByType("navigation")`
```javascript
// 现代方式获取导航性能
let [nav] = performance.getEntriesByType("navigation");
console.log(nav.domContentLoadedEventEnd);
```

---

**基本写法：资源加载**
`performance.getEntriesByType("resource")`
```javascript
// 获取所有资源加载耗时
let resources = performance.getEntriesByType("resource");
resources.forEach(r => console.log(r.name, r.duration));
```

---

**基本写法：Observer 监听**
`new PerformanceObserver(<回调>)`
```javascript
// 监听性能条目产生
let observer = new PerformanceObserver(list => {
    list.getEntries().forEach(entry => console.log(entry));
});
observer.observe({ entryTypes: ["measure", "resource"] });
```

---

## Web Vitals

**基本写法：核心指标**
`new PerformanceObserver(<回调>)`
```javascript
// 监听 LCP 最大内容绘制
new PerformanceObserver(list => {
    list.getEntries().forEach(e => console.log("LCP", e.startTime));
}).observe({ type: "largest-contentful-paint", buffered: true });
```

---

**基本写法：FID 首次输入延迟**
`new PerformanceObserver(<回调>)`
```javascript
// 监听首次交互延迟
new PerformanceObserver(list => {
    list.getEntries().forEach(e => console.log("FID", e.processingStart - e.startTime));
}).observe({ type: "first-input", buffered: true });
```

---

**基本写法：CLS 布局偏移**
`new PerformanceObserver(<回调>)`
```javascript
// 监听布局偏移累计
new PerformanceObserver(list => {
    list.getEntries().forEach(e => console.log("CLS", e.value));
}).observe({ type: "layout-shift", buffered: true });
```

---

## 内存监测

**基本写法：堆快照**
`performance.memory`
```javascript
// Chrome 提供内存使用估算
let mem = performance.memory;
console.log(mem.usedJSHeapSize, mem.totalJSHeapSize);
```

---

**基本写法：垃圾回收触发**
`window.gc && gc()`
```javascript
// 需要启动参数开启强制 GC 调试用
if (window.gc) window.gc();
```

---

## 长任务监测

**基本写法：长任务观察**
`new PerformanceObserver(<回调>)`
```javascript
// 监听超过 50ms 的任务
new PerformanceObserver(list => {
    list.getEntries().forEach(e => console.log("long task", e.duration));
}).observe({ entryTypes: ["longtask"] });
```

---

## requestAnimationFrame

**基本写法：动画帧回调**
`requestAnimationFrame(<回调>)`
```javascript
// 在下次重绘前执行适合动画
function loop() {
    update();
    requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

---

**基本写法：取消动画帧**
`cancelAnimationFrame(<id>)`
```javascript
// 取消动画帧请求
let id = requestAnimationFrame(loop);
cancelAnimationFrame(id);
```

---

## requestIdleCallback

**基本写法：空闲时段执行**
`requestIdleCallback(<回调>)`
```javascript
// 浏览器空闲时执行低优先级任务
requestIdleCallback(deadline => {
    while (deadline.timeRemaining() > 0) doWork();
});
```

---

**基本写法：超时选项**
`requestIdleCallback(<回调>, { timeout: <毫秒> })`
```javascript
// 强制在指定时间内执行
requestIdleCallback(fn, { timeout: 2000 });
```

---

## 长任务拆分

**基本写法：分片处理大数组**
`async function <chunk>(<数组>, <大小>)`
```javascript
// 使用 scheduler.yield 拆分
async function chunk(arr, size) {
    for (let i = 0; i < arr.length; i += size) {
        process(arr.slice(i, i + size));
        await scheduler.yield();
    }
}
```

---

**基本写法：使用 setTimeout 让出**
`setTimeout(<回调>, 0)`
```javascript
// 拆分长任务避免阻塞
function chunk(tasks) {
    if (!tasks.length) return;
    tasks.shift()();
    setTimeout(() => chunk(tasks), 0);
}
```

---

## 错误捕获

**基本写法：全局错误监听**
`window.addEventListener("error", <回调>)`
```javascript
// 捕获同步错误与资源加载失败
window.addEventListener("error", e => {
    console.log(e.message, e.filename);
});
```

---

**基本写法：Promise 未处理拒绝**
`window.addEventListener("unhandledrejection", <回调>)`
```javascript
// 捕获未处理的 Promise 拒绝
window.addEventListener("unhandledrejection", e => {
    console.log(e.reason);
});
```

---

## 调试工具

**基本写法：断点条件**
`if (<条件>) debugger`
```javascript
// 满足条件才触发断点
for (let i = 0; i < 1000; i++) {
    if (i === 500) debugger;
}
```

---

**基本写法：logpoint 调试**
`console.log(<变量>)`
```javascript
// 使用浏览器 logpoint 不污染代码
// 在 Sources 面板设置行号日志
```

---

## 网络调试

**基本写法：fetch 包装日志**
`function <fetchLog>(<url>, <选项>)`
```javascript
// 包装 fetch 记录请求耗时
async function fetchLog(url, opts) {
    let start = performance.now();
    let res = await fetch(url, opts);
    console.log(url, performance.now() - start);
    return res;
}
```

---

## 性能优化策略

**基本写法：防抖节流**
`<节流>(<回调>, <等待>)`
```javascript
// 限制高频事件触发频率
window.addEventListener("scroll", throttle(fn, 100));
```

---

**基本写法：事件委托**
`<父节点>.addEventListener(<事件>, <回调>)`
```javascript
// 减少监听器数量
list.addEventListener("click", e => {});
```

---

**基本写法：虚拟列表**
`<容器>.addEventListener("scroll", <节流>(<回调>))`
```javascript
// 大列表只渲染可见项
function renderVisible(start, end) {
    container.innerHTML = items.slice(start, end).map(render).join("");
}
```

---

**基本写法：IntersectionObserver 懒加载**
`new IntersectionObserver(<回调>)`
```javascript
// 图片进入视口才加载
let io = new IntersectionObserver(entries => {
    entries.forEach(e => {
        if (e.isIntersecting) { e.target.src = e.target.dataset.src; io.unobserve(e.target); }
    });
});
imgs.forEach(img => io.observe(img));
```

---

## 内存优化

**基本写法：解除引用**
`<变量> = null`
```javascript
// 不再使用的大对象置 null 利于 GC
let bigData = loadData();
process(bigData);
bigData = null;
```

---

**基本写法：WeakMap 弱引用**
`new WeakMap()`
```javascript
// 弱引用键不影响垃圾回收
let cache = new WeakMap();
cache.set(obj, data);
```

---

**基本写法：对象池复用**
`function <pool>(<工厂>)`
```javascript
// 复用对象减少 GC 压力
function pool(factory) {
    let list = [];
    return { get: () => list.pop() || factory(), put: o => list.push(o) };
}
```

---

## 实用工具

**基本写法：性能测量装饰器**
`function <measure>(<函数>)`
```javascript
// 自动测量函数执行时间
function measure(fn, name = fn.name) {
    return function (...args) {
        console.time(name);
        let result = fn.apply(this, args);
        console.timeEnd(name);
        return result;
    };
}
```

---

**基本写法：FPS 监测**
`function <fpsMonitor>()`
```javascript
// 监测动画帧率
function fpsMonitor() {
    let last = performance.now(), frames = 0;
    function loop() {
        frames++;
        let now = performance.now();
        if (now - last >= 1000) {
            console.log("FPS", frames); frames = 0; last = now;
        }
        requestAnimationFrame(loop);
    }
    requestAnimationFrame(loop);
}
```



<!-- ============ 文档分隔线：008-javascript/024-ES2024NewFeatures.md ============ -->

# ES2023/2024/2025 新特性

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

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

---



<!-- ============ 文档分隔线：008-javascript/025-MapSetWeakMapWeakSet.md ============ -->

# JavaScript Map/Set/WeakMap/WeakSet 语法速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Map 基础

**基本写法：创建与增删改查**
`new Map([[<k>, <v>], ...])`
```javascript
// Map 保留插入顺序，键可为任意类型
const m = new Map([["a", 1]]);
m.set("b", 2);     // 添加
m.get("a");        // 1
m.has("b");        // true
m.size;            // 2
m.delete("a");     // 删除
m.clear();         // 清空
```

---

## Map 遍历

**基本写法：遍历键值对**
`<map>.forEach((<v>, <k>) => {})`
```javascript
// 按插入顺序遍历
const m = new Map([["a", 1], ["b", 2]]);
m.forEach((v, k) => console.log(k, v));
```

---

**基本写法：entries / keys / values**
`<map>.entries()`
```javascript
// 返回迭代器
for (const [k, v] of m.entries()) {}
for (const k of m.keys()) {}
for (const v of m.values()) {}
```

---

## Map 与对象互转

**基本写法：对象转 Map**
`new Map(Object.entries(<对象>))`
```javascript
// 对象转 Map
const obj = { a: 1, b: 2 };
const m = new Map(Object.entries(obj));
```

---

**基本写法：Map 转对象**
`Object.fromEntries(<map>)`
```javascript
// Map 转对象，键须为字符串
const obj = Object.fromEntries(m);
```

---

## Set 基础

**基本写法：创建与增删查**
`new Set([<可迭代>])`
```javascript
// Set 值唯一，自动去重
const s = new Set([1, 2, 2, 3]);
s.add(4);          // 添加
s.has(3);          // true
s.size;            // 4
s.delete(2);       // 删除
s.clear();         // 清空
```

---

## Set 去重与运算

**基本写法：数组去重**
`[...new Set(<数组>)]`
```javascript
// 利用 Set 唯一性去重
const uniq = [...new Set([1, 1, 2, 3, 3])]; // [1, 2, 3]
```

---

**基本写法：交集差集（ES2025 前）**
`new Set([...a].filter(x => b.has(x)))`
```javascript
// 兼容写法
const a = new Set([1, 2, 3]);
const b = new Set([2, 3, 4]);
const inter = new Set([...a].filter(x => b.has(x))); // {2,3}
const diff = new Set([...a].filter(x => !b.has(x))); // {1}
```

---

## Set 遍历

**基本写法：遍历 Set**
`for (const <v> of <set>) {}`
```javascript
// Set 默认遍历 values
for (const v of s) {}
s.forEach(v => {});
```

---

## WeakMap 基础

**基本写法：创建与操作**
`new WeakMap([[<对象键>, <值>]])`
```javascript
// 键必须为对象，键被回收后自动清除该项
const wm = new WeakMap();
const key = {};
wm.set(key, "data");
wm.get(key);   // "data"
wm.has(key);   // true
wm.delete(key);
```

---

**基本写法：私有属性模拟**
`const wm = new WeakMap()` | `wm.set(this, <私有>)`
```javascript
// 利用 WeakMap 模拟私有字段
const priv = new WeakMap();
class Counter {
  constructor() { priv.set(this, 0); }
  inc() { priv.set(this, priv.get(this) + 1); }
  get val() { return priv.get(this); }
}
```

---

## WeakSet 基础

**基本写法：创建与操作**
`new WeakSet([<可迭代对象>])`
```javascript
// 只能存对象，弱引用
const ws = new WeakSet();
const o = {};
ws.add(o);
ws.has(o);   // true
ws.delete(o);
```

---

## WeakRef 与 FinalizationRegistry

**基本写法：弱引用对象**
`new WeakRef(<对象>)`
```javascript
// 不阻止垃圾回收
let obj = { data: 1 };
const ref = new WeakRef(obj);
ref.deref(); // 取值，被回收后返回 undefined
```

---

**基本写法：垃圾回收回调**
`new FinalizationRegistry(<回调>)`
```javascript
// 对象被回收时触发清理
const registry = new FinalizationRegistry(held => {
  console.log("释放", held);
});
registry.register(obj, "标记值");
```

---

## Map 与 Object 区别

**基本写法：键类型与顺序**
`<map>.set(<任意键>, <值>)`
```javascript
// Map 键可为对象函数，Object 键转字符串
const m = new Map();
const key = {};
m.set(key, 1); // 对象作键
// Object 作键会被转成 "[object Object]"
```

---

## 性能与选择

**基本写法：频繁增删用 Map**
`<map>.set(<k>, <v>)`
```javascript
// Map 频繁增删性能优于 Object
// 大数据量查找 Map 接近 O(1)
// 需要键为非字符串时必须用 Map
```

---



<!-- ============ 文档分隔线：008-javascript/026-ArrayBufferTypedArray.md ============ -->

# JavaScript ArrayBuffer 与 TypedArray 语法速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## ArrayBuffer 基础

**基本写法：创建定长缓冲**
`new ArrayBuffer(<字节数>)`
```javascript
// 原始二进制数据，固定长度
const buf = new ArrayBuffer(16);
buf.byteLength; // 16
buf.detached;   // false（是否被转移）
```

---

**基本写法：可扩容 ArrayBuffer（ES2024）**
`new ArrayBuffer(<长度>, { maxByteLength: <最大> })`
```javascript
// 创建可调整大小的缓冲
const buf = new ArrayBuffer(8, { maxByteLength: 32 });
buf.resizable;        // true
buf.maxByteLength;    // 32
buf.resize(16);       // 扩容
buf.resize(4);        // 缩容
```

---

**基本写法：transfer 转移所有权（ES2024）**
`<buffer>.transfer([<新字节长度>])`
```javascript
// 转移后原 buffer 被分离不可用
const a = new ArrayBuffer(8);
const b = a.transfer();   // a.detached === true
```

---

## TypedArray 类型

**基本写法：创建各类定型数组**
`new <TypedArray>(<长度>)`
```javascript
// 常见类型
new Int8Array(4);        // 8 位有符号
new Uint8Array(4);       // 8 位无符号
new Uint8ClampedArray(4);// 钳制 0-255
new Int16Array(4);       // 16 位有符号
new Uint16Array(4);      // 16 位无符号
new Int32Array(4);       // 32 位有符号
new Uint32Array(4);      // 32 位无符号
new Float32Array(4);     // 32 位浮点
new Float64Array(4);     // 64 位浮点
new BigInt64Array(4n);   // 64 位大整数
new BigUint64Array(4n);  // 64 位无符号大整数
new Float16Array(4);     // 16 位浮点（ES2025）
```

---

**基本写法：从数组或缓冲创建**
`new <TypedArray>(<可迭代>)` | `new <TypedArray>(<buffer>, [<偏移>], [<长度>])`
```javascript
// 从数组创建
const a = new Uint8Array([1, 2, 3]);
// 共享底层 ArrayBuffer
const buf = new ArrayBuffer(8);
const view = new Uint8Array(buf, 0, 4); // 偏移 0，长度 4
```

---

## TypedArray 属性与操作

**基本写法：底层视图属性**
`<view>.buffer` | `<view>.byteLength` | `<view>.byteOffset`
```javascript
// 访问底层 buffer 与位置
const v = new Int32Array(buf, 4, 2);
v.buffer;      // 底层 ArrayBuffer
v.byteLength;  // 占用字节数
v.byteOffset;  // 在 buffer 中的偏移
v.length;      // 元素个数
```

---

**基本写法：set 复制数据**
`<view>.set(<数组或定型数组>, [<偏移>])`
```javascript
// 批量写入
const v = new Uint8Array(8);
v.set([10, 20, 30], 2); // 从偏移 2 开始写入
```

---

**基本写法：subarray 共享视图**
`<view>.subarray([<开始>, <结束>])`
```javascript
// 返回共享内存的子视图
const v = new Uint8Array([1, 2, 3, 4]);
const sub = v.subarray(1, 3); // [2, 3]，修改 sub 影响 v
```

---

## DataView 视图

**基本写法：创建 DataView**
`new DataView(<buffer>, [<偏移>], [<长度>])`
```javascript
// 可混用大小端读写不同类型
const dv = new DataView(new ArrayBuffer(8));
dv.setInt8(0, 127);
dv.getInt8(0);    // 127
```

---

**基本写法：指定字节序读写**
`<dv>.setInt32(<偏移>, <值>, [<小端>])`
```javascript
// 第三个参数 true 表示小端序
dv.setInt32(0, 0x12345678, true);
dv.getInt32(0, true);     // 305419896
dv.getFloat64(0, true);   // 读取 64 位浮点
```

---

## SharedArrayBuffer 与 Atomics

**基本写法：共享缓冲**
`new SharedArrayBuffer(<字节数>)`
```javascript
// 可跨线程共享（Worker）
const sab = new SharedArrayBuffer(16);
const view = new Int32Array(sab);
```

---

**基本写法：原子操作**
`Atomics.add(<view>, <索引>, <值>)`
```javascript
// 原子读改写，避免竞态
const view = new Int32Array(sab);
Atomics.store(view, 0, 10);
Atomics.add(view, 0, 5);     // 返回旧值 10
Atomics.load(view, 0);       // 15
Atomics.compareExchange(view, 0, 15, 20); // 期望 15 才写 20
```

---

**基本写法：等待与通知**
`Atomics.wait(<view>, <索引>, <期望值>)` | `Atomics.notify(<view>, <索引>, [<数量>])`
```javascript
// 线程间同步
Atomics.wait(view, 0, 0);        // 阻塞直到被通知
Atomics.notify(view, 0, 1);      // 唤醒 1 个等待者
Atomics.waitAsync(view, 0, 0);   // 异步等待（ES2024）
```

---

## 编码转换

**基本写法：字符串与 TypedArray 互转**
`new TextEncoder().encode(<字符串>)`
```javascript
// UTF-8 编解码
const enc = new TextEncoder();
const bytes = enc.encode("中文"); // Uint8Array
const dec = new TextDecoder("utf-8");
dec.decode(bytes); // "中文"
```

---

## 字节序判断

**基本写法：判断大小端**
`new Uint8Array(new Uint32Array([1]).buffer)`
```javascript
// 小端序返回 [1,0,0,0]，大端序返回 [0,0,0,1]
const le = new Uint8Array(new Uint32Array([1]).buffer)[0] === 1;
console.log(le ? "little-endian" : "big-endian");
```

---



<!-- ============ 文档分隔线：008-javascript/027-WebAPIBrowserInterface.md ============ -->

# JavaScript Web API 浏览器接口语法速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## fetch 请求

**基本写法：基础请求**
`fetch(<url>, [<选项>])`
```javascript
// 返回 Promise<Response>
const res = await fetch("/api/user");
const data = await res.json();
```

---

**基本写法：带请求配置**
`fetch(<url>, { method, headers, body })`
```javascript
// POST JSON
const res = await fetch("/api/user", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: "Tom" }),
});
```

---

**基本写法：错误与状态处理**
`<res>.ok` | `<res>.status`
```javascript
// fetch 仅在网络错误时 reject
if (!res.ok) throw new Error(`HTTP ${res.status}`);
```

---

**基本写法：中止请求**
`new AbortController()` | `signal: <signal>`
```javascript
// 超时或取消请求
const ctrl = new AbortController();
setTimeout(() => ctrl.abort(), 5000);
const res = await fetch("/api", { signal: ctrl.signal });
```

---

## 网络请求与流

**基本写法：读取响应流**
`<res>.body.getReader()`
```javascript
// 流式读取大响应
const reader = res.body.getReader();
while (true) {
  const { done, value } = await reader.read();
  if (done) break;
  console.log(value); // Uint8Array 分块
}
```

---

## IntersectionObserver 可视区观察

**基本写法：观察元素可见性**
`new IntersectionObserver(<回调>, [<选项>])`
```javascript
// 元素进入/离开视口触发
const ob = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) console.log("可见", e.target);
  });
}, { threshold: 0.5 });
ob.observe(document.querySelector(".box"));
```

---

**基本写法：取消观察**
`<observer>.unobserve(<元素>)` | `<observer>.disconnect()`
```javascript
// 停止观察单个或全部
ob.unobserve(el);
ob.disconnect();
```

---

## MutationObserver DOM 变动

**基本写法：监听 DOM 变化**
`new MutationObserver(<回调>)`
```javascript
// 子节点/属性变化回调
const ob = new MutationObserver(muts => {
  muts.forEach(m => console.log(m.type, m.target));
});
ob.observe(document.body, {
  childList: true,     // 子节点变动
  subtree: true,       // 含后代
  attributes: true,    // 属性变动
  characterData: true, // 文本变动
});
```

---

## ResizeObserver 尺寸观察

**基本写法：监听元素尺寸**
`new ResizeObserver(<回调>)`
```javascript
// 元素尺寸变化回调
const ob = new ResizeObserver(entries => {
  entries.forEach(e => console.log(e.contentRect.width));
});
ob.observe(document.querySelector(".box"));
```

---

## LocalStorage 与 SessionStorage

**基本写法：存储读取**
`localStorage.setItem(<键>, <值>)`
```javascript
// 仅存字符串，对象需序列化
localStorage.setItem("user", JSON.stringify({ id: 1 }));
const user = JSON.parse(localStorage.getItem("user"));
localStorage.removeItem("user");
localStorage.clear();
```

---

**基本写法：sessionStorage 会话存储**
`sessionStorage.setItem(<键>, <值>)`
```javascript
// 标签页关闭即清除
sessionStorage.setItem("token", "abc");
sessionStorage.getItem("token");
```

---

## 定时器

**基本写法：延时与循环**
`setTimeout(<回调>, <毫秒>)` | `setInterval(<回调>, <毫秒>)`
```javascript
const t1 = setTimeout(() => {}, 1000);
const t2 = setInterval(() => {}, 1000);
clearTimeout(t1);
clearInterval(t2);
```

---

**基本写法：requestAnimationFrame**
`requestAnimationFrame(<回调>)`
```javascript
// 与刷新率同步的动画帧
let id = requestAnimationFrame(loop);
function loop(t) {
  // t 为高精度时间戳
  id = requestAnimationFrame(loop);
}
cancelAnimationFrame(id);
```

---

## URL 与 History

**基本写法：URL 解析**
`new URL(<url>, [<base>])`
```javascript
// 解析与拼接 URL
const u = new URL("/api", "https://a.com");
u.searchParams.set("q", "js");
u.toString(); // https://a.com/api?q=js
```

---

**基本写法：历史记录操作**
`history.pushState(<state>, <标题>, <url>)`
```javascript
// 不刷新页面改地址
history.pushState({ page: 1 }, "", "/page1");
history.replaceState({}, "", "/page2");
history.back();
window.onpopstate = e => console.log(e.state);
```

---

## Clipboard 剪贴板

**基本写法：读写剪贴板**
`navigator.clipboard.writeText(<文本>)`
```javascript
// 需 HTTPS 与用户手势
await navigator.clipboard.writeText("复制内容");
const text = await navigator.clipboard.readText();
```

---

## BroadcastChannel 跨页通信

**基本写法：同源页面广播**
`new BroadcastChannel(<频道名>)`
```javascript
// 同源多标签页通信
const ch = new BroadcastChannel("evt");
ch.postMessage({ hello: 1 });
ch.onmessage = e => console.log(e.data);
ch.close();
```

---



<!-- ============ 文档分隔线：008-javascript/028-SymbolIteratorProtocol.md ============ -->

# JavaScript Symbol 与迭代协议语法速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Symbol 基础

**基本写法：创建唯一值**
`Symbol([<描述>])`
```javascript
// 每次创建独一无二，不可强制转换
const s1 = Symbol("id");
const s2 = Symbol("id");
s1 === s2; // false
s1.description; // "id"
```

---

**基本写法：作为对象键**
`{ [<symbol>]: <值> }`
```javascript
// Symbol 键不会被 for-in/Object.keys 枚举
const KEY = Symbol("hidden");
const obj = { [KEY]: "secret", name: "Tom" };
Object.keys(obj);          // ["name"]
Object.getOwnPropertySymbols(obj); // [Symbol(hidden)]
```

---

**基本写法：全局注册**
`Symbol.for(<键>)` | `Symbol.keyFor(<symbol>)`
```javascript
// 同键返回同一 Symbol
const a = Symbol.for("shared");
const b = Symbol.for("shared");
a === b;            // true
Symbol.keyFor(a);   // "shared"
```

---

## 内置 Symbol

**基本写法：常用内置 Symbol**
`Symbol.<wellKnown>`
```javascript
Symbol.iterator;       // 自定义迭代器
Symbol.asyncIterator;  // 自定义异步迭代器
Symbol.toPrimitive;    // 类型转换
Symbol.toStringTag;    // toString 标识
Symbol.hasInstance;    // instanceof 行为
```

---

## 迭代协议

**基本写法：iterable 协议**
`[Symbol.iterator]() { return <iterator> }`
```javascript
// 实现 Symbol.iterator 即可迭代
const range = {
  from: 1, to: 3,
  [Symbol.iterator]() {
    let cur = this.from;
    const last = this.to;
    return {
      next() {
        return cur <= last
          ? { value: cur++, done: false }
          : { value: undefined, done: true };
      }
    };
  }
};
[...range]; // [1, 2, 3]
```

---

**基本写法：iterator 协议**
`next() { return { value, done } }`
```javascript
// 迭代器对象须有 next 方法
const it = range[Symbol.iterator]();
it.next(); // { value: 1, done: false }
it.next(); // { value: 2, done: false }
it.next(); // { value: 3, done: false }
it.next(); // { value: undefined, done: true }
```

---

**基本写法：return 提前终止**
`return(<值>) { ... }`
```javascript
// for-of 提前 break/throw 时调用
return {
  next() { /* ... */ },
  return(v) { console.log("清理"); return { value: v, done: true }; }
};
```

---

## 生成器函数

**基本写法：声明生成器**
`function* <名>() { yield <值> }`
```javascript
// 生成器函数返回迭代器
function* gen() {
  yield 1;
  yield 2;
  yield 3;
}
const it = gen();
it.next(); // { value: 1, done: false }
[...gen()]; // [1, 2, 3]
```

---

**基本写法：yield 委托**
`yield* <可迭代>`
```javascript
// 委托给另一个可迭代对象
function* inner() { yield "a"; yield "b"; }
function* outer() { yield 1; yield* inner(); yield 2; }
[...outer()]; // [1, "a", "b", 2]
```

---

**基本写法：双向通信**
`<变量> = yield <值>`
```javascript
// next 参数回传到 yield
function* dialog() {
  const x = yield 1;
  console.log("收到", x); // 收到 hi
}
const it = dialog();
it.next();      // { value: 1 }
it.next("hi");  // 输出 收到 hi
```

---

**基本写法：生成器作迭代器**
`{ [Symbol.iterator]: function* () {} }`
```javascript
// 用生成器简化可迭代对象
const obj = {
  data: [10, 20, 30],
  *[Symbol.iterator]() {
    for (const v of this.data) yield v;
  }
};
[...obj]; // [10, 20, 30]
```

---

## 异步迭代

**基本写法：异步可迭代协议**
`[Symbol.asyncIterator]() { return { next() } }`
```javascript
// 异步迭代器返回 Promise
const src = {
  async *[Symbol.asyncIterator]() {
    yield 1;
    yield 2;
  }
};
for await (const v of src) console.log(v);
```

---

**基本写法：for await 遍历**
`for await (const <v> of <异步可迭代>) {}`
```javascript
// 消费异步迭代器
async function* lines() {
  yield "a"; yield "b";
}
for await (const line of lines()) {
  console.log(line);
}
```

---

## 默认可迭代对象

**基本写法：内置可迭代类型**
`for (const <v> of <可迭代>) {}`
```javascript
// Array Map Set String arguments NodeLists 均可迭代
for (const x of [1, 2]) {}
for (const [k, v] of new Map()) {}
for (const c of "abc") {}
```

---

## 解构与展开

**基本写法：展开可迭代**
`[...<可迭代>]`
```javascript
// 任何可迭代对象都能展开
const arr = [...new Set([1, 2]), ...range];
```

---



<!-- ============ 文档分隔线：008-javascript/029-PackageManagerCommands.md ============ -->

# JavaScript 包管理命令速查（npm/pnpm/yarn）

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 初始化项目

**基本写法：生成 package.json**
`npm init [-y]` | `pnpm init` | `yarn init [-y]`
```bash
# -y 使用默认值跳过提问
npm init -y
pnpm init
yarn init -y
```

---

## 安装依赖

**基本写法：安装全部依赖**
`npm install` | `pnpm install` | `yarn`
```bash
# 读取 lock 文件安装
npm install        # npm
pnpm install       # pnpm
yarn               # yarn
```

---

**基本写法：添加单个包**
`npm install <包> [-D|-g]`
```bash
# -D 开发依赖 -g 全局
npm install lodash            # 生产依赖
npm install -D vitest         # 开发依赖
npm install -g typescript     # 全局安装
pnpm add lodash
pnpm add -D vitest
yarn add lodash
yarn add --dev vitest
```

---

**基本写法：指定版本安装**
`npm install <包>@<版本>`
```bash
# 版本范围
npm install react@18.2.0
npm install react@"^18.0.0"
npm install react@latest
pnpm add react@18.2.0
yarn add react@18.2.0
```

---

## 卸载与更新

**基本写法：卸载依赖**
`npm uninstall <包>` | `pnpm remove <包>` | `yarn remove <包>`
```bash
npm uninstall lodash
pnpm remove lodash
yarn remove lodash
```

---

**基本写法：更新依赖**
`npm update [<包>]` | `pnpm update [<包>]` | `yarn upgrade [<包>]`
```bash
npm update react
pnpm update react
yarn upgrade react
```

---

## 运行脚本

**基本写法：执行 package.json scripts**
`npm run <脚本>` | `pnpm <脚本>` | `yarn <脚本>`
```bash
# package.json: "scripts": { "dev": "vite" }
npm run dev
pnpm dev          # pnpm 可省略 run
yarn dev          # yarn 也可省略 run
```

---

**基本写法：npx 执行本地命令**
`npx <命令>`
```bash
# 执行 node_modules/.bin 下的命令
npx tsc --noEmit
npx create-vite my-app
pnpm dlx create-vite my-app   # pnpm 等价
yarn dlx create-vite my-app
```

---

## 锁文件与严格安装

**基本写法：按 lock 文件严格安装**
`npm ci` | `pnpm install --frozen-lockfile` | `yarn install --frozen-lockfile`
```bash
# CI 环境推荐，不修改 lock
npm ci
pnpm install --frozen-lockfile
yarn install --frozen-lockfile
```

---

## 工作区 Monorepo

**基本写法：定义工作区**
`<根 package.json>: "workspaces": ["packages/*"]`
```json
{
  "private": true,
  "workspaces": ["packages/*", "apps/*"]
}
```

---

**基本写法：工作区命令**
`npm -w <包> <命令>` | `pnpm --filter <包> <命令>` | `yarn workspace <包> <命令>`
```bash
# 在指定工作区执行
npm -w @a/core run build
pnpm --filter @a/core build
yarn workspace @a/core build
```

---

**基本写法：安装工作区包**
`npm -w <包A> i <包B>` | `pnpm add <包B> --filter <包A>`
```bash
# 给 app 安装内部包
npm -w apps/web i @a/core
pnpm add @a/core --filter apps/web
yarn workspace apps/web add @a/core
```

---

## 查询信息

**基本写法：查看包信息**
`npm view <包> [<字段>]`
```bash
npm view react version
npm view react versions --json
pnpm view react version
```

---

**基本写法：列出依赖树**
`npm ls [<包>]` | `pnpm list` | `yarn list`
```bash
npm ls react
npm ls --depth=1
pnpm why react    # 解释为何依赖
```

---

## 清理与缓存

**基本写法：清理 node_modules**
`rm -rf node_modules` + 重装
```bash
# 彻底重装
rm -rf node_modules package-lock.json
npm install
```

---

**基本写法：缓存管理**
`npm cache clean --force` | `pnpm store prune`
```bash
npm cache clean --force
pnpm store prune
yarn cache clean
```

---

## 发布与镜像

**基本写法：设置镜像源**
`npm config set registry <url>`
```bash
npm config set registry https://registry.npmmirror.com
npm config get registry
pnpm config set registry https://registry.npmmirror.com
```

---

**基本写法：发布包**
`npm publish`
```bash
npm publish           # 发布到 registry
npm publish --access public  # 公开 scoped 包
npm deprecate <包>@<版本> "废弃说明"
```

---

## pnpm 硬链接特性

**基本写法：pnpm 全局存储**
`pnpm config set store-dir <路径>`
```bash
# pnpm 用硬链接复用全局存储，节省磁盘
pnpm config get store-dir
pnpm install   # 自动链接 store
```

---



<!-- ============ 文档分隔线：008-javascript/030-ConsoleAPI.md ============ -->

# JavaScript console API 语法速查

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础输出

**基本写法：log 多参数**
`console.log(<值>, [<值>...])`
```javascript
// 多参数空格分隔输出
console.log("id:", 1, "user:", { name: "Tom" });
```

---

**基本写法：info / debug / warn / error**
`console.<level>(<值>)`
```javascript
// 不同级别，渲染样式不同
console.info("信息");
console.debug("调试");
console.warn("警告");
console.error("错误");
```

---

## 格式化输出

**基本写法：格式占位符**
`console.log("<格式串>", <值>)`
```javascript
// %s 字符串 %d/%i 整数 %f 浮点 %o 对象 %c 样式
console.log("%s 有 %d 岁", "Tom", 18);
console.log("%c红色文字", "color:red;font-weight:bold");
```

---

**基本写法：对象表格**
`console.table(<数据>, [<列>])`
```javascript
// 数组或对象渲染为表格
console.table([{ id: 1, name: "A" }, { id: 2, name: "B" }]);
console.table(users, ["name"]);
```

---

**基本写法：分组输出**
`console.group([<标题>])` | `console.groupEnd()`
```javascript
// 折叠分组
console.group("用户信息");
console.log("name: Tom");
console.groupEnd();
// 默认展开
console.groupCollapsed("详情");
console.groupEnd();
```

---

## 计时与计数

**基本写法：计时器**
`console.time(<标签>)` | `console.timeEnd(<标签>)`
```javascript
// 测量代码执行耗时
console.time("loop");
for (let i = 0; i < 1e6; i++) {}
console.timeEnd("loop"); // loop: 1.23ms
```

---

**基本写法：计数器**
`console.count([<标签>])`
```javascript
// 统计调用次数
function fn() { console.count("fn"); }
fn(); fn(); // fn: 1 / fn: 2
console.countReset("fn");
```

---

## 断言与堆栈

**基本写法：断言**
`console.assert(<条件>, [<消息>])`
```javascript
// 条件为 false 才输出错误
console.assert(age >= 0, "年龄不能为负");
```

---

**基本写法：打印堆栈**
`console.trace([<消息>])`
```javascript
// 输出调用栈
function a() { b(); }
function b() { console.trace("位置"); }
a();
```

---

## 目录树与清屏

**基本写法：对象目录树**
`console.dir(<对象>, [<选项>])`
```javascript
// 以可展开树形显示
console.dir(document.body, { depth: 2, colors: true });
```

---

**基本写法：清屏**
`console.clear()`
```javascript
// 清空控制台
console.clear();
```

---

## 性能分析

**基本写法：性能采样**
`console.profile(<标签>)` | `console.profileEnd(<标签>)`
```javascript
// 配合浏览器性能分析器
console.profile("render");
render();
console.profileEnd("render");
```

---

**基本写法：时间戳**
`console.timeStamp(<标签>)`
```javascript
// 在性能时间轴打标记
console.timeStamp("start-render");
```

---

## Node.js 专属

**基本写法：控制台颜色（Node）**
`console.log("\x1b[31m%s\x1b[0m", "红")`
```javascript
// ANSI 转义码着色
// 31 红 32 绿 33 黄 34 蓝 0 重置
console.log("\x1b[32m成功\x1b[0m");
```

---

## 条件与流式

**基本写法：按级别条件输出**
`console.log(<值>)`
```javascript
// 自定义封装按级别过滤
const log = (level, ...args) => {
  if (LEVELS[level] >= LEVELS[config.level]) console[level](...args);
};
```

---

## 推荐实践

**基本写法：生产环境屏蔽**
`console.log(<值>)`
```javascript
// 构建时移除或重写
if (process.env.NODE_ENV === "production") {
  console.log = console.info = () => {};
}
```

---
