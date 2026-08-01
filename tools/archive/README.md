# tools/archive/ 归档说明

本目录存放 FANDEX 内容工程中的一次性资产，冻结维护。

| 子目录 | 内容 | 说明 |
| --- | --- | --- |
| batch-fixes/ | 22 个 fix-*-batch.py | 按模块编写的一次性批量修复脚本（algo、bigdata、c、cloud、cs、csharp、devops、final、go、gs-git、harmonyos、java、kotlin、lua、misc、mysql、p0、redis、se 等），对应缺陷已修复完毕，仅作历史留档 |
| diagnostics/ | audit-docs.py、classify-diagrams.py、preview-converted.py、fix-024-intro.py | 临时诊断与一次性修复 |
| data/ | worklist.json/csv、unconverted.json、broken-report.json、mobile-full-map.json | 会话数据产物（ASCII 转换清单、mobile 映射等） |

约定：

- 归档脚本不修改、不删除；
- 需要复用时，先从归档复制到 tools/ 根目录并核对输入输出，确认仍适用于当前文档结构后再运行；
- 新的一次性脚本请直接放入对应归档子目录，避免根目录脚本数量膨胀与职责漂移。
