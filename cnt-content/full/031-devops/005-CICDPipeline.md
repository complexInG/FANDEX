---
order: 5
title: 'CI/CD 流水线'
module: devops
category: 运维
difficulty: intermediate
description: 'CI/CD 原理、GitHub Actions、GitLab CI、Jenkins、ArgoCD 与发布策略。'
author: fanquanpp
updated: '2026-08-01'
related:
  - devops/容器与Docker
  - devops/Kubernetes容器编排
  - devops/语法速查
  - devops/监控与可观测性
prerequisites: []
---

## 1. 学习目标（Bloom 分类）

本节按照布鲁姆教育目标分类学组织学习路径。本文主题为《CI/CD 流水线》，属于 DevOps 模块，读者可以根据自身阶段选择阅读深度。

记忆层面：能够准确复述本文的核心概念、术语与基本语法或操作步骤，并能够在提问或检索时快速定位对应知识点。能够说出 DevOps 的核心概念、组件与标准流程。

理解层面：能够用自己的语言解释核心原理与工作机制，说明概念之间的因果关系，而不是机械记忆结论。能够解释 DevOps 的工作原理与关键机制。

应用层面：能够在真实项目或练习场景中运用本文知识解决具体问题，写出正确且可维护的实现。能够执行 DevOps 相关的标准操作与配置。

分析层面：能够拆解复杂问题，比较本文主题与相邻概念的异同，识别边界条件与例外情况。能够分析 DevOps 方案在可靠性、成本与性能上的权衡。

评价层面：能够根据约束条件（性能、可读性、安全、成本）评价不同方案的优劣，做出有依据的技术决策。能够评价 DevOps 中的技术选型。

创造层面：能够把本文知识与其他模块知识组合，设计出新的解决方案或可复用的工程模式。能够设计基于 DevOps 的完整解决方案。

通过本节学习，读者应当能够把《CI/CD 流水线》纳入自己的知识网络，并与 DevOps 模块的其他主题（CI/CD、容器、编排、监控、GitOps）建立关联。

## 2. 历史动机与发展脉络

《CI/CD 流水线》是 DevOps 领域的重要主题。要真正理解它，需要先了解它解决的问题与演进过程。

DevOps 源于 2009 年（“DevOpsDays”），核心是打破开发与运维壁垒，用自动化与协作缩短交付周期；CALMS 文化（文化、自动化、精益、度量、共享）是其框架。
技术栈演进：持续集成（CI）与持续交付（CD）、基础设施即代码（IaC）、容器（Docker）与编排（Kubernetes）、可观测性（监控/日志/追踪）。
2020 年代趋势：GitOps（声明式 + 自动同步）、平台工程（内部开发者平台）、FinOps（成本治理）、AI 辅助运维。

回到本文主题：CI/CD 流水线 的提出与成熟，正是上述技术背景下的必然产物。早期实现往往以简单可用为目标，随着工程规模扩大，社区逐渐沉淀出标准做法与最佳实践；理解这一脉络，可以帮助读者判断“为什么文档中的推荐写法是现在这个样子”，也能在遇到历史遗留代码时准确识别其设计年代与取舍。


## 3. 形式化定义与核心概念精讲

本节把《CI/CD 流水线》涉及的核心概念以“定义 + 讲解”的形式展开。读者应把定义当作工具，把讲解当作理解路径；两者结合才能形成可迁移的知识。

CI/CD 管线：代码提交 -> 构建 -> 测试 -> 制品 -> 部署；流水线即代码（GitHub Actions/Jenkins/GitLab CI）。
容器与镜像：OCI 规范、Dockerfile 分层、镜像仓库与签名；容器隔离（cgroup/namespace）。
编排：Kubernetes 的 Pod/Deployment/Service 抽象；声明式期望状态与控制器调和。

### 3.1 原文章节逐一精讲

原文档把主题拆分为 19 个小节，下面按顺序给出每一节的导读讲解，随后保留原文细节供精读。

#### 原文精读（完整保留）

# CI/CD 流水线通用命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

#### 1. CI/CD 原理

##### 1.1 核心概念

| 概念               | 描述                   | 目标           |
| :----------------- | :--------------------- | :------------- |
| **CI（持续集成）** | 频繁合并代码并自动验证 | 尽早发现问题   |
| **CD（持续交付）** | 自动化部署到预生产环境 | 随时可发布     |
| **CD（持续部署）** | 自动化部署到生产环境   | 每次提交都发布 |

##### 1.2 流水线阶段

```
代码提交 → 构建 → 单元测试 → 集成测试 → 安全扫描
    → 制品发布 → 部署预发 → 验收测试 → 部署生产
```

#### 2. GitHub Actions

##### 2.1 基础配置

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: '20'
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # 代码检查
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck

  # 单元测试
  test:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npm test -- --coverage
      - uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}

  # 构建镜像
  build:
    runs-on: ubuntu-latest
    needs: test
    if: github.event_name == 'push'
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/metadata-action@v5
        id: meta
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=sha,prefix=
            type=ref,event=branch
            type=semver,pattern={{version}}
      - uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  # 部署
  deploy:
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'
    environment: production
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to Kubernetes
        run: |
          kubectl set image deployment/web web=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:sha-${{ github.sha }}
          kubectl rollout status deployment/web --timeout=300s
