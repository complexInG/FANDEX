---
order: 30
title: 接口与类型别名
module: 'typescript'
category: 前端技术
difficulty: intermediate
description: interface 与 type 的定义、扩展、交叉与合并。
author: Anonymous
updated: '2026-08-01'
related:
  - 'typescript/001-TypeScriptOverviewEnvSetup'
  - 'typescript/002-BasicTypeSystem'
  - 'typescript/004-FunctionGeneric'
  - 'typescript/005-LocalTypeInference'
prerequisites: []
---

## 1. 接口 (Interface)

接口是 TypeScript 中用于定义对象结构的重要工具，它描述了对象应该具有的属性和方法。

### 1.1 基本接口定义

```typescript
// 基本接口定义
interface Person {
  name: string;
  age: number;
}
// 使用接口
const person: Person = {
  name: 'Alice',
  age: 30,
};
// 错误示例：缺少属性
// const invalidPerson: Person = {
// name: "Bob" // 缺少 age 属性
// };
```

### 1.2 可选属性

使用 `?` 标记可选属性。

```typescript
interface User {
  id: number;
  name: string;
  age?: number; // 可选属性
  email?: string; // 可选属性
}
// 正确：只提供必需属性
const user1: User = {
  id: 1,
  name: 'Alice',
};
// 正确：提供所有属性
const user2: User = {
  id: 2,
  name: 'Bob',
  age: 25,
  email: 'bob@example.com',
};
```

### 1.3 只读属性

使用 `readonly` 标记只读属性，这些属性只能在初始化时赋值，之后不能修改。

```typescript
interface Product {
  readonly id: number;
  name: string;
  price: number;
}
const product: Product = {
  id: 1001,
  name: 'Laptop',
  price: 999.99,
};
// 错误：不能修改只读属性
// product.id = 1002; // 编译错误
product.price = 899.99; // 可以修改非只读属性
```

### 1.4 函数接口

接口可以定义函数的类型。

```typescript
// 函数接口
interface GreetFunction {
  (name: string, age?: number): string;
  ;
}
// 实现函数接口
const greet: GreetFunction = (name, age) => {
  if (age) {
    return `Hello, ${name}! You are ${age} years old.`;
  }
  return `Hello, ${name}!`;
  ;
};
console.log(greet('Alice')); // Hello, Alice!
console.log(greet('Bob', 25)); // Hello, Bob! You are 25 years old.
```

### 1.5 索引签名

使用索引签名定义任意属性。

```typescript
// 字符串索引签名
interface StringMap {
  [key: string]: string;
}
const colors: StringMap = {
  red: '#FF0000',
  green: '#00FF00',
  blue: '#0000FF',
};
// 数字索引签名
interface NumberArray {
  [index: number]: number;
}
const numbers: NumberArray = [1, 2, 3, 4, 5];
// 混合索引签名
interface MixedMap {
  [key: string]: string | number;
  length: number; // 具体属性类型必须与索引签名兼容
}
const mixed: MixedMap = {
  name: 'Alice',
  age: 30,
  length: 2,
};
```

### 1.6 类实现接口

类可以实现一个或多个接口。

```typescript
interface Printable {
  print(): void;
  ;
}
interface Loggable {
  log(message: string): void;
  ;
}
// 实现单个接口
class Document implements Printable {
  print(): void {
    console.log('Printing document...');
  }
  ;
}
// 实现多个接口
class AdvancedDocument implements Printable, Loggable {
  print(): void {
    console.log('Printing advanced document...');
  }
  log(message: string): void {
    console.log(`Logging: ${message}`);
  }
  ;
}
const doc = new AdvancedDocument();
doc.print(); // Printing advanced document...
doc.log('Document created'); // Logging: Document created
```

## 2. 接口继承

接口可以继承其他接口，实现代码复用。

### 2.1 单继承

```typescript
interface Person {
  name: string;
  age: number;
}
interface Employee extends Person {
  employeeId: number;
  department: string;
}
const employee: Employee = {
  name: 'Alice',
  age: 30,
  employeeId: 1001,
  department: 'Engineering',
};
```

### 2.2 多继承

接口可以同时继承多个接口。

