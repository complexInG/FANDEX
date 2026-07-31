# Docker 多阶段构建速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 多阶段基础

**基本用法:多阶段 Dockerfile**
`FROM <镜像> AS <阶段名>`

```dockerfile
# 构建阶段
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# 运行阶段(更小镜像)
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

**基本用法:命名构建阶段**
`COPY --from=<阶段名> <源> <目标>`

```dockerfile
FROM golang:1.22 AS build
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o app ./cmd/server

FROM alpine:3.19
COPY --from=build /src/app /usr/local/bin/app
ENTRYPOINT ["app"]
```

---

## 选择阶段构建

**基本用法:只构建指定阶段**
`docker build --target <阶段名>`

```bash
# 仅构建测试阶段镜像
docker build --target test -t app:test .

# 多阶段用于不同环境
docker build --target dev -t app:dev .
docker build --target prod -t app:prod .
```

---

## 跨阶段依赖

**基本用法:多个构建阶段串联**
`COPY --from=<阶段>`

```dockerfile
# 编译前端
FROM node:20 AS frontend
WORKDIR /web
COPY web/ .
RUN npm ci && npm run build

# 编译后端
FROM golang:1.22 AS backend
WORKDIR /src
COPY . .
RUN go build -o server

# 最终镜像
FROM alpine:3.19
COPY --from=backend /src/server /app/server
COPY --from=frontend /web/dist /app/static
CMD ["/app/server"]
```

---

## 使用外部镜像

**基本用法:从外部镜像复制**
`COPY --from=<镜像>:<标签>`

```dockerfile
FROM alpine:3.19
# 从其他镜像复制二进制
COPY --from=redis:7-alpine /usr/local/bin/redis-server /usr/local/bin/
```

---

## 构建优化技巧

**基本用法:合并 RUN 减少层**
`RUN <命令1> && <命令2>`

```dockerfile
RUN apk add --no-cache curl git \
    && rm -rf /var/cache/apk/*
```

---

**基本用法:BuildKit 缓存挂载**
`RUN --mount=type=cache,target=<路径>`

```dockerfile
# syntax=docker/dockerfile:1.6
FROM node:20
WORKDIR /app
COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm \
    npm ci
```

---