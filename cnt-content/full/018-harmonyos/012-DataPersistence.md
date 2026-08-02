---
order: 120
title: 数据持久化
module: 'harmonyos'
category: 后端技术
difficulty: intermediate
description: Preferences与关系型数据库
author: fanquanpp
updated: '2026-08-01'
related:
  - 'harmonyos/010-NavigationRoute'
  - 'harmonyos/011-NetworkRequest'
  - 'harmonyos/013-AnimationSystem'
  - 'harmonyos/014-GestureInteraction'
prerequisites:
  - 'harmonyos/001-OverviewSetup'
---

## 概述

数据持久化是应用开发中的核心能力之一，用于将数据保存到设备存储中，确保应用重启后数据依然可用。HarmonyOS 提供了三种主要的数据持久化方案：Preferences（轻量级键值存储）、关系型数据库（基于 SQLite 的 RDB）和分布式数据服务。Preferences 适合存储少量配置信息，关系型数据库适合结构化数据的增删改查，分布式数据服务则用于多设备间的数据同步。

## 基础概念

**Preferences**：轻量级键值对存储，类似 Android 的 SharedPreferences。数据以 XML 文件形式保存在应用沙箱目录下，支持 number、string、boolean、Array 等基本类型。适合存储用户设置、登录状态等少量数据。

**关系型数据库（RDB）**：基于 SQLite 的关系型数据库，支持完整的 SQL 语法。通过 relationalStore 模块操作，提供增删改查、事务、加密等能力。适合存储结构化的业务数据。

**安全级别**：RDB 数据库支持 S1（低）、S2（中）、S3（高）三个安全级别，级别越高对数据加密保护越强。

**分布式数据服务**：支持多设备间数据自动同步的持久化方案，基于分布式软总线实现设备发现和数据传输。

## 快速上手

### Preferences 基本操作

```typescript
import dataPreferences from '@ohos.data.preferences'

@Component
struct PreferencesDemo {
  @State username: string = ''

  // 保存数据
  async savePreference(key: string, value: string) {
    // 获取 Preferences 实例
    const prefs = await dataPreferences.getPreferences(getContext(this), 'app_settings')
    // 写入键值对
    await prefs.put(key, value)
    // 刷写到磁盘
    await prefs.flush()
  }

  // 读取数据
  async loadPreference(key: string) {
    const prefs = await dataPreferences.getPreferences(getContext(this), 'app_settings')
    // 第二个参数为默认值
    this.username = await prefs.get(key, '未设置') as string
  }

  build() {
    Column({ space: 10 }) {
      TextInput({ placeholder: '输入用户名' })
        .onChange((value) => {
          this.username = value
        })

      Button('保存')
        .onClick(() => this.savePreference('username', this.username))

      Button('读取')
        .onClick(() => this.loadPreference('username'))

      Text(`当前用户名: ${this.username}`)
    }
    .padding(20)
  }
}
```

### 关系型数据库基本操作

```typescript
import relationalStore from '@ohos.data.relationalStore'

// 建表 SQL
const SQL_CREATE_TABLE = `
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT
  )
`

@Component
struct RdbDemo {
  private rdbStore: relationalStore.RdbStore | null = null

  // 初始化数据库
  async initDatabase() {
    this.rdbStore = await relationalStore.getRdbStore(getContext(this), {
      name: 'app.db',
      securityLevel: relationalStore.SecurityLevel.S1,
    })
    // 执行建表语句
    await this.rdbStore.executeSql(SQL_CREATE_TABLE)
  }

  build() {
    Column({ space: 10 }) {
      Button('初始化数据库')
        .onClick(() => this.initDatabase())
    }
    .padding(20)
  }
}
```

## 详细用法

### Preferences 完整操作

