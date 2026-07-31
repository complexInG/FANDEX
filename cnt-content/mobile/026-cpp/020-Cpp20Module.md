# C++20 模块

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 模块声明

**基本写法：声明一个模块接口单元**
`export module <模块名>;`
```cpp
// 定义名为 math 的模块接口
export module math;
```

---

**基本写法：声明模块分区**
`module <模块名>:<分区名>;`
```cpp
// 模块 math 的内部实现分区
module math:impl;
```

---

**基本写法：声明模块实现单元**
`module <模块名>;`
```cpp
// 模块 math 的实现单元，不导出声明
module math;
```

---

## 导出声明

**基本写法：导出函数**
`export <返回类型> <函数名>(<参数>);`
```cpp
// 导出加法函数供外部使用
export int add(int a, int b);
```

---

**基本写法：导出类**
`export class <类名> { };`
```cpp
// 导出整个类
export class Calculator {
public:
    int sub(int a, int b);
};
```

---

**基本写法：导出命名空间**
`export namespace <命名空间名> { }`
```cpp
// 导出整个命名空间
export namespace geo {
    double pi = 3.14159;
    double area(double r);
}
```

---

**基本写法：分组导出**
`export { <声明1>; <声明2>; }`
```cpp
// 一次性导出多个声明
export {
    int mul(int a, int b);
    int div(int a, int b);
}
```

---

## 导入模块

**基本写法：导入模块**
`import <模块名>;`
```cpp
// 导入 math 模块以使用其导出内容
import math;
```

---

**基本写法：导入头文件单元**
`import <头文件名>;`
```cpp
// 将头文件作为模块单元导入
import <iostream>;
```

---

**基本写法：全局模块片段声明头文件**
`module; <头文件包含> export module <模块名>;`
```cpp
// 全局片段中包含传统头文件
module;
#include <cstdio>
export module logger;
```

---

## 模块分区组合

**基本写法：导入本模块分区**
`import :<分区名>;`
```cpp
// 在主接口中导入分区
export module math;
import :impl;
```

---

**基本写法：导出分区**
`export import :<分区名>;`
```cpp
// 将分区的导出内容重新导出
export module math;
export import :core;
```

---

## 编译与使用

**基本写法：编译模块接口**
`g++ -std=c++20 -fmodules-ts -c <文件>.cpp`
```cpp
// 编译模块接口单元生成 gcm 文件
g++ -std=c++20 -fmodules-ts -c math.cpp
```

---

**基本写法：MSVC 编译模块**
`cl /std:c++20 /c /interface <文件>.cpp`
```cpp
// MSVC 编译模块接口单元
cl /std:c++20 /c /interface math.cpp
```
