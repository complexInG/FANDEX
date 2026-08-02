# -*- coding: utf-8 -*-
"""移除全库文档的"例题/练习"小节，并精简尾部外部链接内容。

用途：
  1. 删除各文档中专门的例题/练习/习题/自测/思考题/作业/参考答案等小节；
  2. 删除尾部纯外部资源类小节（参考文献、参考链接、在线资源等）；
  3. 对"延伸阅读/相关文档"类小节仅剥离外链行，保留站内交叉引用；
  4. 删除纯例题专册（文件名/标题为"XX典型例题"的整篇文档）；
  5. 同步清理 frontmatter 中指向被删文档的 related 条目，以及因删除
     小节而过时的 description 描述。

用法：
  python tools/remove-exercises-and-links.py          # 干跑，输出改动预览
  python tools/remove-exercises-and-links.py --apply  # 实际写回文件

幂等性：
  脚本设计为可重复运行；第二次运行应报告 0 处新增改动。

注意：
  - 只删除"标题级"的例题/练习小节，不删除正文中的教学示例
    （如 "**例 1**：..."、"代码示例"、"案例研究"），以保留零基础可读性；
  - 代码块中的内容不受影响（按围栏状态跳过）。
"""

from __future__ import annotations

import re
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
CONTENT_ROOTS = [ROOT / "cnt-content" / "full", ROOT / "cnt-content" / "mobile"]

# ---------------------------------------------------------------------------
# 规则配置
# ---------------------------------------------------------------------------

# 纯例题专册：整篇文档内容都是例题/练习，直接删除文件（git 可恢复）。
DELETED_EXAMPLE_DOCS = [
    "027-calculus/011-FunctionAndLimitExamples.md",
    "027-calculus/012-DerivativeAndDifferentialExamples.md",
    "027-calculus/013-DifferentialMeanValueTheoremExamples.md",
    "027-calculus/014-IndefiniteIntegralExamples.md",
    "027-calculus/015-DefiniteIntegralApplicationExamples.md",
    "027-calculus/016-MultivariateFunctionDifferentialExamples.md",
    "027-calculus/017-MultipleIntegralExamples.md",
    "027-calculus/018-CurveAndSurfaceIntegralExamples.md",
    "027-calculus/019-InfiniteSeriesAndODEExamples.md",
    "029-linear-algebra/006-DeterminantExamples.md",
    "029-linear-algebra/012-MatrixExamples.md",
    "029-linear-algebra/018-LinearSystemOfEquationsExamples.md",
    "029-linear-algebra/024-VectorSpaceExamples.md",
    "029-linear-algebra/029-EigenvalueExamples.md",
    "029-linear-algebra/033-QuadraticFormExamples.md",
    "030-probability-statistics/007-ProbabilityBasicsExamples.md",
    "030-probability-statistics/013-RandomVariableExamples.md",
    "030-probability-statistics/019-MultivariateRandomVariableExamples.md",
    "030-probability-statistics/025-NumericalCharacteristicsExamples.md",
    "030-probability-statistics/029-LLNAndCLTExamples.md",
    "030-probability-statistics/034-SamplingDistributionExamples.md",
    "030-probability-statistics/039-ParameterEstimationExamples.md",
    "030-probability-statistics/045-HypothesisTestingExamples.md",
]

# 被删文档的标题关键词，用于清理 related 条目与延伸阅读中的失效引用。
DELETED_TITLE_KEYS = [
    "行列式典型例题",
    "矩阵典型例题",
    "线性方程组典型例题",
    "向量空间典型例题",
    "特征值典型例题",
    "二次型典型例题",
    "函数与极限典型例题",
    "导数与微分典型例题",
    "微分中值定理典型例题",
    "不定积分典型例题",
    "定积分与应用典型例题",
    "多元函数微分典型例题",
    "重积分典型例题",
    "曲线与曲面积分典型例题",
    "无穷级数与常微分方程典型例题",
    "概率基础典型例题",
    "随机变量典型例题",
    "多维随机变量典型例题",
    "数字特征典型例题",
    "大数定律与中心极限定理典型例题",
    "抽样分布典型例题",
    "参数估计典型例题",
    "假设检验典型例题",
]