```typescript
interface Readable {
  read(): string;
  ;
}
interface Writeable {
  write(content: string): void;
  ;
}
interface ReadWriteable extends Readable, Writeable {
  readWrite(): void;
  ;
}
class File implements ReadWriteable {
  read(): string {
    return 'File content';
  }
  write(content: string): void {
    console.log(`Writing: ${content}`);
  }
  readWrite(): void {
    console.log('Reading and writing...');
  }
  ;
}
const file = new File();
console.log(file.read()); // File content
file.write('Hello'); // Writing: Hello
file.readWrite(); // Reading and writing...
```

### 2.3 继承与扩展

接口继承后可以添加新的属性和方法。

```typescript
interface BaseConfig {
  host: string;
  port: number;
}
interface DatabaseConfig extends BaseConfig {
  database: string;
  username: string;
  password: string;
  ssl?: boolean; // 新增可选属性
}
const dbConfig: DatabaseConfig = {
  host: 'localhost',
  port: 5432,
  database: 'mydb',
  username: 'admin',
  password: 'password',
};
```

## 3. 类型别名 (Type Aliases)

类型别名使用 `type` 关键字定义，可以为任何类型创建别名，包括原始类型、联合类型、元组等。

### 3.1 基本类型别名

```typescript
// 原始类型别名
type Age = number;
type Name = string;
type IsActive = boolean;
// 使用类型别名
const age: Age = 30;
const name: Name = 'Alice';
const isActive: IsActive = true;
// 对象类型别名
type Person = {
  name: string;
  age: number;
  email?: string;
};
const person: Person = {
  name: 'Bob',
  age: 25,
};
```

### 3.2 联合类型别名

```typescript
// 联合类型别名
type Status = 'active' | 'inactive' | 'pending';
type Result = string | number | boolean;
// 使用联合类型
const userStatus: Status = 'active';
const result1: Result = 'Success';
const result2: Result = 42;
const result3: Result = true;
// 错误示例：不在联合类型中
// const invalidStatus: Status = "deleted"; // 编译错误
```

### 3.3 元组类型别名

```typescript
// 元组类型别名
type Coordinates = [number, number];
type RGB = [number, number, number];
type PersonInfo = [string, number, boolean];
// 使用元组类型
const point: Coordinates = [10, 20];
const color: RGB = [255, 0, 0];
const personInfo: PersonInfo = ['Alice', 30, true];
// 访问元组成员
console.log(point[0]); // 10
console.log(color[1]); // 0
console.log(personInfo[2]); //
```

### 3.4 函数类型别名

```typescript
// 函数类型别名
type AddFunction = (a: number, b: number) => number;
type Callback = () => void;
type ProcessFunction = (data: any, callback: Callback) => void;
// 使用函数类型别名
const add: AddFunction = (a, b) => a + b;
const greet: Callback = () => console.log('Hello!');
const process: ProcessFunction = (data, callback) => {
  console.log('Processing data...', data);
  callback();
};
console.log(add(5, 3)); // 8
greet(); // Hello!
process({ id: 1 }, greet); // Processing data... { id: 1 }
// Hello!
```

### 3.5 交叉类型

使用 `&` 创建交叉类型，组合多个类型的特性。

```typescript
// 交叉类型
type Person = {
  name: string;
  age: number;
};
type Employee = {
  employeeId: number;
  department: string;
};
// 交叉类型：同时具有 Person 和 Employee 的属性
type EmployeePerson = Person & Employee;
const employee: EmployeePerson = {
  name: 'Alice',
  age: 30,
  employeeId: 1001,
  department: 'Engineering',
};
```

### 3.6 条件类型

使用条件类型根据其他类型创建新类型。

```typescript
 // 条件类型
 type IsString<T> = T extends string ?  : false;
 type IsNumber<T> = T extends number ?  : false;
 // 使用条件类型
 type A = IsString<string>; //
 type B = IsString<number>; // false
 type C = IsNumber<number>; //
 type D = IsNumber<string>; // false
 // 复杂条件类型
 type ExtractString<T> = T extends string ? T : never;
 type StringsOnly<T> = T extends Array<infer U> ? ExtractString<U>[] : ExtractString<T>;
 // 使用复杂条件类型
 type E = StringsOnly<string>; // string
 type F = StringsOnly<number>; // never
 type G = StringsOnly<string[]>; // string[]
 type H = StringsOnly<(string | number)[]>; // string[]
```

## 4. 接口与类型别名的对比

### 4.1 核心差异

