# Kubernetes 故障排查命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Pod 状态排查

**基本用法:查看 Pod 状态**
`kubectl get pods [-n <命名空间>]`

```bash
# 列出所有命名空间的 Pod
kubectl get pods -A

# 查看指定命名空间的 Pod(宽输出)
kubectl get pods -n production -o wide

# 按标签筛选
kubectl get pods -l app=web -n production

# 监视 Pod 状态变化
kubectl get pods -w -n production

# 按重启次数排序
kubectl get pods -A --sort-by=.status.containerStatuses[0].restartCount
```

---

**基本用法:查看 Pod 详情**
`kubectl describe pod <名称>`

```bash
# 查看 Pod 详情(包含事件)
kubectl describe pod web-xxx -n production

# 查看事件
kubectl get events -n production --sort-by='.lastTimestamp'

# 过滤 Warning 事件
kubectl get events -n production --field-selector type=Warning

# 查看 Pod 完整 YAML
kubectl get pod web-xxx -n production -o yaml
```

---

**基本用法:Pod 常见状态分析**
`kubectl get pod <名称> -o jsonpath='{.status.phase}'`

```bash
# 查看 Pod 阶段
kubectl get pod web-xxx -o jsonpath='{.status.phase}'

# 查看容器状态
kubectl get pod web-xxx -o jsonpath='{.status.containerStatuses[*].state}'

# 查看 Pod 状态条件
kubectl get pod web-xxx -o jsonpath='{.status.conditions[*].type}'

# 查看 Pod 失败原因
kubectl get pod web-xxx -o jsonpath='{.status.conditions[?(@.type=="Ready")].message}'
```

---

## 容器日志与调试

**基本用法:查看容器日志**
`kubectl logs <pod> [-c <容器>]`

```bash
# 查看当前日志
kubectl logs web-xxx -n production

# 查看多容器 Pod 指定容器日志
kubectl logs web-xxx -c app -n production

# 跟踪日志
kubectl logs -f web-xxx -n production

# 查看前 100 行
kubectl logs --tail=100 web-xxx -n production

# 查看过去 1 小时日志
kubectl logs --since=1h web-xxx -n production

# 查看 Pod 中所有容器日志
kubectl logs web-xxx --all-containers -n production
```

---

**基本用法:查看上一个容器日志**
`kubectl logs <pod> --previous`

```bash
# 查看崩溃前日志(容器重启后查前一次的日志)
kubectl logs web-xxx --previous -n production

# 查看指定容器前一次日志
kubectl logs web-xxx -c app --previous -n production

# 查看上一次日志的最后 50 行
kubectl logs web-xxx --previous --tail=50 -n production
```

---

**基本用法:exec 进入容器**
`kubectl exec -it <pod> -- <命令>`

```bash
# 进入容器 shell
kubectl exec -it web-xxx -n production -- sh

# 进入指定容器
kubectl exec -it web-xxx -c app -n production -- bash

# 在容器内执行单条命令
kubectl exec web-xxx -n production -- ls /app

# 执行多行命令
kubectl exec web-xxx -n production -- sh -c 'cat /etc/resolv.conf && env'
```

---

**基本用法:临时调试容器**
`kubectl debug <pod> --image=<调试镜像>`

```bash
# 给运行中的 Pod 添加临时调试容器
kubectl debug -it web-xxx --image=busybox:latest -n production

# 给 Pod 复制一份用于调试(不影响原 Pod)
kubectl debug -it web-xxx --image=busybox --copy-to=web-debug -n production

# 调试节点
kubectl debug node/node-1 -it --image=busybox

# 在调试容器中共享进程命名空间
kubectl debug -it web-xxx --image=busybox --target=app -n production
```

---

**基本用法:port-forward 端口转发**
`kubectl port-forward <pod> <本地端口>:<容器端口>`

```bash
# 转发 Pod 端口到本地
kubectl port-forward web-xxx 8080:80 -n production

# 转发 Service 端口
kubectl port-forward svc/web 8080:80 -n production

# 转发 Deployment 端口
kubectl port-forward deploy/web 8080:80 -n production

# 后台运行端口转发
kubectl port-forward web-xxx 8080:80 -n production &
```

---

## 资源与调度排查

**基本用法:查看节点资源**
`kubectl top|describe node`

```bash
# 查看节点资源使用
kubectl top nodes

# 查看节点详情(含资源分配)
kubectl describe node node-1

# 查看节点资源分配情况
kubectl describe node node-1 | grep -A 10 "Allocated resources"

# 查看节点上的 Pod
kubectl get pods -A --field-selector spec.nodeName=node-1
```

---

