---
order: 260
title: 微数据与JSON-LD
module: 'html5'
category: 前端技术
difficulty: intermediate
description: Microdata与JSON-LD
author: fanquanpp
updated: '2026-08-02'
related:
  - 'html5/027-CustomDataAttribute'
  - 'html5/028-CrossDocumentCommunication'
prerequisites:
  - 'html5/001-HTML5OverviewCoreFeature'
---

## 0. 直觉：给搜索引擎看的“商品标签”

搜索结果里，有的条目带星级、价格、作者头像——那是搜索引擎读懂了页面里的结构化数据，在结果里渲染出“富媒体摘要”。

结构化数据就是“给机器读的标签”：用统一的 Schema.org 词汇描述“这是什么”（文章、商品、人、事件），让搜索引擎和社交平台准确理解页面内容。Google 官方推荐 JSON-LD 格式。

## 1. 结构化数据概述

| 格式          | 嵌入方式        | 优点                    | 缺点       |
| ------------- | --------------- | ----------------------- | ---------- |
| **Microdata** | HTML 属性       | 与内容一体              | HTML 冗余  |
| **JSON-LD**   | `<script>` 标签 | 独立于内容，Google 推荐 | 需额外维护 |

## 2. Microdata

```html
<div itemscope itemtype="https://schema.org/Person">
  <span itemprop="name">张三</span>
  <span itemprop="jobTitle">软件工程师</span>
</div>
```

**讲解：**

- `itemscope` 声明一个数据项目，`itemtype` 指定类型（Schema.org 的 URL）；
- `itemprop` 标记具体属性，如 `name`、`jobTitle`；
- Microdata 与内容同在一个标签上，属性写在 HTML 里，维护时容易耦合。

| 属性        | 说明                       |
| ----------- | -------------------------- |
| `itemscope` | 声明一个项目               |
| `itemtype`  | 项目类型（Schema.org URL） |
| `itemprop`  | 项目属性                   |

## 3. JSON-LD

```html
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "深入理解 HTML5",
    "author": { "@type": "Person", "name": "张三" },
    "datePublished": "2026-06-14"
  }
</script>
```

**讲解：**

- JSON-LD 用独立的 `<script type="application/ld+json">` 块描述数据，页面内容无需改动；
- `@context` 指向词汇表，`@type` 是实体类型，其余字段是该类型的属性；
- 嵌套对象（如 `author`）可以再声明自己的 `@type`；
- 它是 Google 推荐的结构化数据格式，易于复制与维护。

### 常用类型

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "无线蓝牙耳机",
  "offers": { "@type": "Offer", "price": "299.00", "priceCurrency": "CNY" },
  "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.5" }
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "什么是 HTML5？",
      "acceptedAnswer": { "@type": "Answer", "text": "HTML5 是超文本标记语言的最新标准..." }
    }
  ]
}
```

**讲解：** `Product` 类型可带 `offers`（价格）与 `aggregateRating`（评分）；搜索引擎据此在结果中展示价格与星级。电商、文章、招聘页面是最常见的应用场景。

## 4. 验证与测试

- [Google 富摘要测试](https://search.google.com/test/rich-results)
- [Schema.org 验证器](https://validator.schema.org/)

## 5. 进阶知识点

### 5.1 三种格式对比

| 格式 | 嵌入方式 | 优点 | 缺点 |
| --- | --- | --- | --- |
| Microdata | HTML 属性 | 与内容一体 | HTML 冗余、维护耦合 |
| JSON-LD | `<script>` 标签 | 独立于内容，Google 推荐 | 需额外维护 |
| RDFa | HTML 属性 | 兼容 RDF 生态 | 语法复杂，较少使用 |

## 6. 动手试试

1. 给一篇博客文章添加 JSON-LD 的 `Article` 数据（标题、作者、发布日期）；
2. 用 Google Rich Results Test 或 Schema Markup Validator 验证；
3. 给一个商品页添加 `Product` + `Offer` + `AggregateRating`，观察搜索结果能展示哪些增强信息；
4. 进阶挑战：对比 Microdata 与 JSON-LD 在同一个页面上的维护成本。

## 7. 核心知识点

> 一句话记住结构化数据：`Schema.org` 定词汇，JSON-LD 最推荐；`@type` 说类型，属性描述内容，验证工具保正确。

- 结构化数据让搜索引擎理解页面实体（文章、商品、人、事件）；
- 两种主流格式：Microdata（HTML 属性）与 JSON-LD（script 标签）；
- JSON-LD 独立于内容、Google 推荐，是首选方案；
- `@context`/`@type`/属性字段构成 JSON-LD 基本结构；
- 上线前用 Rich Results Test 验证，错误数据会被忽略。

## 8. 注意事项与改进建议

| 问题点 | 说明 | 改进方案 |
| --- | --- | --- |
| 数据与页面不符 | 被判定为作弊，降低信任 | 结构化数据必须与可见内容一致 |
| 滥用 `Review`/`Rating` | 自评星级违反政策 | 只标记真实评价 |
| 忘记 `@context` | 解析器无法识别词汇表 | 始终声明 `https://schema.org` |
| 只做一种格式 | 维护成本与兼容性 | 新项目直接用 JSON-LD |
| 不上线验证 | 语法错误被静默忽略 | 用 Rich Results Test 检查 |

## 9. 扩展学习

- Schema.org 官方文档：完整类型与属性清单；
- SEO 实践：`css/043-HTMLSemanticSEO` 语义化与结构化数据的配合；
- 社交分享：`html5/009-MetadataCharacterEncoding` 中 Open Graph 与 JSON-LD 的差异；
- 验证工具：Google Rich Results Test、Schema Markup Validator。