| 特性         | Interface                      | Type Alias                                     |
| :----------- | :----------------------------- | :--------------------------------------------- |
| **定义范围** | 主要用于定义对象结构           | 可以定义任何类型（原始类型、联合类型、元组等） |
| **声明合并** | 支持（多个同名接口会自动合并） | 不支持（同名类型别名会导致编译错误）           |
| **扩展方式** | 使用 `extends` 关键字          | 使用交叉类型 `&`                               |
| **计算属性** | 不支持                         | 支持                                           |
| **类型参数** | 支持泛型                       | 支持泛型                                       |
| **使用场景** | 定义对象结构、类接口           | 定义联合类型、元组类型、复杂类型组合           |

### 4.2 声明合并

接口支持声明合并，多个同名接口会自动合并为一个。

```typescript
// 声明合并示例
interface User {
  id: number;
  name: string;
}
// 自动合并到上面的 User 接口
interface User {
  age?: number;
  email?: string;
}
// 使用合并后的接口
const user: User = {
  id: 1,
  name: 'Alice',
  age: 30,
  email: 'alice@example.com',
};
```

类型别名不支持声明合并。

```typescript
// 错误：类型别名不能重复声明
// type User = {
// id: number;
// name: string;
// };
// 编译错误：重复的标识符 'User'
// type User = {
// age?: number;
// };
```

### 4.3 扩展方式

接口使用 `extends` 扩展。

```typescript
interface Person {
  name: string;
  age: number;
  ;
}
interface Employee extends Person {
  employeeId: number;
  department: string;
  ;
}
```

类型别名使用交叉类型 `&` 扩展。

```typescript
type Person = {
  name: string;
  age: number;
  ;
};
type Employee = Person & {
  employeeId: number;
  department: string;
  ;
};
```

### 4.4 计算属性

类型别名支持计算属性。

```typescript
// 计算属性示例
type Keys = 'a' | 'b' | 'c';
type StringMap = {
  [K in Keys]: string;
};
// 等价于
// type StringMap = {
// a: string;
// b: string;
// c: string;
// };
const map: StringMap = {
  a: 'value1',
  b: 'value2',
  c: 'value3',
};
```

接口不支持计算属性。

### 4.5 泛型支持

两者都支持泛型。

```typescript
// 泛型接口
interface GenericInterface<T> {
  value: T;
  getValue(): T;
}
// 泛型类型别名
type GenericType<T> = {
  value: T;
  getValue(): T;
};
// 使用泛型
const numInterface: GenericInterface<number> = {
  value: 42,
  getValue: () => 42,
};
const stringType: GenericType<string> = {
  value: 'Hello',
  getValue: () => 'Hello',
};
```

## 5. 最佳实践

### 5.1 选择原则

- **优先使用接口**：当定义对象结构、类接口时，优先使用 `interface`。
- **使用类型别名**：当需要定义联合类型、元组类型、交叉类型或其他复杂类型时，使用 `type`。

### 5.2 具体场景

| 场景             | 推荐使用    | 原因                             |
| :--------------- | :---------- | :------------------------------- |
| 定义对象结构     | `interface` | 支持声明合并，更符合面向对象思维 |
| 定义类接口       | `interface` | 类可以使用 `implements` 实现接口 |
| 定义联合类型     | `type`      | 接口不支持联合类型               |
| 定义元组类型     | `type`      | 接口不支持元组类型               |
| 定义交叉类型     | `type`      | 使用 `&` 更简洁                  |
| 定义条件类型     | `type`      | 接口不支持条件类型               |
| 定义原始类型别名 | `type`      | 接口只能定义对象结构             |

### 5.3 实际应用建议

1. **保持一致性**：在项目中保持使用接口和类型别名的一致性。
2. **清晰命名**：为接口和类型别名使用清晰、描述性的名称。
3. **合理使用**：根据具体场景选择合适的方式，不要过度使用其中一种。
4. **文档化**：对于复杂的类型定义，添加注释说明其用途。

## 6. 代码示例

### 6.1 接口的综合使用

