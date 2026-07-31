# C 进程与管道

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 进程创建

**基本写法：创建子进程**
`fork();`
```c
// 创建当前进程的副本
pid_t pid = fork();
```

---

**基本写法：区分父子进程**
`if (<pid> == 0) { /* 子进程 */ } else { /* 父进程 */ }`
```c
// 通过返回值区分
pid_t pid = fork();
if (pid == 0) {
    // 子进程代码
} else if (pid > 0) {
    // 父进程代码
}
```

---

**基本写法：替换进程映像**
`execlp(<程序>, <参数0>, ..., NULL);`
```c
// 用新程序替换当前进程
execlp("ls", "ls", "-l", NULL);
```

---

**基本写法：execv 系列**
`execv(<路径>, <参数数组>);`
```c
// 使用数组传参
char* args[] = {"ls", "-l", NULL};
execv("/bin/ls", args);
```

---

**基本写法：fork + exec 组合**
`fork(); execlp(...);`
```c
// 子进程执行新程序
pid_t pid = fork();
if (pid == 0) {
    execlp("echo", "echo", "hi", NULL);
    _exit(1);
}
```

---

## 等待进程

**基本写法：等待任意子进程**
`wait(&<状态>);`
```c
// 阻塞等待子进程结束
int status;
wait(&status);
```

---

**基本写法：等待指定子进程**
`waitpid(<pid>, &<状态>, 0);`
```c
// 等待特定子进程
int status;
waitpid(pid, &status, 0);
```

---

**基本写法：非阻塞等待**
`waitpid(<pid>, &<状态>, WNOHANG);`
```c
// 立即返回不阻塞
int r = waitpid(pid, &status, WNOHANG);
```

---

**基本写法：检查退出码**
`WEXITSTATUS(<状态>);`
```c
// 取出子进程退出值
if (WIFEXITED(status)) {
    int code = WEXITSTATUS(status);
}
```

---

**基本写法：获取自身 PID**
`getpid();`
```c
// 当前进程 ID
pid_t self = getpid();
```

---

**基本写法：获取父进程 PID**
`getppid();`
```c
// 父进程 ID
pid_t parent = getppid();
```

---

## 进程退出

**基本写法：正常退出**
`exit(<状态码>);`
```c
// 调用注册的清理函数后退出
exit(0);
```

---

**基本写法：立即退出**
`_exit(<状态码>);`
```c
// 不执行 atexit 注册函数直接退出
_exit(1);
```

---

**基本写法：注册退出函数**
`atexit(<函数>);`
```c
// 注册程序退出时调用的函数
atexit(cleanup);
```

---

## 管道

**基本写法：创建匿名管道**
`pipe(<int[2]>);`
```c
// 创建一对读写描述符
int fd[2];
pipe(fd);
```

---

**基本写法：父子进程通信**
`pipe(fd); fork();`
```c
// 父进程写子进程读
int fd[2];
pipe(fd);
pid_t pid = fork();
if (pid == 0) {
    close(fd[1]);       // 子进程关闭写端
    read(fd[0], buf, n);
} else {
    close(fd[0]);       // 父进程关闭读端
    write(fd[1], buf, n);
}
```

---

**基本写法：写管道**
`write(<写端>, <数据>, <大小>);`
```c
// 向管道写入数据
write(fd[1], data, sizeof(data));
```

---

**基本写法：读管道**
`read(<读端>, <缓冲>, <大小>);`
```c
// 从管道读取数据
ssize_t n = read(fd[0], buf, sizeof(buf));
```

---

## popen

**基本写法：执行命令并获取输出**
`popen(<命令>, "r");`
```c
// 通过管道读取命令输出
FILE* fp = popen("ls -l", "r");
```

---

**基本写法：读取命令输出**
`fgets(<缓冲>, <大小>, <fp>);`
```c
// 逐行读取
char line[256];
while (fgets(line, sizeof(line), fp)) { }
```

---

**基本写法：关闭 popen**
`pclose(<fp>);`
```c
// 关闭并等待命令结束
pclose(fp);
```

---

## 命名管道 FIFO

**基本写法：创建 FIFO**
`mkfifo(<路径>, <权限>);`
```c
// 创建命名管道文件
mkfifo("/tmp/myfifo", 0666);
```

---

**基本写法：打开 FIFO**
`open(<路径>, <标志>);`
```c
// 以读写方式打开
int fd = open("/tmp/myfifo", O_RDWR);
```

---

**基本写法：删除 FIFO**
`unlink(<路径>);`
```c
// 删除管道文件
unlink("/tmp/myfifo");
```

---

## 环境变量

**基本写法：获取环境变量**
`getenv(<名称>);`
```c
// 读取环境变量值
char* path = getenv("PATH");
```

---

**基本写法：设置环境变量**
`setenv(<名称>, <值>, 1);`
```c
// 设置或覆盖环境变量
setenv("MY_VAR", "1", 1);
```

---

**基本写法：删除环境变量**
`unsetenv(<名称>);`
```c
// 删除环境变量
unsetenv("MY_VAR");
```
