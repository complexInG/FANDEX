# DevOps Dockerfile 语法

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## FROM 基础镜像

**基本写法：指定基础镜像**
`FROM <镜像>[:<标签>]`
```dockerfile
# 使用 nginx 作为基础镜像
FROM nginx:1.25
```

**基本写法：多阶段构建**
`FROM <镜像> AS <阶段名>`
```dockerfile
# 第一阶段构建
FROM golang:1.21 AS builder
WORKDIR /app
COPY . .
RUN go build -o myapp
```

---

## RUN 执行命令

**基本写法：执行 shell 命令**
`RUN <命令>`
```dockerfile
# 安装 nginx
RUN apt-get update && apt-get install -y nginx
```

**基本写法：exec 形式**
`RUN ["<可执行文件>", "<参数1>", "<参数2>"]`
```dockerfile
# 使用 exec 形式执行
RUN ["npm", "install", "--production"]
```

**基本写法：合并多条命令**
`RUN <命令1> && <命令2> && <命令3>`
```dockerfile
# 合并命令减少镜像层
RUN apt-get update \
    && apt-get install -y curl vim \
    && rm -rf /var/lib/apt/lists/*
```

---

## CMD 容器默认命令

**基本写法：shell 形式**
`CMD <命令>`
```dockerfile
# 默认启动 nginx
CMD nginx -g "daemon off;"
```

**基本写法：exec 形式（推荐）**
`CMD ["<可执行文件>", "<参数1>", "<参数2>"]`
```dockerfile
# exec 形式启动 nginx
CMD ["nginx", "-g", "daemon off;"]
```

**基本写法：作为 ENTRYPOINT 参数**
`CMD ["<参数1>", "<参数2>"]`
```dockerfile
# 给 ENTRYPOINT 提供默认参数
ENTRYPOINT ["python", "app.py"]
CMD ["--help"]
```

---

## ENTRYPOINT 入口点

**基本写法：固定执行命令**
`ENTRYPOINT ["<可执行文件>", "<参数>"]`
```dockerfile
# 固定入口点为 app.py
ENTRYPOINT ["python", "app.py"]
```

**基本写法：shell 形式**
`ENTRYPOINT <命令>`
```dockerfile
# shell 形式入口点
ENTRYPOINT python app.py
```

---

## COPY 复制文件

**基本写法：复制文件到镜像**
`COPY <源路径> <目标路径>`
```dockerfile
# 复制当前目录文件到镜像
COPY . /app
```

**基本写法：复制多个文件**
`COPY <文件1> <文件2> <目标目录>`
```dockerfile
# 复制多个配置文件
COPY package.json package-lock.json /app/
```

**基本写法：通配符匹配**
`COPY <通配符> <目标路径>`
```dockerfile
# 复制所有 .json 文件
COPY *.json /app/config/
```

---

## ADD 高级复制

**基本写法：复制并解压 tar 文件**
`ADD <文件> <目标路径>`
```dockerfile
# 自动解压 tar.gz 文件
ADD app.tar.gz /opt/
```

**基本写法：从 URL 下载文件**
`ADD <URL> <目标路径>`
```dockerfile
# 从 URL 下载文件
ADD https://example.com/file.zip /tmp/
```

---

## WORKDIR 工作目录

**基本写法：设置工作目录**
`WORKDIR <路径>`
```dockerfile
# 设置工作目录为 /app
WORKDIR /app
```

**基本写法：相对路径切换**
`WORKDIR <相对路径>`
```dockerfile
# 在已有工作目录下切换
WORKDIR /app
WORKDIR src
```

---

## ENV 环境变量

**基本写法：设置环境变量**
`ENV <键>=<值>`
```dockerfile
# 设置 NODE_ENV 环境变量
ENV NODE_ENV=production
```

**基本写法：设置多个环境变量**
`ENV <键1>=<值1> <键2>=<值2>`
```dockerfile
# 设置多个环境变量
ENV NODE_ENV=production PORT=3000
```

---

## ARG 构建参数

**基本写法：定义构建参数**
`ARG <参数名>[=<默认值>]`
```dockerfile
# 定义 VERSION 构建参数
ARG VERSION=latest
FROM node:$VERSION
```

**基本写法：使用构建参数**
`ARG <参数名>`
```dockerfile
# 在 RUN 中使用构建参数
ARG BUILD_DATE
RUN echo "Build date: $BUILD_DATE" > /build-date.txt
```

---

## EXPOSE 声明端口

**基本写法：声明容器端口**
`EXPOSE <端口>[/<协议>]`
```dockerfile
# 声明 80 端口
EXPOSE 80
```

**基本写法：声明多个端口**
`EXPOSE <端口1> <端口2>`
```dockerfile
# 声明 HTTP 和 HTTPS 端口
EXPOSE 80 443
```

**基本写法：声明 UDP 端口**
`EXPOSE <端口>/udp`
```dockerfile
# 声明 UDP 端口
EXPOSE 53/udp
```

---

## VOLUME 数据卷

**基本写法：声明匿名数据卷**
`VOLUME <路径>`
```dockerfile
# 声明数据卷
VOLUME /data
```

**基本写法：声明多个数据卷**
`VOLUME ["<路径1>", "<路径2>"]`
```dockerfile
# 声明多个数据卷
VOLUME ["/data", "/logs"]
```

---

## USER 切换用户

**基本写法：指定运行用户**
`USER <用户名>[:<组>]`
```dockerfile
# 切换到 node 用户运行
USER node
```

**基本写法：使用 UID**
`USER <UID>[:<GID>]`
```dockerfile
# 使用 UID 切换用户
USER 1000:1000
```

---

## LABEL 标签

**基本写法：添加镜像标签**
`LABEL <键>=<值>`
```dockerfile
# 添加维护者标签
LABEL maintainer="dev@example.com"
```

**基本写法：添加多个标签**
`LABEL <键1>=<值1> <键2>=<值2>`
```dockerfile
# 添加多个元数据标签
LABEL version="1.0" description="My App" author="dev-team"
```

---

## HEALTHCHECK 健康检查

**基本写法：设置健康检查**
`HEALTHCHECK [选项] CMD <命令>`
```dockerfile
# 每 30 秒检查一次健康状态
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost/ || exit 1
```

**基本写法：禁用健康检查**
`HEALTHCHECK NONE`
```dockerfile
# 禁用基础镜像的健康检查
HEALTHCHECK NONE
```
