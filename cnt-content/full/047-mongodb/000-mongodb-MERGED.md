---
order: 10
title: mongodb 模块文档合集
module: 'mongodb'
category: 数据库
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：047-mongodb/001-MongoDBOverviewQuickStart.md ============ -->


## 0. 五分钟跑起 MongoDB（先读这里）

> 学习目标：不管懂不懂概念，先让 MongoDB 跑起来，并插入、查询到第一条数据。

一句话理解：**MongoDB 是"存文档"的数据库——每条数据是一个 JSON 风格的文档，像一张张可以随意增减字段的卡片，而不是必须对齐列名的表格。**

### 0.1 用 Docker 启动（30 秒）

先确认本机已安装 Docker（参考 `getting-started/024-DockerInstall`），然后执行：

```bash
docker run -d --name mongo-dev -p 27017:27017 mongo:8.3
docker exec -it mongo-dev mongosh
```

**讲解：**

1. `docker run -d`：后台启动一个名为 `mongo-dev` 的容器；`-p 27017:27017` 把容器内的 MongoDB 端口映射到本机，方便本地工具连接。
2. `docker exec -it mongo-dev mongosh`：进入容器并打开官方命令行客户端 `mongosh`，此时你已经连上了数据库。
3. 看到 `test>` 提示符即表示成功。MongoDB 默认连接到名为 `test` 的数据库。

### 0.2 第一句增删改查（2 分钟）

在 `mongosh` 里逐行执行：

```javascript
use school

db.students.insertOne({
  name: "小明",
  age: 18,
  courses: ["数学", "英语"]
})

db.students.find({ name: "小明" })

db.students.updateOne(
  { name: "小明" },
  { $set: { age: 19 } }
)

db.students.deleteOne({ name: "小明" })
```

**讲解：**

1. `use school`：切换到（不存在则创建）名为 `school` 的数据库。
2. `db.students.insertOne({...})`：往 `students` 集合里插入一条文档。集合可以理解为"表"，文档可以理解为"行"，但字段不需要预先定义。
3. `find({ name: "小明" })`：按条件查询，参数是一个 JSON 文档，表示"name 等于 小明"。
4. `updateOne(条件, {$set: 新值})`：只更新第一条匹配的文档，`$set` 只修改指定字段，不影响其他字段。
5. `deleteOne(条件)`：删除第一条匹配的文档。
6. 观察：`courses` 直接存了一个数组，不需要建第三张关联表——这是文档模型与关系模型的第一个直观差异。

## 1. MongoDB 是什么

MongoDB 是一个开源的 **NoSQL 文档数据库**，由 MongoDB 公司开发，2009 年发布。它把数据存成 **BSON**（二进制 JSON），支持嵌套对象与数组，天然适合内容、用户、物联网等数据结构多变、读写频繁的场景。

### 1.1 与关系型数据库的对比

| 维度 | MySQL / PostgreSQL | MongoDB |
| --- | --- | --- |
| 数据单位 | 表（table）、行（row）、列（column） | 集合（collection）、文档（document）、字段（field） |
| 结构 | 建表前必须定死列 | 文档字段可动态增减 |
| 关联 | 外键 + JOIN | 内嵌或引用，聚合管道实现类似能力 |
| 事务 | ACID 完整 | 4.0 起支持多文档事务 |
| 横向扩展 | 主从/分库分表，成本较高 | 原生分片（sharding），自动路由 |
| 适用场景 | 强一致、复杂报表、金融账务 | 快速迭代、高写入、数据结构多变 |

### 1.2 当前版本现状（2026-08）

- MongoDB 8.3 为当前稳定版（2026-05 发布）；8.0/8.2 处于维护期，7.0 已接近支持尾声。
- 企业部署优先使用官方维护的 LTS 节奏版本，配合 `mongod` 副本集（Replica Set）保证高可用。
- 配套工具：`mongosh` 命令行、MongoDB Compass 图形客户端、官方各语言驱动。

## 2. 核心概念三件套

1. **数据库（Database）**：一个服务下可以有多个数据库，类似 MySQL 的 schema。
2. **集合（Collection）**：一组文档的容器，类似"表"，但不需要定义结构。
3. **文档（Document）**：一条数据，就是一个 JSON 对象，`_id` 字段是默认主键（可自动生成）。

```javascript
// 文档示例：_id 由 MongoDB 自动生成，其余字段按需增减
{
  _id: ObjectId("65f1a2b3c4d5e6f7a8b9c0d1"),
  name: "小明",
  age: 18,
  address: { city: "上海", district: "浦东" },   // 嵌套对象
  courses: ["数学", "英语"],                     // 数组
  createdAt: ISODate("2026-08-03T00:00:00Z")
}
```

