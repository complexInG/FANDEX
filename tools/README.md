# tools/ 内容工程脚本治理

本目录存放 FANDEX 内容工程（cnt-content/full 文档库）的批处理脚本。
它们是内容工程的半自动化资产，与 tls-tools（TypeScript 内容 ID 与清单治理工具链）职责不同、互补运行。

## 目录结构

```text
tools/
  README.md                 # 本文件：索引与治理约定
  其余 *.py                 # 可复跑的内容工程管线与校验工具（见下）
```

## 可复跑管线（tools/ 根目录）

| 类别 | 脚本 | 用途 |
| --- | --- | --- |
| 合并/提升 | map-mobile-to-full.py、merge-mobile-into-full.py、promote-mobile-to-full.py | mobile 内容并入 full 并注册文档 ID（幂等，可复跑） |
| 清理/精简 | remove-exercises-and-links.py | 移除全库"例题/练习"小节、删除纯例题专册、精简尾部外链（默认干跑，--apply 写回，幂等） |
| 修复/校验 | fix-bad-images.py、repair-registry-modules.py、check-content.py、verify-cleanup.py、verify-no-ascii-diagrams.py、scan-ascii-diagrams.py、scan-bad-images.py、scan-entry-docs.py、scan-islands.py、scan-sections.py、scan-toc-sections.py | 内容质量门禁与巡检 |

## 已清理的一次性脚本（2026-08-02）

以下脚本为一次性迁移/清理操作，任务已完成，按治理约定从仓库删除（git 历史可找回）：

- 论文级 enrich/thesis 管线：enrich-docs.py、thesis-merge.py、upgrade-frontmatter.py、
  strip-enrichment.py、clean-enrichment-filler.py、add-beginner-intro.py 及 kb/、thesis-fragments/
  （文档定位已调整为"笔记、资料"导向，不再使用论文级骨架）
- 全库清理类：clean-doc-sections.py、clean-emoji.py、convert-ascii-diagrams.py、
  convert-remaining-exercises.py、remove-island-fragments.py、remove-learning-objectives.py、
  remove-learning-path.py、remove-toc-sections.py、remove-zero-section.py、repair-registry-modules.py

对应场景的巡检能力保留在 scan-*/verify-*/check-content.py 中，可继续作为质量门禁使用。

## 是否迁移进 tls-tools：评估结论

不建议整体迁移。理由：

1. 技术栈不匹配：tls-tools 是 TypeScript/Node 工具链（allocate-id、generate-manifest、validate-naming），60+ Python 脚本移植为 TS 需要重写与双运行时维护，成本高、收益低。
2. 生命周期不同：tls-tools 是长期治理服务（ID 分配、清单生成、签名验证）；tools/ 下多数脚本是执行一次或按需复跑的内容工程操作，稳定性要求低。
3. 职责边界清晰：内容数据治理属于 Python 管线，内容元数据（ID/清单）治理属于 tls-tools；两者通过 _id-registry.json、_doc-id-map.json、manifest 文件对接，已形成稳定接口。

建议的治理方式（本目录已落实前三条）：

1. 一次性脚本使用完毕直接删除（git 历史可找回），不再留档混入根目录；
2. 可复跑管线保留在根目录，并以本 README 建立索引与状态标注；
3. 全库清理类操作前先运行 check-content.py 记录基线，操作后复跑验证；
4. 若某能力需要跨端复用（如文档 YAML 校验、frontmatter 归一化），以明确 CLI 接口在 tls-tools 中重新实现（TS），而非整包移植 Python 脚本；
5. 新脚本约定：文件头注明用途、输入、输出、是否幂等；涉及中文文本时避免在 shell heredoc 中传递（Windows 控制台编码会破坏非 GBK 字符），统一落盘为 UTF-8 文件执行。

## 脚本漂移风险点（分析结论）

- 硬编码 ROOT 相对路径：脚本均基于仓库根解析，仓库结构变化时需同步更新；
- 直接原地改写 cnt-content：多数清理脚本就地写回文件，运行前应有 Git 基线（git status 干净）且可回退；
- 无单元测试：内容工程脚本以一次性/低频率运行为主，靠 check-content.py 做结果校验，不引入测试框架；
- 幂等性不一：部分脚本（merge/promote）显式幂等，部分清理脚本重复运行可能误删（如 remove-* 系列），运行前需确认目标状态。
