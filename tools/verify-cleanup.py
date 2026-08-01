# -*- coding: utf-8 -*-
"""抽查清理结果：确认模板废话已删除、真实内容保留。"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")

BAD_PATTERNS = [
    "本节按照布鲁姆教育目标分类学组织学习路径",
    "深入讲解：该问题之所以被归类为",
    "从成因上看，",
    "核心概念串讲",
    "术语表",
    "回到本文主题：",
    "该小节围绕",
    "对比是理解",
    "案例研究的学习方法",
    "把以上要点与第",
    "代码中的关键操作可以归纳为三步",
    "进阶思考路径",
    "速查表的作用是",
    "工程实践的共性原则",
]


def main():
    docs = [
        "006-html5/015-SVG.md",
        "006-html5/002-HTML5BasicTagGlobalAttribute.md",
        "020-mysql/032-RedoLog.md",
        "040-python/001-PythonOverviewEnvSetup.md",
        "008-javascript/001-JavaScriptOverviewRuntimeEnv.md",
        "010-vue3/001-OverviewEnv.md",
        "003-git/001-Git.md",
    ]
    for rel in docs:
        p = os.path.join(FULL, rel)
        t = open(p, encoding="utf-8").read()
        bad = [b for b in BAD_PATTERNS if b in t]
        heads = [l.strip() for l in t.split("\n") if l.startswith("## ")]
        print(f"{rel} | {len(t.splitlines())} 行 | 残留废话: {bad if bad else '无'}")
        print("   H2:", " | ".join(heads[:16]))


if __name__ == "__main__":
    main()
