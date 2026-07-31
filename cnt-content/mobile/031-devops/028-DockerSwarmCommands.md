# Docker Swarm 集群命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 集群初始化

**基本用法:初始化 Swarm**
`docker swarm init --advertise-addr <IP>`

```bash
# 初始化 Swarm 集群(指定监听 IP)
docker swarm init --advertise-addr 192.168.1.10

# 指定监听端口
docker swarm init --advertise-addr 192.168.1.10:2377 --listen-addr 0.0.0.0:2377

# 指定默认数据路径
docker swarm init --data-path-addr eth0

# 查看集群状态
docker info | grep Swarm
```

---

**基本用法:获取加入令牌**
`docker swarm join-token <角色>`

```bash
# 获取 worker 节点加入令牌
docker swarm join-token worker

# 获取 manager 节点加入令牌
docker swarm join-token manager

# 仅显示令牌(不加提示文本)
docker swarm join-token -q worker

# 轮换令牌(旧令牌失效)
docker swarm join-token --rotate worker
```

---

**基本用法:节点加入与离开**
`docker swarm join --token <令牌> <manager-IP:port>`

```bash
# worker 节点加入集群
docker swarm join --token SWMTKN-1-xxx 192.168.1.10:2377

# manager 节点加入集群
docker swarm join --token SWMTKN-1-xxx-manager 192.168.1.10:2377

# 节点主动离开集群
docker swarm leave

# 强制离开(不通知 manager)
docker swarm leave --force
```

---

## 节点管理

**基本用法:查看节点列表**
`docker node ls`

```bash
# 列出所有节点
docker node ls

# 查看节点详情
docker node inspect node-1

# 查看节点格式化输出
docker node ls --format "table {{.ID}}\t{{.Hostname}}\t{{.Status}}\t{{.ManagerStatus}}"

# 过滤查看节点
docker node ls --filter role=manager
```

---

**基本用法:节点状态管理**
`docker node promote|demote|update <节点>`

```bash
# 提升 worker 为 manager
docker node promote node-2

# 降级 manager 为 worker
docker node demote node-1

# 节点排水(不再调度任务)
docker node update --availability drain node-3

# 恢复调度
docker node update --availability active node-3

# 暂停节点(保留任务但不新调度)
docker node update --availability pause node-3
```

---

**基本用法:节点标签**
`docker node update --label-add <键>=<值> <节点>`

```bash
# 给节点添加标签
docker node update --label-add env=production node-1

# 添加多个标签
docker node update --label-add role=web --label-add zone=east node-1

# 删除标签
docker node update --label-r env node-1

# 查看节点标签
docker node inspect node-1 --format '{{.Spec.Labels}}'
```

---

**基本用法:删除节点**
`docker node rm <节点>`

```bash
# 删除已离开的节点
docker node rm node-3

# 强制删除(慎用)
docker node rm -f node-3

# 节点移除流程
docker node update --availability drain node-3
docker node ps node-3  # 确认无运行任务
docker node rm node-3
```

---

## 服务管理

**基本用法:创建服务**
`docker service create --name <服务名> <镜像>`

```bash
# 创建 nginx 服务
docker service create --name web -p 80:80 nginx:alpine

# 创建带副本的服务
docker service create --name web --replicas 3 -p 80:80 nginx:alpine

# 指定放置约束
docker service create --name web --replicas 3 \
  --constraint node.labels.env==production \
  -p 80:80 nginx:alpine

# 使用环境变量与挂载
docker service create --name app --replicas 2 \
  -e DB_HOST=mysql \
  --mount type=volume,source=app-data,target=/data \
  -p 8080:8080 myapp:latest
```

---

**基本用法:查看服务**
`docker service ls`

```bash
# 列出所有服务
docker service ls

# 查看服务详情
docker service inspect web

# 仅查看关键信息
docker service inspect --pretty web

# 查看服务任务(实例)
docker service ps web

# 过滤任务状态
docker service ps web --filter desired-state=running
```

---

**基本用法:更新服务**
`docker service update [选项] <服务>`

```bash
# 更新镜像版本
docker service update --image nginx:1.25 web

# 调整副本数
docker service scale web=5

# 更新端口
docker service update --publish-rm 80:80 --publish-add 8080:80 web

# 更新环境变量
docker service update --env-rm DB_HOST --env-add DB_HOST=mysql-v2 web

# 滚动更新策略
docker service update --update-parallelism 2 --update-delay 30s web
```

---

**基本用法:删除与回滚**
`docker service rm|rollback <服务>`

