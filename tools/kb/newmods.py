# -*- coding: utf-8 -*-
"""新增知识模块知识库（项目技术栈与补充语言）。"""

KB_NEW = {}


def _n(label, hint, history, theory, pitfalls, practices, comparisons, engineering,
       case, summary, refs, more, deep):
    axes = [
        f"能够说出 {label} 的核心概念、工具与工作流。",
        f"能够解释 {label} 的关键机制与设计取舍。",
        f"能够独立完成 {label} 的标准开发任务。",
        f"能够分析 {label} 在真实项目中的问题与边界。",
        f"能够评价 {label} 相关技术选型。",
        f"能够把 {label} 集成进完整项目体系。",
    ]
    return {
        "label": label, "related_title_hint": hint, "axes": axes,
        "history": history, "history_tail": [], "definitions": theory[:3],
        "theory": theory, "pitfalls": pitfalls, "practices": practices,
        "comparisons": comparisons, "engineering": engineering, "case": case,
        "summary": summary, "refs": refs, "more": more,
        "supplement_examples": [], "deep_topics": deep,
    }


KB_NEW["rust"] = _n(
    "Rust", "所有权、借用、生命周期、Cargo",
    [
        "Rust 由 Graydon Hoare 于 2006 年在 Mozilla 开始研发，2010 年公开，2015 年 1.0 发布；设计目标是在系统编程中同时获得内存安全与高性能。",
        "2016-2024 年 Rust 连续在 Stack Overflow 开发者调查中被评为“最受喜爱的语言”；2021 年 Rust Foundation 成立，Linux 内核与 Windows 内核开始接纳 Rust 组件。",
        "核心特性：所有权（ownership）、借用（borrowing）、生命周期（lifetime）、零成本抽象、Cargo 构建系统与 crates.io 生态；2024 年起 edition 2024 持续演进。",
    ],
    [
        "所有权：每个值有唯一所有者；所有者离开作用域值被释放；转移（move）与复制（copy）决定赋值行为。",
        "借用与引用：&T 不可变借用、&mut T 可变借用；同一时刻要么多个不可变借用，要么一个可变借用——编译期消除数据竞争。",
        "生命周期：引用必须标注有效范围（多数可推断），保证引用不悬垂。",
        "Cargo：包管理、构建、测试、文档一体化；crates.io 提供丰富生态。",
    ],
    [
        ("借用冲突", "同时持有可变与不可变借用。重构数据流或使用内部可变性（RefCell）。"),
        ("生命周期标注恐慌", "多数可省略；复杂结构需显式标注，先理解“谁拥有谁”。"),
        ("unwrap 滥用", "生产代码 unwrap 导致 panic。使用 Result 与错误传播（? 运算符）。"),
        ("String 与 &str 混淆", "String 拥有缓冲区，&str 是切片；函数参数优先 &str。"),
        ("循环引用泄漏", "Rc 循环引用导致内存泄漏。使用 Weak。"),
        ("unsafe 误用", "unsafe 绕过检查需要严格论证。优先安全抽象。"),
        ("异步生态碎片", "tokio/async-std 选择需统一。按团队选一个生态。"),
        ("编译时间", "泛型与依赖导致编译慢。合理拆分 crate 与增量编译。"),
    ],
    [
        "默认不可变：变量与绑定优先 let 而非 let mut。",
        "错误处理：Result + ? 传播，自定义错误类型实现 From。",
        "测试：单元测试与集成测试目录分离，cargo test 全量运行。",
        "文档：rustdoc 文档注释（///）与 doctest 结合。",
    ],
    [
        "Rust 与 C/C++：Rust 编译期内存安全、工具链现代；C++ 生态成熟灵活。新系统项目考虑 Rust。",
        "Rust 与 Go：Go 简单并发强，Rust 精细控制与零成本抽象；服务端两者皆可。",
        "2015 edition 与 2024 edition：edition 是兼容性里程碑，新项目用最新 edition。",
    ],
    [
        "项目结构：src/lib.rs（库）、src/main.rs（二进制）、tests/（集成测试）；workspace 管理多 crate。",
        "性能：零成本抽象、无 GC；profile.release 优化；benchmark 用 criterion。",
        "生态：Web 后端（Axum/Actix）、CLI（clap）、嵌入式、Wasm。",
    ],
    [
        "需求：实现并发安全的计数器与 Web 服务。",
        "方案：Arc<Mutex<T>> 或原子类型 + Axum 路由。",
        "要点：所有权设计先行；错误类型统一；测试覆盖并发。",
        "验证：cargo test、clippy 零告警、基准测试。",
    ],
    [
        "Rust 的价值是“编译期安全”：所有权系统消灭整类内存错误。",
        "学习曲线陡峭但回报高，适合系统编程与性能敏感服务。",
        "工程基线：cargo fmt、clippy、测试与文档。",
    ],
    [
        "Rust 官方文档：https://www.rust-lang.org/zh-CN/learn",
        "Rust 程序设计语言（中文书）：https://kaisery.github.io/trpl-zh-cn/",
        "Rust 标准库文档：https://doc.rust-lang.org/std/",
        "crates.io：https://crates.io/",
        "Rust 异步编程：https://rust-lang.github.io/async-book/",
    ],
    [
        "Rust 与 C 对比（内存安全），见 025-c 模块。",
        "Rust 与 C++ 对比，见 026-cpp 模块。",
        "系统编程与嵌入式，见 035-iot 模块。",
        "黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 Rust 课程。",
    ],
    [
        ("所有权与借用检查器", [
            "移动语义：赋值与传参转移所有权；Copy 类型（整数、布尔）按位复制不移动。",
            "借用规则：不可变借用可并行；可变借用独占；借用不可超过所有者生命周期。",
            "内部可变性：RefCell 运行时检查借用；Mutex 跨线程；原子类型无锁。",
            "排错：按编译器错误逐条修复，理解“借用冲突”的三个要素（值、借用类型、作用域）。",
        ]),
        ("异步 Rust 与 Tokio", [
            "async/await 基于 Future 与执行器；tokio 提供多线程运行时与任务调度。",
            "异步陷阱：阻塞调用卡死执行器（用 spawn_blocking）；锁跨 await（用 tokio::sync）。",
            "Select 与流（Stream）组合并发任务；超时用 tokio::time::timeout。",
            "性能：任务数而非线程数；背压与缓冲设计。",
        ]),
    ],
)

