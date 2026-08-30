# -*- coding: utf-8 -*-
"""
由子文档再生成 54 个 000-xxx-MERGED 合集文件。

规则：
- 子文档按文件名编号升序拼接，frontmatter 剥离
- 分隔线：<!-- ============ 文档分隔线：{目录号}-{module}/{文件名} ============ -->
- 合集 frontmatter 统一重建（title 不带目录号，updated 取今日）
- 行尾统一 LF
"""
import io
import os
import re
import glob
import sys
import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
ROOT = r"C:\Atian\Project\FANDEX\cnt-content\full"
TODAY = "2026-08-29"

fm_re = re.compile(r"^---\s*\r?\n(.*?)\r?\n---\s*\r?\n", re.S)
title_re = re.compile(r"^title:\s*(.+?)\s*$", re.M)
category_re = re.compile(r"^category:\s*(.+?)\s*$", re.M)

made = 0
for path in sorted(glob.glob(os.path.join(ROOT, "*", "000-*-MERGED.md"))):
    module_dir = os.path.dirname(path)
    module = os.path.basename(module_dir).split("-", 1)[1]
    dirno = os.path.basename(module_dir).split("-", 1)[0]
    subdocs = sorted(
        [p for p in glob.glob(os.path.join(module_dir, "*.md"))
         if not os.path.basename(p).startswith("000-")],
        key=lambda p: int(re.match(r"(\d+)-", os.path.basename(p)).group(1)),
    )
    if not subdocs:
        continue
    first_fm = fm_re.match(open(subdocs[0], encoding="utf-8").read())
    cat = "工具链"
    if first_fm:
        cm = category_re.search(first_fm.group(1))
        if cm:
            cat = cm.group(1).strip()
    parts = [
        "---",
        "order: 10",
        "title: %s 模块文档合集" % module,
        "module: '%s'" % module,
        "category: " + cat,
        "difficulty: intermediate",
        "description: 本模块全部文档合并生成的完整合集，按学习顺序排列。",
        "author: fanquanpp",
        "updated: '%s'" % TODAY,
        "related: []",
        "prerequisites: []",
        "---",
        "",
    ]
    for sd in subdocs:
        t = open(sd, encoding="utf-8").read().replace("\r\n", "\n")
        bm = fm_re.match(t)
        body = t[bm.end():] if bm else t
        body = body.strip("\n")
        rel = "%s-%s/%s" % (dirno, module, os.path.basename(sd))
        parts.append("<!-- ============ 文档分隔线：%s ============ -->" % rel)
        parts.append("")
        parts.append(body)
        parts.append("")
    out = "\n".join(parts).rstrip("\n") + "\n"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(out)
    made += 1
print("MERGED regenerated:", made)
