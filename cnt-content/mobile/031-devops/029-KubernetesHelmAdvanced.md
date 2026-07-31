# Helm 高级命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Chart 仓库管理

**基本用法:添加仓库**
`helm repo add <名称> <URL>`

```bash
# 添加官方稳定仓库
helm repo add stable https://charts.helm.sh/stable

# 添加 Bitnami 仓库
helm repo add bitnami https://charts.bitnami.com/bitnami

# 添加私有仓库(带认证)
helm repo add private-repo https://charts.example.com \
  --username admin --password secret

# 添加 OCI 仓库
helm repo add oci-repo oci://registry.example.com/charts
```

---

**基本用法:管理仓库**
`helm repo list|update|remove`

```bash
# 列出已配置的仓库
helm repo list

# 更新所有仓库索引
helm repo update

# 更新单个仓库
helm repo update bitnami

# 删除仓库
helm repo remove stable

# 从仓库搜索 Chart
helm search repo nginx
helm search repo bitnami/mysql --versions
```

---

**基本用法:OCI 仓库操作**
`helm push|pull`

```bash
# 登录 OCI 仓库
helm registry login registry.example.com -u admin -p secret

# 推送 Chart 到 OCI 仓库
helm push mychart-0.1.0.tgz oci://registry.example.com/charts

# 从 OCI 仓库拉取
helm pull oci://registry.example.com/charts/mychart --version 0.1.0

# 从 OCI 仓库直接安装
helm install myapp oci://registry.example.com/charts/mysql --version 9.0.0

# 登出 OCI 仓库
helm registry logout registry.example.com
```

---

## Chart 依赖管理

**基本用法:添加依赖**
`Chart.yaml dependencies:`

```yaml
# Chart.yaml 依赖声明
apiVersion: v2
name: myapp
version: 1.0.0
dependencies:
- name: mysql
  version: "9.0.0"
  repository: "https://charts.bitnami.com/bitnami"
  condition: mysql.enabled
  importValues:
  - child: service
    parent: mysqlService

- name: redis
  version: "17.0.0"
  repository: "oci://registry.example.com/charts"
  alias: cache
  tags:
  - caching
```

---

**基本用法:管理依赖**
`helm dependency <update|build|list>`

```bash
# 构建依赖(下载到 charts/ 目录)
helm dependency build

# 更新依赖
helm dependency update

# 列出 Chart 依赖
helm dependency list

# 查看已下载的依赖
ls charts/

# 锁定依赖版本(生成 Chart.lock)
helm dependency update
cat Chart.lock
```

---

**基本用法:依赖条件与标签**
`condition: <键> / tags: [<标签>]`

```yaml
# values.yaml 依赖条件控制
mysql:
  enabled: true
  primary:
    persistence:
      size: 10Gi

# 启用部分依赖
helm install myapp ./myapp --set mysql.enabled=true

# 通过 tags 启用/禁用
helm install myapp ./myapp --tags caching=true
helm install myapp ./myapp --set tags.caching=false
```

---

## Chart 创建与开发

**基本用法:创建 Chart 骨架**
`helm create <名称>`

```bash
# 创建新 Chart
helm create mychart

# 查看目录结构
ls -R mychart/

# Chart 目录结构
# mychart/
# ├── Chart.yaml          Chart 元数据
# ├── values.yaml         默认值
# ├── charts/             依赖 Chart
# ├── templates/          模板文件
# │   ├── deployment.yaml
# │   ├── service.yaml
# │   ├── _helpers.tpl    辅助模板
# │   └── NOTES.txt       安装后提示
# └── .helmignore
```

---

**基本用法:Chart.yaml 元数据**
`Chart.yaml`

```yaml
# Chart.yaml 完整配置示例
apiVersion: v2
name: myapp
description: 我的 Web 应用 Chart
type: application
version: 1.0.0           # Chart 版本
appVersion: "2.5.0"      # 应用版本
home: https://example.com
sources:
- https://github.com/org/repo
maintainers:
- name: ops-team
  email: ops@example.com
keywords:
- web
- nginx
icon: https://example.com/icon.png
deprecated: false
```

---

**基本用法:模板编写**
`templates/*.yaml`

```yaml
# templates/deployment.yaml Deployment 模板示例
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "mychart.fullname" . }}
  labels:
    {{- include "mychart.labels" . | nindent 4 }}
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      {{- include "mychart.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      labels:
        {{- include "mychart.selectorLabels" . | nindent 8 }}
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
        imagePullPolicy: {{ .Values.image.pullPolicy }}
        ports:
        - containerPort: {{ .Values.service.port }}
        resources:
          {{- toYaml .Values.resources | nindent 10 }}
```

---

**基本用法:辅助模板**
`templates/_helpers.tpl`