```typescript
import dataPreferences from '@ohos.data.preferences';

class PreferencesManager {
  private prefs: dataPreferences.Preferences | null = null;

  // 初始化
  async init(context: Context) {
    this.prefs = await dataPreferences.getPreferences(context, 'my_app');
  }

  // 存储字符串
  async putString(key: string, value: string) {
    if (this.prefs) {
      await this.prefs.put(key, value);
      await this.prefs.flush();
    }
  }

  // 存储数字
  async putNumber(key: string, value: number) {
    if (this.prefs) {
      await this.prefs.put(key, value);
      await this.prefs.flush();
    }
  }

  // 存储布尔值
  async putBoolean(key: string, value: boolean) {
    if (this.prefs) {
      await this.prefs.put(key, value);
      await this.prefs.flush();
    }
  }

  // 读取字符串
  async getString(key: string, defaultValue: string = ''): Promise<string> {
    if (this.prefs) {
      return (await this.prefs.get(key, defaultValue)) as string;
    }
    return defaultValue;
  }

  // 读取数字
  async getNumber(key: string, defaultValue: number = 0): Promise<number> {
    if (this.prefs) {
      return (await this.prefs.get(key, defaultValue)) as number;
    }
    return defaultValue;
  }

  // 读取布尔值
  async getBoolean(key: string, defaultValue: boolean = false): Promise<boolean> {
    if (this.prefs) {
      return (await this.prefs.get(key, defaultValue)) as boolean;
    }
    return defaultValue;
  }

  // 删除指定键
  async remove(key: string) {
    if (this.prefs) {
      await this.prefs.delete(key);
      await this.prefs.flush();
    }
  }

  // 检查键是否存在
  async has(key: string): Promise<boolean> {
    if (this.prefs) {
      return this.prefs.has(key);
    }
    return false;
  }

  // 清空所有数据
  async clear() {
    if (this.prefs) {
      await this.prefs.clear();
      await this.prefs.flush();
    }
  }
}
```

### RDB 增删改查

```typescript
import relationalStore from '@ohos.data.relationalStore';

// 定义用户数据类型
interface User {
  id?: number;
  name: string;
  age: number;
  email: string;
}

class UserRepository {
  private store: relationalStore.RdbStore | null = null;

  // 初始化
  async init(context: Context) {
    this.store = await relationalStore.getRdbStore(context, {
      name: 'user.db',
      securityLevel: relationalStore.SecurityLevel.S1,
    });
    await this.store.executeSql(`
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
      )
    `);
  }

  // 插入数据
  async insert(user: User): Promise<number> {
    if (!this.store) return -1;
    const valueBucket: relationalStore.ValuesBucket = {
      name: user.name,
      age: user.age,
      email: user.email,
    };
    return await this.store.insert('users', valueBucket);
  }

  // 查询所有数据
  async queryAll(): Promise<User[]> {
    if (!this.store) return [];
    const predicates = new relationalStore.RdbPredicates('users');
    const resultSet = await this.store.query(predicates);
    const users: User[] = [];

    while (resultSet.goToNextRow()) {
      users.push({
        id: resultSet.getLong(resultSet.getColumnIndex('id')),
        name: resultSet.getString(resultSet.getColumnIndex('name')),
        age: resultSet.getLong(resultSet.getColumnIndex('age')),
        email: resultSet.getString(resultSet.getColumnIndex('email')),
      });
    }
    resultSet.close();
    return users;
  }

  // 条件查询
  async queryByName(name: string): Promise<User[]> {
    if (!this.store) return [];
    const predicates = new relationalStore.RdbPredicates('users');
    predicates.equalTo('name', name);
    const resultSet = await this.store.query(predicates);
    const users: User[] = [];

    while (resultSet.goToNextRow()) {
      users.push({
        id: resultSet.getLong(resultSet.getColumnIndex('id')),
        name: resultSet.getString(resultSet.getColumnIndex('name')),
        age: resultSet.getLong(resultSet.getColumnIndex('age')),
        email: resultSet.getString(resultSet.getColumnIndex('email')),
      });
    }
    resultSet.close();
    return users;
  }

  // 更新数据
  async update(user: User): Promise<number> {
    if (!this.store || !user.id) return 0;
    const valueBucket: relationalStore.ValuesBucket = {
      name: user.name,
      age: user.age,
      email: user.email,
    };
    const predicates = new relationalStore.RdbPredicates('users');
    predicates.equalTo('id', user.id);
    return await this.store.update(valueBucket, predicates);
  }

  // 删除数据
  async delete(id: number): Promise<number> {
    if (!this.store) return 0;
    const predicates = new relationalStore.RdbPredicates('users');
    predicates.equalTo('id', id);
    return await this.store.delete(predicates);
  }
}
```

