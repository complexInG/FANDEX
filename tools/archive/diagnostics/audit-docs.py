#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FANDEX full 文档质量审计工具

功能：
1. 扫描 cnt-content/full 下全部 .md 文档
2. 排除 AI 类模块（041-agent ~ 050-ai-ethics）
3. 统计每篇文档的体量、emoji、frontmatter 扩展字段、章节覆盖
4. 生成全量升级工作清单（按优先级与体量排序）

用法：
    python tools/audit-docs.py                # 输出 summary + worklist.csv
    python tools/audit-docs.py --json         # 同时输出 worklist.json
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FULL_DIR = ROOT / "cnt-content" / "full"

# 用户明确要求不升级的 AI 类模块
IGNORED_MODULES = {
    "041-agent",
    "042-machine-learning",
    "043-deep-learning",
    "044-ai-engineering",
    "045-computer-vision",
    "046-nlp",
    "047-llm",
    "048-generative-ai",
    "049-multimodal",
    "050-ai-ethics",
}

# 优先级：P0 编程语言类
P0_MODULES = {
    "002-markdown", "006-html5", "007-css", "008-javascript", "009-typescript",
    "010-vue3", "011-react", "012-svg", "013-java", "014-kotlin", "015-csharp",
    "016-go", "017-lua", "018-harmonyos", "019-sql", "025-c", "026-cpp", "040-python",
}

# P1 工具链类
P1_MODULES = {"001-getting-started", "003-git", "004-github", "005-english"}

# 论文级 12 段章节关键词（按顺序）
SECTIONS = [
    ("学习目标", re.compile(r"学习目标|Bloom|教学目标")),
    ("历史动机", re.compile(r"历史动机|发展脉络|历史|起源")),
    ("形式化定义", re.compile(r"形式化定义|规范定义|语法定义")),
    ("原理分析", re.compile(r"原理|推导|机制")),
    ("代码示例", re.compile(r"代码示例|示例代码|快速上手")),
    ("对比分析", re.compile(r"对比分析|对比表|横向对比")),
    ("常见陷阱", re.compile(r"常见陷阱|注意事项|易错")),
    ("工程实践", re.compile(r"工程实践|实战|生产环境")),
    ("案例研究", re.compile(r"案例研究|案例分析|完整案例")),
    ("习题", re.compile(r"习题|练习|思考题")),
    ("参考文献", re.compile(r"参考文献|Reference")),
    ("延伸阅读", re.compile(r"延伸阅读|扩展阅读|参考链接")),
]

EMOJI_RANGES = [
    (0x1F000, 0x1FAFF),
    (0xFE0F, 0xFE0F),
    (0x2764, 0x2764),
    (0x2728, 0x2728),
    (0x2B50, 0x2B50),
    (0x2705, 0x2705),
    (0x26A0, 0x26A1),
    (0x2600, 0x26FF),
]


def is_emoji(ch: str) -> bool:
    cp = ord(ch)
    return any(lo <= cp <= hi for lo, hi in EMOJI_RANGES)


def extract_frontmatter(text: str) -> dict | None:
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "-", "#")):
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()
    return fm


def fm_source(text: str) -> str | None:
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.S)
    return m.group(1) if m else None


def audit_doc(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    size = len(text.encode("utf-8"))
    emoji_count = sum(1 for ch in text if is_emoji(ch))
    fm = extract_frontmatter(text)
    fm_text = fm_source(text)
    sections_hit = []
    for name, pattern in SECTIONS:
        if pattern.search(text):
            sections_hit.append(name)
    has_ext = {
        key: bool(fm_text and re.search(rf"(?m)^{re.escape(key)}:", fm_text))
        for key in ("learningObjectives", "exercises", "references", "etymology")
    }
    rel = path.relative_to(FULL_DIR)
    module_dir = rel.parts[0] if len(rel.parts) > 1 else ""
    priority = "P0" if module_dir in P0_MODULES else "P1" if module_dir in P1_MODULES else "P2"
    return {
        "path": rel.as_posix(),
        "module": module_dir,
        "priority": priority,
        "size_bytes": size,
        "size_kb": round(size / 1024, 1),
        "emoji": emoji_count,
        "sections": len(sections_hit),
        "sections_detail": ";".join(sections_hit),
        "learningObjectives": has_ext["learningObjectives"],
        "exercises": has_ext["exercises"],
        "references": has_ext["references"],
        "etymology": has_ext["etymology"],
        "needs_upgrade": size < 15000 or emoji_count > 0 or not has_ext["learningObjectives"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="FANDEX full 文档质量审计")
    parser.add_argument("--json", action="store_true", help="同时输出 worklist.json")
    args = parser.parse_args()

    if not FULL_DIR.exists():
        print(f"目录不存在: {FULL_DIR}", file=sys.stderr)
        sys.exit(1)

    rows = []
    for md in sorted(FULL_DIR.rglob("*.md")):
        rel = md.relative_to(FULL_DIR)
        module_dir = rel.parts[0] if len(rel.parts) > 1 else ""
        if module_dir in IGNORED_MODULES:
            continue
        rows.append(audit_doc(md))

    rows.sort(key=lambda r: (r["priority"], r["module"], r["size_bytes"]))

    total = len(rows)
    needs = [r for r in rows if r["needs_upgrade"]]
    emoji_files = [r for r in rows if r["emoji"] > 0]

    print(f"=== FANDEX full 文档审计报告 ===")
    print(f"非 AI 文档总数: {total}")
    print(f"需要升级: {len(needs)} ({len(needs)/total*100:.1f}%)")
    print(f"含 emoji: {len(emoji_files)}")
    print(f"含 learningObjectives: {sum(1 for r in rows if r['learningObjectives'])}")
    print(f"含 exercises: {sum(1 for r in rows if r['exercises'])}")
    print(f"含 references: {sum(1 for r in rows if r['references'])}")
    print()
    print("按优先级与体量统计:")
    for pri in ("P0", "P1", "P2"):
        sub = [r for r in rows if r["priority"] == pri]
        if not sub:
            continue
        weak = sum(1 for r in sub if r["size_kb"] < 15)
        print(f"  {pri}: {len(sub)} 篇, 其中 <15KB {weak} 篇, emoji {sum(1 for r in sub if r['emoji'])} 篇")

    out_csv = ROOT / "tools" / "worklist.csv"
    with out_csv.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "path", "module", "priority", "size_kb", "emoji", "sections",
                "learningObjectives", "exercises", "references", "etymology",
                "needs_upgrade",
            ],
        )
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r[k] for k in writer.fieldnames})

    if args.json:
        out_json = ROOT / "tools" / "worklist.json"
        out_json.write_text(
            json.dumps({"generated_at": "2026-08-01", "docs": rows}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"\n已输出: {out_json}")

    print(f"已输出工作清单: {out_csv}")


if __name__ == "__main__":
    main()
