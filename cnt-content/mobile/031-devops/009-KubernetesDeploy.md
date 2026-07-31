# DevOps Kubernetes 部署管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## kubectl rollout 滚动发布

**基本写法：查看发布状态**
`kubectl rollout status deployment/<名称>`
```bash
# 查看 nginx 部署状态
kubectl rollout status deployment/nginx
```

**基本写法：查看发布历史**
`kubectl rollout history deployment/<名称>`
```bash
# 查看 nginx 部署历史版本
kubectl rollout history deployment/nginx
```

**基本写法：查看指定版本详情**
`kubectl rollout history deployment/<名称> --revision=<版本号>`
```bash
# 查看版本 2 的详情
kubectl rollout history deployment/nginx --revision=2
```

**基本写法：回滚到上一版本**
`kubectl rollout undo deployment/<名称>`
```bash
# 回滚 nginx 到上一版本
kubectl rollout undo deployment/nginx
```

**基本写法：回滚到指定版本**
`kubectl rollout undo deployment/<名称> --to-revision=<版本号>`
```bash
# 回滚到版本 3
kubectl rollout undo deployment/nginx --to-revision=3
```

**基本写法：重启部署**
`kubectl rollout restart deployment/<名称>`
```bash
# 重启 nginx 部署
kubectl rollout restart deployment/nginx
```

---

## kubectl set 更新配置

**基本写法：更新镜像**
`kubectl set image deployment/<名称> <容器>=<新镜像>`
```bash
# 更新 nginx 镜像版本
kubectl set image deployment/nginx nginx=nginx:1.26
```

**基本写法：更新环境变量**
`kubectl set env deployment/<名称> <键>=<值>`
```bash
# 设置环境变量
kubectl set env deployment/nginx DEBUG=true
```

**基本写法：更新资源限制**
`kubectl set resources deployment/<名称> -c <容器> --limits=<资源>`
```bash
# 更新 CPU 和内存限制
kubectl set resources deployment/nginx -c nginx --limits=cpu=1,memory=512Mi
```

**基本写法：设置 Service 选择器**
`kubectl set selector service <名称> <选择器>`
```bash
# 更新 Service 的标签选择器
kubectl set selector svc nginx app=nginx-new
```

---

## kubectl autoscale 自动伸缩

**基本写法：水平自动伸缩**
`kubectl autoscale deployment <名称> --min=<最小> --max=<最大> --cpu-percent=<百分比>`
```bash
# 自动伸缩 nginx 在 2 到 10 副本之间
kubectl autoscale deployment nginx --min=2 --max=10 --cpu-percent=80
```

**基本写法：指定 HPA 目标**
`kubectl autoscale deployment <名称> --min=<最小> --max=<最大> --cpu-percent=<百分比>`
```bash
# CPU 使用率超过 70% 自动扩容
kubectl autoscale deployment web --min=3 --max=20 --cpu-percent=70
```

---

## kubectl label/annotate 标签管理

**基本写法：添加标签**
`kubectl label <资源类型> <名称> <键>=<值>`
```bash
# 给 Pod 添加环境标签
kubectl label pod nginx env=prod
```

**基本写法：更新标签**
`kubectl label <资源类型> <名称> <键>=<新值> --overwrite`
```bash
# 更新标签值
kubectl label pod nginx env=staging --overwrite
```

**基本写法：删除标签**
`kubectl label <资源类型> <名称> <键>-`
```bash
# 删除 env 标签
kubectl label pod nginx env-
```

**基本写法：添加注解**
`kubectl annotate <资源类型> <名称> <键>=<值>`
```bash
# 添加注解信息
kubectl annotate deployment nginx managed-by=kubectl
```

---

## kubectl expose 暴露服务

**基本写法：暴露 Deployment 为 Service**
`kubectl expose deployment <名称> --port=<端口> --target-port=<目标端口>`
```bash
# 暴露 nginx Deployment
kubectl expose deployment nginx --port=80 --target-port=80
```

