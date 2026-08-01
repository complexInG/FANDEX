# -*- coding: utf-8 -*-
"""删除 024-cs-fundamentals 001 文档中误插入的 path-only 入门段，供重新插入完整版。"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(ROOT, "cnt-content", "full", "024-cs-fundamentals", "001-ComputerOverview.md")
t = open(p, encoding="utf-8").read()
marker = "## 0. 零基础入门（从零开始）"
if marker in t:
    start = t.index(marker)
    # 找到下一个 ## 或 ### 0.x 段结尾：截到下一个 "## " 或文件尾
    after = t[start + len(marker):]
    m = re.search(r"\n(?=## )", after)
    end = start + len(marker) + (m.start() if m else len(after))
    t = t[:start] + t[end:]
    open(p, "w", encoding="utf-8", newline="\n").write(t)
    print("removed, lines:", len(t.splitlines()))
else:
    print("marker not found")
