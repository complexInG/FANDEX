# -*- coding: utf-8 -*-
"""将 mobile 文档内容适当融入 full 文档。

策略（标题级合并）：
1. 保留 full 的 frontmatter 与文档头信息
2. 解析 mobile 与 full 的章节（H2/H3）
3. mobile 有而 full 没有的章节 → 追加到 full（保持 mobile 章节顺序）
4. mobile 与 full 同名章节：若 mobile 行数明显更多（>=1.5x），保留 full 标题但以 mobile 内容替换
5. 不删除 full 中 mobile 没有的章节

安全：仅处理 map 中 status=merge/fuzzy 且 full_exact/full_fuzzy 命中的文件；
dry-run 预览；执行前自动备份到 tools/.merge-backup/。
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
FULL = ROOT / "cnt-content" / "full"
MOBILE = ROOT / "cnt-content" / "mobile"
MAP = ROOT / "tools" / "mobile-full-map.json"
BACKUP = ROOT / "tools" / ".merge-backup"


def split_frontmatter(text: str) -> tuple[str, str]:
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", text, re.S)
    if not m:
        return "", text
    return m.group(0), text[m.end():]


def parse_sections(body: str) -> list[tuple[str, str, str]]:
    """返回 [(标题级别, 标题文本, 章节内容)]，按文档顺序。"""
    sections: list[tuple[str, str, str]] = []
    lines = body.splitlines(keepends=True)
    current: list[str] = []
    cur_level = 2
    cur_title = "前言"
    for line in lines:
        m = re.match(r"^(#{2,3})\s+(.*?)\s*$", line)
        if m and line.startswith("##"):
            if current or sections:
                sections.append((f"h{cur_level}", cur_title, "".join(current)))
            cur_level = len(m.group(1))
            cur_title = m.group(2).strip()
            current = [line]
        else:
            current.append(line)
    if current:
        sections.append((f"h{cur_level}", cur_title, "".join(current)))
    return sections


def count_lines(s: str) -> int:
    return len([l for l in s.splitlines() if l.strip()])


def merge_pair(mobile_path: pathlib.Path, full_path: pathlib.Path) -> dict:
    mtext = mobile_path.read_text(encoding="utf-8")
    ftext = full_path.read_text(encoding="utf-8")
    fm, fbody = split_frontmatter(ftext)
    mm, mbody = split_frontmatter(mtext)
    msections = parse_sections(mbody)
    fsections = parse_sections(fbody)

    added = 0
    replaced = 0
    fmap = {t: (lv, c) for lv, t, c in fsections}
    merged: list[tuple[str, str, str]] = []
    used_mobile: set[str] = set()

    # 先替换同名且 mobile 更详细的章节
    for lv, title, content in msections:
        if title in fmap:
            flv, fc = fmap[title]
            if count_lines(content) >= count_lines(fc) * 1.5:
                merged.append((flv, title, content))
                replaced += 1
            else:
                merged.append((flv, title, fc))
            used_mobile.add(title)

    # 保留 full 独有章节（保持原顺序）
    for lv, title, content in fsections:
        if title not in used_mobile:
            merged.append((lv, title, content))

    # 追加 mobile 独有章节（按 mobile 顺序）
    tail: list[tuple[str, str, str]] = []
    for lv, title, content in msections:
        if title not in used_mobile and title not in fmap:
            tail.append((lv, title, content))
            added += 1

    out_lines: list[str] = []
    if fm:
        out_lines.append(fm.rstrip("\n"))
        out_lines.append("\n")
    for lv, title, content in merged:
        out_lines.append(content)
    for lv, title, content in tail:
        out_lines.append(content)

    new_text = "".join(out_lines)
    return {
        "mobile": mobile_path.relative_to(MOBILE).as_posix(),
        "full": full_path.relative_to(FULL).as_posix(),
        "added": added,
        "replaced": replaced,
        "before_lines": len(ftext.splitlines()),
        "after_lines": len(new_text.splitlines()),
        "new_text": new_text,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="只预览不写入")
    parser.add_argument("--limit", type=int, default=0, help="仅处理前 N 个文件（0=全部）")
    args = parser.parse_args()

    plan = json.loads(MAP.read_text(encoding="utf-8"))
    # 仅精确匹配；fuzzy 匹配过度（多个 mobile 文档命中同一 full），跳过避免错误合并
    candidates = [
        p
        for p in plan
        if p["status"] in ("merge", "fuzzy-resolved", "promote-dup")
        or (p["status"] == "fuzzy" and (p["full_exact"] or p["full_fuzzy"]))
    ]
    if args.limit:
        candidates = candidates[: args.limit]

    stats = {"merge": 0, "replaced": 0, "added": 0, "skipped": 0}
    seen_full: set[str] = set()
    for p in candidates:
        mrel = pathlib.Path(p["mobile"])
        targets = p["full_exact"] or p["full_fuzzy"]
        if not targets:
            stats["skipped"] += 1
            continue
        if targets[0] in seen_full:
            stats["skipped"] += 1
            continue
        seen_full.add(targets[0])
        mpath = MOBILE / mrel
        fpath = FULL / targets[0]
        if not mpath.exists() or not fpath.exists():
            stats["skipped"] += 1
            continue
        r = merge_pair(mpath, fpath)
        if args.dry_run:
            if r["added"] or r["replaced"]:
                print(
                    f"[dry] {r['full']}: +{r['added']} 章, 替换 {r['replaced']} 章, "
                    f"{r['before_lines']} -> {r['after_lines']} 行"
                )
        else:
            if r["added"] or r["replaced"]:
                BACKUP.mkdir(parents=True, exist_ok=True)
                bak = BACKUP / r["full"].replace("/", "__")
                bak.write_text(fpath.read_text(encoding="utf-8"), encoding="utf-8")
                fpath.write_text(r["new_text"], encoding="utf-8")
                stats["merge"] += 1
                stats["added"] += r["added"]
                stats["replaced"] += r["replaced"]
            else:
                stats["skipped"] += 1

    print(f"处理: merge={stats['merge']}, 新增章节={stats['added']}, 替换章节={stats['replaced']}, 跳过={stats['skipped']}")


if __name__ == "__main__":
    main()
