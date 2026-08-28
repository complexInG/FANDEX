# TypeScript 装饰器

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 装饰器基础

**基本写法：类装饰器**
`function <装饰器>(<target>: <构造器>) { }`
```typescript
// 类装饰器接收构造器返回新构造器
function Log<T extends new (...args: any[]) => any>(target: T): T {
    return class extends target { }
}
@Log class Foo {}
```

---

**基本写法：方法装饰器**
`function <装饰器>(<target>, <key>, <descriptor>) { }`
```typescript
// 方法装饰器接收原型 方法名 描述符
function Log(target: any, key: string, desc: PropertyDescriptor) {
    const orig = desc.value
    desc.value = function (...args: any[]) {
        console.log(`call ${key}`)
        return orig.apply(this, args)
    }
}
```

---

**基本写法：属性装饰器**
`function <装饰器>(<target>, <key>) { }`
```typescript
// 属性装饰器接收原型 与 属性名
function Meta(target: any, key: string) {
    Object.defineProperty(target, key, { value: null })
}
```

---

**基本写法：参数装饰器**
`function <装饰器>(<target>, <key>, <index>) { }`
```typescript
// 参数装饰器接收原型 方法名 参数索引
function Required(target: any, key: string, index: number) {
    console.log(`param ${index} of ${key}`)
}
```

---

## 方法装饰器实战

**基本写法：日志装饰器**
`function <Log>(<target>, <key>, <descriptor>)`
```typescript
// 记录方法调用
function Log(target: any, key: string, desc: PropertyDescriptor) {
    const orig = desc.value
    desc.value = function (...args: any[]) {
        console.log(`${key} called with`, args)
        return orig.apply(this, args)
    }
}
class Service { @Log greet(name: string) { return `hi ${name}` } }
```

---

**基本写法：性能测量装饰器**
`function <Measure>(<target>, <key>, <descriptor>)`
```typescript
// 测量方法执行时间
function Measure(target: any, key: string, desc: PropertyDescriptor) {
    const orig = desc.value
    desc.value = function (...args: any[]) {
        const start = performance.now()
        const result = orig.apply(this, args)
        console.log(`${key} took ${performance.now() - start}ms`)
        return result
    }
}
```

---

**基本写法：错误捕获装饰器**
`function <Catch>(<target>, <key>, <descriptor>)`
```typescript
// 统一捕获方法异常
function Catch(target: any, key: string, desc: PropertyDescriptor) {
    const orig = desc.value
    desc.value = async function (...args: any[]) {
        try { return await orig.apply(this, args) }
        catch (e) { console.error(`${key} error`, e) }
    }
}
```

---

## 类装饰器实战

**基本写法：单例装饰器**
`function <Singleton><<T>>(<target>: <T>)`
```typescript
// 强制类为单例
function Singleton<T extends new (...args: any[]) => any>(target: T): T {
    let instance: InstanceType<T>
    return class extends target {
        constructor(...args: any[]) {
            if (instance) return instance
            super(...args)
            instance = this as any
        }
    }
}
@Singleton class Config {}
```

---

**基本写法：混入装饰器**
`function <Mixin>(...<bases>): <类装饰器>`
```typescript
// 混入多个类的方法
function Mixin(...bases: any[]) {
    return function (target: any) {
        bases.forEach(base => {
            Object.getOwnPropertyNames(base.prototype).forEach(name => {
                target.prototype[name] = base.prototype[name]
            })
        })
    }
}
```

---

**基本写法：标签元数据**
`function <Tag>(<名称>: string): <类装饰器>`
```typescript
// 给类附加元数据
function Tag(name: string) {
    return function <T extends new (...args: any[]) => any>(target: T): T {
        (target as any).tag = name
        return target
    }
}
@Tag("service") class Service {}
```

---

## 属性装饰器实战

**基本写法：默认值装饰器**
`function <Default>(<值>): <属性装饰器>`
```typescript
// 为属性设置默认值
function Default(value: any) {
    return function (target: any, key: string) {
        target[key] = value
    }
}
class Config { @Default(8080) port: number }
```

---

**基本写法：只读属性装饰器**
`function <ReadOnly>(<target>, <key>)`
```typescript
// 让属性只读
function ReadOnly(target: any, key: string) {
    Object.defineProperty(target, key, { writable: false })
}
```

---

## 装饰器工厂

**基本写法：装饰器工厂**
`function <装饰器>(<配置>): <装饰器>`
```typescript
// 工厂返回实际装饰器
function Log(prefix: string) {
    return function (target: any, key: string, desc: PropertyDescriptor) {
        const orig = desc.value
        desc.value = function (...args: any[]) {
            console.log(`${prefix}: ${key}`)
            return orig.apply(this, args)
        }
    }
}
class S { @Log("APP") run() {} }
```

---

**基本写法：多装饰器组合**
`@<A> @<B> @<C> <声明>`
```typescript
// 多装饰器从下往上执行
function A(target: any, key: string) { console.log("A") }
function B(target: any, key: string) { console.log("B") }
class S { @A @B method() {} }  // B A
```

---

## 元数据反射

**基本写法：emitDecoratorMetadata**
`import "reflect-metadata"`
```typescript
// 需要 tsconfig 开启 emitDecoratorMetadata
import "reflect-metadata"
function Meta(target: any, key: string) {
    const type = Reflect.getMetadata("design:type", target, key)
    console.log(type)  // String
}
class S { @Meta name: string = "" }
```

