# 大数据 Spark 优化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 配置优化

**基本写法：设置执行器内存**
`spark.conf.set("spark.executor.memory", "<大小>")`

```python
# 设置执行器内存
spark.conf.set("spark.executor.memory", "4g")
```

---

**基本写法：设置驱动器内存**
`spark.conf.set("spark.driver.memory", "<大小>")`

```python
# 设置驱动器内存
spark.conf.set("spark.driver.memory", "2g")
```

---

**基本写法：设置执行器核心数**
`spark.conf.set("spark.executor.cores", "<数量>")`

```python
# 设置每个执行器的核心数
spark.conf.set("spark.executor.cores", "4")
```

---

**基本写法：设置执行器实例数**
`spark.conf.set("spark.executor.instances", "<数量>")`

```python
# 设置执行器实例数
spark.conf.set("spark.executor.instances", "10")
```

---

**基本写法：设置序列化器**
`spark.conf.set("spark.serializer", "<序列化器>")`

```python
# 使用 Kryo 序列化器
spark.conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
```

---

**基本写法：设置内存溢出比例**
`spark.conf.set("spark.memory.fraction", "<比例>")`

```python
# 设置用于执行和存储的内存比例（默认 0.6）
spark.conf.set("spark.memory.fraction", "0.7")
```

---

**基本写法：设置存储内存比例**
`spark.conf.set("spark.memory.storageFraction", "<比例>")`

```python
# 设置存储内存占可用内存的比例（默认 0.5）
spark.conf.set("spark.memory.storageFraction", "0.3")
```

---

## 数据倾斜处理

**换行写法：加盐打散倾斜键**
`from pyspark.sql import functions as F`
`df = df.withColumn("salt", F.expr("concat(id, '_', cast(rand() * 10 as int))"))`

```python
# 对倾斜键加盐打散
from pyspark.sql import functions as F

# 给倾斜键加随机前缀
df = df.withColumn("salted_key",
    F.concat(F.lit("salt_"), F.expr("cast(rand() * 10 as int)"), F.lit("_"), F.col("id")))
```

---

**换行写法：两阶段聚合**
`# 第一阶段：局部聚合`
`partial = df.groupBy("salted_key").agg(F.sum("value").alias("partial_sum"))`
`# 第二阶段：全局聚合`
`result = partial.groupBy("id").agg(F.sum("partial_sum").alias("total"))`

```python
# 两阶段聚合解决数据倾斜
# 第一阶段：加盐局部聚合
partial = df.withColumn(
    "salted_key",
    F.concat(F.lit("salt_"), F.expr("cast(rand() * 10 as int)"), F.lit("_"), F.col("id"))
).groupBy("salted_key").agg(F.sum("value").alias("partial_sum"))

# 第二阶段：去盐全局聚合
result = partial.withColumn(
    "id",
    F.expr("substring(salted_key, length('salt_X_') + 1)")
).groupBy("id").agg(F.sum("partial_sum").alias("total"))
```

---

**基本写法：广播小表**
`spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "<字节>")`

```python
# 提高自动广播阈值
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "104857600")  # 100MB
```

---

**基本写法：手动广播提示**
`df.hint("broadcast")`

```python
# 手动提示广播小表
result = big_df.join(small_df.hint("broadcast"), "id")
```

---

## 分区优化

**基本写法：重新分区**
`df.repartition(<分区数>)`

```python
# 重新分区
df = df.repartition(100)
```

---

**基本写法：按列分区**
`df.repartition(<分区数>, <列>)`

```python
# 按列分区（用于 Join 优化）
df = df.repartition(100, "join_key")
```

---

**基本写法：减少分区**
`df.coalesce(<分区数>)`

```python
# 合并分区（不产生 Shuffle）
df = df.coalesce(10)
```

---

**基本写法：设置默认 Shuffle 分区数**
`spark.conf.set("spark.sql.shuffle.partitions", "<数量>")`

```python
# 设置 Shuffle 分区数（默认 200）
spark.conf.set("spark.sql.shuffle.partitions", "500")
```

---

**基本写法：自适应查询执行**
`spark.conf.set("spark.sql.adaptive.enabled", "true")`

```python
# 启用自适应查询执行（AQE）
spark.conf.set("spark.sql.adaptive.enabled", "true")
```

---

