#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 FANDEX 文档中不再存在 ASCII 图表/绘图。"""

from __future__ import annotations

import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
ROOTS = [ROOT / "cnt-content" / "full", ROOT / "cnt-content" / "mobile"]

BOX_UNICODE = re.compile(
    "[\u250c\u2510\u2514\u2518\u251c\u2524\u252c\u2534\u253c\u2500\u2502"
    "\u2554\u2557\u255a\u255d\u2560\u2563\u2566\u2569\u256c\u2550\u2551"
    "\u256d\u256e\u256f\u2570]"
)
ASCII_BOX = re.compile(r"\+[-=+]{2,}\+")
TREE = re.compile(r"^\s*[\u251c\u2514\u2502]")


def is_diagram_line(line: str) -> bool:
    return bool(BOX_UNICODE.search(line) or ASCII_BOX.search(line) or TREE.match(line))


def main() -> None:
    total_files = 0
    total_blocks = 0
    issues: list[str] = []
    for root in ROOTS:
        if not root.exists():
            continue
        for f in sorted(root.rglob("*.md")):
            lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
            i = 0
            found = False
            while i < len(lines):
                stripped = lines[i].strip()
                if stripped.startswith("```"):
                    lang = stripped[3:].strip()
                    if lang.startswith("mermaid"):
                        # 检查 mermaid 块内标签是否残留制表符/框线
                        j = i + 1
                        block = []
                        while j < len(lines) and not lines[j].strip().startswith("```"):
                            block.append(lines[j])
                            j += 1
                        # 只检查 mermaid 标签内（引号中）的制表符残留，忽略 --> 箭头
                        label_chars = sum(
                            1
                            for l in block
                            if re.search(r'["\[]([^"\]]*[\u2500\u2502\u251c\u2514\u250c\u2510\u2518\u2524\u252c\u2534\u253c][^"\]]*)["\]]', l)
                        )
                        if label_chars:
                            found = True
                            total_blocks += 1
                            issues.append(f"{f.relative_to(root)}:{i+1}-{j+1} (mermaid 标签残留)")
                        i = j + 1
                        continue
                    if lang not in ("", "text", "txt"):
                        j = i + 1
                        while j < len(lines) and not lines[j].strip().startswith("```"):
                            j += 1
                        i = j + 1
                        continue
                    block: list[str] = []
                    j = i + 1
                    while j < len(lines) and not lines[j].strip().startswith("```"):
                        block.append(lines[j])
                        j += 1
                    diag = [b for b in block if is_diagram_line(b)]
                    if len(diag) >= 2:
                        found = True
                        total_blocks += 1
                        issues.append(f"{f.relative_to(root)}:{i+1}-{j+1}")
                    i = j + 1
                    continue
                # 正文连续制表线
                if is_diagram_line(lines[i]):
                    k = i
                    block = []
                    while k < len(lines) and is_diagram_line(lines[k]):
                        block.append(lines[k])
                        k += 1
                    if len(block) >= 3:
                        found = True
                        total_blocks += 1
                        issues.append(f"{f.relative_to(root)}:{i+1}-{k} (prose)")
                    i = k
                    continue
                i += 1
            if found:
                total_files += 1
    print(f"残留 ASCII 图表文件: {total_files}, 块数: {total_blocks}")
    for x in issues:
        print("  ", x)
    if total_blocks == 0:
        print("校验通过：无 ASCII 图表残留。")


if __name__ == "__main__":
    main()
