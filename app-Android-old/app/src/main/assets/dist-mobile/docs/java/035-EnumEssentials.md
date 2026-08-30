## 一句话定调

**enum 是"有身份证的常量"**：每个枚举值不仅是一个名字，还可以携带字段、构造函数和行为。别再用 `public static final int` 拼状态码了。

## 极简代码（看懂这 20 行就够了）

```java
// 订单状态：每个状态带一个中文描述字段
public enum OrderStatus {
    CREATED("已创建"),
    PAID("已支付"),
    SHIPPED("已发货"),
    DONE("已完成");

    private final String label;

    // 枚举构造函数：编译时按上面括号里的参数调用
    OrderStatus(String label) {
        this.label = label;
    }

    public String label() {
        return label;
    }
}

// 配合 switch 使用（Java 14+ 表达式写法）
String tip = switch (OrderStatus.PAID) {
    case CREATED -> "等待支付";
    case PAID -> "等待发货";
    case SHIPPED -> "运输中";
    case DONE -> "交易完成";
};
```

两个必记 API：`OrderStatus.values()` 返回全部枚举值数组；`OrderStatus.valueOf("PAID")` 按名字查找（名字写错抛 `IllegalArgumentException`）。

## 如果报这个错，看这里

**报错：`Expected BEGIN_OBJECT but was STRING`（Gson/Jackson 反序列化枚举失败）**

原因：JSON 里存的是字符串 `"PAID"`，而 Gson 默认按对象结构反序列化，或枚举名字与 JSON 值不一致。

对策：一是让 JSON 直接使用枚举名（`PAID`），二是给枚举加 `@JsonValue` 指定序列化字段；零基础阶段最稳妥的做法是把状态存成字符串，在业务代码里用 `OrderStatus.valueOf(str)` 转换并捕获 `IllegalArgumentException`。

**报错：`valueOf` 抛 `IllegalArgumentException: No enum constant`**

原因：传入的字符串与枚举名不完全一致（大小写、空格）。

对策：先 `trim()`，必要时写一个 `fromCode` 静态方法做容错映射。

## 记住

> 枚举 = 固定集合的常量 + 可携带数据；`==` 可以直接比较枚举值，不用 `equals()`。
