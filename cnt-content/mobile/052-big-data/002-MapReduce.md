# 大数据 MapReduce

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## MapReduce 命令

**基本写法：运行 MapReduce 作业**
`hadoop jar <jar包> <主类> <输入路径> <输出路径>`

```bash
# 运行 WordCount 示例
hadoop jar hadoop-mapreduce-examples.jar wordcount /input /output
```

---

**基本写法：查看作业列表**
`mapred job -list`

```bash
# 查看正在运行的作业
mapred job -list
```

---

**基本写法：杀死作业**
`mapred job -kill <作业ID>`

```bash
# 终止指定作业
mapred job -kill job_1234567890_0001
```

---

**基本写法：查看作业状态**
`mapred job -status <作业ID>`

```bash
# 查看作业详细状态
mapred job -status job_1234567890_0001
```

---

## Mapper 实现

**换行写法：Python Mapper 实现**
`#!/usr/bin/env python3`
`import sys`
`for line in sys.stdin:`
`    <处理逻辑>`
`    print(f"{<key>}\t{<value>}")`

```python
#!/usr/bin/env python3
# WordCount Mapper
import sys

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        print(f"{word}\t1")
```

---

**换行写法：Java Mapper 实现**
`public class <Mapper类> extends Mapper<KEYIN, VALUEIN, KEYOUT, VALUEOUT> {`
`    protected void map(KEYIN key, VALUEIN value, Context context) {`
`        <处理逻辑>`
`    }`
`}`

```java
// Java WordCount Mapper
public class WordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String[] words = value.toString().split("\\s+");
        for (String w : words) {
            word.set(w);
            context.write(word, one);
        }
    }
}
```

---

## Reducer 实现

**换行写法：Python Reducer 实现**
`#!/usr/bin/env python3`
`import sys`
`from collections import defaultdict`
`counts = defaultdict(int)`
`for line in sys.stdin:`
`    key, value = line.strip().split("\t")`
`    counts[key] += int(value)`
`for key, count in counts.items():`
`    print(f"{key}\t{count}")`

```python
#!/usr/bin/env python3
# WordCount Reducer
import sys
from collections import defaultdict

counts = defaultdict(int)
for line in sys.stdin:
    key, value = line.strip().split("\t")
    counts[key] += int(value)

for key, count in counts.items():
    print(f"{key}\t{count}")
```

---

**换行写法：Java Reducer 实现**
`public class <Reducer类> extends Reducer<KEYIN, VALUEIN, KEYOUT, VALUEOUT> {`
`    protected void reduce(KEYIN key, Iterable<VALUEIN> values, Context context) {`
`        <聚合逻辑>`
`    }`
`}`

```java
// Java WordCount Reducer
public class WordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    private IntWritable result = new IntWritable();

    @Override
    protected void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
        int sum = 0;
        for (IntWritable val : values) {
            sum += val.get();
        }
        result.set(sum);
        context.write(key, result);
    }
}
```

---

## 使用 Hadoop Streaming

**基本写法：运行 Streaming 作业**
`hadoop jar streaming.jar -input <输入> -output <输出> -mapper <mapper脚本> -reducer <reducer脚本>`

```bash
# 使用 Python 运行 MapReduce
hadoop jar hadoop-streaming.jar \
    -input /input \
    -output /output \
    -mapper mapper.py \
    -reducer reducer.py \
    -file mapper.py \
    -file reducer.py
```

---

**基本写法：指定 Java 类**
`hadoop jar streaming.jar -mapper <Java类> -reducer <Java类>`

```bash
# 指定 Java 类作为 Mapper/Reducer
hadoop jar hadoop-streaming.jar \
    -input /input \
    -output /output \
    -mapper "com.example.Mapper" \
    -reducer "com.example.Reducer"
```

---

**基本写法：设置环境变量**
`hadoop jar streaming.jar -cmdenv <变量名>=<值>`

```bash
# 设置环境变量
hadoop jar hadoop-streaming.jar \
    -input /input -output /output \
    -mapper mapper.py -reducer reducer.py \
    -cmdenv PYTHONPATH=/usr/lib/python3
```

---

## Combiner 优化

**基本写法：设置 Combiner**
`hadoop jar streaming.jar -combiner <combiner脚本>`

```bash
# 使用 Combiner 减少数据传输
hadoop jar hadoop-streaming.jar \
    -input /input -output /output \
    -mapper mapper.py \
    -combiner reducer.py \
    -reducer reducer.py \
    -file mapper.py -file reducer.py
```

---

## Partitioner 分区

**基本写法：设置 Partitioner**
`hadoop jar streaming.jar -partitioner <分区类>`

```bash
# 自定义分区器
hadoop jar hadoop-streaming.jar \
    -input /input -output /output \
    -mapper mapper.py -reducer reducer.py \
    -partitioner org.apache.hadoop.mapreduce.lib.partition.HashPartitioner \
    -numReduceTasks 3
```

---

## 作业配置

**基本写法：设置 Reduce 任务数**
`-D mapreduce.job.reduces=<数量>`

```bash
# 设置 Reduce 任务数为 5
hadoop jar hadoop-streaming.jar \
    -D mapreduce.job.reduces=5 \
    -input /input -output /output \
    -mapper mapper.py -reducer reducer.py
```

---

**基本写法：设置输入格式**
`-D mapreduce.job.inputformat.class=<输入格式类>`

```bash
# 指定输入格式
hadoop jar hadoop-streaming.jar \
    -inputformat org.apache.hadoop.mapreduce.lib.input.TextInputFormat \
    -input /input -output /output \
    -mapper mapper.py -reducer reducer.py
```

---

**基本写法：设置输出格式**
`-D mapreduce.job.outputformat.class=<输出格式类>`

```bash
# 指定输出格式
hadoop jar hadoop-streaming.jar \
    -outputformat org.apache.hadoop.mapreduce.lib.output.TextOutputFormat \
    -input /input -output /output \
    -mapper mapper.py -reducer reducer.py
```

---

## 实战示例

**换行写法：词频统计完整流程**
`hadoop jar streaming.jar \`
`    -input /input \`
`    -output /output \`
`    -mapper "python3 mapper.py" \`
`    -reducer "python3 reducer.py" \`
`    -file mapper.py \`
`    -file reducer.py`

```bash
# 完整的词频统计命令
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
    -input /user/hadoop/input \
    -output /user/hadoop/output \
    -mapper "python3 mapper.py" \
    -reducer "python3 reducer.py" \
    -file mapper.py \
    -file reducer.py \
    -D mapreduce.job.reduces=2
```

---

**换行写法：去重 MapReduce**
`mapper: print(line.strip())`
`reducer: print(key)`

```python
# 去重 Mapper
import sys
for line in sys.stdin:
    print(line.strip())

# 去重 Reducer  
import sys
last_key = None
for line in sys.stdin:
    key = line.strip()
    if key != last_key:
        print(key)
        last_key = key
```

---

**换行写法：排序 MapReduce**
`mapper: print(f"{int(line.strip())}\t")`
`reducer: 依次输出`

```python
# 排序 Mapper（利用 Shuffle 自动排序）
import sys
for line in sys.stdin:
    num = int(line.strip())
    print(f"{num}\t")

# 排序 Reducer
import sys
for line in sys.stdin:
    num = line.strip().split("\t")[0]
    print(num)
```

---

**换行写法：自定义计数器**
`context.getCounter(<组名>, <计数器名>).increment(1)`

```java
// 在 Java Mapper/Reducer 中使用计数器
context.getCounter("Custom", "TotalRecords").increment(1);
context.getCounter("Custom", "ValidRecords").increment(1);
```
