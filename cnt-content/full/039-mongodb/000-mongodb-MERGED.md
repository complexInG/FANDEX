---
order: 10
title: mongodb 模块文档合集
module: 'mongodb'
category: 数据库
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-30'
related: []
prerequisites: []
---

<!-- ============================================================ mongodb/001-MongoDBOverviewQuickStart ============================================================ -->

## 0. 五分钟跑起 MongoDB（先读这里）

> 学习目标：不管懂不懂概念，先让 MongoDB 跑起来，并插入、查询到第一条数据。

一句话理解：**MongoDB 是"存文档"的数据库——每条数据是一个 JSON 风格的文档，像一张张可以随意增减字段的卡片，而不是必须对齐列名的表格。**

### 0.1 用 Docker 启动（30 秒）

先确认本机已安装 Docker（参考 `getting-started/027-DockerInstall`），然后执行：

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

<!-- ============================================================ mongodb/002-CRUDOperations ============================================================ -->

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

<!-- ============================================================ mongodb/003-AggregationPipeline ============================================================ -->

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

<!-- ============================================================ mongodb/004-IndexPerformance ============================================================ -->

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

<!-- ============================================================ mongodb/005-SchemaDesignEnterprise ============================================================ -->

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

<!-- ============================================================ mongodb/006-TransactionSession ============================================================ -->

## 0. 为什么 NoSQL 也需要事务（先读这里）

> 学习目标：说清单文档原子性与多文档事务的边界；会用会话开启、提交、回滚一个多文档事务；理解 writeConcern / readConcern 与 majority 的含义；知道事务的限制清单，并在转账场景写出带重试的完整代码。

很多教程说 MongoDB "为了性能放弃了事务"，这句话只对了一半：**单文档操作天然原子**，一次 `$inc`、一次 `$set` 在服务器端一次性生效，不存在"写了一半"的中间态。所以大量看似需要事务的场景，可以通过建模（内嵌进同一文档，见 005 建模篇）直接消掉，这正是 MongoDB 高性能的来源之一。

业务总有绕不开的跨文档时刻：转账要"扣 A 加 B"同时生效；下单要"建订单、扣库存、加积分"要么全成、要么全不成。于是 MongoDB 4.0 在副本集上引入了多文档 ACID 事务，4.2 起扩展到分片集群。本篇依次回答四个问题：会话是什么、事务怎么写、限制在哪里、一致性怎么读。

## 1. 单文档原子性：很多"事务"其实是建模问题

```javascript
// 秒杀扣库存：把"库存"与"购买记录"内嵌在同一文档，一次原子更新搞定
db.getSiblingDB("shop").flashSales.updateOne(
  { sku: "m-001", stock: { $gt: 0 } },                  // 条件更新：还有库存才允许扣减
  {
    $inc: { stock: -1 },                                // 原子扣减 1 件
    $push: { buyers: { user: "userA", at: new Date() } } // 同步记录买家
  }
)
```

**讲解：**

1. `updateOne` 的"条件 + 修改"在服务器端原子执行：即使一百个请求并发扣减，`stock` 最终一定等于初始值减成功次数；条件里有 `stock > 0`，永远不会扣成负数。
2. 这就是"用建模消灭事务"：数据能放进一个文档，就不需要跨文档协调；005 建模篇"内嵌优先"的原则正是为这一节铺路。
3. 边界也很清楚：一旦数据必须跨集合、跨文档（转账的 A 和 B、订单与库存分表存放），单文档原子性就无能为力了，本篇主角登场。

## 2. 会话（Client Session）：事务与因果一致性的载体

```javascript
// 会话：一组操作的"逻辑上下文"，事务与因果一致性都挂在它身上
const session = db.getMongo().startSession({ causalConsistency: true }) // 默认开启

const bankDb = session.getDatabase("bank")
bankDb.accounts.updateOne({ _id: "A" }, { $inc: { balance: 50 } }) // 经过会话写入

session.getOperationTime() // 会话记录的逻辑时间戳，因果序的"书签"

session.endSession()       // 用完必须释放，否则占用会话资源
```

**讲解：**

1. 会话是客户端与服务器共同维护的逻辑上下文：所有多文档事务必须在会话内执行；可重试写、因果一致性等能力也以会话为单位。
2. 因果一致性：会话记住自己最近一次操作产生的 `operationTime`，之后的读会要求目标节点至少复制到这个时间点。效果是"自己写的自己一定读得到"；即使主从切换，读到的数据也不倒退。
3. 没有会话的普通读没有这种保证："写完立刻读"在极端情况下可能读到旧值，因果一致会话正是这类需求的廉价解法。

## 3. 第一个多文档事务（mongosh 实操）

事务需要副本集或分片集群，单机 mongod 不支持多文档事务；环境搭建见第 7 节与 007 的动手部分。

```javascript
use bank

// 准备两个账户
db.accounts.insertMany([
  { _id: "A", name: "小明", balance: 1000 },
  { _id: "B", name: "小红", balance: 500 }
])

// 开启事务：快照读 + 多数派写
const session = db.getMongo().startSession()
session.startTransaction({
  readConcern: { level: "snapshot" },  // 事务内多次读看到同一版本
  writeConcern: { w: "majority" }      // 提交需获得多数派确认，故障切换不丢
})

try {
  const accounts = session.getDatabase("bank").accounts
  accounts.updateOne({ _id: "A" }, { $inc: { balance: -100 } }, { session }) // 每个操作都必须带 session
  accounts.updateOne({ _id: "B" }, { $inc: { balance: 100 } }, { session })

  // 业务校验：余额不允许为负
  const a = accounts.findOne({ _id: "A" }, { session })
  if (a.balance < 0) { throw new Error("余额不足") }

  session.commitTransaction()   // 全部成功才提交
} catch (err) {
  session.abortTransaction()    // 任一步失败，整体回滚
  print("事务已回滚：" + err.message)
} finally {
  session.endSession()          // 释放会话
}
```

**讲解：**

1. `startTransaction` 的两个参数几乎总是这一套：`snapshot` 读 + `majority` 写，在多数派确认的快照上执行、以多数派确认提交。
2. 事务里的每个读写都必须显式传 `{ session }`，漏传等于在事务外操作；事务内的读固定走主节点。
3. 提交之前，其他会话看不到你的任何修改；提交之后，其他会话看到的是"整体生效"——A 少 100 与 B 多 100 不会出现半个状态。
4. `abortTransaction` 之后两个余额原样不动，这就是原子性；另开窗口在提交前后各查一次数据，可直观感受隔离。

## 4. 错误分类与重试：生产级写法

事务有两类典型的"瞬时错误"，处理方式完全不同：