**基本写法：自适应分区合并**
`spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")`

```python
# 自适应合并小分区
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
```

---

**基本写法：自适应倾斜处理**
`spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")`

```python
# 自适应处理 Join 数据倾斜
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
```

---

## 缓存优化

**基本写法：缓存 DataFrame**
`df.cache()`

```python
# 缓存 DataFrame（默认 MEMORY_AND_DISK）
df.cache()
```

---

**基本写法：指定存储级别**
`df.persist(<存储级别>)`

```python
# 指定存储级别
from pyspark import StorageLevel
df.persist(StorageLevel.MEMORY_AND_DISK_SER)
```

---

**基本写法：解除缓存**
`df.unpersist()`

```python
# 解除缓存
df.unpersist()
```

---

**基本写法：清空缓存**
`spark.catalog.clearCache()`

```python
# 清空所有缓存
spark.catalog.clearCache()
```

---

## 文件优化

**基本写法：合并小文件**
`spark.conf.set("spark.sql.files.maxRecordsPerFile", "<数量>")`

```python
# 设置每个文件最大记录数
spark.conf.set("spark.sql.files.maxRecordsPerFile", "1000000")
```

---

**基本写法：设置最大分区字节数**
`spark.conf.set("spark.sql.files.maxPartitionBytes", "<字节>")`

```python
# 设置每个分区最大字节数（默认 128MB）
spark.conf.set("spark.sql.files.maxPartitionBytes", "134217728")
```

---

**基本写法：设置打开文件数**
`spark.conf.set("spark.sql.files.openCostInBytes", "<字节>")`

```python
# 设置打开文件的估算成本
spark.conf.set("spark.sql.files.openCostInBytes", "8388608")
```

---

## Join 优化

**基本写法：启用广播 Join**
`spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "<字节>")`

```python
# 设置自动广播 Join 阈值（默认 10MB）
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "10485760")
```

---

**基本写法：Sort Merge Join**
`spark.conf.set("spark.sql.join.preferSortMergeJoin", "true")`

```python
# 启用 Sort Merge Join（大表 Join）
spark.conf.set("spark.sql.join.preferSortMergeJoin", "true")
```

---

**基本写法：使用 Bucket Join**
`df1.write.bucketBy(<桶数>, <列>).saveAsTable(<表名>)`

```python
# 创建分桶表优化 Join
df.write.bucketBy(100, "id").sortBy("id").saveAsTable("bucketed_table")
```

---

**基本写法：启用自适应广播**
`spark.conf.set("spark.sql.adaptive.localShuffleReader.enabled", "true")`

```python
# 自适应本地 Shuffle 读取
spark.conf.set("spark.sql.adaptive.localShuffleReader.enabled", "true")
```

---

## 内存管理

**基本写法：设置执行内存**
`spark.conf.set("spark.executor.memoryOverhead", "<大小>")`

```python
# 设置堆外内存
spark.conf.set("spark.executor.memoryOverhead", "1g")
```

---

**基本写法：启用堆外内存**
`spark.conf.set("spark.memory.offHeap.enabled", "true")`

```python
# 启用堆外内存
spark.conf.set("spark.memory.offHeap.enabled", "true")
spark.conf.set("spark.memory.offHeap.size", "1g")
```

---

**基本写法：设置 Python 内存**
`spark.conf.set("spark.executor.pyspark.memory", "<大小>")`

```python
# 设置 Python worker 内存
spark.conf.set("spark.executor.pyspark.memory", "1g")
```

---

## 序列化优化

**基本写法：使用 Kryo 序列化**
`spark.conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")`

```python
# 使用 Kryo 序列化器（比 Java 序列化快 10 倍）
spark.conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
```

---

**基本写法：注册 Kryo 类**
`spark.conf.set("spark.kryo.registrationRequired", "true")`

```python
# 要求注册所有类
spark.conf.set("spark.kryo.registrationRequired", "true")
```

---

**基本写法：启用 RDD 序列化**
`spark.conf.set("spark.rdd.compress", "true")`

```python
# 启用 RDD 压缩
spark.conf.set("spark.rdd.compress", "true")
```

---

## Shuffle 优化

**基本写法：设置 Shuffle 管理器**
`spark.conf.set("spark.shuffle.manager", "<管理器>")`