### RDB 事务操作

```typescript
class OrderService {
  private store: relationalStore.RdbStore | null = null;

  // 使用事务保证数据一致性
  async transferOrder(fromUserId: number, toUserId: number, amount: number) {
    if (!this.store) return;

    try {
      // 开启事务
      this.store.beginTransaction();

      // 扣减转出方余额
      const fromBucket: relationalStore.ValuesBucket = {};
      const fromPredicates = new relationalStore.RdbPredicates('accounts');
      fromPredicates.equalTo('user_id', fromUserId);
      // ... 执行扣减逻辑

      // 增加接收方余额
      const toBucket: relationalStore.ValuesBucket = {};
      const toPredicates = new relationalStore.RdbPredicates('accounts');
      toPredicates.equalTo('user_id', toUserId);
      // ... 执行增加逻辑

      // 提交事务
      this.store.commit();
      console.info('事务提交成功');
    } catch (error) {
      // 回滚事务
      this.store.rollBack();
      console.error(`事务回滚: ${error}`);
    }
  }
}
```

## 常见场景

### 用户设置持久化

```typescript
interface AppSettings {
  theme: string
  fontSize: number
  notifications: boolean
  language: string
}

@Component
struct SettingsPage {
  private prefsManager: PreferencesManager = new PreferencesManager()
  @State settings: AppSettings = {
    theme: 'light',
    fontSize: 14,
    notifications: true,
    language: 'zh-CN',
  }

  async aboutToAppear() {
    // 初始化并加载设置
    await this.prefsManager.init(getContext(this))
    this.settings.theme = await this.prefsManager.getString('theme', 'light')
    this.settings.fontSize = await this.prefsManager.getNumber('fontSize', 14)
    this.settings.notifications = await this.prefsManager.getBoolean('notifications', true)
    this.settings.language = await this.prefsManager.getString('language', 'zh-CN')
  }

  async saveSettings() {
    await this.prefsManager.putString('theme', this.settings.theme)
    await this.prefsManager.putNumber('fontSize', this.settings.fontSize)
    await this.prefsManager.putBoolean('notifications', this.settings.notifications)
    await this.prefsManager.putString('language', this.settings.language)
  }

  build() {
    Column({ space: 15 }) {
      Text('应用设置').fontSize(20).fontWeight(FontWeight.Bold)

      // 主题选择
      Row() {
        Text('主题模式')
        Toggle({ type: ToggleType.Switch, isOn: this.settings.theme === 'dark' })
          .onChange((isOn) => {
            this.settings.theme = isOn ? 'dark' : 'light'
            this.saveSettings()
          })
      }
      .width('100%')
      .justifyContent(FlexAlign.SpaceBetween)

      // 字体大小
      Row() {
        Text(`字体大小: ${this.settings.fontSize}`)
        Slider({
          value: this.settings.fontSize,
          min: 12,
          max: 24,
          step: 1
        })
          .onChange((value) => {
            this.settings.fontSize = Math.round(value)
            this.saveSettings()
          })
      }

      // 通知开关
      Row() {
        Text('推送通知')
        Toggle({ type: ToggleType.Switch, isOn: this.settings.notifications })
          .onChange((isOn) => {
            this.settings.notifications = isOn
            this.saveSettings()
          })
      }
      .width('100%')
      .justifyContent(FlexAlign.SpaceBetween)
    }
    .padding(20)
  }
}
```

### 备忘录数据存储

