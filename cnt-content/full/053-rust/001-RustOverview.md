---
order: 1
title: Rust 语言概述与学习路线
module: rust
category: Rust
difficulty: beginner
description: 'Rust 编程语言概述：设计目标、所有权与借用、Cargo 生态、学习路线与工程实践'
author: fanquanpp
updated: '2026-08-01'
related:
  - c/枚举与typedef
  - cpp/模板
  - go/并发
prerequisites:
  - getting-started/编程基础
---

## 1. Rust 是什么

Rust 是一门系统级编程语言，由 Mozilla 资助开发，2015 年发布 1.0 版本。它的设计目标是在不牺牲性能的前提下提供内存安全：所有内存错误（空指针、悬垂引用、数据竞争、缓冲区溢出）都在编译期被拒绝，而不是等到运行时崩溃或被攻击者利用。

Rust 的 slogan 是“性能、可靠、生产力”（Performance, Reliability, Productivity）。它没有垃圾回收器（GC），也没有运行时开销，却通过所有权（ownership）系统在编译期管理内存。这使它成为 C/C++ 的有力竞争者，并被 Linux 内核、Windows、Cloudflare、Discord 等大型项目采用。

## 2. 为什么需要 Rust

### 2.1 C/C++ 的安全困境

C 语言自 1972 年以来一直是系统编程的主力，但内存安全漏洞（缓冲区溢出、use-after-free）占所有安全漏洞的相当比例。微软与 Google 的统计均显示，其产品中约 70% 的安全漏洞与内存安全相关。C++ 提供了 RAII 与智能指针，但默认仍然不安全：裸指针、手动 delete、迭代器失效仍然可以轻易触发未定义行为。

### 2.2 托管语言的性能天花板

Java、Go、Python 等语言通过 GC 或运行时获得安全性与开发效率，但代价是内存占用与延迟不可控。对操作系统、数据库引擎、游戏引擎、嵌入式设备而言，GC 停顿与运行时体积不可接受。

Rust 的定位是填补空白：拥有 C 级别的性能，同时拥有比 Java 更强的编译期安全保障。

## 3. 核心概念速览

### 3.1 所有权（Ownership）

每个值在任意时刻只有一个所有者（owner）。当所有者离开作用域，值被自动释放（drop）。这替代了 GC 与手动 free。

```rust
fn main() {
    let s = String::from("hello"); // s 拥有字符串
    let t = s;                     // 所有权转移（move）到 t
    // println!("{s}");            // 错误：s 已失效
    println!("{t}");               // t 可以正常使用
}
```

讲解：`let t = s` 不发生深拷贝，而是把所有权从 s 转移给 t；此后 s 不可再使用。编译器在编译期强制执行这一规则，杜绝 double-free 与 use-after-free。

### 3.2 借用（Borrowing）

不转移所有权，而是临时借用：`&T` 不可变借用（可多个），`&mut T` 可变借用（唯一）。

```rust
fn len(s: &String) -> usize {
    s.len() // 只读借用，不获取所有权
}

fn main() {
    let s = String::from("hello");
    println!("{}", len(&s)); // 借用后 s 仍可用
}
```

讲解：借用规则在编译期检查：同一数据不能同时存在可变借用与不可变借用。这一规则让 Rust 在编译期就消除了数据竞争。

### 3.3 生命周期（Lifetime）

引用必须在其指向的值存活期间有效。多数情况下编译器能自动推断；复杂场景需要标注。

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

讲解：`<'a>` 声明生命周期参数，表示返回值引用与两个参数具有相同的有效范围。这保证返回的引用不会悬垂。

### 3.4 模式匹配与枚举

Rust 的 `enum` 是代数数据类型（ADT），配合 `match` 表达穷尽性检查：

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}

fn parse(s: &str) -> Result<i32, String> {
    s.parse::<i32>().map_err(|_| format!("无法解析: {s}"))
}

fn main() {
    match parse("42") {
        Ok(v) => println!("解析成功: {v}"),
        Err(e) => println!("解析失败: {e}"),
    }
}
```

讲解：`Result` 是标准库的错误处理枚举；`match` 必须覆盖所有分支，因此不会漏掉错误路径。

## 4. Cargo 与工具链

Cargo 是 Rust 的构建系统与包管理器，功能类似 npm/Maven 的组合：

```bash
cargo new my-project     # 创建新项目
cargo build              # 构建（debug）
cargo build --release    # 优化构建
cargo run                # 运行
cargo test               # 运行测试
cargo fmt                # 格式化
cargo clippy             # 静态检查
cargo doc                # 生成文档
```

依赖在 `Cargo.toml` 中声明，从 crates.io 下载；`Cargo.lock` 锁定版本保证可复现构建。

```toml
[package]
name = "my-project"
version = "0.1.0"
edition = "2024"

