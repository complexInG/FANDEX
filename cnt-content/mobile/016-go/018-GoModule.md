# Go Modules

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 模块初始化

**基本写法：初始化模块**
`go mod init <模块路径>`
```go
// 创建 go.mod 文件
// go mod init github.com/myname/myproject
```

**基本写法：go.mod 文件结构**
`module <路径>`
```go
// go.mod 文件基本结构
// module github.com/myname/myproject
// go 1.22
// require (
//     github.com/gin-gonic/gin v1.9.1
// )
```

---

## 依赖管理

**基本写法：添加依赖**
`go get <包路径>`
```go
// 下载并添加依赖
// go get github.com/gin-gonic/gin
```

**基本写法：添加指定版本**
`go get <包路径>@<版本>`
```go
// 指定版本添加依赖
// go get github.com/gin-gonic/gin@v1.9.1
```

**基本写法：更新依赖**
`go get -u <包路径>`
```go
// 更新到最新版本
// go get -u github.com/gin-gonic/gin
```

**基本写法：更新所有依赖**
`go get -u ./...`
```go
// 更新项目中所有依赖
// go get -u ./...
```

**基本写法：移除未使用依赖**
`go mod tidy`
```go
// 清理 go.mod 中未使用的依赖
// go mod tidy
```

**基本写法：降级依赖**
`go get <包路径>@<较低版本>`
```go
// 降级到指定版本
// go get github.com/gin-gonic/gin@v1.8.0
```

**基本写法：查看可用版本**
`go list -m -versions <包路径>`
```go
// 列出模块所有可用版本
// go list -m -versions github.com/gin-gonic/gin
```

**基本写法：查看依赖图**
`go mod graph`
```go
// 输出依赖关系图
// go mod graph
```

---

## 依赖下载与缓存

**基本写法：下载依赖到本地**
`go mod download`
```go
// 下载所有依赖到本地缓存
// go mod download
```

**基本写法：下载指定依赖**
`go mod download <包路径>`
```go
// 下载指定模块
// go mod download github.com/gin-gonic/gin
```

**基本写法：将依赖复制到 vendor**
`go mod vendor`
```go
// 创建 vendor 目录存放依赖
// go mod vendor
```

**基本写法：使用 vendor 构建**
`go build -mod=vendor`
```go
// 使用 vendor 目录中的依赖
// go build -mod=vendor
```

---

## 模块查询

**基本写法：列出所有依赖**
`go list -m all`
```go
// 列出当前模块所有依赖
// go list -m all
```

**基本写法：查看依赖信息**
`go list -m -json <包路径>`
```go
// 以 JSON 格式查看模块信息
// go list -m -json github.com/gin-gonic/gin
```

**基本写法：查看模块路径**
`go list -m`
```go
// 输出当前模块路径
// go list -m
```

**基本写法：查看已更改的配置**
`go env -changed`
```go
// Go 1.23+ 仅显示与默认值不同的环境变量
// go env -changed
```

---

## 模块替换与排除

**基本写法：替换依赖**
`replace <原路径> => <新路径>`
```go
// 在 go.mod 中替换依赖源
// replace github.com/old/lib => github.com/new/lib v1.2.0
```

**基本写法：替换为本地路径**
`replace <路径> => <本地目录>`
```go
// 替换为本地开发版本
// replace github.com/myname/lib => ../lib
```

**基本写法：排除特定版本**
`exclude <包路径> <版本>`
```go
// 排除有问题的版本
// exclude github.com/some/pkg v1.5.0
```

**基本写法：撤回版本**
`retract <版本>`
```go
// 在 go.mod 中声明撤回有问题的版本
// retract v1.2.0
// retract [v1.1.0, v1.1.5]
```

---

## Go 1.24+ 工具依赖

**基本写法：添加工具依赖**
`go get -tool <工具路径>`
```go
// Go 1.24+ 使用 tool 指令管理工具
// go get -tool golang.org/x/tools/cmd/stringer
```

**基本写法：go.mod 中的 tool 指令**
`tool ( <工具路径> )`
```go
// go.mod 中声明工具依赖
// tool (
//     github.com/golangci/golangci-lint/cmd/golangci-lint
//     golang.org/x/tools/cmd/stringer
// )
```

**基本写法：运行工具**
`go tool <工具名>`
```go
// 运行声明的工具
// go tool stringer -type=Color
```

**基本写法：安装所有工具**
`go install tool`
```go
// 安装 go.mod 中所有工具到 GOBIN
// go install tool
```

**基本写法：更新所有工具**
`go get tool`
```go
// 更新所有工具到最新版本
// go get tool
```

---

## 版本控制与构建

**基本写法：嵌入版本信息**
`go build -buildvcs`
```go
// Go 1.24+ 默认嵌入 VCS 版本信息
// go build 默认将版本控制信息嵌入二进制
```

**基本写法：禁用版本信息**
`go build -buildvcs=false`
```go
// 不嵌入版本控制信息
// go build -buildvcs=false
```

**基本写法：JSON 构建输出**
`go build -json`
```go
// Go 1.24+ 以 JSON 格式输出构建结果
// go build -json
```

---

## 工具链管理

**基本写法：指定工具链版本**
`//go:toolchain <版本>`
```go
// 在 go.mod 中指定工具链
// go 1.24.0
// toolchain go1.24.3
```

**基本写法：切换工具链**
`go toolchain <命令>`
```go
// 切换 Go 工具链版本
// go toolchain go1.24.0
```

**基本写法：设置工具链策略**
`GOTOOLCHAIN=<值>`
```go
// 环境变量控制工具链行为
// GOTOOLCHAIN=auto  // 自动选择（默认）
// GOTOOLCHAIN=local // 强制使用本地版本
```

---

## 私有模块

**基本写法：设置私有仓库**
`GOPRIVATE=<域名>`
```go
// 跳过代理和校验的私有模块
// GOPRIVATE=git.mycorp.com,*.mycorp.com
```

**基本写法：Go 1.24+ GOAUTH 认证**
`GOAUTH=<认证方式>`
```go
// Go 1.24+ 灵活的私有模块认证
// GOAUTH=netrc:~/.netrc
```

**基本写法：设置模块代理**
`GOPROXY=<代理地址>`
```go
// 设置模块代理服务器
// GOPROXY=https://goproxy.cn,direct
```

**基本写法：设置校验和服务器**
`GOSUMDB=<地址>`
```go
// 设置校验和数据库
// GOSUMDB=sum.golang.org
```

---

## Workspace 工作区

**基本写法：初始化工作区**
`go work init <模块路径>`
```go
// 创建 go.work 文件管理多模块
// go work init ./module1 ./module2
```

**基本写法：添加模块到工作区**
`go work use <模块路径>`
```go
// 将模块添加到工作区
// go work use ./newmodule
```

**基本写法：工作区中同步依赖**
`go work sync`
```go
// 同步工作区依赖到各模块
// go work sync
```
