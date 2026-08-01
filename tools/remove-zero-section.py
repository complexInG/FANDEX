# -*- coding: utf-8 -*-
"""删除所有文档中整个“## 0. 零基础入门（从零开始）”小节（含 0.1/0.2 与尾部分隔线）。"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
AI_RE = re.compile(r"\\0(4[1-9]|5[0-0])-")

SEC = "## 0. 零基础入门（从零开始）"


def process(path):
    text = open(path, encoding="utf-8").read()
    if SEC not in text:
        return False
    lines = text.split("\n")
    out = []
    changed = False
    i = 0
    n = len(lines)
    while i < n:
        if lines[i].strip() == SEC:
            # 收集整节：到下一个非围栏内的 ## 标题为止
            j = i + 1
            in_fence = False
            while j < n:
                s = lines[j].strip()
                if s.startswith("```"):
                    in_fence = not in_fence
                    j += 1
                    continue
                if not in_fence and re.match(r"^##\s+", lines[j]):
                    break
                j += 1
            # 若节尾紧跟 --- 分隔线，一并删除
            k = j
            while k < n and lines[k].strip() == "":
                k += 1
            if k < n and lines[k].strip().startswith("---"):
                j = k + 1
            changed = True
            i = j
            continue
        out.append(lines[i])
        i += 1
    if changed:
        new = "\n".join(out)
        new = re.sub(r"\n{3,}", "\n\n", new)
        open(path, "w", encoding="utf-8", newline="\n").write(new)
    return changed


def main():
    files = 0
    for dp, dn, fn in os.walk(FULL):
        if AI_RE.search(dp):
            continue
        for f in sorted(fn):
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            if process(p):
                files += 1
    print("removed 0-section in", files, "files")


if __name__ == "__main__":
    main()
