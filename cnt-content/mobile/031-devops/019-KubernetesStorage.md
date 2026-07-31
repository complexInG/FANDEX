# Kubernetes 持久化存储速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## PersistentVolume 持久卷

**基本用法:查看持久卷**
`kubectl get pv [名称]`

```bash
# 列出所有 PV
kubectl get pv

# 查看 PV 详情
kubectl describe pv pv-001

# 按容量排序
kubectl get pv --sort-by=.spec.capacity.storage
```

---

**基本用法:静态创建 PV**
`kubectl apply -f <pv.yaml>`

```yaml
# pv.yaml 静态持久卷示例
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-nfs-001
  labels:
    type: nfs
spec:
  capacity:
    storage: 20Gi
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Retain
  nfs:
    server: 192.168.1.100
    path: /data/nfs/share
```

---

**基本用法:回收策略**
`persistentVolumeReclaimPolicy: <Retain|Delete|Recycle>`

```bash
# Retain:删除 PVC 后 PV 保留数据,需手动回收
# Delete:删除 PVC 后自动删除 PV 和后端存储(动态供应默认)
# Recycle:已废弃,仅保留兼容

# 修改已有 PV 回收策略
kubectl patch pv pv-001 -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
```

---

## PersistentVolumeClaim 持久卷声明

**基本用法:查看 PVC**
`kubectl get pvc [名称] -n <命名空间>`

```bash
# 列出当前命名空间 PVC
kubectl get pvc

# 列出指定命名空间 PVC
kubectl get pvc -n production

# 查看 PVC 详情(包含绑定状态)
kubectl describe pvc data-pvc -n production
```

---

**基本用法:创建 PVC**
`kubectl apply -f <pvc.yaml>`

```yaml
# pvc.yaml 持久卷声明示例
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data-pvc
  namespace: production
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: standard
  resources:
    requests:
      storage: 10Gi
```

---

**基本用法:访问模式**
`accessModes: <模式>`

```bash
# ReadWriteOnce (RWO):单节点读写
# ReadOnlyMany (ROX):多节点只读
# ReadWriteMany (RWX):多节点读写
# ReadWriteOncePod (RWOP):单 Pod 读写(K8s 1.22+)

# 查看支持访问模式的 PV
kubectl get pv -o custom-columns=NAME:.metadata.name,ACCESS:.spec.accessModes
```

---

**基本用法:扩容 PVC**
`kubectl patch pvc <名称> -p '{"spec":{"resources":{"requests":{"storage":"<大小>"}}}}'`

```bash
# 在线扩容 PVC(需 StorageClass 允许扩容)
kubectl patch pvc data-pvc -p '{"spec":{"resources":{"requests":{"storage":"50Gi"}}}}'

# 查看扩容状态
kubectl get pvc data-pvc -w
```

---

## StorageClass 存储类

**基本用法:查看 StorageClass**
`kubectl get sc [名称]`

```bash
# 列出所有 StorageClass
kubectl get sc

# 查看默认 StorageClass(带 default 标识)
kubectl get sc

# 查看 StorageClass 详情
kubectl describe sc standard
```

---

**基本用法:创建 StorageClass**
`kubectl apply -f <sc.yaml>`

```yaml
# sc.yaml 动态供应存储类示例
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: kubernetes.io/aws-ebs
reclaimPolicy: Delete
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
parameters:
  type: gp3
  fsType: ext4
```

---

**基本用法:设置默认 StorageClass**
`kubectl patch sc <名称> -p '{"metadata":{"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'`

```bash
# 设置为默认 StorageClass
kubectl patch sc fast-ssd -p '{"metadata":{"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

# 取消默认标记
kubectl patch sc fast-ssd -p '{"metadata":{"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
```

---

## 在 Pod 中使用存储

**基本用法:Pod 挂载 PVC**
`volumes: - persistentVolumeClaim`

```yaml
# pod-pvc.yaml Pod 使用 PVC 示例
apiVersion: v1
kind: Pod
metadata:
  name: app-with-storage
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: data
      mountPath: /usr/share/nginx/html
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: data-pvc
```

---

**基本用法:Deployment 使用 PVC**
`spec.template.spec.volumes`

```yaml
# deployment-pvc.yaml Deployment 持久化示例
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
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
        image: nginx
        volumeMounts:
        - name: html
          mountPath: /usr/share/nginx/html
      volumes:
      - name: html
        persistentVolumeClaim:
          claimName: shared-html
```

---

## 临时卷与配置卷

**基本用法:emptyDir 临时目录**
`volumes: - emptyDir: {}`

