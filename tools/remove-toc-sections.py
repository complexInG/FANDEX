# -*- coding: utf-8 -*-
"""删除文档中的链接式目录小节（## 目录 + 编号链接列表 + ---）。"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
AI_RE = re.compile(r"\\0(4[1-9]|5[0-0])-")

TOC = re.compile(r"^#{1,4}\s*目录\s*$")
LINK_ITEM = re.compile(r"^[\s\d\.\u3001\-*]*\[[^\]]+\]\(#")


def remove_toc(lines, idx):
    """从目录标题行开始删除，直到下一个 ## 标题（含中间的 --- 分隔线）。"""
    j = idx + 1
    n = len(lines)
    seen_list = False
    while j < n:
        s = lines[j].strip()
        if re.match(r"^##\s+", lines[j]):
            break
        if LINK_ITEM.match(s):
            seen_list = True
            j += 1
            continue
        if s == "":
            j += 1
            continue
        if s.startswith("---") or s.startswith("***") or s.startswith("___"):
            j += 1
            continue
        if not seen_list:
            # 标题后第一段非列表内容：不是链接式目录，放弃
            return False
        break
    if not seen_list:
        return False
    return True


def process(path):
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    out = []
    changed = False
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if TOC.match(line):
            if remove_toc(lines, i):
                j = i + 1
                while j < n and not re.match(r"^##\s+", lines[j]):
                    j += 1
                changed = True
                i = j
                continue
        out.append(line)
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
    print("removed TOC in", files, "files")


if __name__ == "__main__":
    main()
