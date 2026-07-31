# Redis Cluster 集群命令速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 集群创建

**基本写法：redis-cli 创建集群**
`redis-cli --cluster create <节点1> <节点2> ... --cluster-replicas <每主几个从>`
```bash
# 创建 3 主 3 从集群
redis-cli --cluster create \
  192.168.1.1:7000 192.168.1.2:7000 192.168.1.3:7000 \
  192.168.1.1:7001 192.168.1.2:7001 192.168.1.3:7001 \
  --cluster-replicas 1

# cluster-replicas 1 表示每个主库配 1 个从库
```

---

**基本写法：节点配置文件**
`cluster-enabled yes`
```conf
# 每个节点的 redis.conf
port 7000
cluster-enabled yes
cluster-config-file nodes-7000.conf
cluster-node-timeout 15000
cluster-announce-ip 192.168.1.1
cluster-announce-port 7000
cluster-announce-bus-port 17000

# 集群总线端口 = 数据端口 + 10000
# 节点间通信用总线端口，客户端用数据端口
```

---

## CLUSTER 节点管理

**基本写法：CLUSTER MEET 加入节点**
`CLUSTER MEET <ip> <port>`
```redis
-- 向集群添加新节点
CLUSTER MEET 192.168.1.4 7000

-- 查看集群节点列表
CLUSTER NODES
-- 返回格式：id ip:port@bus flags master ping pong epoch link slots
-- flags: master/slave/fail/myself/handshake/noaddr
```

---

**基本写法：CLUSTER INFO 集群状态**
`CLUSTER INFO`
```redis
-- 查看集群信息
CLUSTER INFO
-- 关键字段：
-- cluster_state:ok
-- cluster_slots_assigned:16384
-- cluster_slots_ok:16384
-- cluster_known_nodes:6
-- cluster_size:3
```

---

## 槽位管理

**基本写法：CLUSTER SLOTS 槽位分布**
`CLUSTER SLOTS`
```redis
-- 查看槽位分配
CLUSTER SLOTS
-- 返回：起始槽-结束槽-主节点信息-从节点信息
-- 如：0-5460 [ip,port,id] [从ip,从port,从id]
```

---

**基本写法：CLUSTER COUNTKEYSINSLOT**
`CLUSTER COUNTKEYSINSLOT <slot>`
```redis
-- 统计某槽位的 key 数量
CLUSTER COUNTKEYSINSLOT 5500

-- 计算 key 的槽位
CLUSTER KEYSLOT mykey
-- Redis 用 CRC16(key) % 16384 计算槽位
```

---

**基本写法：分配槽位**
`CLUSTER ADDSLOTS <slot> [<slot>...]`
```redis
-- 给当前节点分配槽位
CLUSTER ADDSLOTS 0 1 2 3 4 5

-- 删除槽位
CLUSTER DELSLOTS 0 1 2

-- 批量分配（创建集群时用 bash 循环）
# for i in {0..5460}; do redis-cli -p 7000 CLUSTER ADDSLOTS $i; done
```

---

**基本写法：迁移槽位**
`CLUSTER SETSLOT <slot> MIGRATING <目标nodeid> | IMPORTING <源nodeid>`
```redis
-- 槽位迁移流程（手动迁移 slot 100 从 A 到 B）
-- 1. B 准备接收
CLUSTER SETSLOT 100 IMPORTING <A的nodeid>

-- 2. A 准备迁出
CLUSTER SETSLOT 100 MIGRATING <B的nodeid>

-- 3. 迁移 key
MIGRATE <B_ip> <B_port> '' 0 5000 KEYS key1 key2

-- 4. 两端都确认新归属
CLUSTER SETSLOT 100 NODE <B的nodeid>

-- 推荐：用 redis-cli --cluster reshard 自动迁移
```

---

## redis-cli 集群工具

**基本写法：集群重平衡**
`redis-cli --cluster reshard <任意节点>`
```bash
# 交互式迁移槽位
redis-cli --cluster reshard 192.168.1.1:7000
# 输入：迁移多少槽位、目标节点id、源节点（all 或 id 列表）

# 自动平衡槽位分布
redis-cli --cluster rebalance 192.168.1.1:7000

# 检查集群健康
redis-cli --cluster check 192.168.1.1:7000

# 修复槽位异常
redis-cli --cluster fix 192.168.1.1:7000
```

---

**基本写法：添加/移除节点**
`redis-cli --cluster add-node <新节点> <集群任意节点>`
```bash
# 添加主节点
redis-cli --cluster add-node 192.168.1.4:7000 192.168.1.1:7000

# 添加从节点（指定主库 id）
redis-cli --cluster add-node 192.168.1.4:7001 192.168.1.1:7000 \
  --cluster-slave --cluster-master-id <主库nodeid>

# 移除节点（先迁移槽位）
redis-cli --cluster del-node 192.168.1.1:7000 <待移除nodeid>
```

---

## 客户端集群操作

**基本写法：-c 启用集群模式**
`redis-cli -c -h <host> -p <port>`
```bash
# -c 自动跟随 MOVED/ASK 重定向
redis-cli -c -h 192.168.1.1 -p 7000

# 不加 -c 时遇到跨槽 key 会报错并返回 MOVED
# MOVED 5474 192.168.1.2:7000 表示去 2 号节点查
```

---

**基本写法：Hash Tag 保证同槽**
`SET {tag}key1 v1 | SET {tag}key2 v2`
```redis
-- 用 {} 指定 hash tag，大括号内内容参与槽位计算
SET {user100}.name 'Alice'
SET {user100}.age '30'
SET {user100}.email 'a@x.com'

-- 三个 key 槽位相同，可在同节点执行 MGET/事务
MGET {user100}.name {user100}.age {user100}.email

-- 适用于多 key 操作（事务/聚合）必须在同节点
```

---

## 集群限制

**基本写法：跨槽操作限制**
`<多key命令> 仅当所有 key 同槽时可用`
```redis
-- 以下命令要求所有 key 在同一槽位，否则报 CROSSSLOT 错误
MGET k1 k2 k3          -- 若槽位不同则失败
MULTI / EXEC            -- 事务中跨槽 key 失败
SINTER s1 s2            -- 集合运算跨槽失败
ZUNIONSTORE dst 2 s1 s2

-- 解决方案：用 Hash Tag {tag} 强制同槽
MGET {tag}k1 {tag}k2 {tag}k3
```

---

## 故障转移

**基本写法：手动故障转移**
`CLUSTER FAILOVER [FORCE|TAKEOVER]`
```redis
-- 从库执行，请求升主（需主库同意）
CLUSTER FAILOVER

-- FORCE：不等主库确认，直接升主（主库不可达时）
CLUSTER FAILOVER FORCE

-- TAKEOVER：跳过集群协商，强制升主（危险，可能脑裂）
CLUSTER FAILOVER TAKEOVER

-- 流程：从库停止复制 -> 通知主库 -> 主库停止处理 -> 从库升主
```

---

**基本写法：故障节点处理**
`CLUSTER FORGET <nodeid>`
```redis
-- 从集群中移除故障节点（需对所有存活节点执行）
CLUSTER FORGET <故障nodeid>

-- 重置当前节点集群状态
CLUSTER RESET [HARD|SOFT]
-- SOFT：保留数据，重置集群信息
-- HARD：清空数据 + 重置集群（重新加入用）
```
