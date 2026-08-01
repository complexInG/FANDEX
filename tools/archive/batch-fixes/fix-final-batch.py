# -*- coding: utf-8 -*-
"""修复最后一批 ASCII 图表。"""

from __future__ import annotations

import pathlib
import re

FULL = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full")
BOX = re.compile(
    "[\u250c\u2510\u2514\u2518\u251c\u2524\u252c\u2534\u253c\u2500\u2502"
    "\u2554\u2557\u255a\u255d\u2560\u2563\u2566\u2569\u256c\u2550\u2551"
    "\u256d\u256e\u256f\u2570]|\+[-=+]{2,}\+"
)


def replace_fence(path: pathlib.Path, keyword: str, new: str) -> bool:
    text = path.read_text(encoding="utf-8")
    idx = text.find(keyword)
    while idx >= 0:
        start = text.rfind("```", 0, idx)
        end = text.find("```", idx)
        if start >= 0 and end > start and BOX.search(text[start:end]):
            path.write_text(text[:start] + new + text[end + 3 :], encoding="utf-8")
            return True
        idx = text.find(keyword, idx + 1)
    return False


results = []

# 004 github Actions cron
p = FULL / "004-github/030-ActionsTrigger.md"
new = (
    "```mermaid\nflowchart LR\n"
    "    Min[分钟 0-59] --- Hour[小时 0-23] --- Day[日 1-31] --- Mon[月 1-12] --- Wk[星期 0-6 0=周日]\n"
    "```"
)
results.append(("gh-030-cron", replace_fence(p, "分钟 (0-59)", new)))

p = FULL / "004-github/035-ActionsArtifact.md"
new2 = (
    "```mermaid\nflowchart LR\n"
    "    JA[Job A 构建<br/>编译代码<br/>上传制品] -->|制品| JB[Job B 测试<br/>下载制品 运行测试<br/>上传报告] -->|报告| JC[Job C 部署<br/>下载制品 部署]\n"
    "```"
)
results.append(("gh-035-artifact", replace_fence(p, "Job A (构建)", new2)))

# 032 networking 机柜
p = FULL / "032-networking/003-NetworkWiringAndConstruction.md"
new3 = (
    "```mermaid\nflowchart TD\n"
    "    R[机柜标准 42U 1U=44.45mm<br/>典型布局 从上到下：<br/>42U 理线架 → 41U 交换机 → 40U 交换机 → 39U 理线架 → 38U 配线架 → 37U 配线架<br/>... → 4U UPS → 3U UPS → 2U PDU → 1U 理线架]\n"
    "```"
)
results.append(("net-003-rack", replace_fence(p, "机柜标准", new3)))

# 033 cybersecurity
p = FULL / "033-cybersecurity/003-BinarySecurityAndIncidentResponse.md"
new4 = (
    "```mermaid\nflowchart TD\n"
    "    E[ELF Header<br/>魔数 7f 45 4c 46<br/>文件类型/架构/入口] --> P[Program Headers 段加载信息]\n"
    "    P --> S[.text 代码段<br/>.data 数据段 已初始化全局变量<br/>.bss 未初始化全局变量<br/>.rodata 只读数据 常量/字符串<br/>.plt/.got 动态链接 延迟绑定表]\n"
    "    S --> H[Section Headers 节区信息]\n"
    "```"
)
results.append(("sec-003-elf", replace_fence(p, "ELF Header", new4)))

new5 = (
    "```mermaid\nflowchart TD\n"
    "    A[函数参数 高地址] --> R[返回地址 EIP<br/>覆盖目标] --> E[旧 EBP]\n"
    "    E --> L[局部变量 缓冲区<br/>溢出起点 低地址]\n"
    "```\n\n"
    "溢出方向：局部变量 → 旧 EBP → 返回地址 → 控制执行流"
)
results.append(("sec-003-stack", replace_fence(p, "函数参数", new5)))

new6 = (
    "```mermaid\nflowchart TD\n"
    "    C[Chunk 结构<br/>prev_size 前一个 chunk 大小<br/>size | A|M|P 本 chunk 大小+标志位<br/>fd 前向指针 空闲时有效<br/>bk 后向指针 空闲时有效<br/>数据区]\n"
    "```\n\n"
    "Fast Bins：≤ 0x80 字节（单链表 LIFO）；Small Bins：≤ 0x400 字节（双链表 FIFO）；Large Bins：> 0x400 字节（按大小排序）；Unsorted Bin：释放后先进入，分配时再分类"
)
results.append(("sec-003-chunk", replace_fence(p, "Chunk 结构", new6)))