KB_NEW["shell"] = _n(
    "Shell", "命令、脚本、管道、进程控制",
    [
        "Unix Shell 诞生于 1970 年代（Thompson shell、Bourne shell），是系统管理与自动化的核心接口；POSIX 规范统一语法。",
        "现代 Shell 家族：bash（默认）、zsh（交互增强）、fish（友好）、PowerShell（Windows）；Linux 服务器脚本以 bash 为主。",
        "应用：文件处理、日志分析、部署脚本、CI 步骤、系统监控；是 DevOps 与后端开发的基本功。",
    ],
    [
        "命令与参数：命令 + 选项 + 参数；环境变量与 PATH；exit code 表达成败。",
        "管道与重定向：| 连接命令流，> / >> / < 重定向；2>&1 合并错误流。",
        "脚本结构：#!/bin/bash shebang、变量、条件（if/test/[[ ]]）、循环（for/while）、函数。",
        "进程控制：& 后台、wait、jobs；信号（kill、trap）与进程组。",
    ],
    [
        ("忘记引号", "文件名含空格被拆分。变量一律双引号包裹。"),
        ("set -e 缺失", "命令失败继续执行。脚本开头 set -euo pipefail。"),
        ("使用废弃语法", "` ` 命令替换过时。用 $( )。"),
        ("误删文件", "rm -rf 无确认。先列出目标，谨慎使用。"),
        ("变量名冲突", "覆盖 PATH 等系统变量。使用前缀命名。"),
        ("管道丢失退出码", "管道只返回最后命令状态。用 pipefail 或 PIPESTATUS。"),
        ("脚本不可移植", "依赖 GNU 扩展。POSIX 兼容优先。"),
        ("无错误处理", "失败静默。检查 $? 或 set -e。"),
    ],
    [
        "脚本首行 set -euo pipefail，声明严格模式。",
        "函数化组织：main 函数 + 子命令风格。",
        "所有外部输入校验；临时文件用 mktemp。",
        "用 shellcheck 静态检查。",
    ],
    [
        "bash 与 PowerShell：bash 类 Unix 标准，PowerShell 对象管道适合 Windows 管理。",
        "脚本与工具：复杂文本处理可用 awk/sed，更复杂逻辑用 Python。",
        "sh 与 bash：sh 是 POSIX 子集，bash 扩展更丰富。",
    ],
    [
        "部署脚本：构建、测试、发布步骤串联；失败即停止。",
        "日志处理：grep/awk/sort/uniq 组合分析；cron 定时任务。",
        "CI：GitHub Actions 的 run 步骤即 Shell；本地与 CI 行为一致。",
    ],
    [
        "需求：编写备份脚本（打包 + 加密 + 上传 + 清理）。",
        "方案：tar + gpg + rsync/oss + find 清理旧备份。",
        "要点：严格模式、日志、失败告警、幂等。",
        "验证：模拟故障（磁盘满、网络断）验证行为。",
    ],
    [
        "Shell 的价值是“胶水”：把工具串成自动化。",
        "严格模式与错误处理是脚本质量的基线。",
        "复杂逻辑交给专门语言，Shell 保持薄层。",
    ],
    [
        "Bash 参考手册：https://www.gnu.org/software/bash/manual/",
        "ShellCheck：https://www.shellcheck.net/",
        "Explain Shell：https://explainshell.com/",
        "Bash 陷阱：https://mywiki.wooledge.org/BashPitfalls",
    ],
    [
        "Shell 与 Linux 命令，见 001-getting-started/012-CommandLineBasics 文档。",
        "CI/CD 中的 Shell，见 031-devops 模块。",
        "文本处理工具，见 051-data-analysis 模块相关文档。",
        "尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Linux 课程。",
    ],
    [
        ("bash 严格模式详解", [
            "set -e：命令非零退出即终止；注意管道与 if 条件的例外。",
            "set -u：未定义变量报错；配合 ${var:-default} 提供默认。",
            "set -o pipefail：管道任一段失败整体失败。",
            "陷阱：set -e 在函数内与 && 链的行为差异；用 set -x 调试。",
        ]),
        ("文本处理三剑客", [
            "grep：行匹配与正则；-E 扩展正则、-r 递归、-v 反选。",
            "sed：流编辑；s/查找/替换/、-n p 打印、地址范围。",
            "awk：列处理与统计；$NF 最后一列、BEGIN/END 块。",
            "组合：管道串联三剑客完成日志统计报表。",
        ]),
    ],
)