- `TransientTransactionError`：写冲突、主节点切换等，事务没有真正完成，**整体重开**即可。
- `UnknownTransactionCommitResult`：提交结果未知，事务可能已提交，**只重试提交**，不要重开。

```javascript
// mongosh 手写版：帮助理解重试语义
function transfer(fromId, toId, amount) {
  const session = db.getMongo().startSession()
  try {
    let done = false
    while (!done) {
      session.startTransaction({
        readConcern: { level: "snapshot" },
        writeConcern: { w: "majority" }
      })
      try {
        const accounts = session.getDatabase("bank").accounts
        accounts.updateOne({ _id: fromId }, { $inc: { balance: -amount } }, { session })
        accounts.updateOne({ _id: toId }, { $inc: { balance: amount } }, { session })

        // 提交阶段：结果未知时只重试提交
        while (true) {
          try {
            session.commitTransaction()
            done = true
            break
          } catch (e) {
            if (e.hasErrorLabel && e.hasErrorLabel("UnknownTransactionCommitResult")) {
              print("提交结果未知，重试提交")
              continue
            }
            throw e
          }
        }
      } catch (e) {
        // 事务体阶段的瞬时错误：整体重开事务
        if (e.hasErrorLabel && e.hasErrorLabel("TransientTransactionError")) {
          print("瞬时冲突，重开事务：" + e.message)
          continue
        }
        throw e // 业务错误直接放弃，不重试
      }
    }
  } finally {
    session.endSession() // 未提交的事务会随会话结束自动中止
  }
}
```

**讲解：**

1. 两层循环对应两类错误：内层只重试 `commit`，外层重开整个事务；判断依据是错误对象上的标签，不要按错误码字符串猜。生产代码应优先使用驱动的 `withTransaction`，它自动处理这两类重试。
2. 业务校验抛出的错误没有瞬时标签，直接上抛放弃——重试解决不了"钱不够"。
3. `finally` 里 `endSession()` 兜底释放资源；若事务还在活动中，会话结束会隐式中止它。

## 5. 事务的限制清单：先知道边界再设计

| 限制 | 说明 |
| --- | --- |
| 运行环境 | 必须是副本集或分片集群，单机 mongod 不支持多文档事务 |
| 默认 60 秒 | `transactionLifetimeLimitSeconds` 默认 60，超时自动中止；长事务还会拖累 oplog 与缓存 |
| oplog 16MB | 整个事务提交后作为一条 oplog 记录写入，总大小超 16MB 直接失败，大批量写不要塞进事务 |
| 会话绑定 | 一个会话同一时刻只能有一个活动事务；事务内的读固定走主节点 |
| 集合与索引 | 早期版本不允许在事务内创建集合与索引（4.4 起放开）；实践仍是"提前建好，事务只做读写"，完整限制以官方文档为准 |
| 写冲突 | 两个事务并发修改同一文档会触发 WriteConflict，后者需整体重试；事务范围越小，冲突概率越低 |
| 吞吐成本 | 事务持有锁与快照，吞吐显著低于普通写，能不用就不用 |

决策顺序：**单文档能解决就内嵌；不需要实时强一致就异步对账补偿；真的跨文档强一致才开事务，并且把事务做小、做短。**

## 6. writeConcern 与 readConcern：确定性从哪来

**写关注 writeConcern** 回答"这次写要多稳才算成功"：

```javascript
// 订单写入：多数派确认 + 落 journal + 5 秒超时
db.orders.insertOne(
  { orderNo: "C001", total: 199 },
  { writeConcern: { w: "majority", j: true, wtimeout: 5000 } }
)
```

| writeConcern | 语义 |
| --- | --- |
| `w: 1` | 主节点确认即返回，最快；主节点宕机时最近的写可能丢失 |
| `w: "majority"` | 多数派节点确认，故障切换后已确认的写不会丢 |
| `j: true` + `wtimeout` | 写入磁盘 journal 后才确认，防掉电丢数据；`wtimeout` 是等待确认的超时毫秒数，超时报错而不是无限挂起 |

**读关注 readConcern** 回答"我读到的数据有多可信"：

| readConcern | 语义 |
| --- | --- |
| `local` | 返回本节点可见的最新数据；可能尚未获得多数派确认，故障切换后可能"回滚" |
| `majority` | 只返回已获多数派确认的数据，选举后不会消失 |
| `linearizable` | 线性一致读，最强也最贵；只能配合唯一索引（如 `_id`）的等值查询，且要求对应写使用 majority 写关注 |
| `snapshot` | 一致性快照，事务内默认，保证多次读看到同一版本 |

**组合建议：**

| 场景 | 读 | 写 |
| --- | --- | --- |
| 普通内容浏览 | local（默认） | w: 1 |
| 订单 / 账务 | majority | majority（可加 j: true） |
| 单文档强一致读（如秒杀余量） | linearizable | majority |
| 事务内部 | snapshot（默认） | majority |

写用 `majority`，已提交的写不会因选举丢失；读用 `majority`，读到的版本一定是多数派确认过的——单文档上这就是线性一致的读语义；跨文档的整体一致需要事务 + `snapshot`；"读自己的写"用因果一致会话即可，代价小得多。

## 7. 实战：转账不变量验证

```javascript
use bank

// 1. 准备账户
db.accounts.drop()
db.accounts.insertMany([
  { _id: "A", name: "小明", balance: 1000 },
  { _id: "B", name: "小红", balance: 500 }
])

// 2. 定义不变量：A + B 的总余额恒为 1500
const total = () =>
  db.accounts.aggregate([{ $group: { _id: null, total: { $sum: "$balance" } } }]).toArray()[0].total

// 3. 正常转账 200（复用第 4 节的 transfer 函数）
transfer("A", "B", 200)
print("正常转账后总余额：" + total())   // 1500

// 4. 余额不足的转账：业务失败，分文不动
transfer("A", "B", 5000)
print("失败转账后总余额：" + total())   // 仍是 1500

// 5. 回滚验证：两笔更新都执行了，但提交前模拟下游崩溃
const s = db.getMongo().startSession()
try {
  s.startTransaction({ writeConcern: { w: "majority" } })
  s.getDatabase("bank").accounts.updateOne({ _id: "A" }, { $inc: { balance: -100 } }, { session: s })
  s.getDatabase("bank").accounts.updateOne({ _id: "B" }, { $inc: { balance: 100 } }, { session: s })
  throw new Error("模拟下游服务崩溃")    // 此时尚未提交
} catch (e) {
  s.abortTransaction()                   // 显式回滚
  print("已回滚：" + e.message)
} finally {
  s.endSession()
}

print("回滚后总余额：" + total())        // 仍是 1500
db.accounts.find().sort({ _id: 1 })      // A: 800，B: 700
```

