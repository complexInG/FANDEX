# 大数据 ZooKeeper 命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 连接 ZooKeeper

**基本写法：连接本地 ZooKeeper**
`zkCli.sh`

```bash
# 连接本地 ZooKeeper（默认端口 2181）
zkCli.sh
```

---

**基本写法：连接远程 ZooKeeper**
`zkCli.sh -server <主机>:<端口>`

```bash
# 连接远程 ZooKeeper
zkCli.sh -server namenode:2181
```

---

**基本写法：带超时连接**
`zkCli.sh -server <主机>:<端口> -timeout <毫秒>`

```bash
# 带 5 秒超时连接
zkCli.sh -server namenode:2181 -timeout 5000
```

---

## 节点操作

**基本写法：创建持久节点**
`create <路径> <数据>`

```bash
# 创建持久节点
create /myapp "my application"
```

---

**基本写法：创建临时节点**
`create -e <路径> <数据>`

```bash
# 创建临时节点（会话断开自动删除）
create -e /myapp/temp "temporary data"
```

---

**基本写法：创建顺序节点**
`create -s <路径> <数据>`

```bash
# 创建顺序节点（自动追加递增序号）
create -s /myapp/node "sequential data"
```

---

**基本写法：创建临时顺序节点**
`create -e -s <路径> <数据>`

```bash
# 创建临时顺序节点
create -e -s /myapp/lock "lock data"
```

---

**基本写法：创建带 TTL 的节点**
`create -t <毫秒> <路径> <数据>`

```bash
# 创建带 TTL 的节点（3.5+ 版本）
create -t 60000 /myapp/ttl "ttl data"
```

---

**基本写法：创建容器节点**
`create -c <路径> <数据>`

```bash
# 创建容器节点（子节点为空时自动删除）
create -c /myapp/container "container"
```

---

## 读取数据

**基本写法：列出子节点**
`ls <路径>`

```bash
# 列出根节点的子节点
ls /
# 列出指定节点的子节点
ls /myapp
```

---

**基本写法：递归列出**
`ls -R <路径>`

```bash
# 递归列出所有子节点
ls -R /myapp
```

---

**基本写法：获取节点数据**
`get <路径>`

```bash
# 获取节点数据和元信息
get /myapp
```

---

**基本写法：获取节点状态**
`stat <路径>`

```bash
# 获取节点状态信息
stat /myapp
```

---

**基本写法：仅获取数据**
`get -s <路径>`

```bash
# 获取数据和状态
get -s /myapp
```

---

## 更新数据

**基本写法：设置节点数据**
`set <路径> <新数据>`

```bash
# 更新节点数据
set /myapp "updated data"
```

---

**基本写法：带版本设置**
`set <路径> <新数据> <版本号>`

```bash
# 乐观锁更新（版本号需匹配）
set /myapp "versioned data" 2
```

---

## 删除节点

**基本写法：删除节点**
`delete <路径>`

```bash
# 删除节点（节点必须无子节点）
delete /myapp/temp
```

---

**基本写法：带版本删除**
`delete <路径> <版本号>`

```bash
# 带版本号删除
delete /myapp 3
```

---

**基本写法：递归删除**
`deleteall <路径>`

```bash
# 递归删除节点及其所有子节点
deleteall /myapp
```

---

## 监视器

**基本写法：监视节点数据变化**
`get -w <路径>`

```bash
# 设置数据变化监视器
get -w /myapp
```

---

**基本写法：监视子节点变化**
`ls -w <路径>`

```bash
# 设置子节点变化监视器
ls -w /myapp
```

---

**基本写法：监视节点状态**
`stat -w <路径>`

```bash
# 设置节点存在性监视器
stat -w /myapp
```

---

**基本写法：查看监视器**
`printwatches`

```bash
# 查看当前设置的监视器
printwatches on
```

---

## ACL 权限

**基本写法：查看 ACL**
`getAcl <路径>`

```bash
# 查看节点 ACL
getAcl /myapp
```

---

**基本写法：设置 ACL**
`setAcl <路径> <权限>`

```bash
# 设置 ACL（world 所有用户可读）
setAcl /myapp world:anyone:r
```