KB_NEW["astro"] = _n(
    "Astro", "静态站点、岛屿架构、内容集合、SSR",
    [
        "Astro 于 2021 年发布，定位“内容驱动网站”的 Web 框架：默认零 JS 输出，按需注入交互（岛屿架构）；2024-2025 年 Astro 5-7 持续演进。",
        "核心理念：默认静态、按需增强——页面在构建期渲染为 HTML，只有显式组件（岛屿）才携带客户端 JS，兼顾性能与交互。",
        "能力版图：内容集合（Content Collections/Content Layer）、Markdown/MDX、视图过渡（View Transitions）、服务端渲染（SSR）与适配器（Node/Netlify/Cloudflare）。",
    ],
    [
        "页面与路由：src/pages 文件即路由；.astro 组件由 frontmatter（---）与模板组成。",
        "岛屿架构：<Component client:load> 等指令决定 JS 何时加载；无指令的组件仅服务端渲染。",
        "内容集合：src/content 或 Content Layer 定义 schema，类型安全地加载 Markdown/MDX；getCollection 查询。",
        "构建管线：Vite 底层驱动，集成 Tailwind、MDX、Shiki 代码高亮；astro build 输出静态或 SSR 产物。",
    ],
    [
        ("JS 全部打包", "岛屿指令缺失导致页面变重。按交互需求选 client: 指令。"),
        ("前端框架混用", "React/Vue 混合增加包体。统一一个框架。"),
        ("图片未优化", "大图拖慢 LCP。使用 Astro 图片组件与 Image 服务。"),
        ("内容 schema 缺失", "frontmatter 随意导致站点异常。内容集合强制校验。"),
        ("SSR 误用", "全站 SSR 丢失静态优势。按页面选择输出模式。"),
        ("构建缓存失效", "内容变化不重建。理解缓存与 CI 策略。"),
        ("忽略 404 与 RSS", "站点完整性缺失。配置 404 页与 RSS。"),
        ("依赖版本漂移", "Astro 升级破坏 API。锁定版本与升级指南。"),
    ],
    [
        "组件最小化：静态内容不引 JS；交互封装为独立岛屿。",
        "内容与展示分离：内容集合管数据，组件管渲染。",
        "性能预算：Lighthouse 全绿为目标，图片与字体优化。",
        "SEO 内置：路由、sitemap、RSS、规范链接。",
    ],
    [
        "Astro 与 Next.js：Astro 内容站性能极致、默认静态；Next.js 全栈与生态更重。",
        "Astro 与 VitePress：Astro 通用内容站 + 自定义 UI；VitePress 文档站开箱即用。",
        "岛屿架构与 MPA/SPA：MPA 多页天然轻；SPA 交互连续但 JS 重；Astro 按需融合。",
    ],
    [
        "文档站模式：内容集合 + 自动目录 + 搜索集成 + 视图过渡。",
        "部署：静态托管（Netlify/Vercel/GitHub Pages）或 SSR 适配器。",
        "工程化：ESLint + Prettier + CI 构建校验 + 链接检查。",
    ],
    [
        "需求：用 Astro 重构 FANDEX 文档站。",
        "方案：内容集合管理 2000+ 文档、MDX 组件、岛屿搜索、RSS 与 sitemap。",
        "要点：文档 frontmatter schema、目录导航生成、构建性能。",
        "验证：构建零错误、Lighthouse 评分、全站链接检查。",
    ],
    [
        "Astro 的核心是“内容优先、按需交互”。",
        "岛屿架构让性能与交互兼得。",
        "内容集合是文档站的类型安全基座。",
    ],
    [
        "Astro 官方文档：https://docs.astro.build/zh-cn/",
        "Astro 主题市场：https://astro.build/themes/",
        "Astro 集成：https://astro.build/integrations/",
        "Astro 博客：https://astro.build/blog/",
    ],
    [
        "Vite 构建机制，见 056-vite 模块。",
        "Markdown/MDX 写作，见 002-markdown 模块。",
        "Tailwind 样式，见 058-tailwind 模块。",
        "尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供前端工程化课程。",
    ],
    [
        ("内容集合与类型安全", [
            "定义 schema（zod）：title、description、日期、标签；集合加载时校验。",
            "getCollection('docs') 返回类型化条目；slug 由文件名或 frontmatter 决定。",
            "Content Layer（Astro 5+）：从远程或本地数据源加载，缓存策略可配置。",
            "实践：文档站把全部课程文档注册为集合，目录与搜索基于集合生成。",
        ]),
        ("岛屿架构原理", [
            "静态页面输出 HTML 与 CSS；client:load 组件单独打包为岛屿脚本。",
            "指令：client:load（加载即水合）、client:idle（空闲）、client:visible（可见）、client:only（仅客户端）。",
            "水合成本：每个岛屿独立 JS 块，页面级状态传递用 store（nanostores）。",
            "性能分析：astro build 报告每页 JS 大小，按报告调整指令。",
        ]),
    ],
)