```typescript
interface Memo {
  id?: number
  title: string
  content: string
  createdAt: string
  updatedAt: string
}

@Component
struct MemoApp {
  private store: relationalStore.RdbStore | null = null
  @State memos: Memo[] = []

  async aboutToAppear() {
    // 初始化数据库
    this.store = await relationalStore.getRdbStore(getContext(this), {
      name: 'memo.db',
      securityLevel: relationalStore.SecurityLevel.S1,
    })
    await this.store.executeSql(`
      CREATE TABLE IF NOT EXISTS memos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT,
        createdAt TEXT,
        updatedAt TEXT
      )
    `)
    await this.loadMemos()
  }

  // 加载所有备忘录
  async loadMemos() {
    if (!this.store) return
    const predicates = new relationalStore.RdbPredicates('memos')
    predicates.orderByDesc('updatedAt')
    const resultSet = await this.store.query(predicates)
    this.memos = []

    while (resultSet.goToNextRow()) {
      this.memos.push({
        id: resultSet.getLong(resultSet.getColumnIndex('id')),
        title: resultSet.getString(resultSet.getColumnIndex('title')),
        content: resultSet.getString(resultSet.getColumnIndex('content')),
        createdAt: resultSet.getString(resultSet.getColumnIndex('createdAt')),
        updatedAt: resultSet.getString(resultSet.getColumnIndex('updatedAt')),
      })
    }
    resultSet.close()
  }

  // 添加备忘录
  async addMemo(title: string, content: string) {
    if (!this.store) return
    const now = new Date().toISOString()
    await this.store.insert('memos', {
      title,
      content,
      createdAt: now,
      updatedAt: now,
    })
    await this.loadMemos()
  }

  // 删除备忘录
  async deleteMemo(id: number) {
    if (!this.store) return
    const predicates = new relationalStore.RdbPredicates('memos')
    predicates.equalTo('id', id)
    await this.store.delete(predicates)
    await this.loadMemos()
  }

  build() {
    Column() {
      List() {
        ForEach(this.memos, (memo: Memo) => {
          ListItem() {
            Column() {
              Text(memo.title).fontSize(16).fontWeight(FontWeight.Medium)
              Text(memo.content).fontSize(13).fontColor('#666666').maxLines(2)
              Text(memo.updatedAt).fontSize(11).fontColor('#999999')
            }
            .padding(12)
            .backgroundColor(Color.White)
            .borderRadius(8)
          }
          .swipeAction({
            end: Button('删除')
              .backgroundColor(Color.Red)
              .onClick(() => {
                if (memo.id) this.deleteMemo(memo.id)
              })
          })
        }, (memo: Memo) => memo.id?.toString() ?? '')
      }
      .layoutWeight(1)
    }
    .padding(16)
  }
}
```

## 注意事项

- **Preferences 数据量**：Preferences 不适合存储大量数据，建议单个文件不超过几百条记录。大量结构化数据应使用 RDB。
- **flush 调用**：Preferences 的 put 操作仅修改内存缓存，必须调用 flush 才能持久化到磁盘。应用退出前确保已调用 flush。
- **RDB 线程安全**：RDB 操作是线程安全的，但大量并发写入时应考虑使用事务批量处理，避免频繁的单条操作。
- **ResultSet 关闭**：查询返回的 ResultSet 必须手动关闭，否则会导致内存泄漏。建议在 finally 块中关闭。
- **安全级别选择**：S1 适合普通数据，S2 适合包含隐私信息的数据，S3 适合高度敏感数据。级别越高性能开销越大。
- **数据库版本迁移**：RDB 没有内置的版本迁移机制，需要自行管理数据库升级逻辑，通过检查版本号执行增量 SQL。

## 进阶用法

### 数据库加密

```typescript
import relationalStore from '@ohos.data.relationalStore';

async function createEncryptedDatabase(context: Context) {
  // 创建加密数据库
  const store = await relationalStore.getRdbStore(context, {
    name: 'secure.db',
    securityLevel: relationalStore.SecurityLevel.S3, // 高安全级别
    encrypt: true, // 启用加密
  });

  await store.executeSql(`
    CREATE TABLE IF NOT EXISTS credentials (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      service TEXT NOT NULL,
      username TEXT,
      password TEXT
    )
  `);

  return store;
}
```

