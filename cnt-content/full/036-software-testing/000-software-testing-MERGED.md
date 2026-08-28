---
order: 10
title: software-testing 模块文档合集
module: 'software-testing'
category: 云与基础设施
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：036-software-testing/001-TestBasicsMethod.md ============ -->


## 1. 软件测试概述

### 1.1 定义

软件测试是通过**手动或自动化手段**来运行或检验软件系统的过程，目的是发现软件缺陷、验证软件是否满足需求，并评估软件质量。

### 1.2 测试原则

| 原则                 | 说明                                     |
| :------------------- | :--------------------------------------- |
| **测试显示缺陷存在** | 测试只能证明缺陷存在，不能证明没有缺陷   |
| **穷尽测试不可能**   | 无法测试所有输入组合，需用风险驱动优先级 |
| **尽早测试**         | 缺陷越早发现，修复成本越低               |
| **缺陷集群性**       | 少数模块往往包含大部分缺陷（二八定律）   |
| **杀虫剂悖论**       | 反复使用相同测试用例将无法发现新缺陷     |
| **测试依赖于上下文** | 不同系统需要不同的测试策略               |
| **无错误谬误**       | 没有发现缺陷 ≠ 系统满足用户需求          |

### 1.3 缺陷成本曲线

```mermaid
flowchart TD
    T0["修复成本"]
    T1["╱"]
    T2["╱"]
    T3["╱"]
    T4["╱"]
    T5["╱"]
    T6["╱"]
    T7["╱"]
    T8["╱"]
    T9["╱"]
    T10["时间"]
    T11["需求  设计  编码  单元测试  集成测试  系统测试  发布后"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T0 --> T4
    T0 --> T5
    T0 --> T6
    T0 --> T7
    T0 --> T8
    T0 --> T9
    T9 --> T10
    T10 --> T11
```

## 2. 测试分类

### 2.1 按开发阶段分类

| 类型         | 测试对象     | 执行者    | 关注点             |
| :----------- | :----------- | :-------- | :----------------- |
| **单元测试** | 函数/方法/类 | 开发人员  | 代码逻辑正确性     |
| **集成测试** | 模块间接口   | 开发/测试 | 模块交互与数据传递 |
| **系统测试** | 完整系统     | 测试人员  | 功能、性能、安全   |
| **验收测试** | 交付系统     | 用户/客户 | 是否满足业务需求   |

### 2.2 按测试方法分类

| 类型         | 特点                     | 是否需要代码 |
| :----------- | :----------------------- | :----------- |
| **黑盒测试** | 关注输入输出，不关注内部 | 不需要       |
| **白盒测试** | 关注内部逻辑与结构       | 需要         |
| **灰盒测试** | 部分了解内部结构         | 部分需要     |

### 2.3 按执行方式分类

| 类型           | 说明                  |
| :------------- | :-------------------- |
| **手动测试**   | 人工执行测试用例      |
| **自动化测试** | 使用工具/脚本执行测试 |

### 2.4 按测试目标分类

| 类型           | 说明                 |
| :------------- | :------------------- |
| **功能测试**   | 验证功能是否正确     |
| **性能测试**   | 验证响应时间、吞吐量 |
| **安全测试**   | 验证系统安全性       |
| **兼容性测试** | 验证多环境适配       |
| **易用性测试** | 验证用户体验         |
| **可靠性测试** | 验证长时间运行稳定性 |

## 3. 黑盒测试方法

### 3.1 等价类划分

将输入域划分为**有效等价类**和**无效等价类**，从每个等价类中选取代表值进行测试。

**示例：用户年龄输入（18-60岁）**

| 等价类       | 范围          | 测试数据 |
| :----------- | :------------ | :------- |
| 有效等价类   | 18 ≤ age ≤ 60 | 25       |
| 无效等价类-1 | age < 18      | 10       |
| 无效等价类-2 | age > 60      | 70       |
| 无效等价类-3 | 非数字输入    | "abc"    |
| 无效等价类-4 | 空输入        | ""       |

```python
# 等价类划分测试用例示例
import pytest

def validate_age(age_input):
    """验证年龄输入"""
    if not age_input:
        raise ValueError("年龄不能为空")
    try:
        age = int(age_input)
    except ValueError:
        raise ValueError("年龄必须为数字")

    if age < 18:
        raise ValueError("年龄不能小于18岁")
    if age > 60:
        raise ValueError("年龄不能大于60岁")
    return age

# 有效等价类测试
def test_valid_age():
    assert validate_age("25") == 25
    assert validate_age("18") == 18   # 边界值
    assert validate_age("60") == 60   # 边界值

# 无效等价类测试
def test_invalid_age_too_young():
    with pytest.raises(ValueError, match="不能小于18岁"):
        validate_age("10")

def test_invalid_age_too_old():
    with pytest.raises(ValueError, match="不能大于60岁"):
        validate_age("70")

def test_invalid_age_not_number():
    with pytest.raises(ValueError, match="必须为数字"):
        validate_age("abc")

def test_invalid_age_empty():
    with pytest.raises(ValueError, match="不能为空"):
        validate_age("")
```

### 3.2 边界值分析

边界值是缺陷最容易出现的区域，需对等价类边界进行重点测试。

**示例：密码长度（6-20位）**

| 边界值   | 数据 | 预期结果 |
| :------- | :--- | :------- |
| 小于下界 | 5位  | 失败     |
| 下界     | 6位  | 成功     |
| 下界+1   | 7位  | 成功     |
| 上界-1   | 19位 | 成功     |
| 上界     | 20位 | 成功     |
| 大于上界 | 21位 | 失败     |

```python
def validate_password(password: str) -> bool:
    """验证密码长度 6-20 位"""
    return 6 <= len(password) <= 20

class TestPasswordBoundary:
    def test_below_min(self):
        assert validate_password("12345") is False    # 5位

    def test_at_min(self):
        assert validate_password("123456") is True    # 6位

    def test_above_min(self):
        assert validate_password("1234567") is True   # 7位

    def test_below_max(self):
        assert validate_password("1" * 19) is True    # 19位

    def test_at_max(self):
        assert validate_password("1" * 20) is True    # 20位

    def test_above_max(self):
        assert validate_password("1" * 21) is False   # 21位
```

### 3.3 因果图法

适用于多条件组合的测试场景，通过分析输入条件（因）与输出结果（果）的逻辑关系设计测试用例。

**基本符号：**

| 符号     | 含义                   |
| :------- | :--------------------- |
| **恒等** | 原因为真，结果为真     |
| **非**   | 原因为真，结果为假     |
| **或**   | 任一原因为真，结果为真 |
| **与**   | 所有原因为真，结果为真 |

**示例：购物折扣规则**

- 条件1：会员用户（C1）
- 条件2：订单金额 > 200（C2）
- 条件3：使用优惠券（C3）
- 结果1：享受8折（E1）：C1 AND C2
- 结果2：减20元（E2）：C3

| 用例 | C1  | C2  | C3  | E1  | E2  |
| :--- | :-- | :-- | :-- | :-- | :-- |
| 1    | Y   | Y   | N   | Y   | N   |
| 2    | Y   | N   | Y   | N   | Y   |
| 3    | N   | Y   | Y   | N   | Y   |
| 4    | Y   | Y   | Y   | Y   | Y   |
| 5    | N   | N   | N   | N   | N   |

### 3.4 错误推测法

基于经验和直觉推测可能存在的错误：

| 经验法则         | 示例                      |
| :--------------- | :------------------------ |
| **特殊字符输入** | `<script>`, `'OR 1=1--`   |
| **空值和 null**  | 空字符串、null、undefined |
| **极端数据**     | 超大文件、超长字符串      |
| **并发操作**     | 同时提交、重复点击        |
| **网络异常**     | 超时、断网、弱网          |
| **时区与日期**   | 跨时区、闰年、2月29日     |

## 4. 白盒测试方法

### 4.1 语句覆盖

确保每条语句至少执行一次：

```python
def calculate(a: int, b: int) -> int:
    if a > 0:           # 语句1
        result = a + b  # 语句2
    else:
        result = a - b  # 语句3
    return result       # 语句4

# 语句覆盖：a=1, b=2 → 执行语句1,2,4（语句3未覆盖）
# 需要补充：a=-1, b=2 → 执行语句1,3,4
```

### 4.2 分支覆盖（判定覆盖）

确保每个判定的真假分支至少执行一次：

```python
# 分支覆盖测试用例
def test_calculate():
    # True 分支
    assert calculate(1, 2) == 3    # a > 0 → True
    # False 分支
    assert calculate(-1, 2) == -3  # a > 0 → False
```

### 4.3 路径覆盖

确保所有可能路径至少执行一次：

```python
def grade(score: int) -> str:
    if score >= 90:          # 判定1
        return "优秀"
    elif score >= 60:        # 判定2
        return "及格"
    else:
        return "不及格"

# 路径1: score=95  → 判定1=True
# 路径2: score=75  → 判定1=False, 判定2=True
# 路径3: score=45  → 判定1=False, 判定2=False
```

### 4.4 覆盖强度对比

| 覆盖类型     | 强度 | 说明                   |
| :----------- | :--- | :--------------------- |
| **语句覆盖** | 最弱 | 每条语句至少执行一次   |
| **分支覆盖** | 中等 | 每个分支至少执行一次   |
| **条件覆盖** | 较强 | 每个条件的真假各取一次 |
| **路径覆盖** | 最强 | 所有路径至少执行一次   |

## 5. 测试用例设计

### 5.1 测试用例模板

| 字段         | 说明                          |
| :----------- | :---------------------------- |
| **用例编号** | TC-模块-序号，如 TC-LOGIN-001 |
| **用例标题** | 简明描述测试目的              |
| **前置条件** | 执行前需满足的条件            |
| **测试步骤** | 详细操作步骤                  |
| **测试数据** | 输入数据                      |
| **预期结果** | 期望的输出或行为              |
| **优先级**   | 高/中/低                      |

### 5.2 测试用例示例

| 字段         | 内容                                                  |
| :----------- | :---------------------------------------------------- |
| **编号**     | TC-LOGIN-001                                          |
| **标题**     | 正确用户名和密码登录                                  |
| **前置条件** | 用户已注册，账号：admin / 密码：123456                |
| **步骤**     | 1. 打开登录页面 2. 输入用户名 3. 输入密码 4. 点击登录 |
| **数据**     | 用户名：admin，密码：123456                           |
| **预期**     | 登录成功，跳转首页                                    |
| **优先级**   | 高                                                    |

| 字段         | 内容                                                      |
| :----------- | :-------------------------------------------------------- |
| **编号**     | TC-LOGIN-002                                              |
| **标题**     | 错误密码登录                                              |
| **前置条件** | 用户已注册                                                |
| **步骤**     | 1. 打开登录页面 2. 输入用户名 3. 输入错误密码 4. 点击登录 |
| **数据**     | 用户名：admin，密码：wrong                                |
| **预期**     | 提示"用户名或密码错误"                                    |
| **优先级**   | 高                                                        |

## 6. 测试计划编写

### 6.1 测试计划结构

```
1. 引言
   1.1 编写目的
   1.2 项目背景
   1.3 术语定义
2. 测试范围
   2.1 测试对象
   2.2 测试功能
   2.3 不测试功能
3. 测试策略
   3.1 测试类型与方法
   3.2 测试工具
   3.3 测试环境
4. 测试进度
   4.1 里程碑
   4.2 时间安排
5. 风险与应对
6. 测试交付物
```

### 6.2 测试进度示例

| 阶段         | 时间    | 交付物       |
| :----------- | :------ | :----------- |
| **需求分析** | 第1周   | 测试计划     |
| **用例设计** | 第2-3周 | 测试用例     |
| **用例评审** | 第3周末 | 评审记录     |
| **测试执行** | 第4-6周 | 缺陷报告     |
| **回归测试** | 第7周   | 回归测试报告 |
| **验收测试** | 第8周   | 验收报告     |

## 7. 测试报告编写

### 7.1 测试报告结构

```
1. 概述
   1.1 测试目的
   1.2 测试范围
   1.3 测试环境
2. 测试结果
   2.1 用例执行统计
   2.2 缺陷统计
   2.3 测试覆盖率
3. 缺陷分析
   3.1 缺陷分布
   3.2 严重程度分布
   3.3 未解决缺陷
4. 测试结论与建议
```

### 7.2 缺陷严重程度

| 等级     | 说明                     | 示例                 |
| :------- | :----------------------- | :------------------- |
| **致命** | 系统崩溃、数据丢失       | 支付失败、系统宕机   |
| **严重** | 主要功能不可用           | 无法登录、搜索无结果 |
| **一般** | 次要功能异常             | 排序错误、样式偏移   |
| **轻微** | 界面文字错误、建议性修改 | 拼写错误、对齐不齐   |

### 7.3 测试结果统计模板

| 指标         | 数值 | 百分比 |
| :----------- | :--- | :----- |
| **总用例数** | 500  | -      |
| **通过**     | 420  | 84%    |
| **失败**     | 50   | 10%    |
| **阻塞**     | 15   | 3%     |
| **未执行**   | 15   | 3%     |
| **缺陷总数** | 65   | -      |
| **已修复**   | 55   | 84.6%  |
| **未修复**   | 10   | 15.4%  |



<!-- ============ 文档分隔线：036-software-testing/002-FunctionalAndAutomatedTest.md ============ -->



## 1. 功能测试执行

### 1.1 功能测试流程

```
需求分析 → 用例设计 → 用例评审 → 测试执行 → 缺陷提交 → 回归验证 → 测试报告
```

### 1.2 功能测试要点

| 要点         | 说明                           |
| :----------- | :----------------------------- |
| **正向验证** | 验证功能正常流程是否正确       |
| **逆向验证** | 验证异常输入是否正确处理       |
| **边界验证** | 验证边界值和临界条件           |
| **交互验证** | 验证功能间的联动和影响         |
| **数据验证** | 验证数据的增删改查和一致性     |
| **兼容验证** | 验证不同浏览器/设备/系统的表现 |

### 1.3 缺陷报告

```yaml
缺陷编号: BUG-2026-001
标题: 用户登录后页面跳转失败
严重程度: 严重
优先级: 高
复现步骤: 1. 打开登录页面
  2. 输入正确用户名和密码
  3. 点击登录按钮
预期结果: 跳转到首页
实际结果: 停留在登录页面，控制台报 500 错误
环境: Chrome 120 / Windows 11 / 测试环境
附件: screenshot.png
```

## 2. Selenium 测试框架

### 2.1 Selenium 体系

| 组件                   | 说明               |
| :--------------------- | :----------------- |
| **Selenium WebDriver** | 浏览器自动化驱动   |
| **Selenium IDE**       | 浏览器录制回放插件 |
| **Selenium Grid**      | 分布式并行测试     |

### 2.2 环境搭建

```bash
# 安装 Selenium
pip install selenium

# 下载浏览器驱动（或使用 webdriver-manager 自动管理）
pip install webdriver-manager
```

### 2.3 WebDriver 基础操作

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 初始化浏览器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 打开页面
driver.get("https://www.example.com/login")

# 获取页面信息
print(driver.title)
print(driver.current_url)

# 退出浏览器
driver.quit()
```

### 2.4 元素定位策略

```python
from selenium.webdriver.common.by import By

# ID 定位（推荐，最快）
element = driver.find_element(By.ID, "username")

# Name 定位
element = driver.find_element(By.NAME, "password")

# Class 定位
element = driver.find_element(By.CLASS_NAME, "btn-primary")

# CSS 选择器（推荐，灵活）
element = driver.find_element(By.CSS_SELECTOR, "#login-form input[type='text']")
element = driver.find_element(By.CSS_SELECTOR, "div.card > h2.title")

# XPath 定位（最强大）
element = driver.find_element(By.XPATH, "//input[@id='username']")
element = driver.find_element(By.XPATH, "//button[contains(text(), '登录')]")
element = driver.find_element(By.XPATH, "//form[@id='login']//input[1]")

# Link Text 定位
element = driver.find_element(By.LINK_TEXT, "忘记密码")
element = driver.find_element(By.PARTIAL_LINK_TEXT, "忘记")

# Tag Name 定位
elements = driver.find_elements(By.TAG_NAME, "input")
```

### 2.5 定位策略对比

| 策略      | 速度 | 可读性 | 稳定性 | 推荐场景       |
| :-------- | :--- | :----- | :----- | :------------- |
| **ID**    | 最快 | 高     | 高     | 有唯一 ID 时   |
| **CSS**   | 快   | 中     | 高     | 通用首选       |
| **XPath** | 较慢 | 低     | 中     | 复杂定位       |
| **Name**  | 快   | 高     | 中     | 表单元素       |
| **Class** | 快   | 中     | 低     | 不推荐单独使用 |

### 2.6 显式等待

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 显式等待（推荐）
wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)

# 等待元素可见
element = wait.until(EC.visibility_of_element_located((By.ID, "username")))

# 等待元素可点击
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-login")))

# 等待文本出现
wait.until(EC.text_to_be_present_in_element((By.ID, "message"), "登录成功"))

# 等待页面标题
wait.until(EC.title_contains("首页"))

# 自定义等待条件
wait.until(lambda d: d.find_element(By.ID, "status").get_attribute("data-loaded") == "true")
```

### 2.7 完整登录测试示例

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

class TestLogin:
    """登录功能测试"""

    def setup_method(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.example.com/login")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_login_success(self):
        """正常登录"""
        # 输入用户名
        username = self.wait.until(EC.visibility_of_element_located((By.ID, "username")))
        username.send_keys("admin")

        # 输入密码
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("123456")

        # 点击登录
        login_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn-login")
        login_btn.click()

        # 验证跳转
        self.wait.until(EC.title_contains("首页"))
        assert "首页" in self.driver.title

    def test_login_wrong_password(self):
        """错误密码登录"""
        username = self.wait.until(EC.visibility_of_element_located((By.ID, "username")))
        username.send_keys("admin")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("wrong_password")

        login_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn-login")
        login_btn.click()

        # 验证错误提示
        error_msg = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message"))
        )
        assert "用户名或密码错误" in error_msg.text

    def test_login_empty_fields(self):
        """空字段登录"""
        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-login"))
        )
        login_btn.click()

        # 验证必填提示
        username_error = self.driver.find_element(By.CSS_SELECTOR, "#username-error")
        assert "请输入用户名" in username_error.text
```

## 3. Unittest 测试框架

### 3.1 基础结构

```python
import unittest

class Calculator:
    """被测类"""
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b

class TestCalculator(unittest.TestCase):
    """计算器测试"""

    def setUp(self):
        """每个测试方法前执行"""
        self.calc = Calculator()

    def tearDown(self):
        """每个测试方法后执行"""
        pass

    @classmethod
    def setUpClass(cls):
        """所有测试前执行一次"""
        print("测试开始")

    @classmethod
    def tearDownClass(cls):
        """所有测试后执行一次"""
        print("测试结束")

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2.0)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.333, places=2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

if __name__ == '__main__':
    unittest.main()
```

### 3.2 常用断言

| 断言方法                          | 说明       |
| :-------------------------------- | :--------- |
| `assertEqual(a, b)`               | 相等       |
| `assertNotEqual(a, b)`            | 不相等     |
| `assertTrue(x)`                   | 为真       |
| `assertFalse(x)`                  | 为假       |
| `assertIs(a, b)`                  | 是同一对象 |
| `assertIsNone(x)`                 | 为 None    |
| `assertIn(a, b)`                  | a 在 b 中  |
| `assertRaises(Exception)`         | 抛出异常   |
| `assertAlmostEqual(a, b, places)` | 近似相等   |

## 4. pytest 测试框架

### 4.1 基础用法

```python
import pytest

# 简单测试函数
def test_addition():
    assert 1 + 1 == 2

def test_string_upper():
    assert "hello".upper() == "HELLO"

# 参数化测试
@pytest.mark.parametrize("input_val, expected", [
    (1, 2),
    (2, 4),
    (3, 6),
    (0, 0),
    (-1, -2),
])
def test_double(input_val, expected):
    assert input_val * 2 == expected
```

### 4.2 Fixture 机制

```python
import pytest

@pytest.fixture
def sample_data():
    """提供测试数据"""
    return {"name": "张三", "age": 25, "email": "zhangsan@example.com"}

@pytest.fixture
def db_connection():
    """模拟数据库连接"""
    conn = {"connected": True, "data": []}
    yield conn  # yield 之前的代码是 setup
    conn["connected"] = False  # yield 之后的代码是 teardown

def test_user_name(sample_data):
    assert sample_data["name"] == "张三"

def test_db_connection(db_connection):
    assert db_connection["connected"] is True
    db_connection["data"].append("record1")
    assert len(db_connection["data"]) == 1
```

### 4.3 Fixture 作用域

| 作用域       | 说明                         |
| :----------- | :--------------------------- |
| **function** | 每个测试函数执行一次（默认） |
| **class**    | 每个测试类执行一次           |
| **module**   | 每个模块执行一次             |
| **session**  | 整个测试会话执行一次         |

```python
@pytest.fixture(scope="session")
def app_client():
    """整个测试会话只初始化一次"""
    client = create_test_client()
    yield client
    client.close()

@pytest.fixture(scope="module")
def test_db():
    """每个模块初始化一次"""
    db = init_test_db()
    yield db
    db.cleanup()
```

### 4.4 标记（Mark）

```python
import pytest

@pytest.mark.slow
def test_large_dataset():
    """慢速测试"""
    pass

@pytest.mark.smoke
def test_basic_function():
    """冒烟测试"""
    pass

@pytest.mark.skip(reason="功能未实现")
def test_future_feature():
    pass

@pytest.mark.xfail(reason="已知缺陷 BUG-001")
def test_known_bug():
    assert 1 == 2

# 运行指定标记
# pytest -m smoke        只运行冒烟测试
# pytest -m "not slow"   排除慢速测试
```

### 4.5 pytest 配置文件

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
markers =
    smoke: 冒烟测试
    slow: 慢速测试
    regression: 回归测试
```

## 5. 测试数据管理

### 5.1 数据驱动测试

```python
import pytest
import csv
import json

# CSV 数据驱动
def load_test_data_csv(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

# JSON 数据驱动
def load_test_data_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

# 使用数据驱动
@pytest.mark.parametrize("data", load_test_data_json("test_data/login.json"))
def test_login_data_driven(data):
    assert login(data["username"], data["password"]) == data["expected"]
```

### 5.2 测试数据文件

```json
// test_data/login.json
[
  { "username": "admin", "password": "123456", "expected": "success" },
  { "username": "admin", "password": "wrong", "expected": "wrong_password" },
  { "username": "", "password": "123456", "expected": "empty_username" },
  { "username": "admin", "password": "", "expected": "empty_password" },
  { "username": "hack' OR 1=1--", "password": "any", "expected": "invalid_input" }
]
```

## 6. 页面对象模式（POM）

### 6.1 POM 架构

```mermaid
flowchart TD
    T0["project/"]
    T1["pages/              # 页面对象层"]
    T2["base_page.py    # 基础页面"]
    T3["login_page.py   # 登录页面"]
    T4["home_page.py    # 首页"]
    T5["tests/              # 测试层"]
    T6["test_login.py"]
    T7["test_home.py"]
    T8["test_data/          # 数据层"]
    T9["login.json"]
    T0 --> T1
    T4 --> T5
    T7 --> T8
    T8 --> T9
```

### 6.2 基础页面封装

```python
# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """页面基类，封装通用操作"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """查找元素（显式等待）"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """点击元素"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        """输入文本"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """获取文本"""
        return self.find_element(locator).text

    def is_visible(self, locator):
        """元素是否可见"""
        try:
            self.find_element(locator)
            return True
        except Exception:
            return False

    def wait_for_url_contains(self, text):
        """等待 URL 包含指定文本"""
        self.wait.until(EC.url_contains(text))
```

### 6.3 登录页面对象

```python
# pages/login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """登录页面对象"""

    # 元素定位器
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-login")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    REMEMBER_CHECKBOX = (By.ID, "remember")

    # 页面 URL
    URL = "/login"

    def open(self):
        self.driver.get(f"{self.base_url}{self.URL}")
        return self

    def login(self, username: str, password: str):
        """执行登录操作"""
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def get_error_message(self) -> str:
        """获取错误提示"""
        return self.get_text(self.ERROR_MESSAGE)

    def is_login_button_enabled(self) -> bool:
        """登录按钮是否可用"""
        return self.find_element(self.LOGIN_BUTTON).is_enabled()
```

### 6.4 使用 POM 的测试

```python
# tests/test_login.py
import pytest
from pages.login_page import LoginPage

class TestLogin:
    """登录测试 - 使用 POM 模式"""

    def test_login_success(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("admin", "123456")

        # 验证跳转到首页
        assert "首页" in driver.title

    def test_login_wrong_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("admin", "wrong")

        # 验证错误提示
        assert "用户名或密码错误" in login_page.get_error_message()

    @pytest.mark.parametrize("username,password,expected_msg", [
        ("", "123456", "请输入用户名"),
        ("admin", "", "请输入密码"),
        ("admin", "wrong", "用户名或密码错误"),
    ])
    def test_login_invalid(self, driver, username, password, expected_msg):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username, password)
        assert expected_msg in login_page.get_error_message()
```

### 6.5 POM 优势

| 优势         | 说明                                    |
| :----------- | :-------------------------------------- |
| **可维护性** | UI 变更只需修改页面对象，不影响测试用例 |
| **可复用性** | 页面操作方法可在多个测试中复用          |
| **可读性**   | 测试代码更接近业务语言                  |
| **团队协作** | 页面对象与测试用例可并行开发            |



