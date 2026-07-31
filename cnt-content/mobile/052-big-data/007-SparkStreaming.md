# 大数据 Spark Streaming

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 StreamingContext

**换行写法：初始化 StreamingContext**
`from pyspark.streaming import StreamingContext`
`ssc = StreamingContext(sc, <批次间隔>)`

```python
# 创建 StreamingContext（批次间隔 1 秒）
from pyspark.streaming import StreamingContext

ssc = StreamingContext(sc, batchDuration=1)
```

---

**基本写法：设置检查点**
`ssc.checkpoint(<路径>)`

```python
# 设置检查点目录（用于状态恢复）
ssc.checkpoint("hdfs://namenode:8020/checkpoint")
```

---

## 数据源

**基本写法：Socket 数据源**
`ssc.socketTextStream(<主机>, <端口>)`

```python
# 从 Socket 接收文本数据
lines = ssc.socketTextStream("localhost", 9999)
```

---

**基本写法：文件流**
`ssc.textFileStream(<目录>)`

```python
# 监控目录中的新文件
lines = ssc.textFileStream("hdfs://namenode:8020/streaming/")
```

---

**换行写法：Kafka 数据源**
`from pyspark.streaming.kafka import KafkaUtils`
`stream = KafkaUtils.createDirectStream(ssc, [<主题>], <kafka参数>)`

```python
# 从 Kafka 接收数据
from pyspark.streaming.kafka import KafkaUtils

kafkaParams = {"metadata.broker.list": "localhost:9092"}
topics = ["my_topic"]
stream = KafkaUtils.createDirectStream(ssc, topics, kafkaParams)
```

---

**换行写法：自定义接收器**
`ssc.receiverStream(<自定义接收器>)`

```python
# 自定义接收器（需继承 Receiver）
from pyspark.streaming.receiver import Receiver

class MyReceiver(Receiver):
    def onStart(self):
        # 启动接收数据的线程
        pass

    def onStop(self):
        # 停止接收
        pass

stream = ssc.receiverStream(MyReceiver())
```

---

## DStream 操作

**基本写法：map 转换**
`<dstream>.map(<函数>)`

```python
# 对每个元素应用函数
words = lines.map(lambda line: line.split(" "))
```

---

**基本写法：flatMap 转换**
`<dstream>.flatMap(<函数>)`

```python
# 展平结果
words = lines.flatMap(lambda line: line.split(" "))
```

---

**基本写法：filter 过滤**
`<dstream>.filter(<函数>)`

```python
# 过滤
long_words = words.filter(lambda word: len(word) > 3)
```

---

**基本写法：count 计数**
`<dstream>.count()`

```python
# 每批次元素计数
counts = words.count()
```

---

**基本写法：reduce 聚合**
`<dstream>.reduce(<函数>)`

```python
# 每批次聚合
total = numbers.reduce(lambda a, b: a + b)
```

---

**基本写法：countByValue**
`<dstream>.countByValue()`

```python
# 统计每个值的出现次数
word_counts = words.countByValue()
```

---

## 窗口操作

**基本写法：窗口聚合**
`<dstream>.reduceByWindow(<函数>, <窗口时长>, <滑动间隔>)`

```python
# 窗口聚合（窗口 10 秒，滑动 5 秒）
windowed = numbers.reduceByWindow(
    lambda a, b: a + b,
    windowDuration=10,
    slideDuration=5
)
```

---

**基本写法：窗口计数**
`<dstream>.countByWindow(<窗口时长>, <滑动间隔>)`

```python
# 窗口内计数
windowed_count = words.countByWindow(
    windowDuration=10,
    slideDuration=5
)
```

---

**基本写法：按值窗口计数**
`<dstream>.countByValueAndWindow(<窗口时长>, <滑动间隔>)`

```python
# 窗口内按值计数
windowed_word_count = words.countByValueAndWindow(
    windowDuration=10,
    slideDuration=5
)
```

---

**基本写法：窗口内分组聚合**
`<dstream>.reduceByKeyAndWindow(<函数>, <窗口时长>, <滑动间隔>)`

```python
# 窗口内按键聚合
windowed_counts = pairs.reduceByKeyAndWindow(
    lambda a, b: a + b,
    windowDuration=10,
    slideDuration=5
)
```

---

**基本写法：带反向函数的窗口**
`<dstream>.reduceByKeyAndWindow(<函数>, <反向函数>, <窗口时长>, <滑动间隔>)`

```python
# 高效窗口聚合（增量计算）
windowed_counts = pairs.reduceByKeyAndWindow(
    lambda a, b: a + b,        # 加入新数据
    lambda a, b: a - b,        # 移除旧数据
    windowDuration=10,
    slideDuration=5
)
```

---

## 状态操作

**基本写法：更新状态**
`<dstream>.updateStateByKey(<更新函数>)`

```python
# 更新状态（需要设置 checkpoint）
def updateFunc(new_values, last_state):
    total = last_state or 0
    for value in new_values:
        total += value
    return total

state_counts = pairs.updateStateByKey(updateFunc)
```

---

