# -*- coding: utf-8 -*-
"""扫描文档中的更新记录段与习题段。"""

from __future__ import annotations

import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
FULL = ROOT / "cnt-content" / "full"

UPDATE_RE = re.compile(r"^#{1,4}\s*(?:更新日志|更新记录|变更记录|Changelog|更新历史|版本历史)", re.M)
EXERCISE_RE = re.compile(r"^#{1,4}\s*(?:习题|练习题|练习|思考题|测试题|题目|作业)", re.M)


def main() -> None:
    update_files = []
    exercise_files = []
    for f in FULL.rglob("*.md"):
        text = f.read_text(encoding="utf-8", errors="replace")
        if UPDATE_RE.search(text):
            update_files.append(f.relative_to(FULL).as_posix())
        if EXERCISE_RE.search(text):
            exercise_files.append(f.relative_to(FULL).as_posix())
    print(f"更新记录段文件: {len(update_files)}")
    print(f"习题段文件: {len(exercise_files)}")
    print("--- 更新记录示例 ---")
    for x in update_files[:10]:
        print(" ", x)
    print("--- 习题示例 ---")
    for x in exercise_files[:10]:
        print(" ", x)


if __name__ == "__main__":
    main()