<!-- ============ 文档分隔线：036-software-testing/003-PerformanceInterfaceTest.md ============ -->



## 1. 性能测试概述

### 1.1 性能测试分类

| 类型           | 目标                   | 典型指标           |
| :------------- | :--------------------- | :----------------- |
| **负载测试**   | 系统在预期负载下的表现 | 响应时间、吞吐量   |
| **压力测试**   | 系统的极限承载能力     | 最大并发、崩溃点   |
| **稳定性测试** | 长时间运行的可靠性     | 内存泄漏、性能衰减 |
| **尖峰测试**   | 突发流量下的表现       | 恢复时间、错误率   |
| **容量测试**   | 系统最大处理能力       | 数据量上限         |

### 1.2 性能指标

| 指标           | 英文             | 说明                     |
| :------------- | :--------------- | :----------------------- |
| **响应时间**   | Response Time    | 请求发出到收到响应的时间 |
| **吞吐量**     | Throughput       | 单位时间处理的请求数     |
| **并发用户数** | Concurrent Users | 同时在线的用户数         |
| **TPS**        | Transactions/s   | 每秒事务数               |
| **QPS**        | Queries/s        | 每秒查询数               |
| **错误率**     | Error Rate       | 失败请求占总请求的比例   |
| **CPU 利用率** | CPU Usage        | 服务器 CPU 使用率        |
| **内存利用率** | Memory Usage     | 服务器内存使用率         |

## 2. JMeter 性能测试

### 2.1 JMeter 核心概念

```mermaid
flowchart TD
    T0["测试计划 (Test Plan)"]
    T1["线程组 (Thread Group)        ← 模拟并发用户"]
    T2["HTTP 请求采样器          ← 发送请求"]
    T3["JSON 提取器             ← 提取响应数据"]
    T4["断言                    ← 验证结果"]
    T5["监听器                  ← 收集结果"]
    T6["配置元件"]
    T7["HTTP 请求默认值"]
    T8["CSV 数据文件设置"]
    T9["前置/后置处理器"]
    T0 --> T1
    T5 --> T6
    T8 --> T9
```

### 2.2 JMeter 脚本示例（.jmx 结构）

```xml
<!-- 线程组配置：模拟 100 并发用户 -->
<ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="用户登录压测">
  <intProp name="ThreadGroup.num_threads">100</intProp>
  <intProp name="ThreadGroup.ramp_time">10</intProp>  <!-- 10秒内启动100线程 -->
  <boolProp name="ThreadGroup.same_user_on_next_iteration">true</boolProp>
  <stringProp name="ThreadGroup.on_sample_error">continue</stringProp>
  <elementProp name="ThreadGroup.main_controller" elementType="LoopController">
    <stringProp name="LoopController.loops">50</stringProp>  <!-- 每线程循环50次 -->
  </elementProp>
</ThreadGroup>

<!-- HTTP 请求采样器 -->
<HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="登录接口">
  <stringProp name="HTTPSampler.domain">api.example.com</stringProp>
  <stringProp name="HTTPSampler.port">443</stringProp>
  <stringProp name="HTTPSampler.protocol">https</stringProp>
  <stringProp name="HTTPSampler.path">/api/login</stringProp>
  <stringProp name="HTTPSampler.method">POST</stringProp>
  <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
  <stringProp name="Argument.value">{"username":"admin","password":"123456"}</stringProp>
</HTTPSamplerProxy>
```

### 2.3 JMeter 命令行执行

```bash
# 非GUI模式执行（推荐用于压测）
jmeter -n -t login_test.jmx -l results.jtl -e -o report/

# 参数说明
# -n  非GUI模式
# -t  测试计划文件
# -l  结果日志文件
# -e  生成HTML报告
# -o  报告输出目录

# 远程分布式压测
jmeter -n -t test.jmx -R server1:1099,server2:1099 -l results.jtl
```

### 2.4 性能测试结果分析

| 指标         | 合格标准     | 需关注     | 严重     |
| :----------- | :----------- | :--------- | :------- |
| **响应时间** | < 200ms      | 200ms - 1s | > 1s     |
| **错误率**   | < 0.1%       | 0.1% - 1%  | > 1%     |
| **TPS**      | 满足业务需求 | 接近瓶颈   | 明显下降 |
| **CPU**      | < 70%        | 70% - 85%  | > 85%    |
| **内存**     | < 70%        | 70% - 85%  | > 85%    |

## 3. LoadRunner 性能测试

### 3.1 LoadRunner 组件

| 组件           | 功能               |
| :------------- | :----------------- |
| **VuGen**      | 虚拟用户脚本生成器 |
| **Controller** | 场景设计与执行控制 |
| **Analysis**   | 结果分析与报告生成 |

### 3.2 脚本录制与增强

```c
// LoadRunner 脚本示例（C语言）
Action()
{
    // 事务开始
    lr_start_transaction("login");

    // 设置参数化
    web_submit_data("login",
        "Action=https://api.example.com/login",
        "Method=POST",
        "RecContentType=application/json",
        ITEMDATA,
        "Name=username", "Value={username}", ENDITEM,  // 参数化
        "Name=password", "Value={password}", ENDITEM,
        LAST);

    // 检查点
    web_reg_find("Text=token",
        "SaveCount=token_count",
        LAST);

    // 事务结束
    if (atoi(lr_eval_string("{token_count}")) > 0) {
        lr_end_transaction("login", LR_PASS);
    } else {
        lr_end_transaction("login", LR_FAIL);
    }

    // 思考时间
    lr_think_time(3);

    return 0;
}
```

### 3.3 场景设计

| 场景类型     | 说明                 | 适用     |
| :----------- | :------------------- | :------- |
| **手动场景** | 手动设置虚拟用户数   | 精确控制 |
| **目标场景** | 设定目标指标自动调整 | 目标导向 |
| **真实场景** | 基于生产流量回放     | 接近真实 |

## 4. API 接口测试

### 4.1 接口测试要点

| 测试维度     | 说明                        |
| :----------- | :-------------------------- |
| **功能验证** | 接口返回数据是否正确        |
| **参数验证** | 必填/选填、类型、范围、边界 |
| **异常处理** | 错误码、错误信息是否合理    |
| **安全性**   | 认证、授权、SQL注入、XSS    |
| **性能**     | 响应时间、并发能力          |
| **兼容性**   | 不同版本接口的向下兼容      |

### 4.2 REST Assured（Java）

```java
import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import org.junit.jupiter.api.Test;
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

class UserApiTest {

    @Test
    void testGetUser() {
        given()
            .baseUri("https://api.example.com")
            .header("Authorization", "Bearer token_value")
        .when()
            .get("/users/1")
        .then()
            .statusCode(200)
            .body("id", equalTo(1))
            .body("name", not(emptyString()))
            .body("email", containsString("@"));
    }

    @Test
    void testCreateUser() {
        given()
            .baseUri("https://api.example.com")
            .contentType(ContentType.JSON)
            .body("{\"name\":\"张三\",\"email\":\"zhangsan@example.com\"}")
        .when()
            .post("/users")
        .then()
            .statusCode(201)
            .body("id", greaterThan(0))
            .body("name", equalTo("张三"));
    }

    @Test
    void testUpdateUser() {
        given()
            .baseUri("https://api.example.com")
            .contentType(ContentType.JSON)
            .header("Authorization", "Bearer token_value")
            .body("{\"name\":\"李四\"}")
        .when()
            .put("/users/1")
        .then()
            .statusCode(200)
            .body("name", equalTo("李四"));
    }

    @Test
    void testDeleteUser() {
        given()
            .baseUri("https://api.example.com")
            .header("Authorization", "Bearer token_value")
        .when()
            .delete("/users/1")
        .then()
            .statusCode(204);
    }

    @Test
    void testNotFound() {
        given()
            .baseUri("https://api.example.com")
        .when()
            .get("/users/99999")
        .then()
            .statusCode(404)
            .body("error", equalTo("Not Found"));
    }
}
```

## 5. Postman 工具

### 5.1 请求构建

```
POST https://api.example.com/api/login
Headers:
  Content-Type: application/json
Body (raw JSON):
{
  "username": "admin",
  "password": "123456"
}
```

### 5.2 环境变量

```javascript
// 设置环境变量
pm.environment.set('base_url', 'https://api.example.com');
pm.environment.set('token', pm.response.json().token);

// 获取环境变量
const baseUrl = pm.environment.get('base_url');
const token = pm.environment.get('token');

// 环境配置
// 开发环境: base_url = https://dev.api.example.com
// 测试环境: base_url = https://test.api.example.com
// 生产环境: base_url = https://api.example.com
```

### 5.3 断言脚本

```javascript
// 状态码断言
pm.test('状态码为 200', function () {
  pm.response.to.have.status(200);
});

// 响应体断言
pm.test('返回 token', function () {
  const json = pm.response.json();
  pm.expect(json.token).to.be.a('string');
  pm.expect(json.token.length).to.be.above(0);
});

// 响应头断言
pm.test('Content-Type 为 JSON', function () {
  pm.response.to.have.header('Content-Type', 'application/json; charset=utf-8');
});

// 响应时间断言
pm.test('响应时间小于 500ms', function () {
  pm.expect(pm.response.responseTime).to.be.below(500);
});

// JSON Schema 验证
pm.test('响应符合 Schema', function () {
  const schema = {
    type: 'object',
    required: ['id', 'name', 'email'],
    properties: {
      id: { type: 'integer' },
      name: { type: 'string' },
      email: { type: 'string', format: 'email' },
    },
  };
  pm.expect(tv4.validate(pm.response.json(), schema)).to.be.true;
});
```

### 5.4 Collection Runner

```javascript
// 集合执行顺序与数据传递

// 1. 登录接口 - 保存 token
pm.test('保存 token', function () {
  const json = pm.response.json();
  pm.environment.set('auth_token', json.token);
});

// 2. 后续接口 - 使用 token
// Headers 中: Authorization: Bearer {{auth_token}}

// 3. 数据清理 - 删除测试数据
pm.sendRequest({
  url: pm.environment.get('base_url') + '/test/cleanup',
  method: 'POST',
  header: { Authorization: 'Bearer ' + pm.environment.get('auth_token') },
});
```

## 6. 接口 Mock

### 6.1 Mock 概述

Mock 是模拟接口行为的技术，用于在依赖服务不可用或未开发完成时进行测试。

### 6.2 Python Mock 示例

```python
from unittest.mock import Mock, patch
import pytest
import requests

# 被测函数
def get_user_info(user_id: int) -> dict:
    response = requests.get(f"https://api.example.com/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    return None

# 使用 Mock 测试
class TestGetUserInfo:
    @patch('requests.get')
    def test_get_user_success(self, mock_get):
        # 配置 Mock 返回值
        mock_get.return_value = Mock(
            status_code=200,
            json=lambda: {"id": 1, "name": "张三", "email": "zhangsan@example.com"}
        )

        result = get_user_info(1)

        assert result["id"] == 1
        assert result["name"] == "张三"
        mock_get.assert_called_once_with("https://api.example.com/users/1")

    @patch('requests.get')
    def test_get_user_not_found(self, mock_get):
        mock_get.return_value = Mock(status_code=404, json=lambda: {})

        result = get_user_info(99999)

        assert result is None
```

### 6.3 Flask Mock Server

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# 模拟用户接口
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = {
        1: {"id": 1, "name": "张三", "email": "zhangsan@example.com"},
        2: {"id": 2, "name": "李四", "email": "lisi@example.com"},
    }
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "Not Found"}), 404

# 模拟登录接口
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if data.get("username") == "admin" and data.get("password") == "123456":
        return jsonify({"token": "mock_token_12345", "user_id": 1})
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(port=5000)
```

### 6.4 Mock 工具对比

| 工具              | 类型      | 特点                | 适用场景   |
| :---------------- | :-------- | :------------------ | :--------- |
| **unittest.mock** | Python 库 | 代码级 Mock         | 单元测试   |
| **Flask Mock**    | 轻量服务  | 快速搭建模拟 API    | 开发联调   |
| **WireMock**      | 独立服务  | 丰富的请求匹配规则  | 集成测试   |
| **MockServer**    | 独立服务  | Java 生态，功能强大 | 企业级项目 |
| **Postman Mock**  | 内置功能  | 与 Collection 集成  | API 测试   |



<!-- ============ 文档分隔线：036-software-testing/004-SecurityAndMobileTest.md ============ -->



## 1. 安全测试方法

### 1.1 安全测试分类

| 类型         | 说明                       | 执行者       |
| :----------- | :------------------------- | :----------- |
| **漏洞扫描** | 使用工具自动检测已知漏洞   | 安全工程师   |
| **渗透测试** | 模拟攻击者发现安全弱点     | 渗透测试人员 |
| **合规检查** | 验证是否符合安全标准与法规 | 审计人员     |
| **代码审计** | 审查源代码中的安全问题     | 安全开发人员 |

### 1.2 OWASP Top 10

| 排名 | 风险                        | 测试方法                    |
| :--- | :-------------------------- | :-------------------------- |
| A01  | **失效的访问控制**          | 越权访问测试、IDOR 测试     |
| A02  | **加密机制失败**            | 传输加密验证、密钥管理检查  |
| A03  | **注入**                    | SQL 注入、XSS、命令注入测试 |
| A04  | **不安全的设计**            | 威胁建模、架构审查          |
| A05  | **安全配置错误**            | 默认配置检查、目录遍历测试  |
| A06  | **过时组件**                | 依赖版本扫描、CVE 检查      |
| A07  | **身份认证失败**            | 暴力破解测试、会话管理测试  |
| A08  | **软件和数据完整性失败**    | CI/CD 安全、更新验证        |
| A09  | **安全日志与监控失败**      | 日志完整性验证、告警测试    |
| A10  | **服务器端请求伪造 (SSRF)** | 内网探测测试、URL 限制绕过  |

### 1.3 SQL 注入测试

```python
# SQL 注入测试用例
sql_injection_payloads = [
    # 经典注入
    "' OR '1'='1",
    "' OR '1'='1' --",
    "' OR '1'='1' /*",
    "1' UNION SELECT NULL--",
    "1' UNION SELECT username,password FROM users--",

    # 盲注
    "' AND 1=1--",
    "' AND 1=2--",
    "' AND SLEEP(5)--",

    # 编码绕过
    "%27%20OR%20%271%27%3D%271",
    "1%27%20UNION%20SELECT%20NULL--",
]

def test_sql_injection(base_url):
    """测试登录接口的 SQL 注入"""
    for payload in sql_injection_payloads:
        response = requests.post(
            f"{base_url}/api/login",
            json={"username": payload, "password": "any"}
        )
        # 不应返回 200（成功登录）
        assert response.status_code != 200, f"SQL注入成功: {payload}"
        # 不应泄露数据库错误信息
        assert "SQL" not in response.text
        assert "syntax error" not in response.text.lower()
```

### 1.4 XSS 测试

```python
# XSS 测试用例
xss_payloads = [
    '<script>alert("XSS")</script>',
    '<img src=x onerror=alert("XSS")>',
    '"><script>alert("XSS")</script>',
    "'-alert('XSS')-'",
    '<svg/onload=alert("XSS")>',
    'javascript:alert("XSS")',
]

def test_xss(base_url):
    """测试评论接口的 XSS"""
    for payload in xss_payloads:
        response = requests.post(
            f"{base_url}/api/comments",
            json={"content": payload},
            headers={"Authorization": "Bearer valid_token"}
        )
        # 响应中不应原样返回未转义的脚本
        assert '<script>' not in response.text
        assert 'onerror=' not in response.text
```

### 1.5 漏洞扫描工具

| 工具           | 类型      | 特点                    |
| :------------- | :-------- | :---------------------- |
| **OWASP ZAP**  | 开源      | 主动/被动扫描，API 支持 |
| **Burp Suite** | 商业+免费 | 功能强大，渗透测试首选  |
| **Nessus**     | 商业      | 基础设施漏洞扫描        |
| **Nuclei**     | 开源      | 基于模板的快速扫描      |
| **Trivy**      | 开源      | 容器镜像漏洞扫描        |

### 1.6 Nuclei 扫描示例

```bash
# 安装 Nuclei
go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest

# 扫描目标
nuclei -u https://example.com -t cves/

# 自定义模板
# templates/custom-xss.yaml
id: custom-xss-test
info:
  name: Custom XSS Test
  severity: medium
http:
  - method: POST
    path:
      - "{{BaseURL}}/api/comments"
    body: 'content=<script>alert(1)</script>'
    matchers:
      - type: word
        words:
          - "<script>alert(1)</script>"
        negative: true
```

## 2. 移动应用测试

### 2.1 Appium 框架

Appium 是跨平台移动应用自动化测试框架，支持 iOS 和 Android：

| 特性         | 说明                         |
| :----------- | :--------------------------- |
| **跨平台**   | 一套 API 适配 iOS 和 Android |
| **多语言**   | 支持 Python、Java、JS 等     |
| **原生支持** | 原生、混合、移动 Web 应用    |
| **无需修改** | 不需要修改应用源码           |

### 2.2 Appium 环境搭建

```bash
# 安装 Appium
npm install -g appium

# 安装 UIAutomator2 驱动（Android）
appium driver install uiautomator2

# 安装 XCUITest 驱动（iOS）
appium driver install xcuitest

# 启动 Appium 服务
appium --address 127.0.0.1 --port 4723
```

### 2.3 Android 自动化测试

```python
from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest

class TestAndroidApp:
    """Android 应用自动化测试"""

    def setup_method(self):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "emulator-5554"
        options.app = "/path/to/app.apk"
        options.app_package = "com.example.myapp"
        options.app_activity = ".MainActivity"
        options.automation_name = "UiAutomator2"
        options.no_reset = False

        self.driver = webdriver.Remote(
            "http://127.0.0.1:4723",
            options=options
        )

    def teardown_method(self):
        self.driver.quit()

    def test_login(self):
        """测试登录流程"""
        # 通过 ID 定位
        username = self.driver.find_element("id", "com.example.myapp:id/username")
        username.send_keys("admin")

        password = self.driver.find_element("id", "com.example.myapp:id/password")
        password.send_keys("123456")

        # 通过 Accessibility ID 定位
        login_btn = self.driver.find_element("accessibility id", "登录")
        login_btn.click()

        # 验证登录成功
        welcome = self.driver.find_element("id", "com.example.myapp:id/welcome_text")
        assert "欢迎" in welcome.text

    def test_scroll_and_click(self):
        """滚动查找并点击"""
        # 使用 UiScrollable 滚动查找
        self.driver.find_element(
            "android uiautomator",
            'new UiScrollable(new UiSelector().scrollable(true))'
            '.scrollIntoView(new UiSelector().text("设置"))'
        ).click()
```

### 2.4 设备兼容性测试

| 维度         | 测试内容                   | 策略              |
| :----------- | :------------------------- | :---------------- |
| **屏幕尺寸** | 不同分辨率和屏幕密度       | 主流设备覆盖      |
| **系统版本** | Android 10-14 / iOS 15-17  | 最低版本+最新版本 |
| **网络环境** | WiFi/4G/5G/弱网/断网       | 模拟网络切换      |
| **内存压力** | 低内存设备运行             | 模拟内存限制      |
| **权限管理** | 授权/拒绝/部分授权         | 全组合测试        |
| **安装升级** | 全新安装/覆盖安装/降级安装 | 版本矩阵          |

### 2.5 移动端性能功耗测试

```bash
# Android 性能分析
# CPU 使用率
adb shell top -n 1 | grep com.example.myapp

# 内存使用
adb shell dumpsys meminfo com.example.myapp

# 电量消耗
adb shell dumpsys batterystats com.example.myapp

# 网络流量
adb shell cat /proc/uid_stat/$(adb shell ps | grep com.example.myapp | awk '{print $2}')/tcp_snd

# 启动时间
adb shell am start -W com.example.myapp/.MainActivity

# FPS 帧率
adb shell dumpsys gfxinfo com.example.myapp
```

## 3. 持续集成中的测试

### 3.1 CI 测试流程

```
代码提交 → 代码扫描 → 单元测试 → 构建打包 → 集成测试 → 部署测试环境 → E2E测试 → 报告
```

### 3.2 GitHub Actions 测试配置

```yaml
# .github/workflows/test.yml
name: Test Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  unit-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run unit tests
        run: pytest tests/unit/ -v --cov=src --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          file: coverage.xml

  integration-test:
    needs: unit-test
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: test
        ports:
          - 5432:5432
    steps:
      - uses: actions/checkout@v4
      - name: Run integration tests
        run: pytest tests/integration/ -v
        env:
          DATABASE_URL: postgresql://postgres:test@localhost:5432/testdb

  api-test:
    needs: integration-test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Start API server
        run: |
          docker-compose up -d api
          sleep 10
      - name: Run API tests
        run: newman run postman_collection.json -e test_environment.json

  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Trivy scan
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
      - name: Run Bandit (Python SAST)
        run: |
          pip install bandit
          bandit -r src/ -f json -o bandit-report.json
```

### 3.3 Jenkins 测试流水线

```groovy
// Jenkinsfile
pipeline {
    agent any

    stages {
        stage('代码扫描') {
            steps {
                sh 'sonar-scanner -Dsonar.projectKey=myapp'
            }
        }

        stage('单元测试') {
            steps {
                sh 'pytest tests/unit/ --junitxml=unit-results.xml'
            }
            post {
                always {
                    junit 'unit-results.xml'
                }
            }
        }

        stage('构建') {
            steps {
                sh 'docker build -t myapp:test .'
            }
        }

        stage('集成测试') {
            steps {
                sh 'docker-compose -f docker-compose.test.yml up -d'
                sh 'pytest tests/integration/ --junitxml=integration-results.xml'
            }
            post {
                always {
                    sh 'docker-compose -f docker-compose.test.yml down'
                    junit 'integration-results.xml'
                }
            }
        }

        stage('性能测试') {
            steps {
                sh 'jmeter -n -t perf_test.jmx -l results.jtl'
                publishHTML(target: [
                    reportDir: 'report',
                    reportFiles: 'index.html',
                    reportName: 'Performance Report'
                ])
            }
        }
    }

    post {
        always {
            emailext(
                subject: "构建 ${currentBuild.result}: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "测试报告: ${env.BUILD_URL}",
                to: 'team@example.com'
            )
        }
    }
}
```

## 4. 测试左移与质量内建

### 4.1 测试左移

将测试活动**前移到开发早期**，从源头预防缺陷：

```
传统模式：需求 → 设计 → 编码 → [测试] → 发布
测试左移：[需求评审] → [设计评审] → [TDD] → [持续测试] → 发布
```

| 实践             | 阶段     | 说明                 |
| :--------------- | :------- | :------------------- |
| **需求评审**     | 需求阶段 | 测试人员参与需求评审 |
| **测试用例前置** | 设计阶段 | 在编码前设计测试用例 |
| **TDD**          | 编码阶段 | 先写测试再写实现     |
| **代码审查**     | 编码阶段 | 包含测试代码的审查   |
| **静态分析**     | 编码阶段 | 自动化代码质量检查   |
| **契约测试**     | 集成阶段 | 验证服务间接口契约   |

### 4.2 质量内建

将质量保障融入开发全流程，而非依赖最终测试：

| 原则             | 实践                         |
| :--------------- | :--------------------------- |
| **预防胜于检测** | 代码规范、设计模式、架构评审 |
| **快速反馈**     | 自动化测试、CI 流水线        |
| **全员负责**     | 开发写测试、测试写工具       |
| **持续改进**     | 缺陷复盘、流程优化           |
| **可视化**       | 质量看板、测试覆盖率报告     |

### 4.3 质量门禁

```yaml
# 质量门禁配置示例
quality_gates:
  code_review:
    required_approvals: 2
    must_include_test: true

  unit_test:
    coverage_minimum: 80%
    all_tests_pass: true

  integration_test:
    critical_paths_pass: true
    error_rate_below: 0.1%

  security:
    no_critical_vulnerabilities: true
    no_high_vulnerabilities: true

  performance:
    p95_response_time_below: 500ms
    tps_above: 1000

  deployment:
    canary_success_rate_above: 99.5%
    rollback_on_failure: true
```

### 4.4 测试金字塔

```mermaid
flowchart TD
    E[E2E 测试<br/>少量、慢速、高成本] --> I[集成/接口测试<br/>适量、中速、中成本]
    I --> U[单元测试<br/>大量、快速、低成本]
