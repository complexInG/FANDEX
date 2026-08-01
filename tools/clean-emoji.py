#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FANDEX full 文档 emoji 清理工具

将文档中的 emoji 表情替换为语义化文本（不删除文档文件）：
- 代码字符串中的 emoji 替换为 \\u{...} 转义，保持代码可运行
- 表格/装饰场景的 emoji 替换为文字评价
- 保留 ★ ☐ ☰ 等排版符号（非 emoji 表情）？否：按用户要求全部消除，转换为文本

用法：python tools/clean-emoji.py
"""

from __future__ import annotations

import pathlib
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT = pathlib.Path(__file__).resolve().parent.parent
FULL_DIR = ROOT / "cnt-content" / "full"

# 需要清理的 emoji 码点区间
RANGES = [
    (0x1F000, 0x1FAFF),
    (0xFE0F, 0xFE0F),
    (0x2764, 0x2764),
    (0x2728, 0x2728),
    (0x2B50, 0x2B50),
    (0x2705, 0x2705),
    (0x26A0, 0x26A1),
    (0x2600, 0x26FF),
    (0x266F, 0x266F),  # ♯
    (0x2610, 0x2611),  # ☐ ☑
    (0x2630, 0x2630),  # ☰
]


def is_emoji(ch: str) -> bool:
    cp = ord(ch)
    return any(lo <= cp <= hi for lo, hi in RANGES)


# 单字符/短序列到文本的映射（装饰场景）
CHAR_TEXT = {
    "⭐": "低",
    "⭐⭐": "中",
    "⭐⭐⭐": "高",
    "⭐⭐⭐⭐": "很高",
    "⭐⭐⭐⭐⭐": "极高",
    "★★★★★": "极高",
    "★★★★": "很高",
    "★★★": "较高",
    "★★": "中",
    "★": "低",
    "★★★★☆": "很高",
    "★★★★★☆": "极高",
    "★★★☆☆": "中",
    "✅": "已达标",
    "❌": "不支持",
    "⚠": "警告",
    "☀": "日",
    "🌙": "月",
    "⚡": "闪电",
    "☕": "咖啡",
    "☰": "菜单",
    "☐": "[ ]",
    "☑": "[x]",
    "♯": "升号",
    "✨": "",
    "🔥": "",
    "📱": "手机",
    "🎉": "庆祝",
    "😀": "笑脸",
    "🇨": "地区",
    "👩": "女性",
    "👦": "男孩",
    "🏿": "深肤色",
    "👧": "女孩",
    "👨": "男性",
    "1️⃣": "数字键1",
    "\uFE0F": "",
}

# 代码字符串中的 emoji -> \\u{...} 转义（保持可运行）
CODE_ESCAPES = {
    "😀": "\\u{1F600}",
    "🎉": "\\u{1F389}",
    "🔥": "\\u{1F525}",
    "📱": "\\u{1F4F1}",
    "✨": "\\u{2728}",
    "☕": "\\u2615",
    "🇨🇳": "\\u{1F1E8}\\u{1F1F3}",
    "👨\u200d👩\u200d👧\u200d👦": "\\u{1F468}\\u200D\\u{1F469}\\u200D\\u{1F467}\\u200D\\u{1F466}",
    "👦🏿": "\\u{1F466}\\u{1F3FF}",
    "1️⃣": "\\u0031\\uFE0F\\u20E3",
}


def escape_code_emoji(text: str) -> str:
    """将字符串字面量中的 emoji 转义为 \\u{...}，仅在代码行内处理。"""
    for emoji, esc in CODE_ESCAPES.items():
        text = text.replace(emoji, esc)
    # 通用：把剩余 emoji 转为 \\u{HEX}
    out = []
    for ch in text:
        if is_emoji(ch):
            out.append("\\u{%X}" % ord(ch))
        else:
            out.append(ch)
    return "".join(out)


def is_code_line(line: str) -> bool:
    stripped = line.lstrip()
    # 含引号与赋值/运算的赋值语句也视为代码（如 emoji_str = "🎉" * 1000）
    if '"' in line or "'" in line:
        if any(op in line for op in ("= ", " * ", "(", ")")):
            return True
    return stripped.startswith(("```", "#", "//", "/*", "*", "console.", "const ",
                                "let ", "var ", "function ", "print", "Text(", "@",
                                "import ", "assert", "val ", "enum ", "typedef ",
                                "icon:")) or line.strip().startswith(("- [",))


def clean_file(path: pathlib.Path) -> tuple[int, int]:
    """返回 (替换前 emoji 数, 替换后残留 emoji 数)。"""
    text = path.read_text(encoding="utf-8")
    before = sum(1 for ch in text if is_emoji(ch))
    lines = text.splitlines(keepends=True)
    new_lines = []
    for line in lines:
        # 表格装饰行：整体替换常用评价序列
        if "|" in line and any(seq in line for seq in ("⭐", "★", "✅", "❌")):
            for seq, txt in sorted(CHAR_TEXT.items(), key=lambda kv: -len(kv[0])):
                line = line.replace(seq, txt)
            # 表格内"已达标"等列文本无需再处理
            new_lines.append(line)
            continue
        # 代码行：转义为 \\u{...}
        if is_code_line(line) and any(is_emoji(ch) for ch in line):
            if line.lstrip().startswith(("//", "#", "/*", "*")):
                # 注释保留可读性：emoji 替换为文字
                for seq, txt in sorted(CHAR_TEXT.items(), key=lambda kv: -len(kv[0])):
                    line = line.replace(seq, txt)
                new_lines.append(line)
            else:
                new_lines.append(escape_code_emoji(line))
            continue
        # 其他行：替换为文字
        for seq, txt in sorted(CHAR_TEXT.items(), key=lambda kv: -len(kv[0])):
            line = line.replace(seq, txt)
        # 剩余 emoji 通用转义（若仍在字符串外则转为文字描述）
        out = []
        for ch in line:
            if is_emoji(ch):
                out.append(CHAR_TEXT.get(ch, "符号"))
            else:
                out.append(ch)
        new_lines.append("".join(out))
    result = "".join(new_lines)
    after = sum(1 for ch in result if is_emoji(ch))
    path.write_text(result, encoding="utf-8")
    return before, after


def main() -> None:
    total_before = 0
    total_after = 0
    changed = 0
    for md in sorted(FULL_DIR.rglob("*.md")):
        text = md.read_text(encoding="utf-8", errors="replace")
        if not any(is_emoji(ch) for ch in text):
            continue
        before, after = clean_file(md)
        total_before += before
        total_after += after
        changed += 1
        status = "OK" if after == 0 else f"REMAIN {after}"
        print(f"{status} {md.relative_to(FULL_DIR).as_posix()} ({before} -> {after})")
    print(f"\n共处理 {changed} 个文件，emoji 从 {total_before} 降至 {total_after}")


if __name__ == "__main__":
    main()
