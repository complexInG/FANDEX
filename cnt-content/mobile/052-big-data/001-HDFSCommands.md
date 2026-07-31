# 大数据 HDFS 命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 文件系统操作

**基本写法：查看目录内容**
`hdfs dfs -ls [<路径>]`

```bash
# 查看 HDFS 根目录
hdfs dfs -ls /
# 查看指定目录
hdfs dfs -ls /user/hadoop
```

---

**基本写法：递归查看目录**
`hdfs dfs -ls -R <路径>`

```bash
# 递归查看目录树
hdfs dfs -ls -R /user
```

---

**基本写法：查看文件内容**
`hdfs dfs -cat <文件路径>`

```bash
# 查看 HDFS 文件内容
hdfs dfs -cat /user/hadoop/input.txt
```

---

**基本写法：分页查看文件**
`hdfs dfs -cat <文件路径> | more`

```bash
# 分页查看大文件
hdfs dfs -cat /user/hadoop/large.log | more
```

---

**基本写法：查看文件末尾**
`hdfs dfs -tail <文件路径>`

```bash
# 查看文件末尾 1KB 内容
hdfs dfs -tail /user/hadoop/log.txt
```

---

## 目录操作

**基本写法：创建目录**
`hdfs dfs -mkdir <路径>`

```bash
# 创建目录
hdfs dfs -mkdir /user/hadoop/data
```

---

**基本写法：递归创建目录**
`hdfs dfs -mkdir -p <路径>`

```bash
# 递归创建多级目录
hdfs dfs -mkdir -p /user/hadoop/data/2024/01
```

---

**基本写法：删除目录**
`hdfs dfs -rm -r <路径>`

```bash
# 递归删除目录
hdfs dfs -rm -r /user/hadoop/temp
```

---

**基本写法：强制删除**
`hdfs dfs -rm -r -f <路径>`

```bash
# 强制删除（不提示确认）
hdfs dfs -rm -r -f /user/hadoop/temp
```

---

**基本写法：删除空目录**
`hdfs dfs -rmdir <路径>`

```bash
# 删除空目录
hdfs dfs -rmdir /user/hadoop/empty_dir
```

---

## 文件上传下载

**基本写法：上传文件到 HDFS**
`hdfs dfs -put <本地路径> <HDFS路径>`

```bash
# 上传本地文件到 HDFS
hdfs dfs -put localfile.txt /user/hadoop/
```

---

**基本写法：上传多个文件**
`hdfs dfs -put <文件1> <文件2> <HDFS目录>`

```bash
# 上传多个文件到 HDFS 目录
hdfs dfs -put file1.txt file2.txt /user/hadoop/data/
```

---

**基本写法：使用 copyFromLocal**
`hdfs dfs -copyFromLocal <本地路径> <HDFS路径>`

```bash
# 等同于 put，上传本地文件
hdfs dfs -copyFromLocal localfile.csv /user/hadoop/
```

---

**基本写法：下载文件**
`hdfs dfs -get <HDFS路径> <本地路径>`

```bash
# 从 HDFS 下载文件到本地
hdfs dfs -get /user/hadoop/output.txt ./
```

---

**基本写法：使用 copyToLocal**
`hdfs dfs -copyToLocal <HDFS路径> <本地路径>`

```bash
# 等同于 get，下载到本地
hdfs dfs -copyToLocal /user/hadoop/result.csv ./
```

---

**基本写法：合并下载**
`hdfs dfs -getmerge <HDFS目录> <本地文件>`

```bash
# 合并 HDFS 目录下所有文件并下载
hdfs dfs -getmerge /user/hadoop/output/ merged.txt
```

---

## 文件复制移动

**基本写法：HDFS 内复制**
`hdfs dfs -cp <源路径> <目标路径>`

```bash
# 在 HDFS 内复制文件
hdfs dfs -cp /user/hadoop/file.txt /user/hadoop/backup/
```

---

**基本写法：递归复制**
`hdfs dfs -cp -r <源目录> <目标目录>`

```bash
# 递归复制目录
hdfs dfs -cp -r /user/hadoop/data /user/hadoop/backup
```

---

**基本写法：HDFS 内移动**
`hdfs dfs -mv <源路径> <目标路径>`

```bash
# 在 HDFS 内移动或重命名
hdfs dfs -mv /user/hadoop/old.txt /user/hadoop/new.txt
```

---

## 权限管理

**基本写法：修改权限**
`hdfs dfs -chmod <权限模式> <路径>`