```python
# 设置 Shuffle 管理器（默认 sort）
spark.conf.set("spark.shuffle.manager", "sort")
```

---

**基本写法：设置 Shuffle 缓冲区**
`spark.conf.set("spark.shuffle.file.buffer", "<大小>")`

```python
# 设置 Shuffle 文件缓冲区大小（默认 32KB）
spark.conf.set("spark.shuffle.file.buffer", "64kb")
```

---

**基本写法：设置 Shuffle 后内存比例**
`spark.conf.set("spark.shuffle.memoryFraction", "<比例>")`

```python
# 设置 Shuffle 内存比例（默认 0.2）
spark.conf.set("spark.shuffle.memoryFraction", "0.3")
```

---

**基本写法：启用 Shuffle 服务**
`spark.conf.set("spark.shuffle.service.enabled", "true")`

```python
# 启用外部 Shuffle 服务
spark.conf.set("spark.shuffle.service.enabled", "true")
```

---

## 动态分配

**基本写法：启用动态分配**
`spark.conf.set("spark.dynamicAllocation.enabled", "true")`

```python
# 启用动态资源分配
spark.conf.set("spark.dynamicAllocation.enabled", "true")
```

---

**基本写法：设置最小执行器数**
`spark.conf.set("spark.dynamicAllocation.minExecutors", "<数量>")`

```python
# 设置最小执行器数
spark.conf.set("spark.dynamicAllocation.minExecutors", "2")
```

---

**基本写法：设置最大执行器数**
`spark.conf.set("spark.dynamicAllocation.maxExecutors", "<数量>")`

```python
# 设置最大执行器数
spark.conf.set("spark.dynamicAllocation.maxExecutors", "20")
```

---

**基本写法：设置初始执行器数**
`spark.conf.set("spark.dynamicAllocation.initialExecutors", "<数量>")`

```python
# 设置初始执行器数
spark.conf.set("spark.dynamicAllocation.initialExecutors", "5")
```

---

## SQL 优化

**基本写法：启用列式存储**
`spark.conf.set("spark.sql.inMemoryColumnarStorage.compressed", "true")`

```python
# 启用列式存储压缩
spark.conf.set("spark.sql.inMemoryColumnarStorage.compressed", "true")
```

---

**基本写法：设置批处理大小**
`spark.conf.set("spark.sql.inMemoryColumnarStorage.batchSize", "<数量>")`

```python
# 设置列式存储批处理大小
spark.conf.set("spark.sql.inMemoryColumnarStorage.batchSize", "10000")
```

---

**基本写法：启用谓词下推**
`spark.conf.set("spark.sql.parquet.filterPushdown", "true")`

```python
# 启用 Parquet 谓词下推
spark.conf.set("spark.sql.parquet.filterPushdown", "true")
```

---

**基本写法：启用wholeStageCodegen**
`spark.conf.set("spark.sql.codegen.wholeStage", "true")`

```python
# 启用全阶段代码生成
spark.conf.set("spark.sql.codegen.wholeStage", "true")
```

---

**基本写法：启用向量化读取**
`spark.conf.set("spark.sql.parquet.enableVectorizedReader", "true")`

```python
# 启用 Parquet 向量化读取
spark.conf.set("spark.sql.parquet.enableVectorizedReader", "true")
```

---

## 监控与调优

**基本写法：启用事件日志**
`spark.conf.set("spark.eventLog.enabled", "true")`

```python
# 启用事件日志记录
spark.conf.set("spark.eventLog.enabled", "true")
spark.conf.set("spark.eventLog.dir", "hdfs://namenode:8020/spark-logs")
```

---

**基本写法：启动历史服务器**
`start-history-server.sh`

```bash
# 启动 Spark 历史服务器
start-history-server.sh
```

---

**基本写法：查看作业进度**
`spark.sparkContext.statusTracker()`

```python
# 获取作业状态
status = sc.statusTracker()
print(status.getActiveJobIds())
```

---

**基本写法：获取执行器信息**
`sc.parallelize(range(1)).map(lambda x: ...).collect()`

```python
# 获取执行器内存使用情况
def get_memory(x):
    import psutil
    process = psutil.Process()
    return process.memory_info().rss

memory_usage = sc.parallelize(range(1)).map(get_memory).collect()
print(f"Executor memory: {memory_usage[0] / 1024 / 1024} MB")
```
