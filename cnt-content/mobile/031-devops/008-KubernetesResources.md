# DevOps Kubernetes 资源 YAML

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Pod 资源定义

**基本写法：定义 Pod**
```yaml
`apiVersion: v1
kind: Pod
metadata:
  name: <名称>
spec:
  containers:
    - name: <容器名>
      image: <镜像>`
```
```yaml
# 定义 nginx Pod
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
    - name: nginx
      image: nginx:1.25
      ports:
        - containerPort: 80
```

**基本写法：多容器 Pod**
```yaml
`spec:
  containers:
    - name: <容器1>
      image: <镜像1>
    - name: <容器2>
      image: <镜像2>`
```
```yaml
# 定义多容器 Pod
apiVersion: v1
kind: Pod
metadata:
  name: app-with-sidecar
spec:
  containers:
    - name: app
      image: myapp:v1
    - name: log-sidecar
      image: busybox
      args: [/bin/sh, -c, "tail -f /log/app.log"]
```

---

## Deployment 资源定义

**基本写法：定义 Deployment**
```yaml
`apiVersion: apps/v1
kind: Deployment
metadata:
  name: <名称>
spec:
  replicas: <副本数>
  selector:
    matchLabels:
      app: <标签>
  template:
    metadata:
      labels:
        app: <标签>
    spec:
      containers:
        - name: <容器名>
          image: <镜像>`
```
```yaml
# 定义 nginx Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.25
          ports:
            - containerPort: 80
```

---

## Service 资源定义

**基本写法：定义 ClusterIP Service**
```yaml
`apiVersion: v1
kind: Service
metadata:
  name: <名称>
spec:
  selector:
    app: <标签>
  ports:
    - port: <端口>
      targetPort: <目标端口>`
```
```yaml
# 定义 ClusterIP Service
apiVersion: v1
kind: Service
metadata:
  name: nginx-svc
spec:
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
```

**基本写法：定义 NodePort Service**
```yaml
`spec:
  type: NodePort
  ports:
    - port: <端口>
      targetPort: <目标端口>
      nodePort: <节点端口>`
```
```yaml
# 定义 NodePort Service
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30080
```

**基本写法：定义 LoadBalancer Service**
```yaml
`spec:
  type: LoadBalancer
  ports:
    - port: <端口>`
```
```yaml
# 定义 LoadBalancer Service
apiVersion: v1
kind: Service
metadata:
  name: nginx-lb
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
```

---

## ConfigMap 资源定义

**基本写法：定义 ConfigMap**
```yaml
`apiVersion: v1
kind: ConfigMap
metadata:
  name: <名称>
data:
  <键>: <值>`
```
```yaml
# 定义应用配置 ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_ENV: production
  LOG_LEVEL: info
  config.yaml: |
    server:
      port: 8080
      host: 0.0.0.0
```

---

## Secret 资源定义

**基本写法：定义 Opaque Secret**
```yaml
`apiVersion: v1
kind: Secret
metadata:
  name: <名称>
type: Opaque
data:
  <键>: <Base64值>`
```
```yaml
# 定义数据库密码 Secret
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  username: YWRtaW4=
  password: c2VjcmV0MTIz
```

**基本写法：使用 stringData 明文**
```yaml
`apiVersion: v1
kind: Secret
metadata:
  name: <名称>
type: Opaque
stringData:
  <键>: <明文值>`
```
```yaml
# 使用明文定义 Secret
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
stringData:
  username: admin
  password: secret123
```

---

## Ingress 资源定义

**基本写法：定义 Ingress**
```yaml
`apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: <名称>
spec:
  rules:
    - host: <域名>
      http:
        paths:
          - path: <路径>
            pathType: Prefix
            backend:
              service:
                name: <服务名>
                port:
                  number: <端口>`
```
```yaml
# 定义 nginx Ingress
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress
spec:
  rules:
    - host: example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: nginx-svc
                port:
                  number: 80
```

---

## 资源配额与限制

**基本写法：定义资源请求和限制**
```yaml
`spec:
  containers:
    - name: <名称>
      resources:
        requests:
          cpu: <CPU请求>
          memory: <内存请求>
        limits:
          cpu: <CPU限制>
          memory: <内存限制>`
```
```yaml
# 设置容器资源配额
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
    - name: app
      image: myapp
      resources:
        requests:
          cpu: 100m
          memory: 128Mi
        limits:
          cpu: 500m
          memory: 512Mi
```

---

## 健康检查

**基本写法：定义存活探针**
```yaml
`spec:
  containers:
    - name: <名称>
      livenessProbe:
        httpGet:
          path: <路径>
          port: <端口>
        initialDelaySeconds: <秒数>`
```
```yaml
# 定义 HTTP 存活探针
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
    - name: app
      image: myapp
      livenessProbe:
        httpGet:
          path: /health
          port: 8080
        initialDelaySeconds: 30
        periodSeconds: 10
```

**基本写法：定义就绪探针**
```yaml
`spec:
  containers:
    - name: <名称>
      readinessProbe:
        httpGet:
          path: <路径>
          port: <端口>`
```
```yaml
# 定义 HTTP 就绪探针
spec:
  containers:
    - name: app
      image: myapp
      readinessProbe:
        httpGet:
          path: /ready
          port: 8080
        initialDelaySeconds: 5
        periodSeconds: 10
```

---

## 持久化存储

**基本写法：定义 PersistentVolumeClaim**
```yaml
`apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: <名称>
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: <大小>`
```
```yaml
# 定义 10GB 的 PVC
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

**基本写法：在 Pod 中使用 PVC**
```yaml
`spec:
  containers:
    - name: <名称>
      volumeMounts:
        - mountPath: <挂载路径>
          name: <卷名>
  volumes:
    - name: <卷名>
      persistentVolumeClaim:
        claimName: <PVC名称>`
```
```yaml
# 在 Pod 中挂载 PVC
spec:
  containers:
    - name: app
      image: myapp
      volumeMounts:
        - mountPath: /data
          name: data-volume
  volumes:
    - name: data-volume
      persistentVolumeClaim:
        claimName: data-pvc
```

---

## 命名空间

**基本写法：定义 Namespace**
```yaml
`apiVersion: v1
kind: Namespace
metadata:
  name: <名称>`
```
```yaml
# 定义开发环境命名空间
apiVersion: v1
kind: Namespace
metadata:
  name: dev
  labels:
    name: dev
```

**基本写法：定义 ResourceQuota**
```yaml
`apiVersion: v1
kind: ResourceQuota
metadata:
  name: <名称>
  namespace: <命名空间>
spec:
  hard:
    requests.cpu: <CPU总量>
    requests.memory: <内存总量>`
```
```yaml
# 限制命名空间资源配额
apiVersion: v1
kind: ResourceQuota
metadata:
  name: dev-quota
  namespace: dev
spec:
  hard:
    requests.cpu: "4"
    requests.memory: 8Gi
    limits.cpu: "8"
    limits.memory: 16Gi
```
