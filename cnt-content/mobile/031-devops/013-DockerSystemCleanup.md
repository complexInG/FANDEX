# DevOps Docker 系统清理与维护

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## docker system 系统管理

**基本写法：查看 Docker 磁盘使用**
`docker system df`
```bash
# 查看 Docker 整体磁盘占用
docker system df
```

**基本写法：显示详细信息**
`docker system df -v`
```bash
# 查看每个镜像和容器的详细磁盘占用
docker system df -v
```

**基本写法：清理所有未使用资源**
`docker system prune`
```bash
# 清理停止的容器、悬空镜像、未使用网络
docker system prune -f
```

**基本写法：彻底清理所有未使用资源**
`docker system prune -a`
```bash
# 清理所有未被容器使用的镜像
docker system prune -a -f
```

**基本写法：清理含数据卷**
`docker system prune --volumes`
```bash
# 清理所有未使用资源含数据卷
docker system prune -a --volumes -f
```

---

## docker image prune 镜像清理

**基本写法：清理悬空镜像**
`docker image prune`
```bash
# 删除无标签的悬空镜像
docker image prune -f
```

**基本写法：清理所有未使用镜像**
`docker image prune -a`
```bash
# 删除所有未被容器使用的镜像
docker image prune -a -f
```

**基本写法：按时间过滤清理**
`docker image prune -a --filter "until=<时间>"`
```bash
# 清理 24 小时前创建的镜像
docker image prune -a --filter "until=24h" -f
```

**基本写法：按标签过滤清理**
`docker image prune -a --filter "label=<标签>"`
```bash
# 清理带指定标签的镜像
docker image prune -a --filter "label=stage=builder" -f
```

---

## docker container prune 容器清理

**基本写法：清理停止的容器**
`docker container prune`
```bash
# 删除所有停止的容器
docker container prune -f
```

**基本写法：按时间过滤清理**
`docker container prune --filter "until=<时间>"`
```bash
# 清理 24 小时前停止的容器
docker container prune --filter "until=24h" -f
```

**基本写法：按状态过滤清理**
`docker container prune --filter "status=<状态>"`
```bash
# 清理已退出的容器
docker container prune --filter "status=exited" -f
```

---

## docker volume prune 数据卷清理

**基本写法：清理未使用数据卷**
`docker volume prune`
```bash
# 删除所有未被容器使用的数据卷
docker volume prune -f
```

**基本写法：清理所有数据卷**
`docker volume prune -a`
```bash
# 删除所有数据卷（谨慎使用）
docker volume prune -a -f
```

**基本写法：按标签过滤清理**
`docker volume prune --filter "label=<标签>"`
```bash
# 清理带指定标签的数据卷
docker volume prune --filter "label=temp" -f
```

---

## docker network prune 网络清理

**基本写法：清理未使用网络**
`docker network prune`
```bash
# 删除所有未被使用的自定义网络
docker network prune -f
```

**基本写法：按时间过滤清理**
`docker network prune --filter "until=<时间>"`
```bash
# 清理 24 小时前创建的网络
docker network prune --filter "until=24h" -f
```

---

## docker builder prune 构建缓存清理

**基本写法：清理构建缓存**
`docker builder prune`
```bash
# 清理悬空的构建缓存
docker builder prune -f
```

**基本写法：清理所有构建缓存**
`docker builder prune -a`
```bash
# 清理所有构建缓存
docker builder prune -a -f
```

**基本写法：按保留大小清理**
`docker builder prune --filter "until=<时间>"`
```bash
# 清理 24 小时前的构建缓存
docker builder prune --filter "until=24h" -a -f
```

---

## 批量删除操作

**基本写法：删除所有停止的容器**
`docker rm $(docker ps -aq)`
```bash
# 删除所有已停止的容器
docker rm $(docker ps -aq)
```

**基本写法：删除所有镜像**
`docker rmi $(docker images -q)`
```bash
# 删除所有本地镜像
docker rmi $(docker images -q) -f
```

**基本写法：删除无标签镜像**
`docker rmi $(docker images -f "dangling=true" -q)`
```bash
# 删除所有悬空镜像
docker rmi $(docker images -f "dangling=true" -q)
```

**基本写法：停止所有运行容器**
`docker stop $(docker ps -q)`
```bash
# 停止所有正在运行的容器
docker stop $(docker ps -q)
```

---

## docker info 系统信息

**基本写法：查看 Docker 系统信息**
`docker info`
```bash
# 查看 Docker 详细系统信息
docker info
```

**基本写法：查看版本**
`docker version`
```bash
# 查看 Docker 客户端和服务端版本
docker version
```

**基本写法：只查看版本号**
`docker --version`
```bash
# 查看 Docker 版本号
docker --version
```

---

## docker events 事件监控

**基本写法：实时查看事件**
`docker events`
```bash
# 实时查看 Docker 事件
docker events
```

**基本写法：按时间过滤事件**
`docker events --since <时间>`
```bash
# 查看最近 10 分钟的事件
docker events --since 10m
```

**基本写法：按类型过滤事件**
`docker events --filter type=<类型>`
```bash
# 只查看容器事件
docker events --filter type=container
```

**基本写法：按容器过滤事件**
`docker events --filter container=<容器>`
```bash
# 查看 web 容器的事件
docker events --filter container=web
```

---

## 日志管理

**基本写法：查看 Docker 守护进程日志**
`journalctl -u docker`
```bash
# 查看 Docker 服务日志
journalctl -u docker.service
```

**基本写法：查看指定时间日志**
`journalctl -u docker --since <时间>`
```bash
# 查看今天的 Docker 日志
journalctl -u docker --since today
```

**基本写法：实时跟踪日志**
`journalctl -u docker -f`
```bash
# 实时跟踪 Docker 日志
journalctl -u docker -f
```

---

## 磁盘占用分析

**基本写法：查看 Docker 数据目录**
`docker info --format '{{.DockerRootDir}}'`
```bash
# 获取 Docker 数据目录路径
docker info --format '{{.DockerRootDir}}'
```

**基本写法：查看容器日志大小**
`du -sh /var/lib/docker/containers/*/*-json.log`
```bash
# 查看所有容器日志文件大小
du -sh /var/lib/docker/containers/*/*-json.log
```

**基本写法：清理容器日志**
`truncate -s 0 /var/lib/docker/containers/*/*-json.log`
```bash
# 清空所有容器日志文件
truncate -s 0 /var/lib/docker/containers/*/*-json.log
```

---

## 配置日志轮转

**基本写法：配置 daemon.json 日志轮转**
```json
`{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "<大小>",
    "max-file": "<数量>"
  }
}`
```
```json
// 配置日志文件最大 10MB，保留 3 个
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```
