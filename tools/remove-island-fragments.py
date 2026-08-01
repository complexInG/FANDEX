# -*- coding: utf-8 -*-
"""
删除文档中的“孤岛片段”：H1 标题 + “> **符号约定**：...” 成对块。
页面标题由 frontmatter 渲染，正文内重复的 H1 与符号约定行均为冗余。
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
AI_RE = re.compile(r"\\0(4[1-9]|5[0-0])-")

LEGEND = re.compile(r"^>\s*\*\*符号约定\*\*[:：]")
H1 = re.compile(r"^#\s+\S")


def process(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^(---\r?\n.*?\r?\n---\r?\n)", text, re.S)
    fm = m.group(1) if m else ""
    body = text[m.end():] if m else text
    lines = body.split("\n")
    out = []
    removed = 0
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if LEGEND.match(line):
            # 回溯 1-2 行找成对的 H1（允许中间一个空行）
            # out 的最后两项：可能 [H1] 或 [H1, ""] 或 ["", H1]
            h1_idx = -1
            if len(out) >= 1 and H1.match(out[-1]):
                h1_idx = len(out) - 1
            elif len(out) >= 2 and out[-1].strip() == "" and H1.match(out[-2]):
                h1_idx = len(out) - 2
            if h1_idx >= 0:
                del out[h1_idx:]
            removed += 1
            i += 1
            # 跳过后面的空行（保留一个分隔）
            while i < n and lines[i].strip() == "":
                i += 1
            if out and out[-1].strip() != "":
                out.append("")
            continue
        out.append(line)
        i += 1
    new = "\n".join(out)
    new = re.sub(r"\n{3,}", "\n\n", new)
    # 清理正文开头残留的 --- 分隔线与多余空行
    new = re.sub(r"^(?:\n)*(?:-{3,}\s*\n)+\n*", "", new)
    changed = removed > 0 or new != body
    new = fm + new
    if changed:
        open(path, "w", encoding="utf-8", newline="\n").write(new)
    return removed


def main():
    total = 0
    files = 0
    for dp, dn, fn in os.walk(FULL):
        if AI_RE.search(dp):
            continue
        for f in sorted(fn):
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            r = process(p)
            if r:
                total += r
                files += 1
    print("removed", total, "islands in", files, "files")


if __name__ == "__main__":
    main()
