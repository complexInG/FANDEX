# -*- coding: utf-8 -*-
"""
外科手术式清理富集文档中的模板废话，保留全部真实知识点。

处理对象：enrich-docs.py 生成的 12 段式结构文档（含“#### 原文精读（完整保留）”标记）。

删除的纯话术：
  1. 学习目标（Bloom 分类）整节（通用模板句）
  2. 历史节的首段引导与“回到本文主题”段
  3. 定义节引导句、3.1 导读段、3.2 通用概念图
  4. 原理节结尾“翻译层”段
  5. 代码示例节（与原文重复 + 通用讲解）
  6. 对比节引导句与结尾句
  7. 每个陷阱后的四段通用“深入讲解”
  8. 工程实践的两节通用原则/清单
  9. 案例节通用扩展讨论与学习方法段
  10. 总结节的“原文档各小节要点回顾”复读块
  11. 模块图谱节的通用叙述（仅保留真实文档速查表）
  12. 术语表整节、核心概念串讲整节

重组后的结构（原文档正文为骨架，仅保留真实且不跑题的附加内容）：
  [原文档正文] -> 深度专题扩展 -> 参考文献 -> 延伸阅读 -> 模块文档速查表

说明：模块级通用文本段（历史/定义/原理/对比/陷阱/工程/案例/总结）会与具体
文档主题错位（例如 SVG 文档中出现 HTML5 的陷阱），因此从正文中移除；
模块级教学素材仍保留在 tools/kb/ 中供按需使用。
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
AI_RE = re.compile(r"\\0(4[1-9]|5[0-0])-")

MARKER = "#### 原文精读（完整保留）"

H_BG = "## 2. 历史动机与发展脉络"
H_DEF = "## 3. 形式化定义与核心概念精讲"
H_THEORY = "## 4. 理论推导与原理解析"
H_CODE = "## 5. 代码示例与逐行讲解"
H_CMP = "## 6. 对比分析"
H_PIT = "## 7. 常见陷阱与最佳实践"
H_ENG = "## 8. 工程实践"
H_CASE = "## 9. 案例研究"
H_SUM = "## 10. 知识要点总结与深入讲解"
H_REF = "## 11. 参考文献"
H_MORE = "## 12. 延伸阅读"
H_DEEP = "## 13. 深度专题扩展"
H_MAP = "## 14. 模块知识图谱与学习路径"
H_GLOSS = "## 15. 术语表"
H_STR = "## 16. 核心概念串讲（复习视角）"
H_OBJ = "## 1. 学习目标（Bloom 分类）"

SUB_3_1 = "### 3.1 原文章节逐一精讲"
SUB_3_2 = "### 3.2 概念关系图"
SUB_8_1 = "### 8.1 工程实践的原则拆解"
SUB_8_2 = "### 8.2 实践落地的检查清单"
SUB_9_1 = "### 9.1 案例的扩展讨论"
SUB_14_1 = "### 14.1 模块主题速查表"


def split_blocks(body):
    """按顶层 ## 标题切块，返回 [(heading, content_lines)]。"""
    lines = body.split("\n")
    blocks = []
    cur_head = None
    cur = []
    for line in lines:
        m = re.match(r"^##\s+(.*)$", line)
        if m:
            if cur_head is not None:
                blocks.append((cur_head, cur))
            cur_head = m.group(1).strip()
            cur = []
        else:
            cur.append(line)
    if cur_head is not None:
        blocks.append((cur_head, cur))
    return blocks


def drop_paragraphs(paras, dropers):
    """按谓词删除段落（保留空行结构）。"""
    out = []
    for p in paras:
        if any(f(p) for f in dropers):
            continue
        out.append(p)
    return out


def para_list(lines):
    """把行分组为段落（连续非空行），返回 [(start_idx, end_idx_exclusive)]。"""
    groups = []
    i = 0
    while i < len(lines):
        if lines[i].strip():
            j = i
            while j < len(lines) and lines[j].strip():
                j += 1
            groups.append((i, j))
            i = j
        else:
            i += 1
    return groups


def un_demote(body):
    lines = body.split("\n")
    out = []
    for line in lines:
        m = re.match(r"^(#{2,6})\s+", line)
        if m:
            level = max(2, len(m.group(1)) - 2)
            line = "#" * level + line[len(m.group(1)):]
        out.append(line)
    return "\n".join(out)


