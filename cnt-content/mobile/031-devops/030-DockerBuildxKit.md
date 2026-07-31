# Docker Buildx 与 BuildKit 命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Buildx 基础

**基本用法:查看 Buildx 版本**
`docker buildx version`

```bash
# 查看 buildx 版本
docker buildx version

# 查看构建器列表
docker buildx ls

# 查看 buildx 详细信息
docker buildx inspect default
```

---

**基本用法:创建构建器**
`docker buildx create --name <名称>`

```bash
# 创建新构建器
docker buildx create --name mybuilder --driver docker-container --use

# 创建远程构建器
docker buildx create --name remote-builder --driver remote tcp://192.168.1.10:1234

# 创建 kubernetes 构建器
docker buildx create --name k8s-builder --driver kubernetes --driver-opt namespace=buildkit

# 查看构建器详情
docker buildx inspect mybuilder --bootstrap
```

---

**基本用法:管理构建器**
`docker buildx use|rm|inspect`

```bash
# 切换构建器
docker buildx use mybuilder

# 查看当前构建器
docker buildx inspect

# 引导构建器(启动 BuildKit 容器)
docker buildx inspect --bootstrap

# 删除构建器
docker buildx rm mybuilder

# 停止构建器(不删除)
docker buildx stop mybuilder
```

---

## 构建镜像

**基本用法:基本构建**
`docker buildx build [选项] <上下文>`

```bash
# 基本构建
docker buildx build -t myapp:latest .

# 指定 Dockerfile
docker buildx build -f Dockerfile.prod -t myapp:prod .

# 构建并推送到仓库
docker buildx build -t registry.example.com/myapp:v1 --push .

# 构建到本地 docker
docker buildx build -t myapp:latest --load .

# 输出为 OCI tar 包
docker buildx build -t myapp:latest --output type=oci,dest=myapp.tar .
```

---

**基本用法:多平台构建**
`--platform <平台1>,<平台2>`

```bash
# 多平台构建并推送
docker buildx build --platform linux/amd64,linux/arm64 \
  -t registry.example.com/myapp:v1 --push .

# 多平台构建并保存为 tar
docker buildx build --platform linux/amd64,linux/arm64 \
  -t myapp:latest --output type=oci,dest=myapp-multi.tar .

# 查看支持的平台
docker buildx inspect --bootstrap | grep Platforms
```

---

**基本用法:输出类型**
`--output type=<类型>`

```bash
# 输出到 docker(本地镜像)
docker buildx build --output type=docker -t myapp:latest .

# 输出到本地目录
docker buildx build --output type=local,dest=./out .

# 输出为 tar 文件
docker buildx build --output type=tar,dest=myapp.tar .

# 输出为 OCI 格式
docker buildx build --output type=oci,dest=myapp-oci.tar .

# 输出为 Docker 格式 tar
docker buildx build --output type=docker,dest=myapp-docker.tar .

# 输出到 registry
docker buildx build --output type=registry -t registry.example.com/myapp:v1 .
```

---

## BuildKit 特性

**基本用法:启用 BuildKit**
`DOCKER_BUILDKIT=1`

```bash
# 通过环境变量启用
DOCKER_BUILDKIT=1 docker build -t myapp:latest .

# 配置 docker daemon 永久启用
# /etc/docker/daemon.json
# {
#   "features": { "buildkit": true }
# }

# 通过 buildx 默认使用 BuildKit
docker buildx build -t myapp:latest .
```

---

**基本用法:语法指令**
`# syntax=<镜像>`

```dockerfile
# 使用最新 BuildKit 前端
# syntax=docker/dockerfile:1.6

FROM alpine:3.19
RUN echo "使用 BuildKit 前端"
```

```bash
# 使用特定版本
# syntax=docker/dockerfile:1.6.0

# 使用实验性前端
# syntax=docker/dockerfile:1-labs
```

---

**基本用法:缓存挂载**
`RUN --mount=type=cache`

```dockerfile
# syntax=docker/dockerfile:1.6
FROM node:20 AS builder
WORKDIR /app

# npm 缓存挂载
COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm \
    npm ci

# Go 模块缓存
FROM golang:1.22 AS go-builder
WORKDIR /src
RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=bind,source=.,target=. \
    go build -o /app ./cmd/server
```

---

**基本用法:SSH 挂载**
`RUN --mount=type=ssh`

```dockerfile
# syntax=docker/dockerfile:1.6
FROM alpine:3.19

# 使用 SSH 拉取私有仓库
RUN --mount=type=ssh \
    apk add --no-cache openssh-client git && \
    mkdir -p ~/.ssh && \
    ssh-keyscan github.com >> ~/.ssh/known_hosts && \
    git clone git@github.com:org/repo.git
```

```bash
# 构建时使用 SSH agent 转发
docker buildx build --ssh default=$SSH_AUTH_SOCK -t myapp:latest .

# 使用具体密钥
docker buildx build --ssh mykey=/path/to/key -t myapp:latest .
```

---

**基本用法:secret 挂载**
`RUN --mount=type=secret`

