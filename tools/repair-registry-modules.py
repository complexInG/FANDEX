# -*- coding: utf-8 -*-
"""修复 _id-registry.json 中 promoted 文档的 module_id 归属（M000 -> 真实模块）。"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = os.path.join(ROOT, "cnt-content", "full")


def main():
    reg_path = os.path.join(FULL, "_id-registry.json")
    map_path = os.path.join(FULL, "_doc-id-map.json")
    reg = json.load(open(reg_path, encoding="utf-8"))
    dmap = json.load(open(map_path, encoding="utf-8"))

    # 模块：folder_order -> module_id
    folder_to_module = {}
    for m in reg["modules"]:
        folder_to_module[m["folder_order"]] = m["module_id"]

    docs_by_id = {d["doc_id"]: d for d in reg["docs"]}
    fixed = 0
    for source_path, doc_id in dmap.get("mappings", {}).items():
        sp = source_path.replace("\\", "/")
        m = re.match(r"^(\d{3})-[^/]+/(\d{3})-([^/]+)\.md$", sp)
        if not m:
            continue
        folder_order = int(m.group(1))
        doc_order = int(m.group(2))
        english = m.group(3)
        module_id = folder_to_module.get(folder_order)
        if not module_id:
            continue
        rec = docs_by_id.get(doc_id)
        if not rec:
            continue
        if rec.get("module_id") != module_id or rec.get("doc_order") != doc_order:
            rec["module_id"] = module_id
            rec["doc_order"] = doc_order
            rec["english_name"] = english
            fixed += 1

    json.dump(reg, open(reg_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("fixed", fixed, "docs")


if __name__ == "__main__":
    main()