```yaml
# 同一 Pod 内容器共享临时目录
apiVersion: v1
kind: Pod
metadata:
  name: worker
spec:
  containers:
  - name: generator
    image: busybox
    command: ["sh", "-c", "while true; do echo $(date) > /data/log; sleep 5; done"]
    volumeMounts:
    - name: shared
      mountPath: /data
  - name: consumer
    image: busybox
    command: ["sh", "-c", "tail -f /data/log"]
    volumeMounts:
    - name: shared
      mountPath: /data
  volumes:
  - name: shared
    emptyDir: {}
```

---

**基本用法:hostPath 挂载宿主机路径**
`volumes: - hostPath`

```yaml
# 挂载宿主机文件到容器(谨慎使用)
apiVersion: v1
kind: Pod
metadata:
  name: node-inspector
spec:
  containers:
  - name: inspector
    image: alpine
    volumeMounts:
    - name: docker-sock
      mountPath: /var/run/docker.sock
  volumes:
  - name: docker-sock
    hostPath:
      path: /var/run/docker.sock
      type: Socket
```

---

**基本用法:ConfigMap 作为卷挂载**
`volumes: - configMap`

```bash
# 创建 ConfigMap
kubectl create configmap app-config --from-file=config.yaml

# 在 Pod 中挂载 ConfigMap
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: config-app
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: config
      mountPath: /etc/config
  volumes:
  - name: config
    configMap:
      name: app-config
EOF
```

---

## StatefulSet 持久化

**基本用法:StatefulSet 使用 volumeClaimTemplates**
`spec.volumeClaimTemplates`

```yaml
# statefulset.yaml 有状态应用持久化示例
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
spec:
  serviceName: mysql
  replicas: 3
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql
        image: mysql:8
        volumeMounts:
        - name: data
          mountPath: /var/lib/mysql
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      storageClassName: standard
      resources:
        requests:
          storage: 20Gi
```

---

**基本用法:查看 StatefulSet 的 PVC**
`kubectl get pvc -l app=<标签>`

```bash
# 查看 StatefulSet 自动创建的 PVC
kubectl get pvc -l app=mysql

# 查看 PVC 绑定的 Pod
kubectl get pvc -o custom-columns=NAME:.metadata.name,STATUS:.status.phase,BOUND:.spec.volumeName
```

---

## 存储快照

**基本用法:创建 VolumeSnapshot**
`kubectl apply -f <snapshot.yaml>`

```yaml
# snapshot.yaml 存储快照示例
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: data-snapshot
spec:
  volumeSnapshotClassName: csi-snapclass
  source:
    persistentVolumeClaimName: data-pvc
```

---

**基本用法:查看快照**
`kubectl get volumesnapshot [名称]`

```bash
# 列出所有快照
kubectl get volumesnapshot

# 查看快照详情
kubectl describe volumesnapshot data-snapshot

# 从快照恢复 PVC
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: restored-pvc
spec:
  accessModes: ["ReadWriteOnce"]
  storageClassName: standard
  resources:
    requests:
      storage: 10Gi
  dataSource:
    name: data-snapshot
    kind: VolumeSnapshot
    apiGroup: snapshot.storage.k8s.io
EOF
```

---

## CSI 驱动管理

**基本用法:查看 CSI 驱动**
`kubectl get csidriver`

```bash
# 列出集群 CSI 驱动
kubectl get csidriver

# 查看 CSI 节点信息
kubectl get csinode

# 查看 CSI 驱动详情
kubectl describe csidriver ebs.csi.aws.com
```

---

**基本用法:查看存储节点**
`kubectl get csinode <节点名>`

```bash
# 查看节点的 CSI 驱动状态
kubectl get csinode

# 查看节点可用的存储拓扑
kubectl get csinode node-01 -o yaml
```

---

## 存储清理与排查

**基本用法:删除 PVC**
`kubectl delete pvc <名称> -n <命名空间>`

```bash
# 删除 PVC(若回收策略为 Retain,PV 数据保留)
kubectl delete pvc data-pvc -n production

# 强制删除卡住的 PVC
kubectl patch pvc data-pvc -p '{"metadata":{"finalizers":null}}' -n production
```

---

**基本用法:强制删除卡住的 PV**
`kubectl patch pv <名称> -p '{"spec":{"claimRef":null}}'`

```bash
# 清除 PV 的 claimRef 引用
kubectl patch pv pv-001 -p '{"spec":{"claimRef":null}}'

# 删除卡在 Terminating 的 PV
kubectl patch pv pv-001 -p '{"metadata":{"finalizers":null}}'
```

---

**基本用法:检查 Pod 卷挂载状态**
`kubectl describe pod <名称> | grep -A 20 Volumes`

```bash
# 查看卷挂载详情
kubectl describe pod app-pod | grep -A 30 Volumes

# 查看挂载到节点的卷
kubectl debug node/<节点名> -it --image=busybox -- ls /var/lib/kubelet/pods
```
