#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
thesis-merge.py
将 tools/thesis-fragments/<module>/<doc>.md 中的论文级教学正文
合并进 cnt-content/full/<module>/<doc>.md：
1. 保留原有 frontmatter（只更新 description/updated 等元数据）
2. 正文以 fragment 为主干；原正文降级为“附录：原章节精读”保留
3. 习题类章节标题转换为讲解标题；删除更新记录类章节
4. 不引入 emoji；大型 ASCII 图转换为 Mermaid 由配套脚本处理
用法：python tools/thesis-merge.py [module/doc.md ...]
无参数时处理全部 fragment。
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
FRAG = os.path.join(ROOT, "tools", "thesis-fragments")

EXERCISE_HEAD = re.compile(r"^(#{2,4})\s*(\d+[\.、]\s*)?(习题|练习|作业|思考题|自测|测验|课堂练习|随堂练习)")
UPDATE_HEAD = re.compile(r"^(#{2,4})\s*(更新记录|更新日志|变更记录|Changelog|版本记录|修订记录|维护记录)")


def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write_text(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def split_frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


def convert_body(body):
    """转换习题标题为讲解标题，删除更新记录章节。"""
    lines = body.split("\n")
    out = []
    i = 0
    in_update = False
    while i < len(lines):
        line = lines[i]
        m = UPDATE_HEAD.match(line)
        if m:
            # 跳过该章节直到下一个同级或更高级标题
            level = len(m.group(1))
            in_update = True
            i += 1
            while i < len(lines):
                nxt = lines[i]
                nm = re.match(r"^(#{1,6})\s+", nxt)
                if nm and len(nm.group(1)) <= level:
                    break
                i += 1
            continue
        m = EXERCISE_HEAD.match(line)
        if m:
            level = m.group(1)
            num = m.group(2) or ""
            title = m.group(3)
            line = f"{level} {num}知识讲解与要点分析（原{title}）"
        out.append(line)
        i += 1
    return "\n".join(out)


def demote_headings(body, top_level=2):
    """把原正文 h2 降为 h3，h3 降为 h4，依次类推，最多降到 h6。"""
    lines = body.split("\n")
    out = []
    for line in lines:
        m = re.match(r"^(#{2,6})\s+", line)
        if m:
            level = len(m.group(1)) + 1
            if level > 6:
                level = 6
            line = "#" * level + line[len(m.group(1)):]
        out.append(line)
    return "\n".join(out)


def merge(fragment_path):
    rel = os.path.relpath(fragment_path, FRAG)
    mod, name = rel.split(os.sep)
    doc_path = os.path.join(FULL, mod, name)
    if not os.path.exists(doc_path):
        print(f"SKIP (no target): {rel}")
        return False
    frag = read_text(fragment_path)
    orig = read_text(doc_path)
    fm, orig_body = split_frontmatter(orig)
    if fm is None:
        print(f"SKIP (no frontmatter): {rel}")
        return False
    orig_body = convert_body(orig_body)
    # 防止原正文与 fragment 重复：fragment 含 {{APPENDIX}} 占位符
    appendix = demote_headings(orig_body)
    if "{{APPENDIX}}" in frag:
        body = frag.replace("{{APPENDIX}}", appendix)
    else:
        body = frag + "\n\n## 附录：原章节精读（完整保留）\n\n" + appendix
    # 更新 updated 字段
    if "updated:" in fm:
        fm = re.sub(r"(?m)^updated:.*$", "updated: '2026-08-01'", fm)
    else:
        fm += "\nupdated: '2026-08-01'"
    new_text = f"---\n{fm}\n---\n\n{body}"
    write_text(doc_path, new_text)
    print(f"OK: {rel} ({len(body.splitlines())} body lines)")
    return True


def main():
    args = sys.argv[1:]
    if args:
        targets = []
        for a in args:
            if os.sep not in a and "/" not in a:
                # 视为模块目录，处理其下所有 fragment
                d = os.path.join(FRAG, a)
                targets.extend(os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith(".md"))
            else:
                targets.append(os.path.join(FRAG, a))
    else:
        targets = []
        for dp, _, fn in os.walk(FRAG):
            for f in sorted(fn):
                if f.endswith(".md"):
                    targets.append(os.path.join(dp, f))
    for t in targets:
        if os.path.exists(t):
            merge(t)


if __name__ == "__main__":
    main()
