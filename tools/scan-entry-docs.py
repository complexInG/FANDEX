# -*- coding: utf-8 -*-
"""检查每个非 AI 模块 001 文档是否具备零基础入门要素。"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
AI_RE = re.compile(r"\\0(4[1-9]|5[0-0])-")

KEYS = {
    "first": ["第一个", "Hello", "hello", "你好", "入门示例", "快速开始", "快速入门", "首个"],
    "pre": ["前置", "零基础", "不需要", "无需", "先决", "前提", "基础要求", "适合谁", "适合人群"],
    "env": ["安装", "下载", "环境", "配置", "setup", "Setup"],
    "path": ["学习路径", "学习路线", "下一步", "继续学习", "进阶"],
}


def main():
    for dp, dn, fn in os.walk(FULL):
        if AI_RE.search(dp):
            continue
        files = sorted(f for f in fn if f.endswith(".md"))
        if not files:
            continue
        first = files[0]
        p = os.path.join(dp, first)
        t = open(p, encoding="utf-8").read()
        found = {k: [] for k in KEYS}
        for i, line in enumerate(t.split("\n"), 1):
            for k, words in KEYS.items():
                for w in words:
                    if w in line:
                        found[k].append((i, w))
                        break
        flags = "".join("1" if found[k] else "0" for k in KEYS)
        print(f"{os.path.basename(dp):28s} 首文={first:40s} 首例/前置/环境/路径={flags}")


if __name__ == "__main__":
    main()