```

| 层级         | 比例 | 执行时间 | 维护成本 | 覆盖广度 |
| :----------- | :--- | :------- | :------- | :------- |
| **单元测试** | 70%  | 毫秒级   | 低       | 代码逻辑 |
| **集成测试** | 20%  | 秒级     | 中       | 模块交互 |
| **E2E 测试** | 10%  | 分钟级   | 高       | 用户流程 |

### 4.5 测试成熟度模型

| 级别        | 特征                   | 典型实践              |
| :---------- | :--------------------- | :-------------------- |
| **L1 初始** | 手动测试为主，无规范   | 人工执行、无计划      |
| **L2 管理** | 有测试流程和规范       | 测试计划、用例管理    |
| **L3 定义** | 自动化测试覆盖核心功能 | 自动化框架、CI 集成   |
| **L4 量化** | 质量指标可度量、可预测 | 覆盖率监控、质量门禁  |
| **L5 优化** | 持续改进、质量内建     | 测试左移、AI 辅助测试 |



<!-- ============ 文档分隔线：036-software-testing/005-TestConceptPrinciple.md ============ -->


## 1. 测试基础概念

### 1.1 什么是软件测试

软件测试是通过**手动或自动化**手段来运行或检验软件系统的过程，目的是发现缺陷、验证功能、评估质量。

### 1.2 测试目的

| 目的     | 描述                 |
| -------- | -------------------- |
| 发现缺陷 | 找出软件中的错误     |
| 验证功能 | 确认软件满足需求     |
| 评估质量 | 度量软件质量水平     |
| 提供信心 | 为发布提供质量保证   |
| 预防缺陷 | 通过早期测试预防问题 |

### 1.3 测试与调试

| 对比项   | 测试              | 调试     |
| -------- | ----------------- | -------- |
| 目的     | 找缺陷            | 修缺陷   |
| 执行者   | 测试人员/开发人员 | 开发人员 |
| 方式     | 系统化            | 探索式   |
| 可预见性 | 可计划            | 不可预见 |

## 2. 测试七原则

### 原则1：测试显示缺陷的存在

测试只能证明缺陷存在，不能证明缺陷不存在。

### 原则2：穷尽测试不可能

无法测试所有输入组合，需要基于风险选择测试范围。

### 原则3：尽早测试

越早发现缺陷，修复成本越低。

```
需求阶段发现 → 修复成本 1x
设计阶段发现 → 修复成本 5x
编码阶段发现 → 修复成本 10x
测试阶段发现 → 修复成本 20x
生产阶段发现 → 修复成本 100x
```

### 原则4：缺陷集群性

少数模块通常包含大部分缺陷（帕累托法则：80% 的缺陷集中在 20% 的模块中）。

### 原则5：杀虫剂悖论

反复使用相同的测试用例将无法发现新缺陷，需要不断更新和补充测试。

### 原则6：测试依赖于上下文

不同类型的应用需要不同的测试方法。

### 原则7：无错误谬误

没有发现缺陷不等于软件可用，还需要验证是否满足用户需求。

## 3. 测试模型

### 3.1 V 模型

```mermaid
flowchart LR
    A[需求分析] <--> B[验收测试]
    C[系统设计] <--> D[系统测试]
    E[详细设计] <--> F[集成测试]
    G[编码] <--> H[单元测试]
    A --> C --> E --> G
    B --> D --> F --> H
```

### 3.2 W 模型

V 模型的改进，强调测试与开发并行：

```
需求分析 → 需求评审
    ↓           ↓
系统设计 → 系统测试设计
    ↓           ↓
详细设计 → 集成测试设计
    ↓           ↓
  编码   → 单元测试设计
```

### 3.3 敏捷测试

| 特点       | 描述           |
| ---------- | -------------- |
| 持续测试   | 每个迭代都测试 |
| 全团队参与 | 开发和测试协作 |
| 自动化优先 | 快速反馈       |
| 探索性测试 | 补充自动化不足 |

## 4. 测试生命周期

### 4.1 基本过程

```
1. 测试计划 → 确定范围、策略、资源
2. 测试分析 → 分析需求、识别测试条件
3. 测试设计 → 设计测试用例
4. 测试实现 → 编写脚本、准备数据
5. 测试执行 → 运行测试、记录结果
6. 测试评估 → 评估出口准则
7. 测试报告 → 生成测试报告
8. 测试收尾 → 归档、经验总结
```

### 4.2 测试出口准则

| 准则   | 描述                    |
| ------ | ----------------------- |
| 覆盖率 | 代码/需求覆盖率达到目标 |
| 缺陷率 | 未修复缺陷低于阈值      |
| 通过率 | 测试通过率达到目标      |
| 风险   | 剩余风险可接受          |

## 5. 缺陷管理

### 5.1 缺陷生命周期

```
新建 → 已确认 → 已分配 → 修复中 → 已修复 → 已验证 → 已关闭
                    ↓                    ↓
               已拒绝              重新打开
```

### 5.2 缺陷属性

| 属性     | 描述                      |
| -------- | ------------------------- |
| 严重程度 | 致命/严重/一般/轻微       |
| 优先级   | 紧急/高/中/低             |
| 状态     | 新建/已确认/已修复/已关闭 |
| 环境     | 操作系统/浏览器/版本      |

### 5.3 严重程度 vs 优先级

| 严重程度 | 优先级 | 示例               |
| -------- | ------ | ------------------ |
| 致命     | 紧急   | 系统崩溃、数据丢失 |
| 严重     | 高     | 核心功能不可用     |
| 一般     | 中     | 非核心功能异常     |
| 轻微     | 低     | UI 文案错误        |
## coverage.py 基础

**基本写法：运行覆盖率测量**
`coverage run -m pytest`
`coverage report`
`coverage html`

```bash
# 使用 coverage.py 测量 Python 代码覆盖率
coverage run -m pytest
coverage report -m
coverage html
```

---

## coverage 配置

**换行写法：.coveragerc 配置文件**
`[run]`
`source = <包名>`
`omit = <排除路径>`

```ini
# .coveragerc 配置文件
[run]
source = src
branch = True

[report]
exclude_lines =
    pragma: no cover
    raise NotImplementedError
show_missing = True
```

---

## pytest-cov 插件

**基本写法：pytest 集成覆盖率**
`pytest --cov=<模块> [--cov-report=<格式>]`

```bash
# pytest-cov 插件生成覆盖率
pytest --cov=src --cov-report=term-missing
pytest --cov=src --cov-report=html --cov-report=xml
pytest --cov=src --cov-branch --cov-fail-under=80
```

---

## 分支覆盖率

**基本写法：启用分支覆盖率**
`coverage run --branch -m pytest`
`pytest --cov=<模块> --cov-branch`

```bash
# 分支覆盖率测量条件分支
coverage run --branch -m pytest
pytest --cov=src --cov-branch
```

---

## Jest 覆盖率

**基本写法：Jest 生成覆盖率**
`jest --coverage`
`jest --coverage --collectCoverageFrom=<路径>`

```bash
# Jest 覆盖率报告
jest --coverage
jest --coverage --collectCoverageFrom='src/**/*.js'
jest --coverage --coverageReporters=text-summary
```

---

## Jest 覆盖率配置

**换行写法：jest.config.js 覆盖率配置**
`collectCoverageFrom: ["<路径>"]`
`coverageThreshold: { global: { lines: <n> } }`

```javascript
# Jest 覆盖率配置项
module.exports = {
  collectCoverageFrom: ["src/**/*.{js,ts}", "!src/**/*.d.ts"],
  coverageDirectory: "coverage",
  coverageReporters: ["text", "lcov"],
  coverageThreshold: {
    global: { branches: 80, functions: 80, lines: 80, statements: 80 },
  },
};
```

---

## JaCoCo Java 覆盖率

**换行写法：Maven 配置 JaCoCo**
`<plugin>`
`    <groupId>org.jacoco</groupId>`
`    <artifactId>jacoco-maven-plugin</artifactId>`
`</plugin>`

```xml
# pom.xml 配置 JaCoCo 插件
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <executions>
    <execution>
      <goals><goal>prepare-agent</goal></goals>
    </execution>
    <execution>
      <id>report</id>
      <phase>test</phase>
      <goals><goal>report</goal></goals>
    </execution>
  </executions>
</plugin>
```

---

## JaCoCo 命令

**基本写法：运行 JaCoCo 覆盖率**
`mvn clean test`
`mvn jacoco:report`

```bash
# 运行 JaCoCo 生成报告
mvn clean test
mvn jacoco:report
# 报告位于 target/site/jacoco/index.html
```

---

## JaCoCo 阈值检查

**换行写法：设置覆盖率规则**
`<rule>`
`    <element>BUNDLE</element>`
`    <limit><counter>LINE</counter><minimum><n></minimum></limit>`
`</rule>`

```xml
# 强制覆盖率达标
<execution>
  <id>check</id>
  <goals><goal>check</goal></goals>
  <configuration>
    <rules>
      <rule>
        <element>BUNDLE</element>
        <limits>
          <limit>
            <counter>LINE</counter>
            <minimum>0.80</minimum>
          </limit>
        </limits>
      </rule>
    </rules>
  </configuration>
</execution>
```

---

## 覆盖率类型

**基本写法：四种覆盖率指标**
`行覆盖率 | 分支覆盖率 | 函数覆盖率 | 语句覆盖率`

```
# 覆盖率指标说明
行覆盖率 (Lines):      被执行的代码行比例
分支覆盖率 (Branches): 条件分支被执行比例
函数覆盖率 (Functions): 函数被调用比例
语句覆盖率 (Statements): 语句被执行比例
```

---

## 排除文件

**基本写法：排除特定文件**
`coverage run --omit="<模式>" -m pytest`
`pytest --cov=<模块> --cov-config=<文件>`

```bash
# 排除测试文件与第三方代码
coverage run --omit="*/tests/*,*/venv/*" -m pytest
pytest --cov=src --cov-config=.coveragerc
```

---

## 覆盖率报告格式

**基本写法：生成不同格式报告**
`coverage html` | `coverage xml` | `coverage json`
`--cov-report=html|xml|term`

```bash
# 生成多种格式覆盖率报告
coverage html    # HTML 报告到 htmlcov/
coverage xml     # XML 报告
coverage json    # JSON 报告
pytest --cov=src --cov-report=html --cov-report=xml
```

---

## 覆盖率合并

**基本写法：合并多次运行结果**
`coverage combine`
`coverage report`

```bash
# 合并多次测试运行的覆盖率数据
coverage run -m pytest tests/unit
coverage run -a -m pytest tests/integration
coverage combine
coverage report
```



<!-- ============ 文档分隔线：036-software-testing/006-TestLevels.md ============ -->



## 1. 测试金字塔

### 1.1 经典金字塔

```mermaid
flowchart TD
    E[E2E 测试<br/>少量、慢、贵] --> I[集成测试<br/>适量、中速]
    I --> U[单元测试<br/>大量、快、便宜]
```

### 1.2 各层对比

| 层级     | 范围     | 速度 | 成本 | 数量 |
| -------- | -------- | ---- | ---- | ---- |
| 单元测试 | 函数/类  | 毫秒 | 低   | 多   |
| 集成测试 | 模块间   | 秒   | 中   | 适量 |
| 系统测试 | 整体系统 | 分钟 | 高   | 少   |
| 验收测试 | 业务场景 | 分钟 | 高   | 少   |

## 2. 单元测试

### 2.1 定义

对软件中最小可测试单元（函数、方法、类）进行验证。

### 2.2 特点

| 特点   | 描述             |
| ------ | ---------------- |
| 隔离性 | 与外部依赖隔离   |
| 快速   | 毫秒级执行       |
| 自动化 | CI/CD 集成       |
| 可重复 | 任何环境结果一致 |

### 2.3 AAA 模式

```python
def test_user_creation():
    # Arrange（准备）
    user_data = {"name": "Alice", "email": "alice@example.com"}

    # Act（执行）
    user = create_user(user_data)

    # Assert（断言）
    assert user.name == "Alice"
    assert user.email == "alice@example.com"
```

### 2.4 Mock 与 Stub

| 技术 | 描述         | 用途               |
| ---- | ------------ | ------------------ |
| Stub | 返回固定值   | 替换外部依赖       |
| Mock | 验证交互行为 | 验证方法是否被调用 |
| Spy  | 记录调用     | 部分模拟           |
| Fake | 简化实现     | 内存数据库         |

```python
from unittest.mock import Mock, patch

# Stub
db = Mock()
db.get_user.return_value = {"id": 1, "name": "Alice"}

# Mock
email_service = Mock()
create_user(data, email_service)
email_service.send_welcome.assert_called_once_with("alice@example.com")
```

## 3. 集成测试

### 3.1 定义

验证模块间的接口和交互是否正确。

### 3.2 集成策略

| 策略     | 描述               | 优缺点         |
| -------- | ------------------ | -------------- |
| 大爆炸   | 一次性集成所有模块 | 简单但定位困难 |
| 自顶向下 | 从上层模块开始     | 需要 Stub      |
| 自底向上 | 从底层模块开始     | 需要 Driver    |
| 三明治   | 上下同时进行       | 综合方案       |
| 增量式   | 逐步添加模块       | 定位容易       |

### 3.3 集成测试类型

| 类型       | 描述           |
| ---------- | -------------- |
| 组件集成   | 模块间接口测试 |
| 系统集成   | 子系统间测试   |
| API 集成   | 接口契约测试   |
| 数据库集成 | 数据层交互测试 |

### 3.4 示例

```python
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_user_api_integration():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # 创建用户
        response = await client.post("/api/users", json={
            "name": "Alice",
            "email": "alice@example.com"
        })
        assert response.status_code == 201
        user_id = response.json()["id"]

        # 查询用户
        response = await client.get(f"/api/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["name"] == "Alice"
```

## 4. 系统测试

### 4.1 定义

对完整系统进行端到端测试，验证是否满足需求规格。

### 4.2 测试类型

| 类型       | 描述               |
| ---------- | ------------------ |
| 功能测试   | 验证功能需求       |
| 非功能测试 | 性能、安全、兼容性 |
| 端到端测试 | 完整业务流程       |

### 4.3 端到端测试示例

```javascript
// Playwright E2E 测试
import { test, expect } from '@playwright/test';

test('user can login and view dashboard', async ({ page }) => {
  await page.goto('/login');
  await page.fill('[name="email"]', 'user@example.com');
  await page.fill('[name="password"]', 'password123');
  await page.click('button[type="submit"]');

  await expect(page).toHaveURL('/dashboard');
  await expect(page.locator('h1')).toContainText('Welcome');
});
```

## 5. 验收测试

### 5.1 定义

由用户或客户验证软件是否满足业务需求。

### 5.2 类型

| 类型       | 描述                 | 执行者   |
| ---------- | -------------------- | -------- |
| Alpha 测试 | 开发环境中的用户测试 | 内部用户 |
| Beta 测试  | 生产环境中的用户测试 | 外部用户 |
| UAT        | 用户验收测试         | 业务用户 |
| 合同验收   | 合同要求验证         | 客户代表 |

### 5.3 验收准则

```gherkin
Feature: 用户登录
  Scenario: 成功登录
    Given 用户在登录页面
    When 输入正确的用户名和密码
    Then 跳转到首页
    And 显示欢迎消息

  Scenario: 密码错误
    Given 用户在登录页面
    When 输入错误的密码
    Then 显示错误提示
    And 仍在登录页面
```

## 6. 测试层级选择

| 场景     | 推荐层级          |
| -------- | ----------------- |
| 日常开发 | 单元测试为主      |
| API 开发 | 单元+集成测试     |
| Web 应用 | 单元+集成+E2E     |
| 微服务   | 契约测试+集成测试 |
| 关键业务 | 全层级覆盖        |



<!-- ============ 文档分隔线：036-software-testing/007-TestType.md ============ -->



## 1. 功能测试

### 1.1 定义

验证软件功能是否符合需求规格说明。

### 1.2 黑盒测试方法

| 方法       | 描述                      |
| ---------- | ------------------------- |
| 等价类划分 | 将输入分为有效/无效等价类 |
| 边界值分析 | 测试边界条件              |
| 决策表     | 组合条件测试              |
| 状态转换   | 状态变迁测试              |
| 用例测试   | 基于用例场景              |

### 1.3 功能测试流程

```
需求分析 → 测试用例设计 → 测试执行 → 缺陷报告 → 回归验证
```

## 2. 性能测试

### 2.1 类型

| 类型       | 描述               | 指标             |
| ---------- | ------------------ | ---------------- |
| 负载测试   | 正常负载下的表现   | 响应时间、吞吐量 |
| 压力测试   | 超出负载的表现     | 系统极限         |
| 稳定性测试 | 长时间运行的稳定性 | 内存泄漏         |
| 并发测试   | 多用户同时访问     | 并发数           |
| 容量测试   | 最大处理能力       | 最大用户数       |

### 2.2 关键指标

| 指标       | 描述             | 目标          |
| ---------- | ---------------- | ------------- |
| 响应时间   | 请求到响应的时间 | < 200ms (P95) |
| 吞吐量     | 单位时间处理量   | QPS/TPS       |
| 并发用户   | 同时在线用户数   | 根据业务      |
| 错误率     | 失败请求占比     | < 0.1%        |
| CPU 使用率 | 服务器 CPU 占用  | < 70%         |
| 内存使用率 | 服务器内存占用   | < 80%         |

### 2.3 性能测试流程

```
1. 需求分析 → 确定性能指标
2. 测试设计 → 设计场景
3. 环境搭建 → 模拟生产环境
4. 脚本开发 → 编写测试脚本
5. 执行测试 → 运行并监控
6. 结果分析 → 分析瓶颈
7. 优化验证 → 优化后复测
```

## 3. 安全测试

### 3.1 测试内容

| 类型     | 描述               |
| -------- | ------------------ |
| 漏洞扫描 | 自动化扫描已知漏洞 |
| 渗透测试 | 模拟攻击者入侵     |
| 认证测试 | 验证认证机制       |
| 授权测试 | 验证权限控制       |
| 数据加密 | 验证加密实现       |
| 会话管理 | 验证会话安全       |

### 3.2 OWASP 测试清单

| 类别 | 测试项            |
| ---- | ----------------- |
| 注入 | SQL/XSS/命令注入  |
| 认证 | 弱密码/会话固定   |
| 授权 | 越权/IDOR         |
| 配置 | 默认配置/信息泄露 |
| 加密 | 弱加密/证书问题   |

## 4. 兼容性测试

### 4.1 测试维度

| 维度     | 示例                                |
| -------- | ----------------------------------- |
| 浏览器   | Chrome, Firefox, Safari, Edge       |
| 操作系统 | Windows, macOS, Linux, iOS, Android |
| 分辨率   | 1920×1080, 1366×768, 375×812        |
| 设备     | PC, 平板, 手机                      |

### 4.2 浏览器兼容性

| 浏览器  | 版本策略        |
| ------- | --------------- |
| Chrome  | 最近 2 个主版本 |
| Firefox | 最近 2 个主版本 |
| Safari  | 最近 2 个主版本 |
| Edge    | 最新版          |

### 4.3 响应式测试断点

| 断点       | 设备     |
| ---------- | -------- |
| < 576px    | 手机     |
| 576-768px  | 平板竖屏 |
| 768-992px  | 平板横屏 |
| 992-1200px | 小桌面   |
| > 1200px   | 大桌面   |

## 5. 其他测试类型

### 5.1 回归测试

验证修改后的代码没有引入新缺陷。

| 策略       | 描述             |
| ---------- | ---------------- |
| 全量回归   | 执行所有测试用例 |
| 选择性回归 | 执行受影响的用例 |
| 自动化回归 | CI/CD 自动执行   |

### 5.2 冒烟测试

验证基本功能是否正常，决定是否进行深入测试。

### 5.3 探索性测试

不预先编写用例，基于经验和直觉进行探索式测试。

| 特点 | 描述         |
| ---- | ------------ |
| 学习 | 了解系统行为 |
| 设计 | 即时设计测试 |
| 执行 | 执行并观察   |
| 反馈 | 根据结果调整 |

### 5.4 无障碍测试

| 标准       | 描述           |
| ---------- | -------------- |
| WCAG 2.1   | Web 无障碍标准 |
| 键盘导航   | 仅用键盘操作   |
| 屏幕阅读器 | 语音辅助       |
| 颜色对比度 | 4.5:1 (AA)     |
| ARIA       | 无障碍标签     |

### 5.5 本地化/国际化测试

| 测试项   | 描述         |
| -------- | ------------ |
| 语言翻译 | 界面文字正确 |
| 日期格式 | 各地区格式   |
| 货币符号 | 正确显示     |
| 字符编码 | Unicode 支持 |
| 布局适配 | 文字长度变化 |

## 6. 测试类型选择矩阵

| 项目阶段 | 推荐类型       |
| -------- | -------------- |
| 开发期   | 单元+集成      |
| 发布前   | 功能+性能+安全 |
| 发布后   | 监控+回归      |
| 迭代中   | 冒烟+回归+探索 |



<!-- ============ 文档分隔线：036-software-testing/008-EquivalenceClassPartition.md ============ -->



## 1. 等价类划分原理

### 1.1 基本概念

等价类划分是将输入域划分为若干等价类，从每个等价类中选取代表性值作为测试用例。同一等价类中的值对揭露缺陷的效果相同。

### 1.2 核心假设

如果某个等价类中的一个值能发现缺陷，则该类中其他值也能发现；反之，如果某个值不能发现缺陷，则该类中其他值也不能。

### 1.3 优势

| 优势       | 描述                 |
| ---------- | -------------------- |
| 减少用例数 | 每个等价类只取代表值 |
| 提高效率   | 避免冗余测试         |
| 系统化     | 有规律的划分方法     |
| 覆盖全面   | 有效+无效等价类      |

## 2. 有效等价类与无效等价类

### 2.1 定义

| 类型       | 定义                 | 示例（年龄 1-120）  |
| ---------- | -------------------- | ------------------- |
| 有效等价类 | 符合需求的输入集合   | 25（1 ≤ age ≤ 120） |
| 无效等价类 | 不符合需求的输入集合 | -1, 0, 121, "abc"   |

### 2.2 划分规则

| 输入条件 | 有效等价类 | 无效等价类         |
| -------- | ---------- | ------------------ |
| 范围     | 范围内     | 小于下界、大于上界 |
| 枚举     | 枚举值之一 | 非枚举值           |
| 布尔     | true/false | 非布尔值           |
| 必填     | 有值       | 空值               |
| 格式     | 符合格式   | 不符合格式         |

## 3. 等价类划分实例

### 3.1 实例1：用户名注册

**需求**：用户名长度 6-20 个字符，仅允许字母、数字和下划线。

| 等价类         | 类型 | 值           |
| -------------- | ---- | ------------ |
| 长度 6-20      | 有效 | "user01"     |
| 长度 < 6       | 无效 | "usr"        |
| 长度 > 20      | 无效 | "a"\*21      |
| 字母数字下划线 | 有效 | "user_name1" |
| 含特殊字符     | 无效 | "user@name"  |
| 空值           | 无效 | ""           |

**测试用例**：

| 用例 | 输入        | 预期结果     | 覆盖等价类        |
| ---- | ----------- | ------------ | ----------------- |
| TC1  | "user01"    | 注册成功     | 有效长度+有效字符 |
| TC2  | "usr"       | 提示过短     | 无效长度（短）    |
| TC3  | 21个a       | 提示过长     | 无效长度（长）    |
| TC4  | "user@name" | 提示非法字符 | 无效字符          |
| TC5  | ""          | 提示必填     | 空值              |

### 3.2 实例2：日期输入

**需求**：输入年份（1900-2100）、月份（1-12）、日期。

| 输入            | 有效等价类   | 无效等价类           |
| --------------- | ------------ | -------------------- |
| 年份            | 1900-2100    | <1900, >2100, 非数字 |
| 月份            | 1-12         | 0, 13, 非数字        |
| 日期            | 1-28（通用） | 0, 29+, 非数字       |
| 日期（31天月）  | 29-31        | 32+                  |
| 日期（30天月）  | 29-30        | 31                   |
| 日期（2月平年） | 29           | 29（闰年才有效）     |

### 3.3 实例3：购物金额折扣

**需求**：

- 金额 < 100：无折扣
- 100 ≤ 金额 < 500：9 折
- 500 ≤ 金额 < 1000：8 折
- 金额 ≥ 1000：7 折

| 等价类            | 类型 | 值    | 预期折扣 |
| ----------------- | ---- | ----- | -------- |
| 0 < 金额 < 100    | 有效 | 50    | 无       |
| 100 ≤ 金额 < 500  | 有效 | 200   | 9折      |
| 500 ≤ 金额 < 1000 | 有效 | 700   | 8折      |
| 金额 ≥ 1000       | 有效 | 1500  | 7折      |
| 金额 ≤ 0          | 无效 | -10   | 错误     |
| 非数字            | 无效 | "abc" | 错误     |

## 4. 等价类与边界值结合

### 4.1 结合策略

等价类划分确定范围，边界值分析选择具体值。

**示例**：输入范围 1-100

| 方法   | 选取值                             |
| ------ | ---------------------------------- |
| 等价类 | 50（有效）, 0（无效）, 101（无效） |
| 边界值 | 0, 1, 2, 99, 100, 101              |
| 结合   | 0, 1, 2, 50, 99, 100, 101          |

### 4.2 完整测试用例设计流程

```
1. 分析需求 → 提取输入条件
2. 划分等价类 → 有效+无效
3. 边界值补充 → 在边界附近取值
4. 组合测试用例 → 覆盖所有等价类
5. 补充异常场景 → 空值、超时等
```

## 5. 多输入组合

### 5.1 组合策略

| 策略     | 描述                 | 用例数 |
| -------- | -------------------- | ------ |
| 全组合   | 所有等价类组合       | 最多   |
| 正交实验 | 正交表选择组合       | 适中   |
| 成对测试 | 每对参数至少组合一次 | 较少   |

### 5.2 成对测试示例

两个参数，各有 3 个等价类：

| 参数     | 等价类                  |
| -------- | ----------------------- |
| 浏览器   | Chrome, Firefox, Safari |
| 操作系统 | Windows, macOS, Linux   |

全组合 9 个，成对测试 3 个即可覆盖所有组合对。

## 6. 最佳实践

| 实践               | 描述                 |
| ------------------ | -------------------- |
| 先有效后无效       | 优先确保正常流程     |
| 每个无效类独立用例 | 避免缺陷掩盖         |
| 结合边界值         | 提高缺陷发现率       |
| 考虑隐含需求       | 非显式约束           |
| 持续更新           | 需求变更时更新等价类 |



<!-- ============ 文档分隔线：036-software-testing/009-BoundaryValueAnalysis.md ============ -->



## 1. 边界值分析原理

### 1.1 基本概念

边界值分析是基于"缺陷往往出现在输入边界"的经验，重点测试边界条件及其附近值。

### 1.2 为什么测试边界

大量缺陷发生在边界条件上：

- 程序员使用 `<` 而非 `<=`
- 数组索引从 0 还是 1 开始
- 循环条件 off-by-one 错误

### 1.3 与等价类划分的关系

边界值分析是等价类划分的补充，在等价类边界处选取测试值。

## 2. 边界值选取

### 2.1 基本边界值

对于范围 $[a, b]$：

| 值      | 描述         |
| ------- | ------------ |
| $a - 1$ | 刚好小于下界 |
| $a$     | 下界         |
| $a + 1$ | 刚好大于下界 |
| 正常值  | 范围内任意值 |
| $b - 1$ | 刚好小于上界 |
| $b$     | 上界         |
| $b + 1$ | 刚好大于上界 |

### 2.2 示例：年龄 1-120

| 值  | 类型             | 预期结果 |
| --- | ---------------- | -------- |
| 0   | 无效（小于下界） | 错误     |
| 1   | 边界（下界）     | 有效     |
| 2   | 边界（下界+1）   | 有效     |
| 60  | 正常值           | 有效     |
| 119 | 边界（上界-1）   | 有效     |
| 120 | 边界（上界）     | 有效     |
| 121 | 无效（大于上界） | 错误     |

### 2.3 健壮性边界值

在基本边界值基础上增加越界值：

| 值      | 描述       |
| ------- | ---------- |
| $a - 2$ | 远小于下界 |
| $a - 1$ | 刚小于下界 |
| $a$     | 下界       |
| $a + 1$ | 下界内侧   |
| $b - 1$ | 上界内侧   |
| $b$     | 上界       |
| $b + 1$ | 刚大于上界 |
| $b + 2$ | 远大于上界 |

## 3. 边界值类型

### 3.1 数值边界

| 场景          | 边界值                                 |
| ------------- | -------------------------------------- |
| 范围 [0, 100] | -1, 0, 1, 99, 100, 101                 |
| 整数范围      | INT_MIN, INT_MIN+1, INT_MAX-1, INT_MAX |
| 浮点数        | 0.0, 最小正值, 最大正值                |

### 3.2 字符串边界

| 场景      | 边界值                                |
| --------- | ------------------------------------- |
| 长度 1-50 | "", "a", "ab", 49字符, 50字符, 51字符 |
| 空字符串  | ""                                    |
| 仅空格    | " "                                   |

### 3.3 集合边界

| 场景     | 边界值         |
| -------- | -------------- |
| 列表索引 | 0, 1, n-2, n-1 |
| 空列表   | []             |
| 单元素   | [1]            |

### 3.4 时间边界

| 场景 | 边界值                       |
| ---- | ---------------------------- |
| 日期 | 1月1日, 12月31日, 2月28/29日 |
| 时间 | 00:00:00, 23:59:59           |
| 时区 | UTC-12, UTC+14               |

## 4. 边界值分析实例

### 4.1 实例1：密码强度

**需求**：密码长度 8-32，必须包含大小写字母和数字。

| 边界    | 长度 | 是否满足 | 预期 |
| ------- | ---- | -------- | ---- |
| 7 字符  | 7    | 否       | 拒绝 |
| 8 字符  | 8    | 是       | 接受 |
| 9 字符  | 9    | 是       | 接受 |
| 31 字符 | 31   | 是       | 接受 |
| 32 字符 | 32   | 是       | 接受 |
| 33 字符 | 33   | 否       | 拒绝 |

### 4.2 实例2：文件上传

**需求**：文件大小 1KB-10MB，仅允许 jpg/png。

| 边界     | 大小     | 预期 |
| -------- | -------- | ---- |
| 0 KB     | 空       | 拒绝 |
| 1 KB     | 下界     | 接受 |
| 10 MB    | 上界     | 接受 |
| 10MB+1KB | 超上界   | 拒绝 |
| .gif     | 非法类型 | 拒绝 |
| .jpg     | 合法类型 | 接受 |

### 4.3 实例3：分页查询

**需求**：每页 10-100 条，页码 ≥ 1。

| 参数     | 边界值 | 预期   |
| -------- | ------ | ------ |
| page=0   | 无效   | 错误   |
| page=1   | 有效   | 第一页 |
| page=2   | 有效   | 第二页 |
| size=9   | 无效   | 错误   |
| size=10  | 有效   | 10条   |
| size=100 | 有效   | 100条  |
| size=101 | 无效   | 错误   |

## 5. 内部边界

### 5.1 数据结构边界

| 场景   | 边界                   |
| ------ | ---------------------- |
| 数组   | 空数组、单元素、满容量 |
| 栈     | 空栈、满栈、单元素     |
| 队列   | 空队列、满队列         |
| 哈希表 | 空表、冲突、扩容阈值   |

### 5.2 状态边界

| 场景   | 边界                 |
| ------ | -------------------- |
| 状态机 | 初始状态、最终状态   |
| 计数器 | 0、最大值、溢出      |
| 超时   | 刚好超时、刚好未超时 |

## 6. 边界值分析最佳实践

| 实践         | 描述               |
| ------------ | ------------------ |
| 识别所有边界 | 显式+隐式边界      |
| 测试两侧     | 边界内外都测       |
| 特殊值       | 0、空、null、负数  |
| 数据类型边界 | INT_MAX、浮点精度  |
| 业务边界     | 折扣阈值、等级分界 |
| 与等价类结合 | 先划分再取边界     |



<!-- ============ 文档分隔线：036-software-testing/010-Selenium.md ============ -->


## 1. Selenium 概述

### 1.1 组件

| 组件      | 描述             |
| --------- | ---------------- |
| WebDriver | 浏览器自动化 API |
| IDE       | 录制回放插件     |
| Grid      | 分布式测试执行   |

### 1.2 WebDriver 架构

```
测试代码 → WebDriver API → Browser Driver → 浏览器
```

## 2. 环境搭建

### 2.1 Python + Selenium

```bash
pip install selenium
pip install pytest
```

### 2.2 基础示例

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

# 查找元素
element = driver.find_element(By.ID, "username")
element.send_keys("admin")

# 点击
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# 断言
assert "Dashboard" in driver.title

driver.quit()
```

## 3. 元素定位

### 3.1 定位策略

| 策略    | By 常量              | 示例                                                 |
| ------- | -------------------- | ---------------------------------------------------- |
| ID      | By.ID                | `find_element(By.ID, "login-btn")`                   |
| Name    | By.NAME              | `find_element(By.NAME, "email")`                     |
| Class   | By.CLASS_NAME        | `find_element(By.CLASS_NAME, "btn-primary")`         |
| CSS     | By.CSS_SELECTOR      | `find_element(By.CSS_SELECTOR, "#login .btn")`       |
| XPath   | By.XPATH             | `find_element(By.XPATH, "//button[@type='submit']")` |
| Tag     | By.TAG_NAME          | `find_element(By.TAG_NAME, "input")`                 |
| Link    | By.LINK_TEXT         | `find_element(By.LINK_TEXT, "Login")`                |
| Partial | By.PARTIAL_LINK_TEXT | `find_element(By.PARTIAL_LINK_TEXT, "Log")`          |

### 3.2 推荐优先级

```
ID > CSS Selector > XPath > 其他
```

## 4. 等待机制

### 4.1 显式等待

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 等待元素可见
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "result"))
)