### 批量操作与性能优化

```typescript
class BatchOperationDemo {
  private store: relationalStore.RdbStore | null = null;

  // 批量插入：使用事务提升性能
  async batchInsert(items: object[]) {
    if (!this.store) return;

    try {
      this.store.beginTransaction();

      for (const item of items) {
        await this.store.insert('items', item as relationalStore.ValuesBucket);
      }

      this.store.commit();
      console.info(`批量插入 ${items.length} 条数据成功`);
    } catch (error) {
      this.store.rollBack();
      console.error(`批量插入失败: ${error}`);
    }
  }

  // 分页查询
  async queryByPage(page: number, pageSize: number) {
    if (!this.store) return [];
    const predicates = new relationalStore.RdbPredicates('items');
    // 设置分页参数
    predicates.limit(pageSize, (page - 1) * pageSize);
    predicates.orderByDesc('id');

    const resultSet = await this.store.query(predicates);
    const results: object[] = [];

    while (resultSet.goToNextRow()) {
      // 解析数据...
      results.push({});
    }
    resultSet.close();
    return results;
  }

  // 模糊查询
  async searchByKeyword(keyword: string) {
    if (!this.store) return [];
    const predicates = new relationalStore.RdbPredicates('items');
    // 使用 like 进行模糊匹配
    predicates.like('name', `%${keyword}%`);

    const resultSet = await this.store.query(predicates);
    const results: object[] = [];

    while (resultSet.goToNextRow()) {
      results.push({});
    }
    resultSet.close();
    return results;
  }
}
```

### 数据变更监听

```typescript
import dataPreferences from '@ohos.data.preferences'

@Component
struct PreferenceObserverDemo {
  @State theme: string = 'light'
  private prefs: dataPreferences.Preferences | null = null

  async aboutToAppear() {
    this.prefs = await dataPreferences.getPreferences(getContext(this), 'settings')

    // 注册数据变更监听
    this.prefs.on('change', (data: dataPreferences.ChangeInfo) => {
      console.info('数据发生变更')
      // 检查 theme 键是否变更
      if (data.keys.includes('theme')) {
        this.loadTheme()
      }
    })

    await this.loadTheme()
  }

  async loadTheme() {
    if (this.prefs) {
      this.theme = (await this.prefs.get('theme', 'light')) as string
    }
  }

  async toggleTheme() {
    if (this.prefs) {
      const newTheme = this.theme === 'light' ? 'dark' : 'light'
      await this.prefs.put('theme', newTheme)
      await this.prefs.flush()
    }
  }

  build() {
    Column() {
      Text(`当前主题: ${this.theme}`)
      Button('切换主题')
        .onClick(() => this.toggleTheme())
    }
    .padding(20)
  }
}
```
## Preferences 模块导入

**导入 preferences 模块**
`import dataPreferences from '@ohos.data.preferences'`
```typescript
import dataPreferences from '@ohos.data.preferences';
```

**通过 ArkData 导入**
`import { preferences } from '@kit.ArkData'`
```typescript
import { preferences } from '@kit.ArkData';
```

**支持的数据类型**
`preferences.ValueType`
```typescript
type ValueType = number | string | boolean | Array<number> | Array<string> | Array<boolean> | Uint8Array;
```

---

## Preferences API

**获取 Preferences 实例**
`preferences.getPreferences(context: Context, name: string): Promise<Preferences>`
```typescript
const prefs = await preferences.getPreferences(getContext(this), 'app_settings');
```

**写入数据**
`prefs.put(key: string, value: ValueType): Promise<void>`
```typescript
await prefs.put('username', '张三');
await prefs.put('fontSize', 16);
await prefs.put('notifications', true);
await prefs.put('tags', ['work', 'life']);
```

**刷写到磁盘**
`prefs.flush(): Promise<void>`
```typescript
await prefs.flush();
```

