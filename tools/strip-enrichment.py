# -*- coding: utf-8 -*-
"""
剥离 enrich-docs.py 生成的模板化章节，恢复原始正文。

被 enrich 处理的文档结构为：
  frontmatter
  ## 1. 学习目标（Bloom 分类）   <- 模板废话
  ## 2. 历史动机与发展脉络        <- 模块级通用内容（与本文主题可能无关）
  ## 3. 形式化定义与核心概念精讲
     ### 3.1 原文章节逐一精讲
       #### 原文精读（完整保留）   <- 从这里开始是真正的原文档正文（标题降级 2 级）
       ...原正文...
     ### 3.2 概念关系图           <- 模板图
  ## 4-16 ... 模板章节

本脚本提取“原文精读”部分，把标题升回原级别，恢复为干净的原文档，
并顺带清理更新记录段与习题标题。
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
AI_RE = re.compile(r"\\0(4[1-9]|5[0-0])-")

MARKER = "#### 原文精读（完整保留）"
END_3_2 = "### 3.2 概念关系图"
END_4 = "## 4. 理论推导与原理解析"

EXERCISE_HEAD = re.compile(
    r"^(#{2,4})\s*(\d+[\.\u3001]\s*)?(习题|练习题?|练习题?与答案|思考题|课后习题|课堂练习|随堂练习|自测|测验|作业)"
)
UPDATE_HEAD = re.compile(r"^(#{2,4})\s*(更新记录|更新日志|变更记录|Changelog|版本记录|修订记录|维护记录)")


def clean_body(body):
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


def un_demote(body):
    """标题降了 2 级（封顶 6），这里升回 2 级。"""
    lines = body.split("\n")
    out = []
    for line in lines:
        m = re.match(r"^(#{2,6})\s+", line)
        if m:
            level = max(2, len(m.group(1)) - 2)
            line = "#" * level + line[len(m.group(1)):]
        out.append(line)
    return "\n".join(out)


def strip(path):
    text = open(path, encoding="utf-8").read()
    if MARKER not in text:
        return False
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return False
    fm = m.group(1)
    body = text[m.end():]
    lines = body.split("\n")
    start = None
    for i, line in enumerate(lines):
        if line.rstrip() == MARKER:
            start = i + 1
            break
    if start is None:
        return False
    end = len(lines)
    for j in range(start, len(lines)):
        l = lines[j].rstrip()
        if l == END_3_2 or l.startswith(END_4):
            end = j
            break
    original = "\n".join(lines[start:end]).strip("\n")
    original = un_demote(original)
    original = clean_body(original)
    if not original.strip():
        return False
    new_text = f"---\n{fm}\n---\n\n{original}\n"
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
        for f in fn:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            if strip(p):
                total += 1
    print("stripped", total, "docs")


if __name__ == "__main__":
    main()