**基本写法：指定类型暴露**
`kubectl expose deployment <名称> --type=<类型> --port=<端口>`
```bash
# 暴露为 NodePort 类型
kubectl expose deployment nginx --type=NodePort --port=80
```

**基本写法：暴露 Pod**
`kubectl expose pod <名称> --port=<端口>`
```bash
# 暴露 Pod 为 Service
kubectl expose pod nginx --port=80 --name=nginx-svc
```

---

## kubectl top 资源监控

**基本写法：查看节点资源使用**
`kubectl top node`
```bash
# 查看所有节点的资源使用情况
kubectl top node
```

**基本写法：查看指定节点**
`kubectl top node <节点名>`
```bash
# 查看指定节点的资源使用
kubectl top node node1
```

**基本写法：查看 Pod 资源使用**
`kubectl top pod`
```bash
# 查看所有 Pod 的资源使用
kubectl top pod
```

**基本写法：查看指定命名空间 Pod**
`kubectl top pod -n <命名空间>`
```bash
# 查看 dev 命名空间的 Pod 资源使用
kubectl top pod -n dev
```

**基本写法：按资源使用排序**
`kubectl top pod --sort-by=<字段>`
```bash
# 按 CPU 使用量排序
kubectl top pod --sort-by=cpu
```

---

## kubectl cordon/drain 节点维护

**基本写法：标记节点不可调度**
`kubectl cordon <节点名>`
```bash
# 标记 node1 不可调度
kubectl cordon node1
```

**基本写法：驱逐节点上的 Pod**
`kubectl drain <节点名>`
```bash
# 驱逐 node1 上的所有 Pod
kubectl drain node1 --ignore-daemonsets --delete-emptydir-data
```

**基本写法：恢复节点调度**
`kubectl uncordon <节点名>`
```bash
# 恢复 node1 调度
kubectl uncordon node1
```

---

## kubectl taint 节点污点

**基本写法：添加污点**
`kubectl taint node <节点名> <键>=<值>:<效果>`
```bash
# 给节点添加专用污点
kubectl taint node node1 dedicated=prod:NoSchedule
```

**基本写法：删除污点**
`kubectl taint node <节点名> <键>-`
```bash
# 删除节点的污点
kubectl taint node node1 dedicated-
```

**基本写法：容忍所有未调度**
`kubectl taint node <节点名> node.kubernetes.io/unschedulable:NoSchedule-`
```bash
# 移除 unschedulable 污点
kubectl taint node node1 node.kubernetes.io/unschedulable:NoSchedule-
```

---

## kubectl dry-run 生成清单

**基本写法：生成 Deployment YAML**
`kubectl create deployment <名称> --image=<镜像> --dry-run=client -o yaml`
```bash
# 生成 nginx Deployment 的 YAML
kubectl create deployment nginx --image=nginx --dry-run=client -o yaml > deploy.yaml
```

**基本写法：生成 Service YAML**
`kubectl expose deployment <名称> --port=<端口> --dry-run=client -o yaml`
```bash
# 生成 Service 的 YAML
kubectl expose deployment nginx --port=80 --dry-run=client -o yaml > svc.yaml
```

**基本写法：生成 Namespace YAML**
`kubectl create namespace <名称> --dry-run=client -o yaml`
```bash
# 生成 Namespace 的 YAML
kubectl create namespace dev --dry-run=client -o yaml > ns.yaml
```

---

## kubectl explain 查询字段

**基本写法：查看资源字段**
`kubectl explain <资源类型>`
```bash
# 查看 Pod 的字段定义
kubectl explain pod
```

**基本写法：查看嵌套字段**
`kubectl explain <资源类型>.<字段路径>`
```bash
# 查看 Pod 容器规格字段
kubectl explain pod.spec.containers
```

**基本写法：递归查看所有字段**
`kubectl explain <资源类型> --recursive`
```bash
# 递归查看 Pod 的所有字段
kubectl explain pod --recursive
```