```
{{/*
辅助模板:生成完整名称
*/}}
{{- define "mychart.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if contains $name .Release.Name -}}
{{- .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
{{- end -}}

{{/*
辅助模板:标准标签
*/}}
{{- define "mychart.labels" -}}
helm.sh/chart: {{ printf "%s-%s" .Chart.Name .Chart.Version }}
{{ include "mychart.selectorLabels" . }}
{{- if .Chart.AppVersion -}}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end -}}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}
```

---

## 模板函数与流程控制

**基本用法:常用函数**
`{{ <函数> <参数> }}`

```
# 字符串函数
{{ .Values.name | upper | quote }}
{{ .Values.url | replace "http://" "https://" }}
{{ trim .Values.path }}

# 默认值
{{ default "80" .Values.port }}

# 类型转换
{{ int .Values.replicas }}
{{ toString .Values.enabled }}

# 列表与字典
{{ range .Values.ports }}
- {{ . }}
{{ end }}

{{ range $key, $val := .Values.config }}
{{ $key }}: {{ $val }}
{{ end }}
```

---

**基本用法:条件判断**
`{{ if <条件> }} ... {{ end }}`

```
# 简单条件
{{- if .Values.ingress.enabled }}
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: {{ include "mychart.fullname" . }}
{{- end }}

# if-else
{{- if eq .Values.env "prod" }}
  replicas: 5
{{- else if eq .Values.env "staging" }}
  replicas: 2
{{- else }}
  replicas: 1
{{- end }}

# with 限定作用域
{{- with .Values.ingress }}
  host: {{ .hostname }}
  tls: {{ .tls }}
{{- end }}
```

---

**基本用法:循环**
`{{ range <列表> }} ... {{ end }}`

```
# 遍历列表
{{- range .Values.servers }}
- name: {{ .name }}
  host: {{ .host }}
{{- end }}

# 遍历字典
{{- range $key, $value := .Values.configMap }}
  {{ $key }}: {{ $value | quote }}
{{- end }}

# 带索引循环
{{- range $i, $port := .Values.ports }}
- containerPort: {{ $port }}
  name: port-{{ $i }}
{{- end }}

# until 生成数字序列
{{- range $i := until 5 }}
  replica-{{ $i }}
{{- end }}
```

---

## Chart 测试

**基本用法:编写测试**
`templates/tests/*.yaml`

```yaml
# templates/tests/test-connection.yaml 测试 Pod
apiVersion: v1
kind: Pod
metadata:
  name: "{{ include "mychart.fullname" . }}-test"
  annotations:
    "helm.sh/hook": test
    "helm.sh/hook-delete-policy": before-hook-creation,hook-succeeded
spec:
  restartPolicy: Never
  containers:
  - name: wget
    image: busybox
    command: ['sh', '-c']
    args:
    - |
      wget -qO- http://{{ include "mychart.fullname" . }}:{{ .Values.service.port }}/health | grep ok
```

---

**基本用法:运行测试**
`helm test <release>`

```bash
# 运行测试
helm test myapp

# 查看测试日志
helm test myapp --logs

# 指定超时
helm test myapp --timeout 5m

# 过滤运行特定测试
helm test myapp --filter 'test-connection'
```

---

**基本用法:Lint 检查**
`helm lint <chart>`

```bash
# 检查 Chart 模板
helm lint mychart/

# 严格模式(连 warning 也失败)
helm lint mychart/ --strict

# 检查时传值
helm lint mychart/ --set replicaCount=3

# 检查时使用 values 文件
helm lint mychart/ -f values-prod.yaml
```

---

## Chart 打包与发布

**基本用法:打包 Chart**
`helm package <chart>`

```bash
# 打包 Chart 为 tgz
helm package mychart/

# 指定输出目录
helm package mychart/ -d ./dist

# 打包时更新版本号
helm package mychart/ --version 1.2.0 --app-version 2.0.0

# 签名 Chart
helm package mychart/ --sign --key admin@example.com --keyring ~/.gnupg/pubring.gpg
```

---

**基本用法:生成仓库索引**
`helm repo index <目录>`

```bash
# 为目录生成 index.yaml
helm repo index ./dist/

# 合并到已有索引
helm repo index ./dist/ --url https://charts.example.com --merge ./dist/index.yaml

# 验证索引
cat ./dist/index.yaml | head -20

# 启动本地 HTTP 仓库测试
cd ./dist && python -m http.server 8080
```

---

**基本用法:验证 Chart**
`helm verify <chart.tgz>`

```bash
# 验证签名
helm verify mychart-1.0.0.tgz

# 验证 prov 文件
helm verify mychart-1.0.0.tgz --keyring ~/.gnupg/pubring.gpg

# 拉取并验证
helm pull --verify https://charts.example.com/mychart-1.0.0.tgz
```

---

