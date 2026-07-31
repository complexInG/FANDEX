# React Fiber 架构原理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Fiber 节点概念

**基本写法：每个组件对应一个 Fiber 节点**
`type <FiberNode> = { type, key, stateNode, child, sibling, return }`
```tsx
// Fiber 树通过链表结构关联
{
  type: 'div',
  child: childFiber,
  sibling: nextFiber,
  return: parentFiber
}
```

---

## 链表结构

**基本写法：child sibling return 三指针**
`<fiber>.child = <子>; <fiber>.sibling = <兄弟>; <fiber>.return = <父>`
```tsx
// 形成可中断遍历的链表
parentFiber.child = firstChild;
firstChild.sibling = secondChild;
firstChild.return = parentFiber;
```

---

## 双缓冲机制

**基本写法：current 树与 workInProgress 树**
`<fiber>.alternate = <对应的另一棵树Fiber>`
```tsx
// 两棵树交替复用节点
const workInProgress = current.alternate;
```

---

## Work Loop 工作循环

**基本写法：performUnitOfWork 逐节点处理**
`function <performUnitOfWork>(<unit>) { <处理>; return <下一个>; }`
```tsx
// 每处理完一个节点检查是否需要让出
while (nextUnitOfWork && !shouldYield()) {
  nextUnitOfWork = performUnitOfWork(nextUnitOfWork);
}
```

---

## 时间切片

**基本写法：使用 MessageChannel 调度**
`shouldYield() = <当前时间> - <开始时间> > <时间片>`
```tsx
// 5ms 左右时间片让出主线程
const DEADLINE = 5;
function shouldYield() { return performance.now() - startTime > DEADLINE; }
```

---

## 优先级调度 Lane 模型

**基本写法：用二进制位表示优先级**
`const <lane> = 1 << <位>`
```tsx
// 不同位代表不同优先级
const SyncLane = 1;          // 同步最高
const InputContinuousLane = 2; // 输入连续
const DefaultLane = 4;       // 默认
```

---

**基本写法：lanes 字段保存待处理优先级**
`<fiber>.lanes = <优先级位图>`
```tsx
// 多个优先级合并存储
fiber.lanes = SyncLane | DefaultLane;
```

---

## Render 阶段

**基本写法：beginWork 处理节点进入**
`function <beginWork>(<fiber>) { return <子fiber> }`
```tsx
// 创建子 Fiber 并标记副作用
function beginWork(fiber) {
  // 比较 props 计算 flags
  return fiber.child;
}
```

---

**基本写法：completeWork 处理节点完成**
`function <completeWork>(<fiber>) { <挂载真实DOM>; }`
```tsx
// 创建 DOM 并挂载属性
function completeWork(fiber) {
  if (fiber.stateNode == null) fiber.stateNode = document.createElement(fiber.type);
}
```

---

## 副作用标记

**基本写法：flags 标记变更类型**
`<fiber>.flags = <Placement> | <Update> | <Deletion>`
```tsx
// 标记插入更新删除
fiber.flags |= Placement;
fiber.flags |= Update;
fiber.flags |= ChildDeletion;
```

---

**基本写法：subtreeFlags 收集子树副作用**
`<fiber>.subtreeFlags |= <child>.flags | <child>.subtreeFlags`
```tsx
// 自下而上汇总
parentFiber.subtreeFlags |= childFiber.flags;
```

---

## Commit 阶段

**基本写法：commitMutation 执行 DOM 操作**
`function <commitMutation>(<fiber>) { <根据flags操作DOM> }`
```tsx
// 提交阶段同步执行
if (flags & Placement) parent.appendChild(stateNode);
if (flags & ChildDeletion) parent.removeChild(child);
```

---

**基本写法：commitLayout 处理生命周期**
`function <commitLayout>(<fiber>) { <调用useLayoutEffect等> }`
```tsx
// 同步执行 layout effect
commitLayout(fiber);
```

---

## 协调 Reconciliation

**基本写法：diff 同层兄弟节点**
`function <reconcileChildren>(<父>, <旧>, <新>) { <diff> }`
```tsx
// 同层比较决定复用或新建
reconcileChildren(parentFiber, currentChildren, nextChildren);
```

---

**基本写法：key 辅助匹配**
`if (<旧>.key === <新>.key) <复用>`
```tsx
// 通过 key 提高复用率
oldFiber.key === newChild.key;
```

---

## 可中断恢复

**基本写法：让出时保存 nextUnitOfWork**
`<nextUnitOfWork> = <当前fiber>`
```tsx
// 恢复时继续处理
let nextUnitOfWork = savedFiber;
```

---

## Lane 调度入口

**基本写法：scheduleUpdateOnFiber 触发更新**
`scheduleUpdateOnFiber(<fiber>, <lane>)`
```tsx
// 标记 lane 后调度
scheduleUpdateOnFiber(fiber, SyncLane);
```

---

## 批处理入口

**基本写法：ensureRootIsOnSchedule 进入调度**
`ensureRootIsOnSchedule(<root>, <lane>)`
```tsx
// 根节点合并 lanes 后调度
ensureRootIsOnSchedule(root, lane);
```

---

## Hook 链表存储

**基本写法：hooks 挂在 Fiber 的 memoizedState**
`<fiber>.memoizedState = <hook链表头>`
```tsx
// 单向链表保存每次 hook 调用
hook.next = nextHook;
fiber.memoizedState = firstHook;
```

---

**基本写法：hook.memoizedState 保存状态**
`<hook>.memoizedState = <状态>`
```tsx
// useState 保存值 useReducer 保存 reducer 返回值
hook.memoizedState = initialState;
```

---

## Update Queue 更新队列

**基本写法：hook 保存 pending 队列**
`<hook>.updateQueue = { pending: <update> }`
```tsx
// 环形链表保存待处理更新
hook.updateQueue.pending = update;
```

---

## Effect 链表

**基本写法：useEffect 通过 updateQueue 关联**
`<hook>.updateQueue.lastEffect = <effect>`
```tsx
// 同组件多个 effect 形成环形链表
hook.updateQueue.lastEffect = effect;
```

---

## Suspense 挂起机制

**基本写法：抛出 Promise 暂停渲染**
`throw <Promise>`
```tsx
// 子组件挂起时由最近 Suspense 接管
throw new Promise(resolve => fetch().then(resolve));
```

---

## 错误处理

**基本写法：捕获子树抛出的错误**
`<fiber>.flags |= <Incomplete>`
```tsx
// 卸载失败子树切换到错误边界
fiber.flags |= Incomplete;
```

---

## DevTools 集成

**基本写法：通过 renderer 接口暴露 Fiber**
`<renderer>.findFiberByHostInstance(<DOM>)`
```tsx
// DevTools 通过协议读取 Fiber
reactDevTools.attach(renderer);
```

---

## Reconciler 包

**基本写法：react-reconciler 暴露可定制接口**
`const <Reconciler> = Reconciler(<hostConfig>)`
```tsx
// 自定义渲染器如 React Three
const Reconciler = require('react-reconciler');
const renderer = Reconciler(hostConfig);
```
