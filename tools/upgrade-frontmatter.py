# -*- coding: utf-8 -*-
"""为指定文档注入论文级 frontmatter 扩展字段（learningObjectives/exercises/references/etymology 等）。

用法：
    python tools/upgrade-frontmatter.py <rel1> <rel2> ...
"""

from __future__ import annotations

import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
FULL = ROOT / "cnt-content" / "full"

# 每篇文档的扩展字段（由对应专题内容提炼）
UPGRADES = {
    "007-css/018-BorderRadius.md": {
        "description": "border-radius 完整原理：1-4 值语法、椭圆半径、百分比计算、圆角裁剪规则与常见形状实现。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述 border-radius 的 1-4 值展开规则与斜杠（/）分隔的椭圆半径语法。", "verifiable": "默写四种简写示例并标注对应角"},
            {"level": "understand", "objective": "能解释百分比半径如何参照元素尺寸计算，以及圆角曲线与边框的交集关系。", "verifiable": "用 100px 宽 200px 高的元素说明 50% 圆角结果"},
            {"level": "apply", "objective": "能实现圆形、胶囊、叶片、对话框气泡等常见形状。", "verifiable": "编写五种形状的完整 CSS 代码"},
            {"level": "analyze", "objective": "能分析圆角不裁剪内容的原因以及 overflow: hidden 的作用。", "verifiable": "对比有无 overflow 时的渲染差异"},
            {"level": "evaluate", "objective": "能评价百分比与固定值在不同场景下的可维护性。", "verifiable": "给出响应式设计的选值依据"},
            {"level": "create", "objective": "能独立设计一套带圆角体系的设计令牌并应用到组件库。", "verifiable": "完成案例研究中的按钮与卡片组件"},
        ],
        "exercises": [
            {"id": "radius-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "border-radius: 10px 20px 30px 40px 中，第二个值 20px 作用于_____角。", "answer": "右上角", "explanation": "四值顺序为左上、右上、右下、左下（顺时针）。", "difficulty": "easy"},
            {"id": "radius-02", "type": "choice", "cognitiveLevel": "understand", "question": "一个 200px 宽、100px 高的元素设置 border-radius: 50%，渲染结果是什么？", "options": ["A. 正圆形", "B. 椭圆形（横向椭圆）", "C. 胶囊形", "D. 无变化"], "answer": "B", "explanation": "50% 的水平和垂直半径分别按宽高的一半计算，宽高不同因此得到椭圆。", "difficulty": "medium"},
        ],
        "references": [
            {"type": "documentation", "authors": ["MDN Web Docs"], "year": 2026, "title": "border-radius - CSS: Cascading Style Sheets", "venue": "MDN Web Docs", "url": "https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius", "accessedDate": "2026-08-01"},
            {"type": "standard", "authors": ["W3C"], "year": 2025, "title": "CSS Backgrounds and Borders Module Level 3", "venue": "W3C", "url": "https://www.w3.org/TR/css-backgrounds-3/", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "圆角", "english": "border-radius", "origin": "由 border（边框）与 radius（半径）组合而成，指用圆形或椭圆弧线替代边框的直角。"}],
    },
    "007-css/019-MediaQuery.md": {
        "description": "CSS 媒体查询完整原理：@media 语法、媒体特性、响应式断点、深色模式与 matchMedia。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述 @media 语法、四种媒体类型与逻辑操作符（and/逗号/not/only）。", "verifiable": "默写媒体查询骨架"},
            {"level": "understand", "objective": "能解释媒体特性（min-width/orientation/prefers-*）的取值与语义。", "verifiable": "说明 prefers-reduced-motion 的作用"},
            {"level": "apply", "objective": "能实现响应式断点、深色模式与减少动画适配。", "verifiable": "编写完整响应式样式"},
            {"level": "analyze", "objective": "能分析媒体查询与容器查询/数值函数的差异。", "verifiable": "给出同一布局三种方案对比"},
            {"level": "evaluate", "objective": "能评价移动优先（min-width）与桌面优先（max-width）的取舍。", "verifiable": "论证断点设计依据"},
            {"level": "create", "objective": "能设计包含明暗模式与动效偏好的完整主题系统。", "verifiable": "完成案例研究中的主题方案"},
        ],
        "exercises": [
            {"id": "mq-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "媒体类型中默认值是 _____，逻辑或使用 _____ 分隔条件。", "answer": "all；逗号", "explanation": "逗号分隔多条查询等价于 OR。", "difficulty": "easy"},
            {"id": "mq-02", "type": "choice", "cognitiveLevel": "understand", "question": "哪个媒体特性用于检测用户是否偏好减少动画？", "options": ["A. prefers-color-scheme", "B. prefers-reduced-motion", "C. orientation", "D. hover"], "answer": "B", "explanation": "prefers-reduced-motion 尊重系统减少动态效果设置。", "difficulty": "easy"},
        ],
        "references": [
            {"type": "standard", "authors": ["W3C"], "year": 2024, "title": "Media Queries Level 4/5", "venue": "W3C", "url": "https://www.w3.org/TR/mediaqueries-5/", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["MDN Web Docs"], "year": 2026, "title": "Using media queries", "venue": "MDN Web Docs", "url": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "媒体查询", "english": "media query", "origin": "源自 print 样式表时代，后扩展为按设备能力查询条件应用样式。"}],
    },
    "007-css/022-Function.md": {
        "description": "CSS 数值函数完整原理：calc/min/max/clamp 的语法、单位混合规则、嵌套与响应式应用。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述 calc/min/max/clamp 四种函数的语法与语义。", "verifiable": "默写四种函数的最小示例"},
            {"level": "understand", "objective": "能解释 calc 运算规则（空格要求、单位混合、嵌套）与 clamp 的钳制机制。", "verifiable": "说明 clamp(MIN, VAL, MAX) 的三段取值"},
            {"level": "apply", "objective": "能使用 calc 实现流体栅格，用 clamp 实现响应式字号。", "verifiable": "编写完整响应式组件样式"},
            {"level": "analyze", "objective": "能分析 min/max/clamp 与媒体查询在响应式实现上的差异。", "verifiable": "给出同一效果两种方案的对比"},
            {"level": "evaluate", "objective": "能评价数值函数与容器查询/自定义属性的组合边界。", "verifiable": "针对复杂布局给出选型依据"},
            {"level": "create", "objective": "能独立构建基于 clamp 的流体排版系统。", "verifiable": "完成案例研究中的排版系统"},
        ],
        "exercises": [
            {"id": "css-fn-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "calc 表达式中运算符前后必须有 _____，min 函数返回参数中的较_____值。", "answer": "空格；小", "explanation": "calc 要求 + - 两侧空格；min 取最小值，max 取最大值。", "difficulty": "easy"},
            {"id": "css-fn-02", "type": "choice", "cognitiveLevel": "understand", "question": "clamp(1.5rem, 5vw, 3rem) 在 5vw 大于 3rem 时返回？", "options": ["A. 1.5rem", "B. 5vw", "C. 3rem", "D. 报错"], "answer": "C", "explanation": "clamp 将中间值钳制在 [MIN, MAX]，超出 MAX 时返回 MAX。", "difficulty": "medium"},
        ],
        "references": [
            {"type": "standard", "authors": ["W3C"], "year": 2024, "title": "CSS Values and Units Module Level 4", "venue": "W3C", "url": "https://www.w3.org/TR/css-values-4/", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["MDN Web Docs"], "year": 2026, "title": "calc() - CSS", "venue": "MDN Web Docs", "url": "https://developer.mozilla.org/en-US/docs/Web/CSS/calc", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "钳制", "english": "clamp", "origin": "电子学钳位术语，把信号限制在上下限之间。"}],
    },
    "006-html5/011-List.md": {
        "description": "HTML 三类列表（ul/ol/dl）的语义、属性、嵌套规则、无障碍要求与 CSS 样式化技巧。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述 ul、ol、dl 三种列表的语义用途与核心子元素（li/dt/dd）。", "verifiable": "默写三种列表的最小合法结构"},
            {"level": "understand", "objective": "能解释 ol 的 start/reversed/value 属性如何影响编号。", "verifiable": "写出 start=5 reversed 的编号序列"},
            {"level": "apply", "objective": "能编写嵌套列表、定义列表与无障碍友好的列表结构。", "verifiable": "完成一个三层嵌套的购物清单与术语表"},
            {"level": "analyze", "objective": "能分析 CSS 计数器与 list-style-type 在自定义编号上的取舍。", "verifiable": "给出同一效果两种方案的实现与对比"},
            {"level": "evaluate", "objective": "能判断何时应使用列表而非 div 组合，并说明语义化理由。", "verifiable": "对导航、面包屑、评论列表给出元素选择依据"},
            {"level": "create", "objective": "能独立实现带自定义标记、编号与响应式布局的完整列表组件。", "verifiable": "完成案例研究中的导航栏组件"},
        ],
        "exercises": [
            {"id": "html-list-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "无序列表使用 _____ 标签，有序列表使用 _____ 标签，定义列表使用 _____ 标签。", "answer": "ul；ol；dl", "explanation": "ul 用于无顺序语义的集合，ol 用于有顺序的步骤，dl 用于术语-定义对。", "difficulty": "easy"},
            {"id": "html-list-02", "type": "choice", "cognitiveLevel": "understand", "question": "ol start=3 li 中 A 项的编号是？", "options": ["A. 1", "B. 2", "C. 3", "D. 无编号"], "answer": "C", "explanation": "start 属性指定起始编号。", "difficulty": "easy"},
        ],
        "references": [
            {"type": "standard", "authors": ["WHATWG"], "year": 2026, "title": "HTML Standard - The ul element", "venue": "WHATWG", "url": "https://html.spec.whatwg.org/multipage/grouping-content.html#the-ul-element", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["MDN Web Docs"], "year": 2026, "title": "ul: The Unordered List element", "venue": "MDN Web Docs", "url": "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "无序列表", "english": "unordered list", "origin": "用于表达顺序无关的项目集合，浏览器默认渲染为圆点标记。"}],
    },
    "006-html5/012-LinkageAnchor.md": {
        "description": "HTML 超链接与锚点完整指南：href 协议、target/rel 属性、路径系统、安全与可访问性。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述 a 元素的 href/target/rel/download 属性及取值。", "verifiable": "默写属性表"},
            {"level": "understand", "objective": "能解释绝对路径、相对路径与根相对路径的解析规则。", "verifiable": "给定目录结构写出正确路径"},
            {"level": "apply", "objective": "能创建外链、页内锚点、邮件/电话链接与下载链接。", "verifiable": "完成含全部类型的导航示例"},
            {"level": "analyze", "objective": "能分析 target=_blank 的安全风险（reverse tabnabbing）与 rel 缓解。", "verifiable": "解释 noopener/noreferrer 的作用"},
            {"level": "evaluate", "objective": "能评价链接文本对可访问性与 SEO 的影响。", "verifiable": "对比描述性文本与点击这里"},
            {"level": "create", "objective": "能设计带平滑滚动与滚动边距的文档目录导航。", "verifiable": "完成案例研究中的目录组件"},
        ],
        "exercises": [
            {"id": "html-link-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "新窗口打开链接使用 target=_____，同时必须搭配 rel=_____ 防止窗口劫持。", "answer": "_blank；noopener noreferrer", "explanation": "_blank 打开新标签，noopener 切断 opener 引用。", "difficulty": "easy"},
            {"id": "html-link-02", "type": "choice", "cognitiveLevel": "understand", "question": "在 /docs/guide/index.html 中引用 /docs/about.html，正确路径是？", "options": ["A. about.html", "B. ../about.html", "C. /about.html", "D. ./about.html"], "answer": "B", "explanation": "从 guide 子目录回到 docs 目录需 ../about.html。", "difficulty": "medium"},
        ],
        "references": [
            {"type": "standard", "authors": ["WHATWG"], "year": 2026, "title": "HTML Standard - The a element", "venue": "WHATWG", "url": "https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-a-element", "accessedDate": "2026-08-01"},
            {"type": "article", "authors": ["OWASP"], "year": 2024, "title": "Reverse Tabnabbing", "venue": "OWASP", "url": "https://owasp.org/www-community/attacks/Reverse_Tabnabbing", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "锚点", "english": "anchor", "origin": "船锚意象，把页面内的导航锚定到特定位置。"}],
    },
    "010-vue3/026-TeleportPortalApp.md": {
        "description": "Vue 3 Teleport 传送门组件完整应用：to 目标解析、disabled、模态框、通知、遮罩、SSR 与无障碍。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述 Teleport 的两个核心属性（to/disabled）及其默认行为。", "verifiable": "默写 Teleport 最小用法"},
            {"level": "understand", "objective": "能解释渲染位置变化但组件逻辑归属不变的含义。", "verifiable": "说明事件冒泡与 provide/inject 在 Teleport 中的行为"},
            {"level": "apply", "objective": "能实现模态框、通知与全屏遮罩三种典型场景。", "verifiable": "编写三个完整组件"},
            {"level": "analyze", "objective": "能分析 Teleport 与 CSS 层叠上下文、fixed 定位的交互。", "verifiable": "解释为何 modal 需要传送至 body"},
            {"level": "evaluate", "objective": "能评价禁用传送（disabled）与多个目标挂载点的取舍。", "verifiable": "针对 SSR 与移动端给出选择依据"},
            {"level": "create", "objective": "能设计可复用的 BaseModal 组件（含过渡、焦点管理与关闭逻辑）。", "verifiable": "完成案例研究中的完整组件"},
        ],
        "exercises": [
            {"id": "teleport-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "Teleport 的 _____ 属性指定目标容器，_____ 属性为 true 时内容渲染在原位。", "answer": "to；disabled", "explanation": "to 支持 CSS 选择器字符串，disabled 控制是否传送。", "difficulty": "easy"},
            {"id": "teleport-02", "type": "choice", "cognitiveLevel": "understand", "question": "Teleport 传送后，组件内部的响应式状态与事件？", "options": ["A. 状态丢失，事件绑定失效", "B. 状态与事件仍属于原组件，DOM 位置在目标容器", "C. 状态属于目标容器所在组件", "D. 事件冒泡到目标容器而非原组件树"], "answer": "B", "explanation": "Teleport 只改变渲染的 DOM 位置，组件实例、状态、props、事件与依赖注入均不变。", "difficulty": "medium"},
        ],
        "references": [
            {"type": "documentation", "authors": ["Vue.js 团队"], "year": 2026, "title": "Teleport - Vue.js 官方文档", "venue": "vuejs.org", "url": "https://vuejs.org/guide/built-ins/teleport.html", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["MDN Web Docs"], "year": 2026, "title": "CSS position: fixed", "venue": "MDN Web Docs", "url": "https://developer.mozilla.org/en-US/docs/Web/CSS/position", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "传送门", "english": "Teleport", "origin": "借鉴游戏/科幻的瞬移概念，指组件渲染内容在 DOM 树中瞬移到其他位置。"}],
    },
    "010-vue3/027-KeepAliveCacheLifecycle.md": {
        "description": "Vue 3 KeepAlive 组件缓存机制完整解析：include/exclude/max、activated/deactivated 生命周期、缓存刷新与内存管理。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述 KeepAlive 的 include/exclude/max 属性语义与 activated/deactivated 钩子。", "verifiable": "默写属性与钩子对照"},
            {"level": "understand", "objective": "能解释 KeepAlive 缓存树（子树）与普通组件卸载/挂载的差异。", "verifiable": "说明缓存组件状态为何保留"},
            {"level": "apply", "objective": "能配置 Tab 页签缓存策略（指定缓存、排除、最大数量）。", "verifiable": "实现多页签管理组件"},
            {"level": "analyze", "objective": "能分析缓存导致的内存占用与僵尸组件问题。", "verifiable": "给出缓存列表页滚动位置保留方案"},
            {"level": "evaluate", "objective": "能评价缓存与实时数据刷新需求的取舍。", "verifiable": "针对详情页给出缓存与否的依据"},
            {"level": "create", "objective": "能实现基于路由 meta 的动态缓存控制系统。", "verifiable": "完成案例研究中的完整方案"},
        ],
        "exercises": [
            {"id": "keepalive-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "KeepAlive 属性中 _____ 指定缓存白名单，_____ 指定黑名单，_____ 限制最大缓存数。", "answer": "include；exclude；max", "explanation": "include/exclude 匹配组件 name，max 淘汰最久未用的缓存。", "difficulty": "easy"},
            {"id": "keepalive-02", "type": "choice", "cognitiveLevel": "understand", "question": "组件被 KeepAlive 缓存后再次显示时触发哪个钩子？", "options": ["A. onMounted", "B. onActivated", "C. onCreated", "D. onBeforeUnmount"], "answer": "B", "explanation": "缓存组件再次显示触发 onActivated，卸载才触发 onDeactivated。", "difficulty": "medium"},
        ],
        "references": [
            {"type": "documentation", "authors": ["Vue.js 团队"], "year": 2026, "title": "KeepAlive - Vue.js 官方文档", "venue": "vuejs.org", "url": "https://vuejs.org/guide/built-ins/keep-alive.html", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["Vue.js 团队"], "year": 2026, "title": "Lifecycle Hooks - Vue.js 官方文档", "venue": "vuejs.org", "url": "https://vuejs.org/guide/essentials/lifecycle.html", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "保持活跃", "english": "KeepAlive", "origin": "网络协议保活（keep-alive）概念，组件缓存如同连接保活，避免重建开销。"}],
    },
    "010-vue3/030-VueRouterNavigationGuard.md": {
        "description": "Vue Router 导航守卫详解：全局守卫、路由独享守卫、组件内守卫、触发顺序与鉴权实践。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述全局、路由独享、组件内三类守卫及各自钩子名称。", "verifiable": "默写守卫清单与触发顺序"},
            {"level": "understand", "objective": "能解释守卫的返回值语义（true/false/路由对象）与导航确认流程。", "verifiable": "说明三类返回值的导航结果"},
            {"level": "apply", "objective": "能实现登录鉴权、页面标题更新、离开确认与动态权限控制。", "verifiable": "编写四个完整守卫示例"},
            {"level": "analyze", "objective": "能分析守卫触发顺序与组件生命周期钩子的先后关系。", "verifiable": "画出导航解析流程"},
            {"level": "evaluate", "objective": "能评价在守卫中异步获取数据与在组件内获取数据的取舍。", "verifiable": "针对加载体验给出依据"},
            {"level": "create", "objective": "能设计基于路由 meta 的权限守卫体系。", "verifiable": "完成案例研究中的完整方案"},
        ],
        "exercises": [
            {"id": "router-guard-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "全局前置守卫是 _____，全局后置守卫是 _____。", "answer": "beforeEach；afterEach", "explanation": "beforeEach 在导航确认前执行，afterEach 在确认后执行。", "difficulty": "easy"},
            {"id": "router-guard-02", "type": "choice", "cognitiveLevel": "understand", "question": "守卫返回以下哪个值会取消导航？", "options": ["A. true", "B. false", "C. 路由对象", "D. undefined"], "answer": "B", "explanation": "false 取消导航；true/undefined 放行；路由对象重定向。", "difficulty": "medium"},
        ],
        "references": [
            {"type": "documentation", "authors": ["Vue Router 团队"], "year": 2026, "title": "Navigation Guards - Vue Router 官方文档", "venue": "router.vuejs.org", "url": "https://router.vuejs.org/guide/advanced/navigation-guards.html", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["Vue Router 团队"], "year": 2026, "title": "Route Meta Fields - Vue Router 官方文档", "venue": "router.vuejs.org", "url": "https://router.vuejs.org/guide/advanced/meta.html", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "导航守卫", "english": "navigation guard", "origin": "类似门口守卫，在导航进入/离开节点检查放行或拦截。"}],
    },
    "013-java/041-JavaKubernetes.md": {
        "description": "Java 应用在 Kubernetes 上的部署完整指南：资源限制、健康检查、优雅停机、自动伸缩与云原生实践。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述 Kubernetes 核心资源（Deployment/Service/ConfigMap/Secret/HPA/Ingress）的职责。", "verifiable": "默写资源清单与职责对照"},
            {"level": "understand", "objective": "能解释 JVM 容器感知、健康检查与优雅停机的原理。", "verifiable": "说明 MaxRAMPercentage 与 preStop hook 的作用"},
            {"level": "apply", "objective": "能编写 Java 应用的 Deployment、Service、ConfigMap 与探针配置。", "verifiable": "完成一个最小可部署的 YAML 集合"},
            {"level": "analyze", "objective": "能分析 JVM 堆内存、容器 Limit 与 OOMKilled 之间的关系。", "verifiable": "根据内存配置推演 OOM 场景"},
            {"level": "evaluate", "objective": "能评价不同 GC（G1/ZGC）与启动方式（JIT/Native Image）在 K8s 下的取舍。", "verifiable": "针对延迟/吞吐需求给出选型依据"},
            {"level": "create", "objective": "能设计完整的 Java 云原生部署流水线（镜像构建、HPA、监控、滚动更新）。", "verifiable": "完成案例研究中的完整部署方案"},
        ],
        "exercises": [
            {"id": "java-k8s-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "Kubernetes 中管理无状态应用副本数的资源是 _____，提供稳定访问入口的资源是 _____。", "answer": "Deployment；Service", "explanation": "Deployment 管理 Pod 副本与滚动更新，Service 提供稳定的虚拟 IP 与 DNS。", "difficulty": "easy"},
            {"id": "java-k8s-02", "type": "choice", "cognitiveLevel": "understand", "question": "JVM 在容器中识别内存限制的推荐方式是？", "options": ["A. -Xmx 硬编码", "B. -XX:MaxRAMPercentage=75.0", "C. 关闭 GC", "D. 不设置任何参数"], "answer": "B", "explanation": "MaxRAMPercentage 按容器可用内存百分比设置堆上限，适配动态限制。", "difficulty": "medium"},
        ],
        "references": [
            {"type": "documentation", "authors": ["Kubernetes 团队"], "year": 2026, "title": "Kubernetes Documentation - Configure Liveness, Readiness and Startup Probes", "venue": "kubernetes.io", "url": "https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["Microsoft Learn"], "year": 2026, "title": "Containerize your Java applications for Kubernetes", "venue": "Microsoft Learn", "url": "https://learn.microsoft.com/en-us/azure/developer/java/containers/kubernetes", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "容器编排", "english": "orchestration", "origin": "借音乐指挥意象，指统一调度、部署与管理容器集群。"}],
    },
    "014-kotlin/002-KotlinBasicSyntax.md": {
        "description": "Kotlin 基础语法完整讲解：变量声明、基本类型、字符串模板、包与导入、控制流与区间。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述 val 与 var 的区别、Kotlin 八大基本类型名称与区间（Range）语法。", "verifiable": "默写变量声明与区间遍历代码"},
            {"level": "understand", "objective": "能解释 Kotlin 无隐式类型转换与一切皆对象的设计含义。", "verifiable": "说明 Int 与 Long 之间为何必须显式转换"},
            {"level": "apply", "objective": "能使用字符串模板、原始字符串、when 表达式与 for 区间完成日常编码。", "verifiable": "编写一个包含上述特性的完整函数"},
            {"level": "analyze", "objective": "能分析 when 表达式与 Java switch 的差异（穷举性、智能转换、无 fall-through）。", "verifiable": "给出二者对同一逻辑的实现对比"},
            {"level": "evaluate", "objective": "能评价显式类型转换与类型推断在可读性和安全性上的取舍。", "verifiable": "针对团队代码规范给出建议"},
            {"level": "create", "objective": "能独立实现一个基于 when 与区间的命令行评分工具。", "verifiable": "完成案例研究中的完整程序"},
        ],
        "exercises": [
            {"id": "kotlin-basic-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "Kotlin 中只读变量使用 _____ 关键字，可变变量使用 _____ 关键字。", "answer": "val；var", "explanation": "val 只能赋值一次，var 可重新赋值；优先使用 val。", "difficulty": "easy"},
            {"id": "kotlin-basic-02", "type": "choice", "cognitiveLevel": "understand", "question": "关于 Kotlin 数值类型转换，下列说法正确的是？", "options": ["A. Int 可以隐式赋值给 Long", "B. 必须使用 toLong() 等显式转换函数", "C. 转换总是安全的", "D. Float 可以直接赋给 Double"], "answer": "B", "explanation": "Kotlin 不支持隐式拓宽转换，需要显式调用 toLong()/toDouble() 等。", "difficulty": "medium"},
        ],
        "references": [
            {"type": "documentation", "authors": ["JetBrains"], "year": 2026, "title": "Basic syntax - Kotlin Documentation", "venue": "kotlinlang.org", "url": "https://kotlinlang.org/docs/basic-syntax.html", "accessedDate": "2026-08-01"},
            {"type": "standard", "authors": ["JetBrains"], "year": 2026, "title": "Kotlin Language Specification", "venue": "kotlinlang.org", "url": "https://kotlinlang.org/spec/syntax-and-grammar.html", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "只读变量", "english": "val", "origin": "取自 value（值），表示一经赋值不可再变的绑定。"}],
    },
    "016-go/058-RaceDetectionAtomic.md": {
        "description": "Go 竞态检测与原子操作详解：-race 原理、atomic 包、常见竞态模式与无锁编程实践。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述数据竞争的三个必要条件与 -race 标志的启用方式。", "verifiable": "默写 go test -race 命令与竞争条件清单"},
            {"level": "understand", "objective": "能解释 ThreadSanitizer（TSan）在编译期与运行期的工作原理。", "verifiable": "说明 -race 如何插桩并报告竞争"},
            {"level": "apply", "objective": "能使用 sync.Mutex、atomic 包与 channel 三种方式修复数据竞争。", "verifiable": "编写三种修复方案并通过 -race 验证"},
            {"level": "analyze", "objective": "能解读竞态检测报告中的内存地址、goroutine 栈与创建位置。", "verifiable": "针对样例报告指出冲突双方"},
            {"level": "evaluate", "objective": "能评价原子操作、互斥锁与 channel 在不同并发场景下的性能与正确性取舍。", "verifiable": "给出选择依据与基准测试结果"},
            {"level": "create", "objective": "能实现无锁计数器、自旋锁与并发安全配置热更新组件。", "verifiable": "完成案例研究中的三个组件并通过 -race 测试"},
        ],
        "exercises": [
            {"id": "go-race-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "运行测试时启用竞态检测的命令是 go test _____。", "answer": "-race", "explanation": "go test -race ./... 可检测测试覆盖路径上的数据竞争。", "difficulty": "easy"},
            {"id": "go-race-02", "type": "choice", "cognitiveLevel": "understand", "question": "关于 Go 竞态检测器，下列说法错误的是？", "options": ["A. 基于 ThreadSanitizer 实现", "B. 只能发现实际执行到的代码路径上的竞争", "C. 可以证明程序不存在任何数据竞争", "D. 有显著的性能开销"], "answer": "C", "explanation": "竞态检测器只能发现运行过的路径，无法穷尽证明无竞争。", "difficulty": "medium"},
        ],
        "references": [
            {"type": "documentation", "authors": ["Go Team"], "year": 2026, "title": "Data Race Detector - Go Documentation", "venue": "go.dev", "url": "https://go.dev/doc/articles/race_detector", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["Go Team"], "year": 2026, "title": "Package atomic - Go Documentation", "venue": "pkg.go.dev", "url": "https://pkg.go.dev/sync/atomic", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "原子操作", "english": "atomic operation", "origin": "atom 源自希腊语 atomos（不可分割），指不可被并发打断的单一操作。"}],
    },
    "025-c/007-EnumTypedef.md": {
        "description": "C 语言枚举与 typedef 详解：枚举本质、typedef 别名、函数指针、状态机与可移植类型体系。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述 enum 与 typedef 的定义语法与核心语义。", "verifiable": "默写两种语法的最小示例"},
            {"level": "understand", "objective": "能解释枚举在 C 中本质为整数类型，typedef 不创建新类型而只是别名。", "verifiable": "说明枚举与整数的隐式转换规则"},
            {"level": "apply", "objective": "能使用枚举定义状态机、错误码与位标志，并用 typedef 简化函数指针。", "verifiable": "完成三类场景的完整代码"},
            {"level": "analyze", "objective": "能分析枚举名作用域冲突、重复值与位组合的类型安全边界。", "verifiable": "指出两个枚举同名常量的编译错误及解决方式"},
            {"level": "evaluate", "objective": "能评价 X-Macro 等元编程技巧的收益与可维护性代价。", "verifiable": "对比手写映射与 X-Macro 两种实现"},
            {"level": "create", "objective": "能设计可移植的类型别名体系与事件回调架构。", "verifiable": "完成案例研究中的完整模块"},
        ],
        "exercises": [
            {"id": "c-enum-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "C 语言中定义枚举类型的关键字是 _____，定义类型别名的关键字是 _____。", "answer": "enum；typedef", "explanation": "enum 定义枚举类型，typedef 为已有类型创建别名。", "difficulty": "easy"},
            {"id": "c-enum-02", "type": "choice", "cognitiveLevel": "understand", "question": "关于 typedef，下列说法正确的是？", "options": ["A. typedef 创建新的独立类型", "B. typedef 只是为已有类型创建别名", "C. typedef 只能用于结构体", "D. typedef 改变类型的内存布局"], "answer": "B", "explanation": "typedef 不创建新类型，不改变存储与布局。", "difficulty": "medium"},
        ],
        "references": [
            {"type": "documentation", "authors": ["cppreference"], "year": 2026, "title": "Enumeration declaration", "venue": "cppreference.com", "url": "https://en.cppreference.com/w/c/language/enum", "accessedDate": "2026-08-01"},
            {"type": "book", "authors": ["Kernighan, B. W.", "Ritchie, D. M."], "year": 1988, "title": "The C Programming Language (2nd Edition)", "venue": "Prentice Hall", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "枚举", "english": "enumeration", "origin": "来自 enumerate（列举），指把一组具名常量逐一列举出来。"}],
    },
    "026-cpp/062-CppTemplate.md": {
        "description": "C++ 模板完整解析：函数模板、类模板、模板特化、SFINAE、概念（concepts）与现代 C++ 泛型实践。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述函数模板、类模板、模板特化、SFINAE 与概念的定义。", "verifiable": "默写五种模板机制的最小示例"},
            {"level": "understand", "objective": "能解释模板实例化（instantiation）的时机与两阶段查找。", "verifiable": "说明模板定义与实例化的分离"},
            {"level": "apply", "objective": "能编写类型安全的泛型函数、类与约束版本。", "verifiable": "实现泛型容器与算法"},
            {"level": "analyze", "objective": "能分析模板特化与函数重载的解析优先级。", "verifiable": "给出同签名模板/重载/特化的调用结果"},
            {"level": "evaluate", "objective": "能评价 SFINAE 与 C++20 概念两种约束机制的优劣。", "verifiable": "对比代码可读性与错误信息质量"},
            {"level": "create", "objective": "能基于模板实现可复用的泛型组件库（含概念约束）。", "verifiable": "完成案例研究中的泛型容器"},
        ],
        "exercises": [
            {"id": "cpp-tpl-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "函数模板使用 template <_____> 声明，类模板使用 template <_____> 声明。", "answer": "typename T；typename T", "explanation": "类型参数通常用 typename 或 class 关键字声明。", "difficulty": "easy"},
            {"id": "cpp-tpl-02", "type": "choice", "cognitiveLevel": "understand", "question": "关于模板实例化，下列说法正确的是？", "options": ["A. 模板在编译时全部实例化", "B. 只有被使用的具体类型才会触发实例化", "C. 模板与普通函数一样在链接期生成", "D. 实例化发生在运行期"], "answer": "B", "explanation": "模板按需实例化，未使用的类型组合不会生成代码。", "difficulty": "medium"},
        ],
        "references": [
            {"type": "documentation", "authors": ["cppreference"], "year": 2026, "title": "Templates - cppreference.com", "venue": "cppreference.com", "url": "https://en.cppreference.com/w/cpp/language/templates", "accessedDate": "2026-08-01"},
            {"type": "book", "authors": ["Vandevoorde, D.", "Josuttis, N. M.", "Gregor, D."], "year": 2017, "title": "C++ Templates: The Complete Guide", "venue": "Addison-Wesley", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "模板", "english": "template", "origin": "源自模具意象，模板描述一类结构的模式，编译时按具体类型铸造实例。"}],
    },
    "040-python/043-PythonGraphQL.md": {
        "description": "Python GraphQL API 开发完整指南：Strawberry + FastAPI、Schema/Query/Mutation/Subscription、DataLoader 与工程实践。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述 GraphQL 核心概念（Schema/Query/Mutation/Resolver/Type/Subscription）。", "verifiable": "默写六个概念的职责"},
            {"level": "understand", "objective": "能解释 GraphQL 与 REST 在数据获取粒度与端点组织上的差异。", "verifiable": "对比同一场景两种 API 的请求/响应"},
            {"level": "apply", "objective": "能使用 Strawberry + FastAPI 搭建可运行的 GraphQL 服务。", "verifiable": "完成最小 Query/Mutation 服务并通过 GraphiQL 验证"},
            {"level": "analyze", "objective": "能分析 N+1 查询问题及 DataLoader 批量加载原理。", "verifiable": "用示例说明循环引用场景下的性能问题"},
            {"level": "evaluate", "objective": "能评价 GraphQL 与 REST 在缓存、安全、版本管理上的取舍。", "verifiable": "针对具体项目给出选型论证"},
            {"level": "create", "objective": "能独立设计完整的博客系统 GraphQL API（含订阅与认证）。", "verifiable": "完成案例研究中的完整 API"},
        ],
        "exercises": [
            {"id": "py-gql-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "GraphQL 读取数据的操作称为 _____，修改数据的操作称为 _____。", "answer": "Query；Mutation", "explanation": "Query 对应读操作，Mutation 对应写操作。", "difficulty": "easy"},
            {"id": "py-gql-02", "type": "choice", "cognitiveLevel": "understand", "question": "关于 GraphQL 相比 REST 的优势，下列说法错误的是？", "options": ["A. 客户端可精确选择字段", "B. 一次请求可获取嵌套数据", "C. 天然具备 HTTP 缓存语义", "D. 有类型化 Schema 契约"], "answer": "C", "explanation": "GraphQL 默认使用 POST 单端点，HTTP 缓存需要额外设计。", "difficulty": "medium"},
        ],
        "references": [
            {"type": "documentation", "authors": ["GraphQL 基金会"], "year": 2026, "title": "GraphQL Specification", "venue": "spec.graphql.org", "url": "https://spec.graphql.org/", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["Strawberry GraphQL 团队"], "year": 2026, "title": "Strawberry GraphQL - FastAPI Integration", "venue": "strawberry.rocks", "url": "https://strawberry.rocks/docs/integrations/fastapi", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "图查询语言", "english": "GraphQL", "origin": "由 Graph（图）与 QL（Query Language）组合，指基于数据图结构进行查询的语言。"}],
    },
    "019-sql/019-SelfJoin.md": {
        "description": "SQL 自连接完整详解：同一表与自身连接的语法、典型场景（层级结构、比较、去重）与性能优化。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述自连接的基本语法与表别名（alias）的必要性。", "verifiable": "默写自连接最小 SQL"},
            {"level": "understand", "objective": "能解释同一张表如何通过两个别名扮演两个逻辑角色。", "verifiable": "说明 JOIN 两边的表实体与角色"},
            {"level": "apply", "objective": "能实现层级查询、相邻行比较、重复检测与中转路径等典型场景。", "verifiable": "编写四种场景的完整 SQL"},
            {"level": "analyze", "objective": "能分析自连接与递归 CTE 在可变层级查询上的边界。", "verifiable": "对比固定层级与任意层级方案"},
            {"level": "evaluate", "objective": "能评价 < 与 <> 在去重配对中的性能差异。", "verifiable": "说明 n(n-1)/2 与 n(n-1) 的差异"},
            {"level": "create", "objective": "能独立设计组织架构报表查询并配套索引优化。", "verifiable": "完成案例研究中的完整方案"},
        ],
        "exercises": [
            {"id": "sql-selfjoin-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "自连接中同一表需要两个不同的 _____ 来区分两个角色。", "answer": "别名", "explanation": "使用 AS a / AS b 区分连接两侧。", "difficulty": "easy"},
            {"id": "sql-selfjoin-02", "type": "choice", "cognitiveLevel": "understand", "question": "自连接的本质是？", "options": ["A. 复制表后再连接", "B. 同一表逻辑上扮演两个角色进行连接", "C. 与临时表连接", "D. 递归查询"], "answer": "B", "explanation": "物理上只有一张表，逻辑上通过别名呈现两个角色。", "difficulty": "medium"},
        ],
        "references": [
            {"type": "documentation", "authors": ["PostgreSQL 团队"], "year": 2026, "title": "PostgreSQL Documentation - Query: JOIN", "venue": "postgresql.org", "url": "https://www.postgresql.org/docs/current/queries-table-expressions.html", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["PostgreSQL 团队"], "year": 2026, "title": "WITH Queries (Recursive)", "venue": "postgresql.org", "url": "https://www.postgresql.org/docs/current/queries-with.html", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "自连接", "english": "self join", "origin": "连接操作的两侧均引用同一关系，如同照镜子般与自身比较。"}],
    },
    "002-markdown/010-Strikethrough.md": {
        "description": "Markdown 删除线语法完整讲解：GFM 扩展、使用场景、HTML 替代与跨平台兼容性。",
        "learningObjectives": [
            {"level": "remember", "objective": "能陈述删除线的双波浪线语法与 GFM 扩展地位。", "verifiable": "默写删除线最小示例"},
            {"level": "understand", "objective": "能解释删除线在 CommonMark 与 GFM 中的规范差异。", "verifiable": "说明为何标准 Markdown 不支持"},
            {"level": "apply", "objective": "能使用删除线表达价格标注、修订记录、废弃标记与任务状态。", "verifiable": "完成五种场景的 Markdown 编写"},
            {"level": "analyze", "objective": "能分析 del/s/strike 三种 HTML 标签的语义差异。", "verifiable": "给出标签语义对比表"},
            {"level": "evaluate", "objective": "能评价删除线与可访问性（屏幕阅读器）的相互作用。", "verifiable": "说明 AT 兼容策略"},
            {"level": "create", "objective": "能设计含删除线语义的文档修订规范。", "verifiable": "完成案例研究中的变更记录模板"},
        ],
        "exercises": [
            {"id": "md-strike-01", "type": "fill-blank", "cognitiveLevel": "remember", "question": "Markdown 删除线使用两个 _____ 包裹文本。", "answer": "波浪号（~~）", "explanation": "GFM 用 ~~ 表示删除线，单波浪号无效。", "difficulty": "easy"},
            {"id": "md-strike-02", "type": "choice", "cognitiveLevel": "understand", "question": "标准 CommonMark 是否支持删除线？", "options": ["A. 支持", "B. 不支持，属于 GFM 扩展", "C. 仅支持 HTML 形式", "D. 支持但语法不同"], "answer": "B", "explanation": "删除线是 GFM 的扩展语法，CommonMark 核心不含此特性。", "difficulty": "medium"},
        ],
        "references": [
            {"type": "standard", "authors": ["GitHub"], "year": 2026, "title": "GitHub Flavored Markdown Spec - Strikethrough (extension)", "venue": "github.github.com", "url": "https://github.github.com/gfm/#strikethrough-extension-", "accessedDate": "2026-08-01"},
            {"type": "standard", "authors": ["CommonMark"], "year": 2024, "title": "CommonMark Spec 0.31.2", "venue": "spec.commonmark.org", "url": "https://spec.commonmark.org/0.31.2/", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "删除线", "english": "strikethrough", "origin": "编辑排版中表示应删除的贯穿线，GFM 用双波浪线 ~~ 触发。"}],
    },
}


