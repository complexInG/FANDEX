# -*- coding: utf-8 -*-
"""扫描“孤岛片段”：独立成段的 H1 标题 + 符号约定行。"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
AI_RE = re.compile(r"\\0(4[1-9]|5[0-0])-")

LEGEND = re.compile(r"^>\s*\*\*符号约定\*\*[:：]")


def main():
    hits = []
    for dp, dn, fn in os.walk(FULL):
        if AI_RE.search(dp):
            continue
        for f in sorted(fn):
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            lines = open(p, encoding="utf-8").read().split("\n")
            for i, line in enumerate(lines):
                if LEGEND.match(line):
                    # 回溯最多 2 行找 H1 标题（允许中间一个空行）
                    prev1 = lines[i - 1].strip() if i >= 1 else ""
                    prev2 = lines[i - 2].strip() if i >= 2 else ""
                    is_h1 = bool(re.match(r"^#\s+\S", prev1) or re.match(r"^#\s+\S", prev2))
                    # 判断是否为文档正文第一段（frontmatter 后首个非空行）
                    first_body = None
                    for j, l in enumerate(lines):
                        if l.strip() and not l.startswith("---"):
                            first_body = j
                            break
                    is_first = (first_body is not None and i - 1 <= first_body + 1)
                    hits.append((p, i + 1, is_h1, is_first, (prev1 or prev2)[:40]))
    total = len(hits)
    h1 = [h for h in hits if h[2]]
    h1_not_first = [h for h in h1 if not h[3]]
    h1_first = [h for h in h1 if h[3]]
    print("total legend lines:", total)
    print("with preceding H1:", len(h1), "| 非正文首段(孤岛):", len(h1_not_first), "| 正文首段:", len(h1_first))
    for p, ln, flag, first, prev in h1_not_first[:60]:
        print(f"  {p}:{ln} 前一行: {prev}")


if __name__ == "__main__":
    main()
