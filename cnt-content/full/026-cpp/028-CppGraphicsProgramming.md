---
order: 71
title: C++图形编程
module: cpp
category: C++
difficulty: intermediate
description: OpenGL与Vulkan图形编程
author: fanquanpp
updated: '2026-08-01'
related:
  - cpp/C++23与C++26新特性
  - cpp/C++网络编程
  - cpp/C++序列化
  - cpp/C++与Rust对比
prerequisites:
  - cpp/概述与环境配置
---

## 概述

C++ 图形编程是利用 C++ 调用图形 API 在屏幕上绘制图像的技术。主要的图形 API 包括 OpenGL 和 Vulkan。OpenGL 是历史悠久的跨平台图形库，API 简单直观，适合入门学习；Vulkan 是新一代图形 API，提供更底层的控制，性能更高但学习曲线更陡。两者都通过着色器（Shader）在 GPU 上执行图形计算。

为什么需要图形编程？游戏引擎、CAD 软件、数据可视化、虚拟现实等应用都需要直接与 GPU 交互。虽然 Unity、Unreal 等引擎封装了底层细节，但理解图形 API 的工作原理能帮助你更好地优化性能和解决渲染问题。

## 基础概念

**渲染管线**：GPU 处理图形数据的流程。顶点数据经过顶点着色器、图元装配、光栅化、片段着色器等阶段，最终输出到屏幕上的像素。

**着色器**：运行在 GPU 上的小程序，用 GLSL（OpenGL）或 SPIR-V（Vulkan）编写。顶点着色器处理顶点位置，片段着色器处理像素颜色。

**顶点缓冲对象（VBO）**：在 GPU 显存中存储顶点数据的缓冲区，避免每帧从 CPU 传输数据。

**纹理**：贴在三维物体表面的二维图像，让物体看起来更真实。

**帧缓冲**：渲染的目标缓冲区，默认是屏幕，也可以是离屏缓冲区（用于后期处理等）。

## 快速上手

### OpenGL 环境搭建

使用 GLFW 创建窗口，GLAD 加载 OpenGL 函数：

```bash
# 安装依赖（Ubuntu）
sudo apt install libglfw3-dev libglad-dev

# 安装依赖（vcpkg）
vcpkg install glfw3 glad
```

```cmake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.20)
project(OpenGLDemo)

find_package(glfw3 CONFIG REQUIRED)
find_package(glad CONFIG REQUIRED)

add_executable(demo main.cpp)
target_link_libraries(demo glfw glad)
```

### 最简单的 OpenGL 程序

```cpp
// main.cpp - 创建窗口并清屏
#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <iostream>

// 窗口大小变化时的回调
void framebuffer_size_callback(GLFWwindow* window, int width, int height) {
    glViewport(0, 0, width, height);
}

// 处理输入
void processInput(GLFWwindow* window) {
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) {
        glfwSetWindowShouldClose(window, true);
    }
}

int main() {
    // 初始化 GLFW
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    // 创建窗口
    GLFWwindow* window = glfwCreateWindow(800, 600, "OpenGL Demo", nullptr, nullptr);
    if (!window) {
        std::cerr << "创建窗口失败" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);

    // 加载 OpenGL 函数
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        std::cerr << "加载 OpenGL 函数失败" << std::endl;
        return -1;
    }

    // 设置视口和回调
    glViewport(0, 0, 800, 600);
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

    // 渲染循环
    while (!glfwWindowShouldClose(window)) {
        processInput(window);

        // 清屏 - 使用深蓝色背景
        glClearColor(0.1f, 0.2f, 0.4f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}
```

## 详细用法

### 绘制三角形