```

##### 2.2 常用 Action

| Action                        | 用途         |
| :---------------------------- | :----------- |
| `actions/checkout@v4`         | 检出代码     |
| `actions/setup-node@v4`       | 配置 Node.js |
| `actions/setup-python@v5`     | 配置 Python  |
| `docker/build-push-action@v5` | 构建推送镜像 |
| `actions/cache@v4`            | 缓存依赖     |

#### 3. GitLab CI

##### 3.1 基础配置

```yaml
# .gitlab-ci.yml
stages:
  - lint
  - test
  - build
  - deploy

variables:
  DOCKER_REGISTRY: registry.example.com
  APP_IMAGE: $DOCKER_REGISTRY/myapp

# 缓存配置
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .npm/

# 代码检查
lint:
  stage: lint
  image: node:20-alpine
  script:
    - npm ci
    - npm run lint
    - npm run typecheck
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

# 测试
test:
  stage: test
  image: node:20-alpine
  services:
    - postgres:16-alpine
  variables:
    POSTGRES_DB: testdb
    POSTGRES_USER: test
    POSTGRES_PASSWORD: test
    DATABASE_URL: postgresql://test:test@postgres:5432/testdb
  script:
    - npm ci
    - npm test -- --coverage
  coverage: '/Statements\s*:\s*(\d+\.?\d*)%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

# 构建镜像
build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  before_script:
    - echo $CI_REGISTRY_PASSWORD | docker login -u $CI_REGISTRY_USER --password-stdin $CI_REGISTRY
  script:
    - docker build -t $APP_IMAGE:$CI_COMMIT_SHORT_SHA .
    - docker push $APP_IMAGE:$CI_COMMIT_SHORT_SHA
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

# 部署生产
deploy:production:
  stage: deploy
  image: bitnami/kubectl
  script:
    - kubectl config use-context production
    - kubectl set image deployment/web web=$APP_IMAGE:$CI_COMMIT_SHORT_SHA
    - kubectl rollout status deployment/web --timeout=300s
  environment:
    name: production
    url: https://example.com
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
  when: manual
```

#### 4. Jenkins

##### 4.1 Jenkinsfile

```groovy
// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any

    environment {
        REGISTRY = 'registry.example.com'
        IMAGE = "${REGISTRY}/myapp"
        TAG = "${env.BUILD_NUMBER}"
    }

    tools {
        nodejs 'Node20'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh 'npm ci'
            }
        }

        stage('Lint') {
            steps {
                sh 'npm run lint'
            }
        }

        stage('Test') {
            steps {
                sh 'npm test -- --coverage'
            }
            post {
                always {
                    junit 'reports/junit.xml'
                    publishHTML(target: [
                        reportDir: 'coverage',
                        reportFiles: 'index.html',
                        reportName: 'Coverage'
                    ])
                }
            }
        }

        stage('Build') {
            steps {
                sh "docker build -t ${IMAGE}:${TAG} ."
                sh "docker push ${IMAGE}:${TAG}"
            }
        }

        stage('Deploy') {
            steps {
                input 'Deploy to production?'
                sh "kubectl set image deployment/web web=${IMAGE}:${TAG}"
                sh 'kubectl rollout status deployment/web --timeout=300s'
            }
        }
    }

    post {
        success {
            slackSend(color: 'good', message: "Build ${TAG} deployed successfully!")
        }
        failure {
            slackSend(color: 'danger', message: "Build ${TAG} failed!")
        }
        always {
            cleanWs()
        }
    }
}
```

#### 5. ArgoCD

##### 5.1 GitOps 模式

```mermaid
flowchart LR
    D[开发者] -->|push| G[Git 仓库]
    A[ArgoCD] <-->|sync| G
    A -->|apply| K[Kubernetes]
```

##### 5.2 ArgoCD Application

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/myapp-manifests.git
    targetRevision: main
    path: overlays/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
      - ServerSideApply=true
    retry:
      limit: 3
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

#### 6. 发布策略

##### 6.1 蓝绿发布

```mermaid
flowchart LR
    B1[Blue v1 当前版本<br/>← 流量] G1[Green v2 新版本<br/>无流量]
    B2[Blue v1 旧版本<br/>无流量] G2[Green v2 当前版本<br/>← 流量]
    B1 -->|切换流量| G2
```

```yaml
# 蓝绿发布 - ArgoCD + Service 切换
apiVersion: v1
kind: Service
metadata:
  name: web-active
spec:
  selector:
    app: web
    version: green # 切换时修改 blue/green
  ports:
    - port: 80
      targetPort: 8080