```typescript
// 基本接口
interface User {
  readonly id: number;
  name: string;
  age?: number;
  email?: string;
  ;
}
// 函数接口
interface UserService {
  getUser(id: number): User;
  createUser(user: Omit<User, 'id'>): User;
  updateUser(id: number, user: Partial<User>): User;
  deleteUser(id: number): boolean;
  ;
}
// 实现接口
class UserServiceImpl implements UserService {
  private users: User[] = [
    { id: 1, name: 'Alice', age: 30, email: 'alice@example.com' },
    { id: 2, name: 'Bob', age: 25 },
  ];
  getUser(id: number): User {
    const user = this.users.find((u) => u.id === id);
    if (!user) {
      throw new Error(`User with id ${id} not found`);
    }
    return user;
  }
  createUser(user: Omit<User, 'id'>): User {
    const newUser: User = {
      id: this.users.length + 1,
      ...user,
    };
    this.users.push(newUser);
    return newUser;
  }
  updateUser(id: number, user: Partial<User>): User {
    const index = this.users.findIndex((u) => u.id === id);
    if (index === -1) {
      throw new Error(`User with id ${id} not found`);
    }
    this.users[index] = { ...this.users[index], ...user };
    return this.users[index];
  }
  deleteUser(id: number): boolean {
    const initialLength = this.users.length;
    this.users = this.users.filter((u) => u.id !== id);
    return this.users.length < initialLength;
  }
  ;
}
// 使用示例
const userService = new UserServiceImpl();
console.log('Get user 1:', userService.getUser(1));
const newUser = userService.createUser({ name: 'Charlie', age: 35 });
console.log('Created user:', newUser);
const updatedUser = userService.updateUser(1, { age: 31, email: 'alice.updated@example.com' });
console.log('Updated user:', updatedUser);
const deleted = userService.deleteUser(2);
console.log('Deleted user 2:', deleted);
console.log('All users:', userService);
```

### 6.2 类型别名的综合使用

```typescript
// 基本类型别名
type UserId = number;
type UserName = string;
type Email = string;
// 联合类型
type UserRole = 'admin' | 'user' | 'guest';
type Status = 'active' | 'inactive' | 'pending';
// 元组类型
type UserCredentials = [UserName, string]; // [username, password]
type Coordinates = [number, number]; // [x, y]
// 对象类型
type User = {
  id: UserId;
  name: UserName;
  email: Email;
  role: UserRole;
  status: Status;
  lastLogin?: Date;
  ;
};
// 交叉类型
type AdminPermissions = {
  canManageUsers: boolean;
  canManageSettings: boolean;
  ;
};
type AdminUser = User & AdminPermissions;
// 函数类型
type UserValidator = (user: User) => boolean;
type AsyncCallback = (error: Error | null, result: any) => void;
// 使用示例
const validateUser: UserValidator = (user) => {
  return !!user.name && !!user.email && !!user.role;
  ;
};
const adminUser: AdminUser = {
  id: 1,
  name: 'Alice',
  email: 'alice@example.com',
  role: 'admin',
  status: 'active',
  canManageUsers: true,
  canManageSettings: True,
};
const credentials: UserCredentials = ['alice', 'password123'];
const position: Coordinates = [10, 20];
console.log('Admin user:', adminUser);
console.log('Credentials:', credentials);
console.log('Position:', position);
console.log('Is valid user:', validateUser(adminUser));
```

### 6.3 接口与类型别名的混合使用

```typescript
// 接口定义核心结构
interface BaseEntity {
  id: number;
  createdAt: Date;
  updatedAt: Date;
}
// 类型别名定义复杂类型
type EntityType = 'user' | 'product' | 'order';
type EntityStatus = 'active' | 'inactive' | 'deleted';
// 接口继承并使用类型别名
interface User extends BaseEntity {
  name: string;
  email: string;
  type: Extract<EntityType, 'user'>;
  status: EntityStatus;
}
interface Product extends BaseEntity {
  name: string;
  price: number;
  type: Extract<EntityType, 'product'>;
  status: EntityStatus;
}
// 类型别名创建联合类型
type Entity = User | Product;
// 类型守卫函数
type EntityGuard<T extends EntityType> = (entity: Entity) => entity is Extract<Entity, { type: T }>;
const isUser: EntityGuard<'user'> = (entity): entity is User => {
  return entity.type === 'user';
};
const isProduct: EntityGuard<'product'> = (entity): entity is Product => {
  return entity.type === 'product';
};
// 使用示例
const user: User = {
  id: 1,
  name: 'Alice',
  email: 'alice@example.com',
  type: 'user',
  status: 'active',
  createdAt: new Date(),
  updatedAt: new Date(),
};
const product: Product = {
  id: 1001,
  name: 'Laptop',
  price: 999.99,
  type: 'product',
  status: 'active',
  createdAt: new Date(),
  updatedAt: new Date(),
};
const processEntity = (entity: Entity) => {
  console.log(`Processing entity ${entity.id} (${entity.type})`);
  if (isUser(entity)) {
    console.log(`User: ${entity.name}, Email: ${entity.email}`);
  } else if (isProduct(entity)) {
    console.log(`Product: ${entity.name}, Price: $${entity.price}`);
  }
};
processEntity(user);
processEntity(product);
```

