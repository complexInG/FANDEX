# -*- coding: utf-8 -*-
"""把剩余习题章节转换为知识讲解（FAQ 自问自答形式，保留解析内容）。"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
AI_RE = re.compile(r"\\0(4[1-9]|5[0-0])-")

EX_HEAD = re.compile(
    r"^(#{1,4})\s*(\d+[\.\u3001]\s*)?"
    r"(习题|练习题?|练习题?与答案|思考题|课后习题|课堂练习|随堂练习|自测|测验|作业|LeetCode\s*练习|编程练习|题目)"
)
SUB_HEAD = re.compile(
    r"^(#{2,5})\s*\d+[\.\u3001]\d*\s*(选择题|填空题|判断题|简答题|编程题|综合题|应用题|论述题|问答题|答案与解析)"
)
Q_PREFIX = re.compile(r"^\*\*Q(\d+)\*\*\s*[:：]?\s*")
ANS_PREFIX = re.compile(r"^\*\*(答案|参考答案|解析|答案解析)\*\*\s*[:：]?\s*")
PLAIN_ANS = re.compile(r"^(答案|参考答案|解析|答案解析)\s*[:：]\s*")
DETAILS_OPEN = re.compile(r"^\s*<details>\s*$")
SUMMARY_OPEN = re.compile(r"^\s*<summary>.*</summary>\s*$")
DETAILS_CLOSE = re.compile(r"^\s*</details>\s*$")


def convert(path):
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    out = []
    changed = 0
    qn = 0
    for line in lines:
        m = EX_HEAD.match(line)
        if m:
            level = m.group(1)
            title = m.group(3)
            out.append(f"{level} 知识讲解与要点分析（原{title}）")
            changed += 1
            continue
        m = SUB_HEAD.match(line)
        if m:
            level = m.group(1)
            kind = m.group(2)
            out.append(f"{level} {kind}知识点讲解")
            changed += 1
            continue
        m = Q_PREFIX.match(line)
        if m:
            qn += 1
            rest = line[m.end():]
            out.append(f"**常见疑问 {qn}**：{rest}")
            continue
        m = ANS_PREFIX.match(line)
        if m:
            rest = line[m.end():]
            out.append(f"**解析讲解**：{rest}")
            continue
        m = PLAIN_ANS.match(line)
        if m:
            rest = line[m.end():]
            out.append(f"解析讲解：{rest}")
            continue
        if DETAILS_OPEN.match(line) or SUMMARY_OPEN.match(line) or DETAILS_CLOSE.match(line):
            continue
        out.append(line)
    new = "\n".join(out)
    if changed:
        open(path, "w", encoding="utf-8", newline="\n").write(new)
    return changed


def main():
    total = 0
    files = 0
    for dp, dn, fn in os.walk(FULL):
        if AI_RE.search(dp):
            continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            c = convert(p)
            if c:
                total += c
                files += 1
    print(f"converted {total} headings in {files} files")


if __name__ == "__main__":
    main()