**讲解：**

1. 不变量（总余额恒定）是验证事务正确性最简单的尺子：成功、失败、回滚都不该破坏它。
2. 第 5 步刻意在两笔更新都执行之后才抛错——只要没提交，事务内的写对其他会话完全不可见，abort 后连痕迹都没有。
3. 脚本需在副本集上运行；一条命令即可把单机变成单节点副本集：

```bash
# 单机副本集：一个 mongod 即可练事务
mkdir -p ~/mongo-rs0
mongod --dbpath ~/mongo-rs0 --replSet rs0 --port 27017 --bind_ip 127.0.0.1
```

```javascript
// 另开终端初始化，members 出现 PRIMARY 即可
rs.initiate({ _id: "rs0", members: [ { _id: 0, host: "127.0.0.1:27017" } ] })
```

## 小结与延伸

> 单文档原子性是免费的，多文档事务是收费的；先用建模消灭事务，再用最短的持锁时间使用事务。

收工自查清单：

1. 会话是事务与因果一致性的载体，用完 `endSession()`。
2. 事务默认搭配 `snapshot` 读 + `majority` 写，每个操作显式带 `session`。
3. 两类瞬时错误：`TransientTransactionError` 重开事务，`UnknownTransactionCommitResult` 只重试提交；生产用驱动的 `withTransaction`。
4. 硬限制记三条：默认 60 秒、oplog 记录 16MB、必须副本集环境。
5. 读写的确定性来自 readConcern / writeConcern 的组合，账务类场景用 majority + majority。

延伸阅读：CRUD 前置见 `002-CRUDOperations`；"内嵌优先"建模决策见 `005-SchemaDesignEnterprise`；事务运行环境（副本集与分片）见 007。官方文档关键词：Transactions、Causal Consistency、Read Concern、Write Concern，参数与默认值以官方文档为准。

<!-- ============================================================ mongodb/007-ReplicaSetSharding ============================================================ -->

## 0. 从单机到分片：演进路线（先读这里）

> 学习目标：复述副本集的三大机制（oplog、心跳、选举）；区分 Priority / Hidden / Delayed / Arbiter 四种成员角色；按业务场景组合 readPreference / readConcern / writeConcern；独立完成单机副本集搭建，并说出 shard key 选型的四条原则。

单机 MongoDB 是绝大多数人的起点，但它有两个天花板：**机器坏了服务就停**（可用性），**一台机器装不下、写不动**（容量与吞吐）。副本集解决第一个问题，分片集群解决第二个。这一篇先拆开副本集看内部机制，再动手搭环境，最后进入分片的世界。

## 1. 三级演进：什么时候需要什么架构

| 阶段 | 解决什么 | 代价 |
| --- | --- | --- |
| 单机 mongod | 学习、原型、内部小工具 | 无高可用，故障即停服 |
| 副本集（一主多从） | 高可用、读扩展、容灾备份 | 写仍是单点；数据量受单机限制 |
| 分片集群 | 写吞吐与数据量的水平扩展 | 组件变多，shard key 选型不可轻易反悔，跨分片查询与事务更贵 |

判断口诀：**先上副本集保可用；当单机磁盘装不下、写吞吐到顶、热点数据撑不进内存时，才考虑分片。** 分片引入的复杂度（路由、再均衡、跨分片聚合）是实打实的运维成本，不要为"以后可能用上"提前分片。

## 2. 副本集原理：oplog、心跳与选举

副本集由一个主节点（PRIMARY）与若干从节点（SECONDARY）组成：所有写都进主节点，主节点把操作记录进 **oplog**（操作日志，一个固定大小的环形集合 `local.oplog.rs`），从节点持续拉取 oplog 并重放，最终达到与主节点一致。

```javascript
// 查看最近的 oplog 条目（local 库只读，绝不要往里写）
db.getSiblingDB("local").oplog.rs.find().sort({ $natural: -1 }).limit(3)

// 两条常用体检命令
rs.printReplicationInfo()           // oplog 窗口大小：能"回放"多长时间的操作
rs.printSecondaryReplicationInfo()  // 各从节点落后主节点多少
```

**故障检测与切换：**

1. **心跳**：成员之间默认每 2 秒互发心跳，用于感知彼此存活。
2. **选举**：主节点失联后，有投票权的成员发起选举，获得**多数派**票数的节点成为新主；默认约 10 秒完成切换（`electionTimeoutMillis` 可调）。因此副本集投票节点数必须是奇数——偶数票等于浪费一张票。
3. 成员数量：一个副本集最多约 50 个成员，其中只有 7 个拥有投票权；生产常用 3 节点或 5 节点。

```javascript
rs.status()  // 成员健康、角色、延迟的一览表，排障第一站
rs.conf()    // 当前配置：成员列表、优先级、隐藏、延迟等
```

## 3. 成员角色：Priority、Hidden、Delayed 与 Arbiter

| 角色 | 关键配置 | 用途 |
| --- | --- | --- |
| 普通成员 | 默认 | 参与投票、可被选为主、可承接读流量 |
| 零优先级 | `priority: 0` | 永不竞选主节点，只做数据冗余与读 |
| 隐藏节点 | `hidden: true`（需配 priority: 0） | 对客户端读路由不可见，专供备份、报表 |
| 延迟节点 | `secondaryDelaySecs`（如 3600） | 滞后一段时间重放 oplog，误删数据后的"后悔药" |
| 仲裁节点 | 不存数据，只投票 | 官方更推荐用带数据的奇数节点替代，新版本中已不推荐，以官方文档为准 |

```javascript
// 把 2 号成员设为"隐藏 + 零优先级"（例如专跑 nightly 备份）
cfg = rs.conf()
cfg.members[2].priority = 0
cfg.members[2].hidden = true
rs.reconfig(cfg)
```

**讲解：**

1. `priority` 越高越容易当选；把硬件最好、网络最居中的节点设为高优先级，其余设 0，可以让主节点稳定落在指定机器上。
2. 延迟节点的价值：`DROP TABLE` 这类误操作会立刻同步到所有从节点，只有延迟节点还留着"一小时前"的数据。
3. 改配置用 `rs.reconfig(cfg)`，生产上改投票成员数量等敏感项时注意官方文档对多数派的要求。

## 4. 读写语义三件套：readPreference / readConcern / writeConcern

三者各管一件事：**读偏好管"读谁"，读关注管"读到的多可信"，写关注管"写多稳才算成功"**（readConcern 与 writeConcern 的细节语义在 006 第 6 节已展开，这里补上读偏好与组合）。

