# Kubernetes 命名空间与标签速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Namespace 命名空间

**基本用法:创建命名空间**
`kubectl create namespace <名称>`

```bash
# 创建命名空间
kubectl create namespace production

# 通过 YAML 创建
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Namespace
metadata:
  name: production
EOF
```

---

**基本用法:查看命名空间**
`kubectl get namespaces`

```bash
# 列出所有命名空间
kubectl get ns

# 查看指定命名空间详情
kubectl describe ns production
```

---

**基本用法:切换默认命名空间**
`kubectl config set-context --current --namespace=<名称>`

```bash
# 永久切换当前上下文命名空间
kubectl config set-context --current --namespace=production

# 临时指定命名空间执行命令
kubectl get pods -n staging
```

---

**基本用法:删除命名空间**
`kubectl delete namespace <名称>`

```bash
# 删除命名空间(级联删除其下资源)
kubectl delete namespace old-env
```

---

## Label 标签

**基本用法:给资源打标签**
`kubectl label <资源> <名称> <键>=<值>`

```bash
# 给 Pod 打标签
kubectl label pod nginx env=production

# 给 Deployment 打标签
kubectl label deploy web tier=frontend version=v2
```

---

**基本用法:查看标签**
`kubectl get <资源> --show-labels`

```bash
# 查看 Pod 及其标签
kubectl get pods --show-labels

# 仅显示指定标签列
kubectl get pods -L env,version
```

---

**基本用法:按标签筛选**
`kubectl get <资源> -l <选择器>`

```bash
# 等值匹配
kubectl get pods -l env=production

# 多标签交集
kubectl get pods -l env=production,tier=frontend

# 不等于匹配
kubectl get pods -l env!=staging

# 集合匹配
kubectl get pods -l 'tier in (frontend,backend)'
```

---

**基本用法:修改与删除标签**
`kubectl label <资源> <名称> <键>=<新值> --overwrite`

```bash
# 更新标签值
kubectl label pod nginx env=staging --overwrite

# 删除标签(键后加减号)
kubectl label pod nginx env-
```

---

## 注解 Annotation

**基本用法:添加注解**
`kubectl annotate <资源> <名称> <键>=<值>`

```bash
# 添加注解(用于非标识性元数据)
kubectl annotate pod nginx description="生产环境 Nginx"

# 删除注解
kubectl annotate pod nginx description-
```

---