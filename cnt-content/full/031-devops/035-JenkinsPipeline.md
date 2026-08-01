---
order: 350
title: DevOps Jenkins Pipeline
module: 031-devops
category: '031-devops'
difficulty: beginner
description: DevOps Jenkins Pipeline 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# DevOps Jenkins Pipeline

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## pipeline 声明式流水线

**基本写法：定义声明式 pipeline**
```groovy
`pipeline {
    agent any
    stages {
        stage('<阶段名>') {
            steps {
                <步骤>
            }
        }
    }
}`
```
```groovy
// 基本声明式流水线
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'make build'
            }
        }
    }
}
```

---

## agent 代理配置

**基本写法：使用任意节点**
`agent any`
```groovy
// 在任意可用节点执行
pipeline {
    agent any
}
```

**基本写法：使用指定标签节点**
`agent { label '<标签>' }`
```groovy
// 在带 docker 标签的节点执行
pipeline {
    agent { label 'docker' }
}
```

**基本写法：使用 Docker 镜像**
`agent { docker { image '<镜像>' } }`
```groovy
// 在 maven 容器中执行
pipeline {
    agent { docker { image 'maven:3.8-openjdk-11' } }
}
```

**基本写法：不分配节点**
`agent none`
```groovy
// 不分配节点，由各 stage 指定
pipeline {
    agent none
    stages {
        stage('Build') {
            agent { label 'build' }
            steps { sh 'make build' }
        }
    }
}
```

---

## environment 环境变量

**基本写法：定义环境变量**
```groovy
`environment {
    <变量名> = '<值>'
}`
```
```groovy
// 定义构建环境变量
pipeline {
    agent any
    environment {
        VERSION = '1.0.0'
        BUILD_ENV = 'production'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building version ${VERSION}"
            }
        }
    }
}
```

**基本写法：使用 credentials**
```groovy
`environment {
    <变量> = credentials('<凭据ID>')
}`
```
```groovy
// 使用 Jenkins 存储的凭据
pipeline {
    agent any
    environment {
        DOCKER_PASSWORD = credentials('docker-hub-credentials')
    }
}
```

---

## stages 阶段定义

**基本写法：定义多个阶段**
```groovy
`stages {
    stage('<阶段1>') { steps { ... } }
    stage('<阶段2>') { steps { ... } }
}`
```
```groovy
// 完整的 CI/CD 阶段
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'npm install'
                sh 'npm run build'
            }
        }
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}
```

---

## steps 步骤

**基本写法：执行 shell 命令**
`sh '<命令>'`
```groovy
// 执行 shell 命令
steps {
    sh 'echo hello'
    sh 'make build'
}
```

**基本写法：执行脚本并获取结果**
`sh script: '<命令>', returnStdout: true`
```groovy
// 获取命令输出
steps {
    script {
        def version = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
        echo "Commit: ${version}"
    }
}
```

**基本写法：打印消息**
`echo '<消息>'`
```groovy
// 打印消息
steps {
    echo 'Starting build process'
}
```

---

## when 条件执行

**基本写法：分支条件**
```groovy
`when {
    branch '<分支名>'
}`
```
```groovy
// 只在 main 分支执行部署
stage('Deploy') {
    when {
        branch 'main'
    }
    steps {
        sh 'kubectl apply -f k8s/'
    }
}
```

**基本写法：表达式条件**
```groovy
`when {
    expression { <条件> }
}`
```
```groovy
// 满足条件时执行
stage('Deploy') {
    when {
        expression { env.BRANCH_NAME == 'main' && params.DEPLOY == true }
    }
    steps {
        sh 'deploy.sh'
    }
}
```

**基本写法：环境变量条件**
```groovy
`when {
    environment name: '<变量>', value: '<值>'
}`
```
```groovy
// 根据 DEPLOY_TO 变量执行
stage('Deploy Prod') {
    when {
        environment name: 'DEPLOY_TO', value: 'production'
    }
    steps {
        sh 'deploy-prod.sh'
    }
}
```

---

## post 构建后操作

**基本写法：成功后操作**
```groovy
`post {
    success { <步骤> }
}`
```
```groovy
// 构建成功后通知
pipeline {
    agent any
    stages { /* ... */ }
    post {
        success {
            echo 'Build succeeded!'
            sh 'curl -X POST https://hooks.slack.com/...'
        }
    }
}
```

**基本写法：失败后操作**
```groovy
`post {
    failure { <步骤> }
}`
```
```groovy
// 构建失败后通知
post {
    failure {
        echo 'Build failed!'
        emailext to: 'team@example.com', subject: 'Build Failed', body: 'Check logs'
    }
}
```