readPreference 五个取值：`primary`（只读主）、`primaryPreferred`（主优先）、`secondary`（只读从）、`secondaryPreferred`（从优先）、`nearest`（就近）。读从节点时建议配 `maxStalenessSeconds` 限制从节点最大延迟（下限 90 秒，以官方文档为准）。

```javascript
// mongosh 会话级设置读偏好（也可以写在连接串 ?readPreference=... 里）
db.getMongo().setReadPref("secondaryPreferred")

// 单次查询同时指定读关注与读偏好（mongosh 游标方法）
db.orders.find({ status: "paid" }).readConcern("majority").readPref("secondaryPreferred")

// 写入时指定写关注：多数派 + journal + 5 秒超时
db.orders.insertOne(
  { orderNo: "C001" },
  { writeConcern: { w: "majority", j: true, wtimeout: 5000 } }
)
```

**组合建议：**

| 场景 | readPreference | readConcern | writeConcern |
| --- | --- | --- | --- |
| 订单写入 | primary（默认） | - | majority |
| 报表、数据导出 | secondaryPreferred | local | - |
| 金融单点强一致读 | primary | linearizable | majority |
| "读自己刚写的" | 任意 + 因果一致会话 | majority | majority |

**讲解：** 读从节点不是免费的——复制延迟意味着可能读到旧数据；报表能容忍，购物车不能。把"哪些读容忍旧数据"想清楚，读偏好才有答案。

## 5. 动手：本机搭建副本集

### 方式一：单机副本集（最省事，学习推荐）

```bash
# 一个 mongod 就能变成副本集，事务、变更流等特性都能练
mkdir -p ~/mongo-rs0
mongod --dbpath ~/mongo-rs0 --replSet rs0 --port 27017 --bind_ip 127.0.0.1
```

```javascript
// 另开终端，初始化副本集
rs.initiate({ _id: "rs0", members: [ { _id: 0, host: "127.0.0.1:27017" } ] })
rs.status()  // 稍等几秒，members 里出现 PRIMARY 即成功
```

### 方式二：Docker 一主两从

```yaml
# docker-compose.yml：同一网络里跑三个 mongod
services:
  mongo1:
    image: mongo:8.0
    command: ["mongod", "--replSet", "rs0", "--bind_ip_all"]
    ports: ["30001:27017"]
    networks: [mongonet]
  mongo2:
    image: mongo:8.0
    command: ["mongod", "--replSet", "rs0", "--bind_ip_all"]
    ports: ["30002:27017"]
    networks: [mongonet]
  mongo3:
    image: mongo:8.0
    command: ["mongod", "--replSet", "rs0", "--bind_ip_all"]
    ports: ["30003:27017"]
    networks: [mongonet]
networks:
  mongonet: {}
```

```bash
docker compose up -d
# 在 mongo1 容器里初始化三成员副本集（容器间用容器名互相发现）
docker compose exec mongo1 mongosh --eval '
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongo1:27017" },
    { _id: 1, host: "mongo2:27017" },
    { _id: 2, host: "mongo3:27017" }
  ]
})'
```

**讲解：**

1. rs 配置里写的是容器名，因为成员之间走容器网络；从宿主机连接时加 `?directConnection=true` 直连单个节点做管理，或在 `/etc/hosts` 里把 mongo1/2/3 映射到 127.0.0.1。
2. 生产副本集必须配 keyFile 内部认证（见安全篇 008）与 majority 写关注，本例为了演示省略了认证。
3. 搭好后把 006 的转账事务跑一遍：单机 mongod 会直接报错，副本集上则正常提交——事务的第一道门槛就是环境。

## 6. 分片集群：mongos、config server 与 shard

分片集群由三类角色组成，理解数据流就理解了架构：

1. **mongos（路由）**：无状态查询路由器。应用只连 mongos；它根据元数据把请求发给对应 shard，再合并结果返回。
2. **config server（配置副本集，CSRS）**：保存"哪段数据在哪个 shard"的元数据；balancer 也在其主节点上运行（新版本行为，旧版本由 mongos 协调，以官方文档为准）。
3. **shard（分片）**：每个 shard 本身就是一个完整的副本集，复用上一节的高可用机制。

数据流：带 shard key 的查询走**定点路由**（只碰一个 shard）；不带 shard key 的查询是 **scatter-gather**（发到所有 shard 再汇总），成本随 shard 数量线性上涨——这就是 shard key 要贴合查询的原因。分片集合上的多文档事务、跨 shard 聚合同理，都比单 shard 贵。

## 7. shard key 选型：决定分片成败的一步

```javascript
use shop
// 新版本中 shardCollection 会隐式开启库的分片；显式 enableSharding 在旧版本必需
sh.enableSharding("shop")

// 哈希分片：写入均匀，适合等值查询多的场景
sh.shardCollection("shop.orders", { userId: "hashed" })

// 复合键范围分片：需先建索引，适合"按用户查订单"这类模式
db.orders.createIndex({ userId: 1, orderId: 1 })
sh.shardCollection("shop.orders", { userId: 1, orderId: 1 })
```

| 策略 | 写入分布 | 等值点查 | 范围查询 | 适用 |
| --- | --- | --- | --- | --- |
| 单调递增键 + 范围（如 _id、时间戳） | 差：永远写最后一段，单 shard 热点 | 好 | 好 | 几乎不该用 |
| 哈希键（hashed） | 好 | 好 | 差（哈希打散了顺序） | 写多、按 key 等值查 |
| 复合键范围（如 userId + orderId） | 好（userId 足够分散时） | 好 | 按 userId 的范围查询好 | 多数业务首选 |

**四条选型原则：**

1. **基数要高**：userId 有千万个取值，status 只有三个，前者才撑得起几百个 chunk。
2. **避免单调递增**：ObjectId、时间戳在范围分片下全部落在最后一个 chunk（热点）；要么用 hashed，要么把无序字段放在最前面。
3. **贴合查询**：最高频的查询必须带上 shard key 前缀，否则退化为 scatter-gather。
4. **想好不可逆**：shard key 一经选定，修改代价很高（新版本支持在线 resharding，但条件多、耗时长，以官方文档为准），选型前把读写模式画出来再决定。

补充：地域合规、冷热分层等需求可用 zone 分片，把指定 key 范围"钉"在指定 shard 上。

## 8. balancer 与 chunk 迁移

分片集合的数据按 shard key 切成若干 **chunk**（每段连续 key 区间，阈值随版本变化，以官方文档为准）。**balancer** 在后台巡检各 shard 的 chunk 数量，差异超过阈值就发起迁移，让数据尽量均匀。

