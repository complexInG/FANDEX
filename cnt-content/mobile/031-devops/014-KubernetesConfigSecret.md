# DevOps Kubernetes ConfigMap 与 Secret

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## ConfigMap 创建

**基本写法：从字面值创建 ConfigMap**
`kubectl create configmap <名称> --from-literal=<键>=<值>`
```bash
# 创建应用配置 ConfigMap
kubectl create configmap app-config --from-literal=APP_ENV=production --from-literal=LOG_LEVEL=info
```

**基本写法：从文件创建 ConfigMap**
`kubectl create configmap <名称> --from-file=<文件>`
```bash
# 从配置文件创建 ConfigMap
kubectl create configmap nginx-config --from-file=nginx.conf
```

**基本写法：从目录创建 ConfigMap**
`kubectl create configmap <名称> --from-file=<目录>`
```bash
# 从目录批量创建 ConfigMap
kubectl create configmap app-configs --from-file=./configs/
```

**基本写法：从环境变量文件创建**
`kubectl create configmap <名称> --from-env-file=<文件>`
```bash
# 从 env 文件创建 ConfigMap
kubectl create configmap app-env --from-env-file=.env
```

---

## ConfigMap YAML 定义

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
# 定义应用配置
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_ENV: production
  LOG_LEVEL: info
  APP_PORT: "8080"
```

**基本写法：多行配置文件**
```yaml
`data:
  <文件名>: |
    <文件内容>`
```
```yaml
# 定义多行配置文件
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-config
data:
  nginx.conf: |
    server {
      listen 80;
      location / {
        proxy_pass http://backend:8080;
      }
    }
```

---

## Secret 创建

**基本写法：从字面值创建 Secret**
`kubectl create secret generic <名称> --from-literal=<键>=<值>`
```bash
# 创建数据库密码 Secret
kubectl create secret generic db-secret --from-literal=username=admin --from-literal=password=secret123
```

**基本写法：从文件创建 Secret**
`kubectl create secret generic <名称> --from-file=<键>=<文件>`
```bash
# 从文件创建 Secret
kubectl create secret generic tls-secret --from-file=tls.crt=cert.pem --from-file=tls.key=key.pem
```

**基本写法：创建 docker-registry Secret**
`kubectl create secret docker-registry <名称> --docker-server=<服务器> --docker-username=<用户> --docker-password=<密码>`
```bash
# 创建镜像仓库认证 Secret
kubectl create secret docker-registry regcred --docker-server=registry.example.com --docker-username=user --docker-password=pass
```

**基本写法：创建 TLS Secret**
`kubectl create secret tls <名称> --cert=<证书> --key=<私钥>`
```bash
# 创建 TLS 证书 Secret
kubectl create secret tls tls-secret --cert=cert.pem --key=key.pem
```

---

## Secret YAML 定义

**基本写法：定义 Opaque Secret**
```yaml
`apiVersion: v1
kind: Secret
metadata:
  name: <名称>
type: Opaque
data:
  <键>: <Base64编码值>`
```
```yaml
# 定义 Secret（值需 Base64 编码）
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
# 使用明文定义 Secret（自动编码）
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

## 在 Pod 中使用 ConfigMap

**基本写法：作为环境变量使用**
```yaml
`spec:
  containers:
    - name: <名称>
      envFrom:
        - configMapRef:
            name: <ConfigMap名>`
```
```yaml
# 将 ConfigMap 所有键值作为环境变量
spec:
  containers:
    - name: app
      image: myapp
      envFrom:
        - configMapRef:
            name: app-config
```

**基本写法：单个环境变量引用**
```yaml
`spec:
  containers:
    - name: <名称>
      env:
        - name: <环境变量名>
          valueFrom:
            configMapKeyRef:
              name: <ConfigMap名>
              key: <键>`
```
```yaml
# 引用 ConfigMap 中的单个键
spec:
  containers:
    - name: app
      image: myapp
      env:
        - name: APP_ENV
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: APP_ENV
```

**基本写法：作为数据卷挂载**
```yaml
`spec:
  containers:
    - name: <名称>
      volumeMounts:
        - name: <卷名>
          mountPath: <挂载路径>
  volumes:
    - name: <卷名>
      configMap:
        name: <ConfigMap名>`
```
```yaml
# 将 ConfigMap 挂载为配置文件
spec:
  containers:
    - name: nginx
      image: nginx
      volumeMounts:
        - name: config
          mountPath: /etc/nginx/nginx.conf
          subPath: nginx.conf
  volumes:
    - name: config
      configMap:
        name: nginx-config
```

---

## 在 Pod 中使用 Secret

