# -*- coding: utf-8 -*-
"""前端技术类模块知识库。"""

KB_FRONTEND = {}


def _m(label, hint, history, theory, pitfalls, practices, comparisons, engineering,
       case, summary, refs, more, deep, axes=None):
    axes = axes or [
        f"能够说出 {label} 的核心概念、术语与标准写法。",
        f"能够解释 {label} 的工作原理与设计动机。",
        f"能够编写符合 {label} 规范的完整实现。",
        f"能够分析 {label} 与相邻方案的差异与边界。",
        f"能够根据场景评价 {label} 相关方案的优劣。",
        f"能够组合 {label} 与其他技术设计完整方案。",
    ]
    return {
        "label": label, "related_title_hint": hint, "axes": axes,
        "history": history, "history_tail": [], "definitions": theory[:3],
        "theory": theory, "pitfalls": pitfalls, "practices": practices,
        "comparisons": comparisons, "engineering": engineering, "case": case,
        "summary": summary, "refs": refs, "more": more,
        "supplement_examples": [], "deep_topics": deep,
    }


KB_FRONTEND["html5"] = _m(
    "HTML5", "语义化、表单、多媒体、Canvas",
    [
        "HTML 由 Tim Berners-Lee 于 1991 年创建，是 Web 的结构语言；HTML5 于 2014 年成为 W3C 推荐标准，WHATWG 维护的 Living Standard 是当前权威规范。",
        "HTML5 引入语义化元素（header/nav/main/article/section/footer）、表单增强（date/range/placeholder）、多媒体（video/audio）、图形（canvas/SVG）与离线存储（localStorage/Web Worker）。",
        "现代 HTML 强调“语义优先”：结构表达内容含义，样式与行为分离；可访问性（ARIA）与 SEO 都建立在正确语义之上。",
    ],
    [
        "文档结构：<!DOCTYPE html> 声明标准模式；html/head/body 层级固定；meta charset 必须在前 1024 字节内。",
        "语义元素：header/footer 表示页眉页脚，nav 表示导航，main 表示主内容（每页唯一），article 表示独立内容，section 表示分区。",
        "表单：input 类型决定键盘与校验（email/url/number），label 关联控件提升可访问性，required/pattern 提供原生校验。",
        "媒体与图形：video/audio 支持多源（source）；canvas 是位图画布（JavaScript 绘制），SVG 是矢量结构（DOM 操作）。",
    ],
    [
        ("div 滥用", "全部用 div 导致语义缺失。优先语义元素，div 仅作无语义容器。"),
        ("img 缺 alt", "图片无法访问时无替代文本。alt 描述内容，装饰图用空 alt。"),
        ("标题层级跳变", "h1 直接到 h3 破坏文档大纲。按层级使用标题。"),
        ("按钮用 a 标签", "动作语义错误。导航用 a，动作用 button。"),
        ("表单无 label", "辅助技术无法识别控件。每个输入关联 label。"),
        ("脚本阻塞渲染", "同步脚本放 body 底部或用 defer。"),
        ("内联样式与事件", "内联 style/onclick 破坏分离。使用 class 与 addEventListener。"),
        ("忽略 meta viewport", "移动端布局异常。添加 viewport meta。"),
    ],
    [
        "结构、样式、行为三层分离。",
        "每个页面唯一 main，标题层级连贯。",
        "图片提供 alt 与尺寸（防 CLS）。",
        "表单控件全部关联 label，错误信息可编程关联。",
        "使用 W3C 校验器与 axe 检查。",
    ],
    [
        "HTML5 与 XHTML：HTML5 容错性强、语法宽松；XHTML 严格 XML 语法，已基本退出。",
        "语义元素与 div+class：语义元素免费获得可访问性与 SEO；class 命名方案只是风格。",
        "canvas 与 SVG：canvas 适合像素级绘制（游戏、图像处理），SVG 适合矢量图形与交互（图表、图标）。",
    ],
    [
        "可访问性基线：语义元素 + ARIA（仅补充）+ 键盘可达 + 对比度达标（WCAG 2.1 AA）。",
        "性能：图片懒加载（loading=lazy）、字体子集化、资源预加载。",
        "SEO：语义标题、meta description、结构化数据（JSON-LD）。",
    ],
    [
        "需求：重构文档站点首页为语义化结构。",
        "方案：header/nav/main/article/footer 布局，面包屑用 nav + ol，卡片用 article。",
        "要点：标题层级从 h1 开始连续；所有图片 alt；表单字段 label 关联。",
        "验证：W3C 校验零错误；axe 扫描无严重问题；移动端视口正常。",
    ],
    [
        "HTML 是内容的骨架，语义决定信息能否被机器与人共同理解。",
        "HTML5 的特性围绕“结构、媒体、交互”三条线展开。",
        "可访问性不是附加项，而是 HTML 的一部分。",
    ],
    [
        "WHATWG HTML Living Standard：https://html.spec.whatwg.org/",
        "MDN HTML 文档：https://developer.mozilla.org/zh-CN/docs/Web/HTML",
        "W3C Markup Validation Service：https://validator.w3.org/",
        "WebAIM 可访问性指南：https://webaim.org/",
    ],
    [
        "HTML 列表与链接精讲，见 006-html5/011-List 与 012-LinkageAnchor 文档。",
        "CSS 样式与布局，见 007-css 模块。",
        "JavaScript DOM 操作，见 008-javascript 模块。",
        "尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 HTML/CSS 课程。",
    ],
    [
        ("HTML 解析与 DOM 树", [
            "浏览器解析 HTML 时先 tokenize 再建树；解析器对错误标记有容错规则（错误恢复算法）。",
            "DOM 是内存中的树结构：元素节点、文本节点、属性；document.querySelector 沿树查找。",
            "渲染流程：HTML -> DOM，CSS -> CSSOM，合并为渲染树，布局与绘制；理解流程可定位性能瓶颈。",
            "脚本与解析：defer 延后执行，async 异步执行，模块脚本默认 defer 语义。",
        ]),
        ("表单校验与无障碍", [
            "原生校验：required、pattern、min/max、type 约束；novalidate 可关闭，交由 JS 自定义。",
            "校验 UI：:invalid/:valid 伪类样式；aria-invalid 标记错误；错误信息用 aria-describedby 关联。",
            "键盘可达：所有交互元素可 Tab 聚焦，焦点可见，弹层焦点管理（trap）。",
            "屏幕阅读器测试：NVDA/VoiceOver 实际朗读验证语义。",
        ]),
    ],
)

