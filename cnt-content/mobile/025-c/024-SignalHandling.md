# C 信号处理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 信号基础

**基本写法：发送信号**
`raise(<信号>);`
```c
// 向自身发送信号
raise(SIGINT);
```

---

**基本写法：向进程发送信号**
`kill(<pid>, <信号>);`
```c
// 给指定进程发信号
kill(pid, SIGTERM);
```

---

## 注册信号处理函数

**基本写法：signal 注册**
`signal(<信号>, <处理函数>);`
```c
// 简单注册信号处理
signal(SIGINT, handler);
```

---

**基本写法：信号处理函数签名**
`void <函数名>(int <信号>);`
```c
// 信号处理函数原型
void handler(int sig) {
    // 仅调用异步信号安全函数
}
```

---

**基本写法：忽略信号**
`signal(<信号>, SIG_IGN);`
```c
// 忽略指定信号
signal(SIGINT, SIG_IGN);
```

---

**基本写法：恢复默认处理**
`signal(<信号>, SIG_DFL);`
```c
// 恢复默认行为
signal(SIGINT, SIG_DFL);
```

---

## sigaction

**基本写法：sigaction 注册**
`sigaction(<信号>, &<新动作>, [NULL]);`
```c
// 更健壮的信号注册方式
struct sigaction sa;
sa.sa_handler = handler;
sigemptyset(&sa.sa_mask);
sa.sa_flags = 0;
sigaction(SIGINT, &sa, NULL);
```

---

**基本写法：设置 sa_flags**
`<sa>.sa_flags = SA_RESTART;`
```c
// 被中断系统调用自动重启
sa.sa_flags = SA_RESTART;
```

---

**基本写法：获取旧动作**
`sigaction(<信号>, &<新动作>, &<旧动作>);`
```c
// 保存原有处理方式
struct sigaction oldsa;
sigaction(SIGINT, &sa, &oldsa);
```

---

## 信号集

**基本写法：初始化空信号集**
`sigemptyset(&<集合>);`
```c
// 清空信号集
sigset_t set;
sigemptyset(&set);
```

---

**基本写法：添加信号**
`sigaddset(&<集合>, <信号>);`
```c
// 向集合添加信号
sigaddset(&set, SIGINT);
```

---

**基本写法：填充所有信号**
`sigfillset(&<集合>);`
```c
// 集合包含所有信号
sigfillset(&set);
```

---

**基本写法：删除信号**
`sigdelset(&<集合>, <信号>);`
```c
// 从集合删除信号
sigdelset(&set, SIGINT);
```

---

**基本写法：判断信号是否在集合**
`sigismember(&<集合>, <信号>);`
```c
// 检查信号是否属于集合
if (sigismember(&set, SIGINT)) { }
```

---

## 信号屏蔽

**基本写法：设置屏蔽字**
`sigprocmask(<how>, &<集合>, [NULL]);`
```c
// 阻塞指定信号
sigset_t set;
sigemptyset(&set);
sigaddset(&set, SIGINT);
sigprocmask(SIG_BLOCK, &set, NULL);
```

---

**基本写法：解除屏蔽**
`sigprocmask(SIG_UNBLOCK, &<集合>, NULL);`
```c
// 解除信号阻塞
sigprocmask(SIG_UNBLOCK, &set, NULL);
```

---

**基本写法：获取未决信号**
`sigpending(&<集合>);`
```c
// 查询被阻塞的未决信号
sigset_t pending;
sigpending(&pending);
```

---

## 等待信号

**基本写法：暂停等待信号**
`pause();`
```c
// 挂起直到收到任意信号
pause();
```

---

**基本写法：sigsuspend 等待**
`sigsuspend(&<临时集合>);`
```c
// 原子替换屏蔽字并等待
sigset_t empty;
sigemptyset(&empty);
sigsuspend(&empty);
```

---

## 常用信号

**基本写法：终止信号**
`SIGTERM` / `SIGKILL`
```c
// SIGTERM 可捕获 SIGKILL 不可捕获
kill(pid, SIGTERM);
```

---

**基本写法：中断信号**
`SIGINT`
```c
// Ctrl+C 产生
signal(SIGINT, handler);
```

---

**基本写法：闹钟信号**
`alarm(<秒数>);`
```c
// 定时发送 SIGALRM
alarm(5);
```

---

**基本写法：子进程状态变化**
`SIGCHLD`
```c
// 子进程结束时发送
signal(SIGCHLD, handler);
```

---

## 异步信号安全

**基本写法：可重入处理函数**
`void <handler>(int <sig>) { write(STDERR_FILENO, "sig", 3); }`
```c
// 仅调用 write 等异步信号安全函数
void handler(int sig) {
    write(2, "interrupt\n", 10);
}
```

---

**基本写法：自管道技巧**
`write(<管道写端>, &<sig>, sizeof(int));`
```c
// 信号处理仅写管道主循环读取处理
void handler(int sig) {
    write(pipefd[1], &sig, sizeof(sig));
}
```
