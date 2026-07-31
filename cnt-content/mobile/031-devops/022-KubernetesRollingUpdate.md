# Kubernetes 滚动更新与回滚速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Deployment 滚动更新

**基本用法:触发滚动更新**
`kubectl set image deployment/<名称> <容器>=<镜像>`

```bash
# 更新 Deployment 镜像
kubectl set image deployment/web web=nginx:1.25 -n production

# 更新多个容器
kubectl set image deployment/app app=app:v2 sidecar=busybox:1.36 -n production

# 通过 apply 应用 YAML 变更
kubectl apply -f deployment-v2.yaml -n production
```

---

**基本用法:查看滚动更新状态**
`kubectl rollout status deployment/<名称>`

```bash
# 查看 Deployment 滚动状态
kubectl rollout status deployment/web -n production

# 监视滚动更新直到完成
kubectl rollout status deployment/web -n production --watch

# 查看 ReplicaSet 历史
kubectl get rs -n production
```

---

**基本用法:配置滚动更新策略**
`spec.strategy.type: RollingUpdate`

```yaml
# deployment.yaml 滚动更新策略配置
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 10
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 25%
      maxSurge: 25%
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
        image: nginx:1.25
```

---

**基本用法:暂停与恢复滚动更新**
`kubectl rollout pause|resume deployment/<名称>`

```bash
# 暂停滚动更新(用于多次修改后一次性更新)
kubectl rollout pause deployment/web -n production

# 暂停期间可多次修改
kubectl set image deployment/web web=nginx:1.26 -n production
kubectl set resources deployment/web -c web --limits=cpu=1,memory=1Gi -n production

# 恢复滚动更新
kubectl rollout resume deployment/web -n production
```

---

## 回滚操作

**基本用法:查看发布历史**
`kubectl rollout history deployment/<名称>`

```bash
# 查看 Deployment 修订历史
kubectl rollout history deployment/web -n production

# 查看指定版本的详情
kubectl rollout history deployment/web -n production --revision=3

# 查看历史 ReplicaSet
kubectl get rs -n production -l app=web
```

---

**基本用法:回滚到上一版本**
`kubectl rollout undo deployment/<名称>`

```bash
# 回滚到上一版本
kubectl rollout undo deployment/web -n production

# 查看回滚状态
kubectl rollout status deployment/web -n production
```

---

**基本用法:回滚到指定版本**
`kubectl rollout undo deployment/<名称> --to-revision=<版本号>`

```bash
# 回滚到指定版本
kubectl rollout undo deployment/web --to-revision=3 -n production

# 查看回滚后状态
kubectl rollout status deployment/web -n production

# 确认当前运行的版本
kubectl get deployment web -n production -o jsonpath='{.metadata.annotations.deployment\.kubernetes\.io/revision}'
```

---

**基本用法:配置历史版本数量**
`spec.revisionHistoryLimit`

```yaml
# deployment.yaml 保留历史版本数量
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 5
  revisionHistoryLimit: 10
  strategy:
    type: RollingUpdate
  selector:
    matchLabels:
      app: web
  template:
    spec:
      containers:
      - name: web
        image: nginx:1.25
```

---

## StatefulSet 滚动更新

**基本用法:查看 StatefulSet 滚动状态**
`kubectl rollout status statefulset/<名称>`

```bash
# 查看 StatefulSet 滚动状态
kubectl rollout status statefulset/mysql -n production

# 查看 StatefulSet 各 Pod 状态
kubectl get pods -l app=mysql -n production -w

# 查看 StatefulSet 当前版本
kubectl get statefulset mysql -n production -o jsonpath='{.status.currentRevision}'
```

---

**基本用法:配置 StatefulSet 更新策略**
`spec.updateStrategy.type`

```yaml
# statefulset.yaml 滚动更新策略
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
spec:
  serviceName: mysql
  replicas: 5
  podManagementPolicy: OrderedReady
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      partition: 2
      maxUnavailable: 1
  selector:
    matchLabels:
      app: mysql
  template:
    spec:
      containers:
      - name: mysql
        image: mysql:8.0
```

---

**基本用法:灰度更新(partition)**
`spec.updateStrategy.rollingUpdate.partition`

```bash
# 设置 partition=4,仅更新序号 >= 4 的 Pod(即只更新 mysql-4)
kubectl patch statefulset mysql -n production -p '{"spec":{"updateStrategy":{"rollingUpdate":{"partition":4}}}}'

# 触发更新
kubectl set image statefulset/mysql mysql=mysql:8.1 -n production

# 验证仅最后一个 Pod 被更新
kubectl get pods -l app=mysql -n production -o custom-columns=NAME:.metadata.name,IMAGE:.spec.containers[0].image

# 全量更新(移除 partition)
kubectl patch statefulset mysql -n production -p '{"spec":{"updateStrategy":{"rollingUpdate":{"partition":0}}}}'
```

---

## DaemonSet 滚动更新

**基本用法:查看 DaemonSet 滚动状态**
`kubectl rollout status daemonset/<名称>`

```bash
# 查看 DaemonSet 滚动状态
kubectl rollout status daemonset/log-agent -n kube-system

# 查看更新情况
kubectl get daemonset log-agent -n kube-system

# 查看节点上 Pod 的分布
kubectl get pods -l app=log-agent -n kube-system -o wide
```

---

