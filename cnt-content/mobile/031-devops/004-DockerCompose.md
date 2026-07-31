# DevOps Docker Compose 编排

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## docker-compose up 启动服务

**基本写法：启动所有服务**
`docker-compose up`
```bash
# 前台启动所有服务
docker-compose up
```

**基本写法：后台启动服务**
`docker-compose up -d`
```bash
# 后台启动所有服务
docker-compose up -d
```

**基本写法：启动并重新构建镜像**
`docker-compose up --build`
```bash
# 重新构建镜像并启动
docker-compose up --build -d
```

**基本写法：启动指定服务**
`docker-compose up <服务名>`
```bash
# 只启动 web 服务
docker-compose up web
```

---

## docker-compose down 停止服务

**基本写法：停止并删除容器**
`docker-compose down`
```bash
# 停止并删除所有容器
docker-compose down
```

**基本写法：同时删除数据卷**
`docker-compose down -v`
```bash
# 停止服务并删除数据卷
docker-compose down -v
```

**基本写法：删除镜像**
`docker-compose down --rmi all`
```bash
# 停止服务并删除所有镜像
docker-compose down --rmi all
```

---

## docker-compose.yml 服务定义

**基本写法：定义服务**
```yaml
`version: "<版本>"
services:
  <服务名>:
    image: <镜像>`
```
```yaml
# 定义 web 服务
version: "3.9"
services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
```

**基本写法：使用 build 构建**
```yaml
`services:
  <服务名>:
    build: <Dockerfile 路径>`
```
```yaml
# 从 Dockerfile 构建服务
services:
  app:
    build: .
    ports:
      - "3000:3000"
```

---

## 端口映射与网络

**基本写法：端口映射**
```yaml
`services:
  <服务名>:
    ports:
      - "<宿主端口>:<容器端口>"`
```
```yaml
# 映射端口
services:
  web:
    image: nginx
    ports:
      - "8080:80"
      - "443:443"
```

**基本写法：自定义网络**
```yaml
`networks:
  <网络名>:
    driver: <驱动>`
```
```yaml
# 定义自定义网络
networks:
  appnet:
    driver: bridge
services:
  web:
    image: nginx
    networks:
      - appnet
```

---

## 数据卷挂载

**基本写法：挂载命名卷**
```yaml
`volumes:
  <卷名>:
services:
  <服务名>:
    volumes:
      - <卷名>:<容器路径>`
```
```yaml
# 使用命名卷
volumes:
  dbdata:
services:
  db:
    image: mysql
    volumes:
      - dbdata:/var/lib/mysql
```

**基本写法：绑定挂载宿主目录**
```yaml
`services:
  <服务名>:
    volumes:
      - <宿主路径>:<容器路径>`
```
```yaml
# 挂载当前目录到容器
services:
  app:
    build: .
    volumes:
      - .:/app
```

---

## 环境变量配置

**基本写法：定义环境变量**
```yaml
`services:
  <服务名>:
    environment:
      <键>: <值>`
```
```yaml
# 设置环境变量
services:
  db:
    image: mysql
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: appdb
```

**基本写法：使用 env 文件**
```yaml
`services:
  <服务名>:
    env_file:
      - <文件>`
```
```yaml
# 使用 .env 文件
services:
  app:
    image: myapp
    env_file:
      - .env
```

---

## 服务依赖

**基本写法：定义服务依赖关系**
```yaml
`services:
  <服务名>:
    depends_on:
      - <依赖服务>`
```
```yaml
# web 依赖 db 服务
services:
  web:
    image: nginx
    depends_on:
      - db
  db:
    image: mysql
```

**基本写法：依赖条件**
```yaml
`services:
  <服务名>:
    depends_on:
      <依赖服务>:
        condition: service_healthy`
```
```yaml
# 等待 db 健康检查通过
services:
  web:
    image: nginx
    depends_on:
      db:
        condition: service_healthy
```

---

## docker-compose ps/logs 查看状态

**基本写法：查看服务状态**
`docker-compose ps`
```bash
# 查看所有服务状态
docker-compose ps
```

**基本写法：查看服务日志**
`docker-compose logs <服务名>`
```bash
# 查看 web 服务日志
docker-compose logs web
```

**基本写法：实时跟踪所有日志**
`docker-compose logs -f`
```bash
# 实时跟踪所有服务日志
docker-compose logs -f
```

---

## docker-compose exec 进入容器

**基本写法：进入服务容器**
`docker-compose exec <服务名> <命令>`
```bash
# 进入 web 服务的 bash
docker-compose exec web bash
```

**基本写法：以指定用户进入**
`docker-compose exec -u <用户> <服务名> <命令>`
```bash
# 以 root 用户进入容器
docker-compose exec -u root web sh
```

---

## docker-compose restart/scale 操作

**基本写法：重启服务**
`docker-compose restart [服务名]`
```bash
# 重启 web 服务
docker-compose restart web
```

**基本写法：重新构建服务**
`docker-compose build <服务名>`
```bash
# 重新构建 web 服务镜像
docker-compose build web
```

**基本写法：拉取最新镜像**
`docker-compose pull`
```bash
# 拉取所有服务的最新镜像
docker-compose pull
```

---

## 指定 compose 文件

**基本写法：使用指定 compose 文件**
`docker-compose -f <文件> <命令>`
```bash
# 使用生产环境配置
docker-compose -f docker-compose.prod.yml up -d
```

**基本写法：多文件覆盖**
`docker-compose -f <文件1> -f <文件2> <命令>`
```bash
# 基础配置覆盖生产配置
docker-compose -f docker-compose.yml -f docker-compose.override.yml up
```