KB_FRONTEND["css"] = _m(
    "CSS", "选择器、盒模型、布局、动画、响应式",
    [
        "CSS 于 1994 年由 Håkon Wium Lie 提出，1996 年 CSS1 发布，解决 HTML 表现层混杂问题；CSS2.1（2011）与 CSS3 模块化（2012+）奠定现代 Web 样式基础。",
        "现代 CSS 的能力版图：Flexbox/Grid 布局、自定义属性（变量）、容器查询、子网格、层叠层（@layer）、现代颜色（oklch）。",
        "CSS 的设计核心是“层叠与继承”：来源、优先级、顺序共同决定最终样式；理解层叠是排查样式问题的前提。",
    ],
    [
        "选择器与优先级：id > class/属性/伪类 > 元素/伪元素；!important 打破优先级（应避免）。",
        "盒模型：content/padding/border/margin，box-sizing 决定 width 语义（border-box 推荐）。",
        "布局体系：普通流、浮动（历史）、Flexbox（一维）、Grid（二维）；position 定位（relative/absolute/fixed/sticky）。",
        "层叠上下文：z-index 只在同一层叠上下文中比较；transform/opacity/filter 创建新上下文。",
    ],
    [
        ("!important 滥用", "覆盖链失控。通过优先级与结构设计解决。"),
        ("全局选择器", "* 选择器影响性能与意外覆盖。使用类与作用域。"),
        ("rem 与 em 混淆", "em 相对父级字体，rem 相对根；嵌套 em 累积。间距字号统一 rem。"),
        ("固定像素布局", "不可响应。使用流式单位、clamp 与断点。"),
        ("z-index 魔法数字", "层级失控。用层叠上下文与令牌。"),
        ("样式覆盖顺序依赖", "过度依赖源顺序。用 @layer 声明层。"),
        ("动画性能", "动画 width/height 触发布局。使用 transform/opacity。"),
        ("flex 溢出", "子项默认不收缩文本溢出。min-width: 0 修正。"),
    ],
    [
        "类名语义化（BEM 或类似），避免 id 样式。",
        "设计令牌：颜色、间距、字号用自定义属性统一。",
        "移动优先媒体查询 + 容器查询组合。",
        "重置/基线：现代用相对重置（如基于 margin 0 + 继承）。",
        "提交前检查对比度与焦点样式。",
    ],
    [
        "Flexbox 与 Grid：一维布局（导航、按钮组）用 Flex；二维布局（页面网格、卡片墙）用 Grid。",
        "浮动与现代布局：浮动是文字环绕工具，布局已由 Flex/Grid 取代。",
        "媒体查询与容器查询：视口级用媒体查询，组件级用容器查询。",
    ],
    [
        "组件样式隔离：CSS Modules、Tailwind（工具类）、CSS-in-JS 各有权衡；团队统一。",
        "性能：选择器避免深嵌套；动画只动 transform/opacity；字体与图片优化。",
        "主题：自定义属性 + prefers-color-scheme 实现浅深色切换。",
    ],
    [
        "需求：实现响应式卡片网格，支持浅深色与减少动画。",
        "方案：Grid + auto-fill/minmax、CSS 变量主题、prefers-reduced-motion。",
        "要点：断点内容驱动；变量集中定义；动画降级。",
        "验证：多视口截图对比、axe 可访问性扫描、Lighthouse 性能。",
    ],
    [
        "CSS 的复杂度来自层叠与上下文，掌握它们就掌握了排错的钥匙。",
        "现代 CSS 已能覆盖大部分布局需求，预处理器只是增强。",
        "响应式与主题化是工程基座，令牌与变量是基础设施。",
    ],
    [
        "MDN CSS 文档：https://developer.mozilla.org/zh-CN/docs/Web/CSS",
        "CSS 规范（W3C）：https://www.w3.org/Style/CSS/",
        "CSS-Tricks：https://css-tricks.com/",
        "Can I use：https://caniuse.com/",
        "Tailwind CSS：https://tailwindcss.com/",
    ],
    [
        "CSS 圆角与形状，见 007-css/018-BorderRadius 文档。",
        "CSS 媒体查询与响应式，见 007-css/019-MediaQuery 文档。",
        "CSS 函数与变量，见 007-css/022-Function 文档。",
        "HTML 结构与语义，见 006-html5 模块。",
        "黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 CSS 课程。",
    ],
    [
        ("层叠上下文全解", [
            "层叠上下文由根、position+z-index、flex/grid 子项 z-index、opacity<1、transform、filter、backdrop-filter、contain、will-change 等创建。",
            "上下文内的 z-index 只在内部比较；子上下文整体参与父级排序。",
            "常见事故：fixed 弹窗被父级 transform 包裹后定位与层级异常。",
            "调试：DevTools 层叠上下文可视化；避免不必要的 will-change。",
        ]),
        ("现代布局：Grid 与容器查询", [
            "Grid 模板：grid-template-columns 的 fr、minmax、auto-fill；命名区域提升可读性。",
            "容器查询：container-type: inline-size 定义容器，@container 查询容器宽度，组件可移植。",
            "子网格（subgrid）继承父网格轨道，适合对齐嵌套组件。",
            "浏览器支持与回退：@supports 特性检测；移动端优先降级。",
        ]),
    ],
)