**基本用法:查看 Pod 资源**
`kubectl top pod`

```bash
# 查看 Pod 资源使用
kubectl top pods -n production

# 查看指定 Pod 各容器资源
kubectl top pod web-xxx -n production --containers

# 按 CPU 排序
kubectl top pods -n production --sort-by=CPU

# 按内存排序
kubectl top pods -n production --sort-by=MEMORY
```

---

**基本用法:排查 Pending Pod**
`kubectl describe pod <pending-pod>`

```bash
# 查看 Pending 原因
kubectl describe pod pending-pod | grep -A 10 Events

# 查看调度失败详情
kubectl get pod pending-pod -o jsonpath='{.status.conditions[?(@.reason=="Unschedulable")].message}'

# 检查资源是否足够
kubectl describe nodes | grep -A 5 "Allocated resources"

# 查看 Pod 资源请求
kubectl get pod pending-pod -o jsonpath='{.spec.containers[*].resources.requests}'
```

---

**基本用法:查看调度器决策**
`kubectl get events --field-selector reason=Scheduling`

```bash
# 查看调度相关事件
kubectl get events -n production --field-selector reason=Scheduled

# 查看调度失败事件
kubectl get events -n production --field-selector reason=FailedScheduling

# 查看 Pod 亲和性失败
kubectl get events -n production --field-selector reason=FailedScheduling -o jsonpath='{.items[*].message}'
```

---

## 网络排查

**基本用法:查看 Service**
`kubectl get svc|endpoints`

```bash
# 查看 Service
kubectl get svc -n production

# 查看 Endpoints(检查后端 Pod 是否就绪)
kubectl get endpoints web -n production

# 查看 Service 详情
kubectl describe svc web -n production

# 查看未关联 Pod 的 Service
kubectl get svc -A -o jsonpath='{range .items[*]}{@.metadata.name}{"\t"}{range @.spec.selector}{@}{"="}{@}{" "}{end}{"\n"}{end}'
```

---

**基本用法:DNS 排查**
`kubectl exec <pod> -- nslookup`

```bash
# 在 Pod 内测试 DNS 解析
kubectl exec -it web-xxx -- nslookup kubernetes.default

# 测试外部域名解析
kubectl exec -it web-xxx -- nslookup example.com

# 查看 CoreDNS 状态
kubectl get pods -n kube-system -l k8s-app=kube-dns

# 查看 CoreDNS 配置
kubectl get configmap coredns -n kube-system -o yaml

# 查看 CoreDNS 日志
kubectl logs -n kube-system -l k8s-app=kube-dns --tail=50
```

---

**基本用法:网络连通性测试**
`kubectl exec <pod> -- curl|ping`

```bash
# 测试到 Service 的连通性
kubectl exec -it web-xxx -- curl -v http://backend:8080/health

# 测试到外部网络
kubectl exec -it web-xxx -- curl -v https://example.com

# ping 测试(需要镜像支持)
kubectl exec -it web-xxx -- ping -c 3 8.8.8.8

# 测试 Pod 间连通性
kubectl exec -it web-xxx -- curl http://10.244.1.5:8080
```

---

**基本用法:网络策略排查**
`kubectl get networkpolicy`

```bash
# 查看网络策略
kubectl get networkpolicy -n production

# 查看策略详情
kubectl describe networkpolicy deny-all -n production

# 查看是否有策略限制流量
kubectl get networkpolicy -n production -o yaml

# 检查 Pod 标签是否匹配策略
kubectl get pods -n production --show-labels
```

---

## 控制器排查

**基本用法:Deployment 排查**
`kubectl rollout status`

```bash
# 查看滚动更新状态
kubectl rollout status deployment/web -n production

# 查看 Deployment 事件
kubectl get events -n production --field-selector involvedObject.kind=Deployment

# 查看 ReplicaSet
kubectl get rs -n production

# 查看 Pod 模板哈希
kubectl get pods -n production -l pod-template-hash --show-labels
```

---

**基本用法:StatefulSet 排查**
`kubectl get statefulset|pods`

```bash
# 查看 StatefulSet 状态
kubectl get statefulset mysql -n production

# 查看 StatefulSet Pod(按序号)
kubectl get pods -l app=mysql -n production -o wide

# 查看 PVC 绑定状态
kubectl get pvc -l app=mysql -n production

# 查看 Pod 亲和性
kubectl get pods -l app=mysql -n production -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.affinity}{"\n"}{end}'
```

---

**基本用法:查看控制器事件**
`kubectl describe <控制器>`

