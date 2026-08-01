# -*- coding: utf-8 -*-
"""数据库类模块知识库。"""

KB_DATA = {}


def _db(label, hint, history, theory, pitfalls, practices, comparisons, engineering,
        case, summary, refs, more, deep):
    axes = [
        f"能够说出 {label} 的核心概念、语法与常用对象。",
        f"能够解释 {label} 的执行原理与优化机制。",
        f"能够编写正确、高效的 {label} 语句与操作。",
        f"能够分析 {label} 相关方案在性能与一致性上的权衡。",
        f"能够根据业务场景评价 {label} 技术选型。",
        f"能够组合 {label} 与其他技术设计数据架构。",
    ]
    return {
        "label": label, "related_title_hint": hint, "axes": axes,
        "history": history, "history_tail": [], "definitions": theory[:3],
        "theory": theory, "pitfalls": pitfalls, "practices": practices,
        "comparisons": comparisons, "engineering": engineering, "case": case,
        "summary": summary, "refs": refs, "more": more,
        "supplement_examples": [], "deep_topics": deep,
    }


KB_DATA["sql"] = _db(
    "SQL", "DDL/DML、查询、索引、事务",
    [
        "SQL（结构化查询语言）源于 1970 年 Codd 的关系模型，1974 年由 Chamberlin 与 Boyce 设计（SEQUEL），1986 年成为 ANSI 标准；SQL:2023 是当前国际标准。",
        "SQL 分为 DDL（建表）、DML（增删改）、DQL（查询）、DCL（权限）与 TCL（事务）；各大数据库在标准基础上扩展方言。",
        "SQL 是声明式语言：描述“要什么”而非“怎么做”，优化器负责执行计划；这一设计让 SQL 具有跨数据库的表达一致性。",
    ],
    [
        "关系模型：表（关系）、行（元组）、列（属性）；主键唯一标识、外键表达关联、范式消除冗余。",
        "查询执行：解析 -> 绑定 -> 优化（基于代价选择计划）-> 执行；索引、统计信息与连接算法决定性能。",
        "事务 ACID：原子性（Atomicity）、一致性（Consistency）、隔离性（Isolation）、持久性（Durability）；隔离级别控制并发行为。",
        "集合语义：SELECT 返回结果集；JOIN 组合关系，GROUP BY 聚合，子查询与 CTE 表达复杂逻辑。",
    ],
    [
        ("SELECT * 滥用", "返回多余列浪费带宽且破坏视图依赖。显式列出所需列。"),
        ("隐式类型转换", "字符串与数字比较走转换，索引失效。保持类型一致。"),
        ("函数包裹索引列", "WHERE DATE(ts)=... 无法用索引。使用范围条件。"),
        ("分页偏移过大", "OFFSET 大时扫描大量行。使用游标或键集分页。"),
        ("事务内做慢查询", "长事务锁资源。事务保持短小。"),
        ("N+1 查询", "循环查库。使用 JOIN 或批量查询。"),
        ("不设外键约束", "应用层维护引用完整性易漏。关键关系使用外键。"),
        ("忽略执行计划", "凭直觉优化。用 EXPLAIN 验证。"),
    ],
    [
        "命名规范：表名复数或单数统一，列名小写下划线，主键 id。",
        "每个表必须有主键，时间戳列记录变更。",
        "查询先 WHERE 缩小数据量，再 JOIN 与聚合。",
        "迁移脚本版本化，变更可回滚。",
        "生产查询全部过 EXPLAIN 与慢日志检查。",
    ],
    [
        "SQL 与 NoSQL：SQL 适合关系与事务，NoSQL（文档/键值/宽表）适合弹性扩展与特定模型；混合架构常见。",
        "MySQL 与 PostgreSQL：MySQL 生态普及、复制成熟；PostgreSQL 功能全面（窗口、JSON、扩展）。",
        "存储过程与业务代码：复杂逻辑放应用层更可测试；存储过程适合强封装场景。",
    ],
    [
        "连接池管理数据库连接；迁移工具（Flyway/Alembic）版本化 schema。",
        "读写分离与分库分表按量级引入；缓存（Redis）承担热数据。",
        "监控：慢查询日志、连接数、QPS、复制延迟。",
    ],
    [
        "需求：为订单系统设计表结构与核心查询。",
        "方案：订单主表 + 明细表 + 用户表；事务保证一致；索引覆盖高频查询。",
        "要点：金额用 decimal；状态用枚举；时间用 UTC；分页用键集。",
        "验证：EXPLAIN 检查索引；并发插入测试唯一约束；压测查询延迟。",
    ],
    [
        "SQL 的声明式表达力建立在关系代数之上，理解集合思维是进阶关键。",
        "索引、执行计划与事务是三大实战主题。",
        "工程化：迁移、连接池、监控与慢查询治理缺一不可。",
    ],
    [
        "SQL 标准（ISO/IEC 9075）：https://www.iso.org/standard/76583.html",
        "PostgreSQL 文档（SQL 章节）：https://www.postgresql.org/docs/current/sql.html",
        "MySQL 文档：https://dev.mysql.com/doc/",
        "SQLite 文档：https://www.sqlite.org/docs.html",
        "Use The Index, Luke：https://use-the-index-luke.com/",
    ],
    [
        "SQL 连接与子查询，见 019-sql 模块文档。",
        "SQL 自连接与递归，见 019-sql/019-SelfJoin 文档。",
        "MySQL 深入，见 020-mysql 模块。",
        "PostgreSQL 深入，见 021-postgresql 模块。",
        "尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 MySQL 课程。",
    ],
    [
        ("索引原理与 B+ 树", [
            "B+ 树：非叶节点存索引键，叶节点存数据指针并链表相连；高度低（3-4 层）支撑千万级数据。",
            "聚集索引（主键）决定数据物理顺序；二级索引存主键值，回表取行；覆盖索引避免回表。",
            "最左前缀：复合索引按定义顺序匹配；范围查询后列失效。",
            "选择率：区分度高的列放前面；低基数列（性别）单列索引收益低。",
        ]),
        ("事务隔离与 MVCC", [
            "四种隔离级别：读未提交、读已提交、可重复读、可串行化；各自解决脏读、不可重复读、幻读。",
            "MVCC（多版本并发控制）：快照读不加锁，写通过版本链与回滚段实现；读写互不阻塞。",
            "PostgreSQL 默认读已提交，MySQL InnoDB 默认可重复读；理解差异避免跨库移植踩坑。",
            "死锁处理：锁顺序一致、超时检测、重试策略。",
        ]),
    ],
)