KB_FRONTEND["vue3"] = _m(
    "Vue 3", "组合式 API、响应式、组件通信、路由、状态管理",
    [
        "Vue 由尤雨溪于 2014 年发布，以“渐进式框架”定位：可作库嵌入，也可作框架构建完整应用。Vue 3 于 2020 年 9 月发布，核心是组合式 API 与全新响应式系统。",
        "Vue 3 的技术支柱：Proxy 响应式（替代 Object.defineProperty）、虚拟 DOM 重写（PatchFlags）、Fragment/Teleport/Suspense 内置组件、组合式 API（setup/ref/reactive/computed）。",
        "生态现状：Vue Router 4、Pinia（官方状态库）、Vite 构建、Nuxt 全栈框架；Vue 3.5 引入 useTemplateRef 等开发者体验改进。",
    ],
    [
        "响应式：ref 包装基本类型，reactive 包装对象；effect 收集依赖，Proxy 拦截读写；computed 缓存派生值。",
        "组件通信：props 向下、emit 向上、v-model 双向、provide/inject 跨层、事件总线（慎用）。",
        "生命周期：setup 在创建前执行；onMounted/onUpdated/onUnmounted 对应挂载、更新、卸载；KeepAlive 增加 activated/deactivated。",
        "模板编译：模板在构建期编译为渲染函数，指令（v-if/v-for/v-model）是编译糖。",
    ],
    [
        ("响应式丢失", "解构 reactive 或赋值整对象丢失响应。使用 ref/toRefs。"),
        ("v-for key 用索引", "列表变更导致状态错位。使用稳定唯一 key。"),
        ("props 直接修改", "单向数据流被破坏。通过 emit 通知父组件修改。"),
        ("watch 深层陷阱", "监听对象默认浅层；深层用 deep 或改写为 getter。"),
        ("组件样式泄漏", "未用 scoped 导致全局污染。组件样式默认 scoped。"),
        ("setup 中 async 误用", "setup 顶层 await 变为异步组件需 Suspense。"),
        ("路由组件复用不刷新", "参数变化组件复用。watch route 或 beforeRouteUpdate。"),
        ("响应式大对象性能", "深层代理开销大。大数据用 shallowRef 或冻结。"),
    ],
    [
        "组合式 API 按逻辑组织（自定义组合函数 useXxx）。",
        "组件单一职责，props 使用类型定义（TS）。",
        "状态管理：局部状态用 ref，跨组件用 Pinia，服务端状态用 Query 类库。",
        "模板保持声明式，复杂逻辑进 script。",
    ],
    [
        "Vue 与 React：Vue 模板 + 响应式自动追踪，React JSX + 手动依赖（hooks）；Vue 上手平缓，React 生态更广。",
        "Options API 与 Composition API：Composition 更适合逻辑复用与 TS；Options 保留简单场景。",
        "Vue 2 与 Vue 3：响应式实现、API 形态、生态差异显著，新项目一律 Vue 3。",
    ],
    [
        "项目脚手架：create-vue（Vite + TS + Router + Pinia）。",
        "目录分层：views（页面）、components（组件）、composables（逻辑）、stores（状态）、api（请求）。",
        "性能：defineAsyncComponent 懒加载、v-memo 优化、虚拟列表。",
        "测试：Vitest 单测 + Vue Test Utils；Playwright E2E。",
    ],
    [
        "需求：实现文档站的搜索页与主题切换。",
        "方案：Vue Router 路由 + Pinia 管理主题 + 组合函数封装搜索。",
        "要点：搜索防抖与竞态取消；主题变量持久化。",
        "验证：路由守卫权限、主题刷新保持、搜索准确性测试。",
    ],
    [
        "Vue 3 的核心是响应式与组合式：理解依赖收集才能驾驭性能与陷阱。",
        "组件通信按层级选型：props/emit 为默认，provide/inject 跨层，Pinia 全局。",
        "工程化（Vite + TS + 测试）是生产项目的基线。",
    ],
    [
        "Vue 官方文档：https://vuejs.org/",
        "Vue Router：https://router.vuejs.org/zh/",
        "Pinia：https://pinia.vuejs.org/zh/",
        "Vue 3 迁移指南：https://v3-migration.vuejs.org/",
        "VueUse 组合函数库：https://vueuse.org/",
    ],
    [
        "Vue Teleport 与 Portal，见 010-vue3/026-TeleportPortalApp 文档。",
        "Vue KeepAlive 缓存，见 010-vue3/027-KeepAliveCacheLifecycle 文档。",
        "Vue Router 导航守卫，见 010-vue3/030-VueRouterNavigationGuard 文档。",
        "TypeScript 与 Vue 组合，见 009-typescript 模块。",
        "尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Vue3 课程。",
    ],
    [
        ("响应式原理与依赖收集", [
            "ref 内部用 class RefImpl 保存值并收集依赖；reactive 用 Proxy 的 get/set 拦截，依赖以 WeakMap<target, Map<key, Set<effect>>> 存储。",
            "effect 在触发时重新执行，scheduler 控制批处理（微任务队列）；computed 用惰性求值与缓存标志。",
            "渲染更新：组件渲染函数是 effect，数据变化触发重渲染；Vue 的更新粒度到组件级，配合虚拟 DOM diff。",
            "调试：onRenderTracked/onRenderTriggered 追踪依赖；性能面板观察更新频率。",
        ]),
        ("组合函数与可复用逻辑", [
            "组合函数（composable）以 use 前缀命名，内部可组合 ref/computed/watch/lifecycle，实现逻辑复用。",
            "示例：useFetch 封装请求状态（data/error/loading）与取消；useLocalStorage 同步持久化。",
            "与 Mixin 对比：组合函数无命名冲突、显式依赖、类型友好。",
            "工程规范：每个组合函数单一职责，返回只读引用防止外部破坏。",
        ]),
    ],
)