```cpp
// 顶点着色器源码
const char* vertexShaderSource = R"(
    #version 330 core
    layout (location = 0) in vec3 aPos;  // 输入顶点位置
    void main() {
        gl_Position = vec4(aPos, 1.0);
    }
)";

// 片段着色器源码
const char* fragmentShaderSource = R"(
    #version 330 core
    out vec4 FragColor;  // 输出颜色
    void main() {
        FragColor = vec4(1.0, 0.5, 0.2, 1.0);  // 橙色
    }
)";

// 编译着色器的辅助函数
GLuint compileShader(GLenum type, const char* source) {
    GLuint shader = glCreateShader(type);
    glShaderSource(shader, 1, &source, nullptr);
    glCompileShader(shader);

    // 检查编译错误
    GLint success;
    glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
    if (!success) {
        char infoLog[512];
        glGetShaderInfoLog(shader, 512, nullptr, infoLog);
        std::cerr << "着色器编译失败: " << infoLog << std::endl;
    }
    return shader;
}

// 创建着色器程序
GLuint createShaderProgram() {
    GLuint vertexShader = compileShader(GL_VERTEX_SHADER, vertexShaderSource);
    GLuint fragmentShader = compileShader(GL_FRAGMENT_SHADER, fragmentShaderSource);

    GLuint program = glCreateProgram();
    glAttachShader(program, vertexShader);
    glAttachShader(program, fragmentShader);
    glLinkProgram(program);

    // 着色器已链接到程序，可以删除
    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);

    return program;
}

// 绘制三角形的完整流程
void drawTriangle() {
    // 三角形的三个顶点
    float vertices[] = {
        -0.5f, -0.5f, 0.0f,  // 左下
         0.5f, -0.5f, 0.0f,  // 右下
         0.0f,  0.5f, 0.0f   // 顶部
    };

    // 创建顶点缓冲对象和顶点数组对象
    GLuint VAO, VBO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);

    // 绑定 VAO（记录后续的顶点属性配置）
    glBindVertexArray(VAO);

    // 绑定 VBO 并复制数据
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    // 设置顶点属性指针
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    // 解绑
    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glBindVertexArray(0);

    // 创建着色器程序
    GLuint shaderProgram = createShaderProgram();

    // 在渲染循环中绘制
    glUseProgram(shaderProgram);
    glBindVertexArray(VAO);
    glDrawArrays(GL_TRIANGLES, 0, 3);
}
```

### 纹理映射

```cpp
// 带纹理坐标的顶点数据
float texturedVertices[] = {
    // 位置              // 纹理坐标
    -0.5f, -0.5f, 0.0f,  0.0f, 0.0f,  // 左下
     0.5f, -0.5f, 0.0f,  1.0f, 0.0f,  // 右下
     0.5f,  0.5f, 0.0f,  1.0f, 1.0f,  // 右上
    -0.5f,  0.5f, 0.0f,  0.0f, 1.0f   // 左上
};

// 索引数据（两个三角形组成一个矩形）
unsigned int indices[] = {
    0, 1, 2,  // 第一个三角形
    2, 3, 0   // 第二个三角形
};

// 加载纹理
GLuint loadTexture(const char* imagePath) {
    GLuint texture;
    glGenTextures(1, &texture);
    glBindTexture(GL_TEXTURE_2D, texture);

    // 设置纹理参数
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

    // 加载图片数据（这里使用 stb_image 库）
    int width, height, nrChannels;
    unsigned char* data = stbi_load(imagePath, &width, &height, &nrChannels, 0);
    if (data) {
        GLenum format = (nrChannels == 4) ? GL_RGBA : GL_RGB;
        glTexImage2D(GL_TEXTURE_2D, 0, format, width, height, 0, format, GL_UNSIGNED_BYTE, data);
        glGenerateMipmap(GL_TEXTURE_2D);
    } else {
        std::cerr << "纹理加载失败: " << imagePath << std::endl;
    }
    stbi_image_free(data);

    return texture;
}
```

### 变换矩阵

```cpp
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

// 在渲染循环中应用变换
void renderWithTransform(GLuint shaderProgram) {
    // 模型矩阵：旋转物体
    glm::mat4 model = glm::rotate(glm::mat4(1.0f),
        glm::radians(45.0f), glm::vec3(0.0f, 0.0f, 1.0f));

    // 视图矩阵：移动相机
    glm::mat4 view = glm::translate(glm::mat4(1.0f), glm::vec3(0.0f, 0.0f, -3.0f));

    // 投影矩阵：透视投影
    glm::mat4 projection = glm::perspective(glm::radians(45.0f),
        800.0f / 600.0f, 0.1f, 100.0f);

    // 传递矩阵到着色器
    glUseProgram(shaderProgram);
    glUniformMatrix4fv(glGetUniformLocation(shaderProgram, "model"), 1, GL_FALSE, glm::value_ptr(model));
    glUniformMatrix4fv(glGetUniformLocation(shaderProgram, "view"), 1, GL_FALSE, glm::value_ptr(view));
    glUniformMatrix4fv(glGetUniformLocation(shaderProgram, "projection"), 1, GL_FALSE, glm::value_ptr(projection));
}
```

