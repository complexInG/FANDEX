# 测试覆盖率工具

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

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
