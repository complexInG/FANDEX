# Java 序列化

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Serializable 接口

**基本写法：实现可序列化**
`class <类名> implements Serializable {}`
```java
// 标记类为可序列化
public class User implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
}
```

---

**基本写法：定义 serialVersionUID**
`private static final long serialVersionUID = <值>L;`
```java
// 显式声明版本号保证兼容
private static final long serialVersionUID = 42L;
```

---

## 对象流序列化

**基本写法：写入对象**
`new ObjectOutputStream(<输出流>).writeObject(<对象>);`
```java
// 序列化对象到文件
try (ObjectOutputStream oos = new ObjectOutputStream(
        new FileOutputStream("user.dat"))) {
    oos.writeObject(user);
}
```

---

**基本写法：读取对象**
`new ObjectInputStream(<输入流>).readObject();`
```java
// 从文件反序列化对象
try (ObjectInputStream ois = new ObjectInputStream(
        new FileInputStream("user.dat"))) {
    User u = (User) ois.readObject();
}
```

---

## 关键字 transient

**基本写法：排除字段**
`transient <类型> <字段名>;`
```java
// 标记字段不参与序列化
private transient String password;
```

---

## 自定义序列化

**基本写法：重写 writeObject**
`private void writeObject(ObjectOutputStream out) throws IOException {}`
```java
// 自定义写入逻辑
private void writeObject(ObjectOutputStream out) throws IOException {
    out.defaultWriteObject();
    out.writeUTF(encrypt(password));
}
```

---

**基本写法：重写 readObject**
`private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {}`
```java
// 自定义读取逻辑
private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
    in.defaultReadObject();
    this.password = decrypt(in.readUTF());
}
```

---

**基本写法：writeReplace 替换对象**
`private Object writeReplace() { return <新对象>; }`
```java
// 序列化时替换为另一个对象
private Object writeReplace() {
    return new UserProxy(name);
}
```

---

**基本写法：readResolve 单例恢复**
`private Object readResolve() { return <实例>; }`
```java
// 反序列化时返回单例实例
private Object readResolve() {
    return INSTANCE;
}
```

---

## Externalizable 接口

**基本写法：实现 Externalizable**
`class <类名> implements Externalizable { public void writeExternal(ObjectOutput o) {} public void readExternal(ObjectInput i) {} }`
```java
// 完全自定义序列化
public class User implements Externalizable {
    public void writeExternal(ObjectOutput out) throws IOException {
        out.writeUTF(name);
    }
    public void readExternal(ObjectInput in) throws IOException {
        this.name = in.readUTF();
    }
}
```

---

## 序列化过滤（Java 9+）

**基本写法：设置输入过滤器**
`ObjectInputFilter.Config.createFilter("<规则>")`
```java
// 反序列化白名单过滤
ObjectInputFilter filter = ObjectInputFilter.Config.createFilter(
    "com.example.*;java.lang.*;!*");
ois.setObjectInputFilter(filter);
```

---

**基本写法：全局过滤器**
`ObjectInputFilter.Config.setSerialFilter(<过滤器>);`
```java
// 设置全局反序列化过滤器
ObjectInputFilter.Config.setSerialFilter(info -> {
    if (info.serialClass() == User.class) return ObjectInputFilter.Status.ALLOWED;
    return ObjectInputFilter.Status.REJECTED;
});
```

---

## JSON 序列化（Jackson）

**基本写法：Jackson 写 JSON**
`new ObjectMapper().writeValueAsString(<对象>);`
```java
// 将对象序列化为 JSON 字符串
String json = new ObjectMapper().writeValueAsString(user);
```

---

**基本写法：Jackson 读 JSON**
`new ObjectMapper().readValue(<json>, <类>.class);`
```java
// 将 JSON 字符串反序列化为对象
User u = new ObjectMapper().readValue(json, User.class);
```

---

**基本写法：Jackson 写文件**
`new ObjectMapper().writeValue(<文件>, <对象>);`
```java
// 将对象序列化到 JSON 文件
new ObjectMapper().writeValue(new File("user.json"), user);
```

---

**基本写法：忽略字段**
`@JsonIgnore`
```java
// 标记字段不参与 JSON 序列化
@JsonIgnore
private String password;
```

---

**基本写法：指定字段名**
`@JsonProperty("<名称>")`
```java
// 自定义 JSON 字段名
@JsonProperty("user_name")
private String userName;
```

---

## JSON 序列化（Gson）

**基本写法：Gson 写 JSON**
`new Gson().toJson(<对象>);`
```java
// 使用 Gson 序列化为 JSON
String json = new Gson().toJson(user);
```

---

**基本写法：Gson 读 JSON**
`new Gson().fromJson(<json>, <类>.class);`
```java
// 使用 Gson 反序列化
User u = new Gson().fromJson(json, User.class);
```

---

## ProtoBuf 二进制序列化

**基本写法：ProtoBuf 写入**
`<消息类>.writeTo(<输出流>);`
```java
// ProtoBuf 消息写入字节流
UserProto.User u = UserProto.User.newBuilder().setName("Alice").build();
u.writeTo(new FileOutputStream("u.bin"));
```

---

**基本写法：ProtoBuf 读取**
`<消息类>.parseFrom(<输入流>);`
```java
// 从字节流解析 ProtoBuf 消息
UserProto.User u = UserProto.User.parseFrom(new FileInputStream("u.bin"));
```
