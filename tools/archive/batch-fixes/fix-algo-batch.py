# -*- coding: utf-8 -*-
"""修复 023-algorithm 下 ASCII 图表。"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\023-algorithm")
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

# 001 算法分析层次
p = ROOT / "001-MIT6006IntroductionToAlgorithms.md"
new = (
    "```mermaid\nflowchart TD\n"
    "    A[算法分析]\n"
    "    A --> T[时间分析<br/>最坏/平均/最好/摊还/期望/概率]\n"
    "    A --> S[空间分析<br/>辅助空间/总空间]\n"
    "    A --> C[正确性分析<br/>不变式归纳法/前后置条件]\n"
    "    A --> O[最优性分析<br/>下界证明 Ω/上界证明 O]\n"
    "```"
)
results.append(("001-analysis", replace_fence(p, "算法分析层次模型", new)))

# 002 排序分类树（两处）
p = ROOT / "002-SortAlgorithm.md"
new2 = (
    "```mermaid\nflowchart TD\n"
    "    S[排序]\n"
    "    S --> I[内部排序<br/>比较排序 Ω(n log n)<br/>插入类：插入/希尔<br/>交换类：冒泡/快排<br/>堆排选择类/归并归并类]\n"
    "    S --> E[外部排序<br/>多路归并]\n"
    "    S --> D[分布排序<br/>计数排序 O(n+k)/基数排序 O(d(n+k))/桶排序 O(n+k) 平均]\n"
    "    S --> M[混合排序<br/>内省排序 Musser 1997/Timsort Peters 2002]\n"
    "```"
)
results.append(("002-sorttree", replace_fence(p, "排序算法分类树", new2)))

new3 = (
    "```mermaid\nflowchart TD\n"
    "    S[排序]\n"
    "    S --> C[比较排序 Ω(n log n)<br/>插入类：插入/希尔<br/>交换类：冒泡/快排/堆排/归并]\n"
    "    S --> N[非比较排序 O(n)<br/>计数/基数 LSD MSD/桶]\n"
    "    S --> E[外部排序 O(n log n / M)<br/>多路归并/替换选择/Fibonacci/多步归并]\n"
    "    S --> M[混合排序 工业级<br/>introsort Musser 1997 堆排+快排+插入排序<br/>Timsort Peters 2002 自然 run+二分插入+归并栈]\n"
    "```"
)
results.append(("002-knowledge", replace_fence(p, "排序算法知识体系", new3)))

# 003 栈与队列
p = ROOT / "003-ConcurrencyInGoToolsAndTechniquesForDevelopers.md"
new4 = (
    "```mermaid\nflowchart LR\n"
    "    subgraph Stack[栈 LIFO push/pop]\n"
        "        S1[5 top] S2[3] S3[1] S4[7 bottom]\n"
    "    end\n"
    "    subgraph Queue[队列 FIFO enqueue/dequeue]\n"
    "        Q[7 | 1 | 3 | 5<br/>rear → front]\n"
    "    end\n"
    "```"
)
results.append(("003-stackq", replace_fence(p, "栈（LIFO）", new4)))

new5 = (
    "```mermaid\nflowchart LR\n"
    "    Q1[入队 7,1,3,5 后出队 7,1：空 空 3 5 空 空<br/>front ↑ rear ↑]\n"
    "    Q2[继续入队 9,8：空 空 3 5 9 8<br/>front ↑ rear 越界 前方空间无法使用]\n"
    "    Q1 --> Q2\n"
    "```"
)
results.append(("003-ring", replace_fence(p, "入队 7, 1, 3, 5", new5)))

new6 = (
    "```mermaid\nflowchart LR\n"
    "    D[双端队列<br/>左端 addFirst/removeFirst/getFirst<br/>5 | 3 | 1 | 7 | 9<br/>右端 addLast/removeLast/getLast]\n"
    "```"
)
results.append(("003-deque", replace_fence(p, "左端操作", new6)))

# 004 搜索分类树（两处）
p = ROOT / "004-SearchAlgorithm.md"
new7 = (
    "```mermaid\nflowchart TD\n"
    "    S[搜索]\n"
    "    S --> ST[静态查找 数组/链表<br/>线性 O(n)/二分 O(log n)/哈希 O(1)]\n"
    "    S --> U[无信息搜索 状态空间图<br/>BFS O(V+E)/DFS O(V+E)/UCS O(E log V)/IDDFS O(b^d)]\n"
    "    S --> I[有信息搜索 状态空间图+启发式<br/>A* O(b^d)/IDA* O(b^d)/贪婪 GBFS/WIDA*]\n"
    "    S --> G[对抗搜索 博弈树<br/>Minimax O(b^d)/MCTS/Alpha-Beta O(b^(d/2))]\n"
    "```"
)
results.append(("004-searchtree", replace_fence(p, "搜索算法分类树", new7)))

new8 = (
    "```mermaid\nflowchart TD\n"
    "    S[搜索算法]\n"
    "    S --> ST[静态查找 数组/链表<br/>线性 O(n)/二分 O(log n)/哈希 O(1)]\n"
    "    S --> U[无信息搜索 状态空间图<br/>BFS O(V+E)/DFS O(V+E)/双向BFS O(b^(d/2))/IDDFS O(b^d) O(d)]\n"
    "    S --> I[有信息搜索 状态空间图+启发式<br/>A* O(b^d)/IDA* O(b^d)/贪婪 GBFS/WIDA*]\n"
    "    S --> G[对抗搜索 博弈树<br/>Minimax O(b^d)/MCTS/Alpha-Beta O(b^(d/2))]\n"
    "```"
)
results.append(("004-panorama", replace_fence(p, "搜索算法全景图", new8)))

# 009 分治
p = ROOT / "009-GaussAndTheHistoryOfTheFastFourierTransform.md"
new9 = (
    "```mermaid\nflowchart TD\n"
    "    D[分治算法]\n"
    "    D --> S[排序分治<br/>归并排序 von Neumann 1945/快排 Hoare 1961]\n"
    "    D --> A[代数分治<br/>Karatsuba 1963 O(n^1.585)/Strassen 1969 O(n^2.807)]\n"
    "    D --> G[几何分治<br/>最近点对 1976/最大子数组 1976 O(n log n)]\n"
    "    D --> F[信号分治<br/>FFT 1965 O(n log n)/数论变换 NTT]\n"
    "```"
)
results.append(("009-divide", replace_fence(p, "分治算法分类树", new9)))

new10 = (
    "```mermaid\nflowchart TD\n"
    "    P[分治三步范式 Divide-Conquer-Combine]\n"
    "    P --> M[主定理分析 Bentley 1980<br/>情况1/2/3 T=Θ(n^logba)<br/>递归树归约]\n"
    "    P --> A[代数恒等式优化<br/>Karatsuba O(n^1.585)/Strassen O(n^2.807)]\n"
    "    P --> G[几何分治 Bentley-Shamos<br/>最近点对/最大子数组 O(n log n) 势能摊还]\n"
    "    P --> F[信号分治 Cooley-Tukey<br/>FFT/IFFT O(n log n) 蝶形运算]\n"
    "```"
)
results.append(("009-knowledge", replace_fence(p, "分治算法知识图谱", new10)))

# 010 贪心
p = ROOT / "010-GreedyAlgorithm.md"
new11 = (
    "```mermaid\nflowchart TD\n"
    "    G[贪心算法]\n"
    "    G --> GT[图论贪心<br/>Kruskal 1956/Prim 1957]\n"
    "    G --> C[编码压缩<br/>Huffman 1952/Shannon 1948]\n"
    "    G --> S[调度问题<br/>活动选择/区间调度 O(n log n)]\n"
    "    G --> K[背包问题<br/>分数背包/任务调度 O(n log n)]\n"
    "```"
)
results.append(("010-greedy", replace_fence(p, "贪心算法分类树", new11)))

new12 = (
    "```mermaid\nflowchart TD\n"
    "    G[贪心算法]\n"
    "    G --> GT[图论贪心<br/>Kruskal 1956/Prim 1957 → MST<br/>Dijkstra 1959 O((V+E)logV) → Google Maps]\n"
    "    G --> C[编码压缩<br/>Huffman 1952/Shannon 1948 → DEFLATE/JPEG]\n"
    "    G --> S[调度问题<br/>活动选择 O(n log n)/区间调度 Dilworth]\n"
    "    G --> K[背包问题<br/>分数背包/任务调度 SJF]\n"
    "```"
)
results.append(("010-panorama", replace_fence(p, "贪心算法全景图", new12)))

# 011 回溯
p = ROOT / "011-NQueensBenchmarkBitManipulationApproach.md"
new13 = (
    "```mermaid\nflowchart TD\n"
    "    R[递归与回溯]\n"
    "    R --> L[线性递归<br/>阶乘/斐波那契数列]\n"
    "    R --> T[树形递归<br/>分治递归 归并/快排/树遍历 DFS/BST]\n"
    "    R --> B[回溯算法<br/>子集/排列/组合/数独/N皇后]\n"
    "    R --> BB[分支限界<br/>0-1背包 ILP/TSP VRP]\n"
    "```"
)
results.append(("011-backtrack", replace_fence(p, "递归与回溯算法分类树", new13)))

new14 = (
    "```mermaid\nflowchart TD\n"
    "    R[递归与回溯]\n"
    "    R --> RB[递归基础<br/>基线条件/递归条件<br/>阶乘/斐波那契/记忆化]\n"
    "    R --> B[回溯算法<br/>通用模板 选择-递归-撤销<br/>剪枝 排序/边界/条件/记忆化/位运算<br/>子集/排列/组合/分割/括号/搜索/N皇后/数独/约束传播]\n"
    "    R --> BB[分支限界<br/>界限/LP松弛/BFS/最佳优先<br/>0-1背包/TSP/ILP/精确覆盖 Algorithm X/Dancing Links]\n"
    "```"
)
results.append(("011-panorama", replace_fence(p, "递归与回溯", new14)))

# 014 数组
p = ROOT / "014-NumPyArraysABeginnerGuideCSRCSCSparseMatrixFormats.md"
new15 = (
    "```mermaid\nflowchart LR\n"
    "    S[静态数组 size=capacity=5<br/>10 20 30 40 50<br/>内存连续，索引 0-4]\n"
    "    D[动态数组 size=4 capacity=8<br/>10 20 30 40 空 空 空 空<br/>内存连续，预留空间 索引 0-3 size，可继续追加]\n"
    "```"
)
results.append(("014-arrays", replace_fence(p, "静态数组", new15)))

new16 = (
    "```mermaid\nflowchart LR\n"
    "    A[内存地址 base base+4 base+8 base+12 base+16<br/>索引 0 1 2 3 4<br/>元素 10 20 30 40 50<br/>base = 起始地址，size = 4 字节 int]\n"
    "```\n\n"
    "地址公式：address(A[i]) = base + i × 4"
)
results.append(("014-address", replace_fence(p, "内存地址", new16)))

new17 = (
    "```mermaid\nflowchart LR\n"
    "    B[扩容前 capacity=4 size=4<br/>10 20 30 40<br/>size=capacity 触发扩容]\n"
    "    B --> N[扩容中 分配新数组+复制<br/>10 20 30 40 → 10 20 30 40 空 空 空 空<br/>新数组，新 capacity=8，旧数组释放]\n"
    "    N --> A[扩容后追加 50<br/>10 20 30 40 50 空 空 空<br/>size=5 capacity=8]\n"
    "```"
)
results.append(("014-grow", replace_fence(p, "扩容前", new17)))

new18 = (
    "```mermaid\nflowchart LR\n"
    "    J0[jagged[0] → [1, 2, 3]]\n"
    "    J1[jagged[1] → [4, 5]]\n"
    "    J2[jagged[2] → [6, 7, 8, 9]]\n"
    "```"
)
results.append(("014-jagged", replace_fence(p, "jagged[0]", new18)))

new19 = (
    "```mermaid\nflowchart LR\n"
    "    Z[ziplist 内存布局<br/>zlbytes 4字节 / zltail 4字节 / zllen 2字节 / entry 变长 / ... / zlend 1字节]\n"
    "    E[每个 entry<br/>prev_entry_len 1或5字节 / encoding 1+字节 / content 变长]\n"
    "```"
)
results.append(("014-ziplist", replace_fence(p, "ziplist 内存布局", new19)))

# 017 bisect 查找树
p = ROOT / "017-CPythonBisectPyArrayBisectionAlgorithmImplementation.md"
new20 = (
    "```mermaid\nflowchart TD\n"
    "    F[查找]\n"
    "    F --> SEQ[顺序查找 O(n)<br/>哨兵优化 O(n)]\n"
    "    F --> CMP[比较查找 O(log n)<br/>二分 O(log n)/插值 O(log log n)/斐波那契 O(log n)<br/>树形：BST O(log n) 平均、AVL O(log n) 最坏、红黑树 O(log n) 最坏、B树 O(log_d n)、跳表 O(log n) 期望]\n"
    "    F --> NUM[数字查找 O(L)<br/>Trie 树/Radix Tree]\n"
    "    F --> HASH[哈希查找 O(1) 平均<br/>链地址法/开放寻址 线性探针/二次探针/双重哈希]\n"
    "```"
)
results.append(("017-search", replace_fence(p, "查找算法分类树", new20)))

# 018 ICPC
p = ROOT / "018-InternationalCollegiateProgrammingContestICPC.md"
new21 = (
    "```mermaid\nflowchart TD\n"
    "    T[刷题训练]\n"
    "    T --> A[学术训练<br/>形式化建模/不变式证明/算法范式迁移]\n"
    "    T --> E[工程准备<br/>面试编码/白板沟通/边界处理]\n"
    "    T --> C[竞赛训练<br/>ICPC/Codeforces/周赛/AtCoder ABC-ARC]\n"
    "    A --> AC[复杂度分析/摊还]\n"
    "    E --> ED[工程映射/系统设计/性能调优]\n"
    "```"
)
results.append(("018-leetcode", replace_fence(p, "LeetCode 刷题价值模型", new21)))

new22 = (
    "```mermaid\nflowchart TD\n"
    "    S1[Step 1 审题 2-3 min<br/>复述题目/确认输入输出/询问约束/讨论边界]\n"
    "    S2[Step 2 建模 5-8 min<br/>先说暴力解/分析瓶颈/提出优化思路/确认方向]\n"
    "    S3[Step 3 编码 15-20 min<br/>先写框架/再填细节/变量命名清晰/适当注释]\n"
    "    S4[Step 4 验证 5-10 min<br/>手动模拟/检查边界/分析复杂度/讨论优化扩展]\n"
    "    S1 --> S2 --> S3 --> S4\n"
    "```"
)
results.append(("018-fourstep", replace_fence(p, "四步解题法", new22)))

# 022 LevelDB 跳表
p = ROOT / "022-LevelDBREADMEMemTableImplementation.md"
new23 = (
    "```mermaid\nflowchart LR\n"
    "    L4[Level 4: HEAD - 50 - NIL]\n"
    "    L3[Level 3: HEAD - 25 - 50 - NIL]\n"
    "    L2[Level 2: HEAD - 13 - 25 - 38 - 50 - NIL]\n"
    "    L1[Level 1: HEAD - 7 13 25 19 38 44 50 - NIL]\n"
    "    L0[Level 0: HEAD - 7 13 19 25 31 38 44 50 56 - NIL]\n"
    "```"
)
results.append(("022-skiplist", replace_fence(p, "Level 4", new23)))

# 025 状态压缩 DP
p = ROOT / "025-LeetCodeBitmaskDPProblemsCollection.md"
new24 = (
    "```mermaid\nflowchart TD\n"
    "    S[状态压缩 DP]\n"
    "    S --> E[集合编码<br/>二进制位串/集合运算/popcount]\n"
    "    S --> T[状态转移<br/>枚举子集/超集枚举/增量转移]\n"
    "    S --> O[优化技巧<br/>滚动数组/预处理/位运算/低比特技巧/__builtin/哈希映射]\n"
    "    S --> C[经典问题<br/>TSP/N皇后/子集和/数独/棋盘覆盖/排列]\n"
    "```"
)
results.append(("025-bitdp", replace_fence(p, "状态压缩 DP 层次模型", new24)))

# 027 MST
p = ROOT / "027-BoostGraphLibrary1860KruskalMinimumSpanningTree.md"
new25 = (
    "```mermaid\nflowchart TD\n"
    "    M[最小生成树 MST]\n"
    "    M --> K[Kruskal 1956<br/>边排序贪心 O(E log E)<br/>稀疏图优/并查集]\n"
    "    M --> P[Prim 1957<br/>点扩展贪心 O(V²)/O(E log V)<br/>稠密图优/优先队列]\n"
    "    M --> B[Borůvka 1926<br/>分治合并 O(E log V)<br/>并行友好/分量合并]\n"
    "    P --> J[Jarník 1930<br/>Prim 前身]\n"
    "    P --> KKT[Karger-Klein-Tarjan 1995<br/>随机化线性 O(E) 期望]\n"
    "```"
)
results.append(("027-mst", replace_fence(p, "最小生成树算法家族", new25)))

# 029 P vs NP
p = ROOT / "029-MillenniumPrizeProblemsPVersusNP.md"
new26 = (
    "```mermaid\nflowchart TD\n"
    "    T[算法理论]\n"
    "    T --> C[可计算性理论<br/>图灵机/λ-演算/Church-Turing/停机问题/Rice 定理]\n"
    "    T --> X[计算复杂性理论<br/>P/NP/NPC/PSPACE/EXPTIME/BPP-QC/PCP 定理/归约/不可近似性]\n"
    "    T --> D[算法设计与分析<br/>摊还分析/竞争分析/聚合-核-势能/数据流/随机化/近似算法/启发式]\n"
    "```"
)
results.append(("029-theory", replace_fence(p, "算法理论层次模型", new26)))

new27 = (
    "```mermaid\nflowchart TD\n"
    "    EXP[EXPTIME EXP]\n"
    "    PSP[PSPACE]\n"
    "    NP[NP<br/>NPC 内部]\n"
    "    P[P]\n"
    "    NL[NL ⊆ P<br/>L 内部]\n"
    "    EXP --> PSP --> NP --> P --> NL\n"
    "```\n\n"
    "已知：L ⊆ NL ⊆ P ⊆ NP ⊆ PSPACE ⊆ EXPTIME；L ⊊ PSPACE，P ⊊ EXPTIME（层次定理）；开放：L vs P，P vs NP，NP vs PSPACE"
)
results.append(("029-hierarchy", replace_fence(p, "EXPTIME", new27)))

for name, ok in results:
    print(f"{name}: {ok}")
