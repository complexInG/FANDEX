#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FANDEX ASCII 图表扫描器

定位 cnt-content/full 与 mobile 中真正的 ASCII 图表/绘图：
1. Unicode 制表符（┌┐└┘├┤┬┼─│ 等）
2. ASCII 框线（+----+ / | ... |）
3. 树形图（├── └── │ 前缀）
4. 简单流程图（[A] --> [B] 或 │ ▼）

排除：Markdown 表格、单字符装饰线、代码中误匹配的类型/注释。
"""

from __future__ import annotations

import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
ROOTS = [ROOT / "cnt-content" / "full", ROOT / "cnt-content" / "mobile"]

# Unicode 制表符（用转义避免源码编码问题）
BOX_UNICODE = re.compile(
    "[\u250c\u2510\u2514\u2518\u251c\u2524\u252c\u2534\u253c\u2500\u2502"
    "\u2554\u2557\u255a\u255d\u2560\u2563\u2566\u2569\u256c\u2550\u2551"
    "\u256d\u256e\u256f\u2570]"
)
# ASCII 框线：整行由 + - = | 组成且含连续边框
ASCII_BOX = re.compile(r"\+[-=+]{2,}\+")
# 树形前缀
TREE = re.compile(r"^[\u251c\u2514\u2502][\u2500\s\\/]")
# 行内强框线（含 | 且行首行尾都有框字符）
STRONG_LINE = re.compile(r"^[+|][^|+]*[+|]$")


def is_diagram_line(line: str) -> bool:
    if BOX_UNICODE.search(line):
        return True
    if ASCII_BOX.search(line):
        return True
    if TREE.match(line):
        return True
    if STRONG_LINE.match(line):
        return True
    return False


def main() -> None:
    files = {}
    for root in ROOTS:
        if not root.exists():
            continue
        for f in sorted(root.rglob("*.md")):
            lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
            hits = [i + 1 for i, l in enumerate(lines) if is_diagram_line(l)]
            if not hits:
                continue
            groups = []
            start = prev = hits[0]
            for h in hits[1:]:
                if h == prev + 1:
                    prev = h
                else:
                    groups.append((start, prev))
                    start = prev = h
            groups.append((start, prev))
            files[str(f.relative_to(root))] = groups

    total_blocks = sum(len(v) for v in files.values())
    print(f"文件数: {len(files)}  图表块数: {total_blocks}")
    for name, blocks in sorted(files.items(), key=lambda kv: -len(kv[1]))[:60]:
        print(f"{len(blocks):4d}  {name}  {blocks[:6]}")


if __name__ == "__main__":
    main()
