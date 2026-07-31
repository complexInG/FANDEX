# 分布式数据管理 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## KV 数据库

**基本写法：创建 KVManager**
`const <manager> = distributedKVStore.createKVStoreManager(<配置>)`
```typescript
// 创建分布式键值数据库管理器
import { distributedKVStore } from '@kit.ArkData'

let manager = distributedKVStore.createKVStoreManager({
  context: getContext(this),
  bundleName: 'com.example.myapp'
})
```

---

**基本写法：创建 KVStore**
`manager.getKVStore<KVStore>(<storeId>, <options>)`
```typescript
// 创建键值数据库
let options: distributedKVStore.Options = {
  createIfMissing: true,
  encrypt: false,
  backup: false,
  autoSync: true,
  kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
  securityLevel: distributedKVStore.SecurityLevel.S1
}

manager.getKVStore('my_kvstore', options, (err, store) => {
  if (err) { console.error('创建失败'); return }
  let kvStore = store as distributedKVStore.SingleKVStore
})
```

---

**基本写法：写入数据**
`<kvStore>.put(<键>, <值>)`
```typescript
// 写入键值对
kvStore.put('username', 'Alice').then(() => {
  console.info('写入成功')
})
```

---

**基本写法：读取数据**
`<kvStore>.get(<键>)`
```typescript
// 读取指定键的值
kvStore.get('username').then((value) => {
  console.info(`读取: ${value}`)
})
```

---

**基本写法：删除数据**
`<kvStore>.delete(<键>)`
```typescript
// 删除指定键值对
kvStore.delete('username').then(() => {
  console.info('删除成功')
})
```

---

**基本写法：监听数据变化**
`<kvStore>.on('dataChange', <回调>)`
```typescript
// 监听分布式数据同步变化
kvStore.on('dataChange', distributedKVStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, (data) => {
  for (const entry of data.insertEntries) {
    console.info(`新增: ${entry.key} = ${entry.value.value}`)
  }
  for (const entry of data.updateEntries) {
    console.info(`更新: ${entry.key} = ${entry.value.value}`)
  }
  for (const entry of data.deleteEntries) {
    console.info(`删除: ${entry.key}`)
  }
})
```

---

**基本写法：批量写入**
`<kvStore>.putBatch(<entries>)`
```typescript
// 批量写入键值对
let entries: distributedKVStore.Entry[] = [
  { key: 'key1', value: { type: distributedKVStore.ValueType.STRING, value: 'v1' } },
  { key: 'key2', value: { type: distributedKVStore.ValueType.INTEGER, value: 42 } }
]
kvStore.putBatch(entries).then(() => {
  console.info('批量写入成功')
})
```

---

**基本写法：批量读取**
`<kvStore>.getEntries('<前缀>')`
```typescript
// 按前缀查询批量数据
kvStore.getEntries('key').then((entries) => {
  for (const entry of entries) {
    console.info(`${entry.key}: ${entry.value.value}`)
  }
})
```

---

## 关系型数据库（分布式）

**基本写法：创建 RDB**
`const <rdb> = relationalStore.getRdbStore(<context>, <配置>)`
```typescript
// 创建分布式关系型数据库
import { relationalStore } from '@kit.ArkData'

const config: relationalStore.StoreConfig = {
  name: 'my_db.db',
  securityLevel: relationalStore.SecurityLevel.S1
}

relationalStore.getRdbStore(getContext(this), config, (err, store) => {
  let rdbStore = store as relationalStore.RdbStore
})
```

---

**基本写法：创建表**
`const <sql> = 'CREATE TABLE IF NOT EXISTS <表名> (<列定义>)'`
```typescript
// 执行建表 SQL
const SQL = `CREATE TABLE IF NOT EXISTS USER (
  ID INTEGER PRIMARY KEY AUTOINCREMENT,
  NAME TEXT NOT NULL,
  AGE INTEGER
)`
rdbStore.executeSql(SQL)
```

---

**基本写法：插入数据**
`rdbStore.insert('<表名>', <值桶>)`
```typescript
// 插入一行数据
const valueBucket: relationalStore.ValuesBucket = {
  NAME: 'Alice',
  AGE: 25
}
rdbStore.insert('USER', valueBucket, (err, rowId) => {
  console.info(`插入行 ID: ${rowId}`)
})
```

---

**基本写法：查询数据**
`rdbStore.query(<谓词>, <列数组>)`
```typescript
// 使用 RdbPredicates 查询
let predicates = new relationalStore.RdbPredicates('USER')
predicates.greaterThan('AGE', 18)
predicates.orderByAsc('AGE')

let resultSet = await rdbStore.query(predicates, ['ID', 'NAME', 'AGE'])
while (resultSet.goToNextRow()) {
  let id = resultSet.getLong(resultSet.getColumnIndex('ID'))
  let name = resultSet.getString(resultSet.getColumnIndex('NAME'))
  console.info(`${id}: ${name}`)
}
```

---

**基本写法：更新数据**
`rdbStore.update(<值桶>, <谓词>)`
```typescript
// 更新满足条件的数据
let predicates = new relationalStore.RdbPredicates('USER')
predicates.equalTo('NAME', 'Alice')

const valueBucket: relationalStore.ValuesBucket = {
  AGE: 26
}
let rows = await rdbStore.update(valueBucket, predicates)
console.info(`更新 ${rows} 行`)
```

---

**基本写法：删除数据**
`rdbStore.delete(<谓词>)`
```typescript
// 删除满足条件的数据
let predicates = new relationalStore.RdbPredicates('USER')
predicates.equalTo('NAME', 'Alice')
let rows = await rdbStore.delete(predicates)
console.info(`删除 ${rows} 行`)
```

---

**基本写法：设置分布式表**
`rdbStore.setDistributedTables(['<表名>'])`
```typescript
// 将表标记为分布式同步表
await rdbStore.setDistributedTables(['USER'])
```

---

**基本写法：监听分布式数据变化**
`rdbStore.on('dataChange', <类型>, <回调>)`
```typescript
// 监听远程设备数据变更
rdbStore.on('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, (data) => {
  for (const table of data.tables) {
    console.info(`表 ${table.tableName} 数据变更`)
  }
})
```

---

## 用户首选项

**基本写法：获取 Preferences**
`const <prefs> = preferences.getPreferences(<context>, '<名称>')`
```typescript
// 获取轻量级数据存储
import { preferences } from '@kit.ArkData'

let prefs = await preferences.getPreferences(getContext(this), 'my_prefs')
```

---

**基本写法：写入首选项**
`prefs.put('<键>', <值>)`
```typescript
// 写入配置项
await prefs.put('theme', 'dark')
await prefs.put('fontSize', 14)
await prefs.flush()
```

---

**基本写法：读取首选项**
`prefs.get('<键>', <默认值>)`
```typescript
// 读取配置项，不存在时返回默认值
let theme = await prefs.get('theme', 'light')
let fontSize = await prefs.get('fontSize', 12)
console.info(`主题: ${theme}, 字号: ${fontSize}`)
```

---

**基本写法：删除首选项**
`prefs.delete('<键>')`
```typescript
// 删除指定配置项
await prefs.delete('theme')
await prefs.flush()
```

---

**基本写法：检查键是否存在**
`prefs.has('<键>')`
```typescript
// 判断配置项是否存在
let exists = await prefs.has('theme')
if (exists) {
  console.info('存在该配置')
}
```

---

**基本写法：清除所有数据**
`prefs.clear()`
```typescript
// 清空所有首选项
await prefs.clear()
await prefs.flush()
```
