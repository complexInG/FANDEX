# Kubernetes RBAC 权限控制速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Role 与 ClusterRole

**基本用法:查看角色**
`kubectl get roles,clusterroles [-n <命名空间>]`

```bash
# 列出当前命名空间 Role
kubectl get roles

# 列出集群级 ClusterRole
kubectl get clusterroles

# 查看角色详情
kubectl describe clusterrole cluster-admin
```

---

**基本用法:创建命名空间 Role**
`kubectl apply -f <role.yaml>`

```yaml
# role.yaml 命名空间角色示例
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: production
rules:
- apiGroups: [""]
  resources: ["pods", "pods/log"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs: ["get", "list", "watch", "update", "patch"]
```

---

**基本用法:创建 ClusterRole**
`kubectl apply -f <clusterrole.yaml>`

```yaml
# clusterrole.yaml 集群角色示例
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: node-viewer
rules:
- apiGroups: [""]
  resources: ["nodes", "nodes/metrics"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["metrics.k8s.io"]
  resources: ["nodes"]
  verbs: ["get", "list"]
```

---

**基本用法:使用 kubectl 创建 Role**
`kubectl create role <名称> --verb=<动词> --resource=<资源>`

```bash
# 创建对 Pod 的只读角色
kubectl create role pod-reader --verb=get,list,watch --resource=pods,pods/log -n production

# 创建对 Service 的管理角色
kubectl create role svc-manager --verb='*' --resource=services,services/status -n production
```

---

**基本用法:聚合 ClusterRole**
`aggregationRule`

```yaml
# 聚合带有特定标签的 ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: monitoring-aggregate
aggregationRule:
  clusterRoleSelectors:
  - matchLabels:
      rbac.example.com/aggregate-to-monitoring: "true"
rules: []
```

---

## RoleBinding 与 ClusterRoleBinding

**基本用法:查看绑定**
`kubectl get rolebindings,clusterrolebindings [-n <命名空间>]`

```bash
# 列出当前命名空间 RoleBinding
kubectl get rolebindings

# 列出集群级 ClusterRoleBinding
kubectl get clusterrolebindings

# 查看绑定详情(看绑定的主体和角色)
kubectl describe rolebinding pod-reader-binding -n production
```

---

**基本用法:创建 RoleBinding**
`kubectl apply -f <rolebinding.yaml>`

```yaml
# rolebinding.yaml 角色绑定示例
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pod-reader-binding
  namespace: production
subjects:
- kind: User
  name: alice
  apiGroup: rbac.authorization.k8s.io
- kind: ServiceAccount
  name: app-sa
  namespace: production
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

---

**基本用法:创建 ClusterRoleBinding**
`kubectl apply -f <clusterrolebinding.yaml>`

```yaml
# clusterrolebinding.yaml 集群角色绑定示例
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: global-pod-reader
subjects:
- kind: Group
  name: devops-team
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

---

**基本用法:使用 kubectl 创建绑定**
`kubectl create rolebinding <名称> --role=<角色> --user=<用户>`

```bash
# 创建 RoleBinding(绑定 Role 给用户)
kubectl create rolebinding alice-pod-reader --role=pod-reader --user=alice -n production

# 创建 RoleBinding(绑定 ClusterRole 给用户,限制在该命名空间)
kubectl create rolebinding bob-admin --clusterrole=admin --user=bob -n staging

# 创建 ClusterRoleBinding
kubectl create clusterrolebinding carol-node-viewer --clusterrole=node-viewer --user=carol
```

---

## ServiceAccount 服务账户

**基本用法:查看 ServiceAccount**
`kubectl get sa [-n <命名空间>]`

```bash
# 列出当前命名空间的 ServiceAccount
kubectl get sa

# 查看 ServiceAccount 详情(含挂载的 Secret)
kubectl describe sa default -n production

# 查看 ServiceAccount 的 Token Secret
kubectl get secret -n production --field-selector=type=kubernetes.io/service-account-token
```

---

**基本用法:创建 ServiceAccount**
`kubectl create sa <名称> [-n <命名空间>]`

```bash
# 创建 ServiceAccount
kubectl create sa app-sa -n production

# 通过 YAML 创建(带注解)
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-sa
  namespace: production
  annotations:
    iam.gke.io/gcp-service-account: app-gsa@project.iam.gserviceaccount.com
EOF
```

---

**基本用法:为 ServiceAccount 创建 Token**
`kubectl create token <名称>`

```bash
# 创建临时 Token(K8s 1.24+)
kubectl create token app-sa -n production

# 指定 Token 有效期
kubectl create token app-sa -n production --duration=24h

# 创建长期 Token Secret(传统方式)
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: app-sa-token
  namespace: production
  annotations:
    kubernetes.io/service-account.name: app-sa
type: kubernetes.io/service-account-token
EOF
```

---