```bash
# 删除服务
docker service rm web

# 回滚到上一版本
docker service rollback web

# 查看服务历史
docker service ps web --no-trunc

# 查看回滚状态
docker service inspect web --format '{{.UpdateStatus}}'
```

---

## 服务配置详解

**基本用法:副本与全局服务**
`--mode <replicated|global>`

```bash
# 副本模式(默认,指定数量)
docker service create --name web --mode replicated --replicas 5 nginx

# 全局模式(每个节点运行一个)
docker service create --name log-agent --mode global fluentd:1.16

# 查看服务模式
docker service inspect web --format '{{.Spec.Mode}}'
```

---

**基本用法:网络配置**
`--network <网络>`

```bash
# 创建覆盖网络
docker network create --driver overlay --subnet 10.0.0.0/24 app-net

# 服务连接到网络
docker service create --name app --network app-net --replicas 3 myapp

# 服务连接多个网络
docker service update --network-rm old-net --network-add new-net app

# 查看网络
docker network inspect app-net
```

---

**基本用法:数据卷与挂载**
`--mount type=<类型>`

```bash
# 挂载命名卷
docker service create --name db \
  --mount type=volume,source=db-data,target=/var/lib/mysql \
  mysql:8

# 挂载绑定路径(需在每个节点存在)
docker service create --name web \
  --mount type=bind,source=/etc/nginx/conf.d,target=/etc/nginx/conf.d \
  nginx:alpine

# 挂载 tmpfs
docker service create --name cache \
  --mount type=tmpfs,target=/cache,tmpfs-size=100M \
  redis:alpine
```

---

**基本用法:资源限制**
`--limit-* / --reserve-*`

```bash
# 限制 CPU 与内存
docker service create --name app \
  --limit-cpu 0.5 --limit-memory 512M \
  --reserve-cpu 0.25 --reserve-memory 256M \
  --replicas 3 myapp

# 限制每节点副本数
docker service create --name db \
  --replicas 3 \
  --replicas-max-per-node 1 \
  mysql:8
```

---

**基本用法:健康检查**
`--health-cmd`

```bash
# 配置健康检查
docker service create --name web \
  --health-cmd "curl -f http://localhost/health || exit 1" \
  --health-interval 10s \
  --health-timeout 5s \
  --health-retries 3 \
  nginx:alpine

# 查看健康状态
docker service ps web --no-trunc | grep Health
```

---

## 滚动更新与回滚

**基本用法:更新策略**
`--update-*`

```bash
# 配置更新策略
docker service create --name app \
  --replicas 10 \
  --update-parallelism 2 \
  --update-delay 30s \
  --update-failure-action rollback \
  --update-monitor 30s \
  --update-max-failure-ratio 0.3 \
  myapp:v1

# 触发更新
docker service update --image myapp:v2 app

# 监视更新过程
docker service ps app
```

---

**基本用法:回滚策略**
`--rollback-*`

```bash
# 配置回滚策略
docker service update \
  --rollback-parallelism 1 \
  --rollback-delay 10s \
  --rollback-failure-action pause \
  --rollback-monitor 30s \
  --rollback-max-failure-ratio 0.5 \
  app

# 立即回滚
docker service rollback app

# 禁止自动回滚
docker service update --update-failure-action pause app
```

---

## 配置与机密

**基本用法:创建配置**
`docker config create <名称> <文件>`

```bash
# 从文件创建配置
docker config create nginx-config nginx.conf

# 从 stdin 创建配置
echo "server { listen 80; }" | docker config create site-config -

# 查看配置列表
docker config ls

# 查看配置详情
docker config inspect nginx-config

# 在服务中使用配置
docker service create --name web \
  --config source=nginx-config,target=/etc/nginx/nginx.conf \
  nginx:alpine
```

---

**基本用法:创建机密**
`docker secret create <名称> <文件>`

```bash
# 创建机密
echo "mysupersecret" | docker secret create db-password -

# 从文件创建机密
docker secret create ssl-cert /path/to/cert.pem

# 查看机密列表
docker secret ls

# 在服务中使用机密(以文件形式挂载)
docker service create --name db \
  --secret source=db-password,target=/run/secrets/db_password \
  mysql:8

# 更新机密(需要删除后重建)
docker secret rm db-password
echo "newpassword" | docker secret create db-password -
docker service update --secret-rm db-password --secret-add source=db-password,target=/run/secrets/db_password db
```

---

## 堆栈部署