**讲解：**

1. `_id` 是主键字段，插入时省略会自动生成 24 位十六进制的 `ObjectId`，保证全局唯一。
2. `address` 是嵌套对象：关系型数据库往往要拆成两张表再加外键，文档模型直接内嵌。
3. `courses` 是数组：一对多关系最自然的表达方式。

## 3. 什么时候该用 MongoDB

适合：

- 数据结构频繁变化（产品原型期、配置类数据）；
- 高写入量、海量日志、物联网时序类数据；
- 内容系统（文章、评论树）、用户画像、购物车等"整份对象读写"场景；
- 需要水平分片扩展读写的场景。

不适合：

- 强事务、多表复杂 JOIN 的财务账务系统；
- 列结构极其稳定、报表高度依赖 SQL 聚合的场景（此时 PostgreSQL 更合适）。

## 4. 动手试试

1. 启动容器后，在 `mongosh` 中新建一个 `books` 集合，插入 3 本你喜欢的书（字段：书名、作者、价格）。
2. 用 `find({ 作者: "..." })` 查询其中一本。
3. 用 `updateOne` 把价格加 10，再用 `deleteOne` 删掉一本。
4. 试想：如果用 MySQL 表达"一本书有多个标签"，需要几张表？MongoDB 怎么表达？

## 5. 一句话记住

> MongoDB 把数据当"文档"存：字段随便加、数组随便嵌，先跑起来再设计结构——这是它与 MySQL 最根本的区别。

下一章进入增删改查的完整语法。



<!-- ============ 文档分隔线：047-mongodb/002-CRUDOperations.md ============ -->


## 0. 一句话理解

> MongoDB 的增删改查就是四个动词：`insert` 加、`find` 查、`update` 改、`delete` 删；查询和修改条件都写成 JSON 文档。

## 1. 插入：insertOne 与 insertMany

```javascript
db.students.insertOne({
  name: "小红",
  age: 17,
  scores: { math: 92, english: 88 }
})

db.students.insertMany([
  { name: "小刚", age: 18, scores: { math: 70, english: 75 } },
  { name: "小丽", age: 19, scores: { math: 85, english: 95 } }
])
```

**讲解：**

1. `insertOne` 插入单条；`insertMany` 接收数组批量插入，比循环单条插入快一个数量级。
2. `scores` 字段内嵌了数学和英语成绩，属于典型的"整份对象一起读写"设计。
3. 批量插入时若某条违反唯一索引约束，默认整批失败；传 `{ ordered: false }` 可以让成功的继续、只报告失败的那条。

## 2. 查询：find 与查询运算符

### 2.1 基础查询

```javascript
// 查所有
db.students.find({})

// 等值查询
db.students.find({ age: 18 })

// 投影：只要 name 和 age，_id 默认保留
db.students.find({ age: 18 }, { name: 1, age: 1 })
```

**讲解：**

1. `find({})` 的空对象表示"无条件"，等价于 SQL 的 `SELECT *`。
2. 第二个参数是投影：`1` 表示要的字段，`0` 表示不要的字段（`_id: 0` 可去掉主键）。

### 2.2 比较运算符

```javascript
// age 大于 17：$gt 大于、$gte 大于等于、$lt 小于、$lte 小于等于
db.students.find({ age: { $gt: 17 } })

// age 在 17 到 19 之间（含边界）
db.students.find({ age: { $gte: 17, $lte: 19 } })

// name 在指定数组中
db.students.find({ name: { $in: ["小红", "小刚"] } })

// 逻辑组合：age > 18 且 math 成绩 >= 90
db.students.find({
  age: { $gt: 18 },
  "scores.math": { $gte: 90 }
})
```

**讲解：**

1. `$gt/$gte/$lt/$lte` 对应 `>`、`>=`、`<`、`<=`，是查询条件里最常见的四个运算符。
2. `$in` 相当于 SQL 的 `IN (...)`。
3. 嵌套字段用**点路径** `"scores.math"` 访问，注意键名必须加引号，因为包含点号。
4. 多个条件写在同一对象里表示"并且"（AND）。

### 2.3 数组与正则

```javascript
// courses 数组包含 "数学"
db.students.find({ courses: "数学" })

// name 以 "小" 开头（正则查询）
db.students.find({ name: /^小/ })
```

**讲解：**