**基本用法:Pod 使用 ServiceAccount**
`spec.serviceAccountName`

```yaml
# Pod 指定 ServiceAccount
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  serviceAccountName: app-sa
  automountServiceAccountToken: true
  containers:
  - name: app
    image: nginx
```

---

## 权限验证

**基本用法:检查用户权限**
`kubectl auth can-i <动作> <资源>`

```bash
# 检查当前用户能否创建 Pod
kubectl auth can-i create pods

# 检查指定用户能否删除 Deployment
kubectl auth can-i delete deployments --as=alice -n production

# 检查 ServiceAccount 的权限
kubectl auth can-i list secrets --as=system:serviceaccount:production:app-sa -n production

# 列出当前用户在命名空间内可执行的所有操作
kubectl auth can-i --list -n production
```

---

**基本用法:权限分析**
`kubectl auth can-i --list --as=<用户>`

```bash
# 列出指定用户的所有权限
kubectl auth can-i --list --as=alice -n production

# 列出 ServiceAccount 的所有权限
kubectl auth can-i --list --as=system:serviceaccount:production:app-sa -n production

# 检查跨命名空间权限
kubectl auth can-i get pods --as=bob -A
```

---

## RBAC 排查

**基本用法:查看 Subject 绑定**
`kubectl get rolebindings,clusterrolebindings -o jsonpath=...`

```bash
# 查找用户绑定的所有 RoleBinding
kubectl get rolebindings -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{"\t"}{.subjects[*].name}{"\n"}{end}' | grep alice

# 查找 ServiceAccount 的所有绑定
kubectl get rolebindings,clusterrolebindings -A -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.subjects[*].kind}{"/"}{.subjects[*].name}{"\n"}{end}' | grep app-sa
```

---

**基本用法:查看 Role 引用的资源**
`kubectl get role -o yaml`

```bash
# 查看命名空间内 Role 的权限规则
kubectl get role pod-reader -n production -o yaml

# 查看系统 ClusterRole 的权限
kubectl get clusterrole system:node -o yaml

# 导出所有 ClusterRole 与权限规则
kubectl get clusterroles -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}' > clusterroles.txt
```

---

## 默认角色与最佳实践

**基本用法:查看系统默认角色**
`kubectl get clusterroles`

```bash
# 查看系统内置 ClusterRole
kubectl get clusterroles | grep -E 'system:|cluster-admin|admin|edit|view'

# cluster-admin:超级管理员
# admin:命名空间内大部分资源管理(除资源配额)
# edit:命名空间内可修改资源
# view:命名空间内只读
```

---

**基本用法:最小权限示例**
`kubectl create role <名称> --verb=<动词> --resource=<资源> --resource-name=<名称>`

```bash
# 仅允许访问特定 Pod
kubectl create role single-pod-viewer --verb=get --resource=pods --resource-name=my-app-pod -n production

# 仅允许访问特定 ConfigMap
kubectl create role config-reader --verb=get,list,watch --resource=configmaps --resource-name=app-config -n production
```

---

**基本用法:删除 RBAC 资源**
`kubectl delete <role|rolebinding> <名称>`

```bash
# 删除 Role
kubectl delete role pod-reader -n production

# 删除 RoleBinding
kubectl delete rolebinding pod-reader-binding -n production

# 删除 ClusterRole
kubectl delete clusterrole node-viewer

# 删除 ClusterRoleBinding
kubectl delete clusterrolebinding global-pod-reader
```

---

## Kubeconfig 与认证

**基本用法:为用户生成证书**
`openssl req -new -key <key> -out <csr> -subj "/CN=<用户名>"`

```bash
# 生成私钥
openssl genrsa -out alice.key 2048

# 生成 CSR(用户名 alice,组 devops)
openssl req -new -key alice.key -out alice.csr -subj "/CN=alice/O=devops"

# 用集群 CA 签发证书
openssl x509 -req -in alice.csr -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -out alice.crt -days 365
```

---

**基本用法:配置 kubeconfig**
`kubectl config set-credentials <用户名> --client-certificate=<cert> --client-key=<key>`

```bash
# 添加用户凭据到 kubeconfig
kubectl config set-credentials alice --client-certificate=alice.crt --client-key=alice.key

# 设置上下文
kubectl config set-context alice-context --cluster=kubernetes --user=alice --namespace=production

# 切换上下文
kubectl config use-context alice-context
```

---

**基本用法:为 ServiceAccount 生成 kubeconfig**
`kubectl config set-credentials <名称> --token=<token>`

```bash
# 获取 ServiceAccount Token
TOKEN=$(kubectl create token app-sa -n production)

# 添加到 kubeconfig
kubectl config set-credentials app-sa --token=$TOKEN

# 设置上下文
kubectl config set-context app-sa-context --cluster=kubernetes --user=app-sa --namespace=production

# 切换并测试
kubectl config use-context app-sa-context
kubectl get pods
```