KB_NEW["vite"] = _n(
    "Vite", "开发服务器、HMR、Rollup 构建、插件",
    [
        "Vite 由 Evan You（尤雨溪）于 2020 年发布，基于原生 ES Modules 的开发服务器与 Rollup 生产构建；2021-2025 年成为 Vue/React/Svelte 生态的默认构建工具。",
        "核心创新：开发期按需编译（浏览器直接加载 ESM，依赖预构建用 esbuild）、HMR 毫秒级更新、生产构建用 Rollup 优化。",
        "Vite 6/7 持续演进：环境 API（Environment API）、rolldown 原生打包器（Oxc/Rust 生态）、插件兼容层。",
    ],
    [
        "开发服务器：浏览器请求模块时即时转换（transform），冷启动不打包全部源码。",
        "依赖预构建：node_modules 依赖用 esbuild 预打包为 ESM，缓存于 node_modules/.vite。",
        "HMR：模块图跟踪依赖，变更只更新受影响的模块，保留页面状态。",
        "生产构建：Rollup 树摇、代码分割、资源内联与哈希；manifest 输出供后端集成。",
    ],
    [
        ("生产与开发不一致", "依赖开发特性导致构建异常。CI 必跑 build。"),
        ("大依赖未拆包", "单 chunk 过大。manualChunks 与动态导入。"),
        ("环境变量暴露", "VITE_ 前缀变量进入客户端。敏感信息走服务端。"),
        ("HMR 失效", "修改配置或插件未重启。热更失败时整页刷新兜底。"),
        ("路径别名未配置", "相对路径混乱。resolve.alias + tsconfig paths。"),
        ("忽略 target", "现代浏览器与旧浏览器产物不同。按需求设 build.target。"),
        ("插件顺序", "插件顺序影响转换结果。遵循官方文档顺序。"),
        ("缓存不失效", "node_modules/.vite 与 dist 缓存。必要时强制刷新。"),
    ],
    [
        "配置分层：vite.config.ts 单一入口，环境变量控制模式。",
        "别名与路径：@ 指向 src，类型同步。",
        "性能：依赖优化、代码分割、资源压缩（esbuild/terser）。",
        "质量：build 前跑 lint 与类型检查。",
    ],
    [
        "Vite 与 Webpack：Vite 开发快、配置简洁；Webpack 生态旧项目存量。",
        "esbuild 与 Rollup：esbuild 快但产物优化弱；Rollup 精细。Vite 组合两者。",
        "Vite 与 Turbopack：Turbopack 是 Next.js 方向；Vite 生态更开放。",
    ],
    [
        "框架集成：@vitejs/plugin-react、@vitejs/plugin-vue、SSR 支持。",
        "多页应用：多入口 HTML 配置；库模式输出 ESM/UMD。",
        "测试集成：Vitest 复用 Vite 配置；Playwright E2E。",
    ],
    [
        "需求：为 React 文档站配置 Vite 构建。",
        "方案：别名、代理、代码分割、环境变量、CI 构建。",
        "要点：产物大小监控、HMR 体验、部署路径 base 配置。",
        "验证：build 零错误、产物分析（rollup-plugin-visualizer）。",
    ],
    [
        "Vite 的成功来自“原生 ESM + 按需编译”的开发体验。",
        "开发与生产双引擎各司其职，理解差异才能排错。",
        "配置保持精简，插件按需引入。",
    ],
    [
        "Vite 官方文档：https://cn.vitejs.dev/",
        "Vite 插件市场：https://github.com/vitejs/awesome-vite",
        "Vitest：https://cn.vitest.dev/",
        "Rollup 文档：https://rollupjs.org/",
    ],
    [
        "Astro 构建集成 Vite，见 055-astro 模块。",
        "前端框架工程化，见 011-react/010-vue3 模块。",
        "Monorepo 中的 Vite，见 057-pnpm-monorepo 模块。",
        "尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Vite 课程。",
    ],
    [
        ("HMR 协议与模块图", [
            "模块图：文件到模块的映射；变更触发依赖链分析。",
            "HMR API：import.meta.hot.accept/decline；框架插件自动接入。",
            "边界：非模块化脚本与 CSS 的更新策略；失效时整页 reload。",
            "调试：vite --debug 观察转换与更新日志。",
        ]),
        ("构建优化实战", [
            "代码分割：动态 import 路由级分包；manualChunks 聚合稳定依赖。",
            "资源优化：图片压缩、SVG 内联、字体子集。",
            "产物分析：rollup-plugin-visualizer 识别大块。",
            "缓存策略：文件哈希 + 长期缓存头。",
        ]),
    ],
)

