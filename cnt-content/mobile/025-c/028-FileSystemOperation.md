# C 文件系统操作

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 文件信息

**基本写法：获取文件状态**
`stat(<路径>, &<结构>);`
```c
// 获取文件元数据
struct stat st;
stat("file.txt", &st);
```

---

**基本写法：获取文件大小**
`<st>.st_size`
```c
// 取出文件字节数
off_t size = st.st_size;
```

---

**基本写法：判断是否目录**
`S_ISDIR(<st>.st_mode)`
```c
// 检查是否为目录
if (S_ISDIR(st.st_mode)) { }
```

---

**基本写法：判断是否普通文件**
`S_ISREG(<st>.st_mode)`
```c
// 检查是否为普通文件
if (S_ISREG(st.st_mode)) { }
```

---

**基本写法：获取文件权限**
`<st>.st_mode & 0777`
```c
// 取出权限位
mode_t perm = st.st_mode & 0777;
```

---

**基本写法：获取修改时间**
`<st>.st_mtime`
```c
// 文件最后修改时间戳
time_t mtime = st.st_mtime;
```

---

## 目录操作

**基本写法：创建目录**
`mkdir(<路径>, <权限>);`
```c
// 创建目录
mkdir("newdir", 0755);
```

---

**基本写法：删除目录**
`rmdir(<路径>);`
```c
// 删除空目录
rmdir("newdir");
```

---

**基本写法：打开目录**
`opendir(<路径>);`
```c
// 打开目录流
DIR* dir = opendir(".");
```

---

**基本写法：读取目录项**
`readdir(<dir>);`
```c
// 逐个读取目录项
struct dirent* entry;
while ((entry = readdir(dir)) != NULL) {
    printf("%s\n", entry->d_name);
}
```

---

**基本写法：关闭目录**
`closedir(<dir>);`
```c
// 关闭目录流
closedir(dir);
```

---

**基本写法：切换工作目录**
`chdir(<路径>);`
```c
// 改变当前工作目录
chdir("/tmp");
```

---

**基本写法：获取工作目录**
`getcwd(<缓冲>, <大小>);`
```c
// 取得当前工作目录
char buf[256];
getcwd(buf, sizeof(buf));
```

---

## 文件操作

**基本写法：创建文件**
`creat(<路径>, <权限>);`
```c
// 创建或截断文件
int fd = creat("file.txt", 0644);
```

---

**基本写法：删除文件**
`unlink(<路径>);`
```c
// 删除文件
unlink("file.txt");
```

---

**基本写法：重命名**
`rename(<旧名>, <新名>);`
```c
// 重命名或移动文件
rename("old.txt", "new.txt");
```

---

**基本写法：链接文件**
`link(<原路径>, <新路径>);`
```c
// 创建硬链接
link("file.txt", "hardlink.txt");
```

---

**基本写法：符号链接**
`symlink(<目标>, <链接名>);`
```c
// 创建软链接
symlink("file.txt", "softlink.txt");
```

---

**基本写法：读取符号链接**
`readlink(<链接>, <缓冲>, <大小>);`
```c
// 读取链接指向的目标
char buf[256];
ssize_t n = readlink("softlink.txt", buf, sizeof(buf));
buf[n] = '\0';
```

---

## 权限与所有者

**基本写法：修改权限**
`chmod(<路径>, <权限>);`
```c
// 修改文件权限
chmod("file.txt", 0644);
```

---

**基本写法：修改所有者**
`chown(<路径>, <uid>, <gid>);`
```c
// 修改文件所有者
chown("file.txt", 1000, 1000);
```

---

**基本写法：修改文件描述符权限**
`fchmod(<fd>, <权限>);`
```c
// 通过描述符修改权限
fchmod(fd, 0644);
```

---

## 文件描述符操作

**基本写法：复制描述符**
`dup(<fd>);` / `dup2(<fd>, <新fd>);`
```c
// 重定向到指定描述符
dup2(fd, STDOUT_FILENO);
```

---

**基本写法：打开文件**
`open(<路径>, <标志>);`
```c
// 读写方式打开
int fd = open("file.txt", O_RDWR | O_CREAT, 0644);
```

---

**基本写法：读写**
`read(<fd>, <缓冲>, <大小>);` `write(<fd>, <数据>, <大小>);`
```c
// 底层读写
ssize_t n = read(fd, buf, sizeof(buf));
write(fd, buf, n);
```

---

**基本写法：定位文件偏移**
`lseek(<fd>, <偏移>, <起始>);`
```c
// 移动文件读写位置
lseek(fd, 0, SEEK_SET);   // 回到开头
```

---

**基本写法：关闭描述符**
`close(<fd>);`
```c
// 关闭文件描述符
close(fd);
```

---

## 遍历目录树

**基本写法：递归遍历目录**
`nftw(<路径>, <回调>, <深度>, <标志>);`
```c
// 文件树遍历
int cb(const char* path, const struct stat* st, int type, struct FTW* ftw) {
    if (type == FTW_F) printf("%s\n", path);
    return 0;
}
nftw(".", cb, 10, FTW_PHYS);
```

---

## glob 模式匹配

**基本写法：通配符匹配文件**
`glob(<模式>, 0, NULL, &<结果>);`
```c
// 匹配所有 .txt 文件
glob_t g;
glob("*.txt", 0, NULL, &g);
for (size_t i = 0; i < g.gl_pathc; i++) {
    printf("%s\n", g.gl_pathv[i]);
}
globfree(&g);
```

---

## 临时文件

**基本写法：创建临时文件**
`tmpfile();`
```c
// 创建自动删除的临时文件
FILE* fp = tmpfile();
```

---

**基本写法：生成临时文件名**
`mkstemp(<模板>);`
```c
// 安全创建临时文件
char tmpl[] = "/tmp/myfileXXXXXX";
int fd = mkstemp(tmpl);
```
