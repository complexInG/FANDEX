# DevOps Docker 数据卷管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## docker volume create 创建数据卷

**基本写法：创建命名数据卷**
`docker volume create <卷名>`
```bash
# 创建名为 mydata 的数据卷
docker volume create mydata
```

**基本写法：指定驱动创建数据卷**
`docker volume create -d <驱动> <卷名>`
```bash
# 使用 nfs 驱动创建数据卷
docker volume create -d local mydata
```

**基本写法：指定选项创建数据卷**
`docker volume create --opt <选项>=<值> <卷名>`
```bash
# 创建指定类型的数据卷
docker volume create --opt type=nfs --opt device=:/path mydata
```

---

## docker volume ls 查看数据卷

**基本写法：列出所有数据卷**
`docker volume ls`
```bash
# 列出所有数据卷
docker volume ls
```

**基本写法：过滤悬空数据卷**
`docker volume ls -f dangling=true`
```bash
# 列出未被使用的数据卷
docker volume ls -f dangling=true
```

**基本写法：按名称过滤**
`docker volume ls -f name=<关键词>`
```bash
# 列出名称包含 my 的数据卷
docker volume ls -f name=my
```

---

## docker volume inspect 查看数据卷详情

**基本写法：查看数据卷详情**
`docker volume inspect <卷名>`
```bash
# 查看 mydata 数据卷的详细信息
docker volume inspect mydata
```

**基本写法：查看数据卷挂载点**
`docker volume inspect --format '{{.Mountpoint}}' <卷名>`
```bash
# 获取数据卷在宿主机的挂载路径
docker volume inspect --format '{{.Mountpoint}}' mydata
```

---

## docker volume rm/prune 删除数据卷

**基本写法：删除数据卷**
`docker volume rm <卷名>`
```bash
# 删除 mydata 数据卷
docker volume rm mydata
```

**基本写法：删除所有未使用数据卷**
`docker volume prune`
```bash
# 清理所有未使用的数据卷
docker volume prune -f
```

---

## 挂载命名数据卷

**基本写法：启动容器时挂载命名卷**
`docker run -v <卷名>:<容器路径> <镜像>`
```bash
# 挂载 mydata 卷到 /data
docker run -d -v mydata:/data nginx
```

**基本写法：以只读方式挂载**
`docker run -v <卷名>:<容器路径>:ro <镜像>`
```bash
# 只读方式挂载数据卷
docker run -d -v mydata:/data:ro nginx
```

---

## 绑定挂载宿主目录

**基本写法：挂载宿主目录到容器**
`docker run -v <宿主路径>:<容器路径> <镜像>`
```bash
# 挂载宿主 /opt/data 到容器 /data
docker run -d -v /opt/data:/data nginx
```

**基本写法：使用 --mount 挂载**
`docker run --mount type=bind,source=<宿主路径>,target=<容器路径> <镜像>`
```bash
# 使用 mount 参数挂载
docker run -d --mount type=bind,source=/opt/data,target=/data nginx
```

**基本写法：只读绑定挂载**
`docker run -v <宿主路径>:<容器路径>:ro <镜像>`
```bash
# 只读方式挂载宿主目录
docker run -v /opt/config:/etc/nginx:ro nginx
```

---

## tmpfs 内存文件系统

**基本写法：挂载 tmpfs**
`docker run --tmpfs <容器路径> <镜像>`
```bash
# 在容器内挂载 tmpfs
docker run -d --tmpfs /tmp nginx
```

**基本写法：使用 --mount 挂载 tmpfs**
`docker run --mount type=tmpfs,target=<容器路径> <镜像>`
```bash
# 使用 mount 参数挂载 tmpfs
docker run -d --mount type=tmpfs,target=/cache nginx
```

**基本写法：指定 tmpfs 大小**
`docker run --mount type=tmpfs,tmpfs-size=<大小>,target=<容器路径> <镜像>`
```bash
# 指定 tmpfs 大小为 100MB
docker run --mount type=tmpfs,tmpfs-size=100m,target=/cache nginx
```

---

## 在 Dockerfile 中声明数据卷

**基本写法：声明匿名数据卷**
`VOLUME <路径>`
```dockerfile
# 声明数据卷
VOLUME /var/lib/mysql
```

**基本写法：声明多个数据卷**
`VOLUME ["<路径1>", "<路径2>"]`
```dockerfile
# 声明多个数据卷
VOLUME ["/data", "/logs"]
```

---

## 数据卷备份与恢复

**基本写法：备份数据卷**
`docker run --rm -v <卷名>:<源路径> -v <宿主路径>:<目标路径> <镜像> tar cvf <目标路径>/backup.tar <源路径>`
```bash
# 备份 mydata 数据卷到当前目录
docker run --rm -v mydata:/data -v $(pwd):/backup alpine tar cvf /backup/backup.tar /data
```

**基本写法：恢复数据卷**
`docker run --rm -v <卷名>:<目标路径> -v <宿主路径>:<源路径> <镜像> tar xvf <源路径>/backup.tar -C <目标路径>`
```bash
# 从备份文件恢复数据卷
docker run --rm -v mydata:/data -v $(pwd):/backup alpine tar xvf /backup/backup.tar -C /data
```

---

## 数据卷共享

**基本写法：容器间共享数据卷**
`docker run --volumes-from <容器> <镜像>`
```bash
# 新容器共享 web 容器的数据卷
docker run -d --name logger --volumes-from web alpine tail -f /var/log/nginx/access.log
```

**基本写法：多个容器挂载同一卷**
`docker run -v <卷名>:<路径> <镜像>`
```bash
# 多个容器挂载同一数据卷
docker run -d --name app1 -v shared:/data nginx
docker run -d --name app2 -v shared:/data nginx
```

---

## 数据卷迁移

**基本写法：导出数据卷内容**
`docker run --rm -v <卷名>:<路径> -v <宿主路径>:/backup <镜像> tar czf /backup/volume.tar.gz <路径>`
```bash
# 压缩导出数据卷内容
docker run --rm -v mydata:/data -v $(pwd):/backup alpine tar czf /backup/volume.tar.gz /data
```

**基本写法：导入数据到新卷**
`docker run --rm -v <新卷名>:<路径> -v <宿主路径>:/backup <镜像> tar xzf /backup/volume.tar.gz -C /`
```bash
# 将备份数据导入到新卷
docker run --rm -v newdata:/data -v $(pwd):/backup alpine tar xzf /backup/volume.tar.gz -C /
```