```dockerfile
# syntax=docker/dockerfile:1.6
FROM alpine:3.19

# 挂载 secret 文件(不会留在镜像层)
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc \
    npm install --production

# 挂载多个 secret
RUN --mount=type=secret,id=db_password \
    --mount=type=secret,id=api_key \
    setup-app.sh
```

```bash
# 通过文件传递 secret
docker buildx build --secret id=npmrc,src=.npmrc -t myapp:latest .

# 通过环境变量传递
docker buildx build --secret id=db_password,env=DB_PASSWORD -t myapp:latest .

# 使用 secret ID 与不同源文件
docker buildx build \
  --secret id=npmrc,src=$HOME/.npmrc \
  --secret id=api_key,src=/run/secrets/api.key \
  -t myapp:latest .
```

---

## 高级构建技巧

**基本用法:并行构建**
`FROM <镜像> AS <阶段>`

```dockerfile
# syntax=docker/dockerfile:1.6
# 并行构建前端和后端
FROM node:20 AS frontend
WORKDIR /web
COPY web/ .
RUN npm ci && npm run build

FROM golang:1.22 AS backend
WORKDIR /src
COPY . .
RUN go build -o server ./cmd/server

# 同时执行测试(独立阶段)
FROM backend AS test
RUN go test ./...

# 最终镜像
FROM alpine:3.19
COPY --from=backend /src/server /app/server
COPY --from=frontend /web/dist /app/static
```

---

**基本用法:构建参数与标签**
`--build-arg / --label`

```bash
# 传递构建参数
docker buildx build \
  --build-arg VERSION=1.2.0 \
  --build-arg BUILD_DATE=$(date -u +%Y-%m-%dT%H:%M:%SZ) \
  -t myapp:1.2.0 .

# 添加 OCI 标签
docker buildx build \
  --label org.opencontainers.image.source="https://github.com/org/repo" \
  --label org.opencontainers.image.version="1.2.0" \
  --label maintainer="ops@example.com" \
  -t myapp:1.2.0 .

# 输出元数据信息
docker buildx imagetools inspect registry.example.com/myapp:1.2.0
```

---

**基本用法:缓存策略**
`--cache-from / --cache-to`

```bash
# 使用 registry 缓存
docker buildx build \
  --cache-from type=registry,ref=registry.example.com/myapp:cache \
  --cache-to type=registry,ref=registry.example.com/myapp:cache,mode=max \
  -t registry.example.com/myapp:v1 --push .

# 使用本地目录缓存
docker buildx build \
  --cache-from type=local,src=/tmp/.buildx-cache \
  --cache-to type=local,dest=/tmp/.buildx-cache-new \
  -t myapp:latest .

# 使用 GHA 缓存(GitHub Actions)
docker buildx build \
  --cache-from type=gha \
  --cache-to type=gha,mode=max \
  -t myapp:latest .

# 使用 S3 缓存
docker buildx build \
  --cache-from type=s3,region=us-east-1,bucket=my-cache \
  --cache-to type=s3,region=us-east-1,bucket=my-cache \
  -t myapp:latest .
```

---

## 推送与签名

**基本用法:推送镜像**
`docker buildx build --push`

```bash
# 构建并推送
docker buildx build -t registry.example.com/myapp:v1 --push .

# 多平台构建并推送
docker buildx build --platform linux/amd64,linux/arm64 \
  -t registry.example.com/myapp:v1 --push .

# 推送多个标签
docker buildx build \
  -t registry.example.com/myapp:v1.2.0 \
  -t registry.example.com/myapp:v1 \
  -t registry.example.com/myapp:latest \
  --push .
```

---

**基本用法:签名镜像(cosign)**
`cosign sign <镜像>`

```bash
# 签名镜像
cosign sign --key cosign.key registry.example.com/myapp:v1

# 用 OIDC 签名(无需密钥)
cosign sign --identity-token $OIDC_TOKEN registry.example.com/myapp:v1

# 验证签名
cosign verify --key cosign.pub registry.example.com/myapp:v1

# 签名时附加注解
cosign sign -a version=1.2.0 -a env=prod \
  --key cosign.key registry.example.com/myapp:v1
```

---

**基本用法:SBOM 与 provenance**
`--sbom / --provenance`

```bash
# 生成 SBOM(软件物料清单)
docker buildx build --sbom=true -t registry.example.com/myapp:v1 --push .

# 生成 provenance(来源证明)
docker buildx build --provenance=true -t registry.example.com/myapp:v1 --push .

# 生成 provenance(详细模式)
docker buildx build \
  --provenance=mode=max \
  -t registry.example.com/myapp:v1 --push .

# 查看镜像附件
docker buildx imagetools inspect registry.example.com/myapp:v1
```

---

## imagetools 工具

**基本用法:查看镜像**
`docker buildx imagetools inspect <镜像>`

```bash
# 查看镜像 manifest
docker buildx imagetools inspect registry.example.com/myapp:v1

# 查看镜像各平台详情
docker buildx imagetools inspect --raw registry.example.com/myapp:v1

# 查看镜像层级
docker buildx imagetools inspect --verbose registry.example.com/myapp:v1
```