---

**基本写法：自定义元数据**
`Reflect.defineMetadata(<键>, <值>, <目标>)`
```typescript
// 存储自定义元数据
function Role(role: string) {
    return function (target: any, key: string) {
        Reflect.defineMetadata("role", role, target, key)
    }
}
```

---

**基本写法：读取元数据**
`Reflect.getMetadata(<键>, <目标>)`
```typescript
// 读取存储的元数据
function getRole(target: any, key: string) {
    return Reflect.getMetadata("role", target, key)
}
```

---

## 参数装饰器实战

**基本写法：必填参数装饰器**
`function <Required>(<target>, <key>, <index>)`
```typescript
// 标记参数必填
const required: Set<number> = new Set()
function Required(target: any, key: string, index: number) {
    required.add(index)
}
class S { greet(@Required name: string) {} }
```

---

**基本写法：参数注入**
`function <Inject>(<token>): <参数装饰器>`
```typescript
// 依赖注入标记
function Inject(token: string) {
    return function (target: any, key: string, index: number) {
        Reflect.defineMetadata("inject", token, target, key)
    }
}
class S { constructor(@Inject("DB") db: any) {} }
```

---

## 访问器装饰器

**基本写法：getter setter 装饰器**
`function <装饰器>(<target>, <key>, <descriptor>)`
```typescript
// 装饰访问器属性
function Log(target: any, key: string, desc: PropertyDescriptor) {
    const orig = desc.get
    desc.get = function () {
        const v = orig?.call(this)
        console.log(`get ${key}`)
        return v
    }
}
class S { private _v = 1; @Log get v() { return this._v } }
```

---

## 5.0 新版装饰器

**基本写法：Stage 3 装饰器**
`function <装饰器>(<target>, <context>) { }`
```typescript
// TS 5.0 标准 TC39 装饰器
function log(target: any, context: ClassMethodDecoratorContext) {
    return function (this: any, ...args: any[]) {
        console.log(`call ${String(context.name)}`)
        return target.apply(this, args)
    }
}
class S { @log run() {} }
```

---

**基本写法：新版类装饰器**
`function <装饰器>(<target>, <context>): <新类>`
```typescript
// TC39 类装饰器
function tag(target: any, context: ClassDecoratorContext) {
    return class extends target {
        tag = context.name
    }
}
@tag class S {}
```

---

**基本写法：新版自动访问器**
`accessor <字段>`
```typescript
// TS 5.0 自动访问器
class S {
    accessor count = 0  // 自动生成 getter setter
}
```

---

## 实用模式

**基本写法：缓存装饰器**
`function <Memoize>(<target>, <key>, <descriptor>)`
```typescript
// 缓存方法结果
function Memoize(target: any, key: string, desc: PropertyDescriptor) {
    const orig = desc.value
    const cache = new Map()
    desc.value = function (...args: any[]) {
        const k = JSON.stringify(args)
        if (!cache.has(k)) cache.set(k, orig.apply(this, args))
        return cache.get(k)
    }
}
```

---

**基本写法：防抖装饰器**
`function <Debounce>(<等待>): <方法装饰器>`
```typescript
// 方法防抖
function Debounce(wait: number) {
    return function (target: any, key: string, desc: PropertyDescriptor) {
        const orig = desc.value
        let timer: any
        desc.value = function (...args: any[]) {
            clearTimeout(timer)
            timer = setTimeout(() => orig.apply(this, args), wait)
        }
    }
}
```

---

**基本写法：节流装饰器**
`function <Throttle>(<等待>): <方法装饰器>`
```typescript
// 方法节流
function Throttle(wait: number) {
    return function (target: any, key: string, desc: PropertyDescriptor) {
        const orig = desc.value
        let last = 0
        desc.value = function (...args: any[]) {
            const now = Date.now()
            if (now - last >= wait) { last = now; return orig.apply(this, args) }
        }
    }
}
```

---

**基本写法：权限校验装饰器**
`function <Auth>(<角色>): <方法装饰器>`
```typescript
// 校验调用权限
function Auth(role: string) {
    return function (target: any, key: string, desc: PropertyDescriptor) {
        const orig = desc.value
        desc.value = function (...args: any[]) {
            if (currentUser.role !== role) throw new Error("forbidden")
            return orig.apply(this, args)
        }
    }
}
class Admin { @Auth("admin") delete() {} }
```

---

**基本写法：重试装饰器**
`function <Retry>(<次数>): <方法装饰器>`
```typescript
// 异步方法重试
function Retry(times: number) {
    return function (target: any, key: string, desc: PropertyDescriptor) {
        const orig = desc.value
        desc.value = async function (...args: any[]) {
            for (let i = 0; i < times; i++) {
                try { return await orig.apply(this, args) }
                catch (e) { if (i === times - 1) throw e }
            }
        }
    }
}
```

---

## tsconfig 配置

**基本写法：开启装饰器**
`"experimentalDecorators": true`
```json
// tsconfig.json 开启装饰器支持
{
    "compilerOptions": {
        "experimentalDecorators": true,
        "emitDecoratorMetadata": true
    }
}
```
