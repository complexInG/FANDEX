# -*- coding: utf-8 -*-
"""修复 Markdown 图片/链接目的地为占位文本的问题（仅在代码围栏与行内代码之外）。"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
AI_RE = re.compile(r"\\0(4[1-9]|5[0-0])-")

# 目标占位符 -> 示例 URL
REPLACE = {
    "url": "https://example.com/image.png",
    "链接": "https://example.com/image.png",
    "图片地址": "https://example.com/image.png",
    "图片URL": "https://example.com/image.png",
    "<图片URL>": "https://example.com/image.png",
    "<链接URL>": "https://example.com/page",
    "链接URL": "https://example.com/page",
    "<相对路径>": "images/example.png",
    "src": "https://example.com/image.png",
}


def mask_line(line, in_code):
    """跨行状态机：把位于行内代码内的字符替换为空格。返回掩码与新的 in_code 状态。"""
    out = list(line)
    i = 0
    while i < len(line):
        if line[i] == "`":
            # 围栏内的反引号已在 fence 分支跳过；这里只处理行内代码
            if in_code:
                in_code = False
                out[i] = " "
                i += 1
                continue
            # 打开行内代码；双反引号视为代码定界（内容按代码处理）
            j = i
            while j < len(line) and line[j] == "`":
                j += 1
            for k in range(i, j):
                out[k] = " "
            in_code = True
            i = j
            continue
        if in_code:
            out[i] = " "
        i += 1
    return "".join(out), in_code


def fix(path):
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    fence = 0
    in_code = False
    changed = 0
    img_re = re.compile(r"(!?\[[^\]]*\]\()([^)\s]+)(\s+\"[^\"]*\")?\)")
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```"):
            fence += 1
            in_code = False
            continue
        if fence % 2 == 1:
            continue
        masked, in_code = mask_line(line, in_code)
        # 修复“行尾悬空反引号 + 下一行以反引号开头”的格式错误（反引号本应是加粗结束符）
        if (
            idx + 1 < len(lines)
            and line.rstrip().endswith("`")
            and not line.rstrip().endswith("``")
            and lines[idx + 1].lstrip().startswith("`")
        ):
            lines[idx] = line.rstrip()[:-1] + "**"
        repls = []
        for m in img_re.finditer(masked):
            dest = m.group(2)
            if dest in REPLACE:
                repls.append((m.start(2), m.end(2), REPLACE[dest]))
        if repls:
            # 从右向左应用，避免偏移错位
            cur = lines[idx]
            for start, end, new_dest in sorted(repls, reverse=True):
                cur = cur[:start] + new_dest + cur[end:]
            lines[idx] = cur
            changed += len(repls)
    new_text = "\n".join(lines)
    if changed:
        open(path, "w", encoding="utf-8", newline="\n").write(new_text)
    return changed


def main():
    total = 0
    files = 0
    for dp, dn, fn in os.walk(FULL):
        if AI_RE.search(dp):
            continue
        for f in fn:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            c = fix(p)
            if c:
                total += c
                files += 1
                print(p, c)
    print("fixed", total, "in", files, "files")


if __name__ == "__main__":
    main()