```

##### 6.2 金丝雀发布

```yaml
# 使用 Argo Rollouts
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: web-rollout
spec:
  replicas: 10
  strategy:
    canary:
      steps:
        - setWeight: 10 # 10% 流量到新版本
        - pause: { duration: 5m }
        - setWeight: 30 # 30% 流量
        - pause: { duration: 5m }
        - setWeight: 60 # 60% 流量
        - pause: { duration: 5m }
        - setWeight: 100 # 全量
      canaryService: web-canary
      stableService: web-stable
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web
          image: myapp:v2
```

##### 6.3 发布策略对比

| 策略         | 回滚速度 | 风险 | 资源消耗  | 复杂度 |
| :----------- | :------- | :--- | :-------- | :----- |
| **滚动更新** | 中       | 中   | 低        | 低     |
| **蓝绿发布** | 快       | 低   | 高（2倍） | 中     |
| **金丝雀**   | 快       | 低   | 中        | 高     |
| **A/B 测试** | 快       | 低   | 高        | 高     |

#### 7. 制品管理

##### 7.1 制品仓库

| 仓库                  | 类型   | 特点                       |
| :-------------------- | :----- | :------------------------- |
| **Nexus**             | 通用   | 支持 Docker/NPM/Maven/PyPI |
| **Harbor**            | Docker | 企业级、漏洞扫描           |
| **JFrog Artifactory** | 通用   | 功能最全、商业产品         |
| **GitHub Packages**   | 通用   | 与 GitHub 集成             |

##### 7.2 镜像标签策略

| 标签            | 用途      | 示例           |
| :-------------- | :-------- | :------------- |
| `latest`        | 最新版本  | 不推荐生产使用 |
| `sha-xxxxxx`    | Git SHA   | 精确追溯       |
| `v1.2.3`        | 语义版本  | 正式发布       |
| `main-20260614` | 分支+日期 | 持续部署       |

#### 8. 流水线设计原则

##### 8.1 最佳实践

| 原则           | 描述                              |
| :------------- | :-------------------------------- |
| **快速反馈**   | Lint 和单元测试先行，快速发现问题 |
| **并行执行**   | 独立任务并行运行，缩短总时间      |
| **缓存优化**   | 缓存依赖和构建产物                |
| **安全扫描**   | 集成 SAST/DAST/SCA                |
| **制品不可变** | 一次构建，多处部署                |
| **环境一致**   | 开发/测试/生产使用相同镜像        |
| **最小权限**   | CI/CD 凭证按需授权                |

##### 8.2 流水线安全

```yaml
# GitHub Actions 安全实践
jobs:
  build:
    permissions:
      contents: read # 只读代码
      packages: write # 写入包
    steps:
      # 使用 OIDC 而非长期密钥
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789:role/github-actions
          aws-region: us-east-1

      # 审计第三方 Action
      - uses: actions/checkout@v4 # 使用特定版本，不用 main
```

#### 9. 小结

CI/CD 是 DevOps 的核心实践：

1. **GitHub Actions** 适合开源项目和 GitHub 生态
2. **GitLab CI** 适合自托管和完整 DevOps 平台
3. **Jenkins** 适合复杂的企业级流水线
4. **ArgoCD** 实现 GitOps，声明式管理 K8s 部署
5. **金丝雀发布**是生产环境推荐策略，渐进式降低风险
6. 流水线设计需关注**快速反馈、安全扫描和制品不可变性**
#### GitLab CI/CD

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

#### GitHub Actions

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

#### Jenkins Pipeline

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

#### 通用工具命令

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

#### Helm 部署

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

#### 制品仓库管理

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

#### 通知与集成

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

#### 安全扫描

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

#### 缓存与优化

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

#### 排查与调试

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


### 3.2 概念关系图

下面用 Mermaid 图表达本文核心概念之间的关系，帮助读者建立整体图景：

```mermaid
flowchart LR
    A["CI/CD 流水线"] --> B["核心概念"]
    B --> C["原理机制"]
    B --> D["代码实践"]
    C --> E["工程应用"]
    D --> E
```

图中展示的是本文知识的结构化关系：核心概念是入口，原理机制解释“为什么”，代码实践演示“怎么做”，工程应用回答“何时用”。读者学习时可以把每个小节的内容挂接到对应节点上。

## 4. 理论推导与原理解析

本节深入《CI/CD 流水线》背后的原理。理论部分不求面面俱到，而是聚焦“能解释现象、能指导实践”的关键推导。

CI/CD 管线：代码提交 -> 构建 -> 测试 -> 制品 -> 部署；流水线即代码（GitHub Actions/Jenkins/GitLab CI）。
容器与镜像：OCI 规范、Dockerfile 分层、镜像仓库与签名；容器隔离（cgroup/namespace）。
编排：Kubernetes 的 Pod/Deployment/Service 抽象；声明式期望状态与控制器调和。
可观测性三支柱：指标（Prometheus）、日志（Loki/ELK）、追踪（OpenTelemetry）。

需要强调的是，理论推导与工程实践之间存在翻译层：理论给出的是理想化模型与边界条件，工程代码则必须处理真实环境中的例外。读者在学习时应先掌握理论的“标准情形”，再通过陷阱章节了解“非标准情形”。

## 5. 代码示例与逐行讲解

本节把原文中的代码示例系统整理，并为每个示例补充用途说明与讲解。读者不应只浏览代码，而应逐段对照讲解理解设计意图。

### 5.1 示例：1.2 流水线阶段

该示例来自原文《1.2 流水线阶段》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

```text
代码提交 → 构建 → 单元测试 → 集成测试 → 安全扫描
    → 制品发布 → 部署预发 → 验收测试 → 部署生产
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 2 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.2 示例：2.1 基础配置