```bash
# 修改文件权限
hdfs dfs -chmod 755 /user/hadoop/file.txt
```

---

**基本写法：递归修改权限**
`hdfs dfs -chmod -R <权限模式> <路径>`

```bash
# 递归修改目录权限
hdfs dfs -chmod -R 750 /user/hadoop/data
```

---

**基本写法：修改所有者**
`hdfs dfs -chown <用户>:<组> <路径>`

```bash
# 修改文件所有者
hdfs dfs -chown hadoop:hadoop /user/hadoop/file.txt
```

---

**基本写法：递归修改所有者**
`hdfs dfs -chown -R <用户>:<组> <路径>`

```bash
# 递归修改目录所有者
hdfs dfs -chown -R hadoop:hadoop /user/hadoop/data
```

---

**基本写法：修改所属组**
`hdfs dfs -chgrp <组> <路径>`

```bash
# 修改文件所属组
hdfs dfs -chgrp hadoop /user/hadoop/file.txt
```

---

## 文件信息

**基本写法：查看文件大小**
`hdfs dfs -du <路径>`

```bash
# 查看目录下各文件大小
hdfs dfs -du /user/hadoop
```

---

**基本写法：查看汇总大小**
`hdfs dfs -du -s <路径>`

```bash
# 查看目录总大小
hdfs dfs -du -s /user/hadoop/data
```

---

**基本写法：人类可读格式**
`hdfs dfs -du -h <路径>`

```bash
# 以人类可读格式显示大小
hdfs dfs -du -h /user/hadoop
```

---

**基本写法：查看磁盘使用情况**
`hdfs dfs -df [<路径>]`

```bash
# 查看 HDFS 磁盘使用情况
hdfs dfs -df -h
```

---

**基本写法：统计文件数和大小**
`hdfs dfs -count <路径>`

```bash
# 统计目录下的文件数和大小
hdfs dfs -count /user/hadoop
```

---

## 文件校验

**基本写法：查看文件校验和**
`hdfs dfs -checksum <文件路径>`

```bash
# 查看 HDFS 文件的校验和
hdfs dfs -checksum /user/hadoop/file.txt
```

---

**基本写法：测试文件**
`hdfs dfs -test -[ezd] <路径>`

```bash
# 测试文件是否存在
hdfs dfs -test -e /user/hadoop/file.txt
# 测试是否为空文件
hdfs dfs -test -z /user/hadoop/file.txt
# 测试是否为目录
hdfs dfs -test -d /user/hadoop/data
```

---

## 集群管理

**基本写法：查看文件系统状态**
`hdfs fsck <路径>`

```bash
# 检查 HDFS 文件系统健康状况
hdfs fsck /
# 检查指定目录
hdfs fsck /user/hadoop -files -blocks
```

---

**基本写法：查看 NameNode 状态**
`hdfs dfsadmin -report`

```bash
# 查看 HDFS 集群报告
hdfs dfsadmin -report
```

---

**基本写法：安全模式操作**
`hdfs dfsadmin -safemode <命令>`

```bash
# 查看安全模式状态
hdfs dfsadmin -safemode get
# 进入安全模式
hdfs dfsadmin -safemode enter
# 退出安全模式
hdfs dfsadmin -safemode leave
```

---

**基本写法：刷新节点**
`hdfs dfsadmin -refreshNodes`

```bash
# 刷新 DataNode 列表（用于节点上线/下线）
hdfs dfsadmin -refreshNodes
```

---

**基本写法：设置配额**
`hdfs dfsadmin -setQuota <数量> <目录>`

```bash
# 设置目录文件数配额
hdfs dfsadmin -setQuota 1000 /user/hadoop/data
```

---

**基本写法：设置空间配额**
`hdfs dfsadmin -setSpaceQuota <大小> <目录>`

```bash
# 设置目录空间配额
hdfs dfsadmin -setSpaceQuota 1T /user/hadoop/data
```

---

## 快照管理

**基本写法：允许快照**
`hdfs dfsadmin -allowSnapshot <路径>`

```bash
# 允许目录创建快照
hdfs dfsadmin -allowSnapshot /user/hadoop/data
```

---

**基本写法：创建快照**
`hdfs dfs -createSnapshot <路径> [<快照名>]`

```bash
# 创建快照
hdfs dfs -createSnapshot /user/hadoop/data snapshot_20240101
```

---

**基本写法：删除快照**
`hdfs dfs -deleteSnapshot <路径> <快照名>`

```bash
# 删除快照
hdfs dfs -deleteSnapshot /user/hadoop/data snapshot_20240101
```