1. 数组字段直接写值，表示"包含该元素"，这是文档模型非常实用的特性。
2. 正则 `/^小/` 匹配以"小"开头的字符串；正则查询无法利用普通索引前缀，数据量大时慎用。

## 3. 更新：updateOne / updateMany / replaceOne

```javascript
// 修改第一条匹配的文档：把 age 加 1（$inc 自增）
db.students.updateOne(
  { name: "小红" },
  { $inc: { age: 1 } }
)

// 批量修改：所有 18 岁及以上的学生，标记 adult: true
db.students.updateMany(
  { age: { $gte: 18 } },
  { $set: { adult: true } }
)

// 整个文档替换（保留 _id）
db.students.replaceOne(
  { name: "小刚" },
  { name: "小刚", age: 20, remark: "已毕业" }
)
```

**讲解：**

1. `$set` 只新增/修改指定字段，`$inc` 做原子自增，`$unset` 删除字段。
2. `updateOne` 只更新第一条匹配；需要更新全部匹配时用 `updateMany`，这两个名字最容易写混。
3. `replaceOne` 用新文档整体替换旧文档（`_id` 不变），适合"整份重写"场景；忘记写上的字段会被丢掉。
4. 更新操作的第二个参数必须以 `$` 运算符开头（如 `$set`），直接写 `{ age: 19 }` 是语法错误。

## 4. 删除：deleteOne / deleteMany

```javascript
// 删除第一条匹配
db.students.deleteOne({ name: "小丽" })

// 删除所有 age 小于 18 的学生
db.students.deleteMany({ age: { $lt: 18 } })

// 清空集合（保留集合本身）
db.students.deleteMany({})
```

**讲解：**

1. `deleteOne({})` 会删掉"第一条"文档，而 `deleteMany({})` 会清空整个集合——企业环境里误执行后者是常见事故，操作前务必先用 `find` 确认条件。
2. 想连集合一起删掉，使用 `db.students.drop()`。

## 5. 排序、分页与计数

```javascript
// 按 age 降序，再按 name 升序
db.students.find({}).sort({ age: -1, name: 1 })

// 跳过前 2 条，取 5 条（第 3 页，每页 5 条）
db.students.find({}).sort({ age: -1 }).skip(10).limit(5)

// 计数
db.students.countDocuments({ age: { $gte: 18 } })
```

**讲解：**

1. `sort` 中 `1` 升序、`-1` 降序，多字段按书写顺序依次比较。
2. `skip + limit` 是经典分页写法；数据量极大时深分页性能差，可改用"上一页最后一条的 _id"做游标分页。
3. `countDocuments` 是推荐计数方法，`count()` 已废弃。

## 6. 动手试试

1. 建一个 `products` 集合，批量插入 5 个商品（字段：名称、分类、价格、库存）。
2. 查询价格在 50-200 之间的商品，按价格降序排列，只显示名称和价格。
3. 把所有库存为 0 的商品价格打 8 折（`$mul` 运算符）。
4. 删除"分类为配件"的所有商品，删除前先数一数有多少条。

## 7. 一句话记住

> 条件一律写 JSON：`{ 字段: 值 }` 是等值，`{ 字段: { $gt: 值 } }` 是比较；改数据记得先查一遍，`updateOne/deleteOne` 只动第一条。



<!-- ============ 文档分隔线：047-mongodb/003-AggregationPipeline.md ============ -->


## 0. 一句话理解

> 聚合管道就是把数据处理拆成一个个"管道阶段"，数据像水一样流过去：先过滤、再分组、再排序、再取字段——每个阶段只做一件事。

## 1. 为什么需要聚合管道

SQL 里一句 `GROUP BY` 就能统计，文档模型没有这个语法，所以 MongoDB 提供 `aggregate()`。它的参数是一个数组，数组里的每个元素就是一个"处理站"。

## 2. 第一个聚合：按班级统计平均分

先准备数据：

```javascript
db.scores.insertMany([
  { student: "小明", class: "A班", math: 92, english: 88 },
  { student: "小红", class: "A班", math: 85, english: 95 },
  { student: "小刚", class: "B班", math: 70, english: 75 },
  { student: "小丽", class: "B班", math: 90, english: 82 }
])
```

然后执行：

```javascript
db.scores.aggregate([
  { $match: { math: { $gte: 80 } } },
  {
    $group: {
      _id: "$class",
      avgMath: { $avg: "$math" },
      total: { $sum: 1 }
    }
  },
  { $sort: { avgMath: -1 } }
])
```