### Vulkan 简介

Vulkan 比 OpenGL 更底层，需要手动管理更多细节：

```cpp
// Vulkan 的初始化流程（简化版）
#include <vulkan/vulkan.h>

int main() {
    // 1. 创建 Vulkan 实例
    VkInstance instance;
    VkInstanceCreateInfo createInfo{};
    createInfo.sType = VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO;
    vkCreateInstance(&createInfo, nullptr, &instance);

    // 2. 选择物理设备（GPU）
    uint32_t deviceCount = 0;
    vkEnumeratePhysicalDevices(instance, &deviceCount, nullptr);
    std::vector<VkPhysicalDevice> devices(deviceCount);
    vkEnumeratePhysicalDevices(instance, &deviceCount, devices.data());

    // 3. 创建逻辑设备
    VkDevice device;
    // ... 需要配置队列族、扩展等

    // 4. 创建交换链
    // 5. 创建渲染通道
    // 6. 创建帧缓冲
    // 7. 创建命令缓冲
    // 8. 渲染循环中提交命令

    // 清理
    vkDestroyInstance(instance, nullptr);
    return 0;
}
```

Vulkan 的代码量远大于 OpenGL，通常建议使用辅助库如 Vulkan-Hpp 或框架如 bgfx 来简化开发。

## 常见场景

### 3D 立方体渲染

```cpp
// 立方体的顶点数据（6个面，每面2个三角形）
float cubeVertices[] = {
    // 前面
    -0.5f, -0.5f,  0.5f,  0.0f, 0.0f,
     0.5f, -0.5f,  0.5f,  1.0f, 0.0f,
     0.5f,  0.5f,  0.5f,  1.0f, 1.0f,
    -0.5f,  0.5f,  0.5f,  0.0f, 1.0f,
    // 后面
    -0.5f, -0.5f, -0.5f,  0.0f, 0.0f,
     0.5f, -0.5f, -0.5f,  1.0f, 0.0f,
     0.5f,  0.5f, -0.5f,  1.0f, 1.0f,
    -0.5f,  0.5f, -0.5f,  0.0f, 1.0f,
    // ... 其余4个面
};

// 在渲染循环中旋转立方体
glm::mat4 model = glm::rotate(glm::mat4(1.0f),
    (float)glfwGetTime() * glm::radians(50.0f),
    glm::vec3(0.5f, 1.0f, 0.0f));

// 启用深度测试，确保前面的面遮挡后面的面
glEnable(GL_DEPTH_TEST);
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
```

## 注意事项

**OpenGL 与 Vulkan 的选择**：学习图形编程建议从 OpenGL 开始，概念更简单。需要更高性能和更细粒度控制时再转向 Vulkan。

**着色器调试困难**：着色器运行在 GPU 上，无法像 CPU 代码那样断点调试。使用 `glGetShaderInfoLog` 获取编译错误信息，使用 RenderDoc 等工具分析渲染过程。

**坐标系差异**：OpenGL 使用右手坐标系，Vulkan 使用左手坐标系。纹理坐标的 Y 轴方向也不同。

**驱动兼容性**：不同 GPU 厂商的驱动行为可能不同。在 NVIDIA 上正常的代码在 AMD 或 Intel 上可能有问题，需要多平台测试。

**内存管理**：GPU 资源（缓冲区、纹理）需要手动管理。忘记释放会导致显存泄漏。

## 进阶用法

### 使用 bgfx 跨平台图形库

```cpp
#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

// bgfx 封装了 OpenGL、Vulkan、DirectX 等后端
// 用同一套代码在不同平台上运行

// 初始化
bgfx::Init init;
init.type = bgfx::RendererType::Count;  // 自动选择
init.resolution.width = 800;
init.resolution.height = 600;
init.resolution.reset = BGFX_RESET_VSYNC;
bgfx::init(init);

// 创建顶点缓冲
bgfx::VertexLayout layout;
layout.begin()
    .add(bgfx::Attrib::Position, 3, bgfx::AttribType::Float)
    .add(bgfx::Attrib::TexCoord0, 2, bgfx::AttribType::Float)
.end();

bgfx::VertexBufferHandle vbh = bgfx::createVertexBuffer(
    bgfx::makeRef(vertices, sizeof(vertices)), layout);

// 提交绘制命令
bgfx::submit(0, programHandle);
bgfx::frame();
```

