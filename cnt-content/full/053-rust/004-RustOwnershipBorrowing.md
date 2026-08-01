---
order: 4
title: 所有权与借用
module: rust
category: Rust
difficulty: beginner
description: 'Rust 核心机制：所有权规则、移动与复制、借用与引用、切片'
author: fanquanpp
updated: '2026-08-01'
related:
  - rust/003-RustBasicSyntax
  - rust/005-RustStructEnumMatch
prerequisites:
  - rust/003-RustBasicSyntax
---

## 1. 为什么需要所有权

C/C++ 靠程序员手动管理内存（malloc/free、new/delete），容易产生悬垂指针、double-free；Java/Go 靠垃圾回收（GC）自动回收，但引入停顿与内存占用。Rust 选择了第三条路：**所有权（Ownership）**——在编译期确定每个值的生命周期，既无 GC 也无手动释放，安全且零开销。

Rust 的承诺：所有内存错误（空指针、悬垂引用、数据竞争、缓冲区溢出）在编译期就被拒绝。

## 2. 所有权三规则

1. 每个值有且只有一个所有者（owner）变量。
2. 所有者离开作用域时，值被自动释放（drop）。
3. 值可以被转移（move）给新的所有者，旧所有者随即失效。

```rust
fn main() {
    let s = String::from("hello"); // s 是所有者
    println!("{}", s.len());
} // 此处 s 离开作用域，String 的内存自动释放
```

讲解：无需手动 free，离开作用域即析构。栈上的整数等类型同样适用，只是释放成本趋近于零。

## 3. 移动（Move）与复制（Copy）

### 3.1 移动语义

```rust
let s1 = String::from("hello");
let s2 = s1;              // 所有权转移（move）
// println!("{s1}");      // 错误：s1 已失效
println!("{s2}");         // 正常
```

讲解：`let s2 = s1` 没有深拷贝堆数据，只是把"指针+长度+容量"这三块栈数据转移给 s2，并让 s1 失效。这避免了 double-free，且零拷贝成本。编译器会阻止继续使用 s1。

### 3.2 Copy 类型

像整数、布尔、浮点这样的"纯栈上数据"，赋值是**按位复制**，不会移动：

```rust
let a = 5;
let b = a;   // a 仍然可用，因为 i32 实现了 Copy
println!("{a} {b}"); // 输出 5 5
```

讲解：实现了 `Copy` trait 的类型（标量、元组内全 Copy、`&T` 引用）赋值即复制；而 `String`、`Vec` 等堆类型实现的是 `Move`。规则：**实现 Copy 的类型赋值后原变量仍可用，否则原变量失效**。

函数传参与返回同理：

```rust
fn take(s: String) { /* 消耗传入的所有权 */ }
fn give() -> String { String::from("new") }

fn main() {
    let s = String::from("x");
    take(s);            // s 的所有权被函数消耗
    // println!("{s}"); // 错误

    let t = give();     // 返回值转移所有权给 t
}
```

讲解：把所有权交给函数（消耗）、让函数返回所有权（产出），是 Rust 管理资源的基本节奏。

## 4. 借用与引用

不想转移所有权、只想"借来看看"，用引用 `&T`：

```rust
fn calc_len(s: &String) -> usize {
    s.len()          // 只读访问，不获取所有权
}

fn main() {
    let s = String::from("hello");
    let len = calc_len(&s);
    println!("{len}");       // s 仍可用
}
```

讲解：`&s` 创建不可变引用（借用），借出期间原所有者不受影响，借完自动归还。可以同时存在**多个**不可变引用。

### 4.1 可变借用

```rust
fn push_hello(s: &mut String) {
    s.push_str(", world");
}

fn main() {
    let mut s = String::from("hello");
    push_hello(&mut s);
    println!("{s}");
}
```

讲解：可变引用 `&mut T` 必须配合 `mut` 变量使用。核心约束：**同一时刻，一个值要么有多个不可变借用，要么只有一个可变借用**——这条规则在编译期消灭了数据竞争。

```rust
let mut s = String::from("hi");
let r1 = &s;          // 不可变借用，可以
let r2 = &s;          // 多个不可变借用，可以
let r3 = &mut s;      // 错误：已有不可变借用时不能再创建可变借用
```

