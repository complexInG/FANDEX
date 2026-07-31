# CI/CD 流水线通用命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## GitLab CI/CD

**基本用法:配置文件结构**
`.gitlab-ci.yml`

```yaml
# .gitlab-ci.yml GitLab CI 基础配置
stages:
  - build
  - test
  - deploy

variables:
  IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

build:
  stage: build
  image: docker:24.0
  services:
  - docker:24.0-dind
  script:
  - docker build -t $IMAGE .
  - docker push $IMAGE
  only:
  - main

test:
  stage: test
  image: node:20
  script:
  - npm ci
  - npm test
  artifacts:
    reports:
      junit: test-results.xml

deploy:
  stage: deploy
  script:
  - kubectl apply -f k8s/
  only:
  - main
  when: manual
```

---

**基本用法:常用命令**
`gitlab-runner exec|register|verify`

```bash
# 注册 Runner
gitlab-runner register \
  --url https://gitlab.com \
  --token $RUNNER_TOKEN \
  --executor docker \
  --docker-image alpine:latest

# 列出已注册 Runner
gitlab-runner list

# 验证 Runner 连接
gitlab-runner verify

# 启动 Runner
gitlab-runner run

# 手动触发本地 job(测试用)
gitlab-runner exec docker build
```

---

**基本用法:条件与规则**
`rules / only / except`

```yaml
# rules 现代条件控制
build:
  stage: build
  script: make build
  rules:
  - if: $CI_PIPELINE_SOURCE == "merge_request_event"
    when: never
  - if: $CI_COMMIT_BRANCH == "main"
    changes:
    - src/**
    - Dockerfile
  - if: $CI_COMMIT_TAG =~ /^v\d+\.\d+\.\d+$/

# only/except 传统写法
deploy:
  script: deploy.sh
  only:
  - main
  - tags
  except:
  - branches
```

---

**基本用法:artifacts 与 cache**
`artifacts / cache`

```yaml
build:
  script: make build
  artifacts:
    paths:
    - bin/
    - dist/
    expire_in: 1 week
    reports:
      dotenv: build.env
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml

test:
  script: npm test
  cache:
    key:
      files:
      - package-lock.json
    paths:
    - node_modules/
    policy: pull-push
```

---

## GitHub Actions

**基本用法:Workflow 配置**
`.github/workflows/ci.yml`

```yaml
# .github/workflows/ci.yml GitHub Actions 基础
name: CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read
  packages: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-node@v4
      with:
        node-version: '20'
        cache: 'npm'
    - run: npm ci
    - run: npm test
    - run: npm run build
```

---

**基本用法:常用 actions**
`uses: <动作>@<版本>`

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - uses: actions/setup-java@v4
      with:
        java-version: '17'
        distribution: 'temurin'
        cache: maven

    - uses: docker/setup-buildx-action@v3
    - uses: docker/login-action@v3
      with:
        registry: ghcr.io
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
    - uses: docker/build-push-action@v5
      with:
        context: .
        push: true
        tags: ghcr.io/${{ github.repository }}:${{ github.sha }}
```

---

**基本用法:环境变量与密钥**
`env / secrets`

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    env:
      APP_ENV: production
      REGISTRY: ghcr.io
    steps:
    - uses: actions/checkout@v4
    - name: Deploy
      env:
        KUBE_CONFIG: ${{ secrets.KUBE_CONFIG }}
        DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
      run: |
        echo "$KUBE_CONFIG" | base64 -d > kubeconfig
        kubectl --kubeconfig kubeconfig apply -f k8s/

    - uses: aws-actions/configure-aws-credentials@v4
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-east-1
```

---

**基本用法:矩阵构建**
`strategy.matrix`

```yaml
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        node-version: ['18', '20', '22']
        exclude:
        - os: windows-latest
          node-version: '18'
        include:
        - os: ubuntu-latest
          node-version: '20'
          coverage: true
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-node@v4
      with:
        node-version: ${{ matrix.node-version }}
    - run: npm ci
    - run: npm test
```

---

## Jenkins Pipeline

**基本用法:声明式 Pipeline**
`Jenkinsfile`

```groovy
// Jenkinsfile 声明式 Pipeline
pipeline {
    agent any
    environment {
        IMAGE = "registry.example.com/myapp:${env.BUILD_NUMBER}"
        DOCKER_CREDENTIALS = credentials('docker-registry')
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }
        stage('Test') {
            steps {
                sh 'npm test'
            }
            post {
                always {
                    junit 'test-results.xml'
                    publishHTML([
                        reportDir: 'coverage',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'docker push $IMAGE'
                sh 'kubectl apply -f k8s/'
            }
        }
    }
    post {
        success {
            slackSend channel: '#deploy', message: "Build ${env.BUILD_NUMBER} succeeded"
        }
        failure {
            slackSend channel: '#alerts', message: "Build ${env.BUILD_NUMBER} failed"
        }
    }
}
```

---