KB_FRONTEND["react"] = _m(
    "React", "组件、Hooks、状态管理、渲染性能",
    [
        "React 由 Facebook 于 2013 年开源，核心思想是组件化 UI 与声明式渲染；2019 年 React 16.8 引入 Hooks，函数组件成为主流。",
        "React 19（2024）引入 Actions、useOptimistic、编译器（React Compiler）自动记忆化；并发特性（Suspense、Transitions）持续完善。",
        "生态：Next.js/Remix 全栈框架、TanStack Query 服务端状态、Zustand/Redux 客户端状态、React Native 移动端。",
    ],
    [
        "组件模型：props 输入、state 内部状态、渲染输出 JSX；组件是纯函数，同一输入必得同一输出。",
        "Hooks 规则：只能在顶层调用（不可在条件/循环中），函数组件与自定义 Hook 内使用；依赖数组决定 effect 重跑。",
        "渲染与协调：setState 触发重渲染，虚拟 DOM diff 更新真实 DOM；key 帮助复用元素。",
        "状态提升与下放：共享状态提升到最近公共祖先；Context 跨层传递（Provider/useContext）。",
    ],
    [
        ("setState 直接修改", "直接修改 state 对象不触发渲染。创建新对象/数组。"),
        ("依赖数组缺失", "effect 捕获旧值。按需列出依赖或用函数式更新。"),
        ("条件调用 Hooks", "违反 Hooks 规则导致渲染错乱。把条件放组件内或拆分组件。"),
        ("key 用索引", "列表重排导致状态错位。使用稳定 id。"),
        ("Context 过度使用", "Context 变更使所有消费者重渲染。拆分 Context 或选择状态库。"),
        ("内存泄漏", "异步回调在卸载后 setState。用 cleanup 与取消标志。"),
        ("受控组件误用", "value 无 onChange 导致输入锁定。受控必须成对。"),
        ("性能过早优化", "useMemo/useCallback 滥用。先测量再优化。"),
    ],
    [
        "组件默认不可变数据流：props 只读，状态用函数式更新。",
        "自定义 Hook 封装副作用与复用逻辑。",
        "服务端状态用 TanStack Query，客户端全局状态用 Zustand。",
        "React Compiler（19）开启后减少手工 memo。",
    ],
    [
        "React 与 Vue：React JSX 全 JS、生态自由组合；Vue 模板 + 响应式自动追踪。团队偏好与既有代码决定选择。",
        "函数组件与类组件：函数 + Hooks 是现代标准，类组件仅维护存量。",
        "CSR 与 SSR：CSR 交互快、SSR SEO 好；Next.js 按页选择渲染模式。",
    ],
    [
        "项目结构：components/features/hooks/lib；colocation（相关文件就近）。",
        "请求层：TanStack Query 管理缓存、重试、失效；错误边界兜底。",
        "性能：代码分割（React.lazy）、虚拟列表（TanStack Virtual）、渲染分析（React DevTools Profiler）。",
        "测试：Vitest + Testing Library（行为优先）+ Playwright。",
    ],
    [
        "需求：实现文档列表页，支持搜索、筛选与分页。",
        "方案：TanStack Query 数据层 + Zustand UI 状态 + 受控表单。",
        "要点：查询键设计、防抖搜索、错误与空态处理。",
        "验证：加载/错误/空态测试；请求缓存命中验证。",
    ],
    [
        "React 的核心是“数据驱动视图”：状态变化驱动渲染，渲染结果可预测。",
        "Hooks 是逻辑复用与副作用管理的载体，规则必须严格遵守。",
        "工程基线：TS、测试、服务端状态库与性能分析。",
    ],
    [
        "React 官方文档：https://react.dev/",
        "React 19 发布说明：https://react.dev/blog/2024/12/05/react-19",
        "TanStack Query：https://tanstack.com/query/latest",
        "Zustand：https://zustand.docs.pmnd.rs/",
        "Next.js：https://nextjs.org/",
    ],
    [
        "React Hooks 深入，见 011-react 模块 Hooks 文档。",
        "React 与 TypeScript 类型，见 009-typescript 模块。",
        "前端构建与 Vite，见 057-vite 模块（如已加入）。",
        "黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 React 课程。",
    ],
    [
        ("渲染原理与协调", [
            "React 渲染分阶段：render（构建元素树）、reconcile（diff）、commit（DOM 变更与副作用）。",
            "diff 算法基于类型与 key：同类型复用实例，不同类型重建；列表 diff 按 key 匹配。",
            "并发特性：useTransition 标记低优先级更新可中断；Suspense 等待异步边界。",
            "React Compiler 自动记忆组件，减少手工 useMemo。",
        ]),
        ("状态架构模式", [
            "状态分类：服务端状态（缓存数据）与客户端状态（UI 偏好）；分开管理。",
            "TanStack Query：查询键（queryKey）+ 缓存生命周期（staleTime/gcTime）+ 失效策略。",
            "Zustand：create 定义 store，selector 订阅切片，避免多余渲染。",
            "表单状态：受控 + 校验库（React Hook Form + Zod）。",
        ]),
    ],
)