该示例来自原文《2.1 基础配置》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

```yaml
# .github/workflows/ci.yml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: '20'
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # 代码检查
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm run typecheck

  # 单元测试
  test:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'
      - run: npm ci
      - run: npm test -- --coverage
      - uses: codecov/codecov-action@v4
        with:
          token: ${{ secrets.CODECOV_TOKEN }}

  # 构建镜像
  build:
    runs-on: ubuntu-latest
    needs: test
    if: github.event_name == 'push'
    permissions:
      contents: read
      packages: write
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/metadata-action@v5
        id: meta
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=sha,prefix=
            type=ref,event=branch
            type=semver,pattern={{version}}
      - uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  # 部署
  deploy:
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'
    environment: production
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to Kubernetes
        run: |
          kubectl set image deployment/web web=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:sha-${{ github.sha }}
          kubectl rollout status deployment/web --timeout=300s
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 82 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.3 示例：3.1 基础配置

该示例来自原文《3.1 基础配置》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

```yaml
# .gitlab-ci.yml
stages:
  - lint
  - test
  - build
  - deploy

variables:
  DOCKER_REGISTRY: registry.example.com
  APP_IMAGE: $DOCKER_REGISTRY/myapp

# 缓存配置
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .npm/

# 代码检查
lint:
  stage: lint
  image: node:20-alpine
  script:
    - npm ci
    - npm run lint
    - npm run typecheck
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

# 测试
test:
  stage: test
  image: node:20-alpine
  services:
    - postgres:16-alpine
  variables:
    POSTGRES_DB: testdb
    POSTGRES_USER: test
    POSTGRES_PASSWORD: test
    DATABASE_URL: postgresql://test:test@postgres:5432/testdb
  script:
    - npm ci
    - npm test -- --coverage
  coverage: '/Statements\s*:\s*(\d+\.?\d*)%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

# 构建镜像
build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  before_script:
    - echo $CI_REGISTRY_PASSWORD | docker login -u $CI_REGISTRY_USER --password-stdin $CI_REGISTRY
  script:
    - docker build -t $APP_IMAGE:$CI_COMMIT_SHORT_SHA .
    - docker push $APP_IMAGE:$CI_COMMIT_SHORT_SHA
  rules:
    - if: $CI_COMMIT_BRANCH == "main"

# 部署生产
deploy:production:
  stage: deploy
  image: bitnami/kubectl
  script:
    - kubectl config use-context production
    - kubectl set image deployment/web web=$APP_IMAGE:$CI_COMMIT_SHORT_SHA
    - kubectl rollout status deployment/web --timeout=300s
  environment:
    name: production
    url: https://example.com
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
  when: manual
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 72 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.4 示例：4.1 Jenkinsfile

该示例来自原文《4.1 Jenkinsfile》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

```groovy
// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any

    environment {
        REGISTRY = 'registry.example.com'
        IMAGE = "${REGISTRY}/myapp"
        TAG = "${env.BUILD_NUMBER}"
    }

    tools {
        nodejs 'Node20'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh 'npm ci'
            }
        }

        stage('Lint') {
            steps {
                sh 'npm run lint'
            }
        }

        stage('Test') {
            steps {
                sh 'npm test -- --coverage'
            }
            post {
                always {
                    junit 'reports/junit.xml'
                    publishHTML(target: [
                        reportDir: 'coverage',
                        reportFiles: 'index.html',
                        reportName: 'Coverage'
                    ])
                }
            }
        }

        stage('Build') {
            steps {
                sh "docker build -t ${IMAGE}:${TAG} ."
                sh "docker push ${IMAGE}:${TAG}"
            }
        }

        stage('Deploy') {
            steps {
                input 'Deploy to production?'
                sh "kubectl set image deployment/web web=${IMAGE}:${TAG}"
                sh 'kubectl rollout status deployment/web --timeout=300s'
            }
        }
    }

    post {
        success {
            slackSend(color: 'good', message: "Build ${TAG} deployed successfully!")
        }
        failure {
            slackSend(color: 'danger', message: "Build ${TAG} failed!")
        }
        always {
            cleanWs()
        }
    }
}
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 68 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.5 示例：5.1 GitOps 模式

该示例来自原文《5.1 GitOps 模式》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

```mermaid
flowchart LR
    D[开发者] -->|push| G[Git 仓库]
    A[ArgoCD] <-->|sync| G
    A -->|apply| K[Kubernetes]
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.6 示例：5.2 ArgoCD Application