```javascript
sh.status()                // 总览：shard 列表、分片库、集合与 chunk 分布
sh.isBalancerRunning()     // balancer 是否正在迁移
sh.setBalancerState(false) // 大批量导入等窗口期可暂停（办完事记得恢复 true）
```

**讲解：**

1. chunk 迁移期间要在 shard 之间搬数据，占用带宽与缓存，高峰期会放大延迟——这就是大导入前先停 balancer、选低峰迁移的原因。
2. **jumbo chunk**：同一个 shard key 值的数据量大到无法再拆（比如某超级大 V 的全部数据），balancer 搬不动它；哈希键几乎不会产生 jumbo，这正是它受欢迎的原因之一。
3. 实践顺序：**先定分片、再灌数据**。往一个已分片的空集合写入比"先写满再补分片"便宜得多，后者要做一次全量均衡。

## 小结与延伸

> 副本集解决"坏了怎么办"，分片解决"大了怎么办"；oplog 是副本集的血液，shard key 是分片的命门。

收工自查清单：

1. 心跳 2 秒、选举默认约 10 秒；投票节点取奇数，最多 7 票。
2. 四种成员角色能区分：priority 0 不当主、hidden 不接客、delayed 留后悔药、arbiter 不存数据（不推荐）。
3. 三件套各管一件事：读偏好管"读谁"，读关注管"多可信"，写关注管"多稳"。
4. shard key 四原则：高基数、非单调、贴合查询、想好不可逆；递增键配 hashed。
5. 学习环境一条命令：`mongod --replSet rs0` 加 `rs.initiate()`。

延伸阅读：副本集是多文档事务（006）的运行前提；分片集合的索引设计见 004；建模范式见 005。官方文档关键词：Replication、Replica Set Members、Sharding Introduction、Shard Key，各默认值与版本差异以官方文档为准。

<!-- ============================================================ mongodb/008-SecurityUserManagement ============================================================ -->

## 0. 把数据库的门锁好（先读这里）

> 学习目标：给一台新装的 MongoDB 打开访问控制并创建首位管理员；按最小权限为应用与报表场景分别建号并验证权限边界；会配置 bindIp 与 TLS；能识别六类常见安全反模式并完成一次自查。

MongoDB 历史上最惨烈的安全事故不是技术缺陷，而是配置问题：成千上万台不做认证、直接绑公网的 mongod 被扫到后勒索删库。数据库安全的多数工作其实是"把默认该开的开关打开、把不该开的大门关上"。这一篇按"访问控制、账号与角色、网络、加密审计、反模式自查"的顺序，把门锁好。

## 1. 安全清单总览

| 层面 | 要做的事 |
| --- | --- |
| 访问控制 | 开启 `authorization`，创建首位管理员，禁止裸奔 |
| 账号 | 每个应用独立账号、最小权限，root 只留给人，不进应用配置 |
| 网络 | `bindIp` 只绑内网地址，防火墙 / 安全组收紧，绝不暴露公网 |
| 传输 | 客户端与节点间启用 TLS |
| 存储 | 静态加密（商业版能力）或磁盘层加密；超敏感字段用字段级加密 |
| 审计 | 记录认证与 DDL 事件（企业版 / Atlas 能力） |
| 运维 | 跟进安全补丁与官方安全通告 |

这份清单对应官方 Security Checklist 的思路。下面逐层落地。

## 2. 开启访问控制：localhost exception 与首位管理员

```yaml
# /etc/mongod.conf 关键片段
security:
  authorization: enabled
```

```bash
sudo systemctl restart mongod   # Linux 让配置生效（也可用命令行参数 --auth 启动）
```

**localhost exception**：实例上还没有任何用户时，允许来自本机的连接创建第一个用户——这是"没有用户就无法登录、无法登录就无法建用户"死结的官方解法。这个窗口只维持到第一个用户创建成功，随后立即关闭，因此必须在本机上完成下面的操作。

```javascript
// 重启后在本机直连（mongosh 默认连 127.0.0.1:27017，此时无需认证）
use admin
db.createUser({
  user: "admin",
  pwd: "请改成高强度随机密码",
  roles: [
    { role: "userAdminAnyDatabase", db: "admin" }  // 用户管理员：只管账号与角色，不碰业务数据
  ]
})
```

```javascript
// 此后所有连接都必须认证；用新账号登录验证
db.auth("admin", "请改成高强度随机密码")
```

**讲解：**

1. 首位管理员的最佳实践是只授予 `userAdminAnyDatabase`——它能创建与管理用户，但读不到业务数据；这样即使 admin 账号泄露，攻击者还差一层。
2. 不在首位管理员上直接给 `root` 的理由：权限一旦给出去就很难收回，"高权限账号只管人"是分权的第一步。
3. 如果重启后发现本机也要密码——那说明库里已有用户，localhost exception 已关闭，走正常认证即可。

## 3. SCRAM 认证与 createUser

MongoDB 默认使用 **SCRAM**（当前默认机制为 SCRAM-SHA-256）质询-响应认证：密码以加盐哈希形式存在 admin 库中，认证过程不在网络上传输明文密码（跨不可信网络仍应配合 TLS）。

```javascript
use appdb
// 给应用创建业务账号：只对 appdb 有读写权限
db.createUser({
  user: "app_writer",
  pwd: "另一个高强度密码",
  roles: [ { role: "readWrite", db: "appdb" } ]
})

// 查看库内用户与角色
db.getUsers()
```

```javascript
// 日常运维三件套
db.changeUserPassword("app_writer", "新密码")  // 改密（疑似泄露时第一步）
db.updateUser("app_writer", { roles: [ ... ] }) // 调整角色
db.dropUser("app_writer")                       // 离职 / 下线时回收
```

应用连接串的写法——账号建在哪个库，`authSource` 就指向哪个库：

```bash
# 业务账号建在 appdb，认证库就是 appdb
mongosh "mongodb://app_writer:密码@127.0.0.1:27017/appdb?authSource=appdb"
```

**讲解：** `authSource` 是新手最常踩的坑：账号建在 `admin` 库而连接串没写 `authSource=admin`（或反之），报的是"认证失败"，实际是"找错了验证库"。

## 4. 内置角色体系速查

