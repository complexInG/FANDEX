# C Socket 网络编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 Socket

**基本写法：创建 TCP socket**
`socket(AF_INET, SOCK_STREAM, 0);`
```c
// 创建 IPv4 TCP 套接字
int fd = socket(AF_INET, SOCK_STREAM, 0);
```

---

**基本写法：创建 UDP socket**
`socket(AF_INET, SOCK_DGRAM, 0);`
```c
// 创建 IPv4 UDP 套接字
int fd = socket(AF_INET, SOCK_DGRAM, 0);
```

---

**基本写法：创建本地 socket**
`socket(AF_UNIX, SOCK_STREAM, 0);`
```c
// 创建 Unix 域套接字
int fd = socket(AF_UNIX, SOCK_STREAM, 0);
```

---

## 地址结构

**基本写法：IPv4 地址结构**
`struct sockaddr_in <变量>;`
```c
// 初始化服务器地址
struct sockaddr_in addr;
addr.sin_family = AF_INET;
addr.sin_port = htons(8080);
addr.sin_addr.s_addr = INADDR_ANY;
```

---

**基本写法：字符串转地址**
`inet_pton(AF_INET, <IP串>, &<地址>);`
```c
// 将点分十进制转为二进制
inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr);
```

---

**基本写法：地址转字符串**
`inet_ntop(AF_INET, &<地址>, <缓冲>, <大小>);`
```c
// 二进制地址转可读字符串
char ip[INET_ADDRSTRLEN];
inet_ntop(AF_INET, &addr.sin_addr, ip, sizeof(ip));
```

---

## 服务端流程

**基本写法：绑定地址**
`bind(<fd>, (struct sockaddr*)&<地址>, sizeof(<地址>));`
```c
// 绑定本地地址端口
bind(fd, (struct sockaddr*)&addr, sizeof(addr));
```

---

**基本写法：监听连接**
`listen(<fd>, <队列长度>);`
```c
// 开始监听客户端连接
listen(fd, 5);
```

---

**基本写法：接受连接**
`accept(<fd>, (struct sockaddr*)&<客户端地址>, &<长度>);`
```c
// 接受新连接返回新描述符
struct sockaddr_in cli;
socklen_t len = sizeof(cli);
int cfd = accept(fd, (struct sockaddr*)&cli, &len);
```

---

## 客户端流程

**基本写法：连接服务器**
`connect(<fd>, (struct sockaddr*)&<服务器地址>, sizeof(<地址>));`
```c
// 主动连接服务器
connect(fd, (struct sockaddr*)&srv, sizeof(srv));
```

---

## 数据收发

**基本写法：发送数据**
`send(<fd>, <数据>, <大小>, 0);`
```c
// TCP 发送数据
send(fd, buf, n, 0);
```

---

**基本写法：接收数据**
`recv(<fd>, <缓冲>, <大小>, 0);`
```c
// TCP 接收数据
ssize_t n = recv(fd, buf, sizeof(buf), 0);
```

---

**基本写法：UDP 发送**
`sendto(<fd>, <数据>, <大小>, 0, (struct sockaddr*)&<目标>, sizeof(<目标>));`
```c
// UDP 发送数据到指定地址
sendto(fd, buf, n, 0, (struct sockaddr*)&dst, sizeof(dst));
```

---

**基本写法：UDP 接收**
`recvfrom(<fd>, <缓冲>, <大小>, 0, (struct sockaddr*)&<来源>, &<长度>);`
```c
// UDP 接收数据并获取来源
struct sockaddr_in src;
socklen_t len = sizeof(src);
recvfrom(fd, buf, sizeof(buf), 0, (struct sockaddr*)&src, &len);
```

---

## Socket 选项

**基本写法：设置地址复用**
`setsockopt(<fd>, SOL_SOCKET, SO_REUSEADDR, &<值>, sizeof(<值>));`
```c
// 避免地址占用错误
int opt = 1;
setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
```

---

**基本写法：设置接收超时**
`setsockopt(<fd>, SOL_SOCKET, SO_RCVTIMEO, &<时长>, sizeof(<时长>));`
```c
// 设置接收超时
struct timeval tv = {5, 0};
setsockopt(fd, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(tv));
```

---

## I/O 多路复用

**基本写法：select 等待**
`select(<最大fd+1>, &<读集>, NULL, NULL, &<超时>);`
```c
// 监视多个描述符
fd_set rfds;
FD_ZERO(&rfds);
FD_SET(fd, &rfds);
struct timeval tv = {5, 0};
select(fd + 1, &rfds, NULL, NULL, &tv);
```

---

**基本写法：poll 等待**
`poll(<数组>, <数量>, <超时毫秒>);`
```c
// 使用 poll 监视
struct pollfd fds[1];
fds[0].fd = fd;
fds[0].events = POLLIN;
poll(fds, 1, 5000);
```

---

**基本写法：epoll 创建**
`epoll_create1(0);`
```c
// Linux 高效多路复用
int epfd = epoll_create1(0);
```

---

**基本写法：epoll 注册**
`epoll_ctl(<epfd>, EPOLL_CTL_ADD, <fd>, &<事件>);`
```c
// 添加描述符到 epoll
struct epoll_event ev;
ev.events = EPOLLIN;
ev.data.fd = fd;
epoll_ctl(epfd, EPOLL_CTL_ADD, fd, &ev);
```

---

**基本写法：epoll 等待**
`epoll_wait(<epfd>, <事件数组>, <最大数>, <超时>);`
```c
// 等待事件发生
struct epoll_event events[10];
int n = epoll_wait(epfd, events, 10, -1);
```

---

## 关闭 Socket

**基本写法：关闭描述符**
`close(<fd>);`
```c
// 关闭并释放资源
close(fd);
```

---

**基本写法：优雅关闭**
`shutdown(<fd>, SHUT_WR);`
```c
// 单向关闭写端
shutdown(fd, SHUT_WR);
```

---

## 主机与服务查询

**基本写法：获取主机信息**
`getaddrinfo(<主机>, <服务>, &<提示>, &<结果>);`
```c
// 现代地址查询接口
struct addrinfo hints = {0};
hints.ai_family = AF_INET;
hints.ai_socktype = SOCK_STREAM;
struct addrinfo* res;
getaddrinfo("example.com", "80", &hints, &res);
```

---

**基本写法：释放结果**
`freeaddrinfo(<结果>);`
```c
// 释放 getaddrinfo 结果
freeaddrinfo(res);
```