---

**基本用法:创建 manifest list**
`docker buildx imagetools create`

```bash
# 合并多个平台镜像为 manifest list
docker buildx imagetools create \
  -t registry.example.com/myapp:v1 \
  registry.example.com/myapp:v1-amd64 \
  registry.example.com/myapp:v1-arm64

# 添加注解
docker buildx imagetools create \
  -t registry.example.com/myapp:v1 \
  --annotation "org.opencontainers.image.version=v1.0" \
  registry.example.com/myapp:v1-amd64 \
  registry.example.com/myapp:v1-arm64
```

---

## Bake 批量构建

**基本用法:bake 配置**
`docker buildx bake -f <bake.hcl>`

```hcl
# docker-bake.hcl 批量构建配置
group "default" {
  targets = ["app", "worker"]
}

target "app" {
  context = "."
  dockerfile = "Dockerfile.app"
  tags = ["registry.example.com/app:latest"]
  platforms = ["linux/amd64", "linux/arm64"]
}

target "worker" {
  context = "."
  dockerfile = "Dockerfile.worker"
  tags = ["registry.example.com/worker:latest"]
}

target "ci" {
  inherits = ["app", "worker"]
  tags = ["registry.example.com/app:ci", "registry.example.com/worker:ci"]
  cache-from = ["type=gha"]
  cache-to = ["type=gha,mode=max"]
}
```

---

**基本用法:执行 bake**
`docker buildx bake [目标]`

```bash
# 执行默认目标
docker buildx bake

# 执行指定目标
docker buildx bake app

# 执行多个目标
docker buildx bake app worker

# 执行 ci 目标
docker buildx bake ci

# 指定配置文件
docker buildx bake -f docker-bake.hcl app

# 打印配置(不执行)
docker buildx bake --print app

# 覆盖变量
APP_VERSION=v1.2.0 docker buildx bake app
```

---

## 排查与诊断

**基本用法:查看构建日志**
`docker buildx build --progress=<模式>`

```bash
# 详细进度(默认)
docker buildx build --progress=auto -t myapp:latest .

# 简洁模式
docker buildx build --progress=plain -t myapp:latest .

# 原始输出(适合日志)
docker buildx build --progress=rawjson -t myapp:latest .

# 静默模式
docker buildx build --progress=quiet -t myapp:latest .
```

---

**基本用法:调试构建器**
`docker buildx inspect`

```bash
# 查看构建器详情
docker buildx inspect mybuilder

# 查看 BuildKit 容器
docker ps --filter "name=buildx"

# 查看 BuildKit 日志
docker logs buildx_buildkit_mybuilder0

# 进入构建器容器调试
docker exec -it buildx_buildkit_mybuilder0 sh

# 查看 BuildKit 状态
docker buildx du mybuilder
```

---

**基本用法:清理构建缓存**
`docker buildx prune`

```bash
# 清理所有未使用的构建缓存
docker buildx prune

# 强制清理(无确认)
docker buildx prune -f

# 保留最近 24 小时的缓存
docker buildx prune --filter "until=24h"

# 保留指定大小以内
docker buildx prune --keep-storage 10gb

# 查看构建器磁盘使用
docker buildx du mybuilder
```

---

## CI/CD 集成

**基本用法:GitHub Actions 集成**
`.github/workflows/build.yml`

```yaml
# GitHub Actions 多平台构建示例
name: Build and Push
on:
  push:
    tags: ['v*']
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: docker/setup-qemu-action@v3
    - uses: docker/setup-buildx-action@v3
    - uses: docker/login-action@v3
      with:
        registry: registry.example.com
        username: ${{ secrets.REG_USER }}
        password: ${{ secrets.REG_PASS }}
    - uses: docker/build-push-action@v5
      with:
        context: .
        platforms: linux/amd64,linux/arm64
        push: true
        tags: registry.example.com/myapp:${{ github.ref_name }}
        cache-from: type=gha
        cache-to: type=gha,mode=max
        provenance: true
        sbom: true
```

---

**基本用法:GitLab CI 集成**
`.gitlab-ci.yml`

```yaml
# GitLab CI 多平台构建示例
build:
  image: docker:24.0
  services:
  - docker:24.0-dind
  variables:
    DOCKER_BUILDKIT: 1
    BUILDX_VERSION: 0.12.0
  before_script:
  - apk add --no-cache curl
  - mkdir -p ~/.docker/cli-plugins
  - curl -sSL -o ~/.docker/cli-plugins/docker-buildx
    https://github.com/docker/buildx/releases/download/v${BUILDX_VERSION}/buildx-v${BUILDX_VERSION}.linux-amd64
  - chmod +x ~/.docker/cli-plugins/docker-buildx
  - docker buildx create --use
  - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
  - docker buildx build
    --platform linux/amd64,linux/arm64
    --cache-from type=registry,ref=$CI_REGISTRY_IMAGE:cache
    --cache-to type=registry,ref=$CI_REGISTRY_IMAGE:cache,mode=max
    -t $CI_REGISTRY_IMAGE:$CI_COMMIT_TAG
    --push .
```