def clean_paras(lines, keep_heads=None):
    """去掉段落首尾的模板句：保留真实内容。"""
    out = []
    skip_next = False
    for line in lines:
        s = line.strip()
        if not s:
            out.append(line)
            continue
        # 通用引导/结尾句（精确匹配前缀）
        if re.match(r"^本节(把|以|按照|通过)", s) and ("读者" in s or "路径" in s):
            continue
        if s.startswith("回到本文主题：") or s.startswith("《") and "提出与成熟" in s:
            continue
        if s.startswith("需要强调") or s.startswith("需要说明") or s.startswith("需要指出"):
            continue
        if s.startswith("对比是理解") or s.startswith("对比的目的不是"):
            continue
        if s.startswith("深入讲解：该问题之所以") or s.startswith("从成因上看，") or \
           s.startswith("从影响上看，") or s.startswith("从修复策略上看，"):
            continue
        if s.startswith("把这些最佳实践固化") or s.startswith("工程实践的共性原则"):
            continue
        if s.startswith("案例研究的学习方法"):
            continue
        if s.startswith("把以上要点与第"):
            continue
        if s.startswith("原文档各小节的要点回顾"):
            skip_next = True
            continue
        if skip_next and (s.startswith("- ") or s.startswith("* ") or re.match(r"^-\s", s)):
            continue
        skip_next = False
        if keep_heads and line.lstrip().startswith(keep_heads):
            continue
        out.append(line)
    return out


def extract_range(lines, start_marker, end_markers):
    """取 [start_marker 行之后, 第一个 end_marker 行之前) 的内容。"""
    start = None
    for i, line in enumerate(lines):
        if line.rstrip() == start_marker:
            start = i + 1
            break
    if start is None:
        return None
    for j in range(start, len(lines)):
        s = lines[j].rstrip()
        if any(s == em or s.startswith(em) for em in end_markers):
            return "\n".join(lines[start:j]).strip("\n")
    return "\n".join(lines[start:]).strip("\n")


def clean_one(path):
    text = open(path, encoding="utf-8").read()
    if MARKER not in text:
        return False
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return False
    fm = m.group(1)
    body = text[m.end():]
    blocks = split_blocks(body)
    by_head = {}
    for head, content in blocks:
        by_head.setdefault(head, []).extend(content)

    parts = []

    # 原文档正文
    original = extract_range(body.split("\n"), MARKER, [SUB_3_2, H_THEORY])
    original_heads = set()
    if original:
        original = un_demote(original)
        for line in original.split("\n"):
            mm = re.match(r"^##\s+(.*)$", line)
            if mm:
                original_heads.add(mm.group(1).strip())
        parts.append(("", original.split("\n")))  # 以原文档自身标题为骨架

    # 参考文献
    refs = by_head.get(H_REF[3:], [])
    if any(l.strip() for l in refs) and "参考文献" not in original_heads:
        parts.append(("## 参考文献", refs))

    # 延伸阅读
    more = by_head.get(H_MORE[3:], [])
    if any(l.strip() for l in more) and "延伸阅读" not in original_heads:
        parts.append(("## 延伸阅读", more))

    # 深度专题
    deep = by_head.get(H_DEEP[3:], [])
    if any(l.strip() for l in deep) and "深度专题扩展" not in original_heads:
        parts.append(("## 深度专题扩展", deep))

    # 模块文档速查表
    table = extract_range(body.split("\n"), SUB_14_1, [H_GLOSS, H_STR])
    if table and "|" in table and "模块文档速查表" not in original_heads:
        table_lines = table.split("\n")
        # 去掉表后的通用尾段
        clean_table = []
        for line in table_lines:
            if line.strip().startswith("速查表的作用是"):
                break
            clean_table.append(line)
        parts.append(("## 模块文档速查表", clean_table))

    out = []
    for head, lines in parts:
        if head:
            out.append(head)
            out.append("")
        out.extend(lines)
        if out and out[-1].strip():
            out.append("")
    new_text = f"---\n{fm}\n---\n\n" + "\n".join(out).strip("\n") + "\n"
    open(path, "w", encoding="utf-8", newline="\n").write(new_text)
    return True


def main():
    mod_filter = sys.argv[1] if len(sys.argv) > 1 else None
    total = 0
    for dp, dn, fn in os.walk(FULL):
        if AI_RE.search(dp):
            continue
        if mod_filter and os.path.basename(dp) != mod_filter:
            continue
        for f in sorted(fn):
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            if clean_one(p):
                total += 1
    print("cleaned", total, "docs")


if __name__ == "__main__":
    main()
