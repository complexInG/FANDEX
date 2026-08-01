#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FANDEX ASCII 图表 -> Mermaid 转换器（质量受限版）

只转换"无语言标记或 text 标记"的代码围栏中的 ASCII 图表：
1. timeline -> mermaid timeline
2. tree     -> mermaid flowchart TD（保留树形层级与 ▼ 区块递进）
3. vertical -> mermaid flowchart TD（文本行 + │ 标签 + ▼）
4. box      -> mermaid flowchart TD（简单纵向堆叠框）

含语言标记（代码）的围栏一律跳过，避免破坏代码示例。
无法可靠转换的块写入 --report 供人工处理。

用法：
    python tools/convert-ascii-diagrams.py --dry-run
    python tools/convert-ascii-diagrams.py
"""

from __future__ import annotations

import argparse
import json
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
DATE = re.compile(r"^\s*(?:19|20)\d{2}\s*")
ARROW_LINE = re.compile(r"^\s*[▼▲↓↑vV]\s*$")


def is_diagram_line(line: str) -> bool:
    return bool(BOX_UNICODE.search(line) or ASCII_BOX.search(line) or TREE.match(line))


def classify(lines: list[str]) -> str:
    tree = sum(1 for l in lines if TREE.match(l))
    box = sum(1 for l in lines if ASCII_BOX.search(l))
    date = sum(1 for l in lines if DATE.match(l))
    arrows = sum(1 for l in lines if ARROW_LINE.match(l))
    if date >= 2 and box == 0:
        return "timeline"
    if tree >= 2:
        return "tree"
    if box >= 2:
        return "box"
    if arrows >= 1:
        return "vertical"
    return "other"


def _esc(s: str) -> str:
    s = re.sub(r'["]', "'", s)
    return s.strip(" \u2500\u2502\u251c\u2514\u2192\u2190\u2191\u2193")


def convert_timeline(lines: list[str]) -> str:
    events: list[tuple[str, str]] = []
    cur_year: str | None = None
    cur_text: list[str] = []
    for raw in lines:
        if re.fullmatch(r"\s*[│|\s]+\s*", raw):
            continue
        m = re.match(r"^\s*((?:19|20)\d{2})\s*(?:[-─\u2502]{1,4}\s*)?(.*)$", raw)
        if m:
            if cur_year:
                events.append((cur_year, " ".join(cur_text)))
            cur_year = m.group(1)
            cur_text = [m.group(2).strip()]
        else:
            # 续行：去掉 │ 前缀后并入当前事件
            t = re.sub(r"^\s*[│|]\s*", "", raw).strip()
            if t:
                cur_text.append(_esc(t))
    if cur_year:
        events.append((cur_year, " ".join(cur_text)))
    if not events:
        return ""
    parts = ["timeline", "    title 发展时间线"]
    for year, text in events:
        parts.append(f"    {year}: {text}")
    return "\n".join(parts)


def _glyph_col(line: str) -> int:
    for idx, ch in enumerate(line):
        if ch in "\u251c\u2514\u2502\u2500":
            return idx
        if ch == " ":
            continue
        break
    return -1


def convert_tree(lines: list[str]) -> str:
    """保留树形层级；▼ 行连接上一个父节点的最后一个子节点到下一个父节点。"""
    nodes: list[tuple[str, str, int]] = []
    edges: list[str] = []
    seq = 0
    parents: list[tuple[int, str]] = []
    last_child: str | None = None
    last_depth = 0
    for raw in lines:
        if not raw.strip():
            continue
        if ARROW_LINE.match(raw):
            continue
        col = _glyph_col(raw)
        if col < 0:
            t = _esc(raw.strip())
            if not t:
                continue
            nid = f"T{seq}"
            seq += 1
            nodes.append((nid, t, 0))
            if last_child and parents:
                edges.append(f"    {last_child} --> {nid}")
            parents = [(0, nid)]
            last_child = nid
            last_depth = 0
            continue
        marker = raw[col:].lstrip("\u2500 ")
        text = _esc(marker.lstrip("\u251c\u2514\u2502 ").strip())
        if not text:
            continue
        depth = max(0, round(col / 2)) + (1 if marker.startswith(("\u251c", "\u2514")) else 0)
        nid = f"T{seq}"
        seq += 1
        nodes.append((nid, text, depth))
        while parents and parents[-1][0] >= depth:
            parents.pop()
        if parents:
            edges.append(f"    {parents[-1][1]} --> {nid}")
        parents.append((depth, nid))
        last_child = nid
        last_depth = depth
    if not nodes:
        return ""
    out = ["flowchart TD"]
    for nid, label, _d in nodes:
        out.append(f'    {nid}["{label}"]')
    out.extend(edges)
    return "\n".join(out)


def convert_vertical(lines: list[str]) -> str:
    steps: list[tuple[str, str]] = []
    pending: str | None = None
    for raw in lines:
        t = raw.strip()
        if not t:
            continue
        if re.fullmatch(r"[│|]\s*(.*)", t):
            lab = t.lstrip("\u2502|").strip()
            if lab:
                pending = lab
            continue
        if ARROW_LINE.match(raw):
            continue
        if re.fullmatch(r"[-─=]{2,}[>►]", t) or re.fullmatch(r"[<◄][-─=]{2,}", t):
            continue
        steps.append((_esc(t), pending or ""))
        pending = None
    if not steps:
        return ""
    out = ["flowchart TD"]
    for idx, (label, edge) in enumerate(steps):
        out.append(f'    V{idx}["{label}"]')
        if idx:
            if edge:
                out.append(f"    V{idx-1} -->|{_esc(edge)}| V{idx}")
            else:
                out.append(f"    V{idx-1} --> V{idx}")
    return "\n".join(out)


def convert_box(lines: list[str]) -> str:
    """多列框线图 -> flowchart（每列一个纵向子图）。"""
    # 提取每行的"文本片段 + 列位置"
    cols: dict[int, list[str]] = {}
    for raw in lines:
        if not raw.strip():
            continue
        # 纯框线
        if re.fullmatch(r"\s*[+|=\-.\s]+\s*", raw.replace("|", " ")):
            continue
        # 带文本的框内行：按列切分
        if "|" in raw:
            # 找每个 | 的位置划分列
            parts = raw.split("|")
            col_idx = 0
            for part in parts:
                t = part.strip(" +-=│").strip()
                if t and not re.fullmatch(r"[-+=. ]+", t):
                    cols.setdefault(col_idx, []).append(t)
                col_idx += 1
        else:
            # 无竖线行：文本或箭头
            t = raw.strip(" +-=│┌┐└┘├┤┬┼─").strip()
            if t and not re.fullmatch(r"[▼▲vV↓↑]", t):
                cols.setdefault(0, []).append(t)
    if not cols:
        return ""
    out = ["flowchart TD"]
    ids: list[list[str]] = []
    for c in sorted(cols):
        col_ids: list[str] = []
        for idx, cell in enumerate(cols[c]):
            nid = f"C{c}_{idx}"
            out.append(f'    {nid}["{_esc(cell)}"]')
            col_ids.append(nid)
        ids.append(col_ids)
    # 纵向连接每列；列间首行横向连接
    for col in ids:
        for a, b in zip(col, col[1:]):
            out.append(f"    {a} --> {b}")
    if len(ids) >= 2:
        for i in range(len(ids) - 1):
            if ids[i] and ids[i + 1]:
                out.append(f"    {ids[i][0]} --> {ids[i+1][0]}")
    return "\n".join(out)


def convert_block(kind: str, block: list[str]) -> str:
    if kind == "timeline":
        return convert_timeline(block)
    if kind == "tree":
        return convert_tree(block)
    if kind == "vertical":
        return convert_vertical(block)
    if kind == "box":
        return convert_box(block)
    return ""


def is_clean_mermaid(mm: str) -> bool:
    """质量门槛：输出中不得残留制表符/框线字符。"""
    if not mm:
        return False
    if BOX_UNICODE.search(mm) or ASCII_BOX.search(mm):
        return False
    if mm.rstrip().endswith("-->"):
        return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--report", type=str, default="", help="未转换块清单 JSON")
    args = parser.parse_args()

    stats = {"timeline": 0, "tree": 0, "box": 0, "vertical": 0, "skipped-code": 0, "other": 0}
    warnings: list[dict] = []
    files_touched = 0

    for root in ROOTS:
        if not root.exists():
            continue
        for f in sorted(root.rglob("*.md")):
            lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
            out: list[str] = []
            i = 0
            changed = False
            while i < len(lines):
                stripped = lines[i].strip()
                if stripped.startswith("```"):
                    fence = stripped
                    lang = fence[3:].strip()
                    block: list[str] = []
                    j = i + 1
                    while j < len(lines) and not lines[j].strip().startswith("```"):
                        block.append(lines[j])
                        j += 1
                    end = j
                    if lang not in ("", "text", "txt"):
                        stats["skipped-code"] += 1
                        out.extend(lines[i : end + 1])
                        i = end + 1
                        continue
                    diag = [b for b in block if is_diagram_line(b)]
                    if lang in ("text", "txt"):
                        if not diag:
                            out.extend(lines[i : end + 1])
                            i = end + 1
                            continue
                    elif len(diag) < 2:
                        out.extend(lines[i : end + 1])
                        i = end + 1
                        continue
                    if diag:
                        kind = classify(block)
                        if kind == "other":
                            stats["other"] += 1
                            warnings.append(
                                {
                                    "file": str(f.relative_to(root)),
                                    "lines": f"{i+1}-{end+1}",
                                    "kind": kind,
                                }
                            )
                            out.extend(lines[i : end + 1])
                            i = end + 1
                            continue
                        mm = convert_block(kind, block)
                        if mm and is_clean_mermaid(mm):
                            out.append("```mermaid")
                            out.extend(mm.splitlines())
                            out.append("```")
                            stats[kind] += 1
                            changed = True
                            i = end + 1
                            continue
                        else:
                            stats["other"] += 1
                            warnings.append(
                                {
                                    "file": str(f.relative_to(root)),
                                    "lines": f"{i+1}-{end+1}",
                                    "kind": kind,
                                    "reason": "unclean output",
                                }
                            )
                            out.extend(lines[i : end + 1])
                            i = end + 1
                            continue
                    stats["other"] += 1
                    warnings.append(
                        {"file": str(f.relative_to(root)), "lines": f"{i+1}-{end+1}", "kind": "other"}
                    )
                    out.extend(lines[i : end + 1])
                    i = end + 1
                    continue
                out.append(lines[i])
                i += 1
            if changed:
                files_touched += 1
                if not args.dry_run:
                    f.write_text("\n".join(out) + "\n", encoding="utf-8")

    print(f"涉及文件: {files_touched}")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    if args.report:
        pathlib.Path(args.report).write_text(
            json.dumps(warnings, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"未转换清单: {args.report} ({len(warnings)} 块)")


if __name__ == "__main__":
    main()