**读取数据**
`prefs.get(key: string, defaultValue: ValueType): Promise<ValueType>`
```typescript
const username = await prefs.get('username', '未设置') as string;
const fontSize = await prefs.get('fontSize', 14) as number;
const notifications = await prefs.get('notifications', true) as boolean;
```

**检查键是否存在**
`prefs.has(key: string): Promise<boolean>`
```typescript
const exists = await prefs.has('username');
```

**删除指定键**
`prefs.delete(key: string): Promise<void>`
```typescript
await prefs.delete('username');
await prefs.flush();
```

**清空所有数据**
`prefs.clear(): Promise<void>`
```typescript
await prefs.clear();
await prefs.flush();
```

**获取所有键**
`prefs.getAll(): Promise<Object>`
```typescript
const allData = await prefs.getAll();
```

---

## Preferences 数据变更监听

**注册监听**
`prefs.on('change', callback: (data: ChangeInfo) => void): void`
```typescript
prefs.on('change', (data: preferences.ChangeInfo) => {
  if (data.keys.includes('theme')) {
    console.info('主题已变更');
  }
});
```

**取消监听**
`prefs.off('change', callback?: (data: ChangeInfo) => void): void`
```typescript
prefs.off('change');
```

---

## Preferences 管理器封装

**PreferencesManager 封装**
```typescript
class PreferencesManager {
  private prefs: preferences.Preferences | null = null;

  async init(context: Context): Promise<void> {
    this.prefs = await preferences.getPreferences(context, 'my_app');
  }

  async putString(key: string, value: string): Promise<void> {
    if (this.prefs) {
      await this.prefs.put(key, value);
      await this.prefs.flush();
    }
  }

  async putNumber(key: string, value: number): Promise<void> {
    if (this.prefs) {
      await this.prefs.put(key, value);
      await this.prefs.flush();
    }
  }

  async putBoolean(key: string, value: boolean): Promise<void> {
    if (this.prefs) {
      await this.prefs.put(key, value);
      await this.prefs.flush();
    }
  }

  async getString(key: string, defaultValue: string = ''): Promise<string> {
    if (this.prefs) {
      return (await this.prefs.get(key, defaultValue)) as string;
    }
    return defaultValue;
  }

  async getNumber(key: string, defaultValue: number = 0): Promise<number> {
    if (this.prefs) {
      return (await this.prefs.get(key, defaultValue)) as number;
    }
    return defaultValue;
  }

  async getBoolean(key: string, defaultValue: boolean = false): Promise<boolean> {
    if (this.prefs) {
      return (await this.prefs.get(key, defaultValue)) as boolean;
    }
    return defaultValue;
  }

  async remove(key: string): Promise<void> {
    if (this.prefs) {
      await this.prefs.delete(key);
      await this.prefs.flush();
    }
  }

  async has(key: string): Promise<boolean> {
    if (this.prefs) {
      return await this.prefs.has(key);
    }
    return false;
  }

  async clear(): Promise<void> {
    if (this.prefs) {
      await this.prefs.clear();
      await this.prefs.flush();
    }
  }
}
```

---

## 关系型数据库 RDB 模块

**导入 relationalStore**
`import relationalStore from '@ohos.data.relationalStore'`
```typescript
import relationalStore from '@ohos.data.relationalStore';
```

**通过 ArkData 导入**
`import { relationalStore } from '@kit.ArkData'`
```typescript
import { relationalStore } from '@kit.ArkData';
```

---

## RDB 数据库配置

**StoreConfig 配置**
`relationalStore.StoreConfig`
```typescript
const STORE_CONFIG: relationalStore.StoreConfig = {
  name: 'AppDatabase.db',
  securityLevel: relationalStore.SecurityLevel.S1,
  encrypt: false
};
```

**安全级别枚举**
`relationalStore.SecurityLevel`
```typescript
enum SecurityLevel {
  S1 = 1,
  S2 = 2,
  S3 = 3,
  S4 = 4
}
```

**获取数据库实例**
`relationalStore.getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore>`
```typescript
const store = await relationalStore.getRdbStore(getContext(this), STORE_CONFIG);
```