# 标题中包含这些关键词的小节整体删除（含历史清理遗留的"原习题"转化节）。
DELETE_CONTAINS = (
    "原习题",
    "原练习",
    "原思考题",
    "原练习题",
    "原题目",
    "原作业",
    "综合题知识点讲解",
    "选择题知识点讲解",
    "习题映射",
    "面试题",
)

# 标题以这些关键词开头的小节整体删除（编号前缀先被剥离）。
DELETE_PREFIXES = (
    "例题",
    "典型例题",
    "完整例题",
    "例题详解",
    "例题解析",
    "实践练习",
    "常见面试题",
    "高频面试题",
    "经典面试题",
    "经典例题",
    "综合例题",
    "深入例题",
    "进阶习题",
    "进阶练习",
    "挑战练习",
    "进阶思考题",
    "开放性习题",
    "思考与练习",
    "实战练习",
    "实战演练",
    "课后练习",
    "课后作业",
    "单元练习",
    "阶段练习",
    "阶段测验",
    "上机练习",
    "编程练习",
    "章节练习",
    "模拟测验",
    "模拟练习",
    "练习题",
    "练习",
    "习题",
    "思考题",
    "自测",
    "测验",
    "作业",
    "真题",
    "面试题",
    "参考答案",
    "答案要点",
    "题目",
    "题库",
    "随堂",
    "课堂练习",
    "实战题",
    "复习自测",
    "综合练习",
    "工程练习",
    "工程实现练习",
    "在线练习",
    "推荐练习",
    "基础练习",
    "中级练习",
    "高级练习",
    "单元测验",
    "小测验",
    "测试题",
    "开放思考题",
    "专项训练",
    "综合题",
)

# 误伤豁免：标题命中删除关键词但属于正常教学内容时在此排除。
DELETE_EXCEPTIONS = (
    # CI/流水线中的"作业配置"指 job 配置，与练习题无关。
    "作业配置",
)

# 标题以这些关键词结尾的小节整体删除（先检查 DELETE_KEEP_CONTAINS 豁免）。
DELETE_SUFFIXES = (
    "例题",
    "习题",
    "思考题",
    "自测",
    "测验",
    "练习",
    "参考答案",
    "答案要点",
    "题库",
    "真题",
    "综合题",
)

# 混合型教学小节豁免：标题虽含例题/练习字样，但主体是概念讲解或公式推导。
DELETE_KEEP_CONTAINS = (
    "公式推导",
    "一个直观例题",
    "先理解再算",
    "学习路径",
    "翻译练习方法",
)

# 尾部纯外部资源类小节：整体删除。
TAIL_DELETE_PREFIXES = (
    "参考文献",
    "参考链接",
    "相关链接",
    "参考资料",
    "参考资源",
    "参考书目",
    "参考文档",
    "参考网站",
    "在线资源",
    "社区资源",
    "官方资源",
    "视频资源",
    "学习资源",
    "推荐学习资源",
    "开源项目参考",
    "跨语言参考",
    "关键提案与文献",
    "权威资料",
    "相关资料",
    "外部链接",
)

# 尾部站内导航类小节：只剥离外链行，保留站内交叉引用。
TAIL_STRIP_PREFIXES = (
    "延伸阅读",
    "相关文档",
    "further reading",
    "see also",
)

HEADING_RE = re.compile(r"^(#{2,4})\s+(.*?)\s*$")
FENCE_RE = re.compile(r"^(`{3,}|~{3,})")
NUMBER_PREFIX_RE = re.compile(
    r"^(?:\d+(?:[\.\、．]|\s*[-—–])?\s*"
    r"|\d+\.\d+\s*"
    r"|[A-Za-z]\.\d+\s*"
    r"|第\s*[一二三四五六七八九十百\d]+\s*[章篇节部分]?\s*"
    r"|附录\s*[A-Za-z0-9一二三四五六七八九十]+\s*[：:、]?\s*"
    r"|[一二三四五六七八九十]+[、\.]?\s*"
    r"|[（(]\d+[)）]\s*)+"
)

URL_RE = re.compile(r"https?://\S+")
# 早期批量转换遗留的"知识讲解与要点分析（原…）"标记行，可能被误插入代码块内；
# 无论是否在围栏中，整行删除（真实小节由小节删除逻辑处理）。
STRAY_MARKER_RE = re.compile(
    r"^#{1,6}\s*知识讲解与要点分析（原(?:习题|练习|思考题|题目|作业|练习题)[^）]*）"
)

