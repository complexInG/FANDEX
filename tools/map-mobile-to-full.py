# -*- coding: utf-8 -*-
"""建立 mobile → full 文档对应映射，输出合并计划。

规则：
1. 同名（规范化后）→ 视为"已有对应文档"，标记 merge
2. full 中不存在但主题相关 → 标记 promote（建议提升进 full）
3. 输出 tools/mobile-full-map.json 供后续合并脚本使用
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
FULL = ROOT / "cnt-content" / "full"
MOBILE = ROOT / "cnt-content" / "mobile"


def norm(name: str) -> str:
    n = re.sub(r"^\d{3}-", "", name)
    n = re.sub(r"\.md$", "", n)
    return re.sub(r"[^a-z0-9]+", "", n.lower())


def main() -> None:
    # 读取旧映射以保留 fuzzy-resolved 结果
    old_path = ROOT / "tools" / "mobile-full-map.json"
    old_map = {}
    if old_path.exists():
        try:
            old_map = {p["mobile"]: p for p in json.loads(old_path.read_text(encoding="utf-8"))}
        except Exception:
            old_map = {}

    full_idx: dict[tuple[str, str], list[str]] = {}
    for f in FULL.rglob("*.md"):
        parts = f.relative_to(FULL).parts
        if len(parts) < 2:
            continue
        full_idx.setdefault((parts[0], norm(parts[-1])), []).append(f.relative_to(FULL).as_posix())

    plan: list[dict] = []
    for f in sorted(MOBILE.rglob("*.md")):
        rel = f.relative_to(MOBILE)
        parts = rel.parts
        if len(parts) < 2:
            continue
        mod = parts[0]
        fn = norm(parts[-1])
        exact = full_idx.get((mod, fn), [])
        fuzzy: list[str] = []
        if not exact:
            for (m, n), paths in full_idx.items():
                if m == mod and (n.startswith(fn[:10]) or fn.startswith(n[:10])):
                    fuzzy.extend(paths)
        status = "merge" if exact else ("fuzzy" if fuzzy else "promote")
        if not exact and not fuzzy:
            # full 中无同名，但同模块内主题关键词重合 → 提升但标记为疑似重复（promote-dup）
            mt = norm(parts[-1])
            hits = []
            for (m, n), paths in full_idx.items():
                if m == mod and mt and (
                    mt.startswith(n[:10]) or n.startswith(mt[:10])
                    or (len(mt) >= 6 and mt[:6] in n) or (len(n) >= 6 and n[:6] in mt)
                ):
                    hits.extend(paths)
            if hits:
                plan_entry = {
                    "mobile": rel.as_posix(),
                    "module": mod,
                    "full_exact": [],
                    "full_fuzzy": hits[:1],
                    "status": "promote-dup",
                    "mobile_size": f.stat().st_size,
                }
            else:
                plan_entry = {
                    "mobile": rel.as_posix(),
                    "module": mod,
                    "full_exact": [],
                    "full_fuzzy": [],
                    "status": "promote",
                    "mobile_size": f.stat().st_size,
                }
        else:
            plan_entry = {
                "mobile": rel.as_posix(),
                "module": mod,
                "full_exact": exact[:1],
                "full_fuzzy": fuzzy[:2],
                "status": status,
                "mobile_size": f.stat().st_size,
            }
        # 若旧映射中已解析为 fuzzy-resolved，沿用解析结果
        old = old_map.get(rel.as_posix())
        if old and old.get("status") == "fuzzy-resolved" and old.get("full_exact"):
            plan_entry["status"] = "fuzzy-resolved"
            plan_entry["full_exact"] = old["full_exact"]
            plan_entry["full_fuzzy"] = []
        plan.append(plan_entry)

    out = ROOT / "tools" / "mobile-full-map.json"
    out.write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf-8")

    from collections import Counter

    c = Counter(p["status"] for p in plan)
    print(f"mobile 总数: {len(plan)}")
    print(f"  merge（full 已有同名）: {c['merge']}")
    print(f"  fuzzy（模糊对应）: {c['fuzzy']}")
    print(f"  promote（full 缺失，建议新增）: {c['promote']}")
    print(f"映射已写入: {out}")


if __name__ == "__main__":
    main()