**基本用法:部署堆栈**
`docker stack deploy -c <compose.yml> <堆栈名>`

```bash
# 部署堆栈
docker stack deploy -c docker-compose.yml myapp

# 指定多个 compose 文件
docker stack deploy -c docker-compose.yml -c docker-compose.prod.yml myapp

# 带变量(需先导出)
export VERSION=v1.2
docker stack deploy -c docker-compose.yml myapp

# 不解析变量(原样使用)
docker stack deploy -c docker-compose.yml --compose-file docker-compose.yml myapp
```

---

**基本用法:管理堆栈**
`docker stack ls|ps|services|rm`

```bash
# 列出所有堆栈
docker stack ls

# 查看堆栈中的服务
docker stack services myapp

# 查看堆栈任务
docker stack ps myapp

# 删除堆栈
docker stack rm myapp
```

---

**基本用法:Compose v3 for Swarm**
`docker-compose.yml`

```yaml
# docker-compose.yml Swarm 兼容配置
version: '3.8'

services:
  web:
    image: nginx:alpine
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 30s
        failure_action: rollback
      rollback_config:
        parallelism: 1
      restart_policy:
        condition: on-failure
        max_attempts: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
      placement:
        constraints:
        - node.labels.env == production
    ports:
    - "80:80"
    networks:
    - app-net

  db:
    image: mysql:8
    deploy:
      replicas: 1
      placement:
        constraints:
        - node.role == manager
    environment:
      MYSQL_ROOT_PASSWORD_FILE: /run/secrets/db_password
    secrets:
    - db_password
    volumes:
    - db-data:/var/lib/mysql
    networks:
    - app-net

networks:
  app-net:
    driver: overlay

volumes:
  db-data:

secrets:
  db_password:
    external: true
```

---

## 排查与监控

**基本用法:查看任务状态**
`docker service ps <服务>`

```bash
# 查看服务所有任务
docker service ps web

# 包含失败任务(历史)
docker service ps web --no-trunc

# 过滤失败任务
docker service ps web --filter desired-state=failed

# 查看任务详情
docker service ps -f id=<task-id> web
```

---

**基本用法:查看日志**
`docker service logs <服务>`

```bash
# 查看服务日志
docker service logs web

# 跟踪日志
docker service logs -f web

# 查看指定任务日志
docker service logs --task-id <task-id> web

# 显示时间戳
docker service logs -t web

# 仅查看最后 100 行
docker service logs --tail 100 web
```

---

**基本用法:进入容器调试**
`docker exec -it <容器> <命令>`

```bash
# 找到服务容器 ID
docker ps --filter name=web

# 进入容器
docker exec -it web.1.xxx sh

# 在容器内执行命令
docker exec web.1.xxx curl localhost:8080/health

# 查看容器资源使用
docker stats $(docker ps -q --filter name=web)
```

---

## 备份与维护

**基本用法:备份服务数据**
`docker run --rm -v <卷>:<路径> -v $(pwd):/backup alpine tar czf /backup/<文件> <路径>`

```bash
# 备份命名卷
docker run --rm -v myapp_db-data:/data -v $(pwd):/backup alpine \
  tar czf /backup/db-$(date +%Y%m%d).tar.gz /data

# 恢复数据
docker run --rm -v myapp_db-data:/data -v $(pwd):/backup alpine \
  tar xzf /backup/db-20240101.tar.gz -C /

# 备份服务配置
docker service inspect web > web-config-$(date +%Y%m%d).json

# 导出所有服务
docker service ls --format "{{.Name}}" | xargs -I {} docker service inspect {} > all-services.json
```

---

**基本用法:集群维护**
`docker swarm update`

```bash
# 更新集群配置
docker swarm update --cert-expiry 2160h0m0s

# 设置自动锁(增加安全)
docker swarm update --autolock=true

# 查看 unlock 令牌
docker swarm unlock-key

# 轮换 unlock 令牌
docker swarm unlock-key --rotate

# 解锁集群(重启 manager 后)
docker swarm unlock
```

---

**基本用法:节点疏散与维护**
`docker node update --availability drain <节点>`

```bash
# 完整节点维护流程
# 1. 排水节点(任务迁移到其他节点)
docker node update --availability drain node-3

# 2. 等待任务迁移完成
docker node ps node-3
# 直到无 running 任务

# 3. 执行维护操作(如升级 Docker)
ssh node-3
sudo systemctl stop docker
# ... 维护操作
sudo systemctl start docker

# 4. 恢复节点调度
docker node update --availability active node-3
```