---

## 接口定义

**换行写法：定义基本接口**
`interface <接口名> {`
`    <属性1>: <类型1>`
`    <属性2>: <类型2>`
`}`

```typescript
// 定义基本接口
interface User {
    name: string
    age: number
}
```

---

**基本写法：使用接口**
`let <变量>: <接口名> = { <属性>: <值> }`

```typescript
// 使用接口定义对象
let user: User = { name: "Alice", age: 30 }
```

---

## 可选属性

**换行写法：接口可选属性**
`interface <接口名> {`
`    <属性1>: <类型1>`
`    <属性2>?: <类型2>`
`}`

```typescript
// 接口可选属性（使用 ? 标记）
interface User {
    name: string
    age?: number
}
```

---

## 只读属性

**换行写法：接口只读属性**
`interface <接口名> {`
`    readonly <属性>: <类型>`
`}`

```typescript
// 接口只读属性
interface User {
    readonly id: number
    name: string
}
```

---

## 接口继承

**基本写法：单继承**
`interface <子接口> extends <父接口> { <属性>: <类型> }`

```typescript
// 接口单继承
interface Animal {
    name: string
}

interface Dog extends Animal {
    breed: string
}
```

---

**基本写法：多继承**
`interface <子接口> extends <父接口1>, <父接口2> { <属性>: <类型> }`

```typescript
// 接口多继承
interface Flyable {
    fly(): void
}

interface Swimmable {
    swim(): void
}

interface Duck extends Flyable, Swimmable {
    name: string
}
```

---

## 函数类型接口

**换行写法：定义函数类型接口**
`interface <接口名> {`
`    (<参数>: <类型>): <返回类型>`
`}`

```typescript
// 定义函数类型接口
interface SearchFunc {
    (source: string, sub: string): boolean
}
```

---

**基本写法：使用函数类型接口**
`let <变量>: <接口名> = (<参数>) => <表达式>`

```typescript
// 使用函数类型接口
let search: SearchFunc = (src, sub) => src.includes(sub)
```

---

## 可索引类型接口

**换行写法：字符串索引签名**
`interface <接口名> {`
`    [key: string]: <类型>`
`}`

```typescript
// 字符串索引签名
interface StringArray {
    [index: string]: string
}
```

---

**换行写法：数字索引签名**
`interface <接口名> {`
`    [index: number]: <类型>`
`}`

```typescript
// 数字索引签名
interface NumberArray {
    [index: number]: string
}
```

---

## 类类型接口

**换行写法：类实现接口**
`interface <接口名> {`
`    <方法>(<参数>): <返回类型>`
`}`
`class <类名> implements <接口名> { <语句> }`

```typescript
// 类实现接口
interface Clock {
    current_time: Date
    set_time(d: Date): void
}

class DigitalClock implements Clock {
    current_time = new Date()
    set_time(d: Date) {
        this.current_time = d
    }
}
```

---

## 类型别名

**基本写法：定义类型别名**
`type <别名> = <类型>`

```typescript
// 定义类型别名
type Name = string
type Age = number
```

---

**换行写法：对象类型别名**
`type <别名> = {`
`    <属性1>: <类型1>`
`    <属性2>: <类型2>`
`}`

```typescript
// 对象类型别名
type User = {
    name: string
    age: number
}
```

---

**基本写法：联合类型别名**
`type <别名> = <类型1> | <类型2>`

```typescript
// 联合类型别名
type ID = string | number
```

---

**基本写法：交叉类型别名**
`type <别名> = <类型1> & <类型2>`

```typescript
// 交叉类型别名
type Person = { name: string }
type Employee = { id: number }
type Staff = Person & Employee
```

---

## 接口与类型别名对比

**换行写法：接口扩展**
`interface <接口名> extends <父接口> { <属性>: <类型> }`

```typescript
// 接口扩展（使用 extends）
interface Animal {
    name: string
}

interface Dog extends Animal {
    breed: string
}
```

---

