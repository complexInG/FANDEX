# -*- coding: utf-8 -*-
"""删除所有文档中“零基础入门”的 0.3 学习路径小节；整节为空时删除整节。"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")
AI_RE = re.compile(r"\\0(4[1-9]|5[0-0])-")

SEC = "## 0. 零基础入门（从零开始）"
SUB = "### 0.3 学习路径"
INTRO = "完成上面的第一步后，按以下顺序继续学习："


def process(path):
    text = open(path, encoding="utf-8").read()
    if SEC not in text:
        return False
    lines = text.split("\n")
    out = []
    i = 0
    changed = False
    while i < len(lines):
        if lines[i].strip() == SEC:
            # 收集整个 0 节
            j = i + 1
            block = [lines[i]]
            in_fence = False
            while j < len(lines):
                s = lines[j].strip()
                if s.startswith("```"):
                    in_fence = not in_fence
                    block.append(lines[j])
                    j += 1
                    continue
                if not in_fence and re.match(r"^##\s+", lines[j]):
                    break
                block.append(lines[j])
                j += 1
            # 去掉 0.3 小节
            cleaned = []
            k = 0
            in_03 = False
            while k < len(block):
                if block[k].strip() == SUB:
                    in_03 = True
                    k += 1
                    continue
                if in_03:
                    s = block[k].strip()
                    if s == INTRO or s.startswith("- ") or s == "":
                        k += 1
                        continue
                    # 遇到 0.3 之后的非空内容（一般不会出现）则结束
                    if re.match(r"^###\s+", block[k]):
                        in_03 = False
                        cleaned.append(block[k])
                        k += 1
                        continue
                    in_03 = False
                cleaned.append(block[k])
                k += 1
            # 判断剩余内容是否仍有实质小节（0.1/0.2 或非空段落）
            def _real(c):
                s = c.strip()
                if not s or s == "---" or s.startswith("---"):
                    return False
                return True

            has_content = any(
                re.match(r"^###\s+0\.[12]\b", c) or _real(c) for c in cleaned[1:]
            )
            if has_content:
                out.extend(cleaned)
            changed = True
            i = j
            continue
        out.append(lines[i])
        i += 1
    if changed:
        new = "\n".join(out)
        new = re.sub(r"\n{3,}", "\n\n", new)
        open(path, "w", encoding="utf-8", newline="\n").write(new)
    return changed


def main():
    files = 0
    for dp, dn, fn in os.walk(FULL):
        if AI_RE.search(dp):
            continue
        for f in sorted(fn):
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            if process(p):
                files += 1
    print("processed", files, "files")


if __name__ == "__main__":
    main()
