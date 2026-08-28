# Redis Sentinel 哨兵命令速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 哨兵配置

**基本写法：sentinel.conf 配置**
`sentinel monitor <主库别名> <host> <port> <quorum>`
```conf
# sentinel.conf 配置文件
port 26379
sentinel monitor mymaster 192.168.1.10 6379 2
sentinel auth-pass mymaster <主库密码>
sentinel down-after-milliseconds mymaster 30000
sentinel parallel-syncs mymaster 1
sentinel failover-timeout mymaster 180000

# quorum=2：2 个哨兵同意才判定主观下线转客观下线
# down-after-milliseconds：30s 无响应判定下线
# parallel-syncs：故障转移时并行同步的从库数
# failover-timeout：故障转移超时
```

---

**基本写法：启动哨兵**
`redis-sentinel <配置文件> | redis-server <配置文件> --sentinel`
```bash
# 方式一：redis-sentinel 专用命令
redis-sentinel /etc/redis/sentinel.conf

# 方式二：redis-server 加 --sentinel 参数
redis-server /etc/redis/sentinel.conf --sentinel

# 集群部署：至少 3 个哨兵节点，分散部署
```

---

## 哨兵查询命令

**基本写法：SENTINEL masters**
`SENTINEL masters | SENTINEL master <主库别名>`
```redis
-- 查看所有被监控的主库
SENTINEL masters

-- 查看指定主库详情
SENTINEL master mymaster
-- 返回：name, ip, port, runid, role-reported, slaves, sentinels,
--       quorum, flags(master), down-after-milliseconds, etc.
```

---

**基本写法：查看从库与哨兵**
`SENTINEL slaves <主库别名> | SENTINEL sentinels <主库别名>`
```redis
-- 查看主库下的从库列表
SENTINEL slaves mymaster

-- 查看监控同一主库的其他哨兵
SENTINEL sentinels mymaster
```

---

**基本写法：获取主库地址**
`SENTINEL get-master-addr-by-name <主库别名>`
```redis
-- 客户端连接哨兵查询当前主库地址
SENTINEL get-master-addr-by-name mymaster
-- 返回：1) "192.168.1.11"  2) "6379"（故障转移后地址会变）
```

---

## 故障转移

**基本写法：手动故障转移**
`SENTINEL failover <主库别名>`
```redis
-- 手动触发故障转移，将从库提升为主库
SENTINEL failover mymaster

-- 故障转移流程：
-- 1. 哨兵标记主库下线
-- 2. 选举领头哨兵
-- 3. 选择最优从库（优先级>偏移量>runid）
-- 4. 从库执行 SLAVEOF NO ONE 升主
-- 5. 其他从库指向新主库
-- 6. 旧主恢复后变为从库
```

---

**基本写法：强制重置**
`SENTINEL reset <pattern>`
```redis
-- 重置匹配 pattern 的主库监控（清空状态重新发现）
SENTINEL reset my*
-- 重置所有
SENTINEL reset *

-- 重置后哨兵会重新发现主从拓扑
```

---

**基本写法：检查仲裁**
`SENTINEL ckquorum <主库别名>`
```redis
-- 检查当前哨兵数是否足够达成仲裁
SENTINEL ckquorum mymaster
-- 返回 OK 表示可用；返回 error 表示哨兵不足
```

---

## 故障转移原理

**基本写法：下线判定与选举**
`<主观下线> -> <客观下线> -> <_leader 选举> -> <选从升主>`
```redis
-- 1. 主观下线（SDOWN）：单个哨兵判定 down
--    条件：down-after-milliseconds 内无响应

-- 2. 客观下线（ODOWN）：quorum 个哨兵同意
--    通过 SENTINEL is-master-down-by-addr 投票

-- 3. Leader 选举：Raft 协议选领头哨兵执行转移

-- 4. 从库选举优先级：
--    a. replica-priority 值小的优先（0 永不升主）
--    b. 复制偏移量大的优先（数据更新）
--    c. runid 字典序小的优先
```

---

## 客户端连接哨兵

**基本写法：客户端订阅切换事件**
`SUBSCRIBE +switch-master | +sdown`
```redis
-- 客户端订阅哨兵频道感知主库切换
SUBSCRIBE +switch-master
-- 故障转移后收到：mymaster 192.168.1.10 6379 192.168.1.11 6379

-- 订阅下线事件
PSUBSCRIBE *

-- 常见事件频道：
-- +switch-master：主库切换
-- +sdown：主观下线
-- +odown：客观下线
-- +failover-state-*：故障转移各阶段
-- +slave-reconf-sent：从库重配置
```

---

## 哨兵运维

**基本写法：动态修改配置**
`SENTINEL set <主库别名> <参数> <值>`
```redis
-- 动态修改哨兵配置（运行时生效）
SENTINEL set mymaster down-after-milliseconds 5000
SENTINEL set mymaster parallel-syncs 3
SENTINEL set mymaster failover-timeout 300000
SENTINEL set mymaster quorum 3

-- 动态添加监控主库
SENTINEL monitor newmaster 192.168.2.10 6379 2
-- 移除监控
SENTINEL remove newmaster
```

---

**基本写法：flushconfig 持久化**
`SENTINEL flushconfig`
```redis
-- 将当前哨兵状态写入配置文件（持久化）
SENTINEL flushconfig
-- 哨兵状态变更（发现新从库/哨兵）后建议执行
```
