# C 共享内存与信号量

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## System V 共享内存

**基本写法：创建共享内存**
`shmget(<键>, <大小>, IPC_CREAT | 0666);`
```c
// 创建共享内存段
int shmid = shmget(IPC_PRIVATE, 4096, IPC_CREAT | 0666);
```

---

**基本写法：附加共享内存**
`shmat(<shmid>, NULL, 0);`
```c
// 将共享内存映射到进程地址空间
void* addr = shmat(shmid, NULL, 0);
```

---

**基本写法：分离共享内存**
`shmdt(<地址>);`
```c
// 解除映射但不删除
shmdt(addr);
```

---

**基本写法：删除共享内存**
`shmctl(<shmid>, IPC_RMID, NULL);`
```c
// 标记删除等所有进程分离后回收
shmctl(shmid, IPC_RMID, NULL);
```

---

**基本写法：生成键**
`ftok(<路径>, <项目ID>);`
```c
// 通过文件路径生成键
key_t key = ftok("/tmp/shm", 'A');
```

---

## POSIX 共享内存

**基本写法：创建共享内存对象**
`shm_open(<名称>, O_CREAT | O_RDWR, 0666);`
```c
// 创建 POSIX 共享内存
int fd = shm_open("/myshm", O_CREAT | O_RDWR, 0666);
```

---

**基本写法：设置大小**
`ftruncate(<fd>, <大小>);`
```c
// 设置共享内存大小
ftruncate(fd, 4096);
```

---

**基本写法：映射内存**
`mmap(NULL, <大小>, PROT_READ | PROT_WRITE, MAP_SHARED, <fd>, 0);`
```c
// 映射到地址空间
void* addr = mmap(NULL, 4096, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
```

---

**基本写法：解除映射**
`munmap(<地址>, <大小>);`
```c
// 解除映射
munmap(addr, 4096);
```

---

**基本写法：关闭与删除**
`close(<fd>); shm_unlink(<名称>);`
```c
// 关闭并删除共享内存对象
close(fd);
shm_unlink("/myshm");
```

---

## mmap 文件映射

**基本写法：映射文件**
`mmap(NULL, <大小>, <保护>, MAP_SHARED, <fd>, 0);`
```c
// 将文件映射到内存
int fd = open("data.bin", O_RDWR);
void* addr = mmap(NULL, 4096, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
```

---

**基本写法：同步到磁盘**
`msync(<地址>, <大小>, MS_SYNC);`
```c
// 将修改刷回文件
msync(addr, 4096, MS_SYNC);
```

---

## System V 信号量

**基本写法：创建信号量集**
`semget(<键>, <数量>, IPC_CREAT | 0666);`
```c
// 创建包含 1 个信号量的集合
int semid = semget(key, 1, IPC_CREAT | 0666);
```

---

**基本写法：初始化信号量**
`semctl(<semid>, 0, SETVAL, <值>);`
```c
// 设置初值
semctl(semid, 0, SETVAL, 1);
```

---

**基本写法：PV 操作**
`struct sembuf <op> = {0, -1, 0}; semop(<semid>, &<op>, 1);`
```c
// P 操作减 1
struct sembuf p = {0, -1, 0};
semop(semid, &p, 1);
// V 操作加 1
struct sembuf v = {0, 1, 0};
semop(semid, &v, 1);
```

---

**基本写法：删除信号量集**
`semctl(<semid>, 0, IPC_RMID);`
```c
// 删除信号量集
semctl(semid, 0, IPC_RMID);
```

---

## POSIX 信号量

**基本写法：创建命名信号量**
`sem_open(<名称>, O_CREAT, 0666, <初始>);`
```c
// 创建命名信号量
sem_t* sem = sem_open("/mysem", O_CREAT, 0666, 1);
```

---

**基本写法：等待与释放**
`sem_wait(<sem>);` `sem_post(<sem>);`
```c
// P 与 V 操作
sem_wait(sem);
// 临界区
sem_post(sem);
```

---

**基本写法：关闭与删除**
`sem_close(<sem>);` `sem_unlink(<名称>);`
```c
// 关闭并删除命名信号量
sem_close(sem);
sem_unlink("/mysem");
```

---

**基本写法：无名信号量**
`sem_t <变量>; sem_init(&<变量>, 1, <初始>);`
```c
// 用于共享内存的无名信号量
sem_t sem;
sem_init(&sem, 1, 1);
```

---

## 消息队列

**基本写法：创建消息队列**
`msgget(<键>, IPC_CREAT | 0666);`
```c
// 创建 System V 消息队列
int msqid = msgget(key, IPC_CREAT | 0666);
```

---

**基本写法：发送消息**
`msgsnd(<msqid>, &<消息>, <数据大小>, 0);`
```c
// 发送消息
struct Msg { long type; char data[100]; } msg;
msgsnd(msqid, &msg, sizeof(msg.data), 0);
```

---

**基本写法：接收消息**
`msgrcv(<msqid>, &<消息>, <大小>, <类型>, 0);`
```c
// 接收指定类型消息
msgrcv(msqid, &msg, sizeof(msg.data), 1, 0);
```

---

**基本写法：删除消息队列**
`msgctl(<msqid>, IPC_RMID, NULL);`
```c
// 删除消息队列
msgctl(msqid, IPC_RMID, NULL);
```