KB_NEW["pnpm-monorepo"] = _n(
    "pnpm 与 Monorepo", "workspace、目录、依赖隔离、发布",
    [
        "Monorepo（单仓库多包）通过统一仓库管理多应用与共享包，Google/Meta/微软等大厂实践成熟；pnpm 以“内容寻址存储 + 严格依赖隔离”成为 Node 生态主流。",
        "pnpm 核心：全局内容寻址存储（硬链接）、符号链接 node_modules、隔离依赖（防幽灵依赖）、workspace 协议。",
        "工程形态：apps/（应用）+ packages/（共享库）+ tools/（工具）；catalog 统一依赖版本；Turborepo/Nx 提供任务编排。",
    ],
    [
        "内容寻址存储：依赖按内容存储一次，跨项目硬链接，节省磁盘；不同版本共存。",
        "严格 node_modules：依赖只对声明它的包可见，消除幽灵依赖（依赖未声明却可用）。",
        "workspace：pnpm-workspace.yaml 声明包目录；workspace:* 协议链接本地包。",
        "catalog：集中定义依赖版本，各包用 catalog: 引用，避免版本漂移。",
    ],
    [
        ("幽灵依赖", "未声明的包被隐式使用。pnpm 默认隔离，CI 用 frozen-lockfile。"),
        ("构建顺序", "依赖包未先构建。用 --filter 与拓扑排序（turbo/pnpm -r）。"),
        ("版本漂移", "各包依赖版本不一致。catalog 统一。"),
        ("循环依赖", "包间循环导致构建失败。重新分层。"),
        ("node_modules 膨胀", "重复安装。验证 pnpm store 复用与 dedupe。"),
        ("忽略 lockfile", "环境不一致。pnpm-lock.yaml 必须提交。"),
        ("大仓库 CI 慢", "全量任务浪费时间。增量缓存（turbo）与按需构建。"),
        ("发布顺序", "发布本地依赖前需构建与版本更新。changesets 管理。"),
    ],
    [
        "包命名与目录规范：@scope/name、apps/packages 分层。",
        "依赖显式声明：禁止隐式使用兄弟包。",
        "脚本统一：根 package.json 提供 dev/build/typecheck 聚合命令。",
        "变更管理：changesets 记录并自动发布。",
    ],
    [
        "pnpm 与 npm/yarn：pnpm 磁盘高效、依赖隔离严格；npm 兼容性最广。",
        "Monorepo 与多仓库：Monorepo 原子变更与统一依赖；多仓独立治理。",
        "Turborepo 与 Nx：都是任务编排器；按团队偏好选择。",
    ],
    [
        "FANDEX 即采用 pnpm workspace：app-web/app-desktop/app-android 三应用 + shd-shared 共享层 + tls-tools 工具链。",
        "CI：pnpm install --frozen-lockfile -> filter 构建 -> 缓存（turbo）。",
        "发布：changesets 版本化、Changelog 生成、npm 发布。",
    ],
    [
        "需求：在 Monorepo 中搭建共享 UI 包并被两个应用引用。",
        "方案：packages/ui + workspace:* 依赖 + 构建顺序配置。",
        "要点：类型声明导出、样式隔离、版本管理。",
        "验证：两应用构建通过、依赖图正确、发布流程演练。",
    ],
    [
        "pnpm 的核心价值是严格的依赖管理与高效的存储。",
        "Monorepo 的收益来自统一治理，代价是工具链复杂度。",
        "catalog、lockfile、changesets 是工程化三件套。",
    ],
    [
        "pnpm 官方文档：https://pnpm.io/zh/",
        "pnpm workspace 文档：https://pnpm.io/zh/workspaces",
        "Turborepo：https://turborepo.com/",
        "Changesets：https://changesets-docs.vercel.app/",
        "Monorepo 模式（Nx 博客）：https://nx.dev/blog/",
    ],
    [
        "FANDEX 项目结构解析，见 058-pnpm-monorepo 模块文档。",
        "Vite 多包构建，见 056-vite 模块。",
        "CI/CD 与发布，见 031-devops 模块。",
        "黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供工程化课程。",
    ],
    [
        ("pnpm 存储与链接机制", [
            "全局 store：按内容哈希存储包；硬链接到项目 node_modules/.pnpm。",
            "符号链接：项目直接依赖链接到 .pnpm 中对应版本；间接依赖不暴露。",
            "hoist 选项：shamefully-hoist 模拟 npm 扁平结构（慎用）。",
            "诊断：pnpm store status、why 命令分析依赖来源。",
        ]),
        ("Monorepo 任务编排", [
            "拓扑构建：先构建依赖再构建应用；pnpm -r --topological。",
            "缓存：turbo 按输入哈希缓存任务结果；远程缓存加速 CI。",
            "过滤器：--filter 精确选择任务范围；affected 模式只跑变更相关。",
            "并行与限制：--parallel 与 --concurrency 平衡资源。",
        ]),
    ],
)