# 等待元素可点击
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-btn"))
)
```

### 4.2 常用 Expected Conditions

| 条件                            | 描述           |
| ------------------------------- | -------------- |
| `visibility_of_element_located` | 元素可见       |
| `element_to_be_clickable`       | 元素可点击     |
| `presence_of_element_located`   | 元素存在于 DOM |
| `text_to_be_present_in_element` | 文本出现       |
| `title_contains`                | 标题包含       |
| `url_contains`                  | URL 包含       |

### 4.3 隐式等待

```python
driver.implicitly_wait(10)  # 全局等待 10 秒
```

> 注意：不要混用显式和隐式等待。

## 5. Page Object 模式

### 5.1 页面对象

```python
# pages/login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
```

### 5.2 测试用例

```python
# tests/test_login.py
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

class TestLogin:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://example.com/login")
        yield driver
        driver.quit()

    def test_successful_login(self, driver):
        login_page = LoginPage(driver)
        login_page.login("admin", "password123")
        assert "Dashboard" in driver.title

    def test_invalid_password(self, driver):
        login_page = LoginPage(driver)
        login_page.login("admin", "wrong")
        assert "Invalid credentials" in driver.page_source
```

## 6. 高级操作

### 6.1 多窗口

```python
# 切换到新窗口
driver.switch_to.window(driver.window_handles[-1])

# 切换回主窗口
driver.switch_to.window(driver.window_handles[0])
```

### 6.2 iframe

```python
driver.switch_to.frame("iframe-id")
# 操作 iframe 内元素
driver.switch_to.default_content()
```

### 6.3 下拉选择

```python
from selenium.webdriver.support.select import Select

select = Select(driver.find_element(By.ID, "country"))
select.select_by_visible_text("China")
select.select_by_value("CN")
select.select_by_index(0)
```

### 6.4 截图

```python
driver.save_screenshot("screenshot.png")
element.screenshot("element.png")
```

## 7. 最佳实践

| 实践        | 描述                 |
| ----------- | -------------------- |
| Page Object | 封装页面元素和操作   |
| 显式等待    | 避免硬编码 sleep     |
| 数据驱动    | 分离测试数据         |
| 截图失败    | 失败时自动截图       |
| 并行执行    | Grid/多线程          |
| CI 集成     | Headless 模式        |
| 优先 CSS    | CSS 选择器优于 XPath |
## WebDriver 初始化

**换行写法：初始化浏览器驱动**
`from selenium import webdriver`
`driver = webdriver.<Browser>()`

```python
# 初始化各浏览器驱动
from selenium import webdriver

driver = webdriver.Chrome()         # Chrome 浏览器
driver = webdriver.Firefox()        # Firefox 浏览器
driver = webdriver.Edge()           # Edge 浏览器
driver.get("https://example.com")
driver.quit()
```

---

## Options 配置

**换行写法：配置浏览器选项**
`options = webdriver.<Browser>Options()`
`options.add_argument("<参数>")`
`driver = webdriver.<Browser>(options=options)`

```python
# 无头模式与窗口配置
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
```

---

## 元素定位

**基本写法：定位页面元素**
`driver.find_element(By.<方式>, "<值>")`
`driver.find_elements(By.<方式>, "<值>")`

```python
# Selenium 4 元素定位方式
from selenium.webdriver.common.by import By

driver.find_element(By.ID, "username")
driver.find_element(By.NAME, "password")
driver.find_element(By.CLASS_NAME, "btn-primary")
driver.find_element(By.TAG_NAME, "input")
driver.find_element(By.CSS_SELECTOR, "div.container > p")
driver.find_element(By.XPATH, "//div[@id='main']")
```

---

## 元素交互

**基本写法：与元素交互**
`<element>.send_keys(<文本>)`
`<element>.click()`
`<element>.clear()`

```python
# 输入文本、点击与清空
search = driver.find_element(By.NAME, "q")
search.clear()
search.send_keys("Selenium")
search.send_keys(Keys.RETURN)
driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
```

---

## Keys 键盘操作

**基本写法：模拟键盘按键**
`<element>.send_keys(Keys.<KEY>)`

```python
# 模拟键盘按键
from selenium.webdriver.common.keys import Keys

search.send_keys(Keys.ENTER)
search.send_keys(Keys.TAB)
search.send_keys(Keys.CONTROL, "a")
```

---

## ActionChains 鼠标操作

**换行写法：复杂鼠标交互**
`actions = ActionChains(driver)`
`actions.<操作>().perform()`

```python
# 鼠标悬停、右键、双击、拖拽
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)
actions.move_to_element(menu).perform()         # 悬停
actions.context_click(element).perform()        # 右键
actions.double_click(element).perform()         # 双击
actions.drag_and_drop(src, dst).perform()       # 拖拽
```

---

## 等待机制

**换行写法：显式等待**
`from selenium.webdriver.support.ui import WebDriverWait`
`from selenium.webdriver.support import expected_conditions as EC`
`element = WebDriverWait(driver, <秒>).until(EC.<条件>((By.<方式>, "<值>")))`

```python
# 显式等待元素出现
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "result"))
)
```

---

## expected_conditions 常用条件

**基本写法：常用等待条件**
`EC.presence_of_element_located(<定位器>)`
`EC.visibility_of_element_located(<定位器>)`
`EC.element_to_be_clickable(<定位器>)`
`EC.title_contains("<文本>")`

```python
# 常用 EC 条件
EC.presence_of_element_located((By.ID, "x"))
EC.visibility_of_element_located((By.ID, "x"))
EC.element_to_be_clickable((By.ID, "x"))
EC.title_contains("首页")
EC.text_to_be_present_in_element((By.ID, "x"), "hello")
```

---

## 隐式等待

**基本写法：全局隐式等待**
`driver.implicitly_wait(<秒>)`

```python
# 设置全局元素查找超时
driver.implicitly_wait(10)
```

---

## 页面信息

**基本写法：获取页面信息**
`driver.title`
`driver.current_url`
`driver.page_source`

```python
# 获取页面标题、URL、源码
assert "首页" in driver.title
assert driver.current_url.endswith("/home")
html = driver.page_source
```

---

## 元素属性

**基本写法：获取元素属性**
`<element>.text`
`<element>.get_attribute("<属性名>")`
`<element>.is_displayed()`
`<element>.is_enabled()`

```python
# 获取元素文本与属性
element = driver.find_element(By.ID, "msg")
text = element.text
href = element.get_attribute("href")
visible = element.is_displayed()
enabled = element.is_enabled()
```

---

## 窗口与标签页

**基本写法：管理浏览器窗口与标签页**
`driver.switch_to.window(<句柄>)`
`driver.window_handles`
`driver.switch_to.frame(<frame>)`

```python
# 切换窗口与 iframe
driver.switch_to.window(driver.window_handles[1])
driver.switch_to.default_content()
driver.switch_to.frame("frame-name")
driver.switch_to.parent_frame()
```

---

## Alert 弹窗处理

**基本写法：处理 JS 弹窗**
`alert = driver.switch_to.alert`
`alert.accept()` | `alert.dismiss()` | `alert.send_keys("<文本>")`

```python
# 接受、取消、输入 alert 弹窗
alert = driver.switch_to.alert
alert_text = alert.text
alert.send_keys("input")
alert.accept()
alert.dismiss()
```

---

## 截图

**基本写法：保存页面截图**
`driver.save_screenshot("<文件路径>")`
`<element>.screenshot("<文件路径>")`

```python
# 页面截图与元素截图
driver.save_screenshot("page.png")
element = driver.find_element(By.ID, "logo")
element.screenshot("logo.png")
```

---

## pytest 集成

**换行写法：pytest 与 Selenium 集成**
`@pytest.fixture`
`def driver():`
`    driver = webdriver.Chrome()`
`    yield driver`
`    driver.quit()`

```python
# 使用 fixture 管理 WebDriver 生命周期
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_title(driver):
    driver.get("https://example.com")
    assert "Example" in driver.title
```



<!-- ============ 文档分隔线：036-software-testing/011-Pytest.md ============ -->


## 1. pytest 基础

### 1.1 安装

```bash
pip install pytest pytest-cov pytest-mock
```

### 1.2 基本示例

```python
# test_calc.py
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

```bash
pytest test_calc.py -v
```

### 1.3 测试发现规则

| 规则   | 描述                       |
| ------ | -------------------------- |
| 文件名 | `test_*.py` 或 `*_test.py` |
| 类名   | `Test*`（无 `__init__`）   |
| 函数名 | `test_*`                   |

## 2. Fixture

### 2.1 基本用法

```python
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15
```

### 2.2 Fixture 作用域

| 作用域     | 描述                 |
| ---------- | -------------------- |
| `function` | 每个测试函数（默认） |
| `class`    | 每个测试类           |
| `module`   | 每个模块             |
| `session`  | 整个测试会话         |

```python
@pytest.fixture(scope="session")
def db_connection():
    conn = create_connection()
    yield conn
    conn.close()
```

### 2.3 Fixture 依赖

```python
@pytest.fixture
def db(db_connection):
    return Database(db_connection)

@pytest.fixture
def user(db):
    return db.create_user(name="Alice")
```

### 2.4 conftest.py

```python
# conftest.py - 自动发现，无需导入
import pytest

@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()
```

### 2.5 参数化 Fixture

```python
@pytest.fixture(params=["sqlite", "postgresql"])
def db_engine(request):
    engine = create_engine(request.param)
    yield engine
    engine.dispose()

def test_query(db_engine):
    result = db_engine.execute("SELECT 1")
    assert result.fetchone()[0] == 1
```

## 3. 参数化测试

### 3.1 @pytest.mark.parametrize

```python
@pytest.mark.parametrize("input,expected", [
    (1, 1),
    (2, 4),
    (3, 9),
    (-1, 1),
    (0, 0),
])
def test_square(input, expected):
    assert input ** 2 == expected
```

### 3.2 多参数组合

```python
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [10, 20])
def test_multiply(x, y):
    assert x * y > 0
```

### 3.3 参数化 ID

```python
@pytest.mark.parametrize("input,expected", [
    ("hello", "HELLO"),
    ("WORLD", "WORLD"),
], ids=["lowercase", "uppercase"])
def test_upper(input, expected):
    assert input.upper() == expected
```

## 4. 标记（Markers）

### 4.1 内置标记

| 标记                       | 描述       |
| -------------------------- | ---------- |
| `@pytest.mark.skip`        | 跳过测试   |
| `@pytest.mark.skipif`      | 条件跳过   |
| `@pytest.mark.xfail`       | 预期失败   |
| `@pytest.mark.parametrize` | 参数化     |
| `@pytest.mark.slow`        | 自定义标记 |

### 4.2 自定义标记

```python
# pytest.ini
[pytest]
markers =
    slow: slow tests
    integration: integration tests

# 使用
@pytest.mark.slow
def test_large_dataset():
    ...
```

### 4.3 选择执行

```bash
# 运行非 slow 测试
pytest -m "not slow"

# 运行 integration 测试
pytest -m integration

# 组合
pytest -m "integration and not slow"
```

## 5. Mock 与 Patch

### 5.1 unittest.mock

```python
from unittest.mock import Mock, patch

def test_api_call():
    mock_response = Mock()
    mock_response.json.return_value = {"status": "ok"}
    mock_response.status_code = 200

    with patch("requests.get", return_value=mock_response):
        result = fetch_data("https://api.example.com")
        assert result["status"] == "ok"
```

### 5.2 pytest-mock

```python
def test_database_query(mocker):
    mock_db = mocker.patch("app.database.query")
    mock_db.return_value = [{"id": 1, "name": "Alice"}]

    result = get_users()
    assert len(result) == 1
    mock_db.assert_called_once()
```

## 6. 插件生态

| 插件            | 功能        |
| --------------- | ----------- |
| pytest-cov      | 覆盖率      |
| pytest-mock     | Mock 封装   |
| pytest-asyncio  | 异步测试    |
| pytest-django   | Django 集成 |
| pytest-flask    | Flask 集成  |
| pytest-xdist    | 并行执行    |
| pytest-timeout  | 超时控制    |
| pytest-randomly | 随机顺序    |

## 7. 配置

### 7.1 pyproject.toml

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short --strict-markers"
markers = [
    "slow: slow tests",
    "integration: integration tests",
]
```

### 7.2 覆盖率

```bash
pytest --cov=app --cov-report=html --cov-report=term-missing
```

## 8. 最佳实践

| 实践          | 描述               |
| ------------- | ------------------ |
| 命名规范      | `test_` 前缀       |
| 单一断言      | 每个测试一个关注点 |
| AAA 模式      | Arrange-Act-Assert |
| Fixture 复用  | conftest.py 共享   |
| 参数化        | 减少重复代码       |
| Mock 外部依赖 | 隔离测试           |
| 覆盖率目标    | 80%+               |
## pytest 命令行

**基本写法：运行测试**
`pytest [<选项>] [<路径>]`

```bash
# pytest 常用命令
pytest                          # 运行所有测试
pytest test_file.py             # 运行指定文件
pytest -v                       # 详细输出
pytest -s                       # 显示 print 输出
pytest -k "表达式"              # 按表达式筛选
pytest -x                       # 失败立即停止
pytest --maxfail=2              # 失败 N 次停止
pytest --tb=short               # 简短回溯
```

---

## 测试函数定义

**基本写法：以 test_ 开头定义测试**
`def test_<名称>(): <断言>`

```python
# 定义测试函数，函数名须以 test_ 开头
def test_add():
    assert 1 + 1 == 2
```

---

## assert 断言

**基本写法：使用原生 assert**
`assert <表达式>[, <消息>]`

```python
# pytest 使用原生 assert 语句
def test_equal():
    assert 2 + 3 == 5
    assert "hello" in "hello world"
    assert [1, 2] == [1, 2]
```

---

## 测试类

**换行写法：使用类组织测试**
`class Test<名称>:`
`    def test_<方法>(self): <断言>`

```python
# 测试类名须以 Test 开头，不能有 __init__
class TestCalculator:
    def test_add(self):
        assert self.add(1, 2) == 3

    def add(self, a, b):
        return a + b
```

---

## 异常断言

**基本写法：断言抛出异常**
`with pytest.raises(<异常类型>[, match=<正则>]): <调用>`

```python
# 断言代码抛出指定异常
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_value_error():
    with pytest.raises(ValueError, match="invalid"):
        int("abc")
```

---

## 警告断言

**基本写法：断言产生警告**
`with pytest.warns(<警告类型>[, match=<正则>]): <调用>`

```python
# 断言产生警告
import warnings

def test_warning():
    with pytest.warns(UserWarning):
        warnings.warn("test", UserWarning)
```

---

## fixture 注入

**基本写法：使用 fixture 注入依赖**
`def test_<名称>(<fixture名>): <语句>`

```python
# 通过参数名注入 fixture
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_sum(sample_data):
    assert sum(sample_data) == 6
```

---

## conftest.py 共享 fixture

**基本写法：在 conftest.py 中定义共享 fixture**
`# conftest.py`
`@pytest.fixture`
`def <fixture名>(): <返回值>`

```python
# conftest.py 文件中的 fixture 自动被同目录及子目录测试发现
import pytest

@pytest.fixture
def db_connection():
    conn = create_conn()
    yield conn
    conn.close()
```

---

## 跳过测试

**基本写法：跳过测试用例**
`@pytest.mark.skip(reason="<原因>")`
`@pytest.mark.skipif(<条件>, reason="<原因>")`

```python
# 跳过或条件跳过测试
import pytest

@pytest.mark.skip(reason="未实现")
def test_future():
    pass

@pytest.mark.skipif(sys.platform == "win32", reason="不支持 Windows")
def test_unix_only():
    pass
```

---

## 标记预期失败

**基本写法：标记测试预期失败**
`@pytest.mark.xfail([reason="<原因>"][, raises=<异常>])`

```python
# 标记预期失败的测试
@pytest.mark.xfail(reason="已知 bug")
def test_known_bug():
    assert buggy_func() == 1
```

---

## 自定义标记

**基本写法：自定义标记并筛选**
`@pytest.mark.<标记名>`
`pytest -m <标记名>`

```python
# 自定义标记并按标记筛选
import pytest

@pytest.mark.slow
def test_large_dataset():
    pass

# 运行: pytest -m slow
```

---

## 测试输出捕获

**基本写法：访问捕获的输出**
`capsys.readouterr().out`
`capsys.readouterr().err`

```python
# 捕获 stdout/stderr
def test_output(capsys):
    print("hello")
    captured = capsys.readouterr()
    assert "hello" in captured.out
```

---

## 临时目录

**基本写法：使用临时目录 fixture**
`def test_<名称>(tmp_path): <语句>`
`def test_<名称>(tmp_path_factory): <语句>`

```python
# 使用 tmp_path 创建临时目录
def test_file_write(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("content")
    assert file.read_text() == "content"
```

---

## 退出码

**基本写法：pytest 退出码含义**
`0 全部通过 | 1 部分失败 | 2 中断 | 5 无测试`

```bash
# pytest 退出码: 0 通过, 1 失败, 2 中断, 3 内部错误, 4 命令行错误, 5 无测试
pytest; echo $?
```



<!-- ============ 文档分隔线：036-software-testing/012-JUnit5.md ============ -->


## 1. JUnit 5 概述

### 1.1 架构

| 模块           | 描述                 |
| -------------- | -------------------- |
| JUnit Platform | 测试框架基础平台     |
| JUnit Jupiter  | 新编程模型和扩展模型 |
| JUnit Vintage  | JUnit 3/4 兼容       |

### 1.2 Maven 依赖

```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.10.2</version>
    <scope>test</scope>
</dependency>
```

## 2. 常用注解

| 注解           | 描述               |
| -------------- | ------------------ |
| `@Test`        | 标记测试方法       |
| `@BeforeEach`  | 每个测试前执行     |
| `@AfterEach`   | 每个测试后执行     |
| `@BeforeAll`   | 所有测试前执行一次 |
| `@AfterAll`    | 所有测试后执行一次 |
| `@DisplayName` | 测试显示名称       |
| `@Disabled`    | 禁用测试           |
| `@Nested`      | 嵌套测试类         |
| `@Tag`         | 标签过滤           |
| `@Timeout`     | 超时设置           |

