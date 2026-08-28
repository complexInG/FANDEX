# C++ 测试框架

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## GoogleTest

**基本写法：基本测试**
`TEST(<套件>, <用例>)`
```cpp
#include <gtest/gtest.h>
// 简单测试
TEST(MathTest, Add) {
    EXPECT_EQ(1 + 1, 2);
    ASSERT_EQ(2 * 3, 6);
}
// EXPECT_* 失败继续
// ASSERT_* 失败终止当前测试
```

---

**基本写法：测试夹具**
`struct <夹具> : testing::Test { void SetUp() override {} };`
```cpp
// 共享初始化逻辑
class VectorTest : public testing::Test {
protected:
    void SetUp() override { v = {1, 2, 3}; }
    std::vector<int> v;
};
TEST_F(VectorTest, Size) {
    EXPECT_EQ(v.size(), 3u);
}
```

---

**基本写法：参数化测试**
`TEST_P(<夹具>, <用例>)`
```cpp
// 多组参数运行同一测试
class SortTest : public testing::TestWithParam<std::vector<int>> {};
TEST_P(SortTest, Ascending) {
    auto v = GetParam();
    std::sort(v.begin(), v.end());
    EXPECT_TRUE(std::is_sorted(v.begin(), v.end()));
}
INSTANTIATE_TEST_SUITE_P(Data, SortTest,
    testing::Values(std::vector<int>{3,1,2}, std::vector<int>{5,4,3}));
```

---

**基本写法：断言**
`EXPECT_<条件>` `ASSERT_<条件>`
```cpp
// 常用断言
EXPECT_EQ(a, b);    // a == b
EXPECT_NE(a, b);    // a != b
EXPECT_LT(a, b);    // a < b
EXPECT_LE(a, b);    // a <= b
EXPECT_GT(a, b);    // a > b
EXPECT_GE(a, b);    // a >= b
EXPECT_TRUE(cond);
EXPECT_FALSE(cond);
EXPECT_STREQ("hi", s.c_str()); // C 字符串比较
EXPECT_THROW(f(), std::runtime_error); // 期望抛异常
EXPECT_NO_THROW(f());
```

---

**基本写法：Mock**
`MOCK_METHOD(<返回>, <名>, (<参数>));`
```cpp
#include <gmock/gmock.h>
// 定义 Mock 类
class MockDB : public DB {
public:
    MOCK_METHOD(int, query, (const std::string&), (override));
};
// 使用
MockDB db;
EXPECT_CALL(db, query("id")).WillOnce(testing::Return(42));
EXPECT_EQ(db.query("id"), 42);
```

---

## Catch2

**基本写法：基本测试**
`TEST_CASE("<描述>")`
```cpp
#define CATCH_CONFIG_MAIN
#include <catch2/catch_all.hpp>
// 简单测试
TEST_CASE("Addition works") {
    REQUIRE(1 + 1 == 2);
    REQUIRE_FALSE(1 + 1 == 3);
}
```

---

**基本写法：节与用例**
`TEST_CASE("<描述>") { SECTION("<节>") {} }`
```cpp
// 每个节独立执行
TEST_CASE("Vector operations") {
    std::vector<int> v;
    SECTION("push_back increases size") {
        v.push_back(1);
        REQUIRE(v.size() == 1);
    }
    SECTION("empty initially") {
        REQUIRE(v.empty());
    }
}
```

---

**基本写法：BDD 风格**
`SCENARIO("<场景>") { GIVEN() WHEN() THEN() }`
```cpp
// 行为驱动开发风格
SCENARIO("Vector grows") {
    GIVEN("A vector with one item") {
        std::vector<int> v{1};
        WHEN("push_back is called") {
            v.push_back(2);
            THEN("size becomes 2") {
                REQUIRE(v.size() == 2);
            }
        }
    }
}
```

---

**基本写法：生成器**
`GENERATE(<值>...)`
```cpp
// 多组数据测试
TEST_CASE("Squares") {
    int x = GENERATE(1, 2, 3, 4, 5);
    REQUIRE(x * x >= x);
}
```

---

## doctest

**基本写法：基本测试**
`TEST_CASE("<描述>")`
```cpp
#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest.h>
// 轻量级测试框架
TEST_CASE("Quick test") {
    CHECK(2 + 2 == 4);
    CHECK_FALSE(2 + 2 == 5);
}
```

---

## Benchmark

**基本写法：Google Benchmark**
`static void <名>(benchmark::State& state)`
```cpp
#include <benchmark/benchmark.h>
// 性能基准测试
static void BM_StringCopy(benchmark::State& state) {
    std::string src = "hello";
    for (auto _ : state) {
        std::string dst = src;
        benchmark::DoNotOptimize(dst);
    }
}
BENCHMARK(BM_StringCopy);
BENCHMARK_MAIN();
```

---

## CTest 集成

**基本写法：CMake 注册测试**
`add_test(NAME <名> COMMAND <可执行>)`
```cmake
# CMakeLists.txt 中添加测试
enable_testing()
add_executable(unit_test test.cpp)
target_link_libraries(unit_test PRIVATE gtest_main)
include(GoogleTest)
gtest_discover_tests(unit_test)
# 运行测试
# ctest --test-dir build
```

---

**基本写法：运行 CTest**
`ctest [选项]`
```bash
# 运行所有测试
ctest --test-dir build
ctest --test-dir build -j 8        # 并行
ctest --test-dir build -V          # 详细输出
ctest --test-dir build -R MathTest # 按名称过滤
```