| 分组 | 角色 | 能力摘要 |
| --- | --- | --- |
| 数据库用户 | `read` / `readWrite` | 读 / 读写指定库的集合数据 |
| 数据库管理 | `dbAdmin` | 索引、统计、校验等库级管理（不含数据读写） |
| | `dbOwner` | dbAdmin + readWrite + userAdmin，单库全权 |
| | `userAdmin` | 管理该库的用户与角色 |
| 集群管理 | `clusterMonitor` | 只读监控，Compass、监控 Exporter 用它 |
| | `clusterManager` / `clusterAdmin` | 副本集与分片的管理 / 全权 |
| 备份恢复 | `backup` / `restore` | 导出 / 导入，备份专用账号 |
| 全库角色 | `readAnyDatabase` 等 | 所有库的读 / 写 / 管理，仅能在 admin 库授予 |
| 超级用户 | `root` | 全权，只应属于人类管理员 |

**用角色的三句口诀：**

1. 应用账号给 `readWrite`（很多场景其实只需要 `read`）。
2. 监控系统给 `clusterMonitor`，不要为了看个状态给 `root`。
3. DBA 按需组合 `dbOwner` / `clusterAdmin`，`root` 不进任何应用配置文件。

## 5. 自定义角色与最小权限

内置角色有时仍然太粗：报表机器人需要"只读订单、可写报表结果"，`readWrite` 给多了，`read` 又不够。这时用 `createRole` 精确裁剪：

```javascript
use appdb
db.createRole({
  role: "reportReader",
  privileges: [
    { resource: { db: "appdb", collection: "orders" },  actions: [ "find" ] },          // 只能查订单
    { resource: { db: "appdb", collection: "reports" }, actions: [ "find", "insert" ] } // 可写报表结果
  ],
  roles: []  // 不继承任何内置角色，权限就这么多
})
db.createUser({ user: "report_bot", pwd: "第三把密码", roles: [ "reportReader" ] })
```

```javascript
// 用 report_bot 登录后验证权限边界
db.orders.find().limit(1)             // 正常返回
db.orders.insertOne({ cheat: true })  // 报 unauthorized，符合预期
db.runCommand({ connectionStatus: 1, showPrivileges: true })  // 查看当前连接的真实权限
```

**讲解：**

1. `resource` 支持三种粒度：`{ db, collection }` 集合级；`collection: ""` 该库全部集合；`{ cluster: true }` 集群级动作（如查看服务器状态）。
2. `actions` 是细粒度的动作白名单（`find`、`insert`、`createIndex` 等），以官方文档的 actions 清单为准。
3. 最小权限的三问自检：这个账号不做的事会不会被误授权？它的权限还能不能再小？一旦泄露，影响面有多大？

## 6. 网络层：bindIp、TLS 与副本集内部认证

**bindIp**：mongod 默认只绑 `127.0.0.1`，这是安全的默认值。需要远程访问时显式列出内网地址，永远不要在无认证的情况下绑 `0.0.0.0`。

```yaml
net:
  port: 27017
  bindIp: 10.0.1.5,127.0.0.1   # 只绑内网网卡与本地回环，配合防火墙 / 安全组
```

**TLS 传输加密**：

```yaml
net:
  tls:
    mode: requireTLS                    # 强制所有连接走 TLS
    certificateKeyFile: /etc/ssl/mongodb.pem
    CAFile: /etc/ssl/ca.pem
```

```bash
# 客户端连接同样要带 TLS 参数
mongosh --tls --host mongodb.example.com --tlsCAFile /etc/ssl/ca.pem -u admin -p
```

**副本集内部认证**：节点之间互访也要认证，用共享密钥文件：

```yaml
security:
  authorization: enabled
  keyFile: /etc/mongodb/keyfile   # 节点间共享密钥；文件权限 400，仅 mongod 用户可读
```

**讲解：** 配置 `keyFile` 会隐含开启访问控制——副本集环境下"忘了开认证"并不少见，keyFile 一并解决。云上部署优先用安全组白名单兜底：即使配置失误，公网也进不来。

## 7. 加密与审计概述

**静态加密**：WiredTiger 存储引擎的静态加密是商业版本（Enterprise / Atlas）能力，主密钥可接入 KMIP / KMS 管理；社区版的等价做法是磁盘或文件系统层加密。两者保护的都是"物理介质被拿走"的场景。

**字段级加密**：身份证、手机号这类字段，可在驱动层做客户端字段级加密（CSFLE）或新版本的 Queryable Encryption；自动加密依赖商业版本，手动方案社区可用，细节以官方文档为准。

**审计**（auditLog）为 Enterprise / Atlas 能力，记录认证、建删用户、删集合等敏感事件：

```yaml
auditLog:
  destination: file
  format: JSON
  path: /var/log/mongodb/audit.json
  filter: '{ atype: { $in: [ "authenticate", "createUser", "dropUser", "dropCollection" ] } }'
```

**讲解：** 加密与审计属于"业务长大后再逐层加固"的部分，但清单里要有它们的位置——安全不是一次性的开关，而是随规模升级的分层防线。

## 8. 常见安全反模式与自查

| 反模式 | 风险 | 修复 |
| --- | --- | --- |
| 无认证裸奔 | 公网可扫到，历史上大规模勒索删库的根源 | `authorization: enabled` + 首位管理员 |
| root 满天飞 | 应用被拖库即全库沦陷，误操作无法限权 | 分账号 + 最小权限角色 |
| `bind_ip 0.0.0.0` 且无防火墙 | 数据库直接暴露公网 | 只绑内网 + 安全组白名单 |
| 跨网段明文传输 | 中间人窃听账号与数据 | `requireTLS` |
| 密码硬编码进仓库 | 代码泄露即事故，换密码要发版 | 环境变量 / 密钥管理服务 |
| 全员共用一个账号 | 无法审计到人、无法精细回收 | 一人一号、一应用一号 |

```javascript
// 三条自查命令，巡检时各跑一遍
db.runCommand({ connectionStatus: 1, showPrivileges: true })  // 当前连接是谁、有什么权限
db.getUsers()     // 有没有多余、过期、权限过大的账号
db.currentOp(true) // 有没有来源可疑的连接
```

**讲解：** 安全事故复盘里反复出现同一句话："我们以为内网是安全的"。公网暴露 + 无认证的组合能在几小时内丢掉整个数据库，而修复只需要本篇第二节十分钟。

## 小结与延伸

> 门锁好的三步：开认证、给最小权限、别暴露公网；TLS、加密、审计随业务长大逐层加固。

收工自查清单：

1. 首位管理员用 `userAdminAnyDatabase`，在 localhost exception 窗口内本机创建。
2. 业务账号 `readWrite`、监控 `clusterMonitor`、备份 `backup/restore`、`root` 只给人。
3. 会用 `createRole` 按 `{ db, collection, actions }` 裁剪权限，并用 `connectionStatus` 验证。
4. `bindIp` 只绑内网，副本集配 keyFile，跨网段上 TLS。
5. 三条自查命令纳入巡检：`connectionStatus`、`getUsers`、`currentOp`。