## 3. 断言

### 3.1 标准断言

```java
import static org.junit.jupiter.api.Assertions.*;

@Test
void testAssertions() {
    assertEquals(4, 2 + 2);
    assertNotEquals(5, 2 + 2);
    assertTrue(4 > 3);
    assertFalse(4 < 3);
    assertNull(null);
    assertNotNull(new Object());
    assertThrows(ArithmeticException.class, () -> {
        int result = 1 / 0;
    });
}
```

### 3.2 分组断言

```java
@Test
void testGroupedAssertions() {
    assertAll("person",
        () -> assertEquals("Alice", person.getName()),
        () -> assertEquals(25, person.getAge()),
        () -> assertEquals("alice@example.com", person.getEmail())
    );
}
```

### 3.3 超时断言

```java
@Test
void testTimeout() {
    assertTimeout(Duration.ofMillis(500), () -> {
        Thread.sleep(200);
    });
}
```

## 4. 生命周期

```java
class LifecycleTest {

    @BeforeAll
    static void setupAll() {
        System.out.println("Before all tests");
    }

    @BeforeEach
    void setup() {
        System.out.println("Before each test");
    }

    @Test
    void test1() {
        System.out.println("Test 1");
    }

    @Test
    void test2() {
        System.out.println("Test 2");
    }

    @AfterEach
    void teardown() {
        System.out.println("After each test");
    }

    @AfterAll
    static void teardownAll() {
        System.out.println("After all tests");
    }
}
```

## 5. 参数化测试

### 5.1 基本参数化

```java
@ParameterizedTest
@ValueSource(ints = {1, 2, 3, 4, 5})
void testPositive(int number) {
    assertTrue(number > 0);
}

@ParameterizedTest
@ValueSource(strings = {"hello", "world", "junit"})
void testNonEmpty(String str) {
    assertFalse(str.isEmpty());
}
```

### 5.2 参数来源

| 注解             | 描述         |
| ---------------- | ------------ |
| `@ValueSource`   | 单类型值数组 |
| `@NullSource`    | null 值      |
| `@EmptySource`   | 空值         |
| `@EnumSource`    | 枚举值       |
| `@MethodSource`  | 工厂方法     |
| `@CsvSource`     | CSV 格式     |
| `@CsvFileSource` | CSV 文件     |

### 5.3 CSV 参数化

```java
@ParameterizedTest
@CsvSource({
    "1, 1, 2",
    "2, 3, 5",
    "-1, 1, 0",
    "0, 0, 0"
})
void testAdd(int a, int b, int expected) {
    assertEquals(expected, Calculator.add(a, b));
}
```

### 5.4 MethodSource

```java
@ParameterizedTest
@MethodSource("provideTestData")
void testWithMethodSource(String input, int expected) {
    assertEquals(expected, input.length());
}

static Stream<Arguments> provideTestData() {
    return Stream.of(
        Arguments.of("hello", 5),
        Arguments.of("world", 5),
        Arguments.of("", 0)
    );
}
```

## 6. 嵌套测试

```java
@DisplayName("Stack tests")
class StackTest {

    Stack<String> stack;

    @BeforeEach
    void createStack() {
        stack = new Stack<>();
    }

    @Nested
    @DisplayName("when new")
    class WhenNew {

        @Test
        @DisplayName("is empty")
        void isEmpty() {
            assertTrue(stack.isEmpty());
        }

        @Nested
        @DisplayName("after pushing")
        class AfterPushing {

            @BeforeEach
            void pushElement() {
                stack.push("element");
            }

            @Test
            @DisplayName("is not empty")
            void isNotEmpty() {
                assertFalse(stack.isEmpty());
            }
        }
    }
}
```

## 7. 扩展模型

### 7.1 自定义扩展

```java
public class LoggingExtension implements BeforeEachCallback, AfterEachCallback {
    @Override
    public void beforeEach(ExtensionContext context) {
        System.out.println("Before: " + context.getDisplayName());
    }

    @Override
    public void afterEach(ExtensionContext context) {
        System.out.println("After: " + context.getDisplayName());
    }
}

@ExtendWith(LoggingExtension.class)
class MyTest {
    @Test
    void test() { }
}
```

### 7.2 常用扩展

| 扩展             | 功能         |
| ---------------- | ------------ |
| MockitoExtension | Mockito 集成 |
| SpringExtension  | Spring 集成  |
| TempDirectory    | 临时目录     |

## 8. 最佳实践

| 实践        | 描述               |
| ----------- | ------------------ |
| 命名规范    | `*Test.java`       |
| DisplayName | 使用有意义的名称   |
| 单一断言    | 每个测试一个关注点 |
| 嵌套组织    | 按场景分组         |
| 参数化      | 减少重复代码       |
| 标签过滤    | `@Tag("slow")`     |
| 超时保护    | `@Timeout`         |
## @Test 注解

**基本写法：标记测试方法**
`@Test`
`void <方法名>() { <断言> }`

```java
# 使用 @Test 标记测试方法
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
    @Test
    void testAdd() {
        assertEquals(5, 2 + 3);
    }
}
```

---

## @DisplayName 显示名

**基本写法：设置测试显示名称**
`@DisplayName("<名称>")`

```java
# 为测试类或方法设置友好显示名
@DisplayName("计算器测试")
class CalculatorTest {
    @Test
    @DisplayName("加法应返回正确结果")
    void testAdd() {
        assertEquals(5, 2 + 3);
    }
}
```

---

## @BeforeEach / @AfterEach

**基本写法：每个测试方法前后执行**
`@BeforeEach`
`void <方法>() { <setup> }`
`@AfterEach`
`void <方法>() { <teardown> }`

```java
# 每个测试方法前后执行
import org.junit.jupiter.api.*;

class DatabaseTest {
    @BeforeEach
    void setUp() {
        db = createConnection();
    }

    @AfterEach
    void tearDown() {
        db.close();
    }
}
```

---

## @BeforeAll / @AfterAll

**基本写法：所有测试方法前后执行一次**
`@BeforeAll`
`static void <方法>() { <setup> }`
`@AfterAll`
`static void <方法>() { <teardown> }`

```java
# 所有测试前后执行一次，方法必须为 static
class ServerTest {
    @BeforeAll
    static void startServer() {
        server.start();
    }

    @AfterAll
    static void stopServer() {
        server.stop();
    }
}
```

---

## 生命周期执行顺序

**基本写法：JUnit5 生命周期顺序**
`@BeforeAll → @BeforeEach → @Test → @AfterEach → @AfterAll`

```java
# 生命周期钩子执行顺序示例
class LifecycleTest {
    @BeforeAll  static void initAll() {}
    @BeforeEach void init() {}
    @Test       void test() {}
    @AfterEach  void cleanup() {}
    @AfterAll   static void cleanupAll() {}
}
```

---

## @Disabled 禁用测试

**基本写法：禁用测试方法或类**
`@Disabled(["<原因>"])`

```java
# 禁用测试方法或整个测试类
@Disabled("未实现")
@Test
void testFuture() {
}

@Disabled("维护中")
class MaintenanceTest {
}
```

---

## @Tag 标签过滤

**基本写法：为测试打标签**
`@Tag("<标签名>")`

```java
# 使用标签筛选运行的测试
@Tag("slow")
class LargeDataTest {
    @Test
    @Tag("integration")
    void testLargeQuery() {
    }
}

# 运行: mvn test -Dgroups="slow"
```

---

## @Nested 嵌套测试

**基本写法：嵌套组织测试类**
`@Nested`
`class <内部类> { <测试方法> }`

```java
# 嵌套测试类表达层级关系
class ListTest {
    @Nested
    class WhenEmpty {
        @Test
        void isEmpty() {
            assertTrue(new ArrayList<>().isEmpty());
        }
    }
}
```

---

## @RepeatedTest 重复测试

**基本写法：重复运行测试**
`@RepeatedTest(<次数>[, name="<名称>"])`

```java
# 重复运行同一测试多次
@RepeatedTest(value = 5, name = "重复 {currentRepetition}/{totalRepetitions}")
void testFlaky() {
    assertEquals(4, 2 + 2);
}
```

---

## @ParameterizedTest 参数化

**换行写法：参数化测试**
`@ParameterizedTest`
`@<来源注解>`
`void test_<名称>(<参数>) { <断言> }`

```java
# 参数化测试配合数据来源
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

@ParameterizedTest
@ValueSource(strings = {"", "  "})
void testBlank(String input) {
    assertTrue(input.isBlank());
}
```

---

## @ValueSource 值来源

**基本写法：提供简单值数组**
`@ValueSource(strings = {<值>})`
`@ValueSource(ints = {<值>})`

```java
# 提供基本类型值数组
@ParameterizedTest
@ValueSource(ints = {1, 2, 3})
void testPositive(int n) {
    assertTrue(n > 0);
}
```

---

## @CsvSource CSV 来源

**换行写法：CSV 格式多参数**
`@CsvSource({`
`    "<值1>,<值2>,<期望>",`
`    "<值1>,<值2>,<期望>"`
`})`

```java
# CSV 格式提供多参数
@ParameterizedTest
@CsvSource({
    "1, 2, 3",
    "0, 0, 0",
    "-1, 1, 0"
})
void testAdd(int a, int b, int expected) {
    assertEquals(expected, a + b);
}
```

---

## @MethodSource 方法来源

**换行写法：从工厂方法获取参数**
`@MethodSource("<方法名>")`
`static Stream<Arguments> <方法名>() { return Stream.of(<参数>); }`

```java
# 从静态工厂方法获取复杂参数
@ParameterizedTest
@MethodSource("provideData")
void testAdd(int a, int b, int expected) {
    assertEquals(expected, a + b);
}

static Stream<Arguments> provideData() {
    return Stream.of(
        Arguments.of(1, 2, 3),
        Arguments.of(0, 0, 0)
    );
}
```

---

## AssertAll 分组断言

**基本写法：分组断言一次性报告**
`assertAll(<Executable>...)`

```java
# 分组断言，即使部分失败也全部执行
import static org.junit.jupiter.api.Assertions.*;

@Test
void testUser() {
    User user = new User("Alice", 30);
    assertAll("用户属性",
        () -> assertEquals("Alice", user.getName()),
        () -> assertEquals(30, user.getAge()),
        () -> assertNotNull(user.getEmail())
    );
}
```



<!-- ============ 文档分隔线：036-software-testing/013-APIAutomationTest.md ============ -->


## 1. API 测试概述

### 1.1 什么是 API 测试

API 测试是在没有用户界面的情况下，直接对应用程序编程接口进行测试，验证接口的功能、性能和安全性。

### 1.2 与 UI 测试对比

| 对比项   | API 测试   | UI 测试  |
| -------- | ---------- | -------- |
| 速度     | 快（毫秒） | 慢（秒） |
| 稳定性   | 高         | 低       |
| 覆盖率   | 高         | 中       |
| 维护成本 | 低         | 高       |
| 反馈速度 | 快         | 慢       |

### 1.3 测试层级

```
契约测试 → 功能测试 → 集成测试 → 端到端测试
```

## 2. 工具选型

| 工具              | 语言    | 特点               |
| ----------------- | ------- | ------------------ |
| Postman           | GUI     | 易上手、Collection |
| REST Assured      | Java    | 强大、灵活         |
| Requests + pytest | Python  | 轻量、灵活         |
| SuperTest         | Node.js | JS 生态            |
| Karate            | DSL     | BDD 风格           |
| HttpRunner        | Python  | 中文友好           |

## 3. Python API 测试框架

### 3.1 基础封装

```python
import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None

    def set_token(self, token):
        self.token = token
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def get(self, path, **kwargs):
        return self.session.get(f"{self.base_url}{path}", **kwargs)

    def post(self, path, json=None, **kwargs):
        return self.session.post(f"{self.base_url}{path}", json=json, **kwargs)

    def put(self, path, json=None, **kwargs):
        return self.session.put(f"{self.base_url}{path}", json=json, **kwargs)

    def delete(self, path, **kwargs):
        return self.session.delete(f"{self.base_url}{path}", **kwargs)
```

### 3.2 测试用例

```python
import pytest

@pytest.fixture
def api():
    client = APIClient("https://api.example.com")
    # 登录获取 Token
    response = client.post("/auth/login", json={
        "username": "admin",
        "password": "password123"
    })
    client.set_token(response.json()["token"])
    return client

class TestUserAPI:

    def test_create_user(self, api):
        response = api.post("/api/users", json={
            "name": "Alice",
            "email": "alice@example.com"
        })
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Alice"
        assert "id" in data

    def test_get_user(self, api):
        # 先创建
        create_resp = api.post("/api/users", json={
            "name": "Bob", "email": "bob@example.com"
        })
        user_id = create_resp.json()["id"]

        # 再查询
        response = api.get(f"/api/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["name"] == "Bob"

    def test_update_user(self, api):
        create_resp = api.post("/api/users", json={
            "name": "Charlie", "email": "charlie@example.com"
        })
        user_id = create_resp.json()["id"]

        response = api.put(f"/api/users/{user_id}", json={
            "name": "Charlie Updated"
        })
        assert response.status_code == 200
        assert response.json()["name"] == "Charlie Updated"

    def test_delete_user(self, api):
        create_resp = api.post("/api/users", json={
            "name": "David", "email": "david@example.com"
        })
        user_id = create_resp.json()["id"]

        response = api.delete(f"/api/users/{user_id}")
        assert response.status_code == 204

        # 验证已删除
        get_resp = api.get(f"/api/users/{user_id}")
        assert get_resp.status_code == 404
```

## 4. 断言策略

### 4.1 状态码断言

```python
assert response.status_code == 200
assert response.status_code in [200, 201]
```

### 4.2 响应体断言

```python
# JSON Schema 验证
from jsonschema import validate

schema = {
    "type": "object",
    "required": ["id", "name", "email"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"}
    }
}

validate(instance=response.json(), schema=schema)
```

### 4.3 响应时间断言

```python
assert response.elapsed.total_seconds() < 2.0
```

### 4.4 响应头断言

```python
assert "application/json" in response.headers["Content-Type"]
assert "X-Request-Id" in response.headers
```

## 5. 数据驱动测试

### 5.1 YAML 数据文件

```yaml
# testdata/users.yaml
create_user:
  - name: 'Alice'
    email: 'alice@example.com'
    expected_status: 201
  - name: ''
    email: 'invalid'
    expected_status: 400
  - name: 'Bob'
    email: ''
    expected_status: 400
```

### 5.2 参数化测试

```python
import yaml

@pytest.fixture
def user_test_data():
    with open("testdata/users.yaml") as f:
        return yaml.safe_load(f)["create_user"]

@pytest.mark.parametrize("data", user_test_data(), ids=lambda d: d["name"])
def test_create_user_data_driven(api, data):
    response = api.post("/api/users", json={
        "name": data["name"],
        "email": data["email"]
    })
    assert response.status_code == data["expected_status"]
```

## 6. 契约测试

### 6.1 Pact 框架

```python
from pact import Consumer, Provider

pact = Consumer('WebApp').has_pact_with(Provider('API'))

(pact
 .given('user exists')
 .upon_receiving('a request for user')
 .with_request('GET', '/api/users/1')
 .will_respond_with(200, body={
     'id': 1,
     'name': 'Alice'
 }))

with pact:
    result = api.get('/api/users/1')
    assert result.json()['name'] == 'Alice'
```

## 7. 最佳实践

| 实践     | 描述                    |
| -------- | ----------------------- |
| 分层封装 | Client → Service → Test |
| 数据工厂 | 自动创建测试数据        |
| 清理数据 | 测试后清理              |
| 环境隔离 | 测试环境独立            |
| 幂等设计 | 重复执行结果一致        |
| 并发安全 | 测试间无依赖            |
| 日志记录 | 请求/响应完整记录       |
## requests 基础请求

**基本写法：发送 HTTP 请求**
`import requests`
`requests.<method>(<url>, **<kwargs>)`

```python
# requests 发送各类 HTTP 请求
import requests

r = requests.get("https://api.example.com/users")
r = requests.post("https://api.example.com/users", json={"name": "Alice"})
r = requests.put(url, json=data)
r = requests.delete(url)
```

---

## 响应对象

**基本写法：访问响应内容**
`<response>.status_code`
`<response>.json()`
`<response>.text`
`<response>.headers`

```python
# 访问 HTTP 响应
r = requests.get("https://api.example.com/users")
assert r.status_code == 200
data = r.json()
content = r.text
headers = r.headers
```

---

## 请求参数

**基本写法：传递查询参数与请求体**
`requests.get(<url>, params=<字典>)`
`requests.post(<url>, json=<字典>|data=<字典>)`

```python
# 查询参数与请求体
params = {"page": 1, "size": 10}
r = requests.get(url, params=params)

payload = {"name": "Alice", "age": 30}
r = requests.post(url, json=payload)
r = requests.post(url, data=payload)
```

---

## 请求头与认证

**基本写法：设置请求头与认证**
`requests.get(<url>, headers=<字典>, auth=(<user>, <pass>))`

```python
# 自定义请求头与 Basic 认证
headers = {"Authorization": "Bearer token", "Content-Type": "application/json"}
r = requests.get(url, headers=headers)
r = requests.get(url, auth=("user", "pass"))
```

---

## pytest 集成 API 测试

**换行写法：pytest 测试 API**
`def test_<名称>():`
`    r = requests.<method>(<url>)`
`    assert r.status_code == <期望>`

```python
# pytest 测试 API 接口
import requests

def test_get_users():
    r = requests.get("https://api.example.com/users")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_create_user():
    r = requests.post(url, json={"name": "Alice"})
    assert r.status_code == 201
    assert r.json()["name"] == "Alice"
```

---

## TestClient FastAPI 测试

**换行写法：FastAPI 测试客户端**
`from fastapi.testclient import TestClient`
`client = TestClient(<app>)`
`response = client.<method>("<路径>")`

```python
# FastAPI 内置测试客户端
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello"}
```

---

## responses 模拟 HTTP

**换行写法：使用 responses 拦截请求**
`@responses.activate`
`def test_<名称>():`
`    responses.add(responses.GET, <url>, json=<数据>, status=<状态码>)`

```python
# responses 库模拟 HTTP 响应
import responses
import requests

@responses.activate
def test_mock_api():
    responses.add(
        responses.GET,
        "https://api.example.com/users",
        json={"id": 1},
        status=200,
    )
    r = requests.get("https://api.example.com/users")
    assert r.json() == {"id": 1}
```

---

## httpx 异步测试

**换行写法：httpx 异步客户端**
`async with httpx.AsyncClient() as client:`
`    response = await client.<method>(<url>)`

```python
# httpx 异步 API 测试
import httpx
import pytest

@pytest.mark.asyncio
async def test_async_api():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/users")
        assert response.status_code == 200
```

---

## JSON Schema 验证

**换行写法：验证响应结构**
`from jsonschema import validate`
`validate(instance=<数据>, schema=<schema>)`

```python
# 验证 JSON 响应符合 schema
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
    },
    "required": ["id", "name"],
}

def test_response_schema():
    data = response.json()
    validate(instance=data, schema=schema)
```

---

## 参数化 API 测试

**换行写法：参数化测试多个接口**
`@pytest.mark.parametrize("<参数>", [<数据>])`
`def test_<名称>(<参数>): <调用与断言>`

```python
# 参数化测试多个用例
import pytest
import requests

@pytest.mark.parametrize("user_id, expected_name", [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie"),
])
def test_get_user(user_id, expected_name):
    r = requests.get(f"https://api.example.com/users/{user_id}")
    assert r.json()["name"] == expected_name
```

---

## 会话管理

**换行写法：使用 Session 保持会话**
`s = requests.Session()`
`s.headers.update(<头>)`
`r = s.<method>(<url>)`

```python
# Session 保持 Cookie 与连接
s = requests.Session()
s.headers.update({"Authorization": "Bearer token"})

r = s.post(url, json={"name": "Alice"})
r = s.get(url)  # 复用会话
s.close()
```

---

## 超时与重试

**基本写法：设置超时与自动重试**
`requests.<method>(<url>, timeout=<秒>)`
`from requests.adapters import HTTPAdapter`
`s.mount("<前缀>", HTTPAdapter(max_retries=<n>))`

```python
# 超时设置与自动重试
import requests
from requests.adapters import HTTPAdapter

r = requests.get(url, timeout=5)

s = requests.Session()
adapter = HTTPAdapter(max_retries=3)
s.mount("https://", adapter)
```

---

## pytest-httpserver 本地服务器

**换行写法：启动本地 HTTP 服务器**
`with HTTPServer() as httpserver:`
`    httpserver.expect_request("<路径>").respond_with_json(<数据>)`
`    requests.get(httpserver.url_for("<路径>"))`

```python
# pytest-httpserver 启动本地 Mock 服务器
from pytest_httpserver import HTTPServer
import requests

def test_local_server():
    with HTTPServer() as httpserver:
        httpserver.expect_request("/api").respond_with_json({"ok": True})
        r = requests.get(httpserver.url_for("/api"))
        assert r.json() == {"ok": True}
```



<!-- ============ 文档分隔线：036-software-testing/014-JMeter.md ============ -->



## 1. JMeter 概述

### 1.1 什么是 JMeter

Apache JMeter 是开源的负载测试和性能测量工具，支持多种协议和应用类型。

### 1.2 支持协议

| 协议       | 描述     |
| ---------- | -------- |
| HTTP/HTTPS | Web 应用 |
| FTP        | 文件传输 |
| JDBC       | 数据库   |
| JMS        | 消息队列 |
| SOAP/REST  | Web 服务 |
| TCP        | 原始 TCP |
| SMTP       | 邮件     |

### 1.3 核心概念

| 概念           | 描述               |
| -------------- | ------------------ |
| Test Plan      | 测试计划（顶层）   |
| Thread Group   | 线程组（模拟用户） |
| Sampler        | 采样器（发送请求） |
| Listener       | 监听器（收集结果） |
| Configuration  | 配置元件           |
| Pre-Processor  | 前置处理器         |
| Post-Processor | 后置处理器         |
| Assertion      | 断言               |
| Timer          | 定时器             |

## 2. 测试计划结构

```mermaid
flowchart TD
    T0["Test Plan"]
    T1["Thread Group"]
    T2["HTTP Request Defaults (配置)"]
    T3["CSV Data Set Config (数据)"]
    T4["HTTP Cookie Manager (Cookie)"]
    T5["HTTP Request (采样器)"]
    T6["JSON Path Extractor (后置)"]
    T7["Response Assertion (断言)"]
    T8["HTTP Request (采样器2)"]
    T9["Constant Timer (定时器)"]
    T10["View Results Tree (监听器)"]
    T11["Summary Report"]
    T12["Aggregate Report"]
    T0 --> T1
    T10 --> T11
    T10 --> T12
```

## 3. 线程组配置

### 3.1 基本线程组

| 参数     | 描述                     |
| -------- | ------------------------ |
| 线程数   | 模拟用户数               |
| Ramp-Up  | 启动所有线程的时间（秒） |
| 循环次数 | 重复执行次数             |

**示例**：100 用户，10 秒启动，循环 5 次

```
线程数: 100
Ramp-Up: 10
循环次数: 5
```

### 3.2 Stepping Thread Group

逐步增加负载：

```
初始: 10 用户
每 30 秒增加: 20 用户
最大: 200 用户
持续: 60 秒
逐步减少
```

## 4. 采样器

### 4.1 HTTP 请求

| 参数       | 描述                |
| ---------- | ------------------- |
| 服务器名称 | 目标主机            |
| 端口       | 目标端口            |
| 路径       | URL 路径            |
| 方法       | GET/POST/PUT/DELETE |
| 参数       | 请求参数            |
| Body Data  | 请求体              |

### 4.2 变量与参数化

**用户定义变量**：

| 变量名     | 值                |
| ---------- | ----------------- |
| `base_url` | `api.example.com` |
| `port`     | `443`             |
| `protocol` | `https`           |

**CSV 数据文件**：

```csv
username,password
user1,pass1
user2,pass2
user3,pass3
```

### 4.3 JSON 提取

```
# 从响应中提取 Token
JSON Path: $.token
变量名: auth_token

# 后续请求使用
Header: Authorization: Bearer ${auth_token}
```

## 5. 断言

### 5.1 响应断言

| 类型     | 描述           |
| -------- | -------------- |
| 响应码   | 200, 404 等    |
| 响应文本 | 包含/匹配/等于 |
| 响应头   | 检查头信息     |
| 响应时间 | < 2000ms       |

### 5.2 JSON 断言

```
Assert JSON Path: $.status
Expected Value: success
```

## 6. 监听器

### 6.1 常用监听器

| 监听器               | 描述             |
| -------------------- | ---------------- |
| View Results Tree    | 查看每个请求详情 |
| Summary Report       | 汇总报告         |
| Aggregate Report     | 聚合报告         |
| Response Times Graph | 响应时间图       |
| HTML Report          | HTML 报告        |

### 6.2 关键指标

| 指标       | 描述         |
| ---------- | ------------ |
| Samples    | 采样数       |
| Average    | 平均响应时间 |
| Median     | 中位数       |
| 90% Line   | 90 百分位    |
| 99% Line   | 99 百分位    |
| Min/Max    | 最小/最大    |
| Error%     | 错误率       |
| Throughput | 吞吐量 (QPS) |

## 7. 分布式测试

### 7.1 架构

