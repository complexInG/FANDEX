#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""统计 ASCII 图表类型分布：timeline / tree / box / flow / other"""

from __future__ import annotations

import pathlib
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
ROOTS = [ROOT / "cnt-content" / "full", ROOT / "cnt-content" / "mobile"]

BOX_UNICODE = re.compile(
    "[\u250c\u2510\u2514\u2518\u251c\u2524\u252c\u2534\u253c\u2500\u2502"
    "\u2554\u2557\u255a\u255d\u2560\u2563\u2566\u2569\u256c\u2550\u2551"
    "\u256d\u256e\u256f\u2570]"
)
ASCII_BOX = re.compile(r"\+[-=+]{2,}\+")
TREE = re.compile(r"^[\u251c\u2514\u2502]")


def is_diagram_line(line: str) -> bool:
    return bool(BOX_UNICODE.search(line) or ASCII_BOX.search(line) or TREE.match(line))


def classify(lines: list[str]) -> str:
    date = re.compile(r"^\s*(?:19|20)\d{2}\s*(?:[-─]|[\u2502])")
    timeline = sum(1 for l in lines if date.match(l))
    tree = sum(1 for l in lines if TREE.match(l))
    if timeline >= 2 and tree == 0:
        return "timeline"
    if tree >= 2:
        return "tree"
    # 框线
    boxes = sum(1 for l in lines if ASCII_BOX.search(l))
    if boxes >= 2:
        return "box"
    return "other"


def main() -> None:
    stats: Counter[str] = Counter()
    by_lang: Counter[str] = Counter()
    total = 0
    files_with = 0
    for root in ROOTS:
        if not root.exists():
            continue
        for f in sorted(root.rglob("*.md")):
            lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
            i = 0
            found = False
            while i < len(lines):
                if lines[i].strip().startswith("```"):
                    j = i + 1
                    block: list[str] = []
                    while j < len(lines) and not lines[j].strip().startswith("```"):
                        block.append(lines[j])
                        j += 1
                    diag = [b for b in block if is_diagram_line(b)]
                    if len(diag) >= 2:
                        kind = classify(diag)
                        stats[kind] += 1
                        lang = lines[i].strip()[3:].strip() or "(none)"
                        by_lang[f"{kind}@{lang}"] += 1
                        total += 1
                        found = True
                    i = j + 1
                    continue
                # 非代码块：连续 >=3 行制表/框线视为内嵌图
                if is_diagram_line(lines[i]):
                    k = i
                    block = []
                    while k < len(lines) and is_diagram_line(lines[k]):
                        block.append(lines[k])
                        k += 1
                    if len(block) >= 3:
                        kind = classify(block)
                        stats[f"prose-{kind}"] += 1
                        total += 1
                        found = True
                    i = k
                    continue
                i += 1
            if found:
                files_with += 1
    print("代码块内 ASCII 图表总数:", total)
    for k, v in stats.most_common():
        print(f"  {k}: {v}")
    print("涉及文件数:", files_with)
    print()
    print("按 类型@语言 分布（前 40）:")
    for k, v in by_lang.most_common(40):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
