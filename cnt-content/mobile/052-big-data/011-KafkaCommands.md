# 大数据 Kafka 命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Topic 管理

**基本写法：创建 Topic**
`kafka-topics.sh --create --bootstrap-server <broker地址> --topic <主题名> --partitions <分区数> --replication-factor <副本数>`

```bash
# 创建 Topic
kafka-topics.sh --create \
    --bootstrap-server localhost:9092 \
    --topic my_topic \
    --partitions 3 \
    --replication-factor 2
```

---

**基本写法：查看 Topic 列表**
`kafka-topics.sh --list --bootstrap-server <broker地址>`

```bash
# 查看所有 Topic
kafka-topics.sh --list --bootstrap-server localhost:9092
```

---

**基本写法：查看 Topic 详情**
`kafka-topics.sh --describe --bootstrap-server <broker地址> --topic <主题名>`

```bash
# 查看 Topic 详细信息
kafka-topics.sh --describe \
    --bootstrap-server localhost:9092 \
    --topic my_topic
```

---

**基本写法：删除 Topic**
`kafka-topics.sh --delete --bootstrap-server <broker地址> --topic <主题名>`

```bash
# 删除 Topic
kafka-topics.sh --delete \
    --bootstrap-server localhost:9092 \
    --topic my_topic
```

---

**基本写法：增加分区**
`kafka-topics.sh --alter --bootstrap-server <broker地址> --topic <主题名> --partitions <新分区数>`

```bash
# 增加 Topic 分区数
kafka-topics.sh --alter \
    --bootstrap-server localhost:9092 \
    --topic my_topic \
    --partitions 5
```

---

**基本写法：修改配置**
`kafka-topics.sh --alter --bootstrap-server <broker地址> --topic <主题名> --config <键>=<值>`

```bash
# 修改 Topic 配置
kafka-topics.sh --alter \
    --bootstrap-server localhost:9092 \
    --topic my_topic \
    --config retention.ms=604800000
```

---

**基本写法：删除配置**
`kafka-topics.sh --alter --bootstrap-server <broker地址> --topic <主题名> --delete-config <键>`

```bash
# 删除 Topic 配置
kafka-topics.sh --alter \
    --bootstrap-server localhost:9092 \
    --topic my_topic \
    --delete-config retention.ms
```

---

## 生产者

**基本写法：控制台生产者**
`kafka-console-producer.sh --bootstrap-server <broker地址> --topic <主题名>`

```bash
# 启动控制台生产者
kafka-console-producer.sh \
    --bootstrap-server localhost:9092 \
    --topic my_topic
```

---

**基本写法：带 Key 生产者**
`kafka-console-producer.sh --bootstrap-server <broker地址> --topic <主题名> --property "key.separator=:" --property "parse.key=true"`

```bash
# 带 Key 的生产者（格式: key:value）
kafka-console-producer.sh \
    --bootstrap-server localhost:9092 \
    --topic my_topic \
    --property "key.separator=:" \
    --property "parse.key=true"
```

---

**基本写法：从文件发送**
`kafka-console-producer.sh --bootstrap-server <broker地址> --topic <主题名> < <文件>`

```bash
# 从文件发送消息
kafka-console-producer.sh \
    --bootstrap-server localhost:9092 \
    --topic my_topic < messages.txt
```

---

**基本写法：指定 ACK**
`kafka-console-producer.sh --bootstrap-server <broker地址> --topic <主题名> --request-required-acks <0|1|all>`

```bash
# 指定 ACK 级别
kafka-console-producer.sh \
    --bootstrap-server localhost:9092 \
    --topic my_topic \
    --request-required-acks all
```

---

## 消费者

**基本写法：控制台消费者**
`kafka-console-consumer.sh --bootstrap-server <broker地址> --topic <主题名> --from-beginning`

```bash
# 启动控制台消费者（从头开始消费）
kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic my_topic \
    --from-beginning
```

---

**基本写法：指定消费者组**
`kafka-console-consumer.sh --bootstrap-server <broker地址> --topic <主题名> --group <组名>`

```bash
# 指定消费者组
kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic my_topic \
    --group my_group
```

---

**基本写法：显示 Key 和分区**
`kafka-console-consumer.sh --bootstrap-server <broker地址> --topic <主题名> --property "print.key=true" --property "print.partition=true"`

```bash
# 显示 Key 和分区信息
kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic my_topic \
    --property "print.key=true" \
    --property "print.partition=true" \
    --property "print.timestamp=true"
```

---

**基本写法：限制消费数量**
`kafka-console-consumer.sh --bootstrap-server <broker地址> --topic <主题名> --max-messages <数量>`

```bash
# 最多消费 100 条消息
kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic my_topic \
    --max-messages 100
```

---

**基本写法：超时退出**
`kafka-console-consumer.sh --bootstrap-server <broker地址> --topic <主题名> --timeout-ms <毫秒>`

```bash
# 10 秒无消息后退出
kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic my_topic \
    --timeout-ms 10000
```

---

## 消费者组管理

**基本写法：查看消费者组列表**
`kafka-consumer-groups.sh --list --bootstrap-server <broker地址>`

```bash
# 查看所有消费者组
kafka-consumer-groups.sh --list \
    --bootstrap-server localhost:9092
```

---

**基本写法：查看消费者组详情**
`kafka-consumer-groups.sh --describe --bootstrap-server <broker地址> --group <组名>`

```bash
# 查看消费者组详情
kafka-consumer-groups.sh --describe \
    --bootstrap-server localhost:9092 \
    --group my_group
```

---

**基本写法：重置偏移量到最早**
`kafka-consumer-groups.sh --reset-offsets --bootstrap-server <broker地址> --group <组名> --topic <主题名> --to-earliest --execute`