# description 字段清理规则（仅当文件确实删除了小节时应用）。
# 按顺序执行，前面的规则先移除较长的组合短语，避免残留碎片。
DESC_RULES = [
    (re.compile(r"、常见错误对策与实战练习"), ""),
    (re.compile(r"常见错误对策与实战练习"), ""),
    (re.compile(r"并通过多道完整例题与实战练习帮助零基础"), "并帮助零基础"),
    (re.compile(r"并配完整例题与实战练习"), ""),
    (re.compile(r"与完整例题，"), "，"),
    (re.compile(r"完整例题，"), ""),
    (re.compile(r"、完整例题"), ""),
    (re.compile(r"完整例题、"), ""),
    (re.compile(r"完整例题"), ""),
    (re.compile(r"、实战练习"), ""),
    (re.compile(r"与实战练习"), ""),
    (re.compile(r"及实战练习"), ""),
    (re.compile(r"和实战练习"), ""),
    (re.compile(r"（含实战练习）"), ""),
    (re.compile(r"、四类习题与参考答案"), ""),
    (re.compile(r"、\d+\s*道习题含完整答案与[^。]*"), ""),
    (re.compile(r"、[^。，、]*风格习题"), ""),
    (re.compile(r"与[^。，、]*风格习题"), ""),
    (re.compile(r"[^。，、]*风格习题"), ""),
]


# ---------------------------------------------------------------------------
# 工具函数
# ---------------------------------------------------------------------------


def normalize_title(title: str) -> str:
    """剥离标题前的编号前缀（如 '8.'、'3.2'、'第 3 章'、'附录 E：'、'一、'）。"""
    prev = None
    while prev != title:
        prev = title
        title = NUMBER_PREFIX_RE.sub("", title, count=1).strip()
    return title


def is_deleted_section(title: str) -> bool:
    """判断标题命中的小节是否需要整体删除（例题/练习/习题等）。"""
    t = normalize_title(title)
    if any(k in t for k in DELETE_KEEP_CONTAINS):
        return False
    if any(k in t for k in DELETE_CONTAINS):
        return True
    for kw in DELETE_PREFIXES:
        if t.startswith(kw):
            if t in DELETE_EXCEPTIONS:
                return False
            return True
    for kw in DELETE_SUFFIXES:
        if t.endswith(kw):
            if t in DELETE_EXCEPTIONS:
                return False
            return True
    return False


def tail_kind(title: str) -> str:
    """返回尾部小节类型：'delete'（整段删除）、'strip'（剥离外链）、''（保留）。"""
    t = normalize_title(title).lower()
    for kw in TAIL_DELETE_PREFIXES:
        if t.startswith(kw):
            return "delete"
    # 英文资源小节仅整词匹配（"Reference 规范类型"这类正文标题不误删）
    for kw in ("references", "reference", "resources", "links"):
        if t == kw:
            return "delete"
    for kw in TAIL_STRIP_PREFIXES:
        if t.startswith(kw):
            return "strip"
    return ""


def split_sections(lines: list[str]) -> list[tuple[int, int, int, str]]:
    """按标题层级切分小节，返回 [(起点, 终点, 层级, 原始标题)]，终点不含。"""
    heads: list[tuple[int, int, str]] = []
    in_fence = False
    fence_char = ""
    fence_len = 0
    fm_end = 0  # frontmatter 结束行（跳过 YAML 内容）
    for i, line in enumerate(lines):
        s = line.strip()
        if i == 0 and s == "---":
            fm_end = None
            continue
        if fm_end is None:
            if s == "---":
                fm_end = i + 1
            continue
        fm = FENCE_RE.match(s)
        if fm:
            ch = fm.group(1)[0]
            n = len(fm.group(1))
            if not in_fence:
                # 开围栏：记录字符与长度（支持 4 反引号包裹 3 反引号的教学示例）
                fence_char, fence_len = ch, n
                in_fence = True
            elif (
                ch == fence_char
                and n >= fence_len
                and s[n:].strip() == ""
            ):
                # 闭围栏：同字符、不短于开围栏，且不得携带语言标注（```lang 不闭合）
                in_fence = False
            continue
        if in_fence:
            # 围栏内出现尾部/练习类标题时视为围栏提前闭合：
            # 修复历史批量处理把真实尾部误包裹进代码块的问题（全库仅 3 处）
            hm = HEADING_RE.match(line)
            if hm and (tail_kind(hm.group(2).strip()) or is_deleted_section(hm.group(2).strip())):
                in_fence = False
            else:
                continue
        m = HEADING_RE.match(line)
        if m:
            heads.append((i, len(m.group(1)), m.group(2).strip()))
    sections = []
    for j, (idx, level, title) in enumerate(heads):
        end = heads[j + 1][0] if j + 1 < len(heads) else len(lines)
        sections.append((idx, end, level, title))
    return sections


