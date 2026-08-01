# -*- coding: utf-8 -*-
"""扫描 Markdown 图片语法中目的地为占位文本/中文的相对路径（会导致构建生成非法 import）。"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
AI_RE = re.compile(r"\\0(4[1-9]|5[0-0])-")
IMG = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")


def is_bad(dest):
    if not dest:
        return False
    low = dest.lower()
    if low.startswith(("http://", "https://", "data:", "blob:")):
        return False
    if low.startswith(("assets/", "images/", "img/", "/images", "/assets", "./", "../")):
        return False
    if dest.endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".avif", ".ico")):
        return False
    if re.search(r"[\u4e00-\u9fff]", dest):
        return True
    if len(dest) <= 12 and not dest.startswith(("http", "www")):
        return True
    return False


def main():
    hits = []
    for dp, dn, fn in os.walk(FULL):
        if AI_RE.search(dp):
            continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            for i, line in enumerate(open(p, encoding="utf-8"), 1):
                for m in IMG.finditer(line):
                    if is_bad(m.group(1)):
                        hits.append((p, i, m.group(1), line.strip()[:90]))
    print("hits:", len(hits))
    for h in hits:
        print(h[0], h[1], "|", h[2], "|", h[3])


if __name__ == "__main__":
    main()
