# -*- coding: utf-8 -*-
"""将 full 缺失的 mobile 文档提升进 full（promote 类）。

步骤：
1. 为每个 promote 文档生成 full 文件名：<max+1>-<PascalCase>.md
2. 补全 frontmatter（title/module/category/description/author/order 等）
3. 复制到 full 对应模块
4. 更新 _doc-id-map.json 与 _id-registry.json（分配 D 编号）
5. 更新模块内 order 不冲突
"""

from __future__ import annotations

import json
import pathlib
import re
import sys
from datetime import datetime, timezone

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
FULL = ROOT / "cnt-content" / "full"
MOBILE = ROOT / "cnt-content" / "mobile"
MAP = ROOT / "tools" / "mobile-full-map.json"


def pascal(name: str) -> str:
    n = re.sub(r"^\d{3}-", "", name)
    n = re.sub(r"\.md$", "", n)
    n = re.sub(r"([a-z])([A-Z])", r"\1 \2", n)
    words = re.split(r"[^A-Za-z0-9]+", n)
    return "".join(w[:1].upper() + w[1:] for w in words if w)


def module_category(mod: str) -> str:
    cats = {
        "getting-started": "Getting Started",
        "markdown": "Markdown Basics",
        "git": "Git Basics",
        "github": "GitHub",
        "english": "English",
        "html5": "HTML5",
        "css": "CSS",
        "javascript": "JavaScript",
        "typescript": "TypeScript",
        "vue3": "Vue3",
        "react": "React",
        "svg": "SVG",
        "java": "Java",
        "kotlin": "Kotlin",
        "csharp": "C#",
        "go": "Go",
        "lua": "Lua",
        "harmonyos": "HarmonyOS",
        "sql": "SQL",
        "mysql": "MySQL",
        "postgresql": "PostgreSQL",
        "redis": "Redis",
        "algorithm": "Algorithm",
        "cs-fundamentals": "CS Fundamentals",
        "c": "C",
        "cpp": "C++",
        "calculus": "Calculus",
        "discrete-math": "Discrete Math",
        "linear-algebra": "Linear Algebra",
        "probability-statistics": "Probability & Statistics",
        "devops": "DevOps",
        "networking": "Networking",
        "cybersecurity": "Cybersecurity",
        "cloud-computing": "Cloud Computing",
        "iot": "IoT",
        "software-testing": "Software Testing",
        "software-engineering": "Software Engineering",
        "software-architecture": "Software Architecture",
        "engineering-practices": "Engineering Practices",
        "python": "Python",
        "data-analysis": "Data Analysis",
        "big-data": "Big Data",
    }
    return cats.get(mod, mod)


def next_doc_number(mod_dir: pathlib.Path) -> int:
    nums = []
    for f in mod_dir.glob("*.md"):
        m = re.match(r"^(\d{3})-", f.name)
        if m:
            nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1


def build_frontmatter(title: str, module: str, category: str, order: int) -> str:
    return (
        "---\n"
        f"order: {order}\n"
        f"title: {title}\n"
        f"module: {module}\n"
        f"category: '{category}'\n"
        "difficulty: beginner\n"
        f"description: {title} 的完整教学讲解。\n"
        "author: fanquanpp\n"
        "updated: '2026-08-01'\n"
        "related: []\n"
        "prerequisites: []\n"
        "---\n"
    )


def main() -> None:
    plan = json.loads(MAP.read_text(encoding="utf-8"))
    promote = [p for p in plan if p["status"] == "promote"]

    # 读取 ID 注册表与映射
    reg_path = FULL / "_id-registry.json"
    map_path = FULL / "_doc-id-map.json"
    reg = json.loads(reg_path.read_text(encoding="utf-8"))
    idmap = json.loads(map_path.read_text(encoding="utf-8"))
    next_seq = reg.get("next_doc_sequence", 2316)

    # module_id 查询表
    mod_id = {m["english_short"]: m["module_id"] for m in reg["modules"]}

    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    created = []
    for p in promote:
        mpath = MOBILE / p["mobile"]
        mod = p["module"]
        mod_dir = FULL / mod
        if not mod_dir.exists():
            print(f"跳过（模块不存在）: {p['mobile']}")
            continue
        new_num = next_doc_number(mod_dir)
        new_name = f"{new_num:03d}-{pascal(mpath.name)}.md"
        new_rel = f"{mod}/{new_name}"
        if (FULL / new_rel).exists():
            print(f"跳过（已存在）: {new_rel}")
            continue

        body = mpath.read_text(encoding="utf-8")
        # 移除已有 frontmatter（若有）
        body = re.sub(r"^---\r?\n.*?\r?\n---\r?\n?", "", body, flags=re.S)
        # 从正文提取标题（第一个 # 或粗体行）
        title_m = re.search(r"^#\s+(.+)$", body, re.M)
        title = title_m.group(1).strip() if title_m else pascal(mpath.name)
        fm = build_frontmatter(title, mod, module_category(mod), new_num * 10)
        (FULL / new_rel).write_text(fm + body.lstrip("\n"), encoding="utf-8")

        # 注册 ID
        doc_id = f"D{next_seq:05d}"
        next_seq += 1
        reg["docs"].append(
            {
                "doc_id": doc_id,
                "module_id": mod_id.get(mod, "M000"),
                "sequence": next_seq - 1,
                "doc_order": new_num,
                "english_name": pascal(mpath.name),
                "title": title,
                "allocated_at": now,
                "status": "active",
            }
        )
        idmap["mappings"][new_rel] = doc_id
        created.append((new_rel, doc_id, title))

    reg["next_doc_sequence"] = next_seq
    reg["updated_at"] = now
    idmap["updated_at"] = now
    reg_path.write_text(json.dumps(reg, ensure_ascii=False, indent=2), encoding="utf-8")
    map_path.write_text(json.dumps(idmap, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"新增文档: {len(created)}")
    for rel, doc_id, title in created[:20]:
        print(f"  {doc_id} {rel} {title}")


if __name__ == "__main__":
    main()
