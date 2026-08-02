---
order: 120
title: Emoji表情
module: 'markdown'
category: 工具链
difficulty: beginner
description: Markdown中Emoji的使用方式：短代码语法、Unicode字符与平台兼容性。
author: fanquanpp
updated: '2026-08-01'
related:
  - 'markdown/010-Strikethrough'
  - 'markdown/011-AutoLink'
  - 'markdown/013-SubscriptSuperscript'
  - 'markdown/014-LaTeXMathFormula'
prerequisites:
  - 'markdown/001-SyntaxGuide'
---


## 1. Emoji 概述

### 1.1 在 Markdown 中使用 Emoji

Markdown 支持两种方式插入 Emoji：

| 方式        | 语法           | 示例        | 适用平台      |
| :---------- | :------------- | :---------- | :------------ |
| **短代码**  | `:emoji_name:` | `:smile:` → | GitHub/GitLab |
| **Unicode** | 直接输入       |             | 通用          |

### 1.2 Emoji 的价值

- **增强表达力**：用图形补充文字信息
- **视觉标记**：快速识别内容类型（ 警告、 完成）
- **提升可读性**：在列表和标题中作为视觉锚点
- **情感传达**：在协作讨论中表达语气

## 2. 短代码语法

### 2.1 基本用法

```markdown
今天天气真好 :sunny: :smile:

:tada: 项目发布成功！

:warning: 注意：此 API 已废弃
```

### 2.2 常用 Emoji 短代码

**表情与手势**

| 短代码     | 渲染 | 短代码       | 渲染 |
| :--------- | :--- | :----------- | :--- |
| `:smile:`  |      | `:laughing:` |      |
| `:heart:`  |      | `:thumbsup:` |      |
| `:rocket:` |      | `:fire:`     |      |
| `:eyes:`   |      | `:thinking:` |      |
| `:clap:`   |      | `:pray:`     |      |

**状态与标记**

| 短代码               | 渲染 | 用途      |
| :------------------- | :--- | :-------- |
| `:white_check_mark:` |      | 完成/通过 |
| `:x:`                |      | 失败/错误 |
| `:warning:`          |      | 警告      |
| `:bulb:`             |      | 提示/想法 |
| `:bookmark:`         |      | 标记/书签 |
| `:construction:`     |      | 建设中    |

**技术相关**

| 短代码       | 渲染 | 用途      |
| :----------- | :--- | :-------- |
| `:bug:`      |      | Bug       |
| `:sparkles:` |      | 新功能    |
| `:wrench:`   |      | 配置/修复 |
| `:memo:`     |      | 文档      |
| `:lock:`     |      | 安全      |
| `:gear:`     |      | 设置      |

## 3. 在 Git 提交中使用 Emoji

### 3.1 Gitmoji 规范

Gitmoji 是使用 Emoji 标识提交类型的约定：

| Emoji | 短代码                  | 提交类型    |
| :---- | :---------------------- | :---------- |
|       | `:tada:`                | 初始提交    |
|       | `:sparkles:`            | 新功能      |
|       | `:bug:`                 | 修复 Bug    |
|       | `:memo:`                | 文档更新    |
|       | `:lipstick:`            | UI/样式更新 |
|       | `:recycle:`             | 代码重构    |
|       | `:zap:`                 | 性能优化    |
|       | `:lock:`                | 安全修复    |
| ↑     | `:arrow_up:`            | 依赖升级    |
| ↓     | `:arrow_down:`          | 依赖降级    |
|       | `:construction_worker:` | CI/CD       |
|       | `:white_check_mark:`    | 测试        |

### 3.2 提交消息格式

```bash
git commit -m " feat: add user authentication"
git commit -m " fix: resolve login redirect loop"
git commit -m " docs: update API reference"
git commit -m " refactor: extract validation logic"
```

## 4. Unicode Emoji

### 4.1 直接输入

在支持 Unicode 的编辑器中可以直接输入 Emoji 字符：

```markdown
今天天气真好

项目发布成功！

注意：此 API 已废弃
```

### 4.2 Unicode 编码

每个 Emoji 都有对应的 Unicode 码点：

| Emoji | Unicode | HTML 实体   |
| :---- | :------ | :---------- |
|       | U+1F604 | `&#128516;` |
|       | U+2764  | `&#10084;`  |
|       | U+1F680 | `&#128640;` |
|       | U+2705  | `&#9989;`   |

### 4.3 组合 Emoji

某些 Emoji 可以通过零宽连接符（ZWJ, U+200D）组合：

```
 + ZWJ +  =  (女程序员)
 + ZWJ +  =  (男农民)
```

## 5. 平台兼容性

### 5.1 短代码支持

| 平台           | 短代码支持 | 说明         |
| :------------- | :--------- | :----------- |
| **GitHub**     |            | 完整支持     |
| **GitLab**     |            | 完整支持     |
| **Obsidian**   |            | 完整支持     |
| **Typora**     |            | 完整支持     |
| **Hugo**       |            | 需配置       |
| **CommonMark** |            | 不支持短代码 |

### 5.2 渲染差异

不同操作系统对 Emoji 的渲染风格不同：

| 系统          | 风格           | 示例           |
| :------------ | :------------- | :------------- |
| **macOS/iOS** | Apple 风格     | 圆润、色彩丰富 |
| **Windows**   | Microsoft 风格 | 扁平、轮廓清晰 |
| **Android**   | Google 风格    | 简约、色彩鲜明 |
| **Linux**     | 取决于字体     | 可能显示为黑白 |

## 6. 最佳实践

### 6.1 适度使用

- 在标题和列表中使用少量 Emoji 增强可读性
- 在 Git 提交消息中使用标准 Emoji
- 不要在正式文档中过度使用 Emoji
- 不要用 Emoji 替代必要的文字说明

### 6.2 可访问性

- Emoji 对屏幕阅读器不友好，确保有文字替代
- 不要仅靠 Emoji 传达关键信息
- 在正式文档中优先使用文字 + 格式

## 延伸阅读
Markdown 基础语法，见 002-markdown 模块文档。
Markdown 删除线语法，见 002-markdown/010-Strikethrough 文档。
文档站构建（Astro），见 056-astro 模块（如已加入）。
## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 CommonMark 解析规则

解析分块级与行内两阶段；块结构（列表、引用）优先级高于行内。
强调定界符规则：左右翼属性、匹配优先级；删除线与表格是 GFM 扩展。
HTML 块与内联 HTML 的解析规则；围栏代码块内不做行内解析。
理解规则可解释“为什么同一文档在不同渲染器结果不同”。

### 13.2 文档站自动化

frontmatter 驱动：标题、描述、排序、标签；目录自动生成。
组件化：MDX 嵌入交互组件；KaTeX 渲染公式。
质量门禁：markdownlint、remark 插件、构建期链接校验。
搜索与检索：全文索引（Pagefind）与交叉引用图。