## 参考文献

cppreference C++ 文档：https://zh.cppreference.com/w/cpp
C++ 核心指南：https://isocpp.github.io/CppCoreGuidelines/
C++ 标准草案（WG21）：https://isocpp.org/std/the-standard
CMake 官方文档：https://cmake.org/documentation/
Compiler Explorer：https://godbolt.org/

## 延伸阅读

C++ 模板深入，见 026-cpp/062-CppTemplate 文档。
STL 容器与算法，见 026-cpp 模块 STL 文档。
并发与原子，见 026-cpp 模块并发文档。
Rust 内存安全对比，见 053-rust 模块（若已加入）。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 C++ 课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 RAII 与所有权设计

所有权是资源生命周期的归属：栈对象归作用域，unique_ptr 归唯一持有者，shared_ptr 共享所有权，weak_ptr 观察不持有。
传参选择：只读用 const&，需要拷贝用值，转移所有权用 unique_ptr 值传递或 move。
返回选择：返回值（RVO/移动）优先；需要多态返回 unique_ptr<Base>。
容器元素生命周期：容器持有元素值或智能指针；避免裸指针悬垂。

### 13.2 constexpr 与编译期编程

constexpr 变量与函数在编译期求值，消除运行时开销；consteval（C++20）强制编译期求值。
编译期字符串处理、配置表、哈希可在 constexpr 中实现，配合 static_assert 验证。
模板元编程（如 std::tuple 操作）与 constexpr 互补：前者变换类型，后者计算值。
工程建议：优先 constexpr 函数而非模板递归；编译期逻辑保持可测试（运行时同样可调用）。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| C++ 概述与现代标准 | 001-CppOverviewAndModernStandard | 本文的前置基础 |
| C++ 基础语法 | 002-CppBasicSyntax | 本文的前置基础 |
| C++ 类型系统 | 003-CppTypeSystem | 本文的并列主题 |
| C++ 引用 | 004-CppReference | 本文的并列主题 |
| 右值引用与移动语义 | 005-RvalueReferenceMoveSemantics | 本文的并列主题 |
| C++ 指针 | 006-PointersCppreferenceCom | 本文的并列主题 |
| 智能指针详解 | 007-N4089DeletingSafeBoolInFavorOfExplicitBool | 本文的并列主题 |
| Lambda表达式 | 008-LambdaExpression | 本文的并列主题 |
| 模板元编程 | 009-ATourOfC3rdEditionOnlineExcerpts | 本文的并列主题 |
| C++20范围 | 010-Cpp20Range | 本文的并列主题 |
| C++20模块 | 011-Cpp20Module | 本文的并列主题 |
| 设计模式与C++ | 012-DesignPatternCpp | 本文的并列主题 |
| RAII与资源管理 | 013-RAIIResourceManagement | 本文的并列主题 |
| 运算符重载 | 014-OperatorOverloading | 本文的并列主题 |
| C++ 面向对象基础 | 015-COOPBasics | 本文的前置基础 |
| C++ STL 算法详解 | 016-CSTL | 本文的并列主题 |
| 字符串处理 | 017-StringProcessing | 本文的并列主题 |
| 文件IO与文件系统 | 018-FileIOFileSystem | 本文的并列主题 |
| 异常安全 | 019-ExceptionSecurity | 本文的安全延伸 |
| 多线程与并发 | 020-MultithreadingConcurrency | 本文的并列主题 |
| 类型特征与SFINAE | 021-TypeTraitsSFINAE | 本文的并列主题 |
| 变参模板 | 022-VariadicTemplate | 本文的并列主题 |
| constexpr与编译期计算 | 023-ConstexprCompileTime | 本文的并列主题 |
| 命名空间与链接 | 024-NamespaceLinkage | 本文的并列主题 |
| C++网络编程 | 025-CppNetworkProgramming | 本文的并列主题 |
| C++ 面向对象进阶 | 026-COOPAdvanced | 本文的并列主题 |
| C++内存模型 | 027-CppMemoryModel | 本文的并列主题 |
| C++图形编程 | 028-CppGraphicsProgramming | 本文自身 |
| C++工具链 | 029-CppToolchain | 本文的并列主题 |
| C++正则表达式 | 030-CppRegex | 本文的并列主题 |
| C++与Python交互 | 031-CppPythonInteraction | 本文的并列主题 |
| C++测试框架 | 032-CppTestFramework | 本文的并列主题 |
| C++与Rust对比 | 033-CppRustComparison | 本文的并列主题 |
| C++23与C++26新特性 | 034-Cpp23Cpp26NewFeatures | 本文的并列主题 |
| C++性能优化 | 035-CppPerformance | 本文的性能延伸 |
| C++序列化 | 036-CppSerialization | 本文的并列主题 |
| C++游戏开发 | 037-CppGameDev | 本文的并列主题 |
| C++嵌入式开发 | 038-CppEmbedded | 本文的并列主题 |
| C++ 内存管理 | 039-CppMemoryManagement | 本文的并列主题 |
| C++代码规范 | 040-CppCodeStyle | 本文的并列主题 |
| C++与WebAssembly | 041-CppWebAssembly | 本文的并列主题 |
| C++反射与元编程 | 042-CppReflectionMetaprogramming | 本文的并列主题 |
| C++数学库 | 043-CppMathLibrary | 本文的并列主题 |
| 智能指针 | 044-SmartPointer | 本文的并列主题 |
| C++ 日期时间 | 045-CppDateTime | 本文的并列主题 |
| C++格式化输出 | 046-CppFormatOutput | 本文的并列主题 |
| C++26 与最新标准 | 047-Cpp26AndLatestStandard | 本文的并列主题 |
| C++ STL 容器与迭代器 | 048-CSTL | 本文的并列主题 |
| 并发编程 | 049-ConcurrentProgramming | 本文的并列主题 |
| RAII资源管理 | 050-CCoreGuidelinesResourceManagement | 本文的并列主题 |
| C++ STL 算法与函数对象 | 051-CSTLAlgorithmAndFunctionObject | 本文的并列主题 |
| 移动语义详解 | 052-MoveSemanticsDetailed | 本文的并列主题 |
| 完美转发与引用折叠 | 053-PerfectForwardingReferenceCollapse | 本文的并列主题 |
| 虚函数表与多态内存布局 | 054-VTablePolymorphismMemoryLayout | 本文的并列主题 |
| 智能指针循环引用 | 055-SmartPointerCircularReference | 本文的并列主题 |
| Lambda捕获详解 | 056-LambdaCaptureDetailed | 本文的并列主题 |
| 类型萃取与SFINAE | 057-TypeExtractionSFINAE | 本文的并列主题 |
| 可变参数模板与折叠表达式 | 058-VariadicTemplateFoldExpression | 本文的并列主题 |
| C++20协程 | 059-Cpp20Coroutine | 本文的并列主题 |
| C++20概念 | 060-Cpp20Concept | 本文的并列主题 |
| C++23新特性 | 061-Cpp23NewFeatures | 本文的并列主题 |
| C++ 模板 | 062-CppTemplate | 本文的并列主题 |
| 内存序与无锁编程 | 063-MemoryOrderLockFree | 本文的并列主题 |
| C++ 异常处理与性能优化 | 064-CppExceptionAndPerformance | 本文的性能延伸 |
| C++ 调试与性能分析 | 065-CDebugPerformanceAnalysis | 本文的性能延伸 |
| C++ 项目实战 | 066-CppProjectPractice | 本文的综合应用 |
| C++ STL 容器使用速查 | 067-STLContainerUsage | 本文的并列主题 |
| C++ 结构化绑定语法速查手册 | 068-StructuredBinding | 本文的并列主题 |
| C++ STL 迭代器 | 069-CppSTLIterator | 本文的并列主题 |
| C++ tuple 与 pair | 070-CppTuplePair | 本文的并列主题 |
| C++ variant / optional / any | 071-CppVariantOptionalAny | 本文的并列主题 |
| C++ CMake 构建命令 | 072-CMakeBuild | 本文的并列主题 |
| C++ 调试命令 | 073-DebugCommand | 本文的并列主题 |
| C++ 链接与符号 | 074-LinkSymbol | 本文的并列主题 |
| C++26 最新标准 | 075-Cpp26LatestStandard | 本文的并列主题 |
| C++20 新特性汇总 | 076-Cpp20Overview | 本文的并列主题 |
