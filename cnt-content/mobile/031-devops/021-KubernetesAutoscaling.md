# Kubernetes 自动扩缩容速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## HPA 水平 Pod 自动扩缩容

**基本用法:查看 HPA**
`kubectl get hpa [-n <命名空间>]`

```bash
# 列出当前命名空间所有 HPA
kubectl get hpa

# 查看 HPA 详情(含当前指标与目标指标)
kubectl describe hpa web-hpa -n production

# 监视 HPA 扩缩容状态
kubectl get hpa -w -n production
```

---

**基本用法:基于 CPU 创建 HPA**
`kubectl autoscale deployment <名称> --cpu-percent=<百分比> --min=<最小> --max=<最大>`

```bash
# 创建基于 CPU 利用率的 HPA
kubectl autoscale deployment web --cpu-percent=70 --min=2 --max=10 -n production

# 查看创建结果
kubectl get hpa web -n production
```

---

**基本用法:基于多指标创建 HPA(自定义指标)**
`kubectl apply -f <hpa.yaml>`

```yaml
# hpa.yaml 多指标与自定义指标扩缩容
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web-hpa
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web
  minReplicas: 2
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  - type: Pods
    pods:
      metric:
        name: http_requests_per_second
      target:
        type: AverageValue
        averageValue: "1000"
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 50
        periodSeconds: 60
```

---

**基本用法:扩缩容行为配置**
`spec.behavior`

```yaml
# 平滑扩缩容行为
behavior:
  scaleUp:
    stabilizationWindowSeconds: 0
    policies:
    - type: Percent
      value: 100
      periodSeconds: 15
    - type: Pods
      value: 4
      periodSeconds: 15
    selectPolicy: Max
  scaleDown:
    stabilizationWindowSeconds: 300
    policies:
    - type: Percent
      value: 10
      periodSeconds: 60
    selectPolicy: Min
```

---

**基本用法:删除 HPA**
`kubectl delete hpa <名称>`

```bash
# 删除 HPA(不影响当前副本数)
kubectl delete hpa web-hpa -n production

# 删除前查看
kubectl get hpa -n production
```

---

## VPA 垂直 Pod 自动扩缩容

**基本用法:查看 VPA**
`kubectl get vpa [-n <命名空间>]`

```bash
# 列出所有 VPA
kubectl get vpa -n production

# 查看 VPA 推荐值
kubectl describe vpa web-vpa -n production

# 查看 VPA 推荐的 CPU/内存值
kubectl get vpa web-vpa -n production -o jsonpath='{.status.recommendation.containerRecommendations}'
```

---

**基本用法:创建 VPA**
`kubectl apply -f <vpa.yaml>`

```yaml
# vpa.yaml 垂直扩缩容示例
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: web-vpa
  namespace: production
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: web
  updatePolicy:
    updateMode: Auto
  resourcePolicy:
    containerPolicies:
    - containerName: '*'
      minAllowed:
        cpu: 100m
        memory: 128Mi
      maxAllowed:
        cpu: 2
        memory: 2Gi
      controlledResources: ["cpu", "memory"]
```

---

**基本用法:VPA 模式**
`spec.updatePolicy.updateMode`

```bash
# Auto:自动应用推荐值(会重启 Pod)
# Recomender:仅生成推荐值,不修改 Pod(默认)
# Off:仅收集指标,不生成推荐
# Initial:仅在 Pod 创建时应用推荐值

# 设置为仅推荐模式(用于观察)
kubectl patch vpa web-vpa -n production -p '{"spec":{"updatePolicy":{"updateMode":"RecommenderOnly"}}}'
```

---

## Cluster Autoscaler 集群自动扩缩容

**基本用法:查看 Cluster Autoscaler 状态**
`kubectl get pods -n kube-system | grep cluster-autoscaler`

```bash
# 检查 Cluster Autoscaler 是否运行
kubectl get pods -n kube-system | grep cluster-autoscaler

# 查看 CA 日志
kubectl logs -n kube-system -l app=cluster-autoscaler --tail=50

# 查看 CA 配置
kubectl get deployment cluster-autoscaler -n kube-system -o yaml
```

---

**基本用法:节点自动扩缩容**
`kubectl get nodes`

```bash
# 查看当前节点数
kubectl get nodes

# 查看节点资源使用率
kubectl top nodes

# 查看 Pending 的 Pod(触发扩容)
kubectl get pods -A --field-selector=status.phase=Pending

# 检查 Pod 处于 Pending 的原因
kubectl describe pod <pending-pod-name> | grep -A 10 Events
```

---

**基本用法:节点池与标签管理**
`kubectl label node <节点> <键>=<值>`

```bash
# 给节点打标签(用于节点池识别)
kubectl label node node-1 node-pool=spot

# 查看节点池分布
kubectl get nodes -L node-pool

# 给节点添加污点(防止 Pod 调度)
kubectl taint nodes node-1 dedicated=special:NoSchedule
```