KB_FRONTEND["svg"] = _m(
    "SVG", "矢量图形、路径、变换、动画",
    [
        "SVG（可缩放矢量图形）于 2001 年由 W3C 标准化，是 Web 原生矢量格式；与位图不同，SVG 由几何描述构成，任意缩放不失真。",
        "SVG 是 XML 方言：元素即图形（rect/circle/path），样式可用 CSS，交互可用事件；SPA 生态中常以内联 SVG 与图标组件使用。",
        "现代应用：图标系统、数据可视化（D3）、地图、LOGO、动画与交互图形；浏览器对 SVG 的支持已非常完整。",
    ],
    [
        "坐标系：viewBox 定义逻辑坐标（min-x min-y width height），preserveAspectRatio 控制缩放对齐。",
        "基本图形：rect（矩形）、circle（圆）、ellipse（椭圆）、line（直线）、polyline/polygon（折线/多边形）。",
        "路径 path：M/L/C/Q/A 命令组合任意曲线；fill 填充、stroke 描边。",
        "变换与动画：transform 平移缩放旋转；CSS/SMIL 动画控制属性过渡。",
    ],
    [
        ("viewBox 缺失", "缩放行为异常。始终定义 viewBox 与宽高。"),
        ("无命名空间", "内联 SVG 需 xmlns；HTML5 中内联可省略但外部文件必须。"),
        ("路径命令错误", "坐标格式错误导致图形缺失。检查命令字母与数字。"),
        ("fill-rule 混淆", "非零环绕与奇偶规则结果不同。按需选择。"),
        ("动画性能", "逐帧修改 DOM 属性卡顿。使用 transform 与 CSS 动画。"),
        ("可访问性缺失", "SVG 无 role/title 时屏幕阅读器忽略。添加 role=\"img\" 与 title。"),
        ("字体依赖", "text 元素依赖系统字体。需要一致性时转路径或使用 web 字体。"),
    ],
    [
        "图标组件化（React/Vue）统一尺寸与样式。",
        "图形语义化：装饰用 aria-hidden，信息图提供 title/desc。",
        "性能：复用 symbol/use 减少重复；大图使用懒加载。",
    ],
    [
        "SVG 与 canvas：SVG 矢量、可交互、DOM 友好；canvas 位图、高性能、适合游戏。",
        "SVG 与 PNG：SVG 无损缩放、体积小；PNG 兼容极旧环境但位图放大模糊。",
        "SMIL 与 CSS 动画：CSS 更现代，SMIL 支持部分高级特性；现代项目优先 CSS/Web Animations。",
    ],
    [
        "图标系统：symbol + use 组合 sprite；图标组件接受 size/color props。",
        "数据可视化：D3 生成 SVG 元素；响应式 viewBox 自适应容器。",
        "优化：SVGO 压缩；关键图形内联，非关键用 img 懒加载。",
    ],
    [
        "需求：实现带 hover 交互的折线统计图。",
        "方案：D3 计算坐标生成 path，CSS 过渡动画，tooltip 跟随。",
        "要点：viewport 响应式；坐标轴刻度清晰；无数据时显示空态。",
        "验证：多分辨率截图、交互测试、axe 可访问性。",
    ],
    [
        "SVG 是 Web 的矢量基础设施，理解坐标系与路径就掌握了核心。",
        "内联 SVG 可被 CSS/JS 完全控制，是组件化图标的理想载体。",
        "性能与可访问性并重：复用、压缩、语义化。",
    ],
    [
        "MDN SVG 文档：https://developer.mozilla.org/zh-CN/docs/Web/SVG",
        "SVG 规范（W3C）：https://www.w3.org/TR/SVG2/",
        "SVGO 优化工具：https://github.com/svg/svgo",
        "D3.js：https://d3js.org/",
    ],
    [
        "SVG 图形语法，见 012-svg 模块文档。",
        "CSS 样式与动画，见 007-css 模块。",
        "React/Vue 图标组件实践，见 011-react/010-vue3 模块。",
        "黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供前端图形课程。",
    ],
    [
        ("path 命令详解", [
            "M（移动到）、L（直线）、H/V（水平/垂直线）、C（三次贝塞尔）、S（平滑贝塞尔）、Q（二次贝塞尔）、A（圆弧）、Z（闭合）。",
            "圆弧 A 参数：rx ry x-axis-rotation large-arc-flag sweep-flag x y；flag 组合决定四条弧线。",
            "贝塞尔曲线适合圆角、波浪与平滑曲线；C 需要两个控制点，Q 一个。",
            "实践：用可视化编辑器生成路径，理解命令便于手工调整。",
        ]),
        ("SVG 动画与交互", [
            "CSS 动画：transform/opacity 过渡；stroke-dasharray 实现描边动画。",
            "SMIL：animate/animateTransform 可控制路径运动；兼容性良好但项目中使用渐少。",
            "JS 交互：事件监听 + 属性更新；Framer Motion 等库封装 SVG 动画。",
            "性能：动画元素独立层；避免布局属性动画。",
        ]),
    ],
)

