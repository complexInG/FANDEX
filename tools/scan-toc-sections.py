# -*- coding: utf-8 -*-
"""扫描文档中的“## 目录”小节（链接式目录）。"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
AI_RE = re.compile(r"\\0(4[1-9]|5[0-0])-")

TOC = re.compile(r"^#{1,4}\s*目录\s*$")


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
            in_fence = False
            for i, line in enumerate(lines):
                if line.strip().startswith("```"):
                    in_fence = not in_fence
                    continue
                if TOC.match(line):
                    # 判断后面几行是否是链接列表
                    nxt = " ".join(lines[i + 1:i + 4])
                    is_link_list = bool(re.search(r"\[.+\]\(#", nxt))
                    hits.append((p, i + 1, "fence" if in_fence else "body", is_link_list))
    print("TOC sections:", len(hits))
    body = [h for h in hits if h[2] == "body"]
    print("outside fences:", len(body))
    for p, ln, where, link in body:
        print(f"  {p}:{ln} linklist={link}")


if __name__ == "__main__":
    main()