**基本写法：类型别名交叉**
`type <别名> = <类型1> & <类型2>`

```typescript
// 类型别名交叉（使用 &）
type Animal = { name: string }
type Dog = Animal & { breed: string }
```

---

## 函数类型

**基本写法：使用 type 定义函数类型**
`type <函数类型> = (<参数>: <类型>) => <返回类型>`

```typescript
// 使用 type 定义函数类型
type Callback = (data: string) => void
```

---

**基本写法：使用 interface 定义函数类型**
`interface <函数类型> { (<参数>: <类型>): <返回类型> }`

```typescript
// 使用 interface 定义函数类型
interface Callback {
    (data: string): void
}
```

---

## 合并接口

**换行写法：接口声明合并**
`interface <接口名> { <属性1>: <类型1> }`
`interface <接口名> { <属性2>: <类型2> }`

```typescript
// 接口声明合并（同名接口自动合并）
interface Box {
    width: number
}

interface Box {
    height: number
}
```

---

## 描述对象

**换行写法：描述复杂对象**
`interface <接口名> {`
`    <属性>: <类型>`
`    <嵌套对象>: {`
`        <子属性>: <类型>`
`    }`
`}`

```typescript
// 描述复杂嵌套对象
interface User {
    name: string
    address: {
        street: string
        city: string
    }
}
```

---

## 数组类型接口

**换行写法：描述对象数组**
`interface <接口名> {`
`    <属性>: <类型>`
`}`
`let <变量>: <接口名>[] = [<对象>]`

```typescript
// 描述对象数组
interface Product {
    name: string
    price: number
}

let products: Product[] = [
    { name: "Apple", price: 1.5 },
    { name: "Banana", price: 0.5 },
]
```

---

## readonly 与 Readonly

**基本写法：使用 readonly 修饰符**
`interface <接口名> { readonly <属性>: <类型> }`

```typescript
// 使用 readonly 修饰符
interface Point {
    readonly x: number
    readonly y: number
}
```

---

**基本写法：使用 Readonly 工具类型**
`type <别名> = Readonly<<接口>>`

```typescript
// 使用 Readonly 工具类型
type ReadonlyUser = Readonly<User>
```

---

## Partial 与 Required

**基本写法：使用 Partial 工具类型**
`type <别名> = Partial<<接口>>`

```typescript
// 使用 Partial 使所有属性可选
type PartialUser = Partial<User>
```

---

**基本写法：使用 Required 工具类型**
`type <别名> = Required<<接口>>`

```typescript
// 使用 Required 使所有属性必填
type RequiredUser = Required<User>
```

---

## Pick 与 Omit

**基本写法：使用 Pick 工具类型**
`type <别名> = Pick<<接口>, "<属性1>" | "<属性2>">`

```typescript
// 使用 Pick 选取部分属性
type UserBasic = Pick<User, "name" | "age">
```

---

**基本写法：使用 Omit 工具类型**
`type <别名> = Omit<<接口>, "<属性>">`

```typescript
// 使用 Omit 排除部分属性
type UserWithoutAge = Omit<User, "age">
```

---

## Record 类型

**基本写法：使用 Record 工具类型**
`type <别名> = Record<<键类型>, <值类型>>`

```typescript
// 使用 Record 创建键值对类型
type UserMap = Record<string, User>
```

---

## 函数参数类型

**换行写法：描述函数参数对象**
`interface <参数接口> {`
`    <属性1>: <类型1>`
`    <属性2>: <类型2>`
`}`
`function <函数>(<参数>: <参数接口>): <返回类型> { <语句> }`

```typescript
// 描述函数参数对象
interface Config {
    host: string
    port: number
    timeout?: number
}

function connect(config: Config): void {
    console.log(`${config.host}:${config.port}`)
}
```

---

## 可调用接口

**换行写法：可调用对象接口**
`interface <接口名> {`
`    (<参数>: <类型>): <返回类型>`
`    <属性>: <类型>`
`}`

```typescript
// 可调用对象接口（既是函数又有属性）
interface Counter {
    (start: number): void
    count: number
}
```

---

## 构造器类型

**换行写法：构造器接口**
`interface <接口名> {`
`    new (<参数>: <类型>): <对象类型>`
`}`

```typescript
// 构造器接口
interface ClockConstructor {
    new (hour: number, minute: number): ClockInterface
}

interface ClockInterface {
    tick(): void
}
```