---

**基本写法：设置认证 ACL**
`setAcl <路径> auth:<用户>:<权限>`

```bash
# 设置认证用户权限
setAcl /myapp auth:user1:rw
```

---

**基本写法：设置 IP ACL**
`setAcl <路径> ip:<IP>:<权限>`

```bash
# 设置 IP 权限
setAcl /myapp ip:192.168.1.100:rw
```

---

**基本写法：添加认证**
`addauth <方案> <认证信息>`

```bash
# 添加 digest 认证
addauth digest username:password
```

---

## 配额管理

**基本写法：设置节点配额**
`setquota -n <数量> <路径>`

```bash
# 设置子节点数量配额
setquota -n 100 /myapp
```

---

**基本写法：设置字节配额**
`setquota -b <字节> <路径>`

```bash
# 设置数据大小配额
setquota -b 1048576 /myapp
```

---

**基本写法：查看配额**
`listquota <路径>`

```bash
# 查看节点配额
listquota /myapp
```

---

**基本写法：删除配额**
`delquota [-n|-b] <路径>`

```bash
# 删除数量配额
delquota -n /myapp
# 删除字节配额
delquota -b /myapp
```

---

## 集群管理

**基本写法：查看集群状态**
`zkServer.sh status`

```bash
# 查看 ZooKeeper 服务器状态
zkServer.sh status
```

---

**基本写法：启动服务器**
`zkServer.sh start`

```bash
# 启动 ZooKeeper 服务器
zkServer.sh start
```

---

**基本写法：停止服务器**
`zkServer.sh stop`

```bash
# 停止 ZooKeeper 服务器
zkServer.sh stop
```

---

**基本写法：重启服务器**
`zkServer.sh restart`

```bash
# 重启 ZooKeeper 服务器
zkServer.sh restart
```

---

**基本写法：前台启动**
`zkServer.sh start-foreground`

```bash
# 前台启动（查看日志）
zkServer.sh start-foreground
```

---

## 四字命令

**基本写法：查看状态**
`echo stat | nc <主机> <端口>`

```bash
# 查看服务器状态
echo stat | nc localhost 2181
```

---

**基本写法：查看环境**
`echo envi | nc <主机> <端口>`

```bash
# 查看环境变量
echo envi | nc localhost 2181
```

---

**基本写法：查看监视**
`echo wchs | nc <主机> <端口>`

```bash
# 查看监视器详情
echo wchs | nc localhost 2181
```

---

**基本写法：查看监视详情**
`echo wchc | nc <主机> <端口>`

```bash
# 查看监视器按会话分组
echo wchc | nc localhost 2181
```

---

**基本写法：查看连接**
`echo cons | nc <主机> <端口>`

```bash
# 查看客户端连接
echo cons | nc localhost 2181
```

---

**基本写法：查看配置**
`echo conf | nc <主机> <端口>`

```bash
# 查看服务器配置
echo conf | nc localhost 2181
```

---

**基本写法：查看健康状态**
`echo ruok | nc <主机> <端口>`

```bash
# 查看服务器是否正常（返回 imok）
echo ruok | nc localhost 2181
```

---

**基本写法：查看路径**
`echo dump | nc <主机> <端口>`

```bash
# 查看会话和临时节点
echo dump | nc localhost 2181
```

---

**基本写法：查看统计**
`echo srvr | nc <主机> <端口>`

```bash
# 查看服务器统计信息
echo srvr | nc localhost 2181
```

---

## 其他命令

**基本写法：同步节点**
`sync <路径>`

```bash
# 强制同步节点数据
sync /myapp
```

---

**基本写法：移除监视器**
`removewatches <路径>`

```bash
# 移除指定路径的监视器
removewatches /myapp
```

---

**基本写法：关闭连接**
`close`

```bash
# 关闭当前连接
close
```

---

**基本写法：退出**
`quit`

```bash
# 退出 ZooKeeper 客户端
quit
```

---

**基本写法：查看历史命令**
`history`

```bash
# 查看历史命令
history
```

---

**基本写法：重新执行命令**
`redo <编号>`

```bash
# 重新执行编号为 10 的命令
redo 10
```
