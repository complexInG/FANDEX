# mysqldump 备份命令 语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 基本备份

**基本写法：备份单个数据库**
`mysqldump -u <用户名> -p <数据库名> > <输出文件>.sql`

```bash
# 备份 mydb 数据库到文件
mysqldump -u root -p mydb > mydb_backup.sql
```

**基本写法：备份多个数据库**
`mysqldump -u <用户名> -p --databases <库1> <库2> [库...] > <输出文件>`

```bash
# 同时备份多个数据库（含 CREATE DATABASE 语句）
mysqldump -u root -p --databases db1 db2 db3 > multi_db.sql
```

**基本写法：备份所有数据库**
`mysqldump -u <用户名> -p --all-databases > <输出文件>`

```bash
# 全库备份
mysqldump -u root -p --all-databases > all_db_backup.sql
```

**基本写法：仅备份结构**
`mysqldump -u <用户名> -p --no-data <数据库名> > <输出文件>`

```bash
# 仅导出表结构（不包含数据）
mysqldump -u root -p --no-data mydb > mydb_schema.sql
```

**基本写法：仅备份数据**
`mysqldump -u <用户名> -p --no-create-info <数据库名> > <输出文件>`

```bash
# 仅导出数据（不含建表语句）
mysqldump -u root -p --no-create-info mydb > mydb_data.sql
```

---

## 指定表与条件

**基本写法：备份指定表**
`mysqldump -u <用户名> -p <数据库名> <表1> [表2...] > <输出文件>`

```bash
# 仅备份 users 和 orders 两张表
mysqldump -u root -p mydb users orders > tables_backup.sql
```

**基本写法：按条件备份（WHERE）**
`mysqldump -u <用户名> -p <数据库名> <表名> --where="<条件>" > <输出文件>`

```bash
# 仅备份 id 小于 1000 的记录
mysqldump -u root -p mydb users --where="id < 1000" > users_partial.sql
```

---

## 远程与压缩

**基本写法：备份远程数据库**
`mysqldump -h <主机> -P <端口> -u <用户名> -p <数据库名> > <输出文件>`

```bash
# 备份远程 MySQL 服务器
mysqldump -h 192.168.1.100 -P 3306 -u admin -p mydb > remote_backup.sql
```

**基本写法：管道压缩备份**
`mysqldump -u <用户名> -p <数据库名> | gzip > <输出文件>.sql.gz`

```bash
# 压缩备份减少磁盘占用
mysqldump -u root -p mydb | gzip > mydb_backup.sql.gz
```

**基本写法：解压恢复**
`gunzip -c <压缩文件>.sql.gz | mysql -u <用户名> -p <数据库名>`

```bash
# 解压并恢复数据库
gunzip -c mydb_backup.sql.gz | mysql -u root -p mydb
```

---

## 关键选项

**基本写法：兼容版本输出（8.4 新增 --output-as-version）**
`mysqldump -u <用户名> -p --output-as-version=<版本标识> <数据库名> > <输出文件>`

```bash
# 输出兼容 8.0.23 之前版本的语法
mysqldump -u root -p --output-as-version=BEFORE_8_0_23 mydb > compat.sql
```

**基本写法：事务一致性备份**
`mysqldump -u <用户名> -p --single-transaction --quick --routines --triggers <数据库名> > <输出文件>`

```bash
# InnoDB 一致性快照备份（推荐，不锁表）
mysqldump -u root -p --single-transaction --quick --routines --triggers mydb > consistent.sql
```

**基本写法：包含存储过程与事件**
`mysqldump -u <用户名> -p --routines --events --triggers <数据库名> > <输出文件>`

```bash
# 完整备份含存储过程、函数、事件、触发器
mysqldump -u root -p --routines --events --triggers --single-transaction mydb > full.sql
```

---

## 恢复数据

**基本写法：从文件恢复**
`mysql -u <用户名> -p <数据库名> < <备份文件>.sql`

```bash
# 恢复备份到指定数据库
mysql -u root -p mydb < mydb_backup.sql
```

**基本写法：源命令恢复**
`SOURCE <备份文件路径>`

```sql
-- 在 mysql 客户端内执行
SOURCE /backup/mydb_backup.sql;
```

---