## Release 管理

**基本用法:查看 Release**
`helm list|history|get`

```bash
# 列出所有 Release
helm list -A

# 列出所有命名空间
helm list --all-namespaces

# 包含已卸载的 Release
helm list -A --all

# 查看 Release 历史
helm history myapp

# 查看 Release 配置
helm get values myapp
helm get manifest myapp
helm get notes myapp
```

---

**基本用法:升级与回滚**
`helm upgrade|rollback`

```bash
# 升级 Release
helm upgrade myapp ./mychart -f values-prod.yaml

# 升级并安装(如果不存在)
helm upgrade --install myapp ./mychart -f values-prod.yaml

# 升级时重置值为默认
helm upgrade myapp ./mychart --reset-values

# 升级时强制更新资源
helm upgrade myapp ./mychart --force

# 回滚到指定版本
helm rollback myapp 2

# 查看回滚状态
helm history myapp
```

---

**基本用法:卸载 Release**
`helm uninstall <release>`

```bash
# 卸载 Release
helm uninstall myapp -n production

# 保留历史(可用于回滚)
helm uninstall myapp -n production --keep-history

# 卸载时等待资源删除
helm uninstall myapp -n production --wait

# 卸载指定超时
helm uninstall myapp -n production --timeout 5m
```

---

## 高级特性

**基本用法:Hook 钩子**
`annotations: "helm.sh/hook": <阶段>`

```yaml
# templates/pre-install-job.yaml 安装前钩子
apiVersion: batch/v1
kind: Job
metadata:
  name: "{{ include "mychart.fullname" . }}-init"
  annotations:
    "helm.sh/hook": pre-install
    "helm.sh/hook-weight": "-5"
    "helm.sh/hook-delete-policy": hook-succeeded,before-hook-creation
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: init
        image: busybox
        command: ["sh", "-c", "echo '初始化数据库...'"]
```

```bash
# 常用 Hook 类型
# pre-install / post-install
# pre-upgrade / post-upgrade
# pre-rollback / post-rollback
# pre-delete / post-delete
# test
```

---

**基本用法:子 Chart**
`charts/<子chart>`

```bash
# 在父 Chart 中引用子 Chart
mkdir -p mychart/charts
cd mychart/charts
helm create frontend
helm create backend

# 父 values.yaml 覆盖子 Chart 值
cat >> ../values.yaml <<EOF
frontend:
  replicaCount: 3
  image:
    repository: nginx
    tag: latest

backend:
  replicaCount: 2
  image:
    repository: myapp
    tag: v1.0
EOF
```

---

**基本用法:全局值**
`global:`

```yaml
# values.yaml 全局变量
global:
  imageRegistry: registry.example.com
  imagePullSecrets:
  - name: regcred
  storageClass: fast-ssd

# 子 Chart 中使用
# {{ .Values.global.imageRegistry }}
# {{ .Values.global.storageClass }}

# 安装时覆盖
helm install myapp ./mychart --set global.imageRegistry=docker.io
```

---

## 调试与排查

**基本用法:渲染模板**
`helm template <chart>`

```bash
# 渲染模板输出(不安装)
helm template mychart/

# 指定 Release 名称
helm template myapp ./mychart

# 指定命名空间
helm template myapp ./mychart --namespace production

# 渲染特定模板
helm template myapp ./mychart --show-only templates/deployment.yaml

# 渲染并传值
helm template myapp ./mychart --set replicaCount=5 -f values-prod.yaml
```

---

**基本用法:调试模式**
`helm install --debug --dry-run`

```bash
# 干运行(不实际安装)
helm install myapp ./mychart --dry-run

# 详细调试输出
helm install myapp ./mychart --dry-run --debug

# 渲染模板并校验
helm install myapp ./mychart --dry-run --debug | kubectl apply --dry-run=client -f -

# 执行前用 lint 检查
helm lint ./mychart && helm template myapp ./mychart | head -50
```

---

**基本用法:查看生成资源**
`helm get manifest`

```bash
# 查看当前 Release 部署的资源
helm get manifest myapp -n production

# 查看所有版本
helm history myapp -n production

# 查看指定版本的 manifest
helm get manifest myapp --revision 3 -n production

# 查看值文件
helm get values myapp -n production
helm get values myapp -n production --revision 2

# 查看 Release 状态
helm status myapp -n production
```

---

**基本用法:查看插件**
`helm plugin list|install`

```bash
# 列出已安装插件
helm plugin list

# 安装插件
helm plugin install https://github.com/jkroepke/helm-secrets

# 安装 helm-diff(查看差异)
helm plugin install https://github.com/databus23/helm-diff

# 查看升级前后差异
helm diff upgrade myapp ./mychart -f values-prod.yaml

# 卸载插件
helm plugin uninstall diff
```
