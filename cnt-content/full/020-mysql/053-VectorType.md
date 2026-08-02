---
order: 530
title: VECTOR向量类型
module: 'mysql'
category: 数据库
difficulty: advanced
description: MySQL VECTOR向量类型：向量存储、距离计算、AI嵌入与近似最近邻搜索
author: fanquanpp
updated: '2026-08-01'
related:
  - 'mysql/051-MySQLIndexExecutionPlan'
  - 'mysql/052-MySQL9NewFeaturesParallelQuery'
  - 'mysql/054-JSONSchemaValidationAggregate'
  - 'mysql/055-ReplicationHA'
prerequisites:
  - 'mysql/085-View'
---


## 1. VECTOR 类型概述

MySQL 9.0 引入 VECTOR 类型，用于存储和检索高维向量，支持 AI/ML 应用中的嵌入向量搜索。

## 2. 创建向量列

```sql
-- 创建包含向量列的表
CREATE TABLE documents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT,
    embedding VECTOR(1536)  -- 1536维向量（OpenAI嵌入）
);

-- 插入向量数据
INSERT INTO documents (content, embedding) VALUES (
    'MySQL is a relational database',
    STRING_TO_VECTOR('[0.1, 0.2, 0.3, ...]')
);
```

## 3. 向量函数

### 3.1 距离计算

```sql
-- 欧几里得距离（L2距离）
SELECT id, content,
    DISTANCE(embedding, STRING_TO_VECTOR('[0.1, 0.2, ...]')) AS dist
FROM documents
ORDER BY dist ASC
LIMIT 10;

-- 余弦相似度
SELECT id, content,
    DISTANCE(embedding, STRING_TO_VECTOR('[0.1, 0.2, ...]'), 'COSINE') AS similarity
FROM documents
ORDER BY similarity DESC
LIMIT 10;
```

### 3.2 向量转换

```sql
-- 字符串转向量
SELECT STRING_TO_VECTOR('[0.1, 0.2, 0.3]');

-- 向量转字符串
SELECT VECTOR_TO_STRING(embedding) FROM documents LIMIT 1;
```

## 4. 向量索引

```sql
-- 创建向量索引（近似最近邻搜索）
ALTER TABLE documents ADD VECTOR INDEX idx_embedding (embedding)
    WITH (DISTANCE = 'COSINE', M = 16, EF_BUILD = 100);

-- 使用向量索引搜索
SELECT id, content,
    DISTANCE(embedding, STRING_TO_VECTOR('[0.1, 0.2, ...]'), 'COSINE') AS dist
FROM documents
ORDER BY dist ASC
LIMIT 10;
-- 自动使用向量索引加速
```

## 5. 应用场景

```sql
-- 语义搜索
-- 1. 使用嵌入模型生成查询向量
-- 2. 在数据库中搜索最近邻向量
-- 3. 返回语义相关的文档

-- 推荐系统
-- 1. 用户偏好向量化
-- 2. 商品特征向量化
-- 3. 基于向量相似度推荐

-- 图像搜索
-- 1. 图像特征提取为向量
-- 2. 基于向量距离搜索相似图像
```

## 延伸阅读
MySQL 索引与优化，见 020-mysql 模块文档。
MySQL 日志体系，见 020-mysql 模块 redo/binlog 文档。
Redis 缓存与 MySQL 组合，见 022-redis 模块。
## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 InnoDB 日志与崩溃恢复

redo log 记录物理页修改（WAL：先写日志再写数据页），崩溃后重放恢复；环形文件组 + checkpoint 推进。
undo log 记录事务前镜像，支持回滚与 MVCC 版本链；purge 线程清理。
两阶段提交：redo prepare -> binlog -> redo commit，保证两份日志一致，主从不丢数据。
刷盘策略：innodb_flush_log_at_trx_commit=1 最安全（每次提交 fsync），2 每秒刷。

### 13.2 执行计划与优化器

EXPLAIN 关键列：type（const/ref/range/index/ALL）、key、rows、Extra（Using index/Using filesort）。
优化器基于统计信息选计划；analyze table 更新统计；hint（FORCE INDEX）谨慎使用。
排序与分组：filesort 优化为索引序；避免临时表。
慢查询治理流程：慢日志 -> 计划分析 -> 索引/改写 -> 验证。
