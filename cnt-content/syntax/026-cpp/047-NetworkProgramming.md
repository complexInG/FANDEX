# C++ 网络编程

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## POSIX Socket 基础

**基本写法：创建套接字**
`int socket(<域>, <类型>, <协议>)`
```cpp
#include <sys/socket.h>
// 创建 TCP 套接字
int fd = socket(AF_INET, SOCK_STREAM, 0);
if (fd < 0) { perror("socket"); }
// AF_INET    IPv4
// AF_INET6   IPv6
// SOCK_STREAM TCP
// SOCK_DGRAM  UDP
```

---

**基本写法：绑定地址**
`bind(<fd>, <地址指针>, <地址长度>)`
```cpp
#include <netinet/in.h>
struct sockaddr_in addr{};
addr.sin_family = AF_INET;
addr.sin_port = htons(8080);          // 端口转网络字节序
addr.sin_addr.s_addr = INADDR_ANY;    // 监听所有地址
bind(fd, (struct sockaddr*)&addr, sizeof(addr));
```

---

**基本写法：监听**
`listen(<fd>, <等待队列长度>)`
```cpp
// 开始监听
listen(fd, 5); // backlog=5
```

---

**基本写法：接受连接**
`accept(<fd>, <地址>, <长度>)`
```cpp
// 接受客户端连接（阻塞）
struct sockaddr_in client{};
socklen_t len = sizeof(client);
int conn = accept(fd, (struct sockaddr*)&client, &len);
```

---

**基本写法：连接服务器**
`connect(<fd>, <地址>, <长度>)`
```cpp
// 客户端连接
struct sockaddr_in srv{};
srv.sin_family = AF_INET;
srv.sin_port = htons(8080);
inet_pton(AF_INET, "127.0.0.1", &srv.sin_addr);
connect(fd, (struct sockaddr*)&srv, sizeof(srv));
```

---

**基本写法：收发数据**
`send/recv` 或 `read/write`
```cpp
// TCP 收发
char buf[1024];
ssize_t n = recv(conn, buf, sizeof(buf), 0);
send(conn, "hello", 5, 0);
// UDP 用 sendto/recvfrom
sendto(fd, "hi", 2, 0, (struct sockaddr*)&srv, sizeof(srv));
recvfrom(fd, buf, sizeof(buf), 0, nullptr, nullptr);
```

---

## 地址转换

**基本写法：IP 字符串与二进制互转**
`inet_pton(<域>, <字符串>, <二进制>)`
```cpp
#include <arpa/inet.h>
// 字符串转二进制
struct in_addr addr;
inet_pton(AF_INET, "192.168.1.1", &addr);
// 二进制转字符串
char str[INET_ADDRSTRLEN];
inet_ntop(AF_INET, &addr, str, sizeof(str));
```

---

**基本写法：getaddrinfo 解析**
`getaddrinfo(<主机>, <服务>, <提示>, <结果>)`
```cpp
#include <netdb.h>
struct addrinfo hints{}, *res;
hints.ai_family = AF_INET;
hints.ai_socktype = SOCK_STREAM;
getaddrinfo("example.com", "80", &hints, &res);
// 使用 res 链表
freeaddrinfo(res);
```

---

## 套接字选项

**基本写法：设置选项**
`setsockopt(<fd>, <级别>, <选项>, <值>, <长度>)`
```cpp
// 地址重用
int yes = 1;
setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(yes));
// 接收超时
struct timeval tv{.tv_sec = 5, .tv_usec = 0};
setsockopt(fd, SOL_SOCKET, SO_RCVTIMEO, &tv, sizeof(tv));
```

---

## I/O 复用

**基本写法：select 多路复用**
`select(<最大fd+1>, <读集>, <写集>, <异常集>, <超时>)`
```cpp
#include <sys/select.h>
fd_set readfds;
FD_ZERO(&readfds);
FD_SET(fd, &readfds);
struct timeval tv{5, 0};
int n = select(fd + 1, &readfds, nullptr, nullptr, &tv);
if (n > 0 && FD_ISSET(fd, &readfds)) { /* 可读 */ }
```

---

**基本写法：poll 多路复用**
`poll(<数组>, <数量>, <超时>)`
```cpp
#include <poll.h>
struct pollfd fds[2];
fds[0].fd = fd1; fds[0].events = POLLIN;
fds[1].fd = fd2; fds[1].events = POLLIN;
int n = poll(fds, 2, 5000); // 超时 5 秒
for (int i = 0; i < 2; ++i)
    if (fds[i].revents & POLLIN) { /* 可读 */ }
```

---

**基本写法：epoll（Linux）**
`epoll_create / epoll_ctl / epoll_wait`
```cpp
#include <sys/epoll.h>
int ep = epoll_create1(0);
struct epoll_event ev{.events = EPOLLIN, .data.fd = fd};
epoll_ctl(ep, EPOLL_CTL_ADD, fd, &ev);
struct epoll_event events[10];
int n = epoll_wait(ep, events, 10, -1); // -1 阻塞
```

---

## 非阻塞 I/O

**基本写法：设置非阻塞**
`fcntl(<fd>, F_SETFL, O_NONBLOCK)`
```cpp
#include <fcntl.h>
// 设为非阻塞
int flags = fcntl(fd, F_GETFL, 0);
fcntl(fd, F_SETFL, flags | O_NONBLOCK);
```

---

## 简易 TCP 服务器框架

**基本写法：服务器流程**
`socket → bind → listen → accept → recv/send`
```cpp
// TCP echo 服务器骨架
int srv = socket(AF_INET, SOCK_STREAM, 0);
struct sockaddr_in addr{};
addr.sin_family = AF_INET;
addr.sin_port = htons(8080);
addr.sin_addr.s_addr = INADDR_ANY;
bind(srv, (struct sockaddr*)&addr, sizeof(addr));
listen(srv, 5);
while (true) {
    int conn = accept(srv, nullptr, nullptr);
    char buf[1024];
    ssize_t n = recv(conn, buf, sizeof(buf), 0);
    send(conn, buf, n, 0); // 回显
    close(conn);
}
```

---

## C++ 封装

**基本写法：RAII 套接字**
`struct Socket { int fd; ~Socket() { close(fd); } };`
```cpp
// RAII 管理套接字生命周期
struct Socket {
    int fd;
    Socket(int f) : fd(f) {}
    ~Socket() { if (fd >= 0) close(fd); }
    Socket(const Socket&) = delete;
    Socket& operator=(const Socket&) = delete;
    Socket(Socket&& o) noexcept : fd(o.fd) { o.fd = -1; }
};
```