[dependencies]
serde = { version = "1", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
```

讲解：edition 是 Rust 的兼容性里程碑（2015/2018/2021/2024），新项目应使用最新 edition。

## 5. 标准库与常用生态

标准库（std）提供：集合（Vec、HashMap）、字符串（String、&str）、错误处理（Result、Option）、并发（线程、channel、原子）、I/O 与文件系统。

常用第三方生态：

| 领域 | crate | 说明 |
| --- | --- | --- |
| Web 后端 | axum / actix-web | 异步 HTTP 框架 |
| 异步运行时 | tokio | 事件驱动运行时 |
| 序列化 | serde | JSON/二进制序列化 |
| 命令行 | clap | 参数解析 |
| 日志 | tracing / log | 结构化日志与追踪 |
| 测试 | criterion | 基准测试 |
| 嵌入式 | embedded-hal | 硬件抽象 |
| WebAssembly | wasm-bindgen | JS 互操作 |

## 6. Rust 与其他语言的对比

### 6.1 Rust 与 C

Rust 提供与 C 相当的性能，但默认内存安全；C 语法简单、生态庞大，适合嵌入式与遗留系统。新系统项目应评估 Rust。

### 6.2 Rust 与 C++

C++ 功能最全、生态最成熟，但安全依赖纪律；Rust 用类型系统强制安全，工具链（cargo/clippy）更现代。游戏引擎与既有 C++ 代码库通常继续用 C++，新模块可用 Rust（FFI）。

### 6.3 Rust 与 Go

Go 语法简单、并发模型友好、编译快；Rust 控制精细、无 GC、性能上限更高。服务端选型：追求开发速度与生态用 Go，追求极致性能与资源控制用 Rust。

## 7. 学习路线建议

第一阶段（2-4 周）：所有权、借用、生命周期、基本类型与模式匹配；每天用 cargo 写小练习。

第二阶段（4-8 周）：错误处理、泛型与 trait、集合与迭代器、测试；读《Rust 程序设计语言》（TRPL）。

第三阶段（2-3 月）：异步（tokio）、Web 服务（axum）、serde 序列化、与 C 互操作；完成一个实战项目。

持续：读标准库源码、参与开源、用 clippy 保持代码质量。

## 8. 常见误区与注意事项

误区一：把 Rust 当成“更难写的 C”。Rust 的难度来自安全约束，但编译器错误信息非常友好，跟随提示修改即可。

误区二：到处用 `clone()` 逃避借用检查。clone 有性能成本；先理解借用与生命周期，再决定是否 clone。

误区三：滥用 `unwrap()`。生产代码应使用 `Result` 与 `?` 传播错误。

误区四：忽视异步生态的选型。tokio 是事实标准，团队应统一。

## 9. 参考资源

Rust 官方文档：https://www.rust-lang.org/zh-CN/learn

《Rust 程序设计语言》中文版：https://kaisery.github.io/trpl-zh-cn/

Rust 标准库文档：https://doc.rust-lang.org/std/

crates.io：https://crates.io/

Rust 异步编程：https://rust-lang.github.io/async-book/

黑马程序员 Bilibili 空间：https://space.bilibili.com/37974444

尚硅谷 Bilibili 空间：https://space.bilibili.com/302417610

## 10. 小结

Rust 是系统编程领域近十年最重要的语言创新：所有权系统把内存安全从“运行时检查”提升到“编译期保证”。学习 Rust 不仅获得一门语言，更能加深对内存、并发与编译原理的理解——这些知识对所有语言都有迁移价值。

## 参考文献

Rust 官方文档：https://www.rust-lang.org/zh-CN/learn
Rust 程序设计语言（中文书）：https://kaisery.github.io/trpl-zh-cn/
Rust 标准库文档：https://doc.rust-lang.org/std/
crates.io：https://crates.io/
Rust 异步编程：https://rust-lang.github.io/async-book/

## 延伸阅读

Rust 与 C 对比（内存安全），见 025-c 模块。
Rust 与 C++ 对比，见 026-cpp 模块。
系统编程与嵌入式，见 035-iot 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 Rust 课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 所有权与借用检查器

移动语义：赋值与传参转移所有权；Copy 类型（整数、布尔）按位复制不移动。
借用规则：不可变借用可并行；可变借用独占；借用不可超过所有者生命周期。
内部可变性：RefCell 运行时检查借用；Mutex 跨线程；原子类型无锁。
排错：按编译器错误逐条修复，理解“借用冲突”的三个要素（值、借用类型、作用域）。

### 13.2 异步 Rust 与 Tokio

async/await 基于 Future 与执行器；tokio 提供多线程运行时与任务调度。
异步陷阱：阻塞调用卡死执行器（用 spawn_blocking）；锁跨 await（用 tokio::sync）。
Select 与流（Stream）组合并发任务；超时用 tokio::time::timeout。
性能：任务数而非线程数；背压与缓冲设计。