```mermaid
flowchart TD
    T0["Master (控制端)"]
    T1["Slave 1 (执行端)"]
    T2["Slave 2 (执行端)"]
    T3["Slave 3 (执行端)"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
```

### 7.2 配置步骤

```bash
# Slave 端启动
jmeter-server -Djava.rmi.server.hostname=slave-ip

# Master 瑞执行
jmeter -n -t test_plan.jmx -R slave1,slave2,slave3 -l results.jtl
```

## 8. CLI 模式

```bash
# 非GUI模式执行
jmeter -n -t test_plan.jmx -l results.jtl -e -o report/

# 参数化
jmeter -n -t test_plan.jmx \
  -Jusers=100 \
  -Jrampup=10 \
  -Jduration=300 \
  -l results.jtl

# 生成 HTML 报告
jmeter -g results.jtl -o html-report/
```

## 9. 最佳实践

| 实践       | 描述               |
| ---------- | ------------------ |
| CLI 模式   | 性能测试不用 GUI   |
| 参数化     | 变量替代硬编码     |
| 思考时间   | 模拟真实用户       |
| 断言       | 验证响应正确性     |
| 逐步加压   | 避免突发流量       |
| 监控服务端 | 同时监控服务器资源 |
| 多次运行   | 取平均值           |
| 清理数据   | 测试前清理         |



<!-- ============ 文档分隔线：036-software-testing/015-WhiteBoxTestCoverage.md ============ -->



## 1. 覆盖度层次

### 1.1 语句覆盖

语句覆盖是白盒测试覆盖度的重要组成部分。本节详细介绍语句覆盖的核心概念、工作原理和实际应用。

**关键要点**：

- 语句覆盖的定义与核心原理
- 语句覆盖的实现方式与技术细节
- 语句覆盖在实际场景中的应用与最佳实践
- 语句覆盖的常见问题与解决方案

语句覆盖在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 判定覆盖（分支覆盖）

判定覆盖（分支覆盖）是白盒测试覆盖度的重要组成部分。本节详细介绍判定覆盖（分支覆盖）的核心概念、工作原理和实际应用。

**关键要点**：

- 判定覆盖（分支覆盖）的定义与核心原理
- 判定覆盖（分支覆盖）的实现方式与技术细节
- 判定覆盖（分支覆盖）在实际场景中的应用与最佳实践
- 判定覆盖（分支覆盖）的常见问题与解决方案

判定覆盖（分支覆盖）在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 条件覆盖

条件覆盖是白盒测试覆盖度的重要组成部分。本节详细介绍条件覆盖的核心概念、工作原理和实际应用。

**关键要点**：

- 条件覆盖的定义与核心原理
- 条件覆盖的实现方式与技术细节
- 条件覆盖在实际场景中的应用与最佳实践
- 条件覆盖的常见问题与解决方案

条件覆盖在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 高级覆盖

### 2.1 判定-条件覆盖

判定-条件覆盖是白盒测试覆盖度的重要组成部分。本节详细介绍判定-条件覆盖的核心概念、工作原理和实际应用。

**关键要点**：

- 判定-条件覆盖的定义与核心原理
- 判定-条件覆盖的实现方式与技术细节
- 判定-条件覆盖在实际场景中的应用与最佳实践
- 判定-条件覆盖的常见问题与解决方案

判定-条件覆盖在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 条件组合覆盖

条件组合覆盖是白盒测试覆盖度的重要组成部分。本节详细介绍条件组合覆盖的核心概念、工作原理和实际应用。

**关键要点**：

- 条件组合覆盖的定义与核心原理
- 条件组合覆盖的实现方式与技术细节
- 条件组合覆盖在实际场景中的应用与最佳实践
- 条件组合覆盖的常见问题与解决方案

条件组合覆盖在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 MC/DC

MC/DC是白盒测试覆盖度的重要组成部分。本节详细介绍MC/DC的核心概念、工作原理和实际应用。

**关键要点**：

- MC/DC的定义与核心原理
- MC/DC的实现方式与技术细节
- MC/DC在实际场景中的应用与最佳实践
- MC/DC的常见问题与解决方案

MC/DC在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. MC/DC 详解

### 3.1 定义与要求

定义与要求是白盒测试覆盖度的重要组成部分。本节详细介绍定义与要求的核心概念、工作原理和实际应用。

**关键要点**：

- 定义与要求的定义与核心原理
- 定义与要求的实现方式与技术细节
- 定义与要求在实际场景中的应用与最佳实践
- 定义与要求的常见问题与解决方案

定义与要求在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 独立影响对

独立影响对是白盒测试覆盖度的重要组成部分。本节详细介绍独立影响对的核心概念、工作原理和实际应用。

**关键要点**：

- 独立影响对的定义与核心原理
- 独立影响对的实现方式与技术细节
- 独立影响对在实际场景中的应用与最佳实践
- 独立影响对的常见问题与解决方案

独立影响对在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 航空软件标准 DO-178C

航空软件标准 DO-178C是白盒测试覆盖度的重要组成部分。本节详细介绍航空软件标准 DO-178C的核心概念、工作原理和实际应用。

**关键要点**：

- 航空软件标准 DO-178C的定义与核心原理
- 航空软件标准 DO-178C的实现方式与技术细节
- 航空软件标准 DO-178C在实际场景中的应用与最佳实践
- 航空软件标准 DO-178C的常见问题与解决方案

航空软件标准 DO-178C在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 覆盖度工具

### 4.1 JaCoCo

JaCoCo是白盒测试覆盖度的重要组成部分。本节详细介绍JaCoCo的核心概念、工作原理和实际应用。

**关键要点**：

- JaCoCo的定义与核心原理
- JaCoCo的实现方式与技术细节
- JaCoCo在实际场景中的应用与最佳实践
- JaCoCo的常见问题与解决方案

JaCoCo在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 Istanbul/NYC

Istanbul/NYC是白盒测试覆盖度的重要组成部分。本节详细介绍Istanbul/NYC的核心概念、工作原理和实际应用。

**关键要点**：

- Istanbul/NYC的定义与核心原理
- Istanbul/NYC的实现方式与技术细节
- Istanbul/NYC在实际场景中的应用与最佳实践
- Istanbul/NYC的常见问题与解决方案

Istanbul/NYC在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 gcov

gcov是白盒测试覆盖度的重要组成部分。本节详细介绍gcov的核心概念、工作原理和实际应用。

**关键要点**：

- gcov的定义与核心原理
- gcov的实现方式与技术细节
- gcov在实际场景中的应用与最佳实践
- gcov的常见问题与解决方案

gcov在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：036-software-testing/016-AutomationTestFrameworkComparison.md ============ -->



## 1. Selenium

### 1.1 WebDriver 协议

WebDriver 协议是自动化测试框架对比的重要组成部分。本节详细介绍WebDriver 协议的核心概念、工作原理和实际应用。

**关键要点**：

- WebDriver 协议的定义与核心原理
- WebDriver 协议的实现方式与技术细节
- WebDriver 协议在实际场景中的应用与最佳实践
- WebDriver 协议的常见问题与解决方案

WebDriver 协议在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 Grid 分布式

Grid 分布式是自动化测试框架对比的重要组成部分。本节详细介绍Grid 分布式的核心概念、工作原理和实际应用。

**关键要点**：

- Grid 分布式的定义与核心原理
- Grid 分布式的实现方式与技术细节
- Grid 分布式在实际场景中的应用与最佳实践
- Grid 分布式的常见问题与解决方案

Grid 分布式在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 优缺点

优缺点是自动化测试框架对比的重要组成部分。本节详细介绍优缺点的核心概念、工作原理和实际应用。

**关键要点**：

- 优缺点的定义与核心原理
- 优缺点的实现方式与技术细节
- 优缺点在实际场景中的应用与最佳实践
- 优缺点的常见问题与解决方案

优缺点在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. Cypress

### 2.1 架构特点

架构特点是自动化测试框架对比的重要组成部分。本节详细介绍架构特点的核心概念、工作原理和实际应用。

**关键要点**：

- 架构特点的定义与核心原理
- 架构特点的实现方式与技术细节
- 架构特点在实际场景中的应用与最佳实践
- 架构特点的常见问题与解决方案

架构特点在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 时间旅行

时间旅行是自动化测试框架对比的重要组成部分。本节详细介绍时间旅行的核心概念、工作原理和实际应用。

**关键要点**：

- 时间旅行的定义与核心原理
- 时间旅行的实现方式与技术细节
- 时间旅行在实际场景中的应用与最佳实践
- 时间旅行的常见问题与解决方案

时间旅行在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 优缺点

优缺点是自动化测试框架对比的重要组成部分。本节详细介绍优缺点的核心概念、工作原理和实际应用。

**关键要点**：

- 优缺点的定义与核心原理
- 优缺点的实现方式与技术细节
- 优缺点在实际场景中的应用与最佳实践
- 优缺点的常见问题与解决方案

优缺点在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. Playwright

### 3.1 多浏览器支持

多浏览器支持是自动化测试框架对比的重要组成部分。本节详细介绍多浏览器支持的核心概念、工作原理和实际应用。

**关键要点**：

- 多浏览器支持的定义与核心原理
- 多浏览器支持的实现方式与技术细节
- 多浏览器支持在实际场景中的应用与最佳实践
- 多浏览器支持的常见问题与解决方案

多浏览器支持在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 自动等待

自动等待是自动化测试框架对比的重要组成部分。本节详细介绍自动等待的核心概念、工作原理和实际应用。

**关键要点**：

- 自动等待的定义与核心原理
- 自动等待的实现方式与技术细节
- 自动等待在实际场景中的应用与最佳实践
- 自动等待的常见问题与解决方案

自动等待在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 优缺点

优缺点是自动化测试框架对比的重要组成部分。本节详细介绍优缺点的核心概念、工作原理和实际应用。

**关键要点**：

- 优缺点的定义与核心原理
- 优缺点的实现方式与技术细节
- 优缺点在实际场景中的应用与最佳实践
- 优缺点的常见问题与解决方案

优缺点在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 选型指南

### 4.1 功能对比

功能对比是自动化测试框架对比的重要组成部分。本节详细介绍功能对比的核心概念、工作原理和实际应用。

**关键要点**：

- 功能对比的定义与核心原理
- 功能对比的实现方式与技术细节
- 功能对比在实际场景中的应用与最佳实践
- 功能对比的常见问题与解决方案

功能对比在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 性能对比

性能对比是自动化测试框架对比的重要组成部分。本节详细介绍性能对比的核心概念、工作原理和实际应用。

**关键要点**：

- 性能对比的定义与核心原理
- 性能对比的实现方式与技术细节
- 性能对比在实际场景中的应用与最佳实践
- 性能对比的常见问题与解决方案

性能对比在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 场景推荐

场景推荐是自动化测试框架对比的重要组成部分。本节详细介绍场景推荐的核心概念、工作原理和实际应用。

**关键要点**：

- 场景推荐的定义与核心原理
- 场景推荐的实现方式与技术细节
- 场景推荐在实际场景中的应用与最佳实践
- 场景推荐的常见问题与解决方案

场景推荐在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：036-software-testing/017-APIAutomationTestDetailed.md ============ -->



## 1. Postman

### 1.1 集合与变量

集合与变量是API自动化测试详解的重要组成部分。本节详细介绍集合与变量的核心概念、工作原理和实际应用。

**关键要点**：

- 集合与变量的定义与核心原理
- 集合与变量的实现方式与技术细节
- 集合与变量在实际场景中的应用与最佳实践
- 集合与变量的常见问题与解决方案

集合与变量在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 Pre-request Script

Pre-request Script是API自动化测试详解的重要组成部分。本节详细介绍Pre-request Script的核心概念、工作原理和实际应用。

**关键要点**：

- Pre-request Script的定义与核心原理
- Pre-request Script的实现方式与技术细节
- Pre-request Script在实际场景中的应用与最佳实践
- Pre-request Script的常见问题与解决方案

Pre-request Script在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 Tests 断言

Tests 断言是API自动化测试详解的重要组成部分。本节详细介绍Tests 断言的核心概念、工作原理和实际应用。

**关键要点**：

- Tests 断言的定义与核心原理
- Tests 断言的实现方式与技术细节
- Tests 断言在实际场景中的应用与最佳实践
- Tests 断言的常见问题与解决方案

Tests 断言在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.4 Newman CLI

Newman CLI是API自动化测试详解的重要组成部分。本节详细介绍Newman CLI的核心概念、工作原理和实际应用。

**关键要点**：

- Newman CLI的定义与核心原理
- Newman CLI的实现方式与技术细节
- Newman CLI在实际场景中的应用与最佳实践
- Newman CLI的常见问题与解决方案

Newman CLI在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. RestAssured

### 2.1 Given-When-Then

Given-When-Then是API自动化测试详解的重要组成部分。本节详细介绍Given-When-Then的核心概念、工作原理和实际应用。

**关键要点**：

- Given-When-Then的定义与核心原理
- Given-When-Then的实现方式与技术细节
- Given-When-Then在实际场景中的应用与最佳实践
- Given-When-Then的常见问题与解决方案

Given-When-Then在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 JSON Path 断言

JSON Path 断言是API自动化测试详解的重要组成部分。本节详细介绍JSON Path 断言的核心概念、工作原理和实际应用。

**关键要点**：

- JSON Path 断言的定义与核心原理
- JSON Path 断言的实现方式与技术细节
- JSON Path 断言在实际场景中的应用与最佳实践
- JSON Path 断言的常见问题与解决方案

JSON Path 断言在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 数据驱动

数据驱动是API自动化测试详解的重要组成部分。本节详细介绍数据驱动的核心概念、工作原理和实际应用。

**关键要点**：

- 数据驱动的定义与核心原理
- 数据驱动的实现方式与技术细节
- 数据驱动在实际场景中的应用与最佳实践
- 数据驱动的常见问题与解决方案

数据驱动在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. Supertest

### 3.1 Node.js 集成测试

Node.js 集成测试是API自动化测试详解的重要组成部分。本节详细介绍Node.js 集成测试的核心概念、工作原理和实际应用。

**关键要点**：

- Node.js 集成测试的定义与核心原理
- Node.js 集成测试的实现方式与技术细节
- Node.js 集成测试在实际场景中的应用与最佳实践
- Node.js 集成测试的常见问题与解决方案

Node.js 集成测试在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 Express 应用测试

Express 应用测试是API自动化测试详解的重要组成部分。本节详细介绍Express 应用测试的核心概念、工作原理和实际应用。

**关键要点**：

- Express 应用测试的定义与核心原理
- Express 应用测试的实现方式与技术细节
- Express 应用测试在实际场景中的应用与最佳实践
- Express 应用测试的常见问题与解决方案

Express 应用测试在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 最佳实践

### 4.1 测试数据管理

测试数据管理是API自动化测试详解的重要组成部分。本节详细介绍测试数据管理的核心概念、工作原理和实际应用。

**关键要点**：

- 测试数据管理的定义与核心原理
- 测试数据管理的实现方式与技术细节
- 测试数据管理在实际场景中的应用与最佳实践
- 测试数据管理的常见问题与解决方案

测试数据管理在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 环境隔离

环境隔离是API自动化测试详解的重要组成部分。本节详细介绍环境隔离的核心概念、工作原理和实际应用。

**关键要点**：

- 环境隔离的定义与核心原理
- 环境隔离的实现方式与技术细节
- 环境隔离在实际场景中的应用与最佳实践
- 环境隔离的常见问题与解决方案

环境隔离在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 契约测试

契约测试是API自动化测试详解的重要组成部分。本节详细介绍契约测试的核心概念、工作原理和实际应用。

**关键要点**：

- 契约测试的定义与核心原理
- 契约测试的实现方式与技术细节
- 契约测试在实际场景中的应用与最佳实践
- 契约测试的常见问题与解决方案

契约测试在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：036-software-testing/018-StressAndStabilityTest.md ============ -->



## 1. 测试类型

### 1.1 负载测试

负载测试是压力测试与稳定性测试的重要组成部分。本节详细介绍负载测试的核心概念、工作原理和实际应用。

**关键要点**：

- 负载测试的定义与核心原理
- 负载测试的实现方式与技术细节
- 负载测试在实际场景中的应用与最佳实践
- 负载测试的常见问题与解决方案

负载测试在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 压力测试

压力测试是压力测试与稳定性测试的重要组成部分。本节详细介绍压力测试的核心概念、工作原理和实际应用。

**关键要点**：

- 压力测试的定义与核心原理
- 压力测试的实现方式与技术细节
- 压力测试在实际场景中的应用与最佳实践
- 压力测试的常见问题与解决方案

压力测试在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 稳定性测试

稳定性测试是压力测试与稳定性测试的重要组成部分。本节详细介绍稳定性测试的核心概念、工作原理和实际应用。

**关键要点**：

- 稳定性测试的定义与核心原理
- 稳定性测试的实现方式与技术细节
- 稳定性测试在实际场景中的应用与最佳实践
- 稳定性测试的常见问题与解决方案

稳定性测试在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.4 峰值测试

峰值测试是压力测试与稳定性测试的重要组成部分。本节详细介绍峰值测试的核心概念、工作原理和实际应用。

**关键要点**：

- 峰值测试的定义与核心原理
- 峰值测试的实现方式与技术细节
- 峰值测试在实际场景中的应用与最佳实践
- 峰值测试的常见问题与解决方案

峰值测试在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. JMeter

### 2.1 线程组与采样器

线程组与采样器是压力测试与稳定性测试的重要组成部分。本节详细介绍线程组与采样器的核心概念、工作原理和实际应用。

**关键要点**：

- 线程组与采样器的定义与核心原理
- 线程组与采样器的实现方式与技术细节
- 线程组与采样器在实际场景中的应用与最佳实践
- 线程组与采样器的常见问题与解决方案

线程组与采样器在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 断言与监听器

断言与监听器是压力测试与稳定性测试的重要组成部分。本节详细介绍断言与监听器的核心概念、工作原理和实际应用。

**关键要点**：

- 断言与监听器的定义与核心原理
- 断言与监听器的实现方式与技术细节
- 断言与监听器在实际场景中的应用与最佳实践
- 断言与监听器的常见问题与解决方案

断言与监听器在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 分布式压测

分布式压测是压力测试与稳定性测试的重要组成部分。本节详细介绍分布式压测的核心概念、工作原理和实际应用。

**关键要点**：

- 分布式压测的定义与核心原理
- 分布式压测的实现方式与技术细节
- 分布式压测在实际场景中的应用与最佳实践
- 分布式压测的常见问题与解决方案

分布式压测在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 指标分析

### 3.1 TPS/QPS

TPS/QPS是压力测试与稳定性测试的重要组成部分。本节详细介绍TPS/QPS的核心概念、工作原理和实际应用。

**关键要点**：

- TPS/QPS的定义与核心原理
- TPS/QPS的实现方式与技术细节
- TPS/QPS在实际场景中的应用与最佳实践
- TPS/QPS的常见问题与解决方案

TPS/QPS在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 响应时间分位

响应时间分位是压力测试与稳定性测试的重要组成部分。本节详细介绍响应时间分位的核心概念、工作原理和实际应用。

**关键要点**：

- 响应时间分位的定义与核心原理
- 响应时间分位的实现方式与技术细节
- 响应时间分位在实际场景中的应用与最佳实践
- 响应时间分位的常见问题与解决方案

响应时间分位在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 错误率

错误率是压力测试与稳定性测试的重要组成部分。本节详细介绍错误率的核心概念、工作原理和实际应用。

**关键要点**：

- 错误率的定义与核心原理
- 错误率的实现方式与技术细节
- 错误率在实际场景中的应用与最佳实践
- 错误率的常见问题与解决方案

错误率在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 稳定性测试

### 4.1 长时间运行

长时间运行是压力测试与稳定性测试的重要组成部分。本节详细介绍长时间运行的核心概念、工作原理和实际应用。

**关键要点**：

- 长时间运行的定义与核心原理
- 长时间运行的实现方式与技术细节
- 长时间运行在实际场景中的应用与最佳实践
- 长时间运行的常见问题与解决方案

长时间运行在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 内存泄漏检测

内存泄漏检测是压力测试与稳定性测试的重要组成部分。本节详细介绍内存泄漏检测的核心概念、工作原理和实际应用。

**关键要点**：

- 内存泄漏检测的定义与核心原理
- 内存泄漏检测的实现方式与技术细节
- 内存泄漏检测在实际场景中的应用与最佳实践
- 内存泄漏检测的常见问题与解决方案

内存泄漏检测在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 资源耗尽

资源耗尽是压力测试与稳定性测试的重要组成部分。本节详细介绍资源耗尽的核心概念、工作原理和实际应用。

**关键要点**：

- 资源耗尽的定义与核心原理
- 资源耗尽的实现方式与技术细节
- 资源耗尽在实际场景中的应用与最佳实践
- 资源耗尽的常见问题与解决方案

资源耗尽在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：036-software-testing/019-SecurityTesting.md ============ -->



## 1. OWASP ZAP

### 1.1 主动扫描

主动扫描是安全测试的重要组成部分。本节详细介绍主动扫描的核心概念、工作原理和实际应用。

**关键要点**：

- 主动扫描的定义与核心原理
- 主动扫描的实现方式与技术细节
- 主动扫描在实际场景中的应用与最佳实践
- 主动扫描的常见问题与解决方案

主动扫描在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 被动扫描

被动扫描是安全测试的重要组成部分。本节详细介绍被动扫描的核心概念、工作原理和实际应用。

**关键要点**：

- 被动扫描的定义与核心原理
- 被动扫描的实现方式与技术细节
- 被动扫描在实际场景中的应用与最佳实践
- 被动扫描的常见问题与解决方案

被动扫描在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 API 扫描

API 扫描是安全测试的重要组成部分。本节详细介绍API 扫描的核心概念、工作原理和实际应用。

**关键要点**：

- API 扫描的定义与核心原理
- API 扫描的实现方式与技术细节
- API 扫描在实际场景中的应用与最佳实践
- API 扫描的常见问题与解决方案

API 扫描在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. SQLMap

### 2.1 注入检测

注入检测是安全测试的重要组成部分。本节详细介绍注入检测的核心概念、工作原理和实际应用。

**关键要点**：

- 注入检测的定义与核心原理
- 注入检测的实现方式与技术细节
- 注入检测在实际场景中的应用与最佳实践
- 注入检测的常见问题与解决方案

注入检测在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 数据提取

数据提取是安全测试的重要组成部分。本节详细介绍数据提取的核心概念、工作原理和实际应用。

**关键要点**：

- 数据提取的定义与核心原理
- 数据提取的实现方式与技术细节
- 数据提取在实际场景中的应用与最佳实践
- 数据提取的常见问题与解决方案

数据提取在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 自动化利用

自动化利用是安全测试的重要组成部分。本节详细介绍自动化利用的核心概念、工作原理和实际应用。

**关键要点**：

- 自动化利用的定义与核心原理
- 自动化利用的实现方式与技术细节
- 自动化利用在实际场景中的应用与最佳实践
- 自动化利用的常见问题与解决方案

自动化利用在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. Nmap 安全扫描

### 3.1 漏洞扫描脚本

漏洞扫描脚本是安全测试的重要组成部分。本节详细介绍漏洞扫描脚本的核心概念、工作原理和实际应用。

**关键要点**：

- 漏洞扫描脚本的定义与核心原理
- 漏洞扫描脚本的实现方式与技术细节
- 漏洞扫描脚本在实际场景中的应用与最佳实践
- 漏洞扫描脚本的常见问题与解决方案

漏洞扫描脚本在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 服务识别

服务识别是安全测试的重要组成部分。本节详细介绍服务识别的核心概念、工作原理和实际应用。

**关键要点**：

- 服务识别的定义与核心原理
- 服务识别的实现方式与技术细节
- 服务识别在实际场景中的应用与最佳实践
- 服务识别的常见问题与解决方案

服务识别在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 安全测试流程

### 4.1 资产发现

资产发现是安全测试的重要组成部分。本节详细介绍资产发现的核心概念、工作原理和实际应用。

**关键要点**：

- 资产发现的定义与核心原理
- 资产发现的实现方式与技术细节
- 资产发现在实际场景中的应用与最佳实践
- 资产发现的常见问题与解决方案

资产发现在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 漏洞验证

漏洞验证是安全测试的重要组成部分。本节详细介绍漏洞验证的核心概念、工作原理和实际应用。

**关键要点**：

- 漏洞验证的定义与核心原理
- 漏洞验证的实现方式与技术细节
- 漏洞验证在实际场景中的应用与最佳实践
- 漏洞验证的常见问题与解决方案

漏洞验证在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 报告编写

报告编写是安全测试的重要组成部分。本节详细介绍报告编写的核心概念、工作原理和实际应用。

**关键要点**：

- 报告编写的定义与核心原理
- 报告编写的实现方式与技术细节
- 报告编写在实际场景中的应用与最佳实践
- 报告编写的常见问题与解决方案

报告编写在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：036-software-testing/020-TestDouble.md ============ -->



## 1. 测试双分类

### 1.1 Dummy

Dummy是测试双的重要组成部分。本节详细介绍Dummy的核心概念、工作原理和实际应用。

**关键要点**：

- Dummy的定义与核心原理
- Dummy的实现方式与技术细节
- Dummy在实际场景中的应用与最佳实践
- Dummy的常见问题与解决方案

Dummy在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 Stub

Stub是测试双的重要组成部分。本节详细介绍Stub的核心概念、工作原理和实际应用。

**关键要点**：

- Stub的定义与核心原理
- Stub的实现方式与技术细节
- Stub在实际场景中的应用与最佳实践
- Stub的常见问题与解决方案