---

## 指标服务器

**基本用法:查看资源指标**
`kubectl top <资源> [名称]`

```bash
# 查看节点资源使用
kubectl top nodes

# 查看 Pod 资源使用
kubectl top pods -n production

# 按 CPU 排序
kubectl top pods -n production --sort-by=CPU

# 查看指定 Pod 各容器资源
kubectl top pod web-xxx -n production --containers
```

---

**基本用法:检查 metrics-server 状态**
`kubectl get deployment metrics-server -n kube-system`

```bash
# 查看 metrics-server 是否就绪
kubectl get deployment metrics-server -n kube-system

# 查看 metrics-server Pod
kubectl get pods -n kube-system -l k8s-app=metrics-server

# 查看 metrics-server 日志
kubectl logs -n kube-system -l k8s-app=metrics-server --tail=20
```

---

## 自定义指标与 Prometheus Adapter

**基本用法:查看自定义指标**
`kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1"`

```bash
# 列出所有可用自定义指标
kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1"

# 查看 Pod 级自定义指标
kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1/namespaces/production/pods/*/http_requests_per_second"

# 查看命名空间级指标
kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1/namespaces/production/metrics/qps"
```

---

**基本用法:Prometheus Adapter 配置**
`kubectl edit configmap prometheus-adapter -n monitoring`

```yaml
# adapter-config.yaml 自定义指标规则示例
rules:
- seriesQuery: 'http_requests_total{namespace!="",pod!=""}'
  resources:
    overrides:
      namespace: {resource: "namespace"}
      pod: {resource: "pod"}
  name:
    matches: "^(.*)_total"
    as: "${1}_per_second"
  metricsQuery: 'sum(rate(<<.Series>>{<<.LabelMatchers>>}[2m])) by (<<.GroupBy>>)'
```

---

## KEDA 事件驱动扩缩容

**基本用法:查看 ScaledObject**
`kubectl get scaledobjects [-n <命名空间>]`

```bash
# 列出所有 ScaledObject
kubectl get so -n production

# 查看 ScaledObject 详情
kubectl describe so kafka-consumer-so -n production

# 查看 ScaledJob
kubectl get scaledjobs -n production
```

---

**基本用法:创建 KEDA ScaledObject**
`kubectl apply -f <scaledobject.yaml>`

```yaml
# scaledobject.yaml 基于 Kafka 消息扩缩容
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: kafka-consumer
  namespace: production
spec:
  scaleTargetRef:
    name: kafka-consumer
  minReplicaCount: 0
  maxReplicaCount: 30
  pollingInterval: 30
  cooldownPeriod: 300
  triggers:
  - type: kafka
    metadata:
      bootstrapServers: kafka-broker:9092
      consumerGroup: my-group
      topic: events
      lagThreshold: "100"
      offsetResetPolicy: latest
```

---

**基本用法:基于 Cron 的扩缩容**
`triggers: - type: cron`

```yaml
# 工作时间扩容,非工作时间缩容
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: cron-scaled
  namespace: production
spec:
  scaleTargetRef:
    name: web
  minReplicaCount: 1
  maxReplicaCount: 10
  triggers:
  - type: cron
    metadata:
      timezone: Asia/Shanghai
      start: "0 9 * * 1-5"
      end: "0 18 * * 1-5"
      desiredReplicas: "10"
```

---

## 扩缩容排查

**基本用法:查看 HPA 状态**
`kubectl describe hpa <名称>`

```bash
# 查看 HPA 当前状态和事件
kubectl describe hpa web-hpa -n production

# 查看 HPA 状态字段
kubectl get hpa web-hpa -n production -o jsonpath='{.status}'

# 检查 HPA 是否能获取指标
kubectl describe hpa web-hpa -n production | grep -A 5 "Conditions:"
```

---

**基本用法:常见 HPA 问题排查**
`kubectl get --raw "/apis/metrics.k8s.io/v1beta1"`

```bash
# 检查 metrics-server 是否提供指标
kubectl get --raw "/apis/metrics.k8s.io/v1beta1/namespaces/production/pods/web-xxx"

# 检查 Pod 是否设置了资源请求(HPA 必需)
kubectl get pod web-xxx -n production -o jsonpath='{.spec.containers[*].resources.requests}'

# 查看 HPA 无法获取指标的常见原因
kubectl describe hpa web-hpa -n production | grep -A 10 Events
```

---

**基本用法:节点扩容失败排查**
`kubectl describe node <节点>`

```bash
# 查看节点资源分配情况
kubectl describe node node-1 | grep -A 10 "Allocated resources"

# 查看 Pending Pod 详细原因
kubectl get pod pending-pod -o yaml | grep -A 20 "conditions:"

# 查看 Cluster Autoscaler 扩容决策
kubectl logs -n kube-system -l app=cluster-autoscaler --tail=100 | grep -E "scaleUp|scaleDown"
```
