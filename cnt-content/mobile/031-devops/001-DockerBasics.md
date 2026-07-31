# DevOps Docker 容器基础命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## docker run 创建并启动容器

**基本写法：运行容器**
`docker run [选项] <镜像> [命令]`
```bash
# 启动 nginx 容器
docker run nginx
```

**基本写法：后台运行容器**
`docker run -d <镜像>`
```bash
# 后台运行 nginx 容器
docker run -d nginx
```

**基本写法：交互式运行容器**
`docker run -it <镜像> <命令>`
```bash
# 进入 ubuntu 容器的 bash
docker run -it ubuntu bash
```

**基本写法：命名容器并映射端口**
`docker run --name <名称> -p <宿主端口>:<容器端口> <镜像>`
```bash
# 启动命名为 web 的 nginx，映射 8080 到 80
docker run --name web -p 8080:80 nginx
```

**基本写法：挂载数据卷**
`docker run -v <宿主路径>:<容器路径> <镜像>`
```bash
# 挂载当前目录到容器的 /app
docker run -v $(pwd):/app node
```

---

## docker ps 查看容器

**基本写法：查看运行中容器**
`docker ps`
```bash
# 列出正在运行的容器
docker ps
```

**基本写法：查看所有容器（含已停止）**
`docker ps -a`
```bash
# 列出所有容器
docker ps -a
```

**基本写法：只显示容器 ID**
`docker ps -q`
```bash
# 获取所有运行容器的 ID
docker ps -q
```

---

## docker start/stop/restart 生命周期管理

**基本写法：启动已停止的容器**
`docker start <容器>`
```bash
# 启动容器 web
docker start web
```

**基本写法：停止容器**
`docker stop [选项] <容器>`
```bash
# 优雅停止容器 web
docker stop web
```

**基本写法：强制停止容器**
`docker stop -t 0 <容器>`
```bash
# 立即停止容器
docker stop -t 0 web
```

**基本写法：重启容器**
`docker restart <容器>`
```bash
# 重启容器 web
docker restart web
```

---

## docker rm 删除容器

**基本写法：删除已停止容器**
`docker rm <容器>`
```bash
# 删除容器 web
docker rm web
```

**基本写法：强制删除运行中容器**
`docker rm -f <容器>`
```bash
# 强制删除运行中的容器
docker rm -f web
```

**基本写法：删除所有停止的容器**
`docker container prune`
```bash
# 清理所有停止的容器
docker container prune -f
```

---

## docker exec 进入容器执行命令

**基本写法：进入容器交互式 shell**
`docker exec -it <容器> <shell>`
```bash
# 进入 web 容器的 bash
docker exec -it web bash
```

**基本写法：在容器中执行命令**
`docker exec <容器> <命令>`
```bash
# 查看 web 容器的进程列表
docker exec web ps aux
```

**基本写法：以指定用户执行命令**
`docker exec -u <用户> <容器> <命令>`
```bash
# 以 root 用户进入容器
docker exec -u root -it web sh
```

---

## docker logs 查看日志

**基本写法：查看容器日志**
`docker logs <容器>`
```bash
# 查看 web 容器的全部日志
docker logs web
```

**基本写法：实时跟踪日志**
`docker logs -f <容器>`
```bash
# 实时跟踪 web 容器日志
docker logs -f web
```

**基本写法：查看最后 N 行日志**
`docker logs --tail <行数> <容器>`
```bash
# 查看最后 100 行日志
docker logs --tail 100 web
```

**基本写法：查看指定时间后的日志**
`docker logs --since <时间> <容器>`
```bash
# 查看最近 10 分钟的日志
docker logs --since 10m web
```

---

## docker inspect 查看容器详情

**基本写法：查看容器详细信息**
`docker inspect <容器>`
```bash
# 查看 web 容器的完整信息
docker inspect web
```

**基本写法：查看容器 IP 地址**
`docker inspect --format '{{.NetworkSettings.IPAddress}}' <容器>`
```bash
# 提取容器的 IP 地址
docker inspect --format '{{.NetworkSettings.IPAddress}}' web
```

**基本写法：查看容器状态**
`docker inspect --format '{{.State.Status}}' <容器>`
```bash
# 获取容器当前状态
docker inspect --format '{{.State.Status}}' web
```

---

## docker stats 资源监控

**基本写法：查看所有容器资源使用**
`docker stats`
```bash
# 实时显示所有容器资源占用
docker stats
```

**基本写法：查看指定容器资源使用**
`docker stats <容器>`
```bash
# 监控 web 容器的 CPU 和内存
docker stats web
```

**基本写法：只输出一次结果**
`docker stats --no-stream`
```bash
# 一次性输出所有容器资源使用
docker stats --no-stream
```

---

## docker cp 文件拷贝

**基本写法：从容器拷贝文件到宿主机**
`docker cp <容器>:<容器路径> <宿主路径>`
```bash
# 从 web 容器拷贝配置文件到当前目录
docker cp web:/etc/nginx/nginx.conf ./
```

**基本写法：从宿主机拷贝文件到容器**
`docker cp <宿主路径> <容器>:<容器路径>`
```bash
# 拷贝本地文件到容器
docker cp ./app.conf web:/etc/nginx/conf.d/
```