讲解：借用规则（别名与变异的权衡）：不可变借用可以并行（读读不冲突），可变借用独占（写必须独占）。

### 4.2 借用作用域

```rust
let mut s = String::from("hi");
let r = &s;              // r 的借用开始
println!("{r}");         // 最后一次使用 r
let m = &mut s;          // 此时 r 已不再使用，可以创建可变借用
m.push_str("!");
```

讲解：借用结束于**最后一次使用**（NLL，非词法生命周期）。上例中 r 打印后就不再被使用，可变借用随后合法。

## 5. 切片（Slice）

切片是对连续数据的一段**借用**视图，无所有权。字符串切片 `&str` 是最常见的：

```rust
let s = String::from("hello world");
let hello = &s[0..5];     // "hello"
let world = &s[6..];      // "world"（6 到末尾）
println!("{hello} {world}");
```

讲解：`&s[0..5]` 是对 String 的借用，范围是字节索引（注意：中文字符占 3 字节，按字节切可能 panic，多字节边界需谨慎）。字符串字面量本身就是 `&str`：

```rust
let greeting: &str = "你好";  // "你好" 是编译期内置的 &str
```

数组切片：

```rust
let arr = [1, 2, 3, 4, 5];
let mid = &arr[1..4];       // [2, 3, 4]，类型 &[i32; ...] 的切片 &[i32]
for v in mid {
    println!("{v}");
}
```

讲解：函数接收参数时优先用切片而非 `&String`/`&Vec`，因为 `&str`/`&[T]` 能同时接收字面量、String、数组，通用性更强：

```rust
fn first_word(s: &str) -> &str {
    match s.find(' ') {
        Some(i) => &s[..i],
        None => s,
    }
}

fn main() {
    let s = String::from("hello world");
    println!("{}", first_word(&s));    // 传 &String 可自动转为 &str
    println!("{}", first_word("hi ok")); // 直接传字面量
}
```

讲解：`&String` 可自动强转为 `&str`（deref coercion），因此参数写 `&str` 最灵活；返回的切片生命周期与输入绑定，保证不会悬垂。

## 6. 综合示例：统计单词数

```rust
fn count_words(text: &str) -> usize {
    text.split_whitespace().count()
}

fn main() {
    let text = String::from("Rust ownership is safe");
    println!("{}", count_words(&text)); // 输出 4
    println!("{}", count_words("你好 Rust")); // 输出 2
}
```

讲解：全程只借用不拷贝；`split_whitespace` 返回迭代器直接数个数，零分配。所有权系统的收益在此体现：简洁、安全、无 GC、无手动释放。

## 7. 常见错误与对策

| 编译错误 | 原因 | 对策 |
| --- | --- | --- |
| use of moved value | 使用了已转移所有权的变量 | 改用引用传参，或 clone 一份 |
| cannot borrow as mutable | 同时存在不可变与可变借用 | 缩小借用作用域，或调整借用顺序 |
| cannot move out of borrowed content | 尝试从借用中拿走所有权 | 用 clone 或返回引用 |
| temporary value dropped | 引用指向了临时值 | 用变量持有临时值再借用 |

通用调试手段：遇到借用错误时，按编译器提示信息（E0502/E0505 等）逐条阅读，rust-analyzer 会标注问题行；必要时用 `clone()` 快速通过，再回头优化为引用。

## 8. 参考资源

TRPL 第 4 章（所有权）：https://kaisery.github.io/trpl-zh-cn/ch04-00-understanding-ownership.html

Rust 借用检查器详解（官方博客）：https://blog.rust-lang.org/inside-rust/2022/11/03/nll-on-stable.html

Rust 语言参考（所有权）：https://doc.rust-lang.org/reference/ownership.html

## 9. 小结

所有权三规则 + 借用两条约束（不可变可并行、可变要独占）+ 切片视图，构成了 Rust 内存安全的地基。理解"移动 vs 复制""借用 vs 拥有"两组对立概念，就能读懂编译器的大部分报错。下一步学习结构体、枚举与模式匹配，把这些机制组合成真实的数据结构。
