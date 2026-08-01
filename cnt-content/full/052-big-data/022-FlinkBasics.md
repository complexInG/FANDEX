---
order: 220
title: 大数据 Flink 流处理
module: 052-big-data
category: '052-big-data'
difficulty: beginner
description: 大数据 Flink 流处理 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# 大数据 Flink 流处理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 执行环境

**换行写法：创建流执行环境**
`from pyflink.datastream import StreamExecutionEnvironment`
`env = StreamExecutionEnvironment.get_execution_environment()`

```python
# 创建流处理执行环境
from pyflink.datastream import StreamExecutionEnvironment

env = StreamExecutionEnvironment.get_execution_environment()
```

---

**基本写法：设置并行度**
`env.set_parallelism(<并行度>)`

```python
# 设置并行度
env.set_parallelism(4)
```

---

**基本写法：启用检查点**
`env.enable_checkpointing(<间隔毫秒>)`

```python
# 每 60 秒一次检查点
env.enable_checkpointing(60000)
```

---

**换行写法：配置检查点**
`env.enable_checkpointing(<间隔>)`
`env.get_checkpoint_config().set_min_pause_between_checkpoints(<毫秒>)`

```python
# 配置检查点参数
env.enable_checkpointing(60000)
config = env.get_checkpoint_config()
config.set_min_pause_between_checkpoints(30000)
config.set_checkpoint_timeout(120000)
config.set_max_concurrent_checkpoints(1)
```

---

**换行写法：创建表执行环境**
`from pyflink.table import StreamTableEnvironment`
`t_env = StreamTableEnvironment.create(env)`

```python
# 创建 Table API 环境
from pyflink.table import StreamTableEnvironment

t_env = StreamTableEnvironment.create(env)
```

---

## DataStream API

**基本写法：从集合创建流**
`env.from_collection(<集合>)`

```python
# 从列表创建数据流
ds = env.from_collection([1, 2, 3, 4, 5])
```

---

**基本写法：从 Socket 创建流**
`env.socket_text_stream(<主机>, <端口>)`

```python
# 从 Socket 读取数据流
ds = env.socket_text_stream("localhost", 9999)
```

---

**换行写法：从文件创建流**
`ds = env.read_text_file(<路径>)`

```python
# 从文本文件读取
ds = env.read_text_file("data/input.txt")
```

---

**换行写法：从 Kafka 创建流**
`ds = env.add_source(<KafkaSource>)`

```python
# 从 Kafka 读取
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer

props = {"bootstrap.servers": "localhost:9092"}
kafka_source = FlinkKafkaConsumer("my_topic", SimpleStringSchema(), props)
ds = env.add_source(kafka_source)
```

---

## 转换操作

**基本写法：map 转换**
`ds.map(<函数>)`

```python
# map 转换
result = ds.map(lambda x: x * 2)
```

---

**基本写法：flat_map 转换**
`ds.flat_map(<函数>)`

```python
# flatMap 转换
words = ds.flat_map(lambda line: line.split(" "))
```

---

**基本写法：filter 过滤**
`ds.filter(<函数>)`

```python
# 过滤操作
even = ds.filter(lambda x: x % 2 == 0)
```

---

**基本写法：key_by 分组**
`ds.key_by(<键>)`

```python
# 按键分组
keyed = ds.key_by(lambda x: x[0])
```

---

**基本写法：reduce 聚合**
`keyed.reduce(<函数>)`

```python
# 聚合操作
reduced = keyed.reduce(lambda a, b: (a[0], a[1] + b[1]))
```

---

**基本写法：window 窗口**
`keyed.window(<窗口分配器>)`

```python
# 滚动窗口
from pyflink.datastream import TumblingEventTimeWindows
from pyflink.common.time import Time

windowed = keyed.window(TumblingEventTimeWindows.of(Time.minutes(5)))
```

---

**基本写法：滑动窗口**
`keyed.window(SlidingEventTimeWindows.of(<大小>, <滑动>))`

```python
# 滑动窗口（5 分钟窗口，1 分钟滑动）
from pyflink.datastream import SlidingEventTimeWindows

windowed = keyed.window(SlidingEventTimeWindows.of(
    Time.minutes(5), Time.minutes(1)
))
```

---

**基本写法：会话窗口**
`keyed.window(EventTimeSessionWindows.with_gap(<间隔>))`

```python
# 会话窗口（10 分钟间隔）
from pyflink.datastream import EventTimeSessionWindows

windowed = keyed.window(EventTimeSessionWindows.with_gap(Time.minutes(10)))
```

---

**基本写法：窗口聚合**
`windowed.reduce(<函数>)`

```python
# 窗口内聚合
result = windowed.reduce(lambda a, b: (a[0], a[1] + b[1]))
```

---

**基本写法：窗口函数**
`windowed.apply(<函数>)`

