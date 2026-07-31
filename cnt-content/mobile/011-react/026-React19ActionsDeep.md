# React 19 Actions 与表单深入

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Actions 概念

**基本写法：startTransition 内的异步函数即 Action**
`startTransition(async () => <异步>)`
```tsx
// 自动管理 pending 错误乐观更新
const [isPending, startTransition] = useTransition();
startTransition(async () => await submit(data));
```

---

## useActionState

**基本写法：用 Action 管理 form 状态**
`const [<state>, <dispatch>, <isPending>] = useActionState(<action>, <初值>, [<permalink>])`
```tsx
// 表单提交状态一体化
const [error, submitAction, isPending] = useActionState(
  async (prev, formData) => await save(formData.get('name')),
  null
);
```

---

**基本写法：action 函数签名**
`async (<previousState>, <payload>) => <newState>`
```tsx
// 接收上次状态与提交数据
async function reducer(prev, formData) {
  const err = await save(formData.get('name'));
  return err;
}
```

---

**基本写法：permalink 支持渐进增强**
`useActionState(<action>, <初值>, <永久链接>)`
```tsx
// JS 未加载时跳转到该 URL
useActionState(action, null, '/profile');
```

---

## 表单 action 属性

**基本写法：form 直接接收 Action 函数**
`<form action={<action函数>}>`
```tsx
// 提交自动调用 action 并重置表单
<form action={submitAction}>
  <input name="email" />
  <button type="submit">提交</button>
</form>
```

---

**基本写法：button formAction 覆盖**
`<button formAction={<另一个action>}>`
```tsx
// 同表单多个提交按钮
<form action={save}>
  <button formAction={publish}>发布</button>
</form>
```

---

## useFormStatus

**基本写法：子组件读取父表单状态**
`const { pending, data, method, action } = useFormStatus()`
```tsx
// 按钮感知提交中状态
import { useFormStatus } from 'react-dom';
function Submit() {
  const { pending } = useFormStatus();
  return <button disabled={pending}>{pending ? '提交中' : '提交'}</button>;
}
```

---

**基本写法：读取提交的 FormData**
`const { data } = useFormStatus()`
```tsx
// 显示正在提交的字段
const { data } = useFormStatus();
return <span>{data.get('name')}</span>;
```

---

## useOptimistic 乐观更新

**基本写法：提交期间展示乐观值**
`const [<optimistic>, <add>] = useOptimistic(<state>, <updateFn>)`
```tsx
// 立即显示新消息请求成功后保留
const [messages, addOptimistic] = useOptimistic(messages, (state, newMsg) => [
  ...state, { ...newMsg, pending: true }
]);
```

---

**基本写法：在 Action 内调用 add**
`await <add>(<乐观值>); await <真实请求>`
```tsx
// 先乐观展示再确认
async function sendAction(formData) {
  addOptimistic({ id: 'temp', text: formData.get('text') });
  await api.send(formData);
}
```

---

## 表单组件组合

**基本写法：useActionState 配合 form action**
`<form action={<dispatch>}>`
```tsx
// useActionState 返回的 dispatch 作为 form action
const [state, dispatch, pending] = useActionState(action, null);
<form action={dispatch}><input name="q" /></form>
```

---

**基本写法：useFormStatus 用于按钮**
`function <Button>() { const { pending } = useFormStatus(); }`
```tsx
// 子组件无需传递 pending prop
function SubmitButton() {
  const { pending } = useFormStatus();
  return <button disabled={pending}>保存</button>;
}
```

---

## 传统表单处理对比

**基本写法：手动管理 pending 与错误**
`const [<pending>, <setPending>] = useState(false)`
```tsx
// 旧写法繁琐
const [pending, setPending] = useState(false);
const [error, setError] = useState(null);
const onSubmit = async () => {
  setPending(true);
  const err = await save();
  setPending(false);
  if (err) setError(err);
};
```

---

## Action 错误处理

**基本写法：Action 内抛错由错误边界捕获**
`throw new Error(<消息>)`
```tsx
// 失败自动回滚乐观更新
async function action() {
  if (failed) throw new Error('提交失败');
}
```

---

## 多个 Action 类型

**基本写法：根据 payload 分支处理**
`async (<state>, <payload>) => { switch (<payload>.type) { } }`
```tsx
// 类似 reducer 风格
async function reducer(state, payload) {
  switch (payload.type) {
    case 'SAVE': return await save(payload.data);
    case 'DELETE': return await del(payload.id);
  }
}
```

---

## 取消排队 Action

**基本写法：通过返回值控制队列**
`return <newState>`
```tsx
// 后续排队 action 会接收最新 state
return { ok: true };
```

---

## 表单重置

**基本写法：form action 成功后自动重置**
`<form action={<action>}>`
```tsx
// 提交完成后清空输入
<form action={submit}>
  <input name="text" />
</form>
```

---

## useFormState 兼容旧名

**基本写法：React 19 重命名为 useActionState**
`const [<state>, <action>] = useFormState(<fn>, <初值>)`
```tsx
// 兼容旧 API 不推荐使用
import { useFormState } from 'react-dom';
```

---

## 配合 Server Action

**基本写法：Server Action 作为 form action**
`'use server' async function <action>(<formData>) {}`
```tsx
// 服务端执行 Action
async function submitAction(formData) {
  'use server';
  await db.insert(formData.get('name'));
}
```

---

## 表单校验

**基本写法：Action 内做服务端校验**
`if (!<合法>) return { <错误字段>: <消息> }`
```tsx
// 返回错误信息给 useActionState
async function action(prev, formData) {
  if (!formData.get('email')) return { error: '邮箱必填' };
  await save(formData);
  return { ok: true };
}
```

---

## 配合 useOptimistic 与错误边界

**基本写法：失败自动回滚乐观值**
`useOptimistic(<state>, <updateFn>)`
```tsx
// Action 抛错时 useOptimistic 自动回滚
const [items, addOptimistic] = useOptimistic(items, (s, n) => [...s, n]);
```

---

## 渐进增强

**基本写法：JS 未加载时表单仍可提交**
`<form action={<serverAction>} >`
```tsx
// 服务端 Action 支持无 JS 提交
<form action={serverAction}>
  <input name="q" />
</form>
```

---

## 表单状态展示

**基本写法：根据 useActionState 返回值渲染**
`{<state>?.<error> && <错误提示>}`
```tsx
// 显示错误或成功状态
const [state] = useActionState(action, null);
{state?.error && <p className="error">{state.error}</p>}
```

---

## 复用 Action 逻辑

**基本写法：自定义 Hook 封装 Action**
`function use<名称>() { const [...] = useActionState(<action>, <初值>); return { ... }; }`
```tsx
// 提取通用提交逻辑
function useSaveForm() {
  const [state, dispatch, pending] = useActionState(saveAction, null);
  return { state, dispatch, pending };
}
```

---

## Action 与 transition 关系

**基本写法：Action 内部走 transition**
`startTransition(async () => <异步>)`
```tsx
// 因此 isPending 与 useTransition 一致
const [isPending] = useTransition();
```

---

## 表单提交禁用按钮

**基本写法：useFormStatus 控制 disabled**
`<button disabled={<pending>}>`
```tsx
// 防止重复提交
const { pending } = useFormStatus();
<button disabled={pending}>提交</button>
```