**讲解：**

1. `$match` 是"过滤器"：只留下 math 大于等于 80 的文档，越早过滤数据越少，后续阶段越快。
2. `$group` 是"分组统计"：`_id: "$class"` 表示按班级分组（`$字段名` 表示取该字段的值）；`$avg: "$math"` 求数学平均分；`$sum: 1` 每来一条加 1，就是计数。
3. `$sort` 按平均分降序输出。
4. 输出结果形如：`[{ _id: "A班", avgMath: 88.5, total: 2 }, ...]`。

## 3. 常用管道阶段速查

| 阶段 | 作用 | 类似 SQL |
| --- | --- | --- |
| `$match` | 过滤文档 | WHERE |
| `$project` | 选择/生成字段 | SELECT |
| `$group` | 分组聚合 | GROUP BY |
| `$sort` | 排序 | ORDER BY |
| `$limit` / `$skip` | 分页 | LIMIT / OFFSET |
| `$unwind` | 把数组拆成多行 | 展开一对多 |
| `$lookup` | 跨集合关联 | LEFT JOIN |
| `$addFields` | 新增计算字段 | 计算列 |

## 4. 实战一：$project 计算字段

```javascript
db.scores.aggregate([
  {
    $project: {
      student: 1,
      class: 1,
      total: { $add: ["$math", "$english"] },
      pass: { $gte: ["$math", 60] }
    }
  }
])
```

**讲解：**

1. `$project` 控制输出字段：`1` 表示保留，不写则丢弃（`_id` 默认保留）。
2. `$add` 是算术表达式，把数学和英语相加生成 `total` 字段。
3. `$gte` 比较表达式返回布尔值，生成 `pass` 字段——聚合表达式里运算符都写成数组形式 `[参数1, 参数2]`。

## 5. 实战二：$unwind 拆数组

```javascript
db.orders.insertOne({
  orderNo: "A001",
  items: ["鼠标", "键盘", "显示器"]
})

db.orders.aggregate([
  { $unwind: "$items" },
  { $group: { _id: "$items", count: { $sum: 1 } } },
  { $sort: { count: -1 } }
])
```

**讲解：**

1. `$unwind: "$items"` 把一条含 3 个元素的订单拆成 3 条记录，每条含一个 `items` 值。
2. 拆开后再 `$group` 按商品名统计，就能得到"哪个商品被买得多"。
3. 如果数组字段不存在或为空，`$unwind` 默认丢弃该文档；传 `{ preserveNullAndEmptyArrays: true }` 可保留。

## 6. 实战三：$lookup 跨集合关联

```javascript
db.authors.insertOne({ _id: 1, name: "张三" })
db.books.insertMany([
  { title: "书一", authorId: 1 },
  { title: "书二", authorId: 1 }
])

db.books.aggregate([
  {
    $lookup: {
      from: "authors",
      localField: "authorId",
      foreignField: "_id",
      as: "author"
    }
  }
])
```

**讲解：**

1. `from` 是要关联的集合名，`localField` 是本集合的关联字段，`foreignField` 是对方集合的关联字段。
2. 结果会在每条书文档上多出一个 `author` 数组（匹配到多条时数组里有多个元素）。
3. `$lookup` 相当于 LEFT JOIN，但性能开销较大；查询频繁的一对多关系优先考虑"内嵌"而不是关联。

## 7. 性能注意事项

- 尽量把 `$match` 放在最前面，先缩小数据量再分组；
- `$lookup` 的关联字段要建索引；
- 分组字段（`$group` 的 `_id`）建索引也能显著提速；
- 聚合结果很大时加 `$limit`，或用 `allowDiskUse: true` 允许磁盘临时文件。

## 8. 动手试试

1. 往 `scores` 里再插入几条数据，统计"每个学生的两科总分"，按总分降序输出前 3 名。
2. 统计每个班级的英语最高分（`$max`）与最低分（`$min`）。
3. 用 `$unwind + $group` 统计 `courses` 数组里出现次数最多的课程。

## 9. 一句话记住

> 聚合 = 管道里串过滤、分组、投影、排序；`$match` 尽量放最前，`$group` 的 `_id` 决定"按什么分组"。



<!-- ============ 文档分隔线：047-mongodb/004-IndexPerformance.md ============ -->


## 0. 一句话理解

> 索引就是数据库给字段做的"目录"：没有目录就一页页翻（全表扫描），有了目录就能直接翻到目标页。索引让查询变快，但每次写入都要维护目录，所以不能乱建。

