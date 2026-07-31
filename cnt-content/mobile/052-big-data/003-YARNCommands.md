# 大数据 YARN 命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 应用管理

**基本写法：查看运行中的应用**
`yarn application -list`

```bash
# 查看所有运行中的 YARN 应用
yarn application -list
```

---

**基本写法：按状态过滤应用**
`yarn application -list -appStates <状态>`

```bash
# 查看所有状态的应用
yarn application -list -appStates ALL
# 查看已完成的应用
yarn application -list -appStates FINISHED
```

---

**基本写法：查看应用详情**
`yarn application -status <应用ID>`

```bash
# 查看指定应用的详细信息
yarn application -status application_1234567890_0001
```

---

**基本写法：杀死应用**
`yarn application -kill <应用ID>`

```bash
# 终止指定的 YARN 应用
yarn application -kill application_1234567890_0001
```

---

**基本写法：查看应用尝试**
`yarn applicationattempt -list <应用ID>`

```bash
# 查看应用的所有尝试记录
yarn applicationattempt -list application_1234567890_0001
```

---

**基本写法：查看应用尝试状态**
`yarn applicationattempt -status <尝试ID>`

```bash
# 查看应用尝试的详细信息
yarn applicationattempt -status appattempt_1234567890_0001_000001
```

---

## 节点管理

**基本写法：查看所有节点**
`yarn node -list`

```bash
# 查看集群所有节点
yarn node -list
```

---

**基本写法：查看节点状态**
`yarn node -status <节点ID>`

```bash
# 查看指定节点详细信息
yarn node -status node1:8041
```

---

**基本写法：查看所有节点状态**
`yarn node -list -showDetails`

```bash
# 查看所有节点的详细信息
yarn node -list -showDetails
```

---

## Container 管理

**基本写法：查看应用的 Container**
`yarn container -list <应用尝试ID>`

```bash
# 查看应用尝试的所有 Container
yarn container -list appattempt_1234567890_0001_000001
```

---

**基本写法：查看 Container 状态**
`yarn container -status <Container ID>`

```bash
# 查看指定 Container 状态
yarn container -status container_1234567890_0001_01_000001
```

---

## 队列管理

**基本写法：查看队列列表**
`yarn queue -status <队列名>`

```bash
# 查看指定队列状态
yarn queue -status default
```

---

**基本写法：查看所有队列**
`yarn queue -list`

```bash
# 查看所有队列
yarn queue -list
```

---

**基本写法：停止队列**
`yarn queue -stop <队列名>`

```bash
# 停止指定队列
yarn queue -stop my_queue
```

---

**基本写法：启动队列**
`yarn queue -start <队列名>`

```bash
# 启动指定队列
yarn queue -start my_queue
```

---

## 日志管理

**基本写法：查看应用日志**
`yarn logs -applicationId <应用ID>`

```bash
# 查看指定应用的日志
yarn logs -applicationId application_1234567890_0001
```

---

**基本写法：查看指定 Container 日志**
`yarn logs -applicationId <应用ID> -containerId <Container ID>`

```bash
# 查看指定 Container 的日志
yarn logs -applicationId application_1234567890_0001 \
    -containerId container_1234567890_0001_01_000001
```

---

**基本写法：下载日志**
`yarn logs -applicationId <应用ID> -out <输出路径>`

```bash
# 下载应用日志到本地
yarn logs -applicationId application_1234567890_0001 -out ./app_logs
```

---

**基本写法：查看日志末尾**
`yarn logs -applicationId <应用ID> -logFiles <日志文件> -size <字节数>`

```bash
# 查看日志末尾指定大小
yarn logs -applicationId application_1234567890_0001 -logFiles stderr -size 1024
```

---

**基本写法：显示所有日志文件**
`yarn logs -applicationId <应用ID> -showApplicationLogInfo`

```bash
# 显示应用所有日志文件列表
yarn logs -applicationId application_1234567890_0001 -showApplicationLogInfo
```

---

## 集群信息

**基本写法：查看集群信息**
`yarn cluster -list`

```bash
# 查看集群节点列表
yarn cluster -list
```

---

**基本写法：查看集群拓扑**
`yarn cluster -nodes`

```bash
# 查看集群节点状态
yarn cluster -nodes
```

---

## ResourceManager 管理

**基本写法：刷新队列**
`yarn rmadmin -refreshQueues`

```bash
# 刷新队列配置
yarn rmadmin -refreshQueues
```

---

**基本写法：刷新节点**
`yarn rmadmin -refreshNodes`

```bash
# 刷新节点列表（用于节点上线/下线）
yarn rmadmin -refreshNodes
```

---

**基本写法：刷新用户**
`yarn rmadmin -refreshUserToGroupsMappings`

```bash
# 刷新用户到组的映射
yarn rmadmin -refreshUserToGroupsMappings
```

---

**基本写法：刷新超级用户代理**
`yarn rmadmin -refreshSuperUserGroupsConfiguration`

```bash
# 刷新超级用户组配置
yarn rmadmin -refreshSuperUserGroupsConfiguration
```

---

**基本写法：更新管理员 ACL**
`yarn rmadmin -refreshAdminAcls`

```bash
# 更新管理员访问控制列表
yarn rmadmin -refreshAdminAcls
```

---

## 服务管理

**基本写法：启动 ResourceManager**
`yarn --daemon start resourcemanager`

```bash
# 启动 ResourceManager
yarn --daemon start resourcemanager
```

---

**基本写法：启动 NodeManager**
`yarn --daemon start nodemanager`

```bash
# 启动 NodeManager
yarn --daemon start nodemanager
```

---

**基本写法：停止服务**
`yarn --daemon stop <服务名>`

```bash
# 停止 ResourceManager
yarn --daemon stop resourcemanager
# 停止 NodeManager
yarn --daemon stop nodemanager
```

---

**基本写法：启动所有服务**
`start-yarn.sh`

```bash
# 启动所有 YARN 服务
start-yarn.sh
```

---

**基本写法：停止所有服务**
`stop-yarn.sh`

```bash
# 停止所有 YARN 服务
stop-yarn.sh
```

---

## 资源配置

**基本写法：查看调度器配置**
`yarn scheduler -list`

```bash
# 查看调度器信息
yarn scheduler -list
```

---

**基本写法：查看队列资源使用**
`yarn queue -status <队列名>`

```bash
# 查看 default 队列资源使用情况
yarn queue -status default
```

---

## 共享缓存

**基本写法：查看共享缓存**
`yarn sharedcachemeta -list`

```bash
# 查看共享缓存元数据
yarn sharedcachemeta -list
```

---

**基本写法：查看缓存资源**
`yarn sharedcachemeta -entry <资源键>`

```bash
# 查看指定缓存资源
yarn sharedcachemeta -entry my_resource
```