Stub在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 Spy

Spy是测试双的重要组成部分。本节详细介绍Spy的核心概念、工作原理和实际应用。

**关键要点**：

- Spy的定义与核心原理
- Spy的实现方式与技术细节
- Spy在实际场景中的应用与最佳实践
- Spy的常见问题与解决方案

Spy在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.4 Mock

Mock是测试双的重要组成部分。本节详细介绍Mock的核心概念、工作原理和实际应用。

**关键要点**：

- Mock的定义与核心原理
- Mock的实现方式与技术细节
- Mock在实际场景中的应用与最佳实践
- Mock的常见问题与解决方案

Mock在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.5 Fake

Fake是测试双的重要组成部分。本节详细介绍Fake的核心概念、工作原理和实际应用。

**关键要点**：

- Fake的定义与核心原理
- Fake的实现方式与技术细节
- Fake在实际场景中的应用与最佳实践
- Fake的常见问题与解决方案

Fake在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. Mock 详解

### 2.1 行为验证 vs 状态验证

行为验证 vs 状态验证是测试双的重要组成部分。本节详细介绍行为验证 vs 状态验证的核心概念、工作原理和实际应用。

**关键要点**：

- 行为验证 vs 状态验证的定义与核心原理
- 行为验证 vs 状态验证的实现方式与技术细节
- 行为验证 vs 状态验证在实际场景中的应用与最佳实践
- 行为验证 vs 状态验证的常见问题与解决方案

行为验证 vs 状态验证在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 Mockito

Mockito是测试双的重要组成部分。本节详细介绍Mockito的核心概念、工作原理和实际应用。

**关键要点**：

- Mockito的定义与核心原理
- Mockito的实现方式与技术细节
- Mockito在实际场景中的应用与最佳实践
- Mockito的常见问题与解决方案

Mockito在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 Jest mock

Jest mock是测试双的重要组成部分。本节详细介绍Jest mock的核心概念、工作原理和实际应用。

**关键要点**：

- Jest mock的定义与核心原理
- Jest mock的实现方式与技术细节
- Jest mock在实际场景中的应用与最佳实践
- Jest mock的常见问题与解决方案

Jest mock在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. Stub 详解

### 3.1 预设返回值

预设返回值是测试双的重要组成部分。本节详细介绍预设返回值的核心概念、工作原理和实际应用。

**关键要点**：

- 预设返回值的定义与核心原理
- 预设返回值的实现方式与技术细节
- 预设返回值在实际场景中的应用与最佳实践
- 预设返回值的常见问题与解决方案

预设返回值在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 WireMock HTTP Stub

WireMock HTTP Stub是测试双的重要组成部分。本节详细介绍WireMock HTTP Stub的核心概念、工作原理和实际应用。

**关键要点**：

- WireMock HTTP Stub的定义与核心原理
- WireMock HTTP Stub的实现方式与技术细节
- WireMock HTTP Stub在实际场景中的应用与最佳实践
- WireMock HTTP Stub的常见问题与解决方案

WireMock HTTP Stub在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 最佳实践

### 4.1 何时使用哪种

何时使用哪种是测试双的重要组成部分。本节详细介绍何时使用哪种的核心概念、工作原理和实际应用。

**关键要点**：

- 何时使用哪种的定义与核心原理
- 何时使用哪种的实现方式与技术细节
- 何时使用哪种在实际场景中的应用与最佳实践
- 何时使用哪种的常见问题与解决方案

何时使用哪种在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 避免过度 Mock

避免过度 Mock是测试双的重要组成部分。本节详细介绍避免过度 Mock的核心概念、工作原理和实际应用。

**关键要点**：

- 避免过度 Mock的定义与核心原理
- 避免过度 Mock的实现方式与技术细节
- 避免过度 Mock在实际场景中的应用与最佳实践
- 避免过度 Mock的常见问题与解决方案

避免过度 Mock在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 契约测试

契约测试是测试双的重要组成部分。本节详细介绍契约测试的核心概念、工作原理和实际应用。

**关键要点**：

- 契约测试的定义与核心原理
- 契约测试的实现方式与技术细节
- 契约测试在实际场景中的应用与最佳实践
- 契约测试的常见问题与解决方案

契约测试在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：036-software-testing/021-TDDBDD.md ============ -->



## 1. TDD

### 1.1 红-绿-重构循环

红-绿-重构循环是TDD与BDD的重要组成部分。本节详细介绍红-绿-重构循环的核心概念、工作原理和实际应用。

**关键要点**：

- 红-绿-重构循环的定义与核心原理
- 红-绿-重构循环的实现方式与技术细节
- 红-绿-重构循环在实际场景中的应用与最佳实践
- 红-绿-重构循环的常见问题与解决方案

红-绿-重构循环在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 TDD 三定律

TDD 三定律是TDD与BDD的重要组成部分。本节详细介绍TDD 三定律的核心概念、工作原理和实际应用。

**关键要点**：

- TDD 三定律的定义与核心原理
- TDD 三定律的实现方式与技术细节
- TDD 三定律在实际场景中的应用与最佳实践
- TDD 三定律的常见问题与解决方案

TDD 三定律在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 实战示例

实战示例是TDD与BDD的重要组成部分。本节详细介绍实战示例的核心概念、工作原理和实际应用。

**关键要点**：

- 实战示例的定义与核心原理
- 实战示例的实现方式与技术细节
- 实战示例在实际场景中的应用与最佳实践
- 实战示例的常见问题与解决方案

实战示例在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. BDD

### 2.1 Given-When-Then

Given-When-Then是TDD与BDD的重要组成部分。本节详细介绍Given-When-Then的核心概念、工作原理和实际应用。

**关键要点**：

- Given-When-Then的定义与核心原理
- Given-When-Then的实现方式与技术细节
- Given-When-Then在实际场景中的应用与最佳实践
- Given-When-Then的常见问题与解决方案

Given-When-Then在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 Cucumber

Cucumber是TDD与BDD的重要组成部分。本节详细介绍Cucumber的核心概念、工作原理和实际应用。

**关键要点**：

- Cucumber的定义与核心原理
- Cucumber的实现方式与技术细节
- Cucumber在实际场景中的应用与最佳实践
- Cucumber的常见问题与解决方案

Cucumber在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 Gherkin 语法

Gherkin 语法是TDD与BDD的重要组成部分。本节详细介绍Gherkin 语法的核心概念、工作原理和实际应用。

**关键要点**：

- Gherkin 语法的定义与核心原理
- Gherkin 语法的实现方式与技术细节
- Gherkin 语法在实际场景中的应用与最佳实践
- Gherkin 语法的常见问题与解决方案

Gherkin 语法在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. TDD vs BDD

### 3.1 关注点差异

关注点差异是TDD与BDD的重要组成部分。本节详细介绍关注点差异的核心概念、工作原理和实际应用。

**关键要点**：

- 关注点差异的定义与核心原理
- 关注点差异的实现方式与技术细节
- 关注点差异在实际场景中的应用与最佳实践
- 关注点差异的常见问题与解决方案

关注点差异在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 适用场景

适用场景是TDD与BDD的重要组成部分。本节详细介绍适用场景的核心概念、工作原理和实际应用。

**关键要点**：

- 适用场景的定义与核心原理
- 适用场景的实现方式与技术细节
- 适用场景在实际场景中的应用与最佳实践
- 适用场景的常见问题与解决方案

适用场景在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 结合使用

结合使用是TDD与BDD的重要组成部分。本节详细介绍结合使用的核心概念、工作原理和实际应用。

**关键要点**：

- 结合使用的定义与核心原理
- 结合使用的实现方式与技术细节
- 结合使用在实际场景中的应用与最佳实践
- 结合使用的常见问题与解决方案

结合使用在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 实践建议

### 4.1 测试金字塔

测试金字塔是TDD与BDD的重要组成部分。本节详细介绍测试金字塔的核心概念、工作原理和实际应用。

**关键要点**：

- 测试金字塔的定义与核心原理
- 测试金字塔的实现方式与技术细节
- 测试金字塔在实际场景中的应用与最佳实践
- 测试金字塔的常见问题与解决方案

测试金字塔在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 测试覆盖率目标

测试覆盖率目标是TDD与BDD的重要组成部分。本节详细介绍测试覆盖率目标的核心概念、工作原理和实际应用。

**关键要点**：

- 测试覆盖率目标的定义与核心原理
- 测试覆盖率目标的实现方式与技术细节
- 测试覆盖率目标在实际场景中的应用与最佳实践
- 测试覆盖率目标的常见问题与解决方案

测试覆盖率目标在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 持续集成

持续集成是TDD与BDD的重要组成部分。本节详细介绍持续集成的核心概念、工作原理和实际应用。

**关键要点**：

- 持续集成的定义与核心原理
- 持续集成的实现方式与技术细节
- 持续集成在实际场景中的应用与最佳实践
- 持续集成的常见问题与解决方案

持续集成在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：036-software-testing/022-CICDTest.md ============ -->



## 1. 测试门禁概念

### 1.1 质量门定义

质量门定义是CI-CD测试门禁的重要组成部分。本节详细介绍质量门定义的核心概念、工作原理和实际应用。

**关键要点**：

- 质量门定义的定义与核心原理
- 质量门定义的实现方式与技术细节
- 质量门定义在实际场景中的应用与最佳实践
- 质量门定义的常见问题与解决方案

质量门定义在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 门禁策略

门禁策略是CI-CD测试门禁的重要组成部分。本节详细介绍门禁策略的核心概念、工作原理和实际应用。

**关键要点**：

- 门禁策略的定义与核心原理
- 门禁策略的实现方式与技术细节
- 门禁策略在实际场景中的应用与最佳实践
- 门禁策略的常见问题与解决方案

门禁策略在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. SonarQube

### 2.1 代码质量规则

代码质量规则是CI-CD测试门禁的重要组成部分。本节详细介绍代码质量规则的核心概念、工作原理和实际应用。

**关键要点**：

- 代码质量规则的定义与核心原理
- 代码质量规则的实现方式与技术细节
- 代码质量规则在实际场景中的应用与最佳实践
- 代码质量规则的常见问题与解决方案

代码质量规则在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 质量门配置

质量门配置是CI-CD测试门禁的重要组成部分。本节详细介绍质量门配置的核心概念、工作原理和实际应用。

**关键要点**：

- 质量门配置的定义与核心原理
- 质量门配置的实现方式与技术细节
- 质量门配置在实际场景中的应用与最佳实践
- 质量门配置的常见问题与解决方案

质量门配置在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 与 CI 集成

与 CI 集成是CI-CD测试门禁的重要组成部分。本节详细介绍与 CI 集成的核心概念、工作原理和实际应用。

**关键要点**：

- 与 CI 集成的定义与核心原理
- 与 CI 集成的实现方式与技术细节
- 与 CI 集成在实际场景中的应用与最佳实践
- 与 CI 集成的常见问题与解决方案

与 CI 集成在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 覆盖率门禁

### 3.1 JaCoCo 配置

JaCoCo 配置是CI-CD测试门禁的重要组成部分。本节详细介绍JaCoCo 配置的核心概念、工作原理和实际应用。

**关键要点**：

- JaCoCo 配置的定义与核心原理
- JaCoCo 配置的实现方式与技术细节
- JaCoCo 配置在实际场景中的应用与最佳实践
- JaCoCo 配置的常见问题与解决方案

JaCoCo 配置在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 覆盖率阈值

覆盖率阈值是CI-CD测试门禁的重要组成部分。本节详细介绍覆盖率阈值的核心概念、工作原理和实际应用。

**关键要点**：

- 覆盖率阈值的定义与核心原理
- 覆盖率阈值的实现方式与技术细节
- 覆盖率阈值在实际场景中的应用与最佳实践
- 覆盖率阈值的常见问题与解决方案

覆盖率阈值在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 增量覆盖率

增量覆盖率是CI-CD测试门禁的重要组成部分。本节详细介绍增量覆盖率的核心概念、工作原理和实际应用。

**关键要点**：

- 增量覆盖率的定义与核心原理
- 增量覆盖率的实现方式与技术细节
- 增量覆盖率在实际场景中的应用与最佳实践
- 增量覆盖率的常见问题与解决方案

增量覆盖率在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 流水线集成

### 4.1 Jenkins Pipeline

Jenkins Pipeline是CI-CD测试门禁的重要组成部分。本节详细介绍Jenkins Pipeline的核心概念、工作原理和实际应用。

**关键要点**：

- Jenkins Pipeline的定义与核心原理
- Jenkins Pipeline的实现方式与技术细节
- Jenkins Pipeline在实际场景中的应用与最佳实践
- Jenkins Pipeline的常见问题与解决方案

Jenkins Pipeline在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 GitHub Actions

GitHub Actions是CI-CD测试门禁的重要组成部分。本节详细介绍GitHub Actions的核心概念、工作原理和实际应用。

**关键要点**：

- GitHub Actions的定义与核心原理
- GitHub Actions的实现方式与技术细节
- GitHub Actions在实际场景中的应用与最佳实践
- GitHub Actions的常见问题与解决方案

GitHub Actions在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 GitLab CI

GitLab CI是CI-CD测试门禁的重要组成部分。本节详细介绍GitLab CI的核心概念、工作原理和实际应用。

**关键要点**：

- GitLab CI的定义与核心原理
- GitLab CI的实现方式与技术细节
- GitLab CI在实际场景中的应用与最佳实践
- GitLab CI的常见问题与解决方案

GitLab CI在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。



<!-- ============ 文档分隔线：036-software-testing/023-JestBasics.md ============ -->


## describe 测试分组

**基本写法：将相关测试用例分组**
`describe(<名称>, <回调函数>)`

```javascript
// 使用 describe 对测试用例分组
describe("Math 工具", () => {
  it("应正确执行加法", () => {
    expect(1 + 1).toBe(2);
  });
});
```

---

## it / test 测试用例

**基本写法：定义单个测试用例**
`test(<名称>, <回调函数>, [<超时>])`
`it(<名称>, <回调函数>, [<超时>])`

```javascript
// test 与 it 等价，it 是 test 的别名
test("两数相加", () => {
  expect(2 + 3).toBe(5);
});

it("字符串拼接", () => {
  expect("a" + "b").toBe("ab");
});
```

---

## expect 断言入口

**基本写法：断言值满足条件**
`expect(<实际值>).<匹配器>(<期望值>)`

```javascript
// expect 配合匹配器进行断言
expect(sum(2, 3)).toBe(5);
```

---

## toBe 精确相等

**基本写法：使用 Object.is 精确比较**
`expect(<值>).toBe(<期望值>)`

```javascript
// toBe 比较基本类型值
expect(2 + 2).toBe(4);
expect("hello").toBe("hello");
```

---

## toEqual 深度相等

**基本写法：递归比较对象所有属性**
`expect(<值>).toEqual(<期望对象>)`

```javascript
// toEqual 深度对比对象内容
const user = { name: "Alice", age: 30 };
expect(user).toEqual({ name: "Alice", age: 30 });
```

---

## toStrictEqual 严格深度相等

**基本写法：严格比较对象结构与类型**
`expect(<值>).toStrictEqual(<期望对象>)`

```javascript
// toStrictEqual 区分 undefined 与缺失属性
expect({ a: 1 }).not.toStrictEqual({ a: 1, b: undefined });
```

---

## 真值性匹配器

**基本写法：判断真假值**
`expect(<值>).toBeNull()`
`expect(<值>).toBeUndefined()`
`expect(<值>).toBeDefined()`
`expect(<值>).toBeTruthy()`
`expect(<值>).toBeFalsy()`

```javascript
// 真值性断言
expect(null).toBeNull();
expect(undefined).toBeUndefined();
expect(0).toBeFalsy();
expect("non-empty").toBeTruthy();
```

---

## 数字匹配器

**基本写法：数值大小比较**
`expect(<值>).toBeGreaterThan(<n>)`
`expect(<值>).toBeGreaterThanOrEqual(<n>)`
`expect(<值>).toBeLessThan(<n>)`
`expect(<值>).toBeLessThanOrEqual(<n>)`

```javascript
# 数字大小断言
expect(5).toBeGreaterThan(3);
expect(5).toBeGreaterThanOrEqual(5);
expect(2).toBeLessThan(3);
```

---

## toBeCloseTo 浮点近似

**基本写法：解决浮点精度问题**
`expect(<值>).toBeCloseTo(<期望值>, [<小数位数>])`

```javascript
// 浮点数近似比较，默认精度 2 位小数
expect(0.1 + 0.2).toBeCloseTo(0.3);
expect(0.1 + 0.2).toBeCloseTo(0.3, 5);
```

---

## 字符串匹配

**基本写法：正则或子串匹配**
`expect(<字符串>).toMatch(<正则|字符串>)`

```javascript
# 字符串正则匹配
expect("Christoph").toMatch(/stop/);
expect("team").not.toMatch(/I/);
```

---

## 数组包含

**基本写法：检查数组是否包含元素**
`expect(<数组>).toContain(<元素>)`
`expect(<数组>).toContainEqual(<对象>)`

```javascript
// toContain 检查基本类型，toContainEqual 检查对象
expect([1, 2, 3]).toContain(2);
expect([{ a: 1 }]).toContainEqual({ a: 1 });
```

---

## 异常断言

**基本写法：断言函数抛出异常**
`expect(() => <调用>).toThrow([<错误信息>])`
`expect(() => <调用>).toThrowError(<正则|字符串|Error>)`

```javascript
// 断言函数抛出指定异常
function risky() {
  throw new Error("参数无效");
}
expect(risky).toThrow("参数无效");
expect(risky).toThrow(Error);
```

---

## .not 修饰符

**基本写法：反向断言**
`expect(<值>).not.<匹配器>(<期望>)`

```javascript
# 使用 not 进行反向断言
expect(2 + 2).not.toBe(5);
expect([1, 2, 3]).not.toContain(4);
```

---

## 异步 resolves / rejects

**基本写法：断言 Promise 解析或拒绝**
`expect(<Promise>).resolves.<匹配器>(<期望>)`
`expect(<Promise>).rejects.<匹配器>(<期望>)`

```javascript
# 断言 Promise 的解析结果
expect(Promise.resolve(42)).resolves.toBe(42);
expect(Promise.reject(new Error("失败"))).rejects.toThrow("失败");
```

---

## toHaveBeenCalled 调用断言

**基本写法：断言 Mock 函数被调用**
`expect(<mock>).toHaveBeenCalled()`
`expect(<mock>).toHaveBeenCalledTimes(<次数>)`
`expect(<mock>).toHaveBeenCalledWith(<参数>)`

```javascript
// 断言 Mock 函数的调用情况
const fn = jest.fn();
fn("a", "b");
expect(fn).toHaveBeenCalled();
expect(fn).toHaveBeenCalledTimes(1);
expect(fn).toHaveBeenCalledWith("a", "b");
```

---

## toHaveProperty 属性断言

**基本写法：断言对象具有指定属性**
`expect(<对象>).toHaveProperty(<属性路径>, [<值>])`

```javascript
# 断言对象属性存在且匹配
const user = { profile: { name: "Alice" } };
expect(user).toHaveProperty("profile.name", "Alice");
```

---

## 非对称匹配器

**基本写法：使用非对称匹配器**
`expect.any(<构造函数>)`
`expect.anything()`
`expect.stringMatching(<正则>)`
`expect.objectContaining(<对象>)`
`expect.arrayContaining(<数组>)`

```javascript
// 非对称匹配器用于部分匹配
expect({ id: 1, name: "x" }).toEqual({
  id: expect.any(Number),
  name: expect.any(String),
});
expect([1, 2, 3]).toEqual(expect.arrayContaining([1, 2]));
```

---

## 测试跳过与独占

**基本写法：跳过或仅运行测试**
`test.skip(<名称>, <回调>)`
`test.only(<名称>, <回调>)`
`test.todo(<名称>)`

```javascript
# 跳过、独占与待办测试
test.skip("暂时跳过的用例", () => {});
test.only("仅运行此用例", () => {});
test.todo("待补充的用例");
```

---

## 参数化测试 test.each

**换行写法：数据驱动测试**
`test.each(<数据表>)(<名称模板>, <回调>)`

```javascript
# 使用 test.each 实现数据驱动测试
test.each([
  [1, 1, 2],
  [2, 3, 5],
  [-1, 1, 0],
])("%i + %i = %i", (a, b, expected) => {
  expect(a + b).toBe(expected);
});
```

---

## 生命周期钩子

**基本写法：测试前后置处理**
`beforeAll(<回调>, [<超时>])`
`beforeEach(<回调>, [<超时>])`
`afterEach(<回调>, [<超时>])`
`afterAll(<回调>, [<超时>])`

```javascript
# 生命周期钩子
beforeAll(() => { /* 所有测试前执行一次 */ });
beforeEach(() => { /* 每个测试前执行 */ });
afterEach(() => { /* 每个测试后执行 */ });
afterAll(() => { /* 所有测试后执行一次 */ });
```



<!-- ============ 文档分隔线：036-software-testing/024-JestMock.md ============ -->


## jest.fn 创建 Mock 函数

**基本写法：创建模拟函数**
`jest.fn([<实现>])`

```javascript
# 创建 Mock 函数
const mockFn = jest.fn();
mockFn("a");
expect(mockFn).toHaveBeenCalledWith("a");
```

---

## Mock 函数返回值

**基本写法：设置 Mock 返回值**
`<mock>.mockReturnValue(<值>)`
`<mock>.mockReturnValueOnce(<值>)`
`<mock>.mockResolvedValue(<Promise值>)`
`<mock>.mockRejectedValue(<错误>)`

```javascript
# 设置 Mock 函数返回值
const fn = jest.fn();
fn.mockReturnValue(42);
fn.mockReturnValueOnce(1).mockReturnValueOnce(2);
fn.mockResolvedValue("async value");
fn.mockRejectedValue(new Error("失败"));
```

---

## Mock 函数实现

**基本写法：自定义 Mock 实现**
`<mock>.mockImplementation(<函数>)`
`<mock>.mockImplementationOnce(<函数>)`

```javascript
# 自定义 Mock 实现
const fn = jest.fn();
fn.mockImplementation((x) => x * 2);
fn.mockImplementationOnce((x) => x + 1);
```

---

## jest.mock 模块模拟

**基本写法：自动 Mock 整个模块**
`jest.mock(<模块路径>)`

```javascript
# 自动 Mock 整个模块
jest.mock("./utils");
const { add } = require("./utils");
add.mockReturnValue(10);
```

---

## jest.mock 工厂函数

**换行写法：使用工厂函数自定义 Mock**
`jest.mock(<模块路径>, () => { <工厂实现> })`

```javascript
# 使用工厂函数自定义 Mock
jest.mock("./api", () => ({
  fetchData: jest.fn(() => Promise.resolve({ data: "mocked" })),
}));
```

---

## jest.requireActual 真实模块

**基本写法：获取真实模块**
`jest.requireActual(<模块路径>)`

```javascript
# 部分模拟时保留真实模块
jest.mock("./utils", () => ({
  ...jest.requireActual("./utils"),
  onlyMocked: jest.fn(),
}));
```

---

## jest.spyOn 监视方法

**基本写法：监听对象方法**
`jest.spyOn(<对象>, <方法名>)`

```javascript
# 监视对象方法调用
const obj = { method: (x) => x + 1 };
const spy = jest.spyOn(obj, "method");
obj.method(5);
expect(spy).toHaveBeenCalledWith(5);
```

---

## spyOn 模拟实现

**基本写法：监听并替换实现**
`jest.spyOn(<对象>, <方法>).mockImplementation(<函数>)`

```javascript
# 监听并替换方法实现
const spy = jest.spyOn(console, "log").mockImplementation(() => {});
console.log("不会输出");
expect(spy).toHaveBeenCalled();
```

---

## jest.mocked 类型安全 Mock

**基本写法：将导入转为 Mock 类型**
`jest.mocked(<导入函数>)`

```javascript
# 类型安全地访问 Mock 属性
import { fetchData } from "./api";
jest.mock("./api");
jest.mocked(fetchData).mockResolvedValue({ data: "ok" });
```

---

## Mock 调用记录

**基本写法：访问 Mock 调用信息**
`<mock>.mock.calls`
`<mock>.mock.results`
`<mock>.mock.instances`

```javascript
# 访问 Mock 调用记录
const fn = jest.fn();
fn("a", "b");
expect(fn.mock.calls[0]).toEqual(["a", "b"]);
expect(fn.mock.results[0].value).toBeUndefined();
```

---

## mockReset 重置 Mock

**基本写法：重置 Mock 状态**
`<mock>.mockReset()`
`<mock>.mockClear()`
`<mock>.mockRestore()`

```javascript
# 重置 Mock 不同级别
fn.mockClear();   # 清除调用记录
fn.mockReset();   # 清除记录并移除实现
fn.mockRestore(); # 恢复 spyOn 的原始实现
```

---

## jest.useFakeTimers 模拟定时器

**基本写法：使用假定时器**
`jest.useFakeTimers()`
`jest.useRealTimers()`
`jest.runAllTimers()`
`jest.advanceTimersByTime(<毫秒>)`

```javascript
# 模拟定时器执行
jest.useFakeTimers();
const fn = jest.fn();
setTimeout(fn, 1000);
jest.advanceTimersByTime(1000);
expect(fn).toHaveBeenCalled();
```

---

## jest.fn 链式调用

**换行写法：Mock 链式调用**
`jest.fn().mockReturnThis().mockReturnValue(<值>)`