KB_DATA["mysql"] = _db(
    "MySQL", "InnoDB、索引、日志、主从、性能调优",
    [
        "MySQL 于 1995 年由 MySQL AB 发布，2008 年被 Sun 收购，2010 年随 Sun 并入 Oracle；MariaDB 是社区分支。",
        "MySQL 8.0（2018）重写优化器、引入窗口函数与 CTE、默认 utf8mb4、数据字典升级；MySQL 8.4 与 9.x 继续演进（Oracle 创新版 + LTS 双轨）。",
        "InnoDB 是默认存储引擎：事务、行锁、MVCC、崩溃恢复（redo/undo）；MyISAM 仅存于历史场景。",
    ],
    [
        "InnoDB 架构：缓冲池（Buffer Pool）、日志缓冲、redo/undo 日志；脏页刷盘与 checkpoint 机制。",
        "索引：B+ 树主键聚集索引、二级索引、覆盖索引；索引下推（ICP）与 MRR 优化。",
        "事务与锁：两阶段锁、间隙锁/临键锁（可重复读防幻读）、MVCC 快照读；隔离级别。",
        "复制：binlog 逻辑复制（statement/row/mixed），主从异步、半同步与组复制。",
    ],
    [
        ("最大连接数耗尽", "连接池过小或慢查询占连接。调大连接池与优化 SQL。"),
        ("索引失效", "隐式转换、函数包裹、LIKE 前导通配。检查执行计划。"),
        ("大表 DDL 锁表", "8.0 的 INSTANT/INPLACE 减少锁；仍评估窗口。"),
        ("缓冲池过小", "命中率低全盘 IO。调 innodb_buffer_pool_size（约内存 60-70%）。"),
        ("隐式提交", "DDL 隐式提交事务。事务内避免 DDL。"),
        ("utf8 与 utf8mb4", "utf8 非完整 UTF-8，emoji 报错。统一 utf8mb4。"),
        ("主从延迟", "大事务与长查询放大延迟。拆事务、并行复制。"),
        ("备份缺失", "无备份无法恢复。binlog + 定期全备并演练恢复。"),
    ],
    [
        "表与字段：主键自增或有序 UUID；金额 decimal；时间戳统一。",
        "索引：高频查询建覆盖索引；写密集控制索引数量。",
        "配置：字符集 utf8mb4、排序规则 utf8mb4_0900_ai_ci（8.0）。",
        "安全：最小权限账号、SSL 连接、敏感字段加密。",
    ],
    [
        "MySQL 与 PostgreSQL：MySQL 简单易用、复制生态成熟；PostgreSQL 功能与扩展更强。",
        "InnoDB 与 MyISAM：事务/行锁/崩溃恢复 vs 表锁/压缩；新表一律 InnoDB。",
        "异步复制与组复制：异步简单、组复制强一致；按可用性需求选择。",
    ],
    [
        "架构：主从读写分离、分库分表（ShardingSphere）、Proxy（ProxySQL）；容量规划。",
        "运维：Percona Toolkit 巡检、慢日志分析（pt-query-digest）、备份（Xtrabackup）。",
        "监控：QPS、连接、复制延迟、InnoDB 状态（SHOW ENGINE INNODB STATUS）。",
    ],
    [
        "需求：电商订单库优化：订单查询从 2 秒降到 50ms。",
        "方案：复合索引（user_id, status, created_at）、覆盖查询列、分页键集化。",
        "要点：EXPLAIN 前后对比；慢日志验证；避免 SELECT *。",
        "验证：压测 P95 延迟、索引使用率、无全表扫描。",
    ],
    [
        "MySQL 的性能核心是 InnoDB 的缓冲池与索引设计。",
        "日志（redo/undo/binlog）理解是故障恢复与复制的基础。",
        "工程化：字符集、连接池、备份、监控四件套。",
    ],
    [
        "MySQL 官方文档：https://dev.mysql.com/doc/",
        "MySQL 8.0 参考手册：https://dev.mysql.com/doc/refman/8.0/en/",
        "High Performance MySQL（O'Reilly）：https://www.oreilly.com/library/view/high-performance-mysql/",
        "Percona 博客：https://www.percona.com/blog/",
    ],
    [
        "MySQL 索引与优化，见 020-mysql 模块文档。",
        "MySQL 日志体系，见 020-mysql 模块 redo/binlog 文档。",
        "Redis 缓存与 MySQL 组合，见 022-redis 模块。",
        "尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 MySQL 高级课程。",
    ],
    [
        ("InnoDB 日志与崩溃恢复", [
            "redo log 记录物理页修改（WAL：先写日志再写数据页），崩溃后重放恢复；环形文件组 + checkpoint 推进。",
            "undo log 记录事务前镜像，支持回滚与 MVCC 版本链；purge 线程清理。",
            "两阶段提交：redo prepare -> binlog -> redo commit，保证两份日志一致，主从不丢数据。",
            "刷盘策略：innodb_flush_log_at_trx_commit=1 最安全（每次提交 fsync），2 每秒刷。",
        ]),
        ("执行计划与优化器", [
            "EXPLAIN 关键列：type（const/ref/range/index/ALL）、key、rows、Extra（Using index/Using filesort）。",
            "优化器基于统计信息选计划；analyze table 更新统计；hint（FORCE INDEX）谨慎使用。",
            "排序与分组：filesort 优化为索引序；避免临时表。",
            "慢查询治理流程：慢日志 -> 计划分析 -> 索引/改写 -> 验证。",
        ]),
    ],
)

