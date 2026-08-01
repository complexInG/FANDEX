# -*- coding: utf-8 -*-
"""清理文档尾部段落：
1. 删除更新日志/更新记录/变更记录/Changelog 等段落（从标题到文档末尾或下一个一级/二级标题前）
2. 将习题段转换为讲解段（保留内容，改写标题与语气）
"""

from __future__ import annotations

import pathlib
import re
import sys
import argparse

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
FULL = ROOT / "cnt-content" / "full"

UPDATE_HEAD = re.compile(
    r"^#{1,4}\s*(?:更新日志|更新记录|变更记录|Changelog|更新历史|版本历史|附录[:：]?\s*更新)",
    re.M,
)
EXERCISE_HEAD = re.compile(
    r"^#{1,4}\s*(?:习题|练习题|练习|思考题|测试题|题目|作业|LeetCode\s*练习|编程练习)",
    re.M,
)


def remove_update_sections(text: str) -> tuple[str, int]:
    """删除更新记录段：标题行到下一个 H1/H2 或文件末尾。"""
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    removed = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        if UPDATE_HEAD.match(line):
            # 跳过该段直到下一个 H1/H2（不含）或文件末尾
            removed += 1
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if re.match(r"^#{1,2}\s", nxt) and not UPDATE_HEAD.match(nxt):
                    break
                i += 1
            continue
        out.append(line)
        i += 1
    return "".join(out), removed


def convert_exercise_sections(text: str) -> tuple[str, int]:
    """将习题标题改写为讲解标题，去除答题语气（'请回答/请实现/试分析' → 讲解引导语）。"""
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    converted = 0
    in_exercise = False
    for line in lines:
        if EXERCISE_HEAD.match(line):
            in_exercise = True
            converted += 1
            title = re.sub(r"^#{1,4}\s*", "", line).strip()
            out.append(f"## 知识讲解与要点分析（原{title}）\n")
            continue
        if in_exercise:
            # 改写答题语气
            new = line
            new = re.sub(r"^[-*]\s*(请)?(回答|解答|分析|实现|编写|说明|解释|列举|比较|简述)[:：]?", "- 要点：", new)
            new = re.sub(r"^(\d+)[\.、]\s*(请)?(回答|解答|分析|实现|编写|说明|解释|列举|比较|简述)", r"\1. 要点：", new)
            new = re.sub(r"答案[:：]", "讲解要点：", new)
            new = re.sub(r"参考答案[:：]", "讲解要点：", new)
            out.append(new)
        else:
            out.append(line)
    return "".join(out), converted


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--file", type=str, default="", help="仅处理指定相对路径")
    args = parser.parse_args()
    stats_update = 0
    stats_exercise = 0
    for f in FULL.rglob("*.md"):
        rel = f.relative_to(FULL).as_posix()
        if args.file and rel != args.file:
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        new_text, n_up = remove_update_sections(text)
        new_text, n_ex = convert_exercise_sections(new_text)
        if n_up or n_ex:
            if not args.dry_run:
                f.write_text(new_text, encoding="utf-8")
            stats_update += n_up
            stats_exercise += n_ex
            print(f"{'[dry]' if args.dry_run else '处理'}: {rel} 删除更新段 {n_up}, 转换习题段 {n_ex}")
            if args.dry_run and n_ex:
                # 打印转换后的习题段开头
                for line in new_text.splitlines():
                    if "知识讲解与要点分析" in line:
                        print("     ->", line.strip())
                        break
    print(f"总计: 删除更新段 {stats_update}, 转换习题段 {stats_exercise}")


if __name__ == "__main__":
    main()