# 036 testing
p = FULL / "036-software-testing/004-SecurityAndMobileTest.md"
new7 = (
    "```mermaid\nflowchart TD\n"
    "    E[E2E 测试<br/>少量、慢速、高成本] --> I[集成/接口测试<br/>适量、中速、中成本]\n"
    "    I --> U[单元测试<br/>大量、快速、低成本]\n"
    "```"
)
results.append(("test-004-pyramid", replace_fence(p, "E2E 测试", new7)))

p = FULL / "036-software-testing/005-TestConceptPrinciple.md"
new8 = (
    "```mermaid\nflowchart LR\n"
    "    A[需求分析] <--> B[验收测试]\n"
    "    C[系统设计] <--> D[系统测试]\n"
    "    E[详细设计] <--> F[集成测试]\n"
    "    G[编码] <--> H[单元测试]\n"
    "    A --> C --> E --> G\n"
    "    B --> D --> F --> H\n"
    "```"
)
results.append(("test-005-v", replace_fence(p, "需求分析", new8)))

p = FULL / "036-software-testing/006-TestLevels.md"
new9 = (
    "```mermaid\nflowchart TD\n"
    "    E[E2E 测试<br/>少量、慢、贵] --> I[集成测试<br/>适量、中速]\n"
    "    I --> U[单元测试<br/>大量、快、便宜]\n"
    "```"
)
results.append(("test-006-levels", replace_fence(p, "E2E 测试", new9)))

# 042 machine learning
p = FULL / "042-machine-learning/001-MachineLearningOverview.md"
new10 = (
    "```mermaid\ntimeline\n"
    "    title 机器学习发展时间线\n"
    "    1950s: 感知机（Rosenblatt）\n"
    "    1960s: 线性判别分析、K近邻\n"
    "    1970s: AI 寒冬（感知机局限性暴露）\n"
    "    1980s: 决策树（ID3）、BP 算法\n"
    "    1990s: SVM、随机森林、Boosting\n"
    "    2000s: 集成学习、图模型\n"
    "    2010s: 深度学习爆发（CNN、RNN、GAN）\n"
    "    2020s: 大模型时代（Transformer、GPT、LLaMA）\n"
    "```"
)
results.append(("ml-001-timeline", replace_fence(p, "感知机（Rosenblatt）", new10)))

# 006 分类树
new11 = (
    "```mermaid\nflowchart LR\n"
    "    A[A] B[B] C[C] D[D] E[E]<br/>"
    "```"
)
results.append(("ml-006-tree", replace_fence(p, "A   B   C", new11)))

p = FULL / "042-machine-learning/008-ModelEvaluationAndSelection.md"
new12 = (
    "```mermaid\nflowchart LR\n"
    "    A[ROC 曲线<br/>TPR 1.0 ─ 0.0<br/>FPR 0.0 ─ 1.0<br/>对角线为随机分类器]\n"
    "```"
)
results.append(("ml-008-roc", replace_fence(p, "TPR", new12)))

new13 = (
    "```mermaid\nflowchart TD\n"
    "    A[训练误差 随数据量增加而上升<br/>验证误差 随数据量增加而下降]\n"
    "    A --> B[高偏差 欠拟合<br/>训练误差和验证误差都高且接近<br/>→ 增加特征/更复杂模型]\n"
    "    A --> C[高方差 过拟合<br/>训练误差低，验证误差高<br/>→ 增加数据/正则化]\n"
    "```"
)
results.append(("ml-008-bias", replace_fence(p, "训练误差", new13)))

# 044 ai-engineering 分类树
p = FULL / "044-ai-engineering/015-ClassAlgorithm.md"
new14 = (
    "```mermaid\nflowchart LR\n"
    "    A[A] B[B] C[C] D[D] E[E]\n"
    "```"
)
results.append(("ai-015-tree", replace_fence(p, "A   B   C", new14)))

# 045 computer vision
p = FULL / "045-computer-vision/018-ImageBasicsPixelChannelColorSpace.md"
new15 = (
    "```mermaid\nflowchart LR\n"
    "    S[连续场景 无限细节<br/>光线] --> G[传感器网格 H x W 探测器] --> D[数字图像 H x W 整数<br/>210 198 180 155 120<br/>205 195 178 152 118<br/>200 190 175 150 115<br/>195 185 170 148 112<br/>188 180 165 145 108]\n"
    "```"
)
results.append(("cv-018-sampling", replace_fence(p, "连续场景", new15)))

# 051 data analysis 星型模型
p = FULL / "051-data-analysis/009-DataAnalysisAdvancedPractice.md"
new16 = (
    "```mermaid\nflowchart TD\n"
    "    T[时间维度] --- F[事实表]\n"
    "    P[产品维度] --- F\n"
    "    G[地域维度] --- F\n"
    "    C[客户维度] --- F\n"
    "```"
)
results.append(("da-009-star", replace_fence(p, "时间维度", new16)))

for name, ok in results:
    print(f"{name}: {ok}")