KB_DATA["postgresql"] = _db(
    "PostgreSQL", "MVCC、窗口函数、扩展生态、高可用",
    [
        "PostgreSQL 起源于 1986 年伯克利的 POSTGRES 项目，1996 年更名 PostgreSQL；以功能全面与标准遵循著称，社区驱动发展（每年一个大版本）。",
        "特性版图：完整 SQL（窗口、CTE、递归、JSON）、扩展生态（PostGIS、pgvector）、复制（流复制/逻辑复制）、可编程性（PL/pgSQL、自定义类型）。",
        "PG 17（2024）/PG 18 持续增强：vacuum 与 I/O 优化、增量备份、并行查询扩展；被开发者社区长期评为最受欢迎的数据库之一。",
    ],
    [
        "MVCC：每个事务可见性由 xmin/xmax 与快照决定；行更新产生新版本，旧版本由 vacuum 清理；读写互不阻塞。",
        "索引类型：B-tree、Hash、GiST、SP-GiST、GIN（全文/JSON）、BRIN（大表顺序数据）；部分索引与表达式索引。",
        "窗口函数：OVER 子句在结果集内计算排名、移动平均、LAG/LEAD；区别于 GROUP BY 的聚合语义。",
        "逻辑复制与流复制：WAL 流复制同步备库；逻辑复制按表级发布订阅，支持跨版本与异构。",
    ],
    [
        ("vacuum 缺失", "表膨胀与事务 ID 回卷风险。开启 autovacuum 并监控。"),
        ("未用事务包装多语句", "部分成功导致数据不一致。使用事务或 CTE。"),
        ("jsonb 滥用", "频繁更新 jsonb 字段效率低。规范化的列优先。"),
        ("连接数默认限制", "max_connections=100 被连接池打满。使用 PgBouncer。"),
        ("序列回卷", "serial 溢出。使用 bigserial 或 identity。"),
        ("时区混淆", "timestamptz 与 timestamp 语义不同。统一 timestamptz。"),
        ("大事务", "长事务阻止 vacuum 与复制进度。拆分事务。"),
        ("忽略扩展插件", "重复造轮子。先查扩展目录（postgis、pgvector、pg_stat_statements）。"),
    ],
    [
        "主键用 bigint identity 或 UUID；外键保证引用完整性。",
        "高频查询建索引；JSON 用 jsonb；全文检索用 GIN。",
        "启用 pg_stat_statements 收集查询统计。",
        "备份：pg_basebackup + WAL 归档；演练恢复。",
    ],
    [
        "PostgreSQL 与 MySQL：PG 功能全面、标准遵循好、扩展强；MySQL 生态普及、运维资料多。",
        "PostgreSQL 与 Oracle：PG 开源成本低、现代特性多；Oracle 企业级功能与商业支持。",
        "流复制与逻辑复制：流复制整实例容灾；逻辑复制按表分发与升级。",
    ],
    [
        "高可用：Patroni + etcd 选主 + 流复制；读写分离中间件。",
        "容量与性能：分区表（声明式分区）管理大数据；并行查询调优。",
        "监控：pg_stat_activity、pg_stat_replication、Prometheus exporter。",
    ],
    [
        "需求：实现地理围栏查询（半径内 POI）。",
        "方案：PostGIS 扩展 + GiST 空间索引 + ST_DWithin 查询。",
        "要点：几何类型 geometry(Point,4326)；索引生效验证；投影统一。",
        "验证：百万点查询延迟、空间索引命中、精度核对。",
    ],
    [
        "PostgreSQL 以“功能没有短板”著称，MVCC 与扩展生态是核心。",
        "vacuum、连接、事务与索引是日常运维四大主题。",
        "高可用与备份是生产底线，必须演练。",
    ],
    [
        "PostgreSQL 官方文档：https://www.postgresql.org/docs/",
        "PostgreSQL 中文文档：https://www.postgresql.org/docs/current/index.html",
        "PGXN 扩展仓库：https://pgxn.org/",
        "PostGIS：https://postgis.net/",
        "pgvector：https://github.com/pgvector/pgvector",
    ],
    [
        "PostgreSQL 窗口函数，见 021-postgresql 模块文档。",
        "PostgreSQL 递归查询，见 021-postgresql 模块相关文档。",
        "SQL 基础，见 019-sql 模块。",
        "尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 PostgreSQL 课程。",
    ],
    [
        ("MVCC 与 vacuum 机制", [
            "行头存储 xmin（创建事务）与 xmax（删除事务）；可见性由快照比较决定。",
            "更新 = 插入新版本 + 旧版本标记；旧版本对旧事务可见，vacuum 回收不再可见的死元组。",
            "事务 ID 回卷：约 21 亿事务后需要冻结；autovacuum 与 vacuum freeze 防止。",
            "监控：SELECT n_dead_tup, last_autovacuum FROM pg_stat_user_tables。",
        ]),
        ("逻辑复制与高可用", [
            "发布（publication）定义表集，订阅（subscription）在目标端应用变更；支持过滤与列子集。",
            "流复制：主库 WAL 发送到备库，同步/异步模式；级联复制扩展拓扑。",
            "Patroni 使用分布式共识（etcd）选主，故障自动切换，配合虚拟 IP。",
            "切换演练与数据校验（pg_checksums）是可用性工程必备。",
        ]),
    ],
)