def collapse_blank_lines(lines: list[str]) -> list[str]:
    """把连续 3 行及以上的空行压缩为 2 行，并清理末尾多余空行。"""
    out: list[str] = []
    blank = 0
    for line in lines:
        if line.strip() == "":
            blank += 1
            if blank <= 2:
                out.append(line)
        else:
            blank = 0
            out.append(line)
    while out and out[-1].strip() == "":
        out.pop()
    return out


def process_file(path: Path, apply: bool) -> dict:
    """处理单个文档：删除小节/剥离外链/清理 related 与 description。"""
    result = {
        "file": str(path.relative_to(ROOT)),
        "sections": [],
        "urls": 0,
        "desc": False,
        "desc_diff": "",
        "related": [],
        "stripped_tails": [],
        "changed": False,
    }
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    # 0) 先清理代码块内的残留"知识讲解（原…）"标记行
    stray_count = 0
    kept_lines: list[str] = []
    for line in lines:
        if STRAY_MARKER_RE.match(line.strip()):
            stray_count += 1
            continue
        kept_lines.append(line)
    if stray_count:
        result["sections"].append(f"[残留标记×{stray_count}] 知识讲解与要点分析（原…）")
    lines = kept_lines
    fm_end = 0
    for i, line in enumerate(lines):
        if i == 0 and line.strip() == "---":
            for j in range(i + 1, len(lines)):
                if lines[j].strip() == "---":
                    fm_end = j + 1
                    break
            break

    # 1) 按小节删除规则收集操作：drop（整体删除）或 replace（剥离外链后回填）
    sections = split_sections(lines)
    ops: list[tuple[str, int, int, list[str] | None]] = []
    for idx, end, level, title in sections:
        kind = tail_kind(title)
        if kind == "delete":
            ops.append(("drop", idx, end, None))
            result["sections"].append(f"[尾部] {title[:40]}")
        elif is_deleted_section(title):
            ops.append(("drop", idx, end, None))
            result["sections"].append(title[:40])
        elif kind == "strip":
            # 2) 延伸阅读/相关文档：剥离外链与指向已删例题专册的引用
            kept: list[str] = []
            for line in lines[idx + 1:end]:
                s = line.strip()
                if not s:
                    continue
                if URL_RE.search(s) or "](http" in s:
                    result["urls"] += 1
                    continue
                if any(k in s for k in DELETED_TITLE_KEYS):
                    result["urls"] += 1
                    continue
                kept.append(line)
            if kept:
                ops.append(("replace", idx + 1, end, kept))
                result["stripped_tails"].append(title[:30])
            else:
                ops.append(("drop", idx, end, None))
                result["sections"].append(f"[空尾] {title[:30]}")

    # 3) 按原始行号顺序应用 drop/replace 操作（重叠时先到先得）
    ops.sort(key=lambda o: o[1])
    new_lines: list[str] = []
    cursor = 0
    dropped = 0
    for kind, a, b, kept in ops:
        if a < cursor:
            continue  # 与先前操作重叠，跳过
        new_lines.extend(lines[cursor:a])
        if kind == "drop":
            dropped += 1
        else:
            new_lines.extend(kept or [])
        cursor = b
    new_lines.extend(lines[cursor:])
    content_changed = bool(dropped or result["urls"] or stray_count)

    # 4) 清理 frontmatter 中指向已删例题专册的 related 条目
    if fm_end > 0:
        new_lines = clean_related(new_lines, fm_end, result)

    # 5) 清理因删除小节而过时的 description 描述
    if content_changed:
        new_lines = clean_description(new_lines, result)

    # 6) 只有确实发生内容变更时才写回；无变更的文件保持字节级原样
    if content_changed or result["related"] or result["desc"]:
        new_lines = collapse_blank_lines(new_lines)
        if new_lines:
            new_lines.append("")
        new_text = "\n".join(new_lines)
        result["changed"] = new_text != text
        if apply:
            if result["changed"]:
                # 文件可能被 Obsidian 等外部进程短暂占用，失败后重试
                for attempt in range(4):
                    try:
                        path.write_text(new_text, encoding="utf-8")
                        break
                    except OSError:
                        if attempt == 3:
                            raise
                        time.sleep(0.3 * (attempt + 1))
            else:
                result["changed"] = False
    return result


