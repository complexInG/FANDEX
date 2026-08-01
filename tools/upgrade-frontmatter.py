# -*- coding: utf-8 -*-
"""为指定文档注入论文级 frontmatter 扩展字段（references/etymology 等）。

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
        
        
        "references": [
            {"type": "documentation", "authors": ["MDN Web Docs"], "year": 2026, "title": "border-radius - CSS: Cascading Style Sheets", "venue": "MDN Web Docs", "url": "https://developer.mozilla.org/en-US/docs/Web/CSS/border-radius", "accessedDate": "2026-08-01"},
            {"type": "standard", "authors": ["W3C"], "year": 2025, "title": "CSS Backgrounds and Borders Module Level 3", "venue": "W3C", "url": "https://www.w3.org/TR/css-backgrounds-3/", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "圆角", "english": "border-radius", "origin": "由 border（边框）与 radius（半径）组合而成，指用圆形或椭圆弧线替代边框的直角。"}],
    },
    "007-css/019-MediaQuery.md": {
        "description": "CSS 媒体查询完整原理：@media 语法、媒体特性、响应式断点、深色模式与 matchMedia。",
        
        
        "references": [
            {"type": "standard", "authors": ["W3C"], "year": 2024, "title": "Media Queries Level 4/5", "venue": "W3C", "url": "https://www.w3.org/TR/mediaqueries-5/", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["MDN Web Docs"], "year": 2026, "title": "Using media queries", "venue": "MDN Web Docs", "url": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "媒体查询", "english": "media query", "origin": "源自 print 样式表时代，后扩展为按设备能力查询条件应用样式。"}],
    },
    "007-css/022-Function.md": {
        "description": "CSS 数值函数完整原理：calc/min/max/clamp 的语法、单位混合规则、嵌套与响应式应用。",
        
        
        "references": [
            {"type": "standard", "authors": ["W3C"], "year": 2024, "title": "CSS Values and Units Module Level 4", "venue": "W3C", "url": "https://www.w3.org/TR/css-values-4/", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["MDN Web Docs"], "year": 2026, "title": "calc() - CSS", "venue": "MDN Web Docs", "url": "https://developer.mozilla.org/en-US/docs/Web/CSS/calc", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "钳制", "english": "clamp", "origin": "电子学钳位术语，把信号限制在上下限之间。"}],
    },
    "006-html5/011-List.md": {
        "description": "HTML 三类列表（ul/ol/dl）的语义、属性、嵌套规则、无障碍要求与 CSS 样式化技巧。",
        
        
        "references": [
            {"type": "standard", "authors": ["WHATWG"], "year": 2026, "title": "HTML Standard - The ul element", "venue": "WHATWG", "url": "https://html.spec.whatwg.org/multipage/grouping-content.html#the-ul-element", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["MDN Web Docs"], "year": 2026, "title": "ul: The Unordered List element", "venue": "MDN Web Docs", "url": "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "无序列表", "english": "unordered list", "origin": "用于表达顺序无关的项目集合，浏览器默认渲染为圆点标记。"}],
    },
    "006-html5/012-LinkageAnchor.md": {
        "description": "HTML 超链接与锚点完整指南：href 协议、target/rel 属性、路径系统、安全与可访问性。",
        
        
        "references": [
            {"type": "standard", "authors": ["WHATWG"], "year": 2026, "title": "HTML Standard - The a element", "venue": "WHATWG", "url": "https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-a-element", "accessedDate": "2026-08-01"},
            {"type": "article", "authors": ["OWASP"], "year": 2024, "title": "Reverse Tabnabbing", "venue": "OWASP", "url": "https://owasp.org/www-community/attacks/Reverse_Tabnabbing", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "锚点", "english": "anchor", "origin": "船锚意象，把页面内的导航锚定到特定位置。"}],
    },
    "010-vue3/026-TeleportPortalApp.md": {
        "description": "Vue 3 Teleport 传送门组件完整应用：to 目标解析、disabled、模态框、通知、遮罩、SSR 与无障碍。",
        
        
        "references": [
            {"type": "documentation", "authors": ["Vue.js 团队"], "year": 2026, "title": "Teleport - Vue.js 官方文档", "venue": "vuejs.org", "url": "https://vuejs.org/guide/built-ins/teleport.html", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["MDN Web Docs"], "year": 2026, "title": "CSS position: fixed", "venue": "MDN Web Docs", "url": "https://developer.mozilla.org/en-US/docs/Web/CSS/position", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "传送门", "english": "Teleport", "origin": "借鉴游戏/科幻的瞬移概念，指组件渲染内容在 DOM 树中瞬移到其他位置。"}],
    },
    "010-vue3/027-KeepAliveCacheLifecycle.md": {
        "description": "Vue 3 KeepAlive 组件缓存机制完整解析：include/exclude/max、activated/deactivated 生命周期、缓存刷新与内存管理。",
        
        
        "references": [
            {"type": "documentation", "authors": ["Vue.js 团队"], "year": 2026, "title": "KeepAlive - Vue.js 官方文档", "venue": "vuejs.org", "url": "https://vuejs.org/guide/built-ins/keep-alive.html", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["Vue.js 团队"], "year": 2026, "title": "Lifecycle Hooks - Vue.js 官方文档", "venue": "vuejs.org", "url": "https://vuejs.org/guide/essentials/lifecycle.html", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "保持活跃", "english": "KeepAlive", "origin": "网络协议保活（keep-alive）概念，组件缓存如同连接保活，避免重建开销。"}],
    },
    "010-vue3/030-VueRouterNavigationGuard.md": {
        "description": "Vue Router 导航守卫详解：全局守卫、路由独享守卫、组件内守卫、触发顺序与鉴权实践。",
        
        
        "references": [
            {"type": "documentation", "authors": ["Vue Router 团队"], "year": 2026, "title": "Navigation Guards - Vue Router 官方文档", "venue": "router.vuejs.org", "url": "https://router.vuejs.org/guide/advanced/navigation-guards.html", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["Vue Router 团队"], "year": 2026, "title": "Route Meta Fields - Vue Router 官方文档", "venue": "router.vuejs.org", "url": "https://router.vuejs.org/guide/advanced/meta.html", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "导航守卫", "english": "navigation guard", "origin": "类似门口守卫，在导航进入/离开节点检查放行或拦截。"}],
    },
    "013-java/041-JavaKubernetes.md": {
        "description": "Java 应用在 Kubernetes 上的部署完整指南：资源限制、健康检查、优雅停机、自动伸缩与云原生实践。",
        
        
        "references": [
            {"type": "documentation", "authors": ["Kubernetes 团队"], "year": 2026, "title": "Kubernetes Documentation - Configure Liveness, Readiness and Startup Probes", "venue": "kubernetes.io", "url": "https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["Microsoft Learn"], "year": 2026, "title": "Containerize your Java applications for Kubernetes", "venue": "Microsoft Learn", "url": "https://learn.microsoft.com/en-us/azure/developer/java/containers/kubernetes", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "容器编排", "english": "orchestration", "origin": "借音乐指挥意象，指统一调度、部署与管理容器集群。"}],
    },
    "014-kotlin/002-KotlinBasicSyntax.md": {
        "description": "Kotlin 基础语法完整讲解：变量声明、基本类型、字符串模板、包与导入、控制流与区间。",
        
        
        "references": [
            {"type": "documentation", "authors": ["JetBrains"], "year": 2026, "title": "Basic syntax - Kotlin Documentation", "venue": "kotlinlang.org", "url": "https://kotlinlang.org/docs/basic-syntax.html", "accessedDate": "2026-08-01"},
            {"type": "standard", "authors": ["JetBrains"], "year": 2026, "title": "Kotlin Language Specification", "venue": "kotlinlang.org", "url": "https://kotlinlang.org/spec/syntax-and-grammar.html", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "只读变量", "english": "val", "origin": "取自 value（值），表示一经赋值不可再变的绑定。"}],
    },
    "016-go/058-RaceDetectionAtomic.md": {
        "description": "Go 竞态检测与原子操作详解：-race 原理、atomic 包、常见竞态模式与无锁编程实践。",
        
        
        "references": [
            {"type": "documentation", "authors": ["Go Team"], "year": 2026, "title": "Data Race Detector - Go Documentation", "venue": "go.dev", "url": "https://go.dev/doc/articles/race_detector", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["Go Team"], "year": 2026, "title": "Package atomic - Go Documentation", "venue": "pkg.go.dev", "url": "https://pkg.go.dev/sync/atomic", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "原子操作", "english": "atomic operation", "origin": "atom 源自希腊语 atomos（不可分割），指不可被并发打断的单一操作。"}],
    },
    "025-c/007-EnumTypedef.md": {
        "description": "C 语言枚举与 typedef 详解：枚举本质、typedef 别名、函数指针、状态机与可移植类型体系。",
        
        
        "references": [
            {"type": "documentation", "authors": ["cppreference"], "year": 2026, "title": "Enumeration declaration", "venue": "cppreference.com", "url": "https://en.cppreference.com/w/c/language/enum", "accessedDate": "2026-08-01"},
            {"type": "book", "authors": ["Kernighan, B. W.", "Ritchie, D. M."], "year": 1988, "title": "The C Programming Language (2nd Edition)", "venue": "Prentice Hall", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "枚举", "english": "enumeration", "origin": "来自 enumerate（列举），指把一组具名常量逐一列举出来。"}],
    },
    "026-cpp/062-CppTemplate.md": {
        "description": "C++ 模板完整解析：函数模板、类模板、模板特化、SFINAE、概念（concepts）与现代 C++ 泛型实践。",
        
        
        "references": [
            {"type": "documentation", "authors": ["cppreference"], "year": 2026, "title": "Templates - cppreference.com", "venue": "cppreference.com", "url": "https://en.cppreference.com/w/cpp/language/templates", "accessedDate": "2026-08-01"},
            {"type": "book", "authors": ["Vandevoorde, D.", "Josuttis, N. M.", "Gregor, D."], "year": 2017, "title": "C++ Templates: The Complete Guide", "venue": "Addison-Wesley", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "模板", "english": "template", "origin": "源自模具意象，模板描述一类结构的模式，编译时按具体类型铸造实例。"}],
    },
    "040-python/043-PythonGraphQL.md": {
        "description": "Python GraphQL API 开发完整指南：Strawberry + FastAPI、Schema/Query/Mutation/Subscription、DataLoader 与工程实践。",
        
        
        "references": [
            {"type": "documentation", "authors": ["GraphQL 基金会"], "year": 2026, "title": "GraphQL Specification", "venue": "spec.graphql.org", "url": "https://spec.graphql.org/", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["Strawberry GraphQL 团队"], "year": 2026, "title": "Strawberry GraphQL - FastAPI Integration", "venue": "strawberry.rocks", "url": "https://strawberry.rocks/docs/integrations/fastapi", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "图查询语言", "english": "GraphQL", "origin": "由 Graph（图）与 QL（Query Language）组合，指基于数据图结构进行查询的语言。"}],
    },
    "019-sql/019-SelfJoin.md": {
        "description": "SQL 自连接完整详解：同一表与自身连接的语法、典型场景（层级结构、比较、去重）与性能优化。",
        
        
        "references": [
            {"type": "documentation", "authors": ["PostgreSQL 团队"], "year": 2026, "title": "PostgreSQL Documentation - Query: JOIN", "venue": "postgresql.org", "url": "https://www.postgresql.org/docs/current/queries-table-expressions.html", "accessedDate": "2026-08-01"},
            {"type": "documentation", "authors": ["PostgreSQL 团队"], "year": 2026, "title": "WITH Queries (Recursive)", "venue": "postgresql.org", "url": "https://www.postgresql.org/docs/current/queries-with.html", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "自连接", "english": "self join", "origin": "连接操作的两侧均引用同一关系，如同照镜子般与自身比较。"}],
    },
    "002-markdown/010-Strikethrough.md": {
        "description": "Markdown 删除线语法完整讲解：GFM 扩展、使用场景、HTML 替代与跨平台兼容性。",
        
        
        "references": [
            {"type": "standard", "authors": ["GitHub"], "year": 2026, "title": "GitHub Flavored Markdown Spec - Strikethrough (extension)", "venue": "github.github.com", "url": "https://github.github.com/gfm/#strikethrough-extension-", "accessedDate": "2026-08-01"},
            {"type": "standard", "authors": ["CommonMark"], "year": 2024, "title": "CommonMark Spec 0.31.2", "venue": "spec.commonmark.org", "url": "https://spec.commonmark.org/0.31.2/", "accessedDate": "2026-08-01"},
        ],
        "etymology": [{"term": "删除线", "english": "strikethrough", "origin": "编辑排版中表示应删除的贯穿线，GFM 用双波浪线 ~~ 触发。"}],
    },
}


def inject(full_path: pathlib.Path, cfg: dict) -> bool:
    text = full_path.read_text(encoding="utf-8")
    if "references:" in text:
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
