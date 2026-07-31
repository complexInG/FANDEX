# React 国际化 i18n

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## react-i18next 安装

**基本写法：安装 i18next 与 react-i18next**
`npm install i18next react-i18next`
```bash
# 安装国际化核心库
npm install i18next react-i18next
```

---

## 初始化配置

**基本写法：i18n 配置资源与语言**
`i18n.use(<adapter>).init({ resources, lng })`
```ts
// 初始化语言包与默认语言
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
i18n.use(initReactI18next).init({
  resources: {
    en: { translation: { hello: 'Hello' } },
    zh: { translation: { hello: '你好' } }
  },
  lng: 'zh',
  fallbackLng: 'en'
});
```

---

## 翻译资源结构

**基本写法：嵌套命名空间组织文案**
`{ <语言>: { <命名空间>: { <键>: <值> } } }`
```ts
// 按模块拆分文案
{
  en: {
    translation: {
      user: { login: 'Login', logout: 'Logout' }
    }
  }
}
```

---

## useTranslation Hook

**基本写法：组件内使用翻译**
`const { t } = useTranslation([<命名空间>])`
```tsx
// 获取翻译函数
const { t } = useTranslation();
return <h1>{t('hello')}</h1>;
```

---

**基本写法：指定命名空间**
`useTranslation('<命名空间>')`
```tsx
// 仅加载 user 命名空间
const { t } = useTranslation('user');
return <button>{t('login')}</button>;
```

---

## 变量插值

**基本写法：使用占位符插入变量**
`t('<键>', { <变量>: <值> })`
```tsx
// 文案中插入变量
t('welcome', { name: 'Alice' });
// 资源：welcome: '欢迎 {{name}}'
```

---

## 复数处理

**基本写法：根据数量选择文案**
`t('<键>', { count: <数量> })`
```tsx
// 自动选择单复数
t('items', { count: 5 });
// 资源：items_one: '1 item', items_other: '{{count}} items'
```

---

## 日期数字格式化

**基本写法：使用 Intl API 格式化**
`new Intl.DateTimeFormat(<语言>).format(<日期>)`
```tsx
// 按语言格式化日期
new Intl.DateTimeFormat('zh-CN').format(new Date());
```

---

**基本写法：数字格式化**
`new Intl.NumberFormat(<语言>).format(<数字>)`
```tsx
// 货币与千分位
new Intl.NumberFormat('zh-CN', { style: 'currency', currency: 'CNY' }).format(1234);
```

---

## 语言切换

**基本写法：动态切换语言**
`i18n.changeLanguage(<语言码>)`
```tsx
// 切换到英文
i18n.changeLanguage('en');
```

---

**基本写法：当前语言**
`i18n.language`
```tsx
// 读取当前语言
const current = i18n.language;
```

---

## 持久化语言选择

**基本写法：保存到 localStorage**
`localStorage.setItem('<键>', <语言>)`
```tsx
// 启动时读取并应用
const saved = localStorage.getItem('lang') || 'zh';
i18n.changeLanguage(saved);
```

---

**基本写法：语言检测插件**
`npm install i18next-browser-languagedetector`
```bash
# 自动检测浏览器语言
npm install i18next-browser-languagedetector
```

---

**基本写法：使用检测器**
`i18n.use(<LanguageDetector>)`
```ts
// 配置检测顺序与缓存
i18n.use(LanguageDetector).init({
  detection: { order: ['localStorage', 'navigator'], caches: ['localStorage'] }
});
```

---

## Trans 组件富文本

**基本写法：嵌入组件的翻译**
`<Trans i18nKey="<键>" <组件>={<元素>}>`
```tsx
// 文案中嵌入链接组件
<Trans i18nKey="terms" components={{ link: <a href="/t" /> }} />
// 资源：terms: '请阅读 <link>条款</link>'
```

---

## 延迟加载语言包

**基本写法：动态导入语言资源**
`i18n.loadLanguages(<语言>, <回调>)`
```tsx
// 切换时按需加载
import(`./locales/${lang}.json`).then(res => {
  i18n.addResourceBundle(lang, 'translation', res.default);
  i18n.changeLanguage(lang);
});
```

---

## 后端资源加载

**基本写法：使用 i18next-http-backend**
`npm install i18next-http-backend`
```bash
# 从服务端加载语言包
npm install i18next-http-backend
```

---

**基本写法：配置后端加载**
`i18n.use(<HttpBackend>).init({ backend: { loadPath } })`
```ts
// 配置资源加载路径
i18n.use(HttpBackend).init({
  backend: { loadPath: '/locales/{{lng}}/{{ns}}.json' }
});
```

---

## 复数与序数

**基本写法：序数词处理**
`t('<键>_ordinal', { count, ordinal: <函数> })`
```tsx
// 第 1 第 2 第 3
t('place_ordinal', { count: 2 });
```

---

## 上下文 Context

**基本写法：根据上下文选择文案**
`t('<键>', { context: '<上下文>' })`
```tsx
// 男版女版文案
t('greet', { context: 'male' });
// 资源：greet_male: '先生你好', greet_female: '女士你好'
```

---

## 命名空间拆分

**基本写法：按页面拆分命名空间**
`{ ns: ['<命名空间1>', '<命名空间2>'] }`
```ts
// 减少首屏加载量
{
  en: {
    common: { ok: 'OK' },
    home: { title: 'Home' }
  }
}
```

---

**基本写法：默认命名空间**
`defaultNS: '<命名空间>'`
```ts
// 配置默认命名空间
i18n.init({ defaultNS: 'common' });
```

---

## SSR 国际化

**基本写法：每请求独立 i18n 实例**
`const <instance> = i18n.createInstance()`
```tsx
// 避免请求间语言串扰
const instance = i18n.createInstance();
await instance.init({ lng: req.language, resources });
```

---

## ICU MessageFormat

**基本写法：复杂消息格式**
`npm install @formatjs/intl`
```bash
# 处理复数与选择
npm install @formatjs/intl
```

---

**基本写法：使用 intl 格式化**
`new Intl.MessageFormat(<消息>, <语言>).format(<参数>)`
```tsx
// 复杂复数选择
const msg = `{count, plural, =0 {无} one {# 项} other {# 项}}`;
```

---

## 排序与比较

**基本写法：本地化字符串排序**
`new Intl.Collator(<语言>).compare`
```tsx
// 中文拼音排序
['张三', '李四'].sort(new Intl.Collator('zh-Hans-CN').compare);
```

---

## 单复数默认规则

**基本写法：英文复数后缀**
`<键>_one / <键>_other`
```ts
// 自动判断单复数
{
  item_one: 'item',
  item_other: 'items'
}
```

---

## 测试与回退

**基本写法：缺失键回退语言**
`fallbackLng: '<语言>'`
```ts
// 当前语言缺失时回退
i18n.init({ fallbackLng: 'en' });
```

---

**基本写法：缺失键警告**
`saveMissing: true`
```ts
// 开发期收集缺失翻译
i18n.init({ saveMissing: true, missingKeyHandler: (lng, ns, key) => console.warn(key) });
```
