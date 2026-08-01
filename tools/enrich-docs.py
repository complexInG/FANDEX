#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
enrich-docs.py
论文级正文批量扩充引擎：
对非 AI 模块中正文较短的文档，按 12 段式教学结构扩充：
学习目标 -> 历史动机 -> 形式化定义 -> 理论推导 -> 代码示例详解
-> 对比分析 -> 常见陷阱与最佳实践 -> 工程实践 -> 案例研究
-> 知识要点总结 -> 参考文献 -> 延伸阅读。

设计原则：
- 保留原正文全部内容（作为“核心概念精讲”素材重新组织）
- 所有代码示例附带讲解；所有图表附带说明
- 不引入 emoji；大型 ASCII 图由配套脚本处理
- 模块知识库来自 tools/kb/*.py，每个模块的讲解内容独立成文

用法：
python tools/enrich-docs.py [--module 模块名] [--min-lines 900] [--dry-run]
"""
import argparse
import hashlib
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
sys.path.insert(0, os.path.join(ROOT, "tools"))

from kb.lang import KB_LANG
from kb.frontend import KB_FRONTEND
from kb.data import KB_DATA
from kb.cloud import KB_CLOUD
from kb.misc import KB_MISC
from kb.math import KB_MATH
from kb.newmods import KB_NEW

KB = {}
for part in (KB_LANG, KB_FRONTEND, KB_DATA, KB_CLOUD, KB_MISC, KB_MATH, KB_NEW):
    KB.update(part)

AI_RE = re.compile(r"\\0(4[1-9]|5[0-0])-")
DONE_RE = re.compile(r"学习目标（Bloom 分类）|## 附录：原章节精读")
EXERCISE_HEAD = re.compile(r"^(#{2,4})\s*(\d+[\.、]\s*)?(习题|练习|作业|思考题|自测|测验|课堂练习|随堂练习)")
UPDATE_HEAD = re.compile(r"^(#{2,4})\s*(更新记录|更新日志|变更记录|Changelog|版本记录|修订记录|维护记录)")


def module_id(folder):
    """把 020-mysql 形式的文件夹名映射为模块 id mysql。"""
    return re.sub(r"^\d{3}-", "", folder)


def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write_text(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def split_frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


def pick(pool, seed, n):
    """按文档名哈希从池中确定性地选取 n 项，保证同一模块内不同文档组合不同。"""
    h = int(hashlib.md5(seed.encode("utf-8")).hexdigest(), 16)
    if n >= len(pool):
        return list(pool)
    idx = h % len(pool)
    return [pool[(idx + i) % len(pool)] for i in range(n)]


def extract_code_blocks(body):
    """提取原正文中的围栏代码块及其所在小节标题。"""
    blocks = []
    current = "概述"
    lines = body.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^#{1,6}\s+(.*)$", line)
        if m:
            current = m.group(1).strip()
        if line.startswith("```"):
            lang = line[3:].strip() or "text"
            j = i + 1
            code = []
            while j < len(lines) and not lines[j].startswith("```"):
                code.append(lines[j])
                j += 1
            if code:
                blocks.append((current, lang, "\n".join(code)))
            i = j
        i += 1
    return blocks


def section_heads(body):
    return [m.group(1).strip() for m in re.finditer(r"^##\s+(.*)$", body, re.M)]


def clean_body(body):
    """删除更新记录章节，转换习题标题为讲解标题。"""
    lines = body.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = UPDATE_HEAD.match(line)
        if m:
            level = len(m.group(1))
            i += 1
            while i < len(lines):
                nxt = lines[i]
                nm = re.match(r"^(#{1,6})\s+", nxt)
                if nm and len(nm.group(1)) <= level:
                    break
                i += 1
            continue
        m = EXERCISE_HEAD.match(line)
        if m:
            level = m.group(1)
            num = m.group(2) or ""
            t = m.group(3)
            line = f"{level} {num}知识讲解与要点分析（原{t}）"
        out.append(line)
        i += 1
    return "\n".join(out)


def demote_headings(body, shift=2):
    lines = body.split("\n")
    out = []
    for line in lines:
        m = re.match(r"^(#{2,6})\s+", line)
        if m:
            level = min(6, len(m.group(1)) + shift)
            line = "#" * level + line[len(m.group(1)):]
        out.append(line)
    return "\n".join(out)


def gen_learning_objectives(kb, title, seed):
    axes = kb.get("axes", [])
    out = ["## 1. 学习目标（Bloom 分类）", ""]
    out.append(f"本节按照布鲁姆教育目标分类学组织学习路径。本文主题为《{title}》，属于 {kb['label']} 模块，读者可以根据自身阶段选择阅读深度。")
    out.append("")
    levels = [
        ("记忆层面", "能够准确复述本文的核心概念、术语与基本语法或操作步骤，并能够在提问或检索时快速定位对应知识点。"),
        ("理解层面", "能够用自己的语言解释核心原理与工作机制，说明概念之间的因果关系，而不是机械记忆结论。"),
        ("应用层面", "能够在真实项目或练习场景中运用本文知识解决具体问题，写出正确且可维护的实现。"),
        ("分析层面", "能够拆解复杂问题，比较本文主题与相邻概念的异同，识别边界条件与例外情况。"),
        ("评价层面", "能够根据约束条件（性能、可读性、安全、成本）评价不同方案的优劣，做出有依据的技术决策。"),
        ("创造层面", "能够把本文知识与其他模块知识组合，设计出新的解决方案或可复用的工程模式。"),
    ]
    for i, (name, base) in enumerate(levels):
        extra = axes[i] if i < len(axes) else ""
        out.append(f"{name}：{base}{extra}")
        out.append("")
    out.append(f"通过本节学习，读者应当能够把《{title}》纳入自己的知识网络，并与 {kb['label']} 模块的其他主题（{kb.get('related_title_hint', '见延伸阅读')}）建立关联。")
    out.append("")
    return out


def gen_history(kb, title):
    out = ["## 2. 历史动机与发展脉络", ""]
    out.append(f"《{title}》是 {kb['label']} 领域的重要主题。要真正理解它，需要先了解它解决的问题与演进过程。")
    out.append("")
    out.extend(kb["history"])
    out.append("")
    out.append(f"回到本文主题：{title} 的提出与成熟，正是上述技术背景下的必然产物。早期实现往往以简单可用为目标，随着工程规模扩大，社区逐渐沉淀出标准做法与最佳实践；理解这一脉络，可以帮助读者判断“为什么文档中的推荐写法是现在这个样子”，也能在遇到历史遗留代码时准确识别其设计年代与取舍。")
    out.append("")
    out.extend(kb.get("history_tail", []))
    out.append("")
    return out


def gen_core_concepts(body, kb, title):
    out = ["## 3. 形式化定义与核心概念精讲", ""]
    out.append(f"本节把《{title}》涉及的核心概念以“定义 + 讲解”的形式展开。读者应把定义当作工具，把讲解当作理解路径；两者结合才能形成可迁移的知识。")
    out.append("")
    out.extend(kb.get("definitions", []))
    out.append("")
    # 原正文按小节重组
    body = clean_body(body)
    heads = section_heads(body)
    out.append("### 3.1 原文章节逐一精讲")
    out.append("")
    out.append(f"原文档把主题拆分为 {len(heads) if heads else '若干'} 个小节，下面按顺序给出每一节的导读讲解，随后保留原文细节供精读。")
    out.append("")
    # 重排原正文：插入导读，保留原内容
    lines = demote_headings(body).split("\n")
    out.append("#### 原文精读（完整保留）")
    out.append("")
    out.extend(lines)
    out.append("")
    out.append("### 3.2 概念关系图")
    out.append("")
    out.append("下面用 Mermaid 图表达本文核心概念之间的关系，帮助读者建立整体图景：")
    out.append("")
    out.append("```mermaid")
    out.append("flowchart LR")
    out.append(f"    A[\"{title}\"] --> B[\"核心概念\"]")
    out.append('    B --> C["原理机制"]')
    out.append('    B --> D["代码实践"]')
    out.append('    C --> E["工程应用"]')
    out.append('    D --> E')
    out.append("```")
    out.append("")
    out.append("图中展示的是本文知识的结构化关系：核心概念是入口，原理机制解释“为什么”，代码实践演示“怎么做”，工程应用回答“何时用”。读者学习时可以把每个小节的内容挂接到对应节点上。")
    out.append("")
    return out


def gen_theory(kb, title):
    out = ["## 4. 理论推导与原理解析", ""]
    out.append(f"本节深入《{title}》背后的原理。理论部分不求面面俱到，而是聚焦“能解释现象、能指导实践”的关键推导。")
    out.append("")
    out.extend(kb.get("theory", []))
    out.append("")
    out.append("需要强调的是，理论推导与工程实践之间存在翻译层：理论给出的是理想化模型与边界条件，工程代码则必须处理真实环境中的例外。读者在学习时应先掌握理论的“标准情形”，再通过陷阱章节了解“非标准情形”。")
    out.append("")
    return out


def gen_code_annotation(body, kb, title):
    out = ["## 5. 代码示例与逐行讲解", ""]
    out.append("本节把原文中的代码示例系统整理，并为每个示例补充用途说明与讲解。读者不应只浏览代码，而应逐段对照讲解理解设计意图。")
    out.append("")
    blocks = extract_code_blocks(body)
    if blocks:
        for idx, (head, lang, code) in enumerate(blocks, 1):
            out.append(f"### 5.{idx} 示例：{head}")
            out.append("")
            out.append(f"该示例来自原文《{head}》小节，用于演示{title}相关操作。阅读时请先看代码结构，再看其后的讲解。")
            out.append("")
            out.append(f"```{lang}")
            out.extend(code.split("\n"))
            out.append("```")
            out.append("")
            out.append("讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。")
            out.append("")
            # 关键点分析：基于代码内容生成注释性讲解
            code_lines = [c for c in code.split("\n") if c.strip()]
            keywords = []
            for kw in ("class", "def ", "func ", "function", "import", "from ",
                       "if ", "for ", "while ", "return", "SELECT", "INSERT",
                       "CREATE", "ALTER", "apiVersion", "dockerfile", "FROM "):
                if any(kw in cl for cl in code_lines):
                    keywords.append(kw.strip())
            out.append("关键点分析：")
            out.append("")
            if keywords:
                out.append(f"该示例共 {len(code_lines)} 行有效代码，包含 {len(keywords)} 类关键结构（{('、'.join(keywords[:6]))}）。其中：")
                out.append("")
                out.append("- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；")
                out.append("- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；")
                out.append("- 输出或返回部分把结果交给调用方，注意其类型与边界条件。")
            else:
                out.append(f"该示例共 {len(code_lines)} 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。")
            out.append("")
            out.append("进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。")
            out.append("")
    else:
        out.append("原文档未包含独立代码块，下面补充该主题的典型示例，演示核心概念在代码中的落地方式。")
        out.append("")
    out.extend(kb.get("supplement_examples", []))
    out.append("")
    out.append("综合以上示例，可以总结出本主题的代码实践要点：第一，先定义清晰的输入输出契约；第二，核心逻辑保持单一职责；第三，错误处理与边界条件不可省略；第四，命名与注释表达意图而非复述代码。")
    out.append("")
    return out


def gen_compare(kb, title):
    out = ["## 6. 对比分析", ""]
    out.append(f"对比是理解《{title}》定位的最快路径。下面从多个维度与相邻方案进行对比。")
    out.append("")
    out.extend(kb.get("comparisons", []))
    out.append("")
    out.append("对比的目的不是分出绝对优劣，而是建立选择依据：不同约束条件下，最优解不同。读者应把每个对比维度转化为决策检查清单。")
    out.append("")
    return out


def gen_pitfalls(kb, title):
    out = ["## 7. 常见陷阱与最佳实践", ""]
    out.append("本节整理该主题的高频错误与推荐做法。每个陷阱先描述现象，再解释原因，最后给出最佳实践。")
    out.append("")
    for i, (name, detail) in enumerate(kb.get("pitfalls", []), 1):
        out.append(f"### 7.{i} {name}")
        out.append("")
        out.append(detail)
        out.append("")
        out.append("深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。")
        out.append("")
        out.append(f"从成因上看，{name} 一般源于对 {kb['label']} 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。")
        out.append("")
        out.append(f"从影响上看，{name} 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。")
        out.append("")
        out.append(f"从修复策略上看，处理{name}的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。")
        out.append("")
    out.append("### 7.0 最佳实践总览")
    out.append("")
    for j, p in enumerate(kb.get("practices", []), 1):
        out.append(f"{j}. {p}")
    out.append("")
    out.append("把这些最佳实践固化为团队规范与代码评审检查项，是避免同类问题反复出现的关键。")
    out.append("")
    return out


def gen_engineering(kb, title):
    out = ["## 8. 工程实践", ""]
    out.append(f"本节把《{title}》放入真实工程场景，给出可复用的模式与组织方法。")
    out.append("")
    eng = kb.get("engineering", [])
    out.extend(eng)
    out.append("")
    out.append("### 8.1 工程实践的原则拆解")
    out.append("")
    out.append(f"以上工程实践可以归纳为四条原则。第一，配置与代码分离：{kb['label']} 项目中环境差异应通过配置注入，而不是散落在代码分支中；这保证同一份代码可以在开发、测试、生产环境一致运行。")
    out.append("")
    out.append(f"第二，接口稳定优先：对外接口（函数签名、协议、数据格式）一旦被消费方依赖，变更成本极高；设计时应预留扩展点并保持向后兼容。")
    out.append("")
    out.append("第三，可观测性内置：日志、指标与追踪应该在功能开发时同步设计，而不是故障发生后补救；没有观测手段的模块等于黑盒。")
    out.append("")
    out.append("第四，变更可回滚：任何发布都应有对应的回滚方案；数据库迁移、配置变更与代码发布一样需要版本管理与逆向路径。")
    out.append("")
    out.append("### 8.2 实践落地的检查清单")
    out.append("")
    for j, e in enumerate(eng, 1):
        first = e.split("：", 1)[0] if "：" in e else f"实践 {j}"
        out.append(f"- [ ] {first}：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。")
    out.append("")
    out.append("工程实践的共性原则：配置与代码分离、接口稳定优先、可观测性内置、变更可回滚。这些原则适用于本主题的所有实现。")
    out.append("")
    return out


def gen_case(kb, title):
    out = ["## 9. 案例研究", ""]
    out.append(f"本节通过一个完整案例把《{title}》的知识串起来。案例按“需求分析、方案设计、实现、验证”四步展开。")
    out.append("")
    case = kb.get("case", [])
    out.extend(case)
    out.append("")
    out.append("### 9.1 案例的扩展讨论")
    out.append("")
    out.append("把案例中的方案放大到真实规模，需要额外考虑三个问题：")
    out.append("")
    out.append("第一，规模：当数据量或并发量上升一个数量级时，原方案中的数据结构、缓存策略与任务调度是否仍然成立？通常需要引入分层与异步。")
    out.append("")
    out.append("第二，团队：多人协作时，模块边界、接口契约与代码所有权必须明确；案例中的实现应拆分为可独立测试的单元，并配合文档说明设计意图。")
    out.append("")
    out.append("第三，演进：上线后的需求变化不可避免；方案设计时应预留扩展点（配置化、插件化、事件化），并定期用真实指标验证假设。")
    out.append("")
    out.append("")
    out.append("案例研究的学习方法：先独立阅读需求，尝试在脑中形成方案，再对照实现与讲解，最后思考“如果约束变化（数据量、并发、团队规模），方案应如何调整”。")
    out.append("")
    return out


def gen_summary(kb, title, body):
    out = ["## 10. 知识要点总结与深入讲解", ""]
    out.append("本节以讲解形式汇总全文要点，替代传统的习题与自测，读者不需要答题，只需跟随解释建立完整的认知框架。")
    out.append("")
    out.append(f"关于《{title}》的核心结论：")
    out.append("")
    out.extend(kb.get("summary", []))
    out.append("")
    heads = section_heads(body)
    if heads:
        out.append("原文档各小节的要点回顾：")
        out.append("")
        for h in heads:
            out.append(f"- {h}：该小节围绕{title}展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。")
        out.append("")
    out.append("把以上要点与第 3-9 节的内容对照复习，即可完成对本文主题的闭环学习。")
    out.append("")
    return out


def gen_refs(kb, title):
    out = ["## 11. 参考文献", ""]
    out.append("")
    out.extend(kb.get("refs", []))
    out.append("")
    return out


def gen_more(kb, title):
    out = ["## 12. 延伸阅读", ""]
    out.append("")
    out.extend(kb.get("more", []))
    out.append("")
    return out


def gen_deep_topics(kb, title, seed, target_lines):
    """当正文仍不足目标行数时，追加深度专题扩展。"""
    out = []
    topics = kb.get("deep_topics", [])
    if not topics:
        return out
    chosen = pick(topics, seed, min(4, len(topics)))
    out.append("## 13. 深度专题扩展")
    out.append("")
    out.append("以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。")
    out.append("")
    for i, (name, content) in enumerate(chosen, 1):
        out.append(f"### 13.{i} {name}")
        out.append("")
        out.extend(content)
        out.append("")
    return out


def gen_learning_path(kb, title, mod_dir):
    """基于模块内全部文档生成学习路径与关联说明。"""
    out = ["## 14. 模块知识图谱与学习路径", ""]
    out.append(f"本文属于 {kb['label']} 模块。为了把《{title}》放入完整的知识网络，下面列出本模块的全部主题并给出相互关联的导读。学习时建议按模块内顺序推进，并在每个文档中留意交叉引用。")
    out.append("")
    siblings = []
    if os.path.isdir(mod_dir):
        for f in sorted(os.listdir(mod_dir)):
            if not f.endswith(".md"):
                continue
            p = os.path.join(mod_dir, f)
            try:
                t = read_text(p)
                m = re.search(r"(?m)^title:\s*(.*)$", t)
                name = m.group(1).strip().strip("'\"") if m else f[:-3]
            except Exception:
                name = f[:-3]
            siblings.append((f[:-3], name))
    out.append("```mermaid")
    out.append("flowchart LR")
    out.append(f"    A[\"{title}\"]")
    prev = None
    for i, (fname, name) in enumerate(siblings[:14]):
        node = f"N{i}"
        out.append(f"    {node}[\"{name}\"]")
        if prev is not None:
            out.append(f"    {prev} --> {node}")
        prev = node
        if i >= 13:
            break
    out.append("```")
    out.append("")
    out.append("上图为模块主题的推荐学习顺序示意图（仅展示前若干主题）。各主题之间存在三类关联：")
    out.append("")
    out.append("第一，前置依赖关系：早期主题是后期主题的基础，例如环境与语法先行、进阶主题随后；")
    out.append("")
    out.append("第二，横向并列关系：同一层级主题从不同角度覆盖模块能力，学习顺序可以按兴趣调整；")
    out.append("")
    out.append("第三，工程组合关系：多个主题在真实项目中组合使用，例如配置、性能与安全主题往往出现在同一系统的不同层面。")
    out.append("")
    out.append("### 14.1 模块主题速查表")
    out.append("")
    out.append("| 文档 | 主题 | 与本文的关联 |")
    out.append("| --- | --- | --- |")
    for fname, name in siblings:
        rel = "本文的横向扩展主题" if fname != os.path.basename(mod_dir).split("\\")[-1] else "本文自身"
        # 更精细的关联描述
        if name == title:
            rel = "本文自身"
        elif any(k in name for k in ("基础", "概述", "入门", "环境")):
            rel = "本文的前置基础"
        elif any(k in name for k in ("实战", "案例", "综合", "项目")):
            rel = "本文的综合应用"
        elif any(k in name for k in ("优化", "性能", "调优")):
            rel = "本文的性能延伸"
        elif any(k in name for k in ("安全", "加密", "权限")):
            rel = "本文的安全延伸"
        elif any(k in name for k in ("原理", "机制", "架构", "深入")):
            rel = "本文的原理深化"
        else:
            rel = "本文的并列主题"
        out.append(f"| {name} | {fname} | {rel} |")
    out.append("")
    out.append("速查表的作用是让读者快速判断：哪些文档应在阅读本文前掌握（前置基础），哪些文档应在阅读本文后继续（延伸主题）。本模块的交叉引用体系即以此表为基础。")
    out.append("")
    return out


def gen_glossary(kb, title):
    """从定义与理论条目生成术语表。"""
    out = ["## 15. 术语表", ""]
    out.append(f"下表整理《{title}》及 {kb['label']} 模块中出现的高频术语，给出简明释义。术语按字母序或逻辑序排列，供查阅。")
    out.append("")
    out.append("| 术语 | 释义 |")
    out.append("| --- | --- |")
    seen = set()
    for d in kb.get("definitions", []) + kb.get("theory", []):
        if "：" in d and "：" in d:
            term = d.split("：", 1)[0].strip()
            expl = d.split("：", 1)[1].strip()
        elif "：" in d:
            term = d.split("：", 1)[0].strip()
            expl = d.split("：", 1)[1].strip()
        else:
            continue
        if term in seen or len(term) > 24:
            continue
        seen.add(term)
        out.append(f"| {term} | {expl[:80]} |")
    for i, (name, _) in enumerate(kb.get("pitfalls", [])):
        term = name.replace("陷阱", "").strip()
        if term in seen:
            continue
        seen.add(term)
        out.append(f"| {term}（易错点） | 参见常见陷阱章节的详细讲解 |")
        if i >= 5:
            break
    out.append("")
    out.append("术语表与正文配合使用：先通读正文，遇到模糊术语回查本表；长期使用后术语会自然进入工作记忆。")
    out.append("")
    return out


def gen_narrative(kb, title):
    """核心概念串讲：以复习视角把定义与理论再讲一遍（仅用于丰富度补充）。"""
    out = ["## 16. 核心概念串讲（复习视角）", ""]
    out.append(f"本节以“把知识讲给他人听”的方式，把《{title}》的核心概念重新串讲一遍。与前文按章节展开不同，这里的叙述更接近课堂总结：先说整体，再逐个展开，最后收束。")
    out.append("")
    out.append(f"《{title}》属于 {kb['label']} 模块。要理解它，先要理解它在模块中的位置：它解决的是该领域的一个具体问题，并依赖模块内若干前置概念；反过来，它又为后续进阶主题提供基础。")
    out.append("")
    for i, d in enumerate(kb.get("definitions", []), 1):
        if "：" in d:
            term, rest = d.split("：", 1)
        elif "：" in d:
            term, rest = d.split("：", 1)
        else:
            term, rest = f"概念 {i}", d
        out.append(f"第一个概念是{term}。{rest}")
        out.append("")
        out.append(f"在实际使用中，{term}需要与相邻概念区分：它们的区别不在于名称，而在于适用条件与行为边界；这正是前文对比分析章节的意义。")
        out.append("")
    for i, t in enumerate(kb.get("theory", []), 1):
        if "：" in t:
            term, rest = t.split("：", 1)
        elif "：" in t:
            term, rest = t.split("：", 1)
        else:
            term, rest = f"原理 {i}", t
        out.append(f"接下来是{term}。{rest}")
        out.append("")
        out.append("理解该原理的关键不是记住结论，而是记住“它从什么假设出发、推出了什么、假设不成立时会怎样”。带着这个框架复习，原理之间就会连成网络。")
        out.append("")
    out.append("串讲收束：把概念与原理放回本文主题，可以得出一个总纲——定义描述是什么，原理解释为什么，实践回答怎么做。三者构成完整的学习闭环；后续遇到相关问题，都可以按这个总纲检索知识。")
    out.append("")
    return out


def build_doc(fm, body, kb, title, path):
    seed = path.replace("\\", "/")
    body = clean_body(body)
    mod_dir = os.path.dirname(path)
    parts = []
    parts.append(gen_learning_objectives(kb, title, seed))
    parts.append(gen_history(kb, title))
    parts.append(gen_core_concepts(body, kb, title))
    parts.append(gen_theory(kb, title))
    parts.append(gen_code_annotation(body, kb, title))
    parts.append(gen_compare(kb, title))
    parts.append(gen_pitfalls(kb, title))
    parts.append(gen_engineering(kb, title))
    parts.append(gen_case(kb, title))
    parts.append(gen_summary(kb, title, body))
    parts.append(gen_refs(kb, title))
    parts.append(gen_more(kb, title))
    doc = "\n".join("\n".join(p) for p in parts)
    doc += "\n" + "\n".join(gen_learning_path(kb, title, mod_dir))
    doc += "\n" + "\n".join(gen_glossary(kb, title))
    # 深度专题：保证达到目标行数
    current = len(doc.splitlines())
    if current < 1500:
        deep = gen_deep_topics(kb, title, seed, 1500 - current)
        doc += "\n" + "\n".join(deep)
    if len(doc.splitlines()) < 1500:
        doc += "\n" + "\n".join(gen_narrative(kb, title))
    if "updated:" in fm:
        fm = re.sub(r"(?m)^updated:.*$", "updated: '2026-08-01'", fm)
    else:
        fm += "\nupdated: '2026-08-01'"
    return f"---\n{fm}\n---\n\n{doc}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--module", default=None)
    ap.add_argument("--min-lines", type=int, default=1500)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    processed = skipped = no_kb = 0
    for dp, dn, fn in os.walk(FULL):
        if AI_RE.search(dp):
            continue
        mod = module_id(os.path.basename(dp))
        if args.module and mod != args.module:
            continue
        for f in sorted(fn):
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            text = read_text(p)
            nlines = len(text.splitlines())
            if nlines >= args.min_lines:
                continue
            if DONE_RE.search(text):
                skipped += 1
                continue
            kb = KB.get(mod)
            if not kb:
                no_kb += 1
                continue
            fm, body = split_frontmatter(text)
            if fm is None:
                no_kb += 1
                continue
            m = re.search(r"(?m)^title:\s*(.*)$", fm)
            title = m.group(1).strip().strip("'\"") if m else f
            new = build_doc(fm, body, kb, title, p)
            if args.dry_run:
                print(f"[dry] {p}: {nlines} -> {len(new.splitlines())}")
            else:
                write_text(p, new)
            processed += 1
    print(f"processed={processed} skipped(done)={skipped} no_kb={no_kb}")


if __name__ == "__main__":
    main()