该示例来自原文《5.2 ArgoCD Application》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/myapp-manifests.git
    targetRevision: main
    path: overlays/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
      - ServerSideApply=true
    retry:
      limit: 3
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 28 行有效代码，包含 1 类关键结构（apiVersion）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.7 示例：6.1 蓝绿发布

该示例来自原文《6.1 蓝绿发布》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

```mermaid
flowchart LR
    B1[Blue v1 当前版本<br/>← 流量] G1[Green v2 新版本<br/>无流量]
    B2[Blue v1 旧版本<br/>无流量] G2[Green v2 当前版本<br/>← 流量]
    B1 -->|切换流量| G2
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 4 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.8 示例：6.1 蓝绿发布

该示例来自原文《6.1 蓝绿发布》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

```yaml
# 蓝绿发布 - ArgoCD + Service 切换
apiVersion: v1
kind: Service
metadata:
  name: web-active
spec:
  selector:
    app: web
    version: green # 切换时修改 blue/green
  ports:
    - port: 80
      targetPort: 8080
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 12 行有效代码，包含 1 类关键结构（apiVersion）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.9 示例：6.2 金丝雀发布

该示例来自原文《6.2 金丝雀发布》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

```yaml
# 使用 Argo Rollouts
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: web-rollout
spec:
  replicas: 10
  strategy:
    canary:
      steps:
        - setWeight: 10 # 10% 流量到新版本
        - pause: { duration: 5m }
        - setWeight: 30 # 30% 流量
        - pause: { duration: 5m }
        - setWeight: 60 # 60% 流量
        - pause: { duration: 5m }
        - setWeight: 100 # 全量
      canaryService: web-canary
      stableService: web-stable
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web
          image: myapp:v2
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 30 行有效代码，包含 1 类关键结构（apiVersion）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.10 示例：8.2 流水线安全

该示例来自原文《8.2 流水线安全》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

```yaml
# GitHub Actions 安全实践
jobs:
  build:
    permissions:
      contents: read # 只读代码
      packages: write # 写入包
    steps:
      # 使用 OIDC 而非长期密钥
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789:role/github-actions
          aws-region: us-east-1

      # 审计第三方 Action
      - uses: actions/checkout@v4 # 使用特定版本，不用 main