KB_NEW["tailwind"] = _n(
    "Tailwind CSS", "工具类、配置、主题、响应式",
    [
        "Tailwind CSS 由 Adam Wathan 于 2017 年发布，定位“实用优先”（utility-first）的 CSS 框架；2023 年 Tailwind 4 重写为 CSS-first 配置与原生引擎。",
        "核心理念：不预设组件样式，提供原子工具类（utilities），在 HTML 中组合出设计；配合设计令牌实现一致主题。",
        "Tailwind 4：CSS 配置（@theme）、原生层叠、Vite 插件、自动内容检测；v3 的 tailwind.config.js 仍可兼容迁移。",
    ],
    [
        "工具类体系：布局（flex/grid）、间距（p-4/m-2）、排版（text-lg/font-bold）、颜色（bg-red-500）、响应式前缀（sm:/md:/lg:）。",
        "内容检测：扫描源码中的类名，只生成使用到的 CSS（JIT）；内容配置决定扫描范围。",
        "设计令牌：颜色/字体/间距在 @theme 定义，生成对应工具类；暗色模式用 dark: 变体。",
        "组合与复用：@apply 提取重复类；组件类与工具类并存策略由团队约定。",
    ],
    [
        ("类名遗漏扫描", "动态拼接类名不被识别。完整类名写全，或 safelist。"),
        ("滥用 @apply", "回到“语义类”老路且增加复杂度。适度使用。"),
        ("样式优先级", "工具类冲突。用变体与顺序，避免 !important 泛滥。"),
        ("响应式断点臆造", "随意断点导致碎片化。遵循预设断点（sm/md/lg/xl/2xl）。"),
        ("主题覆盖混乱", "直接改默认色值。统一在 @theme 定义。"),
        ("暗色模式未配置", "dark: 不生效。确认 darkMode 策略。"),
        ("构建产物大", "全量生成。验证内容路径覆盖所有模板。"),
        ("与内联样式混用", "维护困难。统一工具类。"),
    ],
    [
        "设计令牌先行：颜色、字体、圆角、间距在主题中定义。",
        "组件模式：UI 组件用工具类组合，页面级样式保持声明式。",
        "响应式移动优先：默认样式为移动端，sm: 起增强。",
        "与框架集成：Vite 插件 + PostCSS，React/Vue 组件内直接使用。",
    ],
    [
        "Tailwind 与 CSS Modules：Tailwind 全局工具类快速一致；CSS Modules 组件隔离。可混合。",
        "Tailwind 与 Bootstrap：Bootstrap 预设组件开箱即用；Tailwind 灵活定制无预设。",
        "v3 与 v4：v4 CSS-first 配置与原生性能；新项目用 v4。",
    ],
    [
        "设计系统落地：令牌 + 组件库（Radix + Tailwind）+ 暗色模式。",
        "性能：JIT 产物极小；CDN 版仅原型。",
        "质量：类名排序（prettier-plugin-tailwindcss）、lint 检查。",
    ],
    [
        "需求：为文档站实现统一主题与暗色模式。",
        "方案：@theme 定义令牌、dark 变体、组件类封装。",
        "要点：语义色（primary/surface/text）而非裸色值。",
        "验证：主题切换一致性、对比度、产物体积。",
    ],
    [
        "Tailwind 的价值是“约束下的效率”：令牌与工具类保证一致与快速。",
        "CSS-first 配置（v4）简化了工程集成。",
        "好的团队规范：令牌统一、变体统一、组件复用。",
    ],
    [
        "Tailwind 官方文档：https://tailwindcss.com/docs",
        "Tailwind 中文文档：https://www.tailwindcss.cn/docs",
        "Tailwind UI 组件：https://tailwindui.com/",
        "prettier-plugin-tailwindcss：https://github.com/tailwindlabs/prettier-plugin-tailwindcss",
    ],
    [
        "CSS 基础与变量，见 007-css 模块。",
        "Astro + Tailwind 集成，见 055-astro 模块。",
        "设计系统与主题，见 007-css 模块相关文档。",
        "尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Tailwind 课程。",
    ],
    [
        ("Tailwind 4 的 CSS-first 配置", [
            "@theme 块定义令牌：--color-primary 生成 bg-primary 等工具类。",
            "原生层叠：@layer 管理 theme/base/components/utilities 顺序。",
            "自动检测：源码扫描无需配置文件；自定义来源用 @source。",
            "与 Vite：@tailwindcss/vite 插件一步集成。",
        ]),
        ("组件复用策略", [
            "方案一：纯工具类 + 组件封装（React 组件、Astro 组件）。",
            "方案二：@apply 提取可复用类（注意 v4 语法变化）。",
            "方案三：CSS 变量 + 工具类组合，动态主题。",
            "选择依据：团队规模、设计系统成熟度、主题需求。",
        ]),
    ],
)
