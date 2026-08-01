# -*- coding: utf-8 -*-
"""第二批 016-go ASCII 图表修复。"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\016-go")


def replace_block(path: pathlib.Path, marker: str, new: str) -> bool:
    text = path.read_text(encoding="utf-8")
    idx = text.find(marker)
    if idx < 0:
        return False
    start = text.rfind("```", 0, idx)
    end = text.find("```", idx)
    if start < 0 or end < 0 or end < start:
        return False
    end += 3
    path.write_text(text[:start] + new + text[end:], encoding="utf-8")
    return True


results = []

# 014 ChannelPrinciple: 时间线
p = ROOT / "014-ChannelPrinciple.md"
new = (
    "```mermaid\ntimeline\n"
    "    title Go channel 演进时间线\n"
    "    1978: CSP（Hoare 提出理论模型）\n"
    "    2012: Go 1.0 hchan + sendq/recvq + ring buffer\n"
    "    2014: Go 1.3 P/M/G 调度器，gopark/goready 集成\n"
    "    2015: Go 1.5 runtime 自举（C → Go）\n"
    "    2018: Go 1.11 channel 性能优化（reduce lock hold time）\n"
    "    2020: Go 1.14 异步抢占，preemptoff 保护\n"
    "    2022: Go 1.18 泛型 channel\n"
    "    2024: Go 1.22 range over function 实验\n"
    "```"
)
results.append(("014-timeline", replace_block(p, "CSP (1978)", new)))

# 014 chansend 状态机（用唯一标记：chansend1）
new2 = (
    "```mermaid\nflowchart TD\n"
    "    A[chansend1(ch, v)] --> B[ch.lock.acquire()]\n"
    "    B --> C{ch.closed == 1?}\n"
    "    C -- Yes --> P1[panic: send on closed channel]\n"
    "    C -- No --> D[sg := ch.recvq.dequeue]\n"
    "    D --> E{sg != nil（有等待 recv）?}\n"
    "    E -- Yes --> F[sendDirect(sg, v)]\n"
    "    F --> G[goready(sg.g)]\n"
    "    G --> H[ch.lock.release()]\n"
    "    H --> I[return]\n"
    "    E -- No --> J{ch.qcount < ch.dataqsiz?}\n"
    "    J -- Yes（有缓冲空间） --> K[buf[sendx] = v]\n"
    "    K --> L[sendx = (sendx+1) mod dataqsiz]\n"
    "    L --> M[qcount++]\n"
    "    M --> N[ch.lock.release()]\n"
    "    N --> O[return]\n"
    "    J -- No（buf 已满） --> Q[gopark(chanpark)]\n"
    "    Q --> R[将 sudog 入 sendq]\n"
    "    R --> S[ch.lock.release()]\n"
    "```"
)
results.append(("014-chansend", replace_block(p, "chansend1(ch, v)", new2)))

# 014 chanrecv 状态机
new3 = (
    "```mermaid\nflowchart TD\n"
    "    A[chanrecv1(ch, &v)] --> B[ch.lock.acquire()]\n"
    "    B --> D[sg := ch.sendq.dequeue]\n"
    "    D --> E{sg != nil（有等待 send）?}\n"
    "    E -- Yes --> F[recvDirect(sg, v)]\n"
    "    F --> G[goready(sg.g)]\n"
    "    G --> H[ch.lock.release()]\n"
    "    H --> I[return true]\n"
    "    E -- No --> J{ch.qcount > 0?}\n"
    "    J -- Yes（buf 有数据） --> K[v = buf[recvx]]\n"
    "    K --> L[recvx = (recvx+1) mod dataqsiz]\n"
    "    L --> M[qcount--]\n"
    "    M --> N[ch.lock.release()]\n"
    "    N --> O[return true]\n"
    "    J -- No（buf 空） --> Q{ch.closed?}\n"
    "    Q -- Yes --> R[return zero, false]\n"
    "    Q -- No --> S[gopark(chanpark)]\n"
    "    S --> T[sudog 入 recvq]\n"
    "    T --> U[ch.lock.release()]\n"
    "```"
)
results.append(("014-chanrecv", replace_block(p, "chanrecv1(ch, &v)", new3)))

# 017 ContextDetailed: 时间线
p = ROOT / "017-ContextDetailed.md"
new4 = (
    "```mermaid\ntimeline\n"
    "    title Go context 演进时间线\n"
    "    2014: golang.org/x/net/context（Google 内部）\n"
    "    2016: Go 1.7 进入标准库 context\n"
    "    2019: Go 1.13 errors.Is/As 集成\n"
    "    2023: Go 1.21 WithCancelCause / Cause / AfterFunc\n"
    "    2024: Go 1.22 WithoutCancel\n"
    "```"
)
results.append(("017-context", replace_block(p, "进入标准库 context", new4)))

# 020 ErrorHandlingAdvanced: 时间线
p = ROOT / "020-ErrorHandlingAdvanced.md"
new5 = (
    "```mermaid\ntimeline\n"
    "    title Go 错误处理演进时间线\n"
    "    2012: Go 1.0 error 接口，errors.New\n"
    "    2014: Go 1.4 内置 error 类型文档化\n"
    "    2019: Go 1.13 Unwrap / Is / As / %w\n"
    "    2022: Go 1.18 errors.Is 性能优化\n"
    "    2023: Go 1.20 errors.Join / Unwrap() []error\n"
    "    2023: Go 1.21 log/slog 集成\n"
    "    2024: Go 1.22 进一步性能优化\n"
    "```"
)
results.append(("020-errors", replace_block(p, "error 接口，errors.New", new5)))

# 032 GoWasm: 时间线
p = ROOT / "032-GoWasm.md"
new6 = (
    "```mermaid\ntimeline\n"
    "    title Go + WebAssembly 时间线\n"
    "    2015-06: WebAssembly 项目启动（Google/Mozilla/Microsoft/Apple）\n"
    "    2017-03: Wasm 1.0 MVP 规范发布\n"
    "    2018-08: Go 1.11 js/wasm 目标，syscall/js，wasm_exec.js\n"
    "    2019-09: Go 1.13 js.FuncOf 内存管理修复\n"
    "    2021-08: Go 1.17 SSA 后端，wasm 体积减少\n"
    "    2023-08: Go 1.21 WASI Preview 1（wasip1）\n"
    "    2024-02: Wasm GC proposal 落地（Rust/Java/Kotlin 跟进）\n"
    "    2025-02: Go 1.24 wasm pprof，PIE 默认启用\n"
    "```"
)
results.append(("032-wasm", replace_block(p, "WebAssembly 项目启动", new6)))

# 036 GoLog: 日志流
p = ROOT / "036-GoLog.md"
new7 = (
    "```mermaid\nflowchart TD\n"
    "    App[Application Code] --> Logger[slog.Logger]\n"
    "    Logger --> Handler[slog.Handler JSON]\n"
    "    Handler --> Stdout[stdout 容器收集]\n"
    "    Handler --> File[file 本地调试]\n"
    "    Handler --> Kafka[Kafka 日志聚合]\n"
    "    App --> OT[OpenTelemetry]\n"
    "    OT --> JT[Jaeger / Tempo]\n"
    "```"
)
results.append(("036-log", replace_block(p, "Application Code", new7)))

# 041 GoRegex: NFA 连接/闭包图（4 个）
p = ROOT / "041-GoRegex.md"
new8 = (
    "```mermaid\nflowchart LR\n"
    "    S[新 s] -->|ε| N1[N(r1)]\n"
    "    N1 -->|ε| T[新 t]\n"
    "    S -->|ε| N2[N(r2)]\n"
    "    N2 -->|ε| T\n"
    "```"
)
results.append(("041-nfa-concat", replace_block(p, "N(r_1)", new8)))

new9 = (
    "```mermaid\nflowchart LR\n"
    "    S[新 s] -->|ε| N[N(r)]\n"
    "    N -->|ε| T[t]\n"
    "    N -->|ε| S\n"
    "    T -->|ε| N\n"
    "```"
)
results.append(("041-nfa-star", replace_block(p, "N(r) ──ε──> t", new9)))

new10 = (
    "```mermaid\nflowchart LR\n"
    "    S0[状态 0] -->|ε| S2[状态 2]\n"
    "    S2 -->|b| S3[状态 3]\n"
    "    S3 -->|ε| S1[状态 1]\n"
    "    S0 -->|ε| S4[状态 4]\n"
    "    S4 -->|c| S5[状态 5]\n"
    "    S5 -->|ε| S1\n"
    "```"
)
results.append(("041-nfa-alt", replace_block(p, "状态 0 ──ε", new10)))

# 041 GoRegex: 选择图（第二处）
new10b = (
    "```mermaid\nflowchart LR\n"
    "    S[新 s] -->|ε| N1[N(r1)]\n"
    "    N1 -->|ε| T[新 t]\n"
    "    S -->|ε| N2[N(r2)]\n"
    "    N2 -->|ε| T\n"
    "```"
)
results.append(("041-choice", replace_block(p, "N(r_1) ──ε──┐", new10b)))

new11 = (
    "```mermaid\nflowchart LR\n"
    "    S6[状态 6] -->|ε| N[b|c NFA]\n"
    "    N -->|ε| S7[状态 7]\n"
    "    N -->|ε| S6\n"
    "    S7 -->|ε| N\n"
    "```"
)
results.append(("041-nfa-alt2", replace_block(p, "[b|c NFA]", new11)))

# 043 GoPerformanceAnalysis: 时间线
p = ROOT / "043-GoPerformanceAnalysis.md"
new12 = (
    "```mermaid\ntimeline\n"
    "    title Go 性能剖析时间线\n"
    "    1982-01: gprof 论文（Graham/Kessler/McKusick）调用图剖析奠基\n"
    "    2005-01: Google gperftools（含 CPUProfile）发布\n"
    "    2012-03: Go 1.0 runtime/pprof（CPU/heap/goroutine/block/threadcreate）\n"
    "    2013-05: Go 1.1 net/http/pprof，/debug/pprof/ HTTP 端点\n"
    "    2015-08: Go 1.5 runtime 自举，runtime/trace 引入\n"
    "    2017-08: Go 1.9 mutex 剖析（SetMutexProfileFraction）\n"
    "    2017-12: Go 1.10 pprof label（pprof.Do + pprof.Labels）\n"
    "    2022-03: Go 1.18 cgo 下 CPU 剖析修复\n"
    "    2023-08: Go 1.21 PGO、trace 重写\n"
    "    2024-02: Go 1.22 pprof 默认 Web 界面\n"
    "    2024-08: Go 1.23 trace flight recorder\n"
    "    2025-02: Go 1.24 pprof gzip 压缩、testing 联合分析\n"
    "```"
)
results.append(("043-pprof-timeline", replace_block(p, "gprof 论文", new12)))

# 043 连续剖析平台
new13 = (
    "```mermaid\nflowchart TD\n"
    "    subgraph Platform[连续剖析平台]\n"
    "        P1[Pyroscope]\n"
    "        P2[Parca]\n"
    "        P3[Grafana]\n"
    "    end\n"
    "    subgraph Instances[服务实例（多副本）]\n"
    "        A1[App #1 :6060]\n"
    "        A2[App #2 :6060]\n"
    "        A3[App #3 :6060]\n"
    "    end\n"
    "    Instances -->|HTTP 抓取（每 60 秒）| Platform\n"
    "```"
)
results.append(("043-platform", replace_block(p, "│ Pyroscope│", new13)))

# 046 GoOAuth2: 网关多 provider
p = ROOT / "046-GoOAuth2.md"
new14 = (
    "```mermaid\nflowchart TD\n"
    "    C[Client] --> GW[Auth Gateway<br/>统一入口]\n"
    "    GW --> GH[/auth/github → GitHub OAuth2]\n"
    "    GW --> GO[/auth/google → Google OIDC]\n"
    "    GW --> GA[/auth/apple → Apple Sign In]\n"
    "    GW --> GS[/auth/saml → SAML IdP]\n"
    "    GH --> JWT[Local JWT<br/>统一签发本地 JWT]\n"
    "    GO --> JWT\n"
    "    GA --> JWT\n"
    "    GS --> JWT\n"
    "```"
)
results.append(("046-oauth-gateway", replace_block(p, "Auth Gateway", new14)))

# 046 GoOAuth2: 身份链接
new15 = (
    "```mermaid\nflowchart TD\n"
    "    U[User] --> GW[Auth Gateway]\n"
    "    GW --> GH[/auth/github → GitHub OAuth2]\n"
    "    GW --> GO[/auth/google → Google OIDC]\n"
    "    GW --> GA[/auth/apple → Apple Sign In]\n"
    "    GH --> IL[Identity Linker<br/>根据邮箱关联用户]\n"
    "    GO --> IL\n"
    "    GA --> IL\n"
    "    IL --> TI[Token Issuer<br/>签发内部 JWT]\n"
    "    TI --> RS[Refresh Store<br/>Redis 存储 Refresh Token]\n"
    "```"
)
results.append(("046-oauth-linker", replace_block(p, "Identity Linker", new15)))

# 047 GoMiddleware: 时间线
p = ROOT / "047-GoMiddleware.md"
new16 = (
    "```mermaid\ntimeline\n"
    "    title Go 中间件演进时间线\n"
    "    2003-01: Python WSGI（PEP 333）规范化中间件概念\n"
    "    2007-01: Ruby Rack 沿用中间件模式\n"
    "    2010-05: Node.js Connect/Express 中间件生态兴起\n"
    "    2012-03: Go 1.0 net/http，Handler/HandlerFunc 接口\n"
    "    2014-06: gin 框架发布，自定义 HandlerFunc\n"
    "    2015-07: chi、echo 框架发布，兼容标准库中间件\n"
    "    2016-08: Go 1.7 context.Context 引入 http.Request\n"
    "    2024-02: Go 1.22 ServeMux 方法匹配、路径参数、Use 方法\n"
    "    2025-02: Go 1.24 进一步优化 ServeMux 性能（radix tree）\n"
    "```"
)
results.append(("047-middleware-timeline", replace_block(p, "2003-01", new16)))

# 047 洋葱模型
new17 = (
    "```mermaid\nflowchart LR\n"
    "    Req[请求] --> A[中间件A前置] --> B[中间件B前置] --> C[中间件C前置] --> H[核心 Handler]\n"
    "    H --> C2[中间件C后置] --> B2[中间件B后置] --> A2[中间件A后置] --> Res[响应]\n"
    "```"
)
results.append(("047-onion", replace_block(p, "请求 ─→", new17)))

# 049 Go: 熔断器状态机
p = ROOT / "049-Go.md"
new18 = (
    "```mermaid\nstateDiagram-v2\n"
    "    [*] --> Closed\n"
    "    Closed --> Open: 失败率超阈值\n"
    "    Open --> HalfOpen: 等待 Timeout\n"
    "    HalfOpen --> HalfOpen: 失败\n"
    "    HalfOpen --> Closed: 成功 N 次\n"
    "    HalfOpen --> Open: 成功\n"
    "```"
)
results.append(("049-circuit", replace_block(p, "Closed ─", new18)))

# 056 GenericDetailed: 时间线
p = ROOT / "056-GenericDetailed.md"
new19 = (
    "```mermaid\ntimeline\n"
    "    title Go 泛型演进时间线\n"
    "    2010-2017: 早期泛型研究（type function）\n"
    "    2018: Contracts 提案（被否决）\n"
    "    2020: Type Parameters 提案（采纳）\n"
    "    2022: Go 1.18 泛型正式发布\n"
    "    2023: Go 1.20 comparable 改进\n"
    "    2023: Go 1.21 slices/maps 标准库\n"
    "    2024: Go 1.22 range over function\n"
    "```"
)
results.append(("056-generic", replace_block(p, "早期泛型研究", new19)))

for name, ok in results:
    print(f"{name}: {ok}")