延伸阅读：安装与首次连接见 `001-MongoDBOverviewQuickStart`；生产落地全景见 `005-SchemaDesignEnterprise`；副本集的 keyFile 内部认证配合 `007-ReplicaSetSharding` 一起读。官方文档关键词：Security Checklist、Authentication、Built-in Roles、TLS，具体配置项以官方文档为准。

<!-- ============================================================ mongodb/009-ChangeStreamRealtime ============================================================ -->

## 0. 让数据变化主动找你（先读这里）

> 学习目标：说明 Change Streams 与 oplog 的关系；用 watch 订阅集合、库、全集群，并用聚合管道过滤事件；理解 fullDocument 与 updateDescription 的取值差异；保存 resume token 实现断点续听，写出容错重启的监听循环；能判断一个需求该轮询还是订阅。

"订单状态变了怎么通知缓存？"——过去的答案通常是定时轮询：每隔一秒查一遍数据库。轮询有天然的尴尬：间隔大了不实时，间隔小了数据库扛不住，还感知不到删除。MongoDB 3.6 起提供了更好的答案：**Change Streams（变更流）**，让数据变化像消息队列一样"推"给订阅者。

## 1. Change Streams 是什么

Change Streams 是构建在 **oplog** 之上的变更订阅接口：oplog 记录了副本集上的每一次写操作（见 007 第 2 节），变更流把它封装成一个"应用可订阅、可过滤、可断点续听"的游标。对应用来说，它就是一条打开 `$changeStream` 阶段的聚合管道——你在 003 学的管道语法在这里直接复用。

```javascript
// 一条 insert 事件长这样（节选）
{
  _id: { _data: "8266CE..." },     // resume token：断点续听的"存折"
  operationType: "insert",
  clusterTime: Timestamp({ t: 1724832000, i: 1 }),  // 事件的集群时间
  ns: { db: "shop", coll: "orders" },
  documentKey: { _id: ObjectId("...") },
  fullDocument: { _id: ObjectId("..."), orderNo: "A001", total: 199, status: "created" }
}
```

**与直接 tail oplog 相比的优势：**

1. 不需要读 `local` 库（那需要更高权限），走正常的聚合接口与权限体系。
2. 天然支持管道过滤与投影，服务端就把噪音滤掉，省网络流量。
3. 每条事件自带 resume token，断点续听是原生能力。
4. 分片集群同样可用，事件全局有序。

前提条件：**副本集或分片集群**（oplog 存在才有得订阅）；事件按 oplog 顺序投递；除了增删改，drop、rename 等 DDL 也会产生事件（事件类型随版本增加，以官方文档为准）。

## 2. 三种监听粒度：集合、库、全集群

```javascript
// 1) 集合级：只听 orders 的变化（最常用）
const cs1 = db.orders.watch()

// 2) 库级：听当前库所有集合的变化
use shop
const cs2 = db.watch()

// 3) 部署级：听所有库的变化
const cs3 = db.getMongo().watch()
```

```javascript
// mongosh 里怎么读事件
const cs = db.orders.watch()
cs.next()     // 阻塞直到下一条事件到达
cs.tryNext()  // 非阻塞：没有新事件立即返回 null，适合轮询式演示
cs.close()    // 用完关闭游标
```

**讲解：**

1. 粒度越细开销越小：能用集合级就不要开库级，能用库级就不要开部署级。
2. 权限方面，应用账号拥有对应范围的读权限即可 watch（变更流权限包含在 read 类角色中，细节以官方文档为准），这也是它与裸读 oplog 的重要差别。
3. 另开一个 mongosh 窗口执行 `db.orders.insertOne({...})`，就能在本窗口的 `cs.next()` 里收到事件——这是验证环境是否就绪的最快办法。

## 3. 用聚合管道过滤与投影

watch 的第一个参数就是聚合管道，但只允许 `$match`、`$project`、`$addFields`、`$replaceRoot` 等少数阶段（支持范围以官方文档为准）：

```javascript
// 只关心"支付成功"的更新事件，且只取必要字段
const pipeline = [
  {
    $match: {
      operationType: "update",                            // 只要更新事件
      "updateDescription.updatedFields.status": "paid"    // 且 status 恰好变为 paid
    }
  },
  {
    $project: {
      operationType: 1,
      documentKey: 1,                                     // 拿到 _id 就够下游使用
      "updateDescription.updatedFields": 1
    }
  }
]
const cs = db.orders.watch(pipeline)
```

```javascript
// 缓存失效场景：只听 update 与 delete，其他事件全部丢弃
const cs = db.orders.watch([
  { $match: { operationType: { $in: [ "update", "delete" ] } } }
])
```

**讲解：**

1. 过滤条件可以直接引用事件文档的字段路径（如 `fullDocument.status`、`updateDescription.updatedFields.xxx`），写法与普通聚合完全一致。
2. **过滤下推到服务端**是变更流性能的关键：网络里只跑你关心的事件，而不是全库流水。

## 4. 读懂事件：fullDocument 与 updateDescription

update 事件默认**不带完整文档**，只带增量描述 `updateDescription`：

```javascript
// 一次 db.orders.updateOne({...}, { $set: { status: "paid" }, $unset: { couponCode: "" } }) 之后的事件（节选）
{
  operationType: "update",
  documentKey: { _id: ObjectId("...") },
  updateDescription: {
    updatedFields: { status: "paid", "items.1.qty": 2 },  // 点路径精确到数组元素
    removedFields: [ "couponCode" ]                       // 被删除的字段
  }
}
```

需要完整文档时用 `fullDocument` 选项：

| 取值 | 行为 |
| --- | --- |
| default（默认） | update 事件不含 fullDocument |
| updateLookup | 事件送达时回查一次当前文档；注意读到的是"此刻"的值，不保证是变更瞬间的版本 |
| whenAvailable / required | 6.0 起，配合集合级前后镜像（pre/post image），可拿到变更前 / 后的完整快照（有额外存储开销，以官方文档为准） |

```javascript
// 需要"变更后的完整文档"时
const cs = db.orders.watch([], { fullDocument: "updateLookup" })

// 6.0+：开启集合级前后镜像后，可同时拿到变更前后的文档
db.runCommand({ collMod: "orders", changeStreamPreAndPostImages: { enabled: true } })
const cs2 = db.orders.watch(
  [],
  { fullDocument: "whenAvailable", fullDocumentBeforeChange: "whenAvailable" }
)
```

**讲解：**

