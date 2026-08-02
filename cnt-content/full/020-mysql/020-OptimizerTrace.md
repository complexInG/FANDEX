---
order: 200
title: 优化器追踪
module: 'mysql'
category: 数据库
difficulty: advanced
description: MySQL优化器追踪OPTIMIZER_TRACE：执行计划选择过程、代价计算与调试方法
author: fanquanpp
updated: '2026-08-01'
related:
  - 'mysql/018-EXPLAINDetailed'
  - 'mysql/019-SlowQueryLog'
  - 'mysql/021-SubqueryOptimization'
  - 'mysql/022-DerivedTableOptimization'
prerequisites:
  - 'mysql/085-View'
---


## 1. 优化器追踪概述

MySQL 5.6 引入 OPTIMIZER_TRACE，记录优化器选择执行计划的完整过程。

## 2. 使用方法

```sql
-- 开启优化器追踪
SET optimizer_trace = 'enabled=on';
SET optimizer_trace_max_mem_size = 1048576;  -- 1MB

-- 执行查询
SELECT * FROM employees WHERE dept_id = 5;

-- 查看追踪结果
SELECT * FROM information_schema.OPTIMIZER_TRACE\G

-- 关闭追踪
SET optimizer_trace = 'enabled=off';
```

## 3. 追踪结果解读

```json
{
  "steps": [
    {
      "join_preparation": {
        "select#": 1,
        "steps": [
          {"expanded_query": "/* select#1 */ SELECT ..."}
        ]
      }
    },
    {
      "join_optimization": {
        "select#": 1,
        "steps": [
          {"condition_processing": {"condition": "WHERE"}},
          {"substitute_generated_columns": {}},
          {"table_dependencies": [...]},
          {"ref_optimizer_key_uses": [...]},
          {"rows_estimation": [...]},
          {"considered_execution_plans": [...]},
          {"attaching_conditions_to_tables": [...]}
        ]
      }
    },
    {
      "join_execution": {
        "select#": 1,
        "steps": [...]
      }
    }
  ]
}
```

## 4. 关键信息

### 4.1 rows_estimation

```json
{
  "rows_estimation": [
    {
      "table": "employees",
      "range_analysis": {
        "table_scan": { "rows": 10000, "cost": 2050 },
        "potential_range_indices": [
          { "index": "idx_dept", "usable": true, "key_parts": ["dept_id"] }
        ],
        "best_range_access": {
          "chosen": true,
          "index": "idx_dept",
          "rows": 100,
          "cost": 121
        }
      }
    }
  ]
}
```

### 4.2 considered_execution_plans

```json
{
  "considered_execution_plans": [
    {
      "plan_prefix": [],
      "table": "employees",
      "best_access_path": {
        "considered_access_paths": [
          { "access_type": "ref", "index": "idx_dept", "cost": 50, "chosen": true },
          { "access_type": "scan", "cost": 2050, "chosen": false }
        ]
      },
      "cost_for_plan": 50,
      "chosen": true
    }
  ]
}
```

## 5. 实际应用

```sql
-- 诊断优化器为何选择全表扫描
SET optimizer_trace = 'enabled=on';
SELECT * FROM large_table WHERE status = 'rare_value';
SELECT TRACE FROM information_schema.OPTIMIZER_TRACE\G
-- 查看 range_analysis 中各索引的代价估算
-- 如果索引代价估算偏高，可能需要更新统计信息
ANALYZE TABLE large_table;
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
