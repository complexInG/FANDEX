---
order: 860
title: 事件调度器 语法速查手册
module: mysql

category: '020-mysql'
difficulty: beginner
description: 事件调度器 语法速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
## 调度器开关

**基本写法：查看事件调度器状态**
`SHOW VARIABLES LIKE 'event_scheduler';`

```sql
-- 查看事件调度器是否开启
SHOW VARIABLES LIKE 'event_scheduler';
-- 输出: event_scheduler | ON / OFF
```

**基本写法：开启事件调度器**
`SET GLOBAL event_scheduler = ON;`

```sql
-- 全局开启事件调度器（运行时生效，重启失效）
SET GLOBAL event_scheduler = ON;
```

**基本写法：配置文件持久开启**
`event_scheduler = ON`

```ini
# my.cnf 中配置，重启后持久生效
[mysqld]
event_scheduler = ON
```

---

## 创建事件

**基本写法：一次性事件**
`CREATE EVENT <事件名> ON SCHEDULE AT <时间点> DO <SQL 语句>;`

```sql
-- 在指定时间执行一次
CREATE EVENT e_clean_logs
ON SCHEDULE AT '2024-12-31 23:59:59'
DO DELETE FROM logs WHERE created_at < NOW() - INTERVAL 30 DAY;
```

**基本写法：当前时间延迟执行**
`CREATE EVENT <事件名> ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL <数值> <单位> DO <SQL>;`

```sql
-- 1 小时后执行一次
CREATE EVENT e_notify
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR
DO UPDATE users SET notified = 1 WHERE last_login < NOW() - INTERVAL 7 DAY;
```

**基本写法：周期事件**
`CREATE EVENT <事件名> ON SCHEDULE EVERY <数值> <单位> DO <SQL 语句>;`

```sql
-- 每天执行一次清理
CREATE EVENT e_daily_clean
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_TIMESTAMP
DO CALL sp_clean_expired();
```

**基本写法：指定起止时间的周期事件**
`CREATE EVENT <事件名> ON SCHEDULE EVERY <间隔> STARTS <开始> ENDS <结束> DO <SQL>;`

```sql
-- 每小时执行，限定起止时间
CREATE EVENT e_hourly_stat
ON SCHEDULE EVERY 1 HOUR
STARTS '2024-01-01 00:00:00'
ENDS '2024-12-31 23:59:59'
DO CALL sp_calc_hourly_stats();
```

**基本写法：复合语句事件**
`CREATE EVENT <事件名> ON SCHEDULE <调度> DO BEGIN <语句1>; <语句2>; END`

```sql
-- 执行多条语句需用 BEGIN...END 包裹并重置分隔符
DELIMITER //
CREATE EVENT e_multi ON SCHEDULE EVERY 1 DAY
DO BEGIN
  DELETE FROM logs WHERE created_at < NOW() - INTERVAL 30 DAY;
  UPDATE stats SET count = 0 WHERE stat_date = CURDATE();
END //
DELIMITER ;
```

---

## 事件管理

**基本写法：查看事件**
`SHOW EVENTS [FROM <数据库名>] [LIKE '<模式>'];`

```sql
-- 查看当前库所有事件
SHOW EVENTS;
-- 查看指定库事件
SHOW EVENTS FROM mydb LIKE 'e_%';
```

**基本写法：查看事件定义**
`SHOW CREATE EVENT <事件名>;`

```sql
-- 查看事件创建语句
SHOW CREATE EVENT e_daily_clean\G
```

**基本写法：查看事件元数据**
`SELECT * FROM information_schema.EVENTS WHERE event_name = '<事件名>';`

```sql
-- 查询事件状态与调度信息
SELECT event_name, last_executed, status, interval_value, interval_field
FROM information_schema.EVENTS
WHERE event_schema = 'mydb';
```

---

## 修改与删除

**基本写法：禁用/启用事件**
`ALTER EVENT <事件名> {DISABLE|ENABLE};`

```sql
-- 临时禁用事件
ALTER EVENT e_daily_clean DISABLE;
-- 重新启用
ALTER EVENT e_daily_clean ENABLE;
```

**基本写法：修改事件调度**
`ALTER EVENT <事件名> ON SCHEDULE <新调度> DO <SQL>;`

```sql
-- 修改执行周期为每周一次
ALTER EVENT e_daily_clean
ON SCHEDULE EVERY 1 WEEK STARTS CURRENT_TIMESTAMP
DO CALL sp_clean_expired();
```

**基本写法：重命名事件**
`ALTER EVENT <旧事件名> RENAME TO <新事件名>;`

```sql
-- 重命名事件
ALTER EVENT e_daily_clean RENAME TO e_weekly_clean;
```

**基本写法：删除事件**
`DROP EVENT [IF EXISTS] <事件名>;`

```sql
-- 安全删除事件
DROP EVENT IF EXISTS e_weekly_clean;
```

---

## 参考文献

MySQL 官方文档：https://dev.mysql.com/doc/
MySQL 8.0 参考手册：https://dev.mysql.com/doc/refman/8.0/en/
High Performance MySQL（O'Reilly）：https://www.oreilly.com/library/view/high-performance-mysql/
Percona 博客：https://www.percona.com/blog/

## 延伸阅读

MySQL 索引与优化，见 020-mysql 模块文档。
MySQL 日志体系，见 020-mysql 模块 redo/binlog 文档。
Redis 缓存与 MySQL 组合，见 022-redis 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 MySQL 高级课程。

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
