# Java 反射与动态代理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 获取 Class 对象

**基本写法：三种获取 Class 的方式**
`<类名>.class | <对象>.getClass() | Class.forName("<全限定名>")`
```java
// 三种方式获取 Class 对象
Class<String> c1 = String.class;
Class<?> c2 = "hello".getClass();
Class<?> c3 = Class.forName("java.lang.String");
```

---

## 反射创建实例

**基本写法：通过 Class 创建对象**
`<class>.getDeclaredConstructor().newInstance();`
```java
// 反射方式创建实例
Object obj = String.class.getDeclaredConstructor().newInstance();
```

---

**基本写法：带参构造**
`<class>.getDeclaredConstructor(<参数类型>...).newInstance(<参数>...);`
```java
// 通过带参构造创建实例
Object obj = String.class.getDeclaredConstructor(byte[].class).newInstance(new byte[]{65});
```

---

## 反射获取字段

**基本写法：获取声明字段**
`<class>.getDeclaredField("<字段名>");`
```java
// 获取私有字段
Field f = Person.class.getDeclaredField("name");
f.setAccessible(true);
```

---

**基本写法：读取字段值**
`<field>.get(<对象>);`
```java
// 读取对象字段值
Object value = f.get(person);
```

---

**基本写法：设置字段值**
`<field>.set(<对象>, <值>);`
```java
// 设置对象字段值
f.set(person, "Alice");
```

---

## 反射获取方法

**基本写法：获取声明方法**
`<class>.getDeclaredMethod("<方法名>", <参数类型>...);`
```java
// 获取私有方法
Method m = Person.class.getDeclaredMethod("greet", String.class);
m.setAccessible(true);
```

---

**基本写法：反射调用方法**
`<method>.invoke(<对象>, <参数>...);`
```java
// 反射调用方法
Object result = m.invoke(person, "World");
```

---

## 反射操作泛型

**基本写法：获取泛型返回类型**
`<method>.getGenericReturnType();`
```java
// 获取方法的泛型返回类型
Type type = method.getGenericReturnType();
```

---

**基本写法：获取参数泛型**
`<method>.getGenericParameterTypes();`
```java
// 获取方法参数的泛型类型数组
Type[] types = method.getGenericParameterTypes();
```

---

## JDK 动态代理

**基本写法：创建 JDK 动态代理**
`Proxy.newProxyInstance(<类加载器>, <接口数组>, <调用处理器>);`
```java
// 为 List 接口创建代理
List<String> proxy = (List<String>) Proxy.newProxyInstance(
    List.class.getClassLoader(),
    new Class[]{List.class},
    (proxyObj, method, args) -> {
        System.out.println("调用: " + method.getName());
        return null;
    }
);
```

---

**基本写法：实现 InvocationHandler**
`class <类名> implements InvocationHandler { public Object invoke(Object p, Method m, Object[] a) {} }`
```java
// 自定义调用处理器
class LogHandler implements InvocationHandler {
    private final Object target;
    public LogHandler(Object target) { this.target = target; }
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        System.out.println("before: " + method.getName());
        Object r = method.invoke(target, args);
        System.out.println("after: " + method.getName());
        return r;
    }
}
```

---

## CGLIB 风格代理（子类代理）

**基本写法：创建子类代理（需第三方库 cglib）**
`Enhancer.create(<类>, <回调>);`
```java
// cglib 创建子类代理
Enhancer enhancer = new Enhancer();
enhancer.setSuperclass(Person.class);
enhancer.setCallback((MethodInterceptor) (obj, method, args, proxy) -> {
    System.out.println("before");
    Object r = proxy.invokeSuper(obj, args);
    System.out.println("after");
    return r;
});
Person proxy = (Person) enhancer.create();
```

---

## 反射获取注解

**基本写法：获取类上注解**
`<class>.getAnnotation(<注解类型>);`
```java
// 获取类上的注解
Deprecated d = MyClass.class.getAnnotation(Deprecated.class);
```

---

**基本写法：判断注解存在**
`<class>.isAnnotationPresent(<注解类型>);`
```java
// 判断注解是否存在
boolean has = MyClass.class.isAnnotationPresent(Deprecated.class);
```

---

## 反射获取数组信息

**基本写法：创建数组实例**
`Array.newInstance(<元素类型>, <长度>);`
```java
// 反射创建数组
Object arr = Array.newInstance(int.class, 5);
```

---

**基本写法：反射读写数组**
`Array.get(<数组>, <索引>); | Array.set(<数组>, <索引>, <值>);`
```java
// 反射方式读写数组元素
Array.set(arr, 0, 42);
int v = (int) Array.get(arr, 0);
```

---

## Module 反射（Java 9+）

**基本写法：获取模块**
`<class>.getModule();`
```java
// 获取类所属模块
Module module = String.class.getModule();
System.out.println(module.getName());
```

---

**基本写法：导出包到指定模块**
`<module>.addExports("<包名>", <目标模块>);`
```java
// 反射方式导出包
module.addExports("com.example.internal", OtherModule);
```

---

## Record 反射（Java 16+）

**基本写法：判断是否为 Record**
`<class>.isRecord();`
```java
// 判断 Class 是否为 Record
boolean isRec = Point.class.isRecord();
```

---

**基本写法：获取 Record 组件**
`<class>.getRecordComponents();`
```java
// 获取 Record 的组件
RecordComponent[] comps = Point.class.getRecordComponents();
```
