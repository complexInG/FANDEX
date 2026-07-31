# DevOps Docker 网络管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## docker network create 创建网络

**基本写法：创建桥接网络**
`docker network create <网络名>`
```bash
# 创建自定义桥接网络
docker network create mynet
```

**基本写法：指定子网创建网络**
`docker network create --subnet <CIDR> <网络名>`
```bash
# 创建指定子网的网络
docker network create --subnet 172.20.0.0/16 mynet
```

**基本写法：创建 overlay 网络**
`docker network create -d overlay <网络名>`
```bash
# 创建跨主机 overlay 网络
docker network create -d overlay myoverlay
```

---

## docker network ls 查看网络

**基本写法：列出所有网络**
`docker network ls`
```bash
# 列出所有 Docker 网络
docker network ls
```

**基本写法：过滤网络**
`docker network ls --filter driver=<驱动>`
```bash
# 只列出桥接网络
docker network ls --filter driver=bridge
```

---

## docker network inspect 查看网络详情

**基本写法：查看网络详情**
`docker network inspect <网络名>`
```bash
# 查看 mynet 网络的详细信息
docker network inspect mynet
```

**基本写法：查看网络中的容器**
`docker network inspect --format '{{range .Containers}}{{.Name}} {{end}}' <网络名>`
```bash
# 列出网络中的所有容器
docker network inspect --format '{{range .Containers}}{{.Name}} {{end}}' mynet
```

---

## docker network connect 连接容器到网络

**基本写法：连接容器到网络**
`docker network connect <网络名> <容器>`
```bash
# 将 web 容器连接到 mynet 网络
docker network connect mynet web
```

**基本写法：指定 IP 连接**
`docker network connect --ip <IP> <网络名> <容器>`
```bash
# 指定 IP 连接容器到网络
docker network connect --ip 172.20.0.5 mynet web
```

**基本写法：使用别名连接**
`docker network connect --alias <别名> <网络名> <容器>`
```bash
# 给容器设置网络别名
docker network connect --alias dbhost mynet web
```

---

## docker network disconnect 断开网络

**基本写法：断开容器与网络连接**
`docker network disconnect <网络名> <容器>`
```bash
# 将 web 容器从 mynet 断开
docker network disconnect mynet web
```

**基本写法：强制断开**
`docker network disconnect -f <网络名> <容器>`
```bash
# 强制断开容器网络
docker network disconnect -f mynet web
```

---

## docker network rm/prune 删除网络

**基本写法：删除网络**
`docker network rm <网络名>`
```bash
# 删除 mynet 网络
docker network rm mynet
```

**基本写法：删除所有未使用网络**
`docker network prune`
```bash
# 清理所有未使用的网络
docker network prune -f
```

---

## 容器使用自定义网络

**基本写法：启动容器时指定网络**
`docker run --network <网络名> <镜像>`
```bash
# 启动容器并加入 mynet 网络
docker run -d --name web --network mynet nginx
```

**基本写法：指定网络别名**
`docker run --network <网络名> --network-alias <别名> <镜像>`
```bash
# 给容器设置网络别名
docker run -d --name app --network mynet --network-alias api node
```

---

## 网络驱动类型

**基本写法：bridge 桥接网络**
`docker network create -d bridge <网络名>`
```bash
# 创建默认桥接网络
docker network create -d bridge mybridge
```

**基本写法：host 主机网络**
`docker run --network host <镜像>`
```bash
# 容器使用主机网络
docker run --network host nginx
```

**基本写法：none 无网络**
`docker run --network none <镜像>`
```bash
# 启动无网络的容器
docker run --network none alpine
```

---

## 端口映射

**基本写法：映射单个端口**
`docker run -p <宿主端口>:<容器端口> <镜像>`
```bash
# 映射 8080 到容器 80
docker run -p 8080:80 nginx
```

**基本写法：映射多个端口**
`docker run -p <端口1>:<端口1> -p <端口2>:<端口2> <镜像>`
```bash
# 映射多个端口
docker run -p 80:80 -p 443:443 nginx
```

**基本写法：绑定指定 IP**
`docker run -p <IP>:<宿主端口>:<容器端口> <镜像>`
```bash
# 绑定到指定 IP
docker run -p 127.0.0.1:8080:80 nginx
```

**基本写法：随机端口映射**
`docker run -P <镜像>`
```bash
# 随机映射到宿主机端口
docker run -P nginx
```

---

## DNS 与服务发现

**基本写法：容器间通过名称访问**
`docker run --name <容器名> --network <网络名> <镜像>`
```bash
# 在同一网络中通过容器名访问
docker run -d --name db --network mynet mysql
docker run -d --name web --network mynet nginx
# web 容器可通过 db 名称访问 mysql
```

**基本写法：自定义 DNS 服务器**
`docker run --dns <DNS服务器> <镜像>`
```bash
# 指定 DNS 服务器
docker run --dns 8.8.8.8 nginx
```

---

## 网络问题排查

**基本写法：查看容器网络配置**
`docker inspect --format '{{.NetworkSettings}}' <容器>`
```bash
# 查看容器网络设置
docker inspect --format '{{json .NetworkSettings.Networks}}' web
```

**基本写法：测试容器间连通性**
`docker exec <容器> ping <目标容器>`
```bash
# 测试 web 到 db 的连通性
docker exec web ping db
```

**基本写法：查看容器端口映射**
`docker port <容器>`
```bash
# 查看 web 容器的端口映射
docker port web
```
