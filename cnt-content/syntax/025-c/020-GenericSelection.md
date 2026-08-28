# C 泛型选择 _Generic

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## _Generic 基础

**基本写法：泛型选择表达式**
`_Generic(<表达式>, <类型>: <结果>, default: <默认>)`
```c
// 根据表达式类型选择结果
const char* name = _Generic(x,
    int: "int",
    double: "double",
    default: "other");
```

---

**基本写法：多类型分支**
`_Generic(<表达式>, <类型1>: <值1>, <类型2>: <值2>)`
```c
// 编译期类型分派
int s = _Generic(arr,
    int*: sizeof(int),
    char*: sizeof(char),
    default: 0);
```

---

## 泛型宏

**基本写法：类型感知打印宏**
`#define <宏名>(<x>) _Generic((<x>), ...)`
```c
// 根据类型选择打印格式
#define print_val(x) _Generic((x), \
    int: printf("%d\n", (x)), \
    double: printf("%f\n", (x)), \
    char*: printf("%s\n", (x)))
```

---

**基本写法：泛型打印调用**
`<宏名>(<值>);`
```c
// 调用自动分派
print_val(42);
print_val(3.14);
```

---

## 泛型函数分发

**基本写法：泛型函数选择**
`#define <宏名>(<x>) _Generic((<x>), <类型>: <函数>, ...)`
```c
// 类型对应的实现函数
int add_i(int a, int b);
double add_d(double a, double b);
#define add(x, y) _Generic((x), \
    int: add_i, \
    double: add_d)((x), (y))
```

---

**基本写法：调用泛型函数**
`<宏名>(<参数1>, <参数2>);`
```c
// 自动选择 int 或 double 版本
int r1 = add(1, 2);
double r2 = add(1.0, 2.0);
```

---

## 类型分组

**基本写法：用 default 兜底**
`_Generic(<表达式>, <类型>: <值>, default: <默认值>)`
```c
// 未匹配类型走 default
int kind = _Generic(x, int: 1, double: 2, default: 0);
```

---

**基本写法：区分有符号无符号**
`_Generic(<表达式>, int: ..., unsigned int: ...)`
```c
// 分别处理有符号无符号
const char* s = _Generic(x,
    int: "signed",
    unsigned int: "unsigned");
```

---

## 实用示例

**基本写法：安全的数组大小宏**
`#define ARR_LEN(<a>) (sizeof(<a>) / sizeof((<a>)[0]))`
```c
// 配合 _Generic 校验类型
#define arr_len(a) _Generic((a), \
    int*: sizeof(a)/sizeof(int), \
    default: sizeof(a)/sizeof((a)[0]))
```

---

**基本写法：类型名查询宏**
`#define TYPE_NAME(<x>) _Generic((<x>), ...)`
```c
// 返回类型名字符串
#define TYPE_NAME(x) _Generic((x), \
    _Bool: "bool", \
    char: "char", \
    signed char: "signed char", \
    short: "short", \
    int: "int", \
    long: "long", \
    long long: "long long", \
    float: "float", \
    double: "double", \
    default: "unknown")
```

---

## 复合类型

**基本写法：处理指针类型**
`_Generic(<表达式>, <类型>*: <分支>)`
```c
// 区分指针与普通类型
const char* s = _Generic(x,
    int*: "pointer",
    int: "value",
    default: "?");
```

---

**基本写法：处理 const**
`_Generic(<表达式>, const <类型>: <分支>, <类型>: <分支>)`
```c
// const 与非 const 视为不同类型
const char* s = _Generic(x,
    const int: "const int",
    int: "int");
```

---

## 注意事项

**基本写法：_Generic 是编译期选择**
`_Generic(<表达式>, ...)  // 仅求值类型不求值表达式`
```c
// 副作用表达式仅类型被使用
int r = _Generic(side_effect(), int: 0);
// side_effect 不会实际调用
```

---

**基本写法：数组退化为指针**
`_Generic(<数组名>, <类型>*: ...)`
```c
// 数组在 _Generic 中退化为指针
int arr[10];
const char* s = _Generic(arr, int*: "ptr", default: "other");
```