```bash
# 查看 Deployment 详情
kubectl describe deployment web -n production

# 查看 StatefulSet 详情
kubectl describe statefulset mysql -n production

# 查看 DaemonSet 详情
kubectl describe daemonset log-agent -n kube-system

# 查看 Job 状态
kubectl get jobs -n production
kubectl describe job batch-job -n production
```

---

## 存储排查

**基本用法:查看 PVC 状态**
`kubectl get pvc|pv`

```bash
# 查看 PVC 状态
kubectl get pvc -n production

# 查看 PV 状态
kubectl get pv

# 查看 PVC 绑定详情
kubectl describe pvc data-pvc -n production

# 查看 StorageClass
kubectl get sc
```

---

**基本用法:查看 Pod 卷挂载**
`kubectl describe pod`

```bash
# 查看卷挂载详情
kubectl describe pod web-xxx -n production | grep -A 30 Volumes

# 查看挂载路径
kubectl get pod web-xxx -n production -o jsonpath='{.spec.containers[*].volumeMounts}'

# 检查 PVC 是否正确挂载
kubectl get pod web-xxx -n production -o jsonpath='{.spec.volumes}'

# 查看挂载失败的 Pod
kubectl get pods -n production -o jsonpath='{range .items[?(@.status.phase=="Pending")]}{.metadata.name}{"\n"}{end}'
```

---

**基本用法:排查存储挂载失败**
`kubectl describe pod | grep -A 10 Events`

```bash
# 查看挂载失败原因
kubectl describe pod web-xxx -n production | grep -A 20 Events

# 查看 CSI 驱动状态
kubectl get csidriver
kubectl get csinode

# 查看 CSI Pod 状态
kubectl get pods -n kube-system | grep csi

# 查看 CSI 控制器日志
kubectl logs -n kube-system csi-controller-xxx
```

---

## 集群组件排查

**基本用法:查看组件状态**
`kubectl get componentstatus`

```bash
# 查看控制面组件
kubectl get componentstatus

# 查看核心组件 Pod
kubectl get pods -n kube-system

# 查看节点状态
kubectl get nodes
kubectl describe node node-1 | grep -A 10 Conditions

# 查看节点污点
kubectl get nodes -o custom-columns=NAME:.metadata.name,TAINTS:.spec.taints
```

---

**基本用法:查看组件日志**
`kubectl logs -n kube-system <组件>`

```bash
# 查看 API Server 日志
kubectl logs -n kube-system kube-apiserver-node-1

# 查看 Controller Manager 日志
kubectl logs -n kube-system kube-controller-manager-node-1

# 查看 Scheduler 日志
kubectl logs -n kube-system kube-scheduler-node-1

# 查看 kubelet 日志(在节点上执行)
journalctl -u kubelet -f --tail=50

# 查看容器运行时日志
journalctl -u containerd -f --tail=50
```

---

**基本用法:查看 etcd 状态**
`kubectl get pods -n kube-system -l component=etcd`

```bash
# 查看 etcd Pod
kubectl get pods -n kube-system -l component=etcd

# 查看 etcd 日志
kubectl logs -n kube-system etcd-node-1 --tail=50

# 在节点上检查 etcd 健康(静态 Pod)
ssh node-1
crictl ps | grep etcd
crictl logs $(crictl ps -q --name etcd) | tail -20

# etcdctl 检查集群状态
ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  endpoint status -w table
```

---

## 证书与认证排查

**基本用法:检查证书过期**
`openssl x509 -in <证书> -noout -dates`

```bash
# 检查 API Server 证书过期时间
openssl x509 -in /etc/kubernetes/pki/apiserver.crt -noout -dates

# 检查所有 K8s 证书过期
for cert in /etc/kubernetes/pki/*.crt; do
  echo "$cert:"
  openssl x509 -in $cert -noout -enddate
done

# 使用 kubeadm 检查证书过期
kubeadm certs check-expiration

# 在 Pod 中检查证书
kubectl exec -it web-xxx -- openssl s_client -connect kubernetes:443 -showcerts
```

---

**基本用法:RBAC 权限排查**
`kubectl auth can-i`

```bash
# 检查当前用户权限
kubectl auth can-i create pods -n production

# 检查指定用户权限
kubectl auth can-i delete pods --as=alice -n production

# 检查 ServiceAccount 权限
kubectl auth can-i get secrets --as=system:serviceaccount:production:app-sa -n production

# 列出所有权限
kubectl auth can-i --list -n production

# 查看角色绑定
kubectl get rolebindings,clusterrolebindings -A -o wide
```

---

## 性能与资源排查

**基本用法:查看资源配额**
`kubectl get resourcequota|limitrange`