```bash
# 重置偏移量到最早
kafka-consumer-groups.sh --reset-offsets \
    --bootstrap-server localhost:9092 \
    --group my_group \
    --topic my_topic \
    --to-earliest \
    --execute
```

---

**基本写法：重置偏移量到最新**
`kafka-consumer-groups.sh --reset-offsets --bootstrap-server <broker地址> --group <组名> --topic <主题名> --to-latest --execute`

```bash
# 重置偏移量到最新
kafka-consumer-groups.sh --reset-offsets \
    --bootstrap-server localhost:9092 \
    --group my_group \
    --topic my_topic \
    --to-latest \
    --execute
```

---

**基本写法：重置到指定偏移量**
`kafka-consumer-groups.sh --reset-offsets --bootstrap-server <broker地址> --group <组名> --topic <主题名> --to-offset <偏移量> --execute`

```bash
# 重置到指定偏移量
kafka-consumer-groups.sh --reset-offsets \
    --bootstrap-server localhost:9092 \
    --group my_group \
    --topic my_topic \
    --to-offset 100 \
    --execute
```

---

**基本写法：重置到指定时间**
`kafka-consumer-groups.sh --reset-offsets --bootstrap-server <broker地址> --group <组名> --topic <主题名> --to-datetime <时间> --execute`

```bash
# 重置到指定时间
kafka-consumer-groups.sh --reset-offsets \
    --bootstrap-server localhost:9092 \
    --group my_group \
    --topic my_topic \
    --to-datetime 2024-01-01T00:00:00.000 \
    --execute
```

---

**基本写法：删除消费者组**
`kafka-consumer-groups.sh --delete --bootstrap-server <broker地址> --group <组名>`

```bash
# 删除消费者组
kafka-consumer-groups.sh --delete \
    --bootstrap-server localhost:9092 \
    --group my_group
```

---

## 配置管理

**基本写法：查看 Topic 配置**
`kafka-configs.sh --describe --bootstrap-server <broker地址> --entity-type topics --entity-name <主题名>`

```bash
# 查看 Topic 配置
kafka-configs.sh --describe \
    --bootstrap-server localhost:9092 \
    --entity-type topics \
    --entity-name my_topic
```

---

**基本写法：修改 Topic 配置**
`kafka-configs.sh --alter --bootstrap-server <broker地址> --entity-type topics --entity-name <主题名> --add-config <键>=<值>`

```bash
# 修改 Topic 配置
kafka-configs.sh --alter \
    --bootstrap-server localhost:9092 \
    --entity-type topics \
    --entity-name my_topic \
    --add-config retention.ms=86400000
```

---

**基本写法：查看 Broker 配置**
`kafka-configs.sh --describe --bootstrap-server <broker地址> --entity-type brokers --entity-name <broker ID>`

```bash
# 查看 Broker 配置
kafka-configs.sh --describe \
    --bootstrap-server localhost:9092 \
    --entity-type brokers \
    --entity-name 1
```

---

## 生产者性能测试

**基本写法：性能测试**
`kafka-producer-perf-test.sh --topic <主题名> --num-records <数量> --record-size <字节> --throughput <吞吐> --bootstrap-server <broker地址>`

```bash
# 生产者性能测试
kafka-producer-perf-test.sh \
    --topic my_topic \
    --num-records 100000 \
    --record-size 1024 \
    --throughput -1 \
    --bootstrap-server localhost:9092
```

---

## 消费者性能测试

**基本写法：消费者性能测试**
`kafka-consumer-perf-test.sh --topic <主题名> --messages <数量> --bootstrap-server <broker地址>`

```bash
# 消费者性能测试
kafka-consumer-perf-test.sh \
    --topic my_topic \
    --messages 100000 \
    --bootstrap-server localhost:9092
```

---

## 集群管理

**基本写法：查看集群信息**
`kafka-cluster.sh --cluster-id --bootstrap-server <broker地址>`

```bash
# 查看 Kafka 集群 ID
kafka-cluster.sh --cluster-id \
    --bootstrap-server localhost:9092
```

---

**基本写法：查看 Broker 列表**
`kafka-broker-api-versions.sh --bootstrap-server <broker地址>`

```bash
# 查看 Broker API 版本
kafka-broker-api-versions.sh \
    --bootstrap-server localhost:9092
```

---

## ACL 权限管理

**基本写法：查看 ACL**
`kafka-acls.sh --list --bootstrap-server <broker地址>`

```bash
# 查看所有 ACL
kafka-acls.sh --list \
    --bootstrap-server localhost:9092
```

---

**基本写法：添加 ACL**
`kafka-acls.sh --add --bootstrap-server <broker地址> --allow-principal <主体> --operation <操作> --topic <主题名>`

```bash
# 添加生产者权限
kafka-acls.sh --add \
    --bootstrap-server localhost:9092 \
    --allow-principal User:alice \
    --operation Write \
    --topic my_topic
```

---

**基本写法：添加消费者 ACL**
`kafka-acls.sh --add --bootstrap-server <broker地址> --allow-principal <主体> --operation Read --topic <主题名> --group <组名>`

```bash
# 添加消费者权限
kafka-acls.sh --add \
    --bootstrap-server localhost:9092 \
    --allow-principal User:bob \
    --operation Read \
    --topic my_topic \
    --group my_group
```

---

**基本写法：删除 ACL**
`kafka-acls.sh --remove --bootstrap-server <broker地址> --allow-principal <主体> --operation <操作> --topic <主题名>`

```bash
# 删除 ACL
kafka-acls.sh --remove \
    --bootstrap-server localhost:9092 \
    --allow-principal User:alice \
    --operation Write \
    --topic my_topic
```