**基本写法：mapWithState**
`<dstream>.mapWithState(<状态规范>)`

```python
# 高效状态更新
from pyspark.streaming import State, StateSpec

def mappingFunction(key, value, state):
    total = state.get() or 0
    total += value
    state.update(total)
    return (key, total)

spec = StateSpec.function(mappingFunction)
state_stream = pairs.mapWithState(spec)
```

---

## 输出操作

**基本写法：打印**
`<dstream>.pprint([<行数>])`

```python
# 打印前 10 条
result.pprint()
# 打印前 20 条
result.pprint(20)
```

---

**基本写法：保存为文本文件**
`<dstream>.saveAsTextFiles(<前缀>, [<后缀>])`

```python
# 保存到文件（每批次一个目录）
result.saveAsTextFiles("output/streaming", "txt")
```

---

**换行写法：foreachRDD 输出**
`<dstream>.foreachRDD(<函数>)`

```python
# 对每个 RDD 执行自定义操作
def process(rdd):
    if not rdd.isEmpty():
        df = spark.createDataFrame(rdd)
        df.write.mode("append").parquet("output/")

result.foreachRDD(process)
```

---

**换行写法：foreachRDD 写入数据库**
`<dstream>.foreachRDD(<函数>)`

```python
# 将结果写入 MySQL
def save_to_mysql(rdd):
    if not rdd.isEmpty():
        pdf = rdd.toDF().toPandas()
        pdf.to_sql("results", engine, if_exists="append", index=False)

result.foreachRDD(save_to_mysql)
```

---

## DStream 转换

**基本写法：转换为 RDD 操作**
`<dstream>.transform(<函数>)`

```python
# 在 DStream 上应用 RDD 操作
sorted_stream = dstream.transform(lambda rdd: rdd.sortBy(lambda x: x[1], False))
```

---

**基本写法：连接静态数据**
`<dstream>.transformWith(<函数>, <静态RDD>)`

```python
# 将流数据与静态 RDD 连接
static_data = sc.parallelize([("apple", "水果"), ("banana", "水果")])
enriched = dstream.transformWith(
    lambda rdd, static: rdd.join(static),
    static_data
)
```

---

## 启动与停止

**基本写法：启动流处理**
`ssc.start()`

```python
# 启动流处理
ssc.start()
```

---

**基本写法：等待终止**
`ssc.awaitTermination()`

```python
# 等待作业终止
ssc.awaitTermination()
```

---

**基本写法：等待终止或超时**
`ssc.awaitTerminationOrTimeout(<超时秒数>)`

```python
# 等待 60 秒或终止
ssc.awaitTerminationOrTimeout(60)
```

---

**基本写法：停止流处理**
`ssc.stop([stopSparkContext], [stopGraceFully])`

```python
# 优雅停止
ssc.stop(stopSparkContext=True, stopGracefully=True)
```

---

## Structured Streaming

**换行写法：创建流式 DataFrame**
`stream = spark.readStream.format(<格式>).load(<路径>)`

```python
# 使用 Structured Streaming
stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "my_topic") \
    .load()
```

---

**基本写法：Socket 数据源**
`spark.readStream.format("socket").option("host", ...).option("port", ...).load()`

```python
# Socket 数据源
lines = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()
```

---

**基本写法：文件数据源**
`spark.readStream.format("<格式>").load(<路径>)`

```python
# 监控 CSV 文件目录
stream = spark.readStream \
    .format("csv") \
    .option("header", True) \
    .schema(schema) \
    .load("data/")
```

---

**基本写法：流式聚合**
`<stream>.groupBy(<列>).agg(<聚合函数>)`

```python
# 流式聚合
from pyspark.sql import functions as F

word_counts = lines.groupBy("word").agg(F.count("*").alias("count"))
```

---

**换行写法：输出查询**
`query = <stream>.writeStream.format(<格式>).outputMode(<模式>).start()`

```python
# 启动输出查询
query = word_counts.writeStream \
    .format("console") \
    .outputMode("complete") \
    .start()

query.awaitTermination()
```

---

**基本写法：输出模式**
`.outputMode(<模式>)`

```python
# 输出模式
# append: 仅输出新行（默认）
# complete: 输出所有结果
# update: 仅输出变化的行
query = stream.writeStream.outputMode("update").format("console").start()
```

---

**基本写法：触发器**
`.trigger(processingTime=<间隔>)`

```python
# 设置触发器
from pyspark.sql.streaming import Trigger

query = stream.writeStream \
    .trigger(processingTime="10 seconds") \
    .format("console") \
    .start()
```

---

**基本写法：检查点**
`.option("checkpointLocation", <路径>)`

```python
# 设置检查点
query = stream.writeStream \
    .option("checkpointLocation", "checkpoint/") \
    .format("parquet") \
    .start("output/")
```

---

**基本写法：水印**
`<stream>.withWatermark(<时间列>, <延迟阈值>)`

```python
# 设置水印（处理迟到数据）
from pyspark.sql import functions as F

result = stream \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(F.window("timestamp", "5 minutes"), "word") \
    .count()
```