**基本用法:配置 DaemonSet 更新策略**
`spec.updateStrategy`

```yaml
# daemonset.yaml DaemonSet 更新策略
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: log-agent
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: log-agent
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 10%
      maxSurge: 0
  template:
    metadata:
      labels:
        app: log-agent
    spec:
      containers:
      - name: agent
        image: fluentd:1.16
```

---

## 健康检查与就绪探针

**基本用法:配置就绪探针**
`spec.containers.readinessProbe`

```yaml
# 就绪探针配置(决定 Pod 是否接收流量)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 3
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
        image: nginx:1.25
        readinessProbe:
          httpGet:
            path: /healthz
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 10
          failureThreshold: 3
```

---

**基本用法:配置存活探针**
`spec.containers.livenessProbe`

```yaml
# 存活探针(失败会重启容器)
livenessProbe:
  httpGet:
    path: /healthz
    port: 80
  initialDelaySeconds: 30
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 3

# 启动探针(应用启动慢时使用,避免被存活探针误杀)
startupProbe:
  httpGet:
    path: /healthz
    port: 80
  failureThreshold: 30
  periodSeconds: 10
```

---

**基本用法:查看探针状态**
`kubectl describe pod <名称>`

```bash
# 查看探针状态与事件
kubectl describe pod web-xxx -n production | grep -A 10 "Liveness\|Readiness\|Startup"

# 查看 Pod 重启次数(存活探针失败导致)
kubectl get pod web-xxx -n production -o jsonpath='{.status.containerStatuses[0].restartCount}'

# 查看 Pod 生命周期事件
kubectl get events -n production --field-selector involvedObject.name=web-xxx
```

---

## 更新策略对比

**基本用法:Recreate vs RollingUpdate**
`spec.strategy.type`

```yaml
# Recreate:先删所有旧 Pod,再创建新 Pod(有停机时间)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 3
  strategy:
    type: Recreate
  selector:
    matchLabels:
      app: web
  template:
    spec:
      containers:
      - name: web
        image: nginx:1.25

# RollingUpdate:滚动更新(默认,无停机时间)
# 适合大多数场景,配合就绪探针使用
```

---

**基本用法:maxUnavailable 与 maxSurge**
`spec.strategy.rollingUpdate`

```bash
# maxUnavailable:更新期间允许不可用的最大 Pod 数(可为整数或百分比)
# maxSurge:更新期间允许超出期望副本数的最大 Pod 数

# 严格不减少可用 Pod(适合关键服务)
# maxUnavailable: 0, maxSurge: 25%
kubectl patch deployment web -n production -p '{"spec":{"strategy":{"rollingUpdate":{"maxUnavailable":0,"maxSurge":"25%"}}}}'

# 快速更新但允许部分不可用(适合非关键服务)
# maxUnavailable: 50%, maxSurge: 0
kubectl patch deployment web -n production -p '{"spec":{"strategy":{"rollingUpdate":{"maxUnavailable":"50%","maxSurge":0}}}}'
```

---

## 更新监控与排查

**基本用法:监视更新过程**
`kubectl get pods -l app=<标签> -w`

```bash
# 实时监视 Pod 创建与销毁
kubectl get pods -l app=web -n production -w

# 查看 ReplicaSet 变化
kubectl get rs -l app=web -n production -w

# 查看事件流
kubectl get events -n production --sort-by='.lastTimestamp' -w
```

---

**基本用法:排查更新失败**
`kubectl get deployment <名称>`

```bash
# 查看 Deployment 状态
kubectl get deployment web -n production

# 查看更新进度
kubectl rollout status deployment/web -n production

# 查看 Pod 失败原因(常见:镜像拉取失败、探针失败、资源不足)
kubectl describe pod web-xxx -n production | grep -A 20 "Events:"
```

---

**基本用法:回滚卡住的更新**
`kubectl rollout undo deployment/<名称>`

```bash
# 滚动更新卡住时立即回滚
kubectl rollout undo deployment/web -n production

# 强制删除卡住的新 Pod
kubectl delete pod web-xxx -n production --force

# 检查资源配额是否限制更新
kubectl describe resourcequota -n production
```

---

## 蓝绿部署与金丝雀

**基本用法:蓝绿部署**
`kubectl apply -f <green-deployment.yaml>`

```bash
# 部署绿色版本(新版本)
kubectl apply -f web-green.yaml -n production

# 切换 Service 到绿色版本
kubectl patch svc web -n production -p '{"spec":{"selector":{"version":"green"}}}'

# 确认无误后删除蓝色版本
kubectl delete deployment web-blue -n production
```

---

**基本用法:金丝雀发布(基于标签)**
`kubectl apply -f <canary-deployment.yaml>`

```yaml
# canary.yaml 金丝雀 Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-canary
  namespace: production
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web
      track: canary
  template:
    metadata:
      labels:
        app: web
        track: canary
    spec:
      containers:
      - name: web
        image: nginx:canary
```

---

**基本用法:基于权重的金丝雀(Istio)**
`kubectl apply -f <virtualservice.yaml>`

```yaml
# virtualservice.yaml Istio 流量分割
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: web
  namespace: production
spec:
  hosts:
  - web.example.com
  http:
  - route:
    - destination:
        host: web
        subset: stable
      weight: 90
    - destination:
        host: web
        subset: canary
      weight: 10
```
