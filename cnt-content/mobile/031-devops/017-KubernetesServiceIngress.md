# Kubernetes Service/Ingress 速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Service 类型

**基本用法:创建 ClusterIP**
`kubectl expose deployment <名称>`

```bash
# 暴露为集群内部服务
kubectl expose deployment nginx --port=80 --target-port=80

# 通过 YAML 创建 ClusterIP
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
EOF
```

---

**基本用法:NodePort 对外暴露**
`kubectl expose deployment <名称> --type=NodePort`

```bash
# 在节点端口暴露
kubectl expose deployment web --type=NodePort --port=80

# 指定端口范围(30000-32767)
kubectl expose deployment web --type=NodePort --port=80 --target-port=8080
```

---

**基本用法:LoadBalancer 类型**
`kubectl expose deployment <名称> --type=LoadBalancer`

```bash
# 云厂商负载均衡器
kubectl expose deployment web --type=LoadBalancer --port=80
```

---

## 查看 Service

**基本用法:查看服务**
`kubectl get svc`

```bash
# 列出所有服务
kubectl get svc

# 查看详情含 Endpoints
kubectl describe svc nginx

# 查看服务 Endpoints
kubectl get endpoints nginx
```

---

## Ingress 配置

**基本用法:创建 Ingress**
`kubectl apply -f <文件>`

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
    - host: app.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web
                port:
                  number: 80
```

---

```bash
# 应用 Ingress
kubectl apply -f ingress.yaml

# 查看 Ingress
kubectl get ingress

# 查看 Ingress 详情含分配地址
kubectl describe ingress web-ingress
```

---

## Ingress TLS

**基本用法:配置 HTTPS**
`spec.tls:`

```yaml
spec:
  tls:
    - hosts:
        - app.example.com
      secretName: app-tls
  rules:
    - host: app.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web
                port:
                  number: 80
```

---

**基本用法:创建 TLS Secret**
`kubectl create secret tls <名称>`

```bash
# 从证书创建 TLS Secret
kubectl create secret tls app-tls \
  --cert=fullchain.pem \
  --key=privkey.pem
```

---