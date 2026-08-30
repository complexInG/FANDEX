# 协程详解

> 本文档对标 MIT 6.005 Software Construction、Stanford CS107 Programming Paradigms、CMU 15-440 Distributed Systems 中并发模型与协作式多任务理论教学水准,面向 0 基础自学者与企业级 Lua 工程师,系统讲解 Lua 协程(coroutine)的本质、API、状态机模型、控制流语义、典型模式(生成器、管道、状态机)、与 OS 线程/事件循环的差异、LuaJIT 与 Lua 5.4 的协程演化、跨语言协程对比以及工程级实战案例。

## 1. 历史动机与演化

### 1.1 并发模型的范式演化

程序语言的并发模型历经五个主要阶段:

1. **顺序执行**(早期 FORTRAN、COBOL):单指令流,无并发概念,程序由顺序语句构成。
2. **基于进程的并发**(Unix fork、C `execvp`):操作系统级进程,独立地址空间,通过管道/信号量通信,上下文切换昂贵。
3. **基于内核线程的并发**(POSIX `pthread`、Java `Thread`):轻量于进程,共享地址空间,需要锁与条件变量,抢占式调度。
4. **基于用户态线程/协程的并发**(Lua coroutine、Python generator、Ruby Fiber):用户态调度,无需内核介入,协作式切换,极低开销。
5. **基于 async/await 的异步并发**(C# Task、JavaScript Promise、Rust async/await):编译器将 async 函数改写为状态机,配合事件循环,协程的语法糖化。

Lua 协程诞生于 1996 年 Lua 3.0,设计动机源于 SIMULA 67、BCPL、Modula-2 中的 coroutine 概念。Lua 团队选择协程而非 OS 线程的理由有三:

- **嵌入式定位**:Lua 作为嵌入脚本语言,不应依赖宿主的线程库;协程纯用户态实现,可移植性高。
- **极简哲学**:Lua 标准库刻意精简,引入 OS 线程会带来同步原语、调度器、内存模型等大量复杂度。
- **确定性需求**:游戏脚本(WoW、Roblox)需要可预测的执行顺序,抢占式多线程难以调试;协作式调度让程序员显式控制切换点。

### 1.2 Lua 协程 API 的版本演化

| Lua 版本 | 关键变化 | 设计动机 |
|---------|---------|---------|
| 3.0 (1996) | 首次引入 `coroutine` 库,API 表面与今天基本一致 | 提供 SIMULA 风格协程原语 |
| 5.0 (2003) | 重构协程实现,引入 `lua_State` 独立栈 | 提升稳定性,隔离协程栈 |
| 5.1 (2006) | 协程无法在 C 函数中 yield,`pcall` 内不能 yield | 简化 C API,牺牲灵活性 |
| 5.2 (2011) | `coroutine.running` 返回协程对象(5.1 返回 boolean) | API 一致性 |
| 5.3 (2015) | 引入 `lua_yieldk`/`lua_callk`/`lua_pcallk` continuation | 允许 C 函数中 yield |
| 5.3 (2015) | 新增 `coroutine.isyieldable()` | 检测当前是否可 yield |
| 5.4 (2020) | 新增 `coroutine.close()`、协程可作为 to-be-closed 变量 | 资源管理 RAII 化 |
| 5.5 (2025 规划) | 协程与 generational GC 协同优化 | 减少 long-running 协程的 GC 压力 |

### 1.3 与其他语言协程的对比定位

Lua 协程在并发模型谱系中处于"对称协程"(symmetric coroutine)与"非对称协程"(asymmetric coroutine)之间。Lua 选择非对称模型:`resume` 调用 `yield` 是父子关系,`yield` 必须返回到调用方 `resume`,不能任意跳转。这与 Python generator、JavaScript async/await 一致;Go goroutine、Erlang process 则属于对称协程,任意两个协程可互相切换。

Lua 协程的独有特征:

- **显式 API**:Lua 协程通过 `coroutine.create`/`resume`/`yield` 显式控制,无 `async`/`await` 语法糖(对比 JavaScript、Python、C#)。
- **双向数据流**:`resume` 与 `yield` 都可携带任意多参数,形成双向消息通道(对比 Python generator 只能单向 `yield` 接收 `send`)。
- **无内建调度器**:Lua 标准库不提供事件循环或任务调度器,需用户自行实现或依赖宿主(OpenResty、Nvim)。

## 2. 形式化定义

### 2.1 协程的数学定义

协程可形式化为一个五元组 $\langle S, s_0, F, \delta, \omega \rangle$,其中:

- $S$:有限状态集 $\{suspended, running, normal, dead\}$
- $s_0 \in S$:初始状态,即 $suspended$
- $F$:协程函数(function)集合,即从输入序列到输出序列的部分映射
- $\delta: S \times A \to S \times O$:状态转移函数,$A$ 为动作集 $\{resume, yield, return, error\}$,$O$ 为输出(传给对端的值)
- $\omega$:观测函数,将状态映射为可观测的字符串

### 2.2 状态机形式化

协程状态转移规则如下:

$$
\delta(suspended, resume(x_1, \ldots, x_n)) = \begin{cases} (running, \bot) & \text{首次 resume,启动协程,}x_i\text{ 作为函数参数} \\ (running, \bot) & \text{非首次 resume,}x_i\text{ 作为 yield 返回值} \end{cases}
$$

$$
\delta(running, yield(y_1, \ldots, y_m)) = (suspended, (y_1, \ldots, y_m))
$$

$$
\delta(running, return(r_1, \ldots, r_k)) = (dead, (true, r_1, \ldots, r_k))
$$

$$
\delta(running, error(e)) = (dead, (false, e))
$$

其中 $running$ 状态实际是相对的:当一个协程 $C_1$ `resume` 另一个协程 $C_2$ 时,$C_1$ 进入 $normal$ 状态,$C_2$ 进入 $running$ 状态。任意时刻只有一个协程处于 $running$。

### 2.3 resume-yield 通信的形式化

设 $C$ 为一协程,$R$ 为其调用方(主协程或另一协程)。`resume`-`yield` 形成对偶通信:

- $R \to C$ 通道:$R$ 调用 `resume(C, a_1, \ldots, a_n)`,$a_i$ 在 $C$ 内部作为 `yield()` 的返回值(或首次启动时作为函数参数)。
- $C \to R$ 通道:$C$ 调用 `yield(b_1, \ldots, b_m)`,$b_j$ 作为 `resume` 的返回值传给 $R$。

形式地,设 $C$ 的生命周期包含 $k$ 次 `resume`-$yield` 对,则:

$$
\begin{aligned}
R_1 &= resume(C, x_{1,1}, \ldots, x_{1,n_1}) = (true, y_{1,1}, \ldots, y_{1,m_1}) \\
R_2 &= resume(C, x_{2,1}, \ldots, x_{2,n_2}) = (true, y_{2,1}, \ldots, y_{2,m_2}) \\
&\vdots \\
R_k &= resume(C, x_{k,1}, \ldots, x_{k,n_k}) = (true, y_{k,1}, \ldots, y_{k,m_k}) \\
R_{k+1} &= resume(C, x_{k+1,1}, \ldots) = (true, r_1, \ldots, r_p) \quad \text{(协程结束)}
\end{aligned}
$$

后续 `resume` 返回 `(false, "cannot resume dead coroutine")`。

### 2.4 协程栈与主栈的关系

Lua 虚拟机中,每个协程拥有独立的 `lua_State`,即独立的 Lua 调用栈与寄存器。但所有协程共享同一份全局表(`_G`)、字符串池、元表缓存与基本类型元方法。

设主线程为 $T_0$,协程 $C_1, C_2, \ldots, C_n$。任意时刻只有一个 $C_i$ 处于 $running$,$T_0$ 处于 $normal$。当 $C_i$ `yield` 时,控制权返回调用它的协程(通常是 $T_0$)。这种"调用栈"逻辑上形成树形结构,根为 $T_0$。

## 3. 理论推导与证明

### 3.1 协程与闭包的等价性

**命题**:任意可用协程表达的状态保持算法,均可改写为闭包形式;反之亦然。

**证明**:

(1) 协程 → 闭包:设协程 $C$ 的函数体为 $f(x)$,包含 $k$ 个 `yield` 点。定义闭包 $g$:

```lua
local function make_generator()
  local state = {phase = 0, locals = {}}
  return function(input)
    -- 用 state.phase 模拟协程的执行点
    -- 用 state.locals 保存局部变量
    -- 显式 goto 跳转到对应阶段
    if state.phase == 0 then
      -- 阶段 0:执行到第一个 yield
      local a, b, c = ...
      state.locals.a, state.locals.b, state.locals.c = a, b, c
      state.phase = 1
      return value_at_yield_1
    elseif state.phase == 1 then
      -- 阶段 1:从 yield_1 恢复,执行到 yield_2
      local input_from_resume = input
      -- 使用 state.locals.a, .b, .c
      state.phase = 2
      return value_at_yield_2
    elseif state.phase == 2 then
      -- ...
    end
  end
end
```

这种转换称为 CPS 变换(continuation-passing style transform)的逆操作。Lua 5.3+ 的 `lua_yieldk` 即采用此机制。

(2) 闭包 → 协程:任意闭包 $g$ 可包装为协程:

```lua
local function closure_to_coro(g)
  return coroutine.create(function(...)
    local args = {...}
    while true do
      local result = g(table.unpack(args))
      if result == nil then return end
      coroutine.yield(result)
      args = {}  -- 后续 yield 的输入
    end
  end)
end
```

但闭包形式无法表达"暂停-恢复"的双向通信,需额外状态变量。因此协程表达力 ≥ 闭包表达力,但二者图灵等价。证毕。

### 3.2 协程无法利用多核

**命题**:Lua 协程无法利用多核 CPU 并行加速。

**证明**:Lua 虚拟机任意时刻只有一个协程处于 $running$ 状态,即只有一个 OS 线程在执行 Lua 字节码。即使宿主启动多个 OS 线程,每个线程也需独立 `lua_State`,无法共享协程。

设 $n$ 为协程数,$c$ 为 CPU 核数。Lua 协程的实际并行度 $P \le 1 \ll \min(n, c)$。要利用多核,需:

- 多 OS 线程 + 多 `lua_State`(隔离,通信昂贵);
- LuaLanes、Lua-Parallel 等第三方库(本质仍是多 `lua_State` + 消息传递);
- LuaJIT 的 `ffi` 调用 native 线程库(放弃协程模型)。

因此 Lua 协程适用于 I/O 密集型场景(网络、文件),不适用于 CPU 密集型并行计算。证毕。

### 3.3 协作式调度的确定性

**命题**:协作式调度的执行顺序是确定的(给定输入,输出唯一),抢占式调度则不确定。

**证明**:协作式调度中,协程切换只发生在显式 `yield` 点。给定相同输入序列,协程的 `resume`-`yield` 链是确定的,执行顺序可静态分析。

抢占式调度中,OS 调度器可在任意指令处打断线程(基于时钟中断),执行顺序受系统负载、定时精度、缓存命中等影响,无法静态预测。

这一性质使协程在游戏脚本、嵌入式控制等领域优于线程:调试可复现,无数据竞争(data race)。代价是程序员需手动管理切换点,长 CPU 任务会阻塞整个调度器。证毕。

## 4. 代码示例

### 4.1 基础:创建与启动协程

```lua
-- 最简单的协程:打印一次后结束
local co = coroutine.create(function()
  print("Hello from coroutine")
end)

print(coroutine.status(co))  -- suspended
coroutine.resume(co)         -- Hello from coroutine
print(coroutine.status(co))  -- dead
```

### 4.2 yield 与多次 resume

```lua
local co = coroutine.create(function(a)
  print("start:", a)
  local b = coroutine.yield(a + 1)
  print("resumed with:", b)
  local c = coroutine.yield(b * 2)
  print("resumed again with:", c)
  return "done"
end)

-- 第一次 resume:启动协程,a = 10
-- yield 返回 11,作为 resume 的第二个返回值
local ok1, r1 = coroutine.resume(co, 10)
print(ok1, r1)  -- true    11

-- 第二次 resume:b 接收 20,yield 返回 40
local ok2, r2 = coroutine.resume(co, 20)
print(ok2, r2)  -- true    40

-- 第三次 resume:c 接收 30,协程返回 "done"
local ok3, r3 = coroutine.resume(co, 30)
print(ok3, r3)  -- true    done

-- 第四次 resume:协程已 dead
local ok4, r4 = coroutine.resume(co)
print(ok4, r4)  -- false   cannot resume dead coroutine
```

### 4.3 生成器:无限斐波那契数列

```lua
local function fib()
  local a, b = 0, 1
  while true do
    coroutine.yield(a)
    a, b = b, a + b
  end
end

local gen = coroutine.wrap(fib)
for i = 1, 10 do
  print(i, gen())  -- 1 0 / 2 1 / 3 1 / 4 2 / 5 3 / 6 5 / 7 8 / 8 13 / 9 21 / 10 34
end
```

### 4.4 生成器:素数序列

```lua
local function primes()
  local known = {2}
  coroutine.yield(2)
  local n = 3
  while true do
    local is_prime = true
    for _, p in ipairs(known) do
      if p * p > n then break end
      if n % p == 0 then is_prime = false; break end
    end
    if is_prime then
      known[#known + 1] = n
      coroutine.yield(n)
    end
    n = n + 2
  end
end

local next_prime = coroutine.wrap(primes)
for i = 1, 20 do
  io.write(next_prime(), " ")
end
-- 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71
```

### 4.5 协程管道:数据流处理

```lua
-- 生产者:产生 1 到 N
local function producer(n)
  return coroutine.wrap(function()
    for i = 1, n do
      coroutine.yield(i)
    end
  end)
end

-- 过滤器:平方
local function square(input)
  return coroutine.wrap(function()
    for x in input do
      coroutine.yield(x * x)
    end
  end)
end

-- 过滤器:加 100
local function add_hundred(input)
  return coroutine.wrap(function()
    for x in input do
      coroutine.yield(x + 100)
    end
  end)
end

-- 串联管道
local pipe = add_hundred(square(producer(5)))
for result in pipe do
  print(result)
end
-- 101 (1^2 + 100)
-- 104 (2^2 + 100)
-- 109 (3^2 + 100)
-- 116 (4^2 + 100)
-- 125 (5^2 + 100)
```

### 4.6 状态机:红绿灯控制器

```lua
local function traffic_light()
  while true do
    print("GREEN - go (3s)")
    coroutine.yield(3)
    print("YELLOW - slow (1s)")
    coroutine.yield(1)
    print("RED - stop (2s)")
    coroutine.yield(2)
  end
end

local light = coroutine.wrap(traffic_light)
for cycle = 1, 3 do
  print("=== Cycle " .. cycle .. " ===")
  for phase = 1, 3 do
    local duration = light()
    os.execute("sleep " .. duration)  -- 演示用,实际项目应使用非阻塞 sleep
  end
end
```

### 4.7 协程实现迭代器

```lua
-- 自定义迭代器:遍历二叉树的中序遍历
local function inorder(node)
  if node == nil then return end
  inorder(node.left)
  coroutine.yield(node.value)
  inorder(node.right)
end

local function tree_iterator(root)
  return coroutine.wrap(function()
    inorder(root)
  end), nil, nil
end

-- 使用示例
local tree = {
  value = 4,
  left = { value = 2, left = { value = 1 }, right = { value = 3 } },
  right = { value = 6, left = { value = 5 }, right = { value = 7 } },
}

for v in tree_iterator(tree) do
  io.write(v, " ")
end
-- 1 2 3 4 5 6 7
```

### 4.8 异步回调扁平化

```lua
-- 模拟异步操作:从远程获取数据
local function fetch_async(url, callback)
  -- 假装异步,实际立即完成
  local data = "data from " .. url
  callback(data)
end

-- 把回调式 API 包装成同步式(借助主循环 + 协程)
local scheduler = { tasks = {} }

function scheduler.spawn(fn)
  local co = coroutine.create(fn)
  scheduler.tasks[#scheduler.tasks + 1] = co
  return co
end

function scheduler.step()
  local i = 1
  while i <= #scheduler.tasks do
    local co = scheduler.tasks[i]
    if coroutine.status(co) ~= "dead" then
      coroutine.resume(co)
      i = i + 1
    else
      table.remove(scheduler.tasks, i)
    end
  end
end

local function await(url)
  local co = coroutine.running()
  local result
  fetch_async(url, function(data)
    result = data
    -- 唤醒等待的协程
    coroutine.resume(co)
  end)
  coroutine.yield()  -- 挂起,等待回调唤醒
  return result
end

-- 主代码:看起来同步
scheduler.spawn(function()
  print("start")
  local data1 = await("http://api.example.com/1")
  print("got:", data1)
  local data2 = await("http://api.example.com/2")
  print("got:", data2)
  print("done")
end)

-- 推进调度器
while #scheduler.tasks > 0 do
  scheduler.step()
end
```

### 4.9 错误处理与 pcall

```lua
local function risky()
  coroutine.yield("safe value")
  error("something went wrong")
end

local co = coroutine.create(risky)

local ok1, v1 = coroutine.resume(co)
print(ok1, v1)  -- true    safe value

local ok2, err = coroutine.resume(co)
print(ok2, err)  -- false   input:3: something went wrong
print(coroutine.status(co))  -- dead

-- 死后再 resume
local ok3, err3 = coroutine.resume(co)
print(ok3, err3)  -- false   cannot resume dead coroutine
```

### 4.10 coroutine.wrap 与错误传播

```lua
local co = coroutine.wrap(function()
  error("boom!")
end)

-- wrap 会直接抛出错误,不像 create 返回 (false, err)
local ok, err = pcall(co)
print(ok, err)  -- false   input:2: boom!
```

### 4.11 协程嵌套

```lua
local function inner()
  coroutine.yield("inner 1")
  coroutine.yield("inner 2")
end

local function outer()
  local inner_co = coroutine.wrap(inner)
  coroutine.yield("outer before inner")
  -- 调用内层协程
  coroutine.yield(inner_co())  -- "inner 1"
  coroutine.yield(inner_co())  -- "inner 2"
  coroutine.yield("outer after inner")
end

local gen = coroutine.wrap(outer)
print(gen())  -- outer before inner
print(gen())  -- inner 1
print(gen())  -- inner 2
print(gen())  -- outer after inner
```

### 4.12 实现简易任务调度器

```lua
local Scheduler = {}
Scheduler.__index = Scheduler

function Scheduler.new()
  return setmetatable({ ready = {} }, Scheduler)
end

function Scheduler:spawn(fn)
  local co = coroutine.create(fn)
  self.ready[#self.ready + 1] = co
  return co
end

function Scheduler:sleep(seconds)
  local co = coroutine.running()
  -- 实际项目用 timer 库,这里简化为立即重新入队
  self.ready[#self.ready + 1] = co
  coroutine.yield()
end

function Scheduler:run()
  while #self.ready > 0 do
    local co = table.remove(self.ready, 1)
    if coroutine.status(co) ~= "dead" then
      local ok, err = coroutine.resume(co)
      if not ok then
        print("Task error:", err)
      end
    end
  end
end

-- 使用
local sched = Scheduler.new()
sched:spawn(function()
  for i = 1, 3 do
    print("Task A step", i)
    sched:sleep(0)
  end
end)
sched:spawn(function()
  for i = 1, 3 do
    print("Task B step", i)
    sched:sleep(0)
  end
end)
sched:run()
-- Task A step 1
-- Task B step 1
-- Task A step 2
-- Task B step 2
-- Task A step 3
-- Task B step 3
```

### 4.13 Lua 5.4+ 的 coroutine.close

```lua
local co = coroutine.create(function()
  print("started")
  coroutine.yield("first")
  print("resumed")
  coroutine.yield("second")
  print("finished")
end)

coroutine.resume(co)  -- started, returns "first"
coroutine.resume(co)  -- resumed, returns "second"

-- 提前关闭协程(类似 Python generator.close)
coroutine.close(co)
print(coroutine.status(co))  -- dead

-- 关闭后再 resume
local ok, err = coroutine.resume(co)
print(ok, err)  -- false   cannot resume dead coroutine
```

### 4.14 to-be-closed 变量与协程

```lua
-- Lua 5.4+:将协程作为 to-be-closed 变量,自动关闭
local function process_data()
  local co <close> = coroutine.create(function()
    print("coroutine started")
    coroutine.yield("partial result")
    print("coroutine natural end")
  end)
  
  local ok, result = coroutine.resume(co)
  print("got:", result)
  -- 块结束时,co 自动关闭,即使未自然结束
end

process_data()
-- coroutine started
-- got: partial result
-- (块结束,co 被 close)
```

### 4.15 协程与元表:协程对象的方法

```lua
-- 协程对象是 thread 类型,可以放在表中
local tasks = {}
for i = 1, 3 do
  tasks[i] = coroutine.create(function(idx)
    for j = 1, 2 do
      coroutine.yield("task " .. idx .. " step " .. j)
    end
  end)
end

-- 轮转调度
local active = true
while active do
  active = false
  for i, co in ipairs(tasks) do
    if coroutine.status(co) ~= "dead" then
      active = true
      local ok, v = coroutine.resume(co, i)
      print(v)
    end
  end
end
-- task 1 step 1
-- task 2 step 1
-- task 3 step 1
-- task 1 step 2
-- task 2 step 2
-- task 3 step 2
```

### 4.16 实现懒加载序列

```lua
local LazySeq = {}
LazySeq.__index = LazySeq

function LazySeq.new(gen_fn)
  local self = setmetatable({}, LazySeq)
  self.co = coroutine.wrap(gen_fn)
  self.cache = {}
  return self
end

function LazySeq:get(n)
  while #self.cache < n do
    local v = self.co()
    if v == nil then break end
    self.cache[#self.cache + 1] = v
  end
  return self.cache[n]
end

function LazySeq:take(n)
  local result = {}
  for i = 1, n do
    local v = self:get(i)
    if v == nil then break end
    result[#result + 1] = v
  end
  return result
end

-- 使用:懒加载的平方序列
local squares = LazySeq.new(function()
  local i = 1
  while true do
    coroutine.yield(i * i)
    i = i + 1
  end
end)

local first_five = squares:take(5)
print(table.concat(first_five, ", "))  -- 1, 4, 9, 16, 25
```

### 4.17 协程与 pcall 嵌套

```lua
local function deep_operation()
  error("deep failure")
end

local co = coroutine.create(function()
  -- 在 pcall 中调用会失败的函数
  local ok, err = pcall(deep_operation)
  if not ok then
    print("caught in coroutine:", err)
    coroutine.yield("recovered")
  end
  return "success"
end)

print(coroutine.resume(co))  -- caught in coroutine: ... / true    recovered
print(coroutine.resume(co))  -- true    success
```

### 4.18 完整案例:协程实现的 WebSocket-like 帧解析

```lua
-- 模拟分块到达的字节流,用协程解析帧
local function frame_parser()
  local buffer = ""
  while true do
    -- 等待新数据到达
    local chunk = coroutine.yield()
    if chunk == nil then return end
    buffer = buffer .. chunk
    
    -- 尝试解析完整帧
    while #buffer >= 4 do  -- 假设帧头 4 字节为长度
      local len = tonumber(buffer:sub(1, 4), 16) or 0
      if #buffer >= 4 + len then
        local payload = buffer:sub(5, 4 + len)
        buffer = buffer:sub(5 + len)
        -- 通过另一个 yield 输出解析结果
        coroutine.yield({length = len, payload = payload})
      else
        break  -- 等待更多数据
      end
    end
  end
end

local parser = coroutine.wrap(frame_parser)
parser()  -- 启动协程,等待第一次输入

-- 模拟分块到达
local function feed(data)
  local result = parser(data)
  if result then
    print(string.format("Frame: len=%d payload=%q", result.length, result.payload))
  end
end

-- 测试:一帧分两次到达
feed("000")          -- 不完整,无输出
feed("5Hello")       -- 完整帧:长度 5,内容 Hello
-- Frame: len=5 payload="Hello"

feed("000AWorld!")   -- 一帧:长度 10,内容 World!
-- Frame: len=10 payload="World!"

feed(nil)            -- 关闭解析器
```

## 5. 对比分析

### 5.1 Lua 协程 vs Python generator

| 维度 | Lua 协程 | Python generator |
|------|---------|-----------------|
| 创建语法 | `coroutine.create(fn)` | `def gen(): yield x` |
| 启动 | `coroutine.resume(co)` | `next(gen)` |
| 暂停 | `coroutine.yield(v)` | `yield v` |
| 双向通信 | `resume` 返回 yield 值,`yield` 返回 resume 参数 | `send()` 注入值,`yield` 表达式返回 |
| 错误传播 | `resume` 返回 `(false, err)` | `throw()` 抛出异常 |
| 关闭 | `coroutine.close()`(5.4+) | `gen.close()` |
| 嵌套 | 协程内可调用其他协程 | `yield from gen` |
| 异步支持 | 无内建 async/await | `async def` + `await` |
| 标准库 | 仅 `coroutine` | `asyncio`、`itertools` |

Python generator 是"半协程":首次必须 `next()` 启动,且不能任意位置 `yield`(必须在 generator 函数内)。Lua 协程更"对称":任意 `resume`-`yield` 均可双向传值。

### 5.2 Lua 协程 vs JavaScript async/await

| 维度 | Lua 协程 | JavaScript async/await |
|------|---------|----------------------|
| 抽象层级 | 显式 `coroutine.*` API | `async` 函数自动改写为协程 |
| Promise 集成 | 无内建 | `await` 接受 Promise |
| 事件循环 | 无内建 | 浏览器/Node.js 内建 |
| 错误处理 | `resume` 返回错误 | `try/catch` 捕获 |
| 多协程并发 | 手动调度 | `Promise.all` |
| 调试 | 栈跟踪限于协程内部 | async 栈跟踪(Chrome) |

JavaScript async/await 在语法层面把协程隐藏,聚焦于 Promise 组合;Lua 把协程作为通用控制流原语,可表达更广模式(生成器、状态机、管道)。

### 5.3 Lua 协程 vs Go goroutine

| 维度 | Lua 协程 | Go goroutine |
|------|---------|-------------|
| 调度方式 | 协作式 | 抢占式(work-stealing) |
| 多核利用 | 单核 | 多核 |
| 切换成本 | ~50-100ns | ~200-500ns |
| 通信原语 | `resume`/`yield` 双向传值 | channel |
| 内存占用 | ~1-2KB 初始栈 | ~2-8KB 初始栈,可增长 |
| 数量上限 | 千级 | 百万级 |
| 内建调度器 | 无 | runtime 内建 |

Go goroutine 是"对称协程",任意两个 goroutine 可通过 channel 通信,调度器自动调度;Lua 协程是"非对称协程",必须 `resume`-`yield` 配对,且需手动实现调度器。

### 5.4 Lua 协程 vs OS 线程

| 维度 | Lua 协程 | OS 线程(pthread) |
|------|---------|----------------|
| 内核态切换 | 无 | 有 |
| 创建成本 | 微秒级 | 毫秒级 |
| 内存占用 | KB 级 | MB 级栈 |
| 并行度 | 1(单核) | N(多核) |
| 数据竞争 | 无(协作式) | 有(需锁) |
| 死锁风险 | 无(单线程) | 有 |
| I/O 阻塞 | 阻塞整个调度器 | 仅阻塞本线程 |
| 适用场景 | I/O 密集 + 单核 | CPU 密集 / 多核并行 |

### 5.5 Lua 协程 vs Rust async/await

| 维度 | Lua 协程 | Rust async/await |
|------|---------|-----------------|
| 类型系统 | 动态类型 | 静态类型,`Future` trait |
| 内存模型 | GC | 所有权 + 借用 |
| 栈分配 | 有栈协程(stackful) | 无栈协程(stackless,状态机) |
| 编译期检查 | 无 | 编译期验证 |
| 性能 | LuaJIT 切换 ~100ns | 零成本抽象 |
| 学习曲线 | 低 | 高 |

Rust 的 async/await 是"无栈协程":async 函数被编译为状态机,无独立栈,内存占用更小但实现复杂。Lua 协程是"有栈协程",每个协程有独立栈,实现简单但内存开销略大。

## 6. 常见陷阱与反模式

### 6.1 在 C 函数中 yield(Lua 5.1)

```lua
-- Lua 5.1 反模式
local function c_call_with_yield()
  -- 假设 ffi.C.sleep 是 C 函数
  ffi.C.sleep(1)  -- 不能在此处 yield
  coroutine.yield()  -- 错误:attempt to yield across metamethod/C-call boundary
end

-- 修正:Lua 5.3+ 使用 lua_yieldk,或 LuaJIT 使用 ffi.C 配合协程友好 API
```

### 6.2 死协程复活

```lua
local co = coroutine.create(function() end)
coroutine.resume(co)  -- 协程立即结束
coroutine.resume(co)  -- 错误:cannot resume dead coroutine
-- 反模式:试图检查后复活
-- 修正:重新创建协程
```

### 6.3 resume 错误被忽略

```lua
local co = coroutine.create(function()
  error("critical failure")
end)
coroutine.resume(co)  -- 返回 (false, err),但易被忽略

-- 修正:检查返回值
local ok, err = coroutine.resume(co)
if not ok then
  error("Coroutine failed: " .. tostring(err))
end
```

### 6.4 wrap 隐藏错误

```lua
local gen = coroutine.wrap(function()
  error("hidden error")
end)
gen()  -- 直接抛出,易导致整个程序崩溃

-- 修正:用 pcall 包裹
local ok, result = pcall(gen)
if not ok then
  print("Generator error:", result)
end
```

### 6.5 协程泄漏

```lua
-- 反模式:创建大量协程但不结束
local cos = {}
for i = 1, 1000000 do
  cos[i] = coroutine.create(function()
    coroutine.yield()  -- 永远挂着
  end)
  coroutine.resume(cos[i])
end
-- 这些协程永远不结束,占用内存

-- 修正:Lua 5.4+ 显式关闭
for i = 1, #cos do
  coroutine.close(cos[i])
end
cos = nil  -- 释放引用
```

### 6.6 协程内 resume 自身

```lua
local co = coroutine.create(function()
  coroutine.resume(co)  -- 错误:cannot resume non-suspended coroutine
end)
coroutine.resume(co)

-- 修正:协程处于 running 状态时不能 resume 自身
```

### 6.7 假设 resume 立即返回

```lua
-- 反模式:协程内执行长 CPU 任务不 yield
local co = coroutine.create(function()
  while true do
    -- 长时间计算,阻塞整个调度器
    heavy_compute()
    coroutine.yield()
  end
end)

-- 修正:在循环内定期 yield
local co = coroutine.create(function()
  while true do
    for i = 1, 1000 do
      heavy_compute_step()
      if i % 100 == 0 then
        coroutine.yield()  -- 让出控制权
      end
    end
  end
end)
```

### 6.8 yield 在 pcall 外的错误传播

```lua
-- 协程内未捕获的错误会通过 resume 返回,但若调用方忽略则丢失
local co = coroutine.create(function()
  local t = nil
  return t.field  -- 运行时错误
end)

local ok, err = coroutine.resume(co)
-- 若不检查 ok,err,错误被静默丢弃
```

### 6.9 协程状态判断错误

```lua
-- 误用 status
local co = coroutine.create(function() coroutine.yield() end)
coroutine.resume(co)
if coroutine.status(co) == "running" then  -- 错误:此时为 suspended
  -- ...
end

-- 修正:正确理解状态
-- suspended: 可 resume
-- running: 当前正在执行(只有主协程或当前协程)
-- normal: resume 了其他协程,自身暂停
-- dead: 已结束
```

### 6.10 跨 resume 共享可变状态

```lua
-- 反模式:依赖协程间的共享状态,但顺序不确定
local shared = {}
local co1 = coroutine.create(function()
  shared.x = 1
  coroutine.yield()
  -- 期望 shared.x 仍为 1,但若 co2 在 yield 期间修改则不然
  print(shared.x)
end)
local co2 = coroutine.create(function()
  shared.x = 99
end)

-- 修正:避免共享可变状态,改用 resume 参数传值
```

## 7. 工程实践与最佳实践

### 7.1 协程命名与封装

```lua
-- 反模式:裸 coroutine.create 散落代码各处
local co = coroutine.create(function() ... end)

-- 最佳实践:封装为命名良好的工厂函数
local function create_worker(task_name, fn)
  local co = coroutine.create(function()
    local ok, err = pcall(fn)
    if not ok then
      log.error("[%s] task failed: %s", task_name, err)
    end
  end)
  return co
end

local worker = create_worker("data_loader", function()
  -- ...
end)
```

### 7.2 错误处理策略

```lua
-- 通用 resume 包装器
local function safe_resume(co, ...)
  local ok, result_or_err = coroutine.resume(co, ...)
  if not ok then
    -- 记录栈跟踪
    log.error("Coroutine error: %s\n%s", result_or_err, debug.traceback(co))
    return nil, result_or_err
  end
  return result_or_err
end
```

### 7.3 协程池模式

```lua
local CoroutinePool = {}
CoroutinePool.__index = CoroutinePool

function CoroutinePool.new(factory, max_size)
  return setmetatable({
    factory = factory,
    max_size = max_size or 10,
    free = {},
    busy = {},
  }, CoroutinePool)
end

function CoroutinePool:acquire(...)
  local co
  if #self.free > 0 then
    co = table.remove(self.free)
    -- 重置协程状态(若支持)
  else
    co = self.factory()
  end
  self.busy[co] = true
  return co
end

function CoroutinePool:release(co)
  if coroutine.status(co) == "dead" then
    -- 死协程不回收
    self.busy[co] = nil
    return
  end
  self.busy[co] = nil
  if #self.free < self.max_size then
    self.free[#self.free + 1] = co
  end
end
```

### 7.4 调试协程

```lua
-- 获取协程的栈跟踪
local function debug_coroutine(co)
  print("Status:", coroutine.status(co))
  print("Traceback:")
  print(debug.traceback(co, 1))
end

-- 在协程内记录 resume-yield 历史
local function instrumented_coroutine(fn)
  local history = {}
  local co = coroutine.create(function(...)
    history[#history + 1] = "started with " .. tostring(select("#", ...)) .. " args"
    fn(...)
  end)
  return co, history
end
```

### 7.5 与 pcall/xpcall 配合

```lua
-- 协程内用 xpcall 捕获错误并附加栈信息
local function safe_coroutine_body(fn)
  return function(...)
    xpcall(fn, function(err)
      -- 此处可记录错误
      log.error("Coroutine failed: %s\n%s", err, debug.traceback())
      -- 重新抛出,让 resume 接收
      error(err, 0)
    end, ...)
  end
end

local co = coroutine.create(safe_coroutine_body(function()
  -- 业务逻辑
end))
```

### 7.6 性能考量

```lua
-- 协程切换成本:LuaJIT 约 50-100ns,Lua 5.4 约 200-500ns
-- 避免在热路径频繁创建/销毁协程
-- 改用协程池或重置协程状态

-- 测量协程切换成本
local function bench_coroutine_switch(n)
  local co = coroutine.create(function()
    for _ = 1, n do
      coroutine.yield()
    end
  end)
  local start = os.clock()
  while coroutine.status(co) ~= "dead" do
    coroutine.resume(co)
  end
  return (os.clock() - start) / n  -- 每次切换秒数
end

print("Avg switch time:", bench_coroutine_switch(1000000), "s")
```

### 7.7 与宿主集成

```lua
-- OpenResty 风格:在 ngx.sleep 等异步 API 内部 yield
-- ngx.sleep(0.1)  -- 内部 yield,让出调度器
-- 用户代码看似同步,实际异步

-- OpenResty 的协程 API 扩展
-- ngx.thread.spawn(fn, ...) -- 创建轻线程
-- ngx.thread.wait(thread1, ...) -- 等待任一完成
-- ngx.semaphore -- 协程间同步

-- 模拟实现
local ngx_thread = {}
function ngx_thread.spawn(fn, ...)
  -- 创建协程并加入调度器
  return scheduler.spawn(function() fn(...) end)
end

function ngx_thread.wait(...)
  local threads = {...}
  -- 等待任一完成
  while true do
    for _, t in ipairs(threads) do
      if coroutine.status(t) == "dead" then
        return t
      end
    end
    coroutine.yield()  -- 让出调度器
  end
end
```

### 7.8 资源管理

```lua
-- Lua 5.4+:用 to-be-closed 变量自动关闭协程
local function process_with_cleanup()
  local co <close> = coroutine.create(function()
    -- 业务逻辑
    coroutine.yield("partial")
    -- 若此处异常,块结束时 co 仍会被 close
  end)
  coroutine.resume(co)
end

-- 旧版本:用 pcall + finally 模式
local function safe_process()
  local co = coroutine.create(function() ... end)
  local ok, err = pcall(function()
    coroutine.resume(co)
  end)
  if coroutine.status(co) ~= "dead" then
    -- Lua 5.4: coroutine.close(co)
    -- 旧版本:无法强制关闭,只能等 GC
  end
  if not ok then error(err) end
end
```

## 8. 案例研究

### 8.1 案例一:WoW 插件的协程化任务系统

WoW 插件需要在主循环外执行耗时任务(如批量处理背包物品)。WoW API 不允许真线程,但提供 `C_Timer.After` 等异步原语。结合协程可实现"看似同步"的批量处理:

```lua
-- MyAddon/TaskRunner.lua
local TaskRunner = {}
TaskRunner.__index = TaskRunner

function TaskRunner:new()
  return setmetatable({
    current = nil,
    pending = {},
  }, self)
end

function TaskRunner:enqueue(fn)
  self.pending[#self.pending + 1] = fn
  if self.current == nil then
    self:next()
  end
end

function TaskRunner:next()
  if #self.pending == 0 then
    self.current = nil
    return
  end
  local fn = table.remove(self.pending, 1)
  self.current = coroutine.create(fn)
  self:resume()
end

function TaskRunner:resume(...)
  local ok, wait_time = coroutine.resume(self.current, ...)
  if not ok then
    print("Task failed:", wait_time)
    self:next()
    return
  end
  if coroutine.status(self.current) ~= "dead" then
    -- wait_time 是 yield 的参数,表示多少秒后继续
    C_Timer.After(wait_time or 0, function()
      self:resume()
    end)
  else
    self:next()
  end
end

function TaskRunner.yield_for(seconds)
  coroutine.yield(seconds)
end

-- 使用:批量处理背包物品,每帧处理 5 个
local runner = TaskRunner:new()
runner:enqueue(function()
  local bag_size = C_Container.GetContainerNumSlots(0)
  for slot = 1, bag_size do
    process_slot(0, slot)
    if slot % 5 == 0 then
      TaskRunner.yield_for(0)  -- 让出主循环
    end
  end
  print("Bag processing done")
end)
```

### 8.2 案例二:OpenResty 中的并发 HTTP 请求

OpenResty 借助 `ngx.location.capture_multi` 实现并发子请求,但若需更细粒度控制,可结合 `ngx.thread.spawn` 与协程:

```lua
-- 同时请求多个上游,合并结果
location /aggregated {
  content_by_lua_block {
    local function fetch(url)
      local res = ngx.location.capture("/proxy", { vars = { target_url = url } })
      return res.body
    end
    
    local threads = {
      ngx.thread.spawn(fetch, "http://api1.example.com"),
      ngx.thread.spawn(fetch, "http://api2.example.com"),
      ngx.thread.spawn(fetch, "http://api3.example.com"),
    }
    
    local results = {}
    for i, t in ipairs(threads) do
      local ok, res = ngx.thread.wait(t)
      if ok then
        results[i] = res
      else
        results[i] = nil
      end
    end
    
    ngx.say(cjson.encode(results))
  }
}
```

### 8.3 案例三:Neovim 中的异步任务

Neovim Lua API 提供 `vim.loop`(libuv 绑定),支持异步 I/O。结合协程可写"同步式"异步代码:

```lua
-- 异步读取多个文件,合并内容
local function read_files_async(paths, callback)
  local results = {}
  local remaining = #paths
  
  for i, path in ipairs(paths) do
    vim.loop.fs_open(path, "r", 438, function(err, fd)
      if err then
        results[i] = nil
      else
        vim.loop.fs_read(fd, 1024 * 1024, -1, function(err2, data)
          results[i] = data
          vim.loop.fs_close(fd, function() end)
          remaining = remaining - 1
          if remaining == 0 then
            callback(results)
          end
        end)
      end
    end)
  end
end

-- 用协程包装为同步风格
local function read_files_sync(paths)
  local co = coroutine.running()
  local results
  read_files_async(paths, function(r)
    results = r
    coroutine.resume(co)
  end)
  coroutine.yield()
  return results
end

-- 使用
local function main()
  local contents = read_files_sync({"/etc/hosts", "/etc/passwd"})
  for i, c in ipairs(contents) do
    print("File " .. i .. ":", #c, "bytes")
  end
end

coroutine.wrap(main)()
```

### 8.4 案例四:Lua 解析大文件不阻塞主循环

读取 GB 级日志文件,分块处理,定期 yield 让 UI 保持响应:

```lua
local function process_large_file(path, processor)
  local co = coroutine.create(function()
    local file = io.open(path, "r")
    if not file then error("Cannot open " .. path) end
    
    local chunk_size = 65536  -- 64KB
    local bytes_processed = 0
    local lines_processed = 0
    
    while true do
      local chunk = file:read(chunk_size)
      if not chunk then break end
      
      for line in chunk:gmatch("[^\n]+") do
        processor(line)
        lines_processed = lines_processed + 1
      end
      
      bytes_processed = bytes_processed + #chunk
      -- 每 1MB 让出一次
      if bytes_processed % (1024 * 1024) < chunk_size then
        coroutine.yield(bytes_processed)
      end
    end
    
    file:close()
    return lines_processed
  end)
  return co
end

-- UI 集成
local function start_processing()
  local co = process_large_file("/var/log/app.log", function(line)
    if line:match("ERROR") then
      error_count = error_count + 1
    end
  end)
  
  local function tick()
    if coroutine.status(co) ~= "dead" then
      local ok, progress = coroutine.resume(co)
      if ok then
        update_progress_bar(progress)
        schedule_next_tick(tick)  -- 例如 setTimer(tick, 0)
      else
        print("Error:", progress)
      end
    else
      print("Done")
    end
  end
  
  tick()
end
```

### 8.5 案例五:协程实现有限状态机

用协程封装 TCP 连接状态机(CLOSED → SYN_SENT → ESTABLISHED → ...):

```lua
local function tcp_state_machine()
  local state = "CLOSED"
  while true do
    local event, data = coroutine.yield(state)
    
    if state == "CLOSED" then
      if event == "connect" then
        send_syn(data.dest)
        state = "SYN_SENT"
      end
    elseif state == "SYN_SENT" then
      if event == "recv_syn_ack" then
        send_ack(data.src)
        state = "ESTABLISHED"
      elseif event == "timeout" then
        state = "CLOSED"
        error("connection timeout")
      end
    elseif state == "ESTABLISHED" then
      if event == "send" then
        send_data(data.payload)
      elseif event == "close" then
        send_fin()
        state = "FIN_WAIT_1"
      elseif event == "recv_fin" then
        send_ack()
        state = "CLOSE_WAIT"
      end
    elseif state == "FIN_WAIT_1" then
      if event == "recv_ack" then
        state = "FIN_WAIT_2"
      end
    elseif state == "FIN_WAIT_2" then
      if event == "recv_fin" then
        send_ack()
        state = "TIME_WAIT"
      end
    elseif state == "CLOSE_WAIT" then
      if event == "close" then
        send_fin()
        state = "LAST_ACK"
      end
    elseif state == "TIME_WAIT" then
      if event == "timeout" then
        state = "CLOSED"
      end
    elseif state == "LAST_ACK" then
      if event == "recv_ack" then
        state = "CLOSED"
      end
    end
  end
end

-- 使用
local tcp = coroutine.wrap(tcp_state_machine)
print(tcp())  -- CLOSED(启动)
print(tcp("connect", {dest = "1.2.3.4"}))  -- SYN_SENT
print(tcp("recv_syn_ack", {src = "1.2.3.4"}))  -- ESTABLISHED
print(tcp("send", {payload = "hello"}))  -- ESTABLISHED
print(tcp("close"))  -- FIN_WAIT_1
```

### 9.1 基础题

1. 写出协程的四种状态及状态间转换条件。
2. 解释 `coroutine.create` 与 `coroutine.wrap` 的区别,各举一个适用场景。
3. 编写协程生成器,产出所有完全平方数。
4. 给定协程 `co`,如何判断它是否可以安全 `resume`?

### 9.2 进阶题

5. 用协程实现 `flatMap` 操作:对输入序列的每个元素生成多个输出。
6. 实现协程管道,将生产者-过滤-消费者串联,处理斐波那契数列的前 N 项。
7. 用协程实现一个简单的 LRU 缓存,每次访问 yield 一次以记录访问顺序。
8. 实现协程池,支持最大并发数与任务排队。

### 9.4 开放题

15. 调研 LuaJIT 的协程实现与标准 Lua 的差异,分析性能数据。
16. 调研 Luau(Roblox)对协程 API 的扩展,如 `coroutine.isyieldable` 的使用模式。
17. 若 Lua 引入真线程(类似 Java),会与现有协程模型产生哪些冲突?可能的设计方案?
18. 调研 Python `asyncio`、JavaScript `Promise`、C# `Task` 的事件循环实现,与 Lua 协程手动调度器的对比。

### 11.1 Lua 官方资源

- Lua 官方站点:https://www.lua.org/
- Lua 5.4 参考手册:https://www.lua.org/manual/5.4/manual.html#6.2
- Lua mailing list archive:https://www.lua.org/lua-l.html

### 11.2 协程理论与历史

- Marlin, M. M. *Coroutines: A Programming Methodology, a Language Design and an Implementation*. Springer, 1980.
- Knuth, Donald E. *The Art of Computer Programming, Volume 1*. Section 1.4.2 on Coroutines.
- Wang, A. and Olsson, R. A. "An Approach to Symmetric Co-routines on the Java Virtual Machine".

### 11.3 跨语言对比

- Python PEP 342 (Coroutines via Enhanced Generators): https://peps.python.org/pep-0342/
- Python PEP 492 (async/await): https://peps.python.org/pep-0492/
- JavaScript async function spec: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function
- Go concurrency tutorial: https://go.dev/tour/concurrency/1
- Rust async book: https://rust-lang.github.io/async-book/

### 11.4 工业级实践

- OpenResty 文档:https://openresty-reference.readthedocs.io/
- Neovim `vim.loop` 文档:https://neovim.io/doc/user/luvref.html
- Luvit(Node.js 风格 Lua 框架):https://luvit.io/
- Lua Lanes(多核并行库):https://github.com/LuaLanes/lanes

### 11.5 高级主题

- Lua 5.4 的 to-be-closed 变量与协程协作
- LuaJIT 的 `ffi.C` 调用与协程边界
- 协程与 generational GC 的交互(Lua 5.5 规划)
- 协程在嵌入式实时系统中的应用
- 协程调试与性能分析工具