**基本写法：总是执行**
```groovy
`post {
    always { <步骤> }
}`
```
```groovy
// 无论成功失败都清理
post {
    always {
        sh 'docker system prune -f'
        cleanWs()
    }
}
```

---

## parameters 参数化构建

**基本写法：字符串参数**
```groovy
`parameters {
    string(name: '<名称>', defaultValue: '<默认值>', description: '<描述>')
}`
```
```groovy
// 定义字符串参数
pipeline {
    agent any
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: '构建分支')
    }
    stages {
        stage('Build') {
            steps {
                git branch: params.BRANCH, url: 'https://github.com/repo.git'
            }
        }
    }
}
```

**基本写法：布尔参数**
```groovy
`parameters {
    booleanParam(name: '<名称>', defaultValue: <布尔值>, description: '<描述>')
}`
```
```groovy
// 定义部署开关
parameters {
    booleanParam(name: 'DEPLOY', defaultValue: false, description: '是否部署')
}
```

**基本写法：选项参数**
```groovy
`parameters {
    choice(name: '<名称>', choices: ['<选项1>', '<选项2>'], description: '<描述>')
}`
```
```groovy
// 定义环境选择
parameters {
    choice(name: 'ENV', choices: ['dev', 'staging', 'prod'], description: '部署环境')
}
```

---

## script 脚本块

**基本写法：执行 Groovy 脚本**
```groovy
`script {
    <Groovy 代码>
}`
```
```groovy
// 在 pipeline 中执行 Groovy
steps {
    script {
        def servers = ['server1', 'server2', 'server3']
        for (server in servers) {
            sh "ssh ${server} 'deploy.sh'"
        }
    }
}
```

---

## 并行执行

**基本写法：并行阶段**
```groovy
`parallel {
    stage('<阶段1>') { steps { ... } }
    stage('<阶段2>') { steps { ... } }
}`
```
```groovy
// 并行执行测试
stage('Test') {
    parallel {
        stage('Unit Test') {
            steps {
                sh 'npm run test:unit'
            }
        }
        stage('Integration Test') {
            steps {
                sh 'npm run test:integration'
            }
        }
    }
}
```

---

## artifacts 归档

**基本写法：归档构建产物**
`archiveArtifacts '<路径>'`
```groovy
// 归档构建产物
steps {
    sh 'make build'
    archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
}
```

**基本写法：归档测试报告**
`junit '<报告路径>'`
```groovy
// 归档 JUnit 测试报告
steps {
    sh 'npm test'
    junit 'reports/**/*.xml'
}
```

---

## 触发器

**基本写法：定时触发**
```groovy
`triggers {
    cron('<Cron 表达式>')
}`
```
```groovy
// 每天凌晨 2 点构建
pipeline {
    agent any
    triggers {
        cron('H 2 * * *')
    }
    stages { /* ... */ }
}
```

**基本写法：上游触发**
```groovy
`triggers {
    upstream(upstreamProjects: '<项目>', threshold: hudson.model.Result.SUCCESS)
}`
```
```groovy
// 上游项目成功后触发
triggers {
    upstream(upstreamProjects: 'my-app-build', threshold: hudson.model.Result.SUCCESS)
}
```

## 参考文献



GitHub Actions 文档：https://docs.github.com/zh/actions
GitLab CI 文档：https://docs.gitlab.com/ci/
Argo CD：https://argo-cd.readthedocs.io/
DORA 研究：https://dora.dev/
DevOps 手册（Gene Kim 等）：https://itrevolution.com/devops-handbook/

## 延伸阅读



Docker 与 Kubernetes 深入，见 031-devops 模块文档。
CI/CD 管线设计，见 031-devops 模块 CICD 文档。
云原生架构，见 034-cloud-computing 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 DevOps 课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 概述与 Linux 基础 | 001-OverviewLinuxBasics | 本文的前置基础 |
| 网络与安全 | 002-NetworkSecurity | 本文的安全延伸 |
| 容器与 Docker | 003-ContainerDocker | 本文的并列主题 |
| Kubernetes | 004-Kubernetes | 本文的并列主题 |
| CI/CD 流水线 | 005-CICDPipeline | 本文的并列主题 |
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
| DevOps Jenkins Pipeline | 035-JenkinsPipeline | 本文自身 |
| DevOps GitLab CI/CD | 036-GitLabCI | 本文的并列主题 |