```

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 14 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.11 示例：GitLab CI/CD

该示例来自原文《GitLab CI/CD》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 33 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.12 示例：GitLab CI/CD

该示例来自原文《GitLab CI/CD》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 14 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.13 示例：GitLab CI/CD

该示例来自原文《GitLab CI/CD》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 20 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.14 示例：GitLab CI/CD

该示例来自原文《GitLab CI/CD》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 21 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.15 示例：GitHub Actions

该示例来自原文《GitHub Actions》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 22 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.16 示例：GitHub Actions

该示例来自原文《GitHub Actions》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 23 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.17 示例：GitHub Actions

该示例来自原文《GitHub Actions》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 20 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.18 示例：GitHub Actions

该示例来自原文《GitHub Actions》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 22 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.19 示例：Jenkins Pipeline

该示例来自原文《Jenkins Pipeline》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 52 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.20 示例：Jenkins Pipeline

该示例来自原文《Jenkins Pipeline》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 29 行有效代码，包含 3 类关键结构（def、if、for）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.21 示例：Jenkins Pipeline

该示例来自原文《Jenkins Pipeline》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 12 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.22 示例：通用工具命令

该示例来自原文《通用工具命令》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 13 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.23 示例：通用工具命令

该示例来自原文《通用工具命令》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 11 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.24 示例：通用工具命令

该示例来自原文《通用工具命令》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.25 示例：Helm 部署

该示例来自原文《Helm 部署》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 16 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.26 示例：制品仓库管理

该示例来自原文《制品仓库管理》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.27 示例：制品仓库管理

该示例来自原文《制品仓库管理》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 9 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.28 示例：通知与集成

该示例来自原文《通知与集成》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 14 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.29 示例：通知与集成

该示例来自原文《通知与集成》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 19 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.30 示例：安全扫描

该示例来自原文《安全扫描》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.31 示例：安全扫描

该示例来自原文《安全扫描》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.32 示例：缓存与优化

该示例来自原文《缓存与优化》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 14 行有效代码，包含 1 类关键结构（from）。其中：

- 入口与初始化部分负责建立上下文，对应实际项目中的启动或装配逻辑；
- 核心逻辑部分体现本文主题的主要操作，是阅读时最需要对照讲解理解的部分；
- 输出或返回部分把结果交给调用方，注意其类型与边界条件。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.33 示例：缓存与优化

该示例来自原文《缓存与优化》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 23 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.34 示例：排查与调试

该示例来自原文《排查与调试》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 10 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.35 示例：排查与调试

该示例来自原文《排查与调试》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 8 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。

### 5.36 示例：排查与调试

该示例来自原文《排查与调试》小节，用于演示CI/CD 流水线相关操作。阅读时请先看代码结构，再看其后的讲解。

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

讲解：这段代码演示了本节核心知识点。代码中的关键操作可以归纳为三步：准备（定义或初始化）、执行（核心逻辑）、收尾（释放资源或返回结果）。实际项目中，这三步往往被封装为函数或类，以提升复用性与可测试性。

关键点分析：

该示例共 11 行有效代码，结构以数据或配置为主。阅读时应关注：数据字段的含义、配置项的作用，以及它们与运行行为的对应关系。

进阶思考路径：先尝试修改参数观察行为变化，再把示例中的模式迁移到自己的项目中；每次修改都记录预期与实测差异，这是把示例转化为能力的最快方式。


综合以上示例，可以总结出本主题的代码实践要点：第一，先定义清晰的输入输出契约；第二，核心逻辑保持单一职责；第三，错误处理与边界条件不可省略；第四，命名与注释表达意图而非复述代码。

## 6. 对比分析

对比是理解《CI/CD 流水线》定位的最快路径。下面从多个维度与相邻方案进行对比。

CI 与 CD：CI 保证可集成，CD 保证可交付；两者可独立实施。
Kubernetes 与 Docker Compose：K8s 生产级编排；Compose 单机开发。
传统运维与 SRE：SRE 用软件工程方法运维，错误预算与 SLO。

对比的目的不是分出绝对优劣，而是建立选择依据：不同约束条件下，最优解不同。读者应把每个对比维度转化为决策检查清单。

## 7. 常见陷阱与最佳实践

本节整理该主题的高频错误与推荐做法。每个陷阱先描述现象，再解释原因，最后给出最佳实践。

### 7.1 环境漂移

手工配置导致环境不一致。全部走 IaC 与镜像。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，环境漂移 一般源于对 DevOps 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，环境漂移 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理环境漂移的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.2 秘密硬编码

密钥进仓库。使用 Secret 管理与注入。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，秘密硬编码 一般源于对 DevOps 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，秘密硬编码 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理秘密硬编码的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.3 构建不可复现

依赖未锁定。锁定依赖版本与基础镜像 digest。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，构建不可复现 一般源于对 DevOps 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，构建不可复现 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理构建不可复现的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.4 测试后置

问题到生产才发现。左移：单元/集成/E2E 分层。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，测试后置 一般源于对 DevOps 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，测试后置 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理测试后置的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.5 回滚缺失

发布失败无法回退。保留历史镜像与一键回滚。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，回滚缺失 一般源于对 DevOps 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，回滚缺失 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理回滚缺失的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.6 监控盲区

无指标与告警。核心链路全量可观测。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，监控盲区 一般源于对 DevOps 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，监控盲区 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理监控盲区的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.7 权限过大

CI 权限超需求。最小权限与短期凭证。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，权限过大 一般源于对 DevOps 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，权限过大 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理权限过大的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.8 部署频率低

大爆炸发布风险高。小步快跑与灰度。

深入讲解：该问题之所以被归类为“常见陷阱”，是因为它在初学者的代码中反复出现，而且往往不在第一时间暴露——错误通常隐藏在特定数据或特定时序下。

从成因上看，部署频率低 一般源于对 DevOps 某个机制的理解偏差：要么误用了默认行为，要么忽略了边界条件，要么把其他语言的思维惯性带了过来。

从影响上看，部署频率低 轻则产生错误结果，重则导致资源泄漏、数据损坏或安全事故；这也是为什么工程评审中会把它列为检查项。

从修复策略上看，处理部署频率低的正确顺序是：先复现（构造最小用例），再定位（确认机制层面的根因），最后修复并补充回归测试。跳过复现直接改代码，往往治标不治本。

### 7.0 最佳实践总览

1. 一切皆代码：流水线、基础设施、配置版本化。
2. 发布可重复：相同代码 + 相同制品 -> 相同环境。
3. 失败可预期：小批量、金丝雀、自动回滚。
4. 度量驱动：DORA 指标（部署频率、变更前置时间、恢复时间、变更失败率）。

把这些最佳实践固化为团队规范与代码评审检查项，是避免同类问题反复出现的关键。

## 8. 工程实践

本节把《CI/CD 流水线》放入真实工程场景，给出可复用的模式与组织方法。

GitHub Actions：workflow/job/step 模型，矩阵测试，环境与密钥管理。
GitOps：Argo CD 同步 Git 仓库与集群状态，PR 即发布审批。
平台工程：模板化应用脚手架（Backstage）、自助环境、成本可视化。

### 8.1 工程实践的原则拆解

以上工程实践可以归纳为四条原则。第一，配置与代码分离：DevOps 项目中环境差异应通过配置注入，而不是散落在代码分支中；这保证同一份代码可以在开发、测试、生产环境一致运行。

第二，接口稳定优先：对外接口（函数签名、协议、数据格式）一旦被消费方依赖，变更成本极高；设计时应预留扩展点并保持向后兼容。

第三，可观测性内置：日志、指标与追踪应该在功能开发时同步设计，而不是故障发生后补救；没有观测手段的模块等于黑盒。

第四，变更可回滚：任何发布都应有对应的回滚方案；数据库迁移、配置变更与代码发布一样需要版本管理与逆向路径。

### 8.2 实践落地的检查清单

- [ ] GitHub Actions：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。
- [ ] GitOps：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。
- [ ] 平台工程：对照本节描述，检查当前项目是否已经落实；未落实的项列入技术债并排期处理。

工程实践的共性原则：配置与代码分离、接口稳定优先、可观测性内置、变更可回滚。这些原则适用于本主题的所有实现。

## 9. 案例研究

本节通过一个完整案例把《CI/CD 流水线》的知识串起来。案例按“需求分析、方案设计、实现、验证”四步展开。

需求：为微服务搭建从提交到生产的自动化管线。
方案：GitHub Actions 构建镜像 + 测试 + 扫描，Argo CD 部署到 K8s，Prometheus 监控。
要点：镜像 tag 用 commit SHA；金丝雀发布；回滚演练。
验证：发布频率与失败率度量、故障注入演练。

### 9.1 案例的扩展讨论

把案例中的方案放大到真实规模，需要额外考虑三个问题：

第一，规模：当数据量或并发量上升一个数量级时，原方案中的数据结构、缓存策略与任务调度是否仍然成立？通常需要引入分层与异步。

第二，团队：多人协作时，模块边界、接口契约与代码所有权必须明确；案例中的实现应拆分为可独立测试的单元，并配合文档说明设计意图。

第三，演进：上线后的需求变化不可避免；方案设计时应预留扩展点（配置化、插件化、事件化），并定期用真实指标验证假设。


案例研究的学习方法：先独立阅读需求，尝试在脑中形成方案，再对照实现与讲解，最后思考“如果约束变化（数据量、并发、团队规模），方案应如何调整”。

## 10. 知识要点总结与深入讲解

本节以讲解形式汇总全文要点，替代传统的习题与自测，读者不需要答题，只需跟随解释建立完整的认知框架。

关于《CI/CD 流水线》的核心结论：

DevOps 的本质是自动化与协作，工具只是载体。
可重复、可回滚、可观测是三条主线。
从 DORA 指标开始度量改进，避免为工具而工具。

原文档各小节的要点回顾：

- 1. CI/CD 原理：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 2. GitHub Actions：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 3. GitLab CI：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 4. Jenkins：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 5. ArgoCD：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 6. 发布策略：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 7. 制品管理：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 8. 流水线设计原则：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 9. 小结：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- GitLab CI/CD：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- GitHub Actions：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- Jenkins Pipeline：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 通用工具命令：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- Helm 部署：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 制品仓库管理：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 通知与集成：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 安全扫描：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 缓存与优化：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。
- 排查与调试：该小节围绕CI/CD 流水线展开具体细节，阅读时应关注其与核心结论的对应关系；每个小节都是核心结论在某一个侧面的展开。

把以上要点与第 3-9 节的内容对照复习，即可完成对本文主题的闭环学习。

## 11. 参考文献


GitHub Actions 文档：https://docs.github.com/zh/actions
GitLab CI 文档：https://docs.gitlab.com/ci/
Argo CD：https://argo-cd.readthedocs.io/
DORA 研究：https://dora.dev/
DevOps 手册（Gene Kim 等）：https://itrevolution.com/devops-handbook/

## 12. 延伸阅读


Docker 与 Kubernetes 深入，见 031-devops 模块文档。
CI/CD 管线设计，见 031-devops 模块 CICD 文档。
云原生架构，见 034-cloud-computing 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 DevOps 课程。

## 14. 模块知识图谱与学习路径

本文属于 DevOps 模块。为了把《CI/CD 流水线》放入完整的知识网络，下面列出本模块的全部主题并给出相互关联的导读。学习时建议按模块内顺序推进，并在每个文档中留意交叉引用。

```mermaid
flowchart LR
    A["CI/CD 流水线"]
    N0["概述与 Linux 基础"]
    N1["网络与安全"]
    N0 --> N1
    N2["容器与 Docker"]
    N1 --> N2
    N3["Kubernetes"]
    N2 --> N3
    N4["CI/CD 流水线"]
    N3 --> N4
    N5["监控与可观测性"]
    N4 --> N5
    N6["基础设施即代码"]
    N5 --> N6
    N7["云原生与 SRE"]
    N6 --> N7
    N8["Shell脚本编程"]
    N7 --> N8
    N9["包管理与仓库"]
    N8 --> N9
    N10["服务网格"]
    N9 --> N10
    N11["日志管理"]
    N10 --> N11
    N12["配置管理"]
    N11 --> N12
    N13["性能调优"]
    N12 --> N13