**基本用法:脚本式 Pipeline**
`node { stage('...') { ... } }`

```groovy
// 脚本式 Pipeline
node('docker') {
    stage('Checkout') {
        git 'https://github.com/org/repo.git'
    }

    stage('Build') {
        def image = docker.build('myapp:latest')
        image.inside {
            sh 'make build'
        }
    }

    stage('Test') {
        try {
            sh 'make test'
        } catch (Exception e) {
            currentBuild.result = 'UNSTABLE'
            emailext subject: 'Tests failed',
                     body: 'Tests failed in build ${BUILD_NUMBER}',
                     to: 'team@example.com'
        }
    }

    stage('Deploy') {
        if (env.BRANCH_NAME == 'main') {
            sh 'make deploy'
        } else {
            echo "Skip deploy for branch ${env.BRANCH_NAME}"
        }
    }
}
```

---

**基本用法:Jenkins CLI**
`java -jar jenkins-cli.jar`

```bash
# 下载 CLI jar
wget http://jenkins:8080/jnlpJars/jenkins-cli.jar

# 列出 jobs
java -jar jenkins-cli.jar -s http://jenkins:8080 list-jobs

# 触发构建
java -jar jenkins-cli.jar -s http://jenkins:8080 build my-app

# 触发构建(带参数)
java -jar jenkins-cli.jar -s http://jenkins:8080 build my-app -p BRANCH=develop

# 查看构建日志
java -jar jenkins-cli.jar -s http://jenkins:8080 console my-app 123

# 重新加载配置
java -jar jenkins-cli.jar -s http://jenkins:8080 reload-configuration
```

---

## 通用工具命令

**基本用法:Docker 构建**
`docker build [选项] <上下文>`

```bash
# 基本构建
docker build -t myapp:latest .

# 指定 Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# 构建并打多标签
docker build -t myapp:latest -t myapp:v1.0 .

# 使用构建参数
docker build --build-arg VERSION=1.0 -t myapp:1.0 .

# 使用 BuildKit
DOCKER_BUILDKIT=1 docker build -t myapp:latest .

# 构建后扫描漏洞
docker build -t myapp:latest .
docker scout cves myapp:latest
```

---

**基本用法:镜像推送**
`docker push <镜像>`

```bash
# 登录仓库
docker login registry.example.com -u user -p pass

# 推送镜像
docker push myapp:latest

# 推送所有标签
docker push --all-tags myapp

# 推送后签名(cosign)
cosign sign --key cosign.key myapp:latest

# 推送多平台镜像
docker buildx build --platform linux/amd64,linux/arm64 \
  -t myapp:latest --push .
```

---

**基本用法:Kubernetes 部署**
`kubectl apply -f <清单>`

```bash
# 部署 YAML 清单
kubectl apply -f k8s/deployment.yaml -n production

# 部署整个目录
kubectl apply -f k8s/ -n production

# 从 Kustomize 部署
kubectl apply -k k8s/overlays/production

# 滚动重启
kubectl rollout restart deployment web -n production

# 等待部署完成
kubectl rollout status deployment web -n production --timeout=5m
```

---

## Helm 部署

**基本用法:CI/CD 中使用 Helm**
`helm upgrade --install <release> <chart>`

```bash
# 部署/升级 Helm Chart
helm upgrade --install myapp ./chart \
  -f values-production.yaml \
  --namespace production --create-namespace \
  --wait --timeout 5m

# 使用原子部署(失败自动回滚)
helm upgrade --install myapp ./chart \
  -f values-production.yaml \
  --namespace production \
  --atomic --wait

# 查看部署差异
helm diff upgrade myapp ./chart -f values-production.yaml

# 部署前 dry-run
helm upgrade --install myapp ./chart \
  -f values-production.yaml \
  --dry-run --debug
```

---

## 制品仓库管理

**基本用法:Nexus 制品仓库**
`curl -u <用户>:<密码> <仓库>/...`

```bash
# 上传 Docker 镜像
docker push nexus.example.com:8082/myapp:v1

# 上传 Maven 制品
curl -u admin:pass --upload-file target/app-1.0.jar \
  "http://nexus:8081/repository/maven-releases/com/example/app/1.0/app-1.0.jar"

# 上传 npm 包
npm publish --registry http://nexus:8081/repository/npm-private/

# 上传 PyPI 包
twine upload --repository-url http://nexus:8081/repository/pypi-hosted/ \
  dist/*.whl -u admin -p pass
```

---

**基本用法:JFrog Artifactory**
`jfrog rt upload|download`

```bash
# 上传制品
jfrog rt upload target/app.jar maven-releases/com/example/app/1.0/

# 下载制品
jfrog rt download maven-releases/com/example/app/1.0/app.jar

# 推送 Docker 镜像
docker push artifactory.example.com/docker/myapp:v1

# 提升制品(晋升)
jfrog rt move maven-snapshots maven-releases \
  --props="version=1.0.0"
```

---

## 通知与集成