KB_DATA["redis"] = _db(
    "Redis", "数据结构、持久化、集群、缓存策略",
    [
        "Redis 由 Salvatore Sanfilippo 于 2009 年发布，是内存数据结构存储，常作缓存、消息中间件与轻量数据库；BSD 许可，单线程事件循环（6.0 起多线程 IO）。",
        "数据模型：String、Hash、List、Set、Sorted Set、Stream、BitMap、HyperLogLog、Geo；每种结构有专门命令与复杂度。",
        "Redis 7.x：ACL、函数（Lua/Redis Functions）、集群路由（Cluster Sharding）、自动故障转移；Redis Stack 集成 JSON/搜索/时序。",
    ],
    [
        "单线程模型：命令串行执行保证原子性，无锁；性能瓶颈在内存与网络；长命令（KEYS）阻塞。",
        "持久化：RDB 快照（fork 子进程）与 AOF 追加日志；混合持久化组合两者；持久化权衡数据安全与性能。",
        "过期与淘汰：惰性删除 + 定期抽样；maxmemory-policy（allkeys-lru/lru/lfu/noeviction）控制内存。",
        "高可用：主从复制（PSYNC）、哨兵（Sentinel）自动故障转移、Cluster 分片（16384 槽）与集群模式。",
    ],
    [
        ("KEYS 阻塞", "大键扫描阻塞服务。使用 SCAN 游标。"),
        ("大 key", "单 key 超大导致网络与内存问题。拆分或压缩。"),
        ("缓存穿透", "查询不存在数据打穿到 DB。布隆过滤器或空值缓存。"),
        ("缓存击穿", "热点 key 过期瞬间并发打 DB。互斥重建或逻辑过期。"),
        ("缓存雪崩", "大量 key 同时过期。过期时间加随机抖动。"),
        ("持久化误配置", "save 策略与 AOF 关闭导致重启丢数据。按数据安全需求配置。"),
        ("连接未关闭", "连接泄漏耗尽 maxclients。使用连接池。"),
        ("事务误用", "MULTI/EXEC 不保证回滚，命令错误才回滚。需要强一致用 Lua。"),
    ],
    [
        "键命名：业务:实体:id（user:profile:1001），过期时间按场景设置。",
        "缓存一致性：Cache Aside（先更新 DB 再删缓存）为主；延迟双删防旧缓存。",
        "集群：Slot 分布、批量操作需 hash tag；客户端路由（lettuce/jedis 集群版）。",
        "监控：INFO 内存/命中率、慢日志、monitor 抽样。",
    ],
    [
        "Redis 与 Memcached：Redis 数据结构丰富、持久化、集群；Memcached 简单多线程缓存。",
        "Redis 与消息队列：List/Stream 可实现轻量队列；强可靠场景用 Kafka/RabbitMQ。",
        "RDB 与 AOF：RDB 恢复快丢数据多；AOF 丢数据少恢复慢；混合取平衡。",
    ],
    [
        "缓存分层：本地缓存（Caffeine）+ Redis 分布式缓存；热点与一致性分层治理。",
        "分布式锁：SET NX EX + 续期（Redisson）；注意时钟跳跃与 GC 暂停。",
        "容量规划：maxmemory + 淘汰策略 + 监控；大促前预热。",
    ],
    [
        "需求：实现商品详情缓存与热点防护。",
        "方案：Cache Aside + 互斥重建（setnx）+ 随机过期抖动 + 布隆过滤器。",
        "要点：序列化协议统一；缓存与 DB 双写顺序；监控命中率。",
        "验证：压测穿透/击穿场景、故障注入（Redis 宕机降级）。",
    ],
    [
        "Redis 的价值在“数据结构即服务”：选择合适结构比堆功能重要。",
        "缓存三兄弟（穿透/击穿/雪崩）是设计必修课。",
        "持久化、复制与集群决定可靠性，生产必须配置齐全。",
    ],
    [
        "Redis 官方文档：https://redis.io/docs/latest/",
        "Redis 命令参考：https://redis.io/docs/latest/commands/",
        "Redis 中文资料：https://redis.com.cn/",
        "Redisson 文档：https://redisson.org/",
    ],
    [
        "Redis 数据结构详解，见 022-redis 模块文档。",
        "Redis 持久化与集群，见 022-redis 模块相关文档。",
        "MySQL 与 Redis 缓存架构，见 020-mysql 模块。",
        "黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 Redis 课程。",
    ],
    [
        ("缓存一致性深度", [
            "Cache Aside：读未命中查 DB 回填；写先 DB 后删缓存；删除失败用消息队列补偿。",
            "延迟双删：更新 DB 后删缓存，等待短暂延迟再删一次，处理并发读写窗口。",
            "读写锁与版本号：缓存携带版本，更新时比较版本，失败重试。",
            "强一致场景：不要依赖缓存，直接读 DB；缓存用于可容忍最终一致的数据。",
        ]),
        ("Redis Cluster 原理", [
            "16384 个槽分布在主节点，键经 CRC16 % 16384 定位；客户端 MOVED/ASK 重定向。",
            "主从复制：每个主节点挂从节点；主故障由从节点提升（cluster 自动 failover）。",
            "多键操作：同一事务/管道中的键必须同槽（hash tag {user1001}）。",
            "扩缩容：槽迁移在线进行，客户端感知重定向；规划容量避免热点槽。",
        ]),
    ],
)
