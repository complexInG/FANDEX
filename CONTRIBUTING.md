# 贡献指南（Contributing）

感谢你考虑为 FANDEX 做出贡献。本文档说明提交流程与必须遵守的规范；工程细节与
文档 frontmatter 字段约束以 [AGENTS.md](AGENTS.md) 为准。

## 贡献方式

- **修正内容错误**：文档中的技术错误、代码示例问题、死链，欢迎直接提交修复；
- **补充知识点**：在现有模块内新增文档，或在现有文档中扩充内容；
- **报告问题**：不便于直接修复的问题，请提交 Issue 并附上复现方式或截图。

## 提交流程

1. Fork 本仓库（外部贡献者）或从最新 `main` 拉取；
2. 创建特性分支，命名遵循 `feat/<描述>`、`fix/<描述>`、`docs/<描述>`、
   `refactor/<描述>` 等前缀，全部小写中划线分隔；
3. 完成修改并自测（见下方自检清单）；
4. 提交 Pull Request 到 `main` 分支，描述中说明变更目的、范围与自测结果。

## 提交信息规范

遵循 Conventional Commits：

```
<type>(<scope>): <描述>

<正文：说明动机与影响，可选>

<footer: 关联 Issue 等，可选>
```

- `type`：feat / fix / docs / refactor / chore / ci / perf / test；
- 描述使用中文、动词开头、结尾不加句号；
- 示例：`fix(content): 修正 go 模块并发章节的代码示例错误`。

## 内容文档规范（重点）

修改 `cnt-content/full/` 下的教学文档时，必须遵守：

1. **frontmatter 规范**：仅允许 AGENTS.md 规定的 10 个标准字段，顺序与取值约束
   见 AGENTS.md（`order` 每模块内从 10 开始、步长 10；`difficulty` 仅限
   beginner / intermediate / advanced）；
2. **引用完整**：`related` 与 `prerequisites` 统一为 `module/文件名` 格式，必须指向
   真实存在的文档，禁止死链；
3. **新增文档**：插入学习顺序对应位置后，模块内整体重新编号，并同步更新所有
   旧引用；
4. **禁止 emoji**；图形需求使用 Mermaid 或 SVG；代码块必须标注语言；
5. **单一来源**：内容只写入 `cnt-content/full`，不修改三端应用内的生成产物
   （assets 目录），构建时由管线自动同步。

## 自检清单

提交前请确认：

- [ ] frontmatter 字段完整、顺序正确、order 编号连续；
- [ ] 新增或修改的 `related` / `prerequisites` 引用全部真实存在；
- [ ] 代码示例语法正确、已标注语言；
- [ ] 网站构建通过（根目录执行 `pnpm build:web`）；
- [ ] 无 emoji、无构建产物入库；
- [ ] 提交信息符合 Conventional Commits。

## 行为准则

保持友善与建设性：讨论针对内容与技术本身，尊重不同背景的学习者。恶意行为将被
移除并限制参与。