def clean_related(lines: list[str], fm_end: int, result: dict) -> list[str]:
    """删除 related 列表中指向已删例题专册的条目（保持 YAML 其他格式不变）。"""
    out = list(lines)
    i = 0
    while i < fm_end:
        if out[i].strip() == "related:":
            j = i + 1
            while j < fm_end and (
                out[j].strip().startswith("- ")
                or (out[j].strip() and not re.match(r"^[A-Za-z_][A-Za-z0-9_]*:", out[j].strip()))
            ):
                j += 1
            kept = []
            for k in range(i + 1, j):
                item = out[k].strip()[2:].strip().strip("'\"")
                if any(key in item for key in DELETED_TITLE_KEYS):
                    result["related"].append(item)
                else:
                    kept.append(out[k])
            out[i + 1:j] = kept
            break
        i += 1
    return out


def clean_description(lines: list[str], result: dict) -> list[str]:
    """按规则清理 description 字段中已失效的"例题/练习"表述。"""
    out = list(lines)
    for i, line in enumerate(out[:40]):
        m = re.match(r"^(description:\s*)(.*)$", line)
        if not m:
            continue
        val = m.group(2)
        new_val = val
        for pattern, repl in DESC_RULES:
            new_val = pattern.sub(repl, new_val)
        # 清理删除后留下的重复标点
        new_val = re.sub(r"[，,]{2,}", "，", new_val)
        new_val = re.sub(r"[。]{2,}", "。", new_val)
        new_val = re.sub(r"[，,。]\s*$", "。", new_val)
        if new_val != val:
            result["desc"] = True
            result["desc_diff"] = f"{val.strip()}  =>  {new_val.strip()}"
            out[i] = m.group(1) + new_val
        break
    return out


def main() -> None:
    apply = "--apply" in sys.argv
    mode = "APPLY" if apply else "DRY-RUN"
    print(f"== 全库清理：{mode} ==")

    deleted_files: list[str] = []
    if apply:
        for rel in DELETED_EXAMPLE_DOCS:
            p = ROOT / "cnt-content" / "full" / rel
            if p.exists():
                p.unlink()
                deleted_files.append(rel)
    else:
        deleted_files = [rel for rel in DELETED_EXAMPLE_DOCS if (ROOT / "cnt-content" / "full" / rel).exists()]

    stats = {
        "files": 0,
        "sections": 0,
        "urls": 0,
        "desc": 0,
        "related": 0,
        "tails": 0,
        "example_docs": len(deleted_files),
    }
    for root in CONTENT_ROOTS:
        if not root.exists():
            continue
        for f in sorted(root.rglob("*.md")):
            rel = f.relative_to(ROOT / "cnt-content").as_posix()
            if any(rel == d for d in DELETED_EXAMPLE_DOCS):
                continue
            r = process_file(f, apply)
            if not r["changed"]:
                continue
            stats["files"] += 1
            stats["sections"] += len(r["sections"])
            stats["urls"] += r["urls"]
            stats["desc"] += 1 if r["desc"] else 0
            stats["related"] += len(r["related"])
            stats["tails"] += len(r["stripped_tails"])
            if not apply:
                print(f"\n[{r['file']}]")
                for s in r["sections"][:6]:
                    print(f"  - 删节: {s}")
                if r["stripped_tails"]:
                    print(f"  - 剥链: {', '.join(r['stripped_tails'][:4])}")
                if r["related"]:
                    print(f"  - related 清理: {', '.join(r['related'][:3])}")
                if r["desc_diff"]:
                    print(f"  - desc: {r['desc_diff']}")

    print("\n== 统计 ==")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    if not apply:
        print("\n（干跑完成，加 --apply 实际写回）")


if __name__ == "__main__":
    main()
