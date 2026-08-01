# -*- coding: utf-8 -*-
"""全库内容校验：习题/更新记录/emoji/ASCII/YAML/行数统计。"""
import os
import re
import sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
AI_RE = re.compile(r"\\0(4[1-9]|5[0-0])-")

EX = re.compile(r"^(#{2,4})\s*\d*[\.\u3001]?\s*(习题|练习|作业|思考题|自测|测验|课堂练习|随堂练习)")
UP = re.compile(r"^(#{2,4})\s*(更新记录|更新日志|变更记录|Changelog|版本记录|修订记录|维护记录)")
EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F"
    "\u2764\u2728\u2705\u274C\u26A0\u26AA\u26AB\u2B06\u2B07\u2B05\u27A1\u2B55\u2B1C]"
)


def scan():
    stats = {"docs": 0, "exercise": [], "update": [], "emoji": [], "yaml": [], "lines": []}
    for dp, dn, fn in os.walk(FULL):
        if AI_RE.search(dp):
            continue
        for f in sorted(fn):
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            text = open(p, encoding="utf-8").read()
            stats["docs"] += 1
            stats["lines"].append((p, len(text.splitlines())))
            lines = text.split("\n")
            for i, line in enumerate(lines, 1):
                if EX.search(line):
                    stats["exercise"].append((p, i, line.strip()[:50]))
                if UP.search(line):
                    stats["update"].append((p, i, line.strip()[:50]))
                if EMOJI.search(line):
                    stats["emoji"].append((p, i, line.strip()[:50]))
            m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
            if not m:
                stats["yaml"].append((p, "no frontmatter"))
            else:
                try:
                    yaml.safe_load(m.group(1))
                except Exception as e:
                    stats["yaml"].append((p, str(e)[:100]))
    return stats


def main():
    s = scan()
    print("docs:", s["docs"])
    print("exercise sections:", len(s["exercise"]))
    for h in s["exercise"][:10]:
        print("  ", h)
    print("update sections:", len(s["update"]))
    for h in s["update"][:10]:
        print("  ", h)
    print("emoji lines:", len(s["emoji"]))
    for h in s["emoji"][:10]:
        print("  ", h)
    print("yaml issues:", len(s["yaml"]))
    for h in s["yaml"][:10]:
        print("  ", h)
    lt1500 = [x for x in s["lines"] if x[1] < 1500]
    ge1500 = [x for x in s["lines"] if x[1] >= 1500]
    print("lines <1500:", len(lt1500), " >=1500:", len(ge1500))
    import statistics
    print("median lines:", statistics.median(n for _, n in s["lines"]))


if __name__ == "__main__":
    main()
