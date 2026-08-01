# -*- coding: utf-8 -*-
"""预览 clean-doc-sections 对指定文件的转换结果。"""

from __future__ import annotations

import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")

import importlib.util

_spec = importlib.util.spec_from_file_location(
    "clean_doc_sections", pathlib.Path(__file__).parent / "clean-doc-sections.py"
)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


def main() -> None:
    rel = sys.argv[1] if len(sys.argv) > 1 else "004-github/029-GitHubActionsCICD.md"
    f = mod.FULL / rel
    text = f.read_text(encoding="utf-8")
    new_text, n_up = mod.remove_update_sections(text)
    new_text, n_ex = mod.convert_exercise_sections(new_text)
    print(f"删除更新段: {n_up}, 转换习题段: {n_ex}")
    print("=== 转换后新增的讲解段 ===")
    idx = new_text.find("知识讲解与要点分析")
    if idx >= 0:
        print(new_text[idx : idx + 900])


if __name__ == "__main__":
    main()
