# -*- coding: utf-8 -*-
"""修复 037-software-engineering 及剩余 025-c 图表。"""

from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\037-software-engineering")
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

# 025-c 残留：指针数组
p = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\025-c\045-DoublePointerPointerArray.md")
new = (
    "```mermaid\nflowchart LR\n"
    "    A[0x1000 arr[0]=1 0x1004 arr[1]=2 0x1008 arr[2]=3 0x100c arr[3]=4 0x1010 arr[4]=5]\n"
    "    P[ptr 0x2000 → 0x1000 指向整个 arr 数组]\n"
    "    P --- A\n"
    "```"
)
results.append(("c-arrptr2", replace_fence(p, "0x2000        0x1000", new)))

# 002 Agile 看板
p = ROOT / "002-AgileDevelopment.md"
new2 = (
    "```mermaid\nflowchart LR\n"
    "    B[Backlog<br/>T-12 T-15 T-18] --> T[To Do 3<br/>T-05 T-07 T-06]\n"
    "    T --> IP[In Progress 2<br/>T-03 T-04 WIP Limit 2]\n"
    "    IP --> R[Review 2<br/>T-01 T-02]\n"
    "    R --> D[Done<br/>T-08 T-09 T-10]\n"
    "```"
)
results.append(("002-kanban", replace_fence(p, "Backlog", new2)))

# 002 燃尽图
new3 = (
    "```mermaid\nflowchart LR\n"
    "    A[剩余故事点 100] --> B[75] --> C[50] --> D[25] --> E[0<br/>→ Sprint 天数]\n"
    "    I[理想线 ╲]<br/>A2[实际线 ╲]\n"
    "```"
)
results.append(("002-burndown", replace_fence(p, "剩余故事点", new3)))

# 004 UML
p = ROOT / "004-UMLGraphDetailed.md"
new4 = (
    "```mermaid\nclassDiagram\n"
    "    class ClassName {\n"
    "        -privateAttr: Type\n"
    "        #protectedAttr: Type\n"
    "        +publicAttr: Type\n"
    "        +publicMethod(): Ret\n"
    "        -privateMethod()\n"
    "    }\n"
    "```"
)
results.append(("004-class", replace_fence(p, "ClassName", new4)))

new5 = (
    "```mermaid\nflowchart TD\n"
    "    S([起始节点]) --> A1[活动1]\n"
    "    A1 --> D{决策}\n"
    "    D --> A2[活动2]\n"
    "    D --> A3[活动3]\n"
    "    A2 --> M{合并}\n"
    "    A3 --> M\n"
    "    M --> E([终止节点])\n"
    "```"
)
results.append(("004-activity", replace_fence(p, "起始节点", new5)))

new6 = (
    "```mermaid\nsequenceDiagram\n"
    "    participant C as 客户端\n"
    "    participant S as 服务端\n"
    "    participant D as 数据库\n"
    "    C->>S: 提交订单\n"
    "    S->>S: 验证订单\n"
    "    S->>D: 保存数据\n"
    "    D-->>S: 返回结果\n"
    "    S-->>C: 显示确认\n"
    "```"
)
results.append(("004-seq", replace_fence(p, "客户端   │", new6)))

new7 = (
    "```mermaid\nstateDiagram-v2\n"
    "    [*] --> 待下单\n"
    "    待下单 --> 待支付: 下单\n"
    "    待支付 --> 已支付: 支付\n"
    "    待支付 --> 已取消: 取消订单\n"
    "    已支付 --> 已发货: 发货\n"
    "    已发货 --> 已完成: 确认收货\n"
    "```"
)
results.append(("004-state", replace_fence(p, "初始状态", new7)))

new8 = (
    "```mermaid\nflowchart TD\n"
    "    W[Web前端] --> G[API网关]\n"
    "    G --> U[用户服务]\n"
    "    G --> O[订单服务]\n"
    "    G --> P[支付服务]\n"
    "```"
)
results.append(("004-deploy", replace_fence(p, "Web前端", new8)))

new9 = (
    "```mermaid\nflowchart TD\n"
    "    W[Web服务器<br/>Nginx] --> A[应用服务器<br/>Node.js]\n"
    "    A --> D[数据库服务器<br/>MySQL]\n"
    "```"
)
results.append(("004-3tier", replace_fence(p, "Web服务器", new9)))

# 005 设计模式
p = ROOT / "005-DesignPatternDetailed.md"
new10 = (
    "```mermaid\nclassDiagram\n"
    "    class Product\n"
    "    class ConcreteProduct\n"
    "    class Creator {\n"
    "        +FactoryMethod()\n"
    "    }\n"
    "    class ConcreteCreator {\n"
    "        +FactoryMethod()\n"
    "    }\n"
    "    Product <|-- ConcreteProduct\n"
    "    Creator <|-- ConcreteCreator\n"
    "    ConcreteCreator --> ConcreteProduct\n"
    "```"
)
results.append(("005-factory", replace_fence(p, "ConcreteProduct", new10)))

new11 = (
    "```mermaid\nclassDiagram\n"
    "    class Component\n"
    "    class ConcreteComponent\n"
    "    class Decorator\n"
    "    class ConcreteDecorator\n"
    "    Component <|-- ConcreteComponent\n"
    "    Component <|-- Decorator\n"
    "    Decorator <|-- ConcreteDecorator\n"
    "```"
)
results.append(("005-decorator", replace_fence(p, "ConcreteDecorator", new11)))

new12 = (
    "```mermaid\nflowchart TD\n"
    "    S[Subject<br/>attach(observer)<br/>detach(observer)<br/>notify()]\n"
    "    S -->|Observer.update()| O1[ConcreteObserver1]\n"
    "    S -->|Observer.update()| O2[ConcreteObserver2]\n"
    "```"
)
results.append(("005-observer", replace_fence(p, "attach(observer)", new12)))

# 007 测试金字塔
p = ROOT / "007-SoftwareTestMethod.md"
new13 = (
    "```mermaid\nflowchart TD\n"
    "    E[E2E 测试<br/>少量，慢，脆弱] --> I[集成测试<br/>适量，中速]\n"
    "    I --> U[单元测试<br/>大量，快速，稳定]\n"
    "```"
)
results.append(("007-pyramid", replace_fence(p, "E2E测试", new13)))

# 010 蓝绿
p = ROOT / "010-DevOpsCICDIntegration.md"
new14 = (
    "```mermaid\nflowchart LR\n"
    "    B[蓝环境 v1.0<br/>← 流量] -->|切换流量| G[绿环境 v2.0<br/>← 流量]\n"
    "```"
)
results.append(("010-bluegreen", replace_fence(p, "蓝环境", new14)))

for name, ok in results:
    print(f"{name}: {ok}")
