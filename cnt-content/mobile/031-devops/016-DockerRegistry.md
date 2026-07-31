# Docker 镜像仓库命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 登录与登出

**基本用法:登录镜像仓库**
`docker login [选项] <仓库地址>`

```bash
# 登录 Docker Hub
docker login -u username

# 登录私有仓库
docker login registry.example.com -u deploy

# 使用密码文件(避免明文)
docker login registry.example.com -u deploy --password-stdin < pass.txt
```

---

**基本用法:登出**
`docker logout <仓库地址>`

```bash
# 登出指定仓库
docker logout registry.example.com
```

---

## 打标签与推送

**基本用法:打镜像标签**
`docker tag <镜像> <仓库>/<镜像>:<标签>`

```bash
# 给本地镜像打远程仓库标签
docker tag myapp:latest registry.example.com/myapp:v1.0

# 打 Docker Hub 标签
docker tag myapp username/myapp:latest
```

---

**基本用法:推送镜像**
`docker push <仓库>/<镜像>:<标签>`

```bash
# 推送镜像到私有仓库
docker push registry.example.com/myapp:v1.0

# 推送所有同名标签
docker push username/myapp --all-tags
```

---

## 拉取镜像

**基本用法:拉取镜像**
`docker pull <仓库>/<镜像>:<标签>`

```bash
# 拉取指定版本
docker pull registry.example.com/myapp:v1.0

# 拉取所有平台镜像
docker pull --all-tags username/myapp
```

---

## 搜索与 inspect

**基本用法:搜索镜像**
`docker search <关键词>`

```bash
# 搜索 Docker Hub 上的镜像
docker search nginx

# 限制结果数
docker search --limit 5 redis
```

---

**基本用法:查看镜像清单**
`docker manifest inspect <镜像>`

```bash
# 查看多架构镜像清单
docker manifest inspect nginx:latest
```

---

## 搭建本地仓库

**基本用法:运行 registry 容器**
`docker run -d -p 5000:5000 registry`

```bash
# 启动本地私有仓库
docker run -d -p 5000:5000 --restart=always --name registry registry:2

# 推送到本地仓库
docker tag myapp localhost:5000/myapp
docker push localhost:5000/myapp
```

---

## 清理与导出

**基本用法:导出镜像**
`docker save -o <文件> <镜像>`

```bash
# 导出镜像为 tar 文件
docker save -o app.tar myapp:latest

# 导出多个镜像
docker save -o all.tar image1 image2

# 导入镜像
docker load -i app.tar
```

---