```javascript
# Mock 链式 API 调用
const chainable = jest.fn().mockReturnThis();
chainable().method().value();
```

---

## mockImplementation async

**换行写法：Mock 异步函数**
`jest.fn().mockImplementation(async (<参数>) => { <异步逻辑> })`

```javascript
# Mock 异步函数实现
const asyncFn = jest.fn().mockImplementation(async (id) => {
  return { id, name: "mocked" };
});
await asyncFn(1);
```



<!-- ============ 文档分隔线：036-software-testing/025-JestAsync.md ============ -->


## async / await 测试

**换行写法：使用 async/await 测试异步**
`test(<名称>, async () => { await <异步调用>; expect(...); })`

```javascript
# 使用 async/await 测试异步函数
test("异步获取用户", async () => {
  const user = await fetchUser(1);
  expect(user).toHaveProperty("name");
});
```

---

## Promise return 测试

**基本写法：返回 Promise 进行断言**
`test(<名称>, () => { return <Promise>.then(<回调>); })`

```javascript
# 返回 Promise 让 Jest 等待
test("Promise 解析", () => {
  return fetchUser(1).then((user) => {
    expect(user.id).toBe(1);
  });
});
```

---

## resolves 匹配器

**基本写法：断言 Promise 成功解析**
`expect(<Promise>).resolves.<匹配器>(<期望>)`

```javascript
# 使用 resolves 断言 Promise 结果
test("resolves 断言", () => {
  return expect(Promise.resolve(42)).resolves.toBe(42);
});
```

---

## rejects 匹配器

**基本写法：断言 Promise 被拒绝**
`expect(<Promise>).rejects.<匹配器>(<期望>)`

```javascript
# 使用 rejects 断言 Promise 抛错
test("rejects 断言", () => {
  return expect(Promise.reject(new Error("失败"))).rejects.toThrow("失败");
});
```

---

## async resolves

**换行写法：async 配合 resolves**
`test(<名称>, async () => { await expect(<Promise>).resolves.<匹配器>(<期望>); })`

```javascript
# async/await 配合 resolves
test("async resolves", async () => {
  await expect(Promise.resolve("ok")).resolves.toBe("ok");
});
```

---

## async rejects

**换行写法：async 配合 rejects**
`test(<名称>, async () => { await expect(<Promise>).rejects.<匹配器>(<期望>); })`

```javascript
# async/await 配合 rejects
test("async rejects", async () => {
  await expect(Promise.reject(new Error("err"))).rejects.toThrow("err");
});
```

---

## 回调函数测试

**换行写法：测试回调函数**
`test(<名称>, (<done>) => { <异步操作>; <done>; })`

```javascript
# 使用 done 回调测试异步
test("回调完成", (done) => {
  fetchData((data) => {
    expect(data).toBe("result");
    done();
  });
});
```

---

## 测试超时设置

**基本写法：设置测试超时时间**
`test(<名称>, <回调>, <超时毫秒>)`
`jest.setTimeout(<毫秒>)`

```javascript
# 设置单个测试与全局超时
test("长时间操作", async () => {
  await longTask();
}, 10000);

jest.setTimeout(15000);
```

---

## fetch 模拟

**换行写法：Mock fetch 请求**
`global.fetch = jest.fn(() => Promise.resolve({ json: () => Promise.resolve(<数据>) }))`

```javascript
# Mock 全局 fetch
global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve({ id: 1, name: "Alice" }),
  })
);
```

---

## axios 模拟

**换行写法：Mock axios 模块**
`jest.mock('axios');`
`axios.get.mockResolvedValue({ data: <数据> });`

```javascript
# Mock axios 请求
import axios from "axios";
jest.mock("axios");
axios.get.mockResolvedValue({ data: { id: 1 } });
```

---

## 并发测试 test.concurrent

**换行写法：并发执行测试**
`test.concurrent(<名称>, <回调>, [<超时>])`

```javascript
# 并发执行多个测试用例
test.concurrent("并发测试1", async () => {
  expect(await fetchData()).toBeDefined();
});
```

---

## 异步错误捕获

**换行写法：断言异步函数抛错**
`await expect(<异步函数>()).rejects.toThrow(<错误>)`

```javascript
# 断言异步函数抛出指定错误
await expect(asyncFail()).rejects.toThrow("失败原因");
```



<!-- ============ 文档分隔线：036-software-testing/026-JestConfig.md ============ -->


## jest.config.js 配置

**换行写法：Jest 配置文件**
`module.exports = { <配置项> };`

```javascript
# Jest 配置文件示例
module.exports = {
  testEnvironment: "node",
  testMatch: ["**/*.test.js"],
  collectCoverageFrom: ["src/**/*.js"],
  coverageDirectory: "coverage",
  moduleNameMapper: { "^@/(.*)$": "<rootDir>/src/$1" },
};
```

---

## testEnvironment 环境

**基本写法：设置测试环境**
`testEnvironment: "<node|jsdom>"`

```javascript
# Node 环境与浏览器环境
testEnvironment: "node";    # Node.js 环境
testEnvironment: "jsdom";   # 浏览器 DOM 环境
```

---

## preset 预设

**基本写法：使用预设配置**
`preset: "<预设名>"`

```javascript
# 使用 ts-jest 或其他预设
preset: "ts-jest";
preset: "@testing-library/react";
```

---

## moduleNameMapper 路径映射

**基本写法：模块路径别名**
`moduleNameMapper: { "<别名正则>": "<真实路径>" }`

```javascript
# 路径别名映射
moduleNameMapper: {
  "^@/(.*)$": "<rootDir>/src/$1",
  "\\.(css|less)$": "identity-obj-proxy",
};
```

---

## 命令行选项

**基本写法：常用 Jest 命令**
`jest [<测试路径>] [--watch] [--coverage] [--verbose]`

```bash
# Jest 常用命令
jest                          # 运行所有测试
jest path/to/test             # 运行指定测试
jest --watch                  # 监视模式
jest --coverage               # 生成覆盖率报告
jest --verbose                # 显示详细输出
jest --bail                   # 失败时停止
```

---

## toMatchSnapshot 快照测试

**基本写法：生成并对比快照**
`expect(<值>).toMatchSnapshot([<属性匹配>, [<提示>]])`

```javascript
# 快照测试序列化对象
expect({ id: 1, name: "Alice" }).toMatchSnapshot();
```

---

## toMatchInlineSnapshot 内联快照

**基本写法：内联快照存储在测试文件中**
`expect(<值>).toMatchInlineSnapshot([<属性匹配>,] "<快照>")`

```javascript
# 内联快照首次运行自动写入
expect(config).toMatchInlineSnapshot();
```

---

## 更新快照

**基本写法：更新过时快照**
`jest --updateSnapshot`

```bash
# 更新所有快照
jest --updateSnapshot
jest -u   # 简写
```

---

## toThrowErrorMatchingSnapshot

**基本写法：异常快照**
`expect(() => <调用>).toThrowErrorMatchingSnapshot()`

```javascript
# 异常信息快照
expect(() => riskyCall()).toThrowErrorMatchingSnapshot();
```

---

## setup 文件

**基本写法：全局设置文件**
`setupFiles: ["<路径>"]`
`setupFilesAfterEnv: ["<路径>"]`

```javascript
# 配置全局 setup 文件
setupFiles: ["<rootDir>/jest.setup.js"];
setupFilesAfterEnv: ["@testing-library/jest-dom"];
```

---

## coverageThreshold 覆盖率阈值

**换行写法：设置覆盖率阈值**
`coverageThreshold: { global: { branches: <n>, functions: <n>, lines: <n>, statements: <n> } }`

```javascript
# 强制覆盖率达标
coverageThreshold: {
  global: {
    branches: 80,
    functions: 80,
    lines: 80,
    statements: 80,
  },
};
```

---

## transform 转换

**基本写法：配置代码转换**
`transform: { "<文件正则>": "<转换器>" }`

```javascript
# 使用 babel 或 ts-jest 转换
transform: {
  "^.+\\.tsx?$": "ts-jest",
  "^.+\\.jsx?$": "babel-jest",
};
```

---

## 全局配置 setup 与 teardown

**换行写法：全局 setup/teardown**
`globalSetup: "<模块路径>"`
`globalTeardown: "<模块路径>"`

```javascript
# 全局 setup 与 teardown 模块
module.exports = {
  globalSetup: "<rootDir>/setup.js",
  globalTeardown: "<rootDir>/teardown.js",
};
```



<!-- ============ 文档分隔线：036-software-testing/027-Mockito.md ============ -->


## mock 创建模拟对象

**基本写法：创建 Mock 对象**
`mock(<类>.class)`
`@Mock <类型> <字段>;`

```java
# 创建 Mock 对象
import static org.mockito.Mockito.*;

List<String> mockList = mock(List.class);
mockList.add("item");
verify(mockList).add("item");
```

---

## @Mock 注解

**换行写法：使用注解创建 Mock**
`@ExtendWith(MockitoExtension.class)`
`class <测试类> {`
`    @Mock <类型> <字段>;`
`}`

```java
# 使用 @Mock 注解
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;
import org.mockito.Mock;

@ExtendWith(MockitoExtension.class)
class ServiceTest {
    @Mock
    private Database db;
}
```

---

## when 打桩返回值

**换行写法：设置方法返回值**
`when(<mock>.<方法>(<参数>)).thenReturn(<值>)`
`when(<mock>.<方法>(<参数>)).thenThrow(<异常>)`

```java
# 设置 Mock 方法返回值或抛异常
when(mockList.size()).thenReturn(10);
when(mockList.get(0)).thenReturn("first");
when(mockList.get(1)).thenThrow(new RuntimeException("不存在"));
```

---

## thenReturn 多次返回

**换行写法：连续调用返回不同值**
`when(<mock>.<方法>()).thenReturn(<值1>, <值2>, <值3>)`

```java
# 同一方法多次调用返回不同值
when(mockIterator.next()).thenReturn("A", "B", "C");
```

---

## thenAnswer 自定义实现

**基本写法：自定义方法实现**
`when(<mock>.<方法>()).thenAnswer(<Answer>)`
`when(<mock>.<方法>()).then(invocation -> <实现>)`

```java
# 使用 lambda 自定义方法行为
when(mockList.get(anyInt())).thenAnswer(invocation -> {
    int index = invocation.getArgument(0);
    return "item-" + index;
});
```

---

## verify 调用验证

**基本写法：验证方法调用**
`verify(<mock>).<方法>(<参数>)`
`verify(<mock>, <times>).<方法>(<参数>)`

```java
# 验证 Mock 方法调用次数与参数
verify(mockList).add("item");
verify(mockList, times(2)).add(anyString());
verify(mockList, never()).clear();
verify(mockList, atLeast(1)).size();
```

---

## 参数匹配器

**基本写法：使用参数匹配器**
`any()` | `anyInt()` | `anyString()` | `eq(<值>)` | `argThat(<断言>)`

```java
# 使用匹配器匹配参数
when(mockList.get(anyInt())).thenReturn("ok");
when(mockMap.get(eq("key"))).thenReturn("value");

verify(mockList).add(argThat(s -> s.length() > 3));
```

---

## ArgumentCaptor 参数捕获

**换行写法：捕获参数进行断言**
`ArgumentCaptor<<类型>> captor = ArgumentCaptor.forClass(<类>.class);`
`verify(<mock>).<方法>(captor.capture());`
`captor.getValue()`

```java
# 捕获方法调用参数
import org.mockito.ArgumentCaptor;

ArgumentCaptor<String> captor = ArgumentCaptor.forClass(String.class);
verify(mockList).add(captor.capture());
assertEquals("item", captor.getValue());

# 多次调用的所有参数
List<String> all = captor.getAllValues();
```

---

## spy 间谍对象

**基本写法：创建间谍保留真实实现**
`spy(<对象>)`
`@Spy <类型> <字段> = new <类>();`

```java
# spy 保留真实方法实现，可部分打桩
List<String> realList = new ArrayList<>();
List<String> spyList = spy(realList);

spyList.add("real");
when(spyList.size()).thenReturn(100);
assertEquals(100, spyList.size());
```

---

## doReturn / doThrow

**基本写法：对 spy 使用 doReturn**
`doReturn(<值>).when(<spy>).<方法>()`
`doThrow(<异常>).when(<spy>).<方法>()`

```java
# 对 spy 对象应使用 doReturn 而非 when
List<String> spyList = spy(new ArrayList<>());
doReturn(100).when(spyList).size();
doThrow(new RuntimeException()).when(spyList).clear();
```

---

## verifyNoInteractions

**基本写法：验证无交互**
`verifyNoInteractions(<mock>)`
`verifyNoMoreInteractions(<mock>)`

```java
# 验证 Mock 没有发生交互
verifyNoInteractions(mockList);
verify(mockList).add("a");
verifyNoMoreInteractions(mockList);
```

---

## @InjectMocks 注入

**换行写法：自动注入 Mock 到被测对象**
`@InjectMocks`
`<类型> <字段>;`

```java
# 自动将 @Mock 字段注入到 @InjectMocks 对象
@ExtendWith(MockitoExtension.class)
class OrderServiceTest {
    @Mock
    private PaymentGateway gateway;
    @InjectMocks
    private OrderService service;

    @Test
    void testPay() {
        when(gateway.charge(any())).thenReturn(true);
        assertTrue(service.placeOrder());
    }
}
```

---

## timeout 超时验证

**基本写法：验证在超时内调用**
`verify(<mock>, timeout(<毫秒>)).<方法>()`

```java
# 验证方法在指定时间内被调用
verify(mockService, timeout(1000)).process(any());
verify(mockService, timeout(1000).times(2)).process(any());
```

---

## Mockito 静态方法模拟

**换行写法：模拟静态方法**
`try (MockedStatic<<类>> mocked = mockStatic(<类>.class)) {`
`    mocked.when(() -> <类>.<方法>()).thenReturn(<值>);`
`}`

```java
# 模拟静态方法（Mockito 3.4+）
try (MockedStatic<Utility> mocked = mockStatic(Utility.class)) {
    mocked.when(() -> Utility.now()).thenReturn(0L);
    assertEquals(0L, Service.getTime());
}
```



<!-- ============ 文档分隔线：036-software-testing/028-E2ETest.md ============ -->


## Cypress 基础

**基本写法：Cypress 测试结构**
`describe("<名称>", () => { cy.<命令>(); })`

```javascript
# Cypress 端到端测试
describe("登录流程", () => {
  it("应成功登录", () => {
    cy.visit("/login");
    cy.get("#username").type("admin");
    cy.get("#password").type("password");
    cy.get("button[type=submit]").click();
    cy.url().should("include", "/dashboard");
  });
});
```

---

## Cypress 元素操作

**基本写法：Cypress 元素定位与交互**
`cy.get("<选择器>").<操作>()`

```javascript
# Cypress 元素操作
cy.get("#input").type("hello");
cy.get("button").click();
cy.get(".item").first().click();
cy.get(".item").eq(2).click();
cy.get("select").select("选项");
```

---

## Cypress 断言

**基本写法：Cypress 链式断言**
`cy.get("<选择器>").should("<断言>", <值>)`

```javascript
# Cypress should 断言
cy.get("#title").should("have.text", "首页");
cy.get("#count").should("have.value", "10");
cy.get(".item").should("have.length", 5);
cy.get("#msg").should("be.visible");
cy.url().should("include", "/home");
```

---

## Cypress fixture 测试数据

**换行写法：使用 fixture 加载测试数据**
`cy.fixture("<文件>").then((<数据>) => { <操作> })`

```javascript
# 从 cypress/fixtures 加载 JSON 数据
cy.fixture("user").then((user) => {
  cy.get("#username").type(user.name);
  cy.get("#password").type(user.password);
});
```

---

## Cypress 自定义命令

**换行写法：定义自定义命令**
`Cypress.Commands.add("<命令名>", (<参数>) => { <操作> })`

```javascript
# 在 cypress/support/commands.js 定义
Cypress.Commands.add("login", (username, password) => {
  cy.session([username, password], () => {
    cy.visit("/login");
    cy.get("#username").type(username);
    cy.get("#password").type(password);
    cy.get("button").click();
  });
});

# 使用
cy.login("admin", "pass");
```

---

## Playwright 基础

**换行写法：Playwright 测试结构**
`test("<名称>", async ({ page }) => { await page.<操作>(); })`

```javascript
# Playwright 端到端测试
import { test, expect } from "@playwright/test";

test("首页加载", async ({ page }) => {
  await page.goto("https://example.com");
  await expect(page).toHaveTitle(/Example/);
});
```

---

## Playwright 定位器

**基本写法：Playwright 推荐定位器**
`page.locator("<选择器>")`
`page.getByRole("<角色>", { name: "<名称>" })`
`page.getByText("<文本>")`

```javascript
# Playwright 语义化定位器
await page.getByRole("button", { name: "提交" }).click();
await page.getByLabel("用户名").fill("admin");
await page.getByPlaceholder("请输入").fill("hello");
await page.getByText("欢迎").click();
await page.locator(".item").first().click();
```

---

## Playwright 交互

**基本写法：页面交互方法**
`await page.<方法>(<参数>)`

```javascript
# Playwright 常用交互
await page.goto("https://example.com");
await page.fill("#input", "text");
await page.click("button");
await page.selectOption("select", "value");
await page.check("#checkbox");
await page.press("#input", "Enter");
```

---

## Playwright 自动等待

**基本写法：Playwright 自动等待机制**
`await expect(<locator>).<条件>()`

```javascript
# Playwright 自动重试断言
await expect(page.locator("#msg")).toBeVisible();
await expect(page.locator("#count")).toHaveText("10");
await expect(page).toHaveURL(/dashboard/);
await page.waitForLoadState("networkidle");
```

---

## Playwright 多浏览器

**换行写法：配置多浏览器测试**
`projects: [`
`    { name: "chromium", use: { ...devices["Desktop Chrome"] } },`
`]`

```javascript
# playwright.config.js 配置多浏览器
module.exports = {
  projects: [
    { name: "chromium", use: { ...devices["Desktop Chrome"] } },
    { name: "firefox", use: { ...devices["Desktop Firefox"] } },
    { name: "webkit", use: { ...devices["Desktop Safari"] } },
  ],
};
```

---

## Playwright 截图与录像

**基本写法：截图与录屏**
`await page.screenshot({ path: "<文件>" })`
`recordVideo: { dir: "<目录>" }`

```javascript
# 截图与录像配置
await page.screenshot({ path: "screenshot.png", fullPage: true });

# playwright.config.js 录像配置
use: {
  video: "on-first-retry",
  screenshot: "only-on-failure",
}
```

---

## Playwright fixture

**换行写法：自定义 fixture**
`test("<名称>", async ({ page, <自定义fixture> }) => { <操作> })`

```javascript
# 自定义 fixture 扩展测试能力
import { test as base } from "@playwright/test";

const test = base.extend({
  loggedInPage: async ({ page }, use) => {
    await page.goto("/login");
    await page.fill("#user", "admin");
    await use(page);
  },
});

test("登录后访问", async ({ loggedInPage }) => {
  await loggedInPage.goto("/dashboard");
});
```

---

## Playwright API 测试

**换行写法：API 接口测试**
`test("<名称>", async ({ request }) => { const res = await request.<方法>(<url>); })`

```javascript
# Playwright API 测试
import { test, expect } from "@playwright/test";

test("创建用户 API", async ({ request }) => {
  const response = await request.post("/api/users", {
    data: { name: "Alice", age: 30 },
  });
  expect(response.status()).toBe(201);
  const body = await response.json();
  expect(body.name).toBe("Alice");
});
```

---

## Playwright 命令

**基本写法：Playwright CLI 命令**
`npx playwright test [<选项>]`

```bash
# Playwright 常用命令
npx playwright test                    # 运行所有测试
npx playwright test tests/login.spec.ts # 运行指定文件
npx playwright test --project=chromium  # 指定浏览器
npx playwright test --headed            # 显示浏览器窗口
npx playwright test --ui                 # UI 模式
npx playwright codegen https://example.com  # 录制测试
```



<!-- ============ 文档分隔线：036-software-testing/029-AssertionLibrary.md ============ -->


## Chai BDD 风格

**基本写法：expect 风格断言**
`expect(<值>).to.<断言>(<期望>)`

```javascript
# Chai expect 风格断言
import { expect } from "chai";

expect(5).to.equal(5);
expect("hello").to.be.a("string");
expect([1, 2, 3]).to.include(2);
expect({ a: 1 }).to.deep.equal({ a: 1 });
```

---

## Chai should 风格

**基本写法：should 风格断言**
`<值>.should.<断言>(<期望>)`

```javascript
# Chai should 风格断言
import "chai/register-should";

(5).should.equal(5);
"hello".should.be.a("string");
[1, 2, 3].should.include(2);
```

---

## Chai assert 风格

**基本写法：TDD 风格断言**
`assert.<方法>(<实际>, <期望>[, <消息>])`

```javascript
# Chai assert 风格断言
import { assert } from "chai";

assert.equal(5, 5);
assert.typeOf("hello", "string");
assert.include([1, 2, 3], 2);
assert.deepEqual({ a: 1 }, { a: 1 });
```

---

## Chai 链式断言

**基本写法：链式修饰符**
`expect(<值>).to.<修饰符>.<断言>(<期望>)`

```javascript
# Chai 链式修饰符增强可读性
expect(5).to.not.equal(6);
expect(null).to.not.exist;
expect([]).to.be.empty;
expect(10).to.be.at.most(10);
expect("hello").to.have.lengthOf(5);
```

---

## Chai 数字断言

**基本写法：数值比较**
`expect(<值>).to.be.<比较>(<n>)`

```javascript
# Chai 数字比较断言
expect(5).to.be.above(3);
expect(5).to.be.at.least(5);
expect(5).to.be.below(10);
expect(5).to.be.at.most(5);
expect(5).to.be.within(1, 10);
```

---

## Chai 字符串断言

**基本写法：字符串匹配**
`expect(<字符串>).to.<包含|匹配>(<值>)`

```javascript
# Chai 字符串断言
expect("hello world").to.include("world");
expect("hello").to.startWith("he");
expect("world").to.endWith("ld");
expect("hello").to.match(/^he/);
expect("hello").to.have.lengthOf(5);
```

---

## Chai 对象断言

**基本写法：对象属性断言**
`expect(<对象>).to.have.<属性>(<值>)`

```javascript
# Chai 对象属性断言
expect({ a: 1, b: 2 }).to.have.property("a");
expect({ a: 1 }).to.have.property("a", 1);
expect({ a: 1, b: 2 }).to.have.all.keys("a", "b");
expect({ a: 1 }).to.include({ a: 1 });
```

---

## Chai 数组断言

**基本写法：数组断言**
`expect(<数组>).to.<包含|长度>(<值>)`

```javascript
# Chai 数组断言
expect([1, 2, 3]).to.include(2);
expect([1, 2, 3]).to.have.lengthOf(3);
expect([1, 2, 3]).to.have.ordered.members([1, 2, 3]);
expect([1, 2, 3]).to.deep.equal([1, 2, 3]);
```

---

## Chai 异常断言

**基本写法：断言抛出异常**
`expect(() => <调用>).to.throw([<错误类型>][, <消息>])`

```javascript
# Chai 异常断言
expect(() => { throw new Error("失败"); }).to.throw("失败");
expect(() => { throw new TypeError(); }).to.throw(TypeError);
expect(() => { throw new Error(); }).to.throw(/失败/);
```

---

## Hamcrest Java 断言

**基本写法：Hamcrest 匹配器断言**
`assertThat(<实际>, <matcher>)`

```java
# Hamcrest 断言库
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

assertThat(5, is(5));
assertThat("hello", containsString("ell"));
assertThat(5, greaterThan(3));
assertThat("hello", notNullValue());
```

---

## Hamcrest 集合匹配器

**基本写法：集合相关匹配器**
`assertThat(<集合>, hasItem(<元素>))`
`assertThat(<集合>, contains(<元素>))`

```java
# Hamcrest 集合匹配器
assertThat(List.of(1, 2, 3), hasItem(2));
assertThat(List.of(1, 2, 3), contains(1, 2, 3));
assert assertThat(List.of(1, 2, 3), hasSize(3));
assertThat(List.of(1, 2, 3), everyItem(lessThan(10)));
```

---

## Hamcrest 字符串匹配器

**基本写法：字符串匹配器**
`assertThat(<字符串>, <匹配器>)`

```java
# Hamcrest 字符串匹配器
assertThat("hello world", containsString("world"));
assertThat("hello", startsWith("he"));
assertThat("world", endsWith("ld"));
assertThat("hello", equalTo("hello"));
assertThat("  hello  ", is(equalToIgnoringWhiteSpace("hello")));
```

---

## AssertJ 流式断言

**基本写法：AssertJ 流式 API**
`assertThat(<值>).<断言>().<断言>()`

```java
# AssertJ 流式断言库
import static org.assertj.core.api.Assertions.*;

assertThat("hello")
    .isNotNull()
    .startsWith("he")
    .hasSize(5)
    .contains("ell");

assertThat(5).isPositive().isGreaterThan(3);
assertThat(List.of(1, 2, 3)).hasSize(3).contains(2);
```

---

## AssertJ 异常断言

**换行写法：AssertJ 异常断言**
`assertThatThrownBy(() -> <调用>).isInstanceOf(<异常类>).hasMessage("<消息>")`

```java
# AssertJ 异常断言
assertThatThrownBy(() -> { throw new IllegalArgumentException("无效"); })
    .isInstanceOf(IllegalArgumentException.class)
    .hasMessageContaining("无效");
```