def inject(full_path: pathlib.Path, cfg: dict) -> bool:
    text = full_path.read_text(encoding="utf-8")
    if "learningObjectives" in text:
        return False  # 已升级
    lines = text.splitlines(keepends=True)
    # 找到 frontmatter 结束行（---）
    end = None
    for i, line in enumerate(lines):
        if i > 0 and line.strip() == "---":
            end = i
            break
    if end is None:
        return False
    # 更新 description / updated
    for i, line in enumerate(lines[:end]):
        if line.startswith("description:"):
            lines[i] = f"description: '{cfg['description']}'\n"
        if line.startswith("updated:"):
            lines[i] = "updated: '2026-08-01'\n"
    # 构造扩展 YAML 块
    ext = []
    ext.append("learningObjectives:")
    for item in cfg["learningObjectives"]:
        ext.append(f"  - level: {item['level']}")
        ext.append(f"    objective: '{item['objective']}'")
        ext.append(f"    verifiable: '{item['verifiable']}'")
    ext.append("exercises:")
    for item in cfg["exercises"]:
        ext.append(f"  - id: {item['id']}")
        ext.append(f"    type: {item['type']}")
        ext.append(f"    cognitiveLevel: {item['cognitiveLevel']}")
        ext.append(f"    question: '{item['question']}'")
        if item.get("options"):
            ext.append("    options:")
            for o in item["options"]:
                ext.append(f"      - '{o}'")
        ext.append(f"    answer: '{item['answer']}'")
        ext.append(f"    explanation: '{item['explanation']}'")
        ext.append(f"    difficulty: {item['difficulty']}")
    ext.append("references:")
    for ref in cfg["references"]:
        ext.append(f"  - type: {ref['type']}")
        ext.append(f"    authors: [{', '.join(repr(a) for a in ref['authors'])}]")
        ext.append(f"    year: {ref['year']}")
        ext.append(f"    title: '{ref['title']}'")
        ext.append(f"    venue: '{ref['venue']}'")
        if ref.get("url"):
            ext.append(f"    url: {ref['url']}")
            ext.append("    accessedDate: '2026-08-01'")
        elif ref.get("pages"):
            ext.append(f"    pages: {ref['pages']}")
    ext.append("etymology:")
    for e in cfg["etymology"]:
        ext.append(f"  - term: '{e['term']}'")
        ext.append(f"    english: '{e['english']}'")
        ext.append(f"    origin: '{e['origin']}'")
    ext.append("estimatedReadingTime: 30")
    ext.append("lastReviewed: '2026-08-01'")
    ext.append("reviewer: fanquanpp")

    # 插入到 frontmatter 结束行之前
    new_lines = lines[:end] + [l + "\n" for l in ext] + lines[end:]
    full_path.write_text("".join(new_lines), encoding="utf-8")
    return True


def main() -> None:
    targets = sys.argv[1:] or list(UPGRADES.keys())
    ok = 0
    for rel in targets:
        cfg = UPGRADES.get(rel)
        if not cfg:
            print(f"跳过（无配置）: {rel}")
            continue
        if inject(FULL / rel, cfg):
            ok += 1
            print(f"已升级: {rel}")
        else:
            print(f"跳过（已升级或格式异常）: {rel}")
    print(f"共升级 {ok} 篇")


if __name__ == "__main__":
    main()