**删除数据库**
`relationalStore.deleteRdbStore(context: Context, name: string): Promise<void>`
```typescript
await relationalStore.deleteRdbStore(getContext(this), 'AppDatabase.db');
```

---

## RDB SQL 执行

**执行 SQL 语句**
`store.executeSql(sql: string): Promise<void>`
```typescript
await store.executeSql(`CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  email TEXT,
  created_at INTEGER DEFAULT (strftime('%s', 'now'))
)`);
```

**建表示例**
```typescript
const SQL_CREATE_CONTACTS = `CREATE TABLE IF NOT EXISTS contacts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  phone TEXT NOT NULL,
  email TEXT,
  created_at INTEGER DEFAULT (strftime('%s', 'now'))
)`;
await store.executeSql(SQL_CREATE_CONTACTS);
```

---

## RDB 数据操作

**插入数据**
`store.insert(table: string, values: ValuesBucket): Promise<number>`
```typescript
const valueBucket: relationalStore.ValuesBucket = {
  name: '张三',
  phone: '13800138000',
  email: 'zhang@example.com'
};
const rowId = await store.insert('contacts', valueBucket);
```

**批量插入(带事务)**
```typescript
async function batchInsert(items: Array<relationalStore.ValuesBucket>): Promise<void> {
  try {
    store.beginTransaction();
    for (const item of items) {
      await store.insert('contacts', item);
    }
    store.commit();
  } catch (error) {
    store.rollBack();
    throw error;
  }
}
```

**查询数据**
`store.query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>`
```typescript
const predicates = new relationalStore.RdbPredicates('contacts');
predicates.equalTo('name', '张三');
predicates.orderByDesc('id');
const resultSet = await store.query(predicates, ['id', 'name', 'phone', 'email']);
```

**更新数据**
`store.update(values: ValuesBucket, predicates: RdbPredicates): Promise<number>`
```typescript
const valueBucket: relationalStore.ValuesBucket = {
  name: '李四',
  phone: '13900139000'
};
const predicates = new relationalStore.RdbPredicates('contacts');
predicates.equalTo('id', 1);
const rowsAffected = await store.update(valueBucket, predicates);
```

**删除数据**
`store.delete(predicates: RdbPredicates): Promise<number>`
```typescript
const predicates = new relationalStore.RdbPredicates('contacts');
predicates.equalTo('id', 1);
const rowsAffected = await store.delete(predicates);
```

---

## RdbPredicates 条件构造

**等于条件**
`predicates.equalTo(field: string, value: ValueType): RdbPredicates`
```typescript
predicates.equalTo('id', 1);
```

**不等于条件**
`predicates.notEqualTo(field: string, value: ValueType): RdbPredicates`
```typescript
predicates.notEqualTo('status', 'deleted');
```

**大于/小于**
`predicates.greaterThan(field: string, value: ValueType): RdbPredicates`
`predicates.lessThan(field: string, value: ValueType): RdbPredicates`
`predicates.greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates`
`predicates.lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates`
```typescript
predicates.greaterThan('age', 18);
predicates.lessThan('age', 60);
```

**模糊匹配**
`predicates.like(field: string, value: string): RdbPredicates`
```typescript
predicates.like('name', '%张%');
```

**范围条件**
`predicates.between(field: string, low: ValueType, high: ValueType): RdbPredicates`
```typescript
predicates.between('age', 18, 60);
```

**IN 条件**
`predicates.in(field: string, value: Array<ValueType>): RdbPredicates`
```typescript
predicates.in('id', [1, 2, 3, 5, 8]);
```

**排序**
`predicates.orderByAsc(field: string): RdbPredicates`
`predicates.orderByDesc(field: string): RdbPredicates`
```typescript
predicates.orderByDesc('created_at');
```

**分页**
`predicates.limit(count: number, offset: number): RdbPredicates`
```typescript
predicates.limit(10, 0);
predicates.limit(20, 20);
```