**基本用法:Slack 通知**
`curl -X POST <webhook-url> -d '<json>'`

```bash
# 发送 Slack 通知
curl -X POST -H 'Content-Type: application/json' \
  https://hooks.slack.com/services/xxx \
  -d '{
    "text": "Build '"$CI_PIPELINE_ID"' succeeded",
    "channel": "#deploy",
    "attachments": [{
      "color": "good",
      "fields": [
        {"title": "Repository", "value": "'"$CI_PROJECT_NAME"'"},
        {"title": "Branch", "value": "'"$CI_COMMIT_BRANCH"'"}
      ]
    }]
  }'
```

---

**基本用法:钉钉/企业微信通知**
`curl -X POST <webhook-url>`

```bash
# 钉钉机器人通知
curl -X POST 'https://oapi.dingtalk.com/robot/send?access_token=xxx' \
  -H 'Content-Type: application/json' \
  -d '{
    "msgtype": "markdown",
    "markdown": {
      "title": "构建通知",
      "text": "## 构建成功\n项目: '"$CI_PROJECT_NAME"'\n分支: '"$CI_COMMIT_BRANCH"'\n[查看详情]('"$CI_PIPELINE_URL"')"
    }
  }'

# 企业微信通知
curl -X POST 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx' \
  -H 'Content-Type: application/json' \
  -d '{
    "msgtype": "markdown",
    "markdown": {
      "content": "## 构建成功\n> 项目: '"$CI_PROJECT_NAME"'\n> 分支: '"$CI_COMMIT_BRANCH"'"
    }
  }'
```

---

## 安全扫描

**基本用法:Trivy 漏洞扫描**
`trivy image <镜像>`

```bash
# 扫描镜像漏洞
trivy image myapp:latest

# 扫描指定严重级别
trivy image --severity HIGH,CRITICAL myapp:latest

# 输出 JSON 格式
trivy image --format json --output report.json myapp:latest

# 扫描文件系统
trivy fs --security-checks vuln,config .

# 扫描代码仓库
trivy repo https://github.com/org/repo
```

---

**基本用法:其他扫描工具**
`<工具> <参数>`

```bash
# Grype 漏洞扫描
grype myapp:latest

# Snyk 漏洞扫描
snyk container test myapp:latest

# Hadolint Dockerfile lint
hadolint Dockerfile

# kubeval 校验 K8s 清单
kubeval k8s/*.yaml

# conftest 策略检查
conftest test k8s/deployment.yaml -p policies/
```

---

## 缓存与优化

**基本用法:Docker 缓存**
`--cache-from / --cache-to`

```bash
# GitHub Actions 中使用缓存
docker buildx build \
  --cache-from type=gha \
  --cache-to type=gha,mode=max \
  -t myapp:latest .

# GitLab CI 中使用 registry 缓存
docker build \
  --cache-from $CI_REGISTRY_IMAGE:cache \
  -t $CI_REGISTRY_IMAGE:cache \
  -t $CI_REGISTRY_IMAGE:latest .

# 使用 BuildKit 缓存挂载
DOCKER_BUILDKIT=1 docker build \
  --build-arg BUILDKIT_CACHE_MOUNT_NS=app \
  -t myapp:latest .
```

---

**基本用法:依赖缓存**
`cache: <配置>`

```yaml
# GitLab CI npm 缓存
test:
  cache:
    key:
      files:
      - package-lock.json
    paths:
    - node_modules/
    - .npm/
  script:
  - npm ci --cache .npm --prefer-offline

# GitHub Actions 缓存
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'
- run: npm ci

# Maven 缓存
- uses: actions/cache@v4
  with:
    path: ~/.m2/repository
    key: ${{ runner.os }}-maven-${{ hashFiles('**/pom.xml') }}
    restore-keys: ${{ runner.os }}-maven-
```

---

## 排查与调试

**基本用法:本地测试 Pipeline**
`act / gitlab-runner exec`

```bash
# 使用 act 本地运行 GitHub Actions
act -j build

# 指定 event
act push -j build

# 详细输出
act -j build -v

# GitLab Runner 本地执行
gitlab-runner exec docker build

# 重新运行失败的 job
gitlab-runner exec docker --docker-privileged build
```

---

**基本用法:查看构建日志**
`<CI-CLI> logs <job>`

```bash
# GitLab 查看 job 日志
glab ci trace <job-id>

# GitHub Actions 日志
gh run view <run-id> --log

# Jenkins 构建日志
java -jar jenkins-cli.jar console my-app 123

# 实时跟踪日志
gh run watch <run-id>
```

---

**基本用法:排查构建失败**
`<检查步骤>`

```bash
# 进入 CI 容器调试
docker run -it --rm node:20 sh

# 重新运行 job 并保留容器
gitlab-runner exec docker build --docker-keep-cache

# 检查 CI 环境变量
env | grep -E 'CI_|GITHUB_'

# 检查 Docker 守护进程
docker info
docker system df

# 查看构建产物大小
du -sh target/ dist/
```