**基本写法：作为环境变量使用**
```yaml
`spec:
  containers:
    - name: <名称>
      env:
        - name: <环境变量名>
          valueFrom:
            secretKeyRef:
              name: <Secret名>
              key: <键>`
```
```yaml
# 引用 Secret 中的密码
spec:
  containers:
    - name: app
      image: myapp
      env:
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
```

**基本写法：作为数据卷挂载**
```yaml
`spec:
  containers:
    - name: <名称>
      volumeMounts:
        - name: <卷名>
          mountPath: <挂载路径>
          readOnly: true
  volumes:
    - name: <卷名>
      secret:
        secretName: <Secret名>`
```
```yaml
# 将 Secret 挂载为文件
spec:
  containers:
    - name: app
      image: myapp
      volumeMounts:
        - name: secrets
          mountPath: /etc/secrets
          readOnly: true
  volumes:
    - name: secrets
      secret:
        secretName: app-secret
```

**基本写法：镜像拉取凭证**
```yaml
`spec:
  imagePullSecrets:
    - name: <Secret名>`
```
```yaml
# 使用镜像仓库认证
spec:
  imagePullSecrets:
    - name: regcred
  containers:
    - name: app
      image: registry.example.com/myapp:v1
```

---

## 查看 ConfigMap 和 Secret

**基本写法：查看 ConfigMap**
`kubectl get configmap <名称> -o yaml`
```bash
# 查看 app-config 的完整内容
kubectl get configmap app-config -o yaml
```

**基本写法：查看 Secret**
`kubectl get secret <名称> -o yaml`
```bash
# 查看 db-secret 的内容（Base64 编码）
kubectl get secret db-secret -o yaml
```

**基本写法：解码 Secret 值**
`kubectl get secret <名称> -o jsonpath='{.data.<键>}' | base64 -d`
```bash
# 解码 Secret 中的 password 值
kubectl get secret db-secret -o jsonpath='{.data.password}' | base64 -d
```

**基本写法：列出所有 ConfigMap**
`kubectl get configmap`
```bash
# 列出所有 ConfigMap
kubectl get cm
```

**基本写法：列出所有 Secret**
`kubectl get secret`
```bash
# 列出所有 Secret
kubectl get secret
```

---

## 更新 ConfigMap 和 Secret

**基本写法：更新 ConfigMap**
`kubectl edit configmap <名称>`
```bash
# 编辑 ConfigMap 内容
kubectl edit configmap app-config
```

**基本写法：使用 apply 更新**
`kubectl apply -f <文件>`
```bash
# 应用更新后的 ConfigMap YAML
kubectl apply -f configmap.yaml
```

**基本写法：重新创建 Secret**
`kubectl create secret generic <名称> --from-literal=<键>=<新值> --dry-run=client -o yaml | kubectl apply -f -`
```bash
# 更新 Secret 值
kubectl create secret generic db-secret --from-literal=password=newpass --dry-run=client -o yaml | kubectl apply -f -
```

---

## 删除 ConfigMap 和 Secret

**基本写法：删除 ConfigMap**
`kubectl delete configmap <名称>`
```bash
# 删除 app-config
kubectl delete configmap app-config
```

**基本写法：删除 Secret**
`kubectl delete secret <名称>`
```bash
# 删除 db-secret
kubectl delete secret db-secret
```

**基本写法：按标签批量删除**
`kubectl delete configmap -l <标签选择器>`
```bash
# 删除带 app=test 标签的 ConfigMap
kubectl delete configmap -l app=test
```

---

## ConfigMap 热更新

**基本写法：挂载为数据卷的 ConfigMap 自动更新**
```yaml
`spec:
  containers:
    - name: <名称>
      volumeMounts:
        - name: <卷名>
          mountPath: <路径>
  volumes:
    - name: <卷名>
      configMap:
        name: <ConfigMap名>`
```
```yaml
# ConfigMap 更新后自动同步到 Pod（约 1 分钟）
spec:
  containers:
    - name: app
      image: myapp
      volumeMounts:
        - name: config
          mountPath: /etc/config
  volumes:
    - name: config
      configMap:
        name: app-config
```

**基本写法：触发 Pod 重新加载**
`kubectl rollout restart deployment/<名称>`
```bash
# 重启 Deployment 使 ConfigMap 生效
kubectl rollout restart deployment/app
```

---

## 使用 subPath 挂载单个文件

**基本写法：挂载 ConfigMap 中的单个文件**
```yaml
`volumeMounts:
  - name: <卷名>
    mountPath: <完整路径>
    subPath: <文件名>`
```
```yaml
# 只挂载 nginx.conf 文件不覆盖目录
spec:
  containers:
    - name: nginx
      image: nginx
      volumeMounts:
        - name: config
          mountPath: /etc/nginx/nginx.conf
          subPath: nginx.conf
  volumes:
    - name: config
      configMap:
        name: nginx-config
```
