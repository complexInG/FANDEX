# -*- coding: utf-8 -*-
"""
删除所有“学习目标（Bloom 分类）”类小节（正文章节 + frontmatter 的
learningObjectives / exercises 字段），并把后续编号章节顺延重排。
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
AI_RE = re.compile(r"\\0(4[1-9]|5[0-0])-")

OBJ_HEAD = re.compile(r"^#{1,4}\s*\d*[\.\u3001]?\s*学习目标")
NUM_HEAD = re.compile(r"^(#{2,4})\s*(\d+)([\.\u3001].*)$")


def remove_body_section(lines):
    """删除学习目标小节（到下一个同级或更高级标题为止）。返回新行列表与是否删除。"""
    out = []
    removed = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if OBJ_HEAD.match(line):
            level = len(re.match(r"^#{1,4}", line).group(0))
            removed = True
            i += 1
            while i < len(lines):
                nxt = lines[i]
                nm = re.match(r"^(#{1,6})\s+", nxt)
                if nm and len(nm.group(1)) <= level:
                    break
                i += 1
            continue
        out.append(line)
        i += 1
    return out, removed


def renumber(lines):
    """把编号首段从 2..N 顺延为 1..N-1（支持 2、2.1、2.1.1 样式）。"""
    out = []
    for line in lines:
        m = NUM_HEAD.match(line)
        if m and int(m.group(2)) >= 2:
            level = m.group(1)
            new_num = int(m.group(2)) - 1
            out.append(f"{level} {new_num}{m.group(3)}")
        else:
            out.append(line)
    return out


def strip_frontmatter_field(fm, key):
    """删除 frontmatter 中的顶层字段（含缩进子行与同列块序列项）。"""
    lines = fm.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(rf"^{re.escape(key)}:", line):
            i += 1
            while i < len(lines):
                nxt = lines[i]
                if nxt.strip() == "":
                    i += 1
                    continue
                if nxt.startswith((" ", "\t")) or nxt.startswith("- "):
                    i += 1
                    continue
                break
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def process(path):
    t = open(path, encoding="utf-8").read()
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", t, re.S)
    changed = False
    if not m:
        return False
    fm = m.group(1)
    body = t[m.end():]
    body_lines = body.split("\n")
    body_lines, removed = remove_body_section(body_lines)
    if removed:
        body_lines = renumber(body_lines)
        changed = True
    for key in ("learningObjectives", "exercises"):
        if re.search(rf"^{re.escape(key)}:", fm, re.M) or re.search(rf"^{re.escape(key)}\s*$", fm, re.M):
            fm = strip_frontmatter_field(fm, key)
            changed = True
    if changed:
        new = f"---\n{fm}\n---\n\n" + "\n".join(body_lines)
        # 清理可能残留的连续空行（保留最多两个）
        new = re.sub(r"\n{4,}", "\n\n\n", new)
        open(path, "w", encoding="utf-8", newline="\n").write(new)
    return changed


def main():
    total = 0
    for dp, dn, fn in os.walk(FULL):
        if AI_RE.search(dp):
            continue
        for f in sorted(fn):
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            if process(p):
                total += 1
    remain = 0
    for dp, dn, fn in os.walk(FULL):
        if AI_RE.search(dp):
            continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            t = open(os.path.join(dp, f), encoding="utf-8").read()
            if OBJ_HEAD.search(t):
                remain += 1
            m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", t, re.S)
            if m and ("learningObjectives" in m.group(1) or re.search(r"^exercises:", m.group(1), re.M)):
                remain += 1
    print("processed", total, "docs; remain:", remain)


if __name__ == "__main__":
    main()