## 1. 查看与创建索引

```javascript
// 查看现有索引
db.students.getIndexes()

// 给 age 建普通索引（1 升序，-1 降序，对等值查询无区别）
db.students.createIndex({ age: 1 })

// 唯一索引：name 不允许重复
db.students.createIndex({ name: 1 }, { unique: true })

// 复合索引：先按 class，再按 age
db.students.createIndex({ class: 1, age: -1 })
```

**讲解：**

1. `getIndexes()` 会看到默认的 `_id` 索引——主键索引由 MongoDB 自动创建。
2. `createIndex({ age: 1 })` 的 `1/-1` 只影响排序方向，等值查询两种都能用。
3. `unique: true` 用来保证字段唯一，插入重复值会报错，适合用户名、订单号。
4. 复合索引的字段顺序很重要：`{ class: 1, age: -1 }` 能服务"按班级查"和"按班级+年龄查"，但单独按年龄查用不上它。

## 2. 用 explain 读查询计划

```javascript
db.students.find({ age: { $gt: 18 } }).explain("executionStats")
```

**讲解：**

1. `explain("executionStats")` 返回查询计划，重点看三个字段：
   - `winningPlan.stage`：`COLLSCAN` 表示全表扫描，`IXSCAN` 表示走了索引；
   - `totalDocsExamined`：实际翻看了多少条文档，越接近返回条数越好；
   - `executionTimeMillis`：本次查询耗时。
2. 练习：给 `age` 建索引前后各 explain 一次，对比 `COLLSCAN` 与 `IXSCAN` 的 `totalDocsExamined`。

## 3. 索引的代价与取舍

| 情况 | 建议 |
| --- | --- |
| 查询条件字段 | 建索引 |
| 排序字段 | 建索引（避免内存排序） |
| 区分度低的字段（如性别） | 不建索引，扫描率太高 |
| 几乎不查的字段 | 不建索引 |
| 写入密集的集合 | 控制索引数量，写入时每条索引都要更新 |
| 超大文本字段 | 用文本索引（`text`）而非普通索引 |

```javascript
// 稀疏索引：只为存在该字段的文档建索引
db.students.createIndex({ phone: 1 }, { sparse: true })

// TTL 索引：字段超过 3600 秒自动删除文档（日志、会话场景）
db.sessions.createIndex({ createdAt: 1 }, { expireAfterSeconds: 3600 })
```

**讲解：**

1. `sparse: true` 适合"很多文档没有这个字段"的情况，减少索引体积。
2. `expireAfterSeconds` 是 MongoDB 的定时过期机制，后台约每 60 秒清理一次，适合验证码、临时会话。

## 4. 查询性能自查清单

1. 先用 `explain` 确认是否 `COLLSCAN`；
2. 检查查询条件与排序是否被同一个复合索引覆盖；
3. 避免对索引字段使用 `$where`、正则前缀以外的表达式；
4. 大结果集用游标分批处理，不要一次 `find({})` 全量拉取；
5. 生产环境用 MongoDB Compass 的索引建议或 `$indexStats` 观察索引使用率。

## 5. 动手试试

1. 造 10 万条测试数据（可用 `insertMany` + 循环），对比 `age` 有/无索引时的查询耗时。
2. 给 `{ class: 1, age: -1 }` 建复合索引，测试三种查询：只按 class、按 class+age、只按 age，观察哪个没走索引。
3. 给订单集合加 TTL 索引，插入一条 `createdAt` 为过去时间的文档，等待清理（可把 `expireAfterSeconds` 设小）。

## 6. 一句话记住

> 查询慢先跑 `explain`：看到 `COLLSCAN` 就建索引；索引不是越多越好，查询多、区分度高的字段才值得建。



<!-- ============ 文档分隔线：047-mongodb/005-SchemaDesignEnterprise.md ============ -->


## 0. 一句话理解

> 建模的核心只有一道选择题：这条数据是"和父文档一起读"还是"独立存在、被多处引用"？前者内嵌，后者引用——选错是 MongoDB 项目最常见的性能事故来源。

## 1. 内嵌（Embedding）

```javascript
// 内嵌：订单直接包含地址，读订单时一次拿到全部
db.orders.insertOne({
  orderNo: "A001",
  user: "小明",
  items: [
    { sku: "m-001", name: "鼠标", price: 99, qty: 2 },
    { sku: "k-002", name: "键盘", price: 299, qty: 1 }
  ],
  total: 497
})
```

**讲解：**

