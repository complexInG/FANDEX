# C 函数指针与回调

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 函数指针基础

**基本写法：声明函数指针**
`<返回类型> (*<指针名>)(<参数>);`
```c
// 声明指向 int(int) 函数的指针
int (*fp)(int);
```

---

**基本写法：赋值函数地址**
`<指针名> = <函数名>;` 或 `<指针名> = &<函数名>;`
```c
// 函数名即地址
int sq(int x) { return x * x; }
fp = sq;
```

---

**基本写法：通过指针调用**
`<指针名>(<参数>);` 或 `(*<指针名>)(<参数>);`
```c
// 两种调用方式等价
int r = fp(5);
```

---

## 函数指针类型别名

**基本写法：typedef 别名**
`typedef <返回类型> (*<别名>)(<参数>);`
```c
// 定义函数指针类型
typedef int (*BinOp)(int, int);
BinOp op = add;
```

---

**基本写法：使用别名声明变量**
`<别名> <变量> = <函数>;`
```c
// 用别名声明更清晰
BinOp op = add;
int r = op(2, 3);
```

---

## 回调函数

**基本写法：回调参数**
`void <函数>(<参数>, <返回类型> (*<回调>)(<回调参数>));`
```c
// 函数接收回调
void process(int x, int (*cb)(int)) {
    int r = cb(x);
}
```

---

**基本写法：传递函数作为回调**
`<函数>(<参数>, <回调函数>);`
```c
// 传入函数名作为回调
process(5, sq);
```

---

**基本写法：回调上下文指针**
`void <函数>(void* <ctx>, void (*<回调>)(void*, int));`
```c
// 携带上下文的回调
void iterate(int* arr, int n, void* ctx, void (*cb)(void*, int)) {
    for (int i = 0; i < n; i++) cb(ctx, arr[i]);
}
```

---

## 函数指针数组

**基本写法：函数指针数组**
`<返回类型> (*<数组名>[<数量>])(<参数>);`
```c
// 存储多个函数指针
int (*ops[4])(int, int) = {add, sub, mul, div};
```

---

**基本写法：通过索引调用**
`<数组名>[<索引>](<参数>);`
```c
// 选择调用对应函数
int r = ops[0](2, 3);
```

---

## 跳转表

**基本写法：跳转表实现**
`<别名> <表名>[] = { <函数1>, <函数2>, ... };`
```c
// 用枚举索引选择操作
typedef int (*Op)(int, int);
Op table[] = { add, sub, mul, div };
int r = table[OP_ADD](a, b);
```

---

## qsort 回调

**基本写法：qsort 比较函数**
`int <比较>(const void* <a>, const void* <b>);`
```c
// 标准库排序比较函数
int cmp(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}
```

---

**基本写法：调用 qsort**
`qsort(<数组>, <数量>, <大小>, <比较函数>);`
```c
// 排序整型数组
qsort(arr, n, sizeof(int), cmp);
```

---

## bsearch 回调

**基本写法：二分查找**
`bsearch(<关键字>, <数组>, <数量>, <大小>, <比较函数>);`
```c
// 在有序数组中查找
int key = 42;
int* found = bsearch(&key, arr, n, sizeof(int), cmp);
```

---

## 返回函数指针

**基本写法：函数返回函数指针**
`<别名> <函数名>(<参数>);`
```c
// 根据条件返回不同操作
BinOp select_op(char c) {
    if (c == '+') return add;
    return sub;
}
```

---

## 复杂声明

**基本写法：指向返回函数指针的函数的指针**
`<返回类型> (*(*<指针>)(<参数>))(<参数>);`
```c
// 指向返回 BinOp 的函数的指针
BinOp (*selector)(char) = select_op;
```

---

## 注意事项

**基本写法：函数指针可为 NULL**
`if (<指针> != NULL) <指针>(<参数>);`
```c
// 调用前检查有效性
if (cb != NULL) cb(data);
```

---

**基本写法：函数指针类型转换**
`(void (*)(void))<函数>`
```c
// 转为通用函数指针类型
void (*generic)(void) = (void (*)(void))cb;
```