```python
# 窗口应用函数
def window_func(key, window, values):
    yield (key, window, sum(values))

result = windowed.apply(window_func)
```

---

## 窗口操作

**基本写法：计数窗口**
`ds.count_window(<大小>)`

```python
# 计数滚动窗口（每 100 条一个窗口）
windowed = ds.count_window(100)
```

---

**基本写法：滑动计数窗口**
`ds.count_window(<大小>, <滑动>)`

```python
# 计数滑动窗口
windowed = ds.count_window(100, 20)
```

---

**基本写法：窗口最小值**
`windowed.min(<字段>)`

```python
# 窗口最小值
result = windowed.min(1)
```

---

**基本写法：窗口最大值**
`windowed.max(<字段>)`

```python
# 窗口最大值
result = windowed.max(1)
```

---

**基本写法：窗口求和**
`windowed.sum(<字段>)`

```python
# 窗口求和
result = windowed.sum(1)
```

---

## 水位线

**换行写法：设置水位线**
`ds.assign_timestamps_and_watermarks(<水位线策略>)`

```python
# 设置水位线
from pyflink.datastream import WatermarkStrategy
from pyflink.common.time import Duration

watermark_strategy = WatermarkStrategy.for_bounded_out_of_orderness(Duration.of_seconds(10))
ds = ds.assign_timestamps_and_watermarks(watermark_strategy)
```

---

**换行写法：自定义时间戳**
`ds.assign_timestamps_and_watermarks(<策略>)`

```python
# 从事件提取时间戳
class MyTimestampAssigner(TimestampAssigner):
    def extract_timestamp(self, value, record_timestamp):
        return value["timestamp"]

strategy = WatermarkStrategy.for_bounded_out_of_orderness(
    Duration.of_seconds(10)
).with_timestamp_assigner(MyTimestampAssigner())
ds = ds.assign_timestamps_and_watermarks(strategy)
```

---

## Sink 输出

**基本写法：打印输出**
`ds.print()`

```python
# 打印到标准输出
result.print()
```

---

**基本写法：写入文本文件**
`ds.write_as_text(<路径>)`

```python
# 写入文本文件
result.write_as_text("output/result.txt")
```

---

**换行写法：写入 Kafka**
`ds.add_sink(<KafkaSink>)`

```python
# 写入 Kafka
from pyflink.datastream.connectors import FlinkKafkaProducer

kafka_sink = FlinkKafkaProducer(
    topic="output_topic",
    serialization_schema=SimpleStringSchema(),
    producer_config={"bootstrap.servers": "localhost:9092"}
)
ds.add_sink(kafka_sink)
```

---

**换行写法：写入 JDBC**
`ds.add_sink(<JdbcSink>)`

```python
# 写入 MySQL
from pyflink.datastream.connectors.jdbc import JdbcSink

ds.add_sink(JdbcSink.sink_sql(
    "INSERT INTO results (id, count) VALUES (?, ?)",
    type_info,
    driver="com.mysql.cj.jdbc.Driver",
    url="jdbc:mysql://localhost:3306/db",
    username="root",
    password="123456"
))
```

---

## 执行与触发

**基本写法：执行作业**
`env.execute(<作业名>)`

```python
# 执行流处理作业
env.execute("MyStreamingJob")
```

---

**基本写法：阻塞执行**
`env.execute()`

```python
# 阻塞执行（无作业名）
env.execute()
```

---

## Table API

**换行写法：创建表**
`t_env.create_temporary_table(<表名>, <表描述器>)`

```python
# 创建临时表
from pyflink.table import TableDescriptor

t_env.create_temporary_table(
    "source_table",
    TableDescriptor.for_connector("kafka")
        .schema(Schema.new_builder()
            .column("word", DataTypes.STRING())
            .build())
        .option("topic", "input_topic")
        .option("properties.bootstrap.servers", "localhost:9092")
        .option("format", "json")
        .build()
)
```

---

**基本写法：从表查询**
`t_env.from(<表名>)`

```python
# 从表创建 Table 对象
table = t_env.from("source_table")
```

---

**基本写法：执行 SQL**
`t_env.sql_query(<SQL语句>)`

```python
# 执行 SQL 查询
result = t_env.sql_query("""
    SELECT word, COUNT(*) as cnt
    FROM source_table
    GROUP BY word
""")
```

---

**基本写法：Table 操作**
`<table>.select(<列>)`

```python
# Table API 操作
result = table.select(table.word, table.count) \
    .where(table.count > 10)
```

---

**基本写法：分组聚合**
`<table>.group_by(<列>).select(<列>, <聚合>)`

```python
# 分组聚合
result = table.group_by(table.word) \
    .select(table.word, table.count)
```

---

**基本写法：转换为流**
`t_env.to_append_stream(<table>, <类型>)`