```bash
# 查看命名空间资源配额
kubectl get resourcequota -n production

# 查看配额详情
kubectl describe resourcequota -n production

# 查看 LimitRange
kubectl get limitrange -n production
kubectl describe limitrange -n production

# 查看 Pod 资源限制
kubectl get pod web-xxx -n production -o jsonpath='{.spec.containers[*].resources}'
```

---

**基本用法:查看节点压力**
`kubectl describe node`

```bash
# 查看节点压力状况
kubectl describe node node-1 | grep -A 10 Conditions

# 查看节点内存压力
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.conditions[?(@.type=="MemoryPressure")].status}{"\n"}{end}'

# 查看磁盘压力
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.conditions[?(@.type=="DiskPressure")].status}{"\n"}{end}'

# 查看节点 PID 压力
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.conditions[?(@.type=="PIDPressure")].status}{"\n"}{end}'
```

---

## 镜像与拉取排查

**基本用法:查看镜像拉取失败**
`kubectl describe pod`

```bash
# 查看镜像拉取失败原因
kubectl describe pod web-xxx -n production | grep -A 10 Events

# 常见错误
# ErrImagePull: 镜像拉取失败(镜像名错误/不存在)
# ImagePullBackOff: 拉取失败后重试退避
# RegistryUnavailable: 仓库不可达

# 查看镜像名称
kubectl get pod web-xxx -n production -o jsonpath='{.spec.containers[*].image}'

# 查看 imagePullSecrets
kubectl get pod web-xxx -n production -o jsonpath='{.spec.imagePullSecrets}'
```

---

**基本用法:配置 imagePullSecrets**
`kubectl create secret docker-registry`

```bash
# 创建镜像拉取凭据
kubectl create secret docker-registry regcred \
  --docker-server=registry.example.com \
  --docker-username=admin \
  --docker-password=secret \
  --docker-email=admin@example.com \
  -n production

# 在 Pod 中使用
kubectl patch serviceaccount default \
  -p '{"imagePullSecrets":[{"name":"regcred"}]}' \
  -n production

# 查看 Secret
kubectl get secret regcred -n production -o jsonpath='{.data.\.dockerconfigjson}' | base64 -d
```

---

## 集群信息收集

**基本用法:收集集群信息**
`kubectl cluster-info dump`

```bash
# 集群信息
kubectl cluster-info

# 集群详细信息
kubectl cluster-info dump --output-directory=/tmp/cluster-dump

# 收集特定命名空间信息
kubectl cluster-info dump --namespaces=production,kube-system \
  --output-directory=/tmp/dump

# 使用 kubectl-debug 插件
kubectl debug-node node-1
```

---

**基本用法:导出资源清单**
`kubectl get <资源> -o yaml`

```bash
# 导出所有 Deployment
kubectl get deployments -A -o yaml > all-deployments.yaml

# 导出指定命名空间所有资源
kubectl get all -n production -o yaml > production-resources.yaml

# 导出资源清单(删除集群特定字段)
kubectl get deployment web -n production -o yaml | \
  kubectl neat > web-deployment.yaml

# 导出带标签的资源
kubectl get all -l app=web -n production -o yaml > web-resources.yaml
```

---

## 常见问题快速诊断

**基本用法:CrashLoopBackOff 排查**
`kubectl logs --previous`

```bash
# 查看崩溃前的日志
kubectl logs web-xxx --previous -n production

# 查看退出码
kubectl get pod web-xxx -n production -o jsonpath='{.status.containerStatuses[0].lastState}'

# 检查存活探针配置(可能是探针太严格)
kubectl get pod web-xxx -n production -o jsonpath='{.spec.containers[0].livenessProbe}'

# 检查资源限制(可能是 OOM)
kubectl describe pod web-xxx -n production | grep -A 5 "Last State"
```

---

**基本用法:OOMKilled 排查**
`kubectl describe pod`

```bash
# 查看是否 OOM
kubectl get pod web-xxx -n production -o jsonpath='{.status.containerStatuses[0].lastState.terminated.reason}'

# 查看内存限制
kubectl get pod web-xxx -n production -o jsonpath='{.spec.containers[0].resources.limits.memory}'

# 查看内存使用情况
kubectl top pod web-xxx -n production --containers

# 查看节点内存
kubectl describe node node-1 | grep -A 5 "Memory Pressure"
```

---

**基本用法:节点 NotReady 排查**
`kubectl describe node`

```bash
# 查看节点状态
kubectl describe node node-1 | grep -A 10 Conditions

# 检查 kubelet 状态(SSH 到节点)
ssh node-1
systemctl status kubelet

# 检查 kubelet 日志
journalctl -u kubelet --since "10 minutes ago" | tail -50

# 检查容器运行时
systemctl status containerd
crictl ps -a | head
```