```

上图为模块主题的推荐学习顺序示意图（仅展示前若干主题）。各主题之间存在三类关联：

第一，前置依赖关系：早期主题是后期主题的基础，例如环境与语法先行、进阶主题随后；

第二，横向并列关系：同一层级主题从不同角度覆盖模块能力，学习顺序可以按兴趣调整；

第三，工程组合关系：多个主题在真实项目中组合使用，例如配置、性能与安全主题往往出现在同一系统的不同层面。

### 14.1 模块主题速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 概述与 Linux 基础 | 001-OverviewLinuxBasics | 本文的前置基础 |
| 网络与安全 | 002-NetworkSecurity | 本文的安全延伸 |
| 容器与 Docker | 003-ContainerDocker | 本文的并列主题 |
| Kubernetes | 004-Kubernetes | 本文的并列主题 |
| CI/CD 流水线 | 005-CICDPipeline | 本文自身 |
| 监控与可观测性 | 006-MonitorAndObservability | 本文的并列主题 |
| 基础设施即代码 | 007-IaC | 本文的前置基础 |
| 云原生与 SRE | 008-CloudNativeSRE | 本文的并列主题 |
| Shell脚本编程 | 009-ShellScriptProgramming | 本文的并列主题 |
| 包管理与仓库 | 010-PackageManagementRepository | 本文的并列主题 |
| 服务网格 | 011-ServiceMesh | 本文的并列主题 |
| 日志管理 | 012-LogManagement | 本文的并列主题 |
| 配置管理 | 013-ConfigManagement | 本文的并列主题 |
| 性能调优 | 014-PerformanceTuning | 本文的性能延伸 |
| 高可用架构 | 015-HighAvailabilityArchitecture | 本文的原理深化 |
| 自动化测试 | 016-AutomationTest | 本文的并列主题 |
| 故障排查 | 017-Troubleshooting | 本文的并列主题 |
| 容器安全 | 018-ContainerSecurity | 本文的安全延伸 |
| GitOps与持续交付 | 019-GitOpsCD | 本文的并列主题 |
| 监控与告警 | 020-MonitorAndAlert | 本文的并列主题 |
| 网络与安全进阶 | 021-NetworkSecurityAdvanced | 本文的安全延伸 |
| 数据库运维 | 022-DatabaseOps | 本文的并列主题 |
| Dockerfile多阶段构建 | 023-DockerfileMultiBuild | 本文的并列主题 |
| Kubernetes核心资源详解 | 024-KubernetesCoreDetailed | 本文的并列主题 |
| Helm-Chart应用打包 | 025-HelmChartApplicationPackage | 本文的并列主题 |
| Terraform资源编排 | 026-Terraform | 本文的并列主题 |
| Ansible-Playbook配置管理 | 027-AnsiblePlaybookConfigManagement | 本文的并列主题 |
| Prometheus指标采集与告警 | 028-Prometheus | 本文的并列主题 |
| Grafana仪表盘配置 | 029-GrafanaTableConfig | 本文的并列主题 |
| ELK-Stack日志分析 | 030-ELKStackLogAnalysis | 本文的并列主题 |
| OpenTelemetry | 031-OpenTelemetry | 本文的并列主题 |
| GitOps与ArgoCD | 032-GitOpsArgoCD | 本文的并列主题 |
| DevOps kubectl 基础命令 | 033-KubectlBasics | 本文的前置基础 |
| DevOps Helm 包管理命令 | 034-HelmCommands | 本文的并列主题 |
| DevOps Jenkins Pipeline | 035-JenkinsPipeline | 本文的并列主题 |
| DevOps GitLab CI/CD | 036-GitLabCI | 本文的并列主题 |

速查表的作用是让读者快速判断：哪些文档应在阅读本文前掌握（前置基础），哪些文档应在阅读本文后继续（延伸主题）。本模块的交叉引用体系即以此表为基础。

## 15. 术语表

下表整理《CI/CD 流水线》及 DevOps 模块中出现的高频术语，给出简明释义。术语按字母序或逻辑序排列，供查阅。

| 术语 | 释义 |
| --- | --- |
| CI/CD 管线 | 代码提交 -> 构建 -> 测试 -> 制品 -> 部署；流水线即代码（GitHub Actions/Jenkins/GitLab CI）。 |
| 容器与镜像 | OCI 规范、Dockerfile 分层、镜像仓库与签名；容器隔离（cgroup/namespace）。 |
| 编排 | Kubernetes 的 Pod/Deployment/Service 抽象；声明式期望状态与控制器调和。 |
| 可观测性三支柱 | 指标（Prometheus）、日志（Loki/ELK）、追踪（OpenTelemetry）。 |
| 环境漂移（易错点） | 参见常见陷阱章节的详细讲解 |
| 秘密硬编码（易错点） | 参见常见陷阱章节的详细讲解 |
| 构建不可复现（易错点） | 参见常见陷阱章节的详细讲解 |
| 测试后置（易错点） | 参见常见陷阱章节的详细讲解 |
| 回滚缺失（易错点） | 参见常见陷阱章节的详细讲解 |
| 监控盲区（易错点） | 参见常见陷阱章节的详细讲解 |

术语表与正文配合使用：先通读正文，遇到模糊术语回查本表；长期使用后术语会自然进入工作记忆。