**分组**
`predicates.groupBy(fields: Array<string>): RdbPredicates`
```typescript
predicates.groupBy(['category']);
```

---

## ResultSet 结果集 API

**移动到下一行**
`resultSet.goToNextRow(): boolean`
```typescript
while (resultSet.goToNextRow()) {
  // 读取数据
}
```

**移动到第一行**
`resultSet.goToFirstRow(): boolean`
```typescript
resultSet.goToFirstRow();
```

**获取列索引**
`resultSet.getColumnIndex(columnName: string): number`
```typescript
const idIndex = resultSet.getColumnIndex('id');
const nameIndex = resultSet.getColumnIndex('name');
```

**获取字段值**
`resultSet.getLong(columnIndex: number): number`
`resultSet.getString(columnIndex: number): string`
`resultSet.getDouble(columnIndex: number): number`
`resultSet.getBlob(columnIndex: number): Uint8Array`
`resultSet.getBoolean(columnIndex: number): boolean`
```typescript
const id = resultSet.getLong(resultSet.getColumnIndex('id'));
const name = resultSet.getString(resultSet.getColumnIndex('name'));
const age = resultSet.getLong(resultSet.getColumnIndex('age'));
```

**获取列数与行数**
`resultSet.columnCount: number`
`resultSet.rowCount: number`
```typescript
const columns = resultSet.columnCount;
const rows = resultSet.rowCount;
```

**关闭结果集**
`resultSet.close(): void`
```typescript
resultSet.close();
```

---

## RDB 事务

**开启事务**
`store.beginTransaction(): void`
```typescript
store.beginTransaction();
```

**提交事务**
`store.commit(): void`
```typescript
store.commit();
```

**回滚事务**
`store.rollBack(): void`
```typescript
store.rollBack();
```

---

## RDB 加密

**创建加密数据库**
```typescript
const store = await relationalStore.getRdbStore(context, {
  name: 'secure.db',
  securityLevel: relationalStore.SecurityLevel.S3,
  encrypt: true
});
```

---

## 分布式 KV 存储

**导入 distributedKVStore**
`import distributedKVStore from '@ohos.data.distributedKVStore'`
```typescript
import distributedKVStore from '@ohos.data.distributedKVStore';
```

**KVStoreConfig 配置**
```typescript
const KV_CONFIG: distributedKVStore.KVStoreConfig = {
  bundleName: 'com.example.app',
  options: {
    createIfMissing: true,
    encrypt: false,
    backup: false,
    autoSync: true,
    kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
    securityLevel: distributedKVStore.SecurityLevel.S1
  }
};
```

**创建 KVManager**
`distributedKVStore.createKVManager(config: KVStoreConfig): KVManager`
```typescript
const kvManager = distributedKVStore.createKVManager(KV_CONFIG);
```

**获取 KVStore**
`kvManager.getKVStore(storeId: string, options: KVStoreOptions): Promise<KVStore>`
```typescript
const kvStore = await kvManager.getKVStore('distributed_store', KV_CONFIG.options);
```

**写入数据**
`kvStore.put(key: string, value: ValueType): Promise<void>`
```typescript
await kvStore.put('sync_key', 'sync_value');
```

**读取数据**
`kvStore.get(key: string): Promise<ValueType>`
```typescript
const value = await kvStore.get('sync_key');
```

**删除数据**
`kvStore.delete(key: string): Promise<void>`
```typescript
await kvStore.delete('sync_key');
```

**监听数据变更**
`kvStore.on('dataChange', type: SubscribeType, callback: (data: ChangeNotification) => void): void`
```typescript
kvStore.on('dataChange', distributedKVStore.SubscribeType.SUBSCRIBE_TYPE_ALL, (data) => {
  console.info(`数据变更: ${JSON.stringify(data)}`);
});
```

## 延伸阅读
TypeScript 基础（ArkTS 语言底座），见 009-typescript 模块。
声明式 UI 概念与 React/Vue 对比，见 011-react/010-vue3 模块。
移动端应用架构，见 018-harmonyos 模块文档。