1. `updateLookup` 有一处语义要特别当心：两次变更挨得很近时，回查到的可能已经是最新状态，事件与快照之间有时间差。
2. 前后镜像解决的是"审计、回滚、Diff"类需求，但每份文档多存一份镜像，要评估存储成本。
3. insert / replace / delete 事件没有这个问题：它们本来就带 `fullDocument`（delete 只带 `documentKey`）。

## 5. resume token 与断点续听

每条事件的 `_id` 就是 **resume token**。把它持久化下来，进程重启后用 `resumeAfter` 从上次位置继续，一条事件都不丢：

```javascript
// 处理完一条事件后，把断点记到 meta 库的 checkpoints 集合
const evt = cs.next()
db.getSiblingDB("meta").checkpoints.updateOne(
  { name: "orders-watcher" },
  { $set: { token: evt._id } },
  { upsert: true }
)

// 重启后从断点继续
const saved = db.getSiblingDB("meta").checkpoints.findOne({ name: "orders-watcher" })
const cs = db.orders.watch([], saved ? { resumeAfter: saved.token } : {})
```

**三个相关选项：**

1. `resumeAfter`：从该事件之后继续；遇到 invalidate（如集合被 drop）后失效。
2. `startAfter`：可以在 invalidate 之后继续，适合"失效后重新接上"的场景。
3. `startAtOperationTime`：从某个时刻开始听，常用于"先做全量初始化、再从初始化时刻接管增量"。

**oplog 窗口是硬约束：** resume token 指向的事件一旦被 oplog 滚动淘汰（比如监听程序停了三天，oplog 只保留两小时），resume 会报 `ChangeStreamHistoryLost`——只能做全量重建后从当前时刻继续。oplog 越大，允许的断线时间越长（用 `rs.printReplicationInfo()` 查看窗口）。

## 6. 容错重启实践：带断点的监听循环

```javascript
// ===== 带断点续听的容错监听循环（mongosh 演示版，Ctrl+C 停止）=====
const META = db.getSiblingDB("meta").checkpoints
const NAME = "orders-watcher"

function handle(evt) {
  // 替换为你的业务：删缓存、推送大屏、同步搜索引擎……
  print(evt.operationType + " -> " + JSON.stringify(evt.documentKey))
}

function watchOrders() {
  // 启动时读取上次断点
  let token = null
  const saved = META.findOne({ name: NAME })
  if (saved) token = saved.token

  while (true) {
    try {
      const cs = db.orders.watch([], token ? { resumeAfter: token } : {})
      if (token) { print("从断点继续监听") } else { print("从当前时刻开始监听") }

      while (true) {
        const evt = cs.tryNext()              // 非阻塞读取
        if (evt) {
          handle(evt)
          token = evt._id                     // 先处理后推进断点（配合幂等消费更稳）
          META.updateOne({ name: NAME }, { $set: { token } }, { upsert: true })
        } else {
          sleep(500)                          // mongosh 的 sleep，单位毫秒
        }
      }
    } catch (err) {
      if (err.hasErrorLabel && err.hasErrorLabel("ChangeStreamHistoryLost")) {
        // 断点已被 oplog 淘汰：执行全量重建（此处略），再从当前时刻接管
        print("断点失效，执行全量重建后从当前时刻继续")
        token = null
      } else {
        // 网络抖动、主从切换等：稍等后带着断点重连
        print("监听异常，5 秒后重连：" + err.message)
        sleep(5000)
      }
    }
  }
}

watchOrders()
```

**讲解：**

1. 循环的三条出口对应三种现实：正常拿到事件、临时故障（带断点重连）、断点失效（全量重建）。生产代码把"全量重建"实现为：清空下游 → 全表扫描灌入 → 用 `startAtOperationTime: 重建开始时刻` 接管增量。
2. mongosh 适合演示与运维脚本；生产环境用官方驱动（Node.js / Java / Python 均内置了 resume 语义与自动重连），并把 checkpoint 落库或落消息队列。
3. "先处理后推进断点"意味着故障重连会重复消费最后一条事件——下游逻辑要写成幂等的（按 `documentKey` 去重或覆盖写）。

## 7. 典型场景与选型对比

**场景一：缓存失效（最经典）**

```javascript
// 变更驱动的缓存失效（伪代码）
if (evt.operationType === "update" || evt.operationType === "delete") {
  redis.del("order:" + evt.documentKey._id)   // 库里一变，缓存立刻失效
}
```

**场景二：实时大屏**——把 `$match` 过滤后的事件经 WebSocket 推给前端，数据入库到图表刷新之间没有轮询间隔。

**场景三：CDC 数据管道**——同步到 Elasticsearch（搜索）、Kafka（消息队列）或数仓，替代"应用层双写"，天然不会漏写、错序。

**场景四：微服务数据分发**——库内一写，多个服务各自订阅，减少服务之间的直接耦合。

**轮询 vs 变更流：**

| 维度 | 定时轮询 | Change Streams |
| --- | --- | --- |
| 实时性 | 取决于轮询间隔（秒到分钟级） | 事件产生即推送，亚秒级 |
| 数据库负载 | 间隔越小负载越高，空转多 | 一条常驻游标，负载平稳 |
| 删除感知 | 难：记录没了才知道 | delete 事件明确送达 |
| 断点续传 | 自己比对时间戳 / 水位，易漏 | resume token 原生支持 |
| 环境要求 | 无 | 需要副本集；注意 oplog 窗口 |
| 适用 | 低频报表、离线任务 | 缓存失效、实时大屏、CDC |

一句话补充：使用 Atlas 的项目可以把"监听 + 处理"托管给 Atlas Triggers（数据库触发器），无需自建常驻进程。

## 小结与延伸

> 变更流 = oplog 的应用层封装；生产可用性取决于三件事：过滤下推、断点持久化、失效重建。

收工自查清单：

1. 三种粒度从细到粗：集合 `watch()`、库 `db.watch()`、部署 `db.getMongo().watch()`。
2. 管道过滤用 `$match` / `$project`，服务端过滤省流量；事件文档的字段路径可直接引用。
3. update 事件默认只带 `updateDescription`；要完整文档用 `fullDocument: "updateLookup"`，要前后镜像用 6.0 的 pre/post image。
4. resume token 每事件一个，持久化到 `checkpoints`；`ChangeStreamHistoryLost` 触发全量重建。
5. 下游消费必须幂等，因为"先处理后推进断点"意味着重连时可能重复消费。

延伸阅读：管道语法详见 `003-AggregationPipeline`（watch 就是管道）；事件里的增删改语义见 `002-CRUDOperations`；oplog 与副本集机制见 `007-ReplicaSetSharding`。官方文档关键词：Change Streams、Change Events、Resume a Change Stream，事件类型与选项以官方文档为准。
