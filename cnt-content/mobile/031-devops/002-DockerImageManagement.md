# DevOps Docker 镜像管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## docker pull 拉取镜像

**基本写法：拉取镜像**
`docker pull <镜像>[:<标签>]`
```bash
# 拉取 nginx 最新版本
docker pull nginx
```

**基本写法：拉取指定版本**
`docker pull <镜像>:<标签>`
```bash
# 拉取 nginx 1.25 版本
docker pull nginx:1.25
```

**基本写法：从私有仓库拉取**
`docker pull <仓库地址>/<镜像>:<标签>`
```bash
# 从私有仓库拉取镜像
docker pull registry.example.com/myapp:v1
```

---

## docker images 查看镜像

**基本写法：列出本地镜像**
`docker images`
```bash
# 列出所有本地镜像
docker images
```

**基本写法：列出指定镜像**
`docker images <镜像名>`
```bash
# 列出所有 nginx 镜像
docker images nginx
```

**基本写法：只显示镜像 ID**
`docker images -q`
```bash
# 获取所有镜像的 ID
docker images -q
```

**基本写法：显示完整镜像 ID**
`docker images --no-trunc`
```bash
# 显示完整镜像 ID 不截断
docker images --no-trunc
```

---

## docker build 构建镜像

**基本写法：构建镜像**
`docker build -t <镜像名>:<标签> <Dockerfile 路径>`
```bash
# 使用当前目录 Dockerfile 构建镜像
docker build -t myapp:v1 .
```

**基本写法：指定 Dockerfile 文件**
`docker build -f <Dockerfile> -t <镜像名> <路径>`
```bash
# 使用自定义 Dockerfile 构建
docker build -f Dockerfile.prod -t myapp:prod .
```

**基本写法：不使用缓存构建**
`docker build --no-cache -t <镜像名> <路径>`
```bash
# 不使用缓存构建镜像
docker build --no-cache -t myapp:v2 .
```

**基本写法：构建参数**
`docker build --build-arg <参数>=<值> -t <镜像名> <路径>`
```bash
# 传递构建参数 VERSION
docker build --build-arg VERSION=1.0 -t myapp .
```

---

## docker tag 标记镜像

**基本写法：给镜像打标签**
`docker tag <源镜像> <目标镜像>:<标签>`
```bash
# 给镜像打新标签
docker tag myapp:v1 myapp:latest
```

**基本写法：标记到远程仓库**
`docker tag <源镜像> <仓库地址>/<镜像>:<标签>`
```bash
# 标记镜像到私有仓库
docker tag myapp:v1 registry.example.com/myapp:v1
```

---

## docker push 推送镜像

**基本写法：登录仓库**
`docker login [仓库地址]`
```bash
# 登录 Docker Hub
docker login
```

**基本写法：推送镜像**
`docker push <镜像>:<标签>`
```bash
# 推送镜像到 Docker Hub
docker push myusername/myapp:v1
```

**基本写法：推送到私有仓库**
`docker push <仓库地址>/<镜像>:<标签>`
```bash
# 推送镜像到私有仓库
docker push registry.example.com/myapp:v1
```

---

## docker rmi 删除镜像

**基本写法：删除镜像**
`docker rmi <镜像>`
```bash
# 删除 nginx 镜像
docker rmi nginx
```

**基本写法：强制删除镜像**
`docker rmi -f <镜像>`
```bash
# 强制删除被容器引用的镜像
docker rmi -f myapp:v1
```

**基本写法：删除所有悬空镜像**
`docker image prune`
```bash
# 清理无标签的悬空镜像
docker image prune -f
```

**基本写法：删除所有未使用镜像**
`docker image prune -a`
```bash
# 清理所有未被容器使用的镜像
docker image prune -a -f
```

---

## docker save/load 镜像迁移

**基本写法：导出镜像为 tar 文件**
`docker save -o <文件> <镜像>`
```bash
# 导出镜像为 tar 文件
docker save -o myapp.tar myapp:v1
```

**基本写法：导入 tar 镜像文件**
`docker load -i <文件>`
```bash
# 从 tar 文件导入镜像
docker load -i myapp.tar
```

**基本写法：导出多个镜像**
`docker save -o <文件> <镜像1> <镜像2>`
```bash
# 导出多个镜像到一个文件
docker save -o all.tar nginx redis mysql
```

---

## docker history 查看镜像层

**基本写法：查看镜像构建历史**
`docker history <镜像>`
```bash
# 查看 myapp 镜像的构建层
docker history myapp:v1
```

**基本写法：显示完整信息**
`docker history --no-trunc <镜像>`
```bash
# 显示完整的构建指令
docker history --no-trunc myapp:v1
```

---

## docker search 搜索镜像

**基本写法：搜索 Docker Hub 镜像**
`docker search <关键词>`
```bash
# 搜索 nginx 相关镜像
docker search nginx
```

**基本写法：限制搜索结果数量**
`docker search --limit <数量> <关键词>`
```bash
# 限制搜索结果为 5 个
docker search --limit 5 redis
```

---

## docker login 仓库认证

**基本写法：使用用户名密码登录**
`docker login -u <用户名> -p <密码> [仓库地址]`
```bash
# 使用账号密码登录
docker login -u myuser -p mypass registry.example.com
```

**基本写法：登出仓库**
`docker logout [仓库地址]`
```bash
# 登出 Docker Hub
docker logout
```