```python
# Table 转换为 DataStream
from pyflink.common.typeinfo import Types

ds = t_env.to_append_stream(result, Types.ROW([str, int]))
```

---

**基本写法：写入表**
`<table>.execute_insert(<目标表>)`

```python
# 将结果写入表
result.execute_insert("sink_table")
```

---

## 状态管理

**换行写法：使用 ValueState**
`from pyflink.datastream.functions import RuntimeContext`
`state = context.get_state(ValueStateDescriptor(<名>, <类型>))`

```python
# 使用 ValueState
from pyflink.datastream.functions import RichMapFunction, ValueStateDescriptor

class MyFunction(RichMapFunction):
    def open(self, runtime_context):
        self.state = runtime_context.get_state(
            ValueStateDescriptor("my_state", Types.INT())
        )

    def map(self, value):
        current = self.state.value() or 0
        self.state.update(current + value)
        return self.state.value()
```

---

**换行写法：使用 ListState**
`state = context.get_list_state(ListStateDescriptor(<名>, <类型>))`

```python
# 使用 ListState
from pyflink.datastream.functions import RichFlatMapFunction, ListStateDescriptor

class MyFunction(RichFlatMapFunction):
    def open(self, runtime_context):
        self.state = runtime_context.get_list_state(
            ListStateDescriptor("my_list", Types.INT())
        )

    def flat_map(self, value):
        self.state.add(value)
        yield list(self.state)
```

---

## 侧输出

**换行写法：定义侧输出标签**
`from pyflink.datastream import OutputTag`
`output_tag = OutputTag(<名称>, <类型>)`

```python
# 定义侧输出标签
from pyflink.datastream import OutputTag

error_tag = OutputTag("errors", Types.STRING())
```

---

**换行写法：输出到侧输出**
`ctx.output(<标签>, <值>)`

```python
# 在 ProcessFunction 中输出到侧输出
from pyflink.datastream.functions import ProcessFunction

class MyFunction(ProcessFunction):
    def process_element(self, value, ctx):
        if value < 0:
            ctx.output(error_tag, value)
        else:
            ctx.output(MainOutput, value)
```

---

**基本写法：获取侧输出**
`ds.get_side_output(<标签>)`

```python
# 获取侧输出流
error_stream = main_stream.get_side_output(error_tag)
```

## 参考文献



Apache Spark：https://spark.apache.org/docs/latest/
Apache Flink：https://flink.apache.org/
Apache Kafka：https://kafka.apache.org/documentation/
ClickHouse：https://clickhouse.com/docs
Airflow：https://airflow.apache.org/docs/

## 延伸阅读



大数据生态概览，见 052-big-data 模块文档。
数据分析与统计，见 051-data-analysis/030-probability-statistics 模块。
分布式系统基础，见 034-cloud-computing 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供大数据课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 大数据概述 | 001-DataOverview | 本文的前置基础 |
| HDFS分布式文件系统 | 002-HDFSDistributedFileSystem | 本文的并列主题 |
| MapReduce | 003-MapReduce | 本文的并列主题 |
| Spark核心 | 004-SparkCore | 本文的并列主题 |
| Spark-Streaming | 005-SparkStreaming | 本文的并列主题 |
| Hive数据仓库 | 006-HiveDataWarehouse | 本文的并列主题 |
| HBase列族数据库 | 007-HBaseDatabase | 本文的并列主题 |
| Kafka消息队列 | 008-KafkaMessageQueue | 本文的并列主题 |
| Flink流处理 | 009-FlinkStreamHandling | 本文的并列主题 |
| 数据湖 | 010-DataLake | 本文的并列主题 |
| Zookeeper协调服务 | 011-Zookeeper | 本文的并列主题 |
| YARN资源管理 | 012-YARNManagement | 本文的并列主题 |
| 大数据 HDFS 命令 | 013-HDFSCommands | 本文的并列主题 |
| 大数据 YARN 命令 | 014-YARNCommands | 本文的并列主题 |
| 大数据 Spark RDD | 015-SparkRDD | 本文的并列主题 |
| 大数据 Spark DataFrame | 016-SparkDataFrame | 本文的并列主题 |
| 大数据 Hive DDL | 017-HiveDDL | 本文的并列主题 |
| 大数据 Hive DML | 018-HiveDML | 本文的并列主题 |
| 大数据 Hive 函数 | 019-HiveFunctions | 本文的并列主题 |
| 大数据 Kafka 命令 | 020-KafkaCommands | 本文的并列主题 |
| 大数据 HBase 命令 | 021-HBaseCommands | 本文的并列主题 |
| 大数据 Flink 流处理 | 022-FlinkBasics | 本文自身 |
| 大数据 Spark 优化 | 023-SparkOptimization | 本文的性能延伸 |