1. 订单条目与订单几乎总是"一起读、一起写"，内嵌让一次查询拿到整份订单，不需要 JOIN。
2. 数组大小有上限（单文档 16MB），购物车、订单明细这类有限条目非常适合内嵌。
3. 内嵌的代价：条目更新必须走整份文档的更新，且无法单独查询"所有订单里的鼠标"（需要聚合 `$unwind`）。

## 2. 引用（Referencing）

```javascript
// 商品被所有订单共享，独立成集合，订单里只存 _id 或冗余快照
db.products.insertOne({ _id: "m-001", name: "鼠标", price: 99 })

db.orders.insertOne({
  orderNo: "A002",
  user: "小红",
  items: [{ productId: "m-001", name: "鼠标", price: 99, qty: 1 }]
})
```

**讲解：**

1. 商品是"主数据"，被成千上万订单引用，必须独立集合；订单条目里既存 `productId`，也冗余存 `name/price` 快照。
2. 快照的意义：商品改名、涨价不影响历史订单展示；这是"读时一致性"的工程取舍。
3. 需要跨集合组合数据时用 `$lookup`，但高频查询路径应尽量通过冗余设计避免 `$lookup`。

## 3. 选择决策表

| 场景 | 推荐 |
| --- | --- |
| 订单 + 明细，一起读一起写 | 内嵌 |
| 用户 + 地址簿，地址独立管理 | 引用（或内嵌数组，看规模） |
| 商品 + 订单，共享主数据 | 引用 + 快照 |
| 评论 + 文章，评论无限增长 | 引用（文章内嵌最近 3 条 + 评论集合） |
| 日志、事件流 | 独立集合 + TTL 索引 |
| 标签、分类 | 内嵌数组 |

## 4. 常用建模模式

1. **子集模式**：文章详情页内嵌"最近评论"，完整评论放独立集合，兼顾速度与无限增长。
2. **桶模式**：物联网传感器按"每小时一条桶文档"聚合 60 条采样，减少文档数量与索引体积。
3. **版本字段模式**：文档加 `schemaVersion` 字段，未来结构变更时按版本迁移。
4. **扩展引用模式**：把引用字段（如作者名）冗余到文档里，避免高频 `$lookup`。

## 5. 生产落地：副本集与事务

```yaml
# docker-compose.yml 片段：一主两从副本集
services:
  mongo-primary:
    image: mongo:8.3
    command: ["mongod", "--replSet", "rs0"]
  mongo-secondary-1:
    image: mongo:8.3
    command: ["mongod", "--replSet", "rs0"]
  mongo-secondary-2:
    image: mongo:8.3
    command: ["mongod", "--replSet", "rs0"]
```

**讲解：**

1. 副本集是 MongoDB 高可用的基本单位：主节点写、从节点同步，主节点故障时自动选举新主。
2. 生产环境至少要一主两从（3 个数据副本），单机 `mongod` 只适合学习。
3. MongoDB 4.0+ 支持多文档事务，但事务有性能成本；能用单文档原子更新解决的（`$inc`、`$set` 本身就是原子的）就不要开事务。

```javascript
// 事务示例：转账（需要副本集环境）
const session = db.getMongo().startSession()
session.startTransaction()
try {
  session.getDatabase("bank").accounts.updateOne(
    { user: "A" }, { $inc: { balance: -100 } }, { session }
  )
  session.getDatabase("bank").accounts.updateOne(
    { user: "B" }, { $inc: { balance: 100 } }, { session }
  )
  session.commitTransaction()
} catch (err) {
  session.abortTransaction()
  throw err
} finally {
  session.endSession()
}
```

**讲解：**

1. `startSession()` 创建会话，`startTransaction()` 开启事务；所有读写都要显式传 `{ session }`，否则不在事务内。
2. 全部成功 `commitTransaction()` 提交；任何一步抛错 `abortTransaction()` 回滚，保证 A 扣钱与 B 加钱同时生效或同时取消。
3. `finally` 里 `endSession()` 释放会话资源，防止连接泄漏。

## 6. 动手试试

1. 设计一个"博客"模型：文章、作者、评论。用内嵌还是引用？写出来并说明理由。
2. 用 Docker 起一个三节点副本集（或使用官方文档的单机副本集初始化），执行上面的转账事务。
3. 为你的模型写一份"读写路径表"：每个页面读哪些集合、需要几次查询。

## 7. 一句话记住

> 一起读一起写的就内嵌，被共享、被独立管理的就引用；高频路径用快照换速度，跨文档强一致才开事务。