KB_FRONTEND["harmonyos"] = _m(
    "HarmonyOS", "ArkTS、ArkUI、分布式能力、应用开发",
    [
        "HarmonyOS（鸿蒙）由华为于 2019 年发布，定位面向全场景的分布式操作系统；HarmonyOS NEXT（5.0，2024）去 Android 化，采用自研鸿蒙内核与 ArkTS 语言栈。",
        "开发框架：ArkTS（TS 超集 + 声明式 UI 扩展）、ArkUI（声明式组件）、Stage 模型（应用模型）、方舟编译器。",
        "分布式能力：跨端流转、分布式数据、一次开发多端部署（手机/平板/车机/穿戴）。",
    ],
    [
        "ArkTS 语法：基于 TypeScript 的类型系统，增加 @Component/@Entry/@State 等装饰器与 UI 描述语法。",
        "ArkUI 组件：Column/Row/Stack 布局容器、Text/Button/Image 基础组件、List/Grid 容器组件；状态管理（@State/@Prop/@Link/@Provide）。",
        "应用模型：Stage 模型以 UIAbility 为页面载体，EntryAbility 入口；module.json5 声明应用配置。",
        "生命周期：Ability 的 onCreate/onWindowStageCreate/onForeground/onBackground/onDestroy。",
    ],
    [
        ("状态未响应", "普通变量赋值不触发 UI 更新。使用 @State 装饰。"),
        ("组件复用 key", "ForEach 缺 key 导致渲染错位。提供稳定键。"),
        ("异步回调更新状态", "非 UI 线程直接改状态。使用主线程回调或状态管理 API。"),
        ("资源引用错误", "字符串硬编码无法国际化。使用 $r 资源引用。"),
        ("分布式能力误用", "跨端能力需权限与用户确认。优先单端能力。"),
        ("内存泄漏", "事件监听未移除。onDisappear/onDestroy 清理。"),
        ("版本兼容", "新 API 在旧版本不可用。使用 canIUse 或版本判断。"),
    ],
    [
        "组件化与状态分层：UI 状态用装饰器，业务状态用 AppStorage/单例。",
        "页面路由：router 或 Navigation 组件；参数传递类型化。",
        "调试：DevEco Studio 预览器、Profiler、日志分级。",
    ],
    [
        "ArkTS 与 TypeScript：ArkTS 是 TS 子集扩展（禁部分动态特性），UI 语法不同。",
        "ArkUI 与 Compose/SwiftUI：声明式思想一致，组件与状态机制各有特色。",
        "Stage 与 FA 模型：Stage 是新标准，FA 为早期模型。",
    ],
    [
        "工程结构：entry 模块（UIAbility）、common 公共能力、resources 资源目录。",
        "测试：HarmonyOS 测试框架 + DevEco 自动化。",
        "发布：HAP 打包、签名、上架华为应用市场。",
    ],
    [
        "需求：实现跨端待办应用首页（手机 + 平板自适应）。",
        "方案：ArkUI 响应式布局（断点）+ @State 列表 + 本地持久化。",
        "要点：ForEach key、删除动画、空态设计。",
        "验证：双端预览、数据持久化、无障碍检查。",
    ],
    [
        "HarmonyOS 开发以 ArkTS/ArkUI 为核心，声明式 UI 与现代前端心智模型一致。",
        "Stage 模型与生命周期是应用骨架，状态管理决定 UI 响应。",
        "多端与分布式是差异化能力，按场景选用。",
    ],
    [
        "华为开发者联盟 HarmonyOS 文档：https://developer.huawei.com/consumer/cn/harmonyos",
        "ArkTS 语言规范：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-overview",
        "ArkUI 组件参考：https://developer.huawei.com/consumer/cn/doc/harmonyos-references/",
        "DevEco Studio：https://developer.huawei.com/consumer/cn/deveco-studio/",
    ],
    [
        "TypeScript 基础（ArkTS 语言底座），见 009-typescript 模块。",
        "声明式 UI 概念与 React/Vue 对比，见 011-react/010-vue3 模块。",
        "移动端应用架构，见 018-harmonyos 模块文档。",
        "尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供鸿蒙开发课程。",
    ],
    [
        ("ArkUI 状态管理模型", [
            "页面级：@State（组件内）、@Prop（单向）、@Link（双向）、@Provide/@Consume（跨层级）。",
            "应用级：AppStorage 全局存储、LocalStorage 页面共享；PersistentStorage 持久化。",
            "更新机制：装饰器变量变化触发组件渲染；复杂状态用状态管理类（V2 状态管理）。",
            "实践：状态就近原则，跨组件先考虑提升与 provide/consume。",
        ]),
        ("分布式开发基础", [
            "分布式软总线：设备发现与连接，跨端调用（Ability 迁移）。",
            "分布式数据：KV Store 同步；分布式任务调度跨设备执行。",
            "权限与隐私：敏感能力需权限声明与用户授权。",
            "实践：先单端验证功能，再引入分布式场景。",
        ]),
    ],
)
