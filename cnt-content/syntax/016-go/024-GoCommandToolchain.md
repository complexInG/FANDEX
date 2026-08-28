# Go 命令工具链

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基础命令

**基本写法：查看版本**
`go version`
```go
// 输出 Go 版本与平台信息
// go version
```

---

**基本写法：查看环境变量**
`go env [变量名]`
```go
// 查看全部或指定环境变量
// go env GOPATH
// go env GOOS GOARCH
```

---

**基本写法：设置环境变量**
`go env -w <变量>=<值>`
```go
// 持久化写入 GOENV 配置文件
// go env -w GOPROXY=https://goproxy.cn,direct
// go env -w GO111MODULE=on
```

---

## 构建与运行

**基本写法：运行程序**
`go run <文件或包>`
```go
// 直接编译并执行，不产生可执行文件
// go run main.go
// go run .
```

---

**基本写法：编译二进制**
`go build [包路径]`
```go
// 编译生成可执行文件
// go build
// go build -o myapp
// go build ./cmd/server
```

---

**基本写法：指定输出名编译**
`go build -o <输出名> <包>`
```go
// 自定义输出文件名
// go build -o bin/app ./cmd/app
```

---

**基本写法：指定目标平台交叉编译**
`GOOS=<系统> GOARCH=<架构> go build`
```go
// 交叉编译，无需额外工具链
// GOOS=linux GOARCH=amd64 go build -o app_linux
// GOOS=windows GOARCH=arm64 go build
```

---

**基本写法：编译并嵌入版本信息**
`go build -ldflags "<参数>"`
```go
// 通过 -ldflags 注入变量值
// go build -ldflags "-X main.Version=1.0.0 -s -w"
// -s -w 去除调试符号与 DWARF 信息减小体积
```

---

**基本写法：安装到 GOBIN**
`go install <包>`
```go
// 编译并安装到 GOBIN/GOPATH/bin
// go install
// go install golang.org/x/tools/cmd/goimports@latest
```

---

## 测试

**基本写法：运行测试**
`go test [包路径]`
```go
// 运行当前包测试
// go test
// go test ./...
```

---

**基本写法：递归测试所有包**
`go test ./...`
```go
// 测试当前模块下所有包
// go test ./...
```

---

**基本写法：显示详细输出**
`go test -v`
```go
// 打印每个用例的执行详情
// go test -v ./...
```

---

**基本写法：运行指定测试**
`go test -run <正则>`
```go
// 按正则匹配用例名执行
// go test -run TestSum
// go test -run TestUser/Delete
```

---

**基本写法：生成覆盖率报告**
`go test -cover`
```go
// 输出覆盖率百分比
// go test -cover ./...
```

---

**基本写法：生成覆盖率详情文件**
`go test -coverprofile=<文件>`
```go
// 生成覆盖率文件，配合 go tool cover 查看
// go test -coverprofile=cover.out ./...
// go tool cover -html=cover.out -o cover.html
```

---

**基本写法：基准测试**
`go test -bench=<正则>`
```go
// 运行 Benchmark 前缀函数
// go test -bench=. -benchmem
```

---

**基本写法：竞态检测**
`go test -race`
```go
// 启用竞态检测器
// go test -race ./...
```

---

## 模块管理

**基本写法：初始化模块**
`go mod init <模块路径>`
```go
// 创建 go.mod 文件
// go mod init github.com/myname/myproject
```

---

**基本写法：整理依赖**
`go mod tidy`
```go
// 添加缺失依赖、移除未用依赖
// go mod tidy
```

---

**基本写法：下载依赖到本地缓存**
`go mod download`
```go
// 下载依赖到 GOMODCACHE，不安装
// go mod download
```

---

**基本写法：添加依赖**
`go get <包路径>`
```go
// 下载并添加到 go.mod
// go get github.com/gin-gonic/gin
```

---

**基本写法：添加指定版本**
`go get <包路径>@<版本>`
```go
// 指定版本、提交或标签
// go get github.com/gin-gonic/gin@v1.9.1
// go get github.com/x/y@latest
```

---

**基本写法：升级依赖**
`go get -u <包路径>`
```go
// 升级到最新次版本及依赖
// go get -u github.com/gin-gonic/gin
```

---

**基本写法：移除依赖**
`go get <包路径>@none`
```go
// 移除指定依赖
// go get github.com/old/pkg@none
```

---

**基本写法：查看依赖图**
`go mod graph`
```go
// 打印模块依赖关系图
// go mod graph
```

---

**基本写法：将依赖复制到 vendor**
`go mod vendor`
```go
// 创建 vendor 目录存放依赖源码
// go mod vendor
```

---

**基本写法：校验依赖完整性**
`go mod verify`
```go
// 校验下载依赖的哈希
// go mod verify
```

---

## 代码质量

**基本写法：格式化代码**
`go fmt [包路径]`
```go
// 按标准格式重写源码
// go fmt ./...
```

---

**基本写法：gofmt 检查差异**
`gofmt -l <目录>`
```go
// 列出格式不符的文件，不修改
// gofmt -l .
```

---

**基本写法：静态检查**
`go vet [包路径]`
```go
// 运行内置可疑构造检查
// go vet ./...
```

---

**基本写法：清理构建缓存**
`go clean`
```go
// 清理构建产生的对象文件
// go clean
```

---

**基本写法：清理缓存目录**
`go clean -cache`
```go
// 清理 go build 缓存
// go clean -cache
// go clean -modcache  // 清理模块下载缓存
// go clean -testcache  // 清理测试结果缓存
```

---

## 文档与依赖查看

**基本写法：查看文档**
`go doc [包路径]`
```go
// 在终端查看包文档
// go doc fmt.Println
// go doc github.com/gin-gonic/gin
```

---

**基本写法：列出包及其依赖**
`go list [包路径]`
```go
// 列出当前模块的包
// go list ./...
// go list -m all  // 列出所有依赖模块
```

---

**基本写法：查看包导入路径**
`go list -f <模板> <包>`
```go
// 自定义输出格式
// go list -f "{{.ImportPath}} {{.Imports}}" ./...
```

---

**基本写法：启动本地文档服务**
`go doc -all`
```go
// 浏览器查看完整文档
// godoc -http=:6060
```

---