# React Router 路由进阶

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Router 配置

**基本写法：BrowserRouter 声明路由根**
`<BrowserRouter> <Routes>...</Routes> </BrowserRouter>`
```tsx
// 顶层路由容器
<BrowserRouter>
  <Routes>
    <Route path="/" element={<Home />} />
  </Routes>
</BrowserRouter>
```

---

**基本写法：HashRouter 用于静态托管**
`<HashRouter> <App /> </HashRouter>`
```tsx
// 无需服务器配置的场景
<HashRouter><App /></HashRouter>
```

---

## 嵌套路由

**基本写法：Route 嵌套配合 Outlet**
`<Route path="<父>" element={<父组件>}> <Route path="<子>" element={<子组件>} /> </Route>`
```tsx
// 父组件渲染子组件出口
<Route path="/user" element={<UserLayout />}>
  <Route path="profile" element={<Profile />} />
</Route>
```

---

**基本写法：Outlet 占位子路由**
`<Outlet />`
```tsx
// 父组件中渲染匹配的子路由
function UserLayout() {
  return <div><h1>用户中心</h1><Outlet /></div>;
}
```

---

## 动态路由参数

**基本写法：路径以冒号声明参数**
`<Route path="/user/:id" element={<User />} />`
```tsx
// 路径 /user/42 中 id 为 42
<Route path="/user/:id" element={<User />} />
```

---

**基本写法：useParams 读取参数**
`const { <参数> } = useParams()`
```tsx
// 获取动态路由参数
const { id } = useParams();
```

---

**基本写法：可选参数**
`<Route path="/post/:id?" element={<Post />} />`
```tsx
// id 可有可无
<Route path="/post/:id?" element={<Post />} />
```

---

## 路径匹配

**基本写法：useLocation 获取当前路径**
`const <loc> = useLocation()`
```tsx
// 读取 pathname 与 search
const loc = useLocation();
console.log(loc.pathname);
```

---

**基本写法：useMatch 匹配路径**
`const <match> = useMatch(<路径模式>)`
```tsx
// 检测当前是否匹配
const match = useMatch('/user/:id');
```

---

## 声明式导航

**基本写法：Link 导航**
`<Link to="<路径>">文本</Link>`
```tsx
// 普通跳转
<Link to="/about">关于</Link>
```

---

**基本写法：NavLink 高亮当前**
`<NavLink to="<路径>" className={<判断函数>}>`
```tsx
// 激活时添加类名
<NavLink to="/home" className={({ isActive }) => isActive ? 'on' : ''}>首页</NavLink>
```

---

**基本写法：Link 携带 state**
`<Link to="<路径>" state={<状态对象>}>`
```tsx
// 传递隐藏状态
<Link to="/detail" state={{ from: 'list' }}>详情</Link>
```

---

## 编程式导航

**基本写法：useNavigate 编程跳转**
`const <navigate> = useNavigate(); <navigate>("<路径>")`
```tsx
// 登录成功后跳转
const navigate = useNavigate();
navigate('/dashboard');
```

---

**基本写法：前进后退**
`<navigate>(-1); <navigate>(1)`
```tsx
// 返回上一页
navigate(-1);
```

---

**基本写法：替换历史记录**
`<navigate>("<路径>", { replace: true })`
```tsx
// 重定向不留历史
navigate('/login', { replace: true });
```

---

**基本写法：携带 state 跳转**
`<navigate>("<路径>", { state: <状态> })`
```tsx
// 传递状态
navigate('/step2', { state: { form: data } });
```

---

## 查询参数处理

**基本写法：useSearchParams 读写查询串**
`const [<params>, <setParams>] = useSearchParams()`
```tsx
// 读取与修改 ?q=react
const [params, setParams] = useSearchParams();
const q = params.get('q');
setParams({ q: 'vue' });
```

---

## 路由守卫

**基本写法：RequireAuth 包裹受保护路由**
`<Route element={<RequireAuth />}> <Route path="<受保护>" element={<组件>} /> </Route>`
```tsx
// 未登录跳转登录页
function RequireAuth() {
  const { user } = useAuth();
  if (!user) return <Navigate to="/login" replace />;
  return <Outlet />;
}
```

---

**基本写法：Navigate 重定向**
`<Navigate to="<路径>" replace />`
```tsx
// 条件重定向
{!isAuth ? <Navigate to="/login" /> : <Dashboard />}
```

---

## 加载器 Loader

**基本写法：路由级数据预取**
`<Route loader={<异步函数>} />`
```tsx
// 进入路由前获取数据
<Route path="/user/:id" element={<User />}
  loader={async ({ params }) => fetchUser(params.id)} />
```

---

**基本写法：useLoaderData 读取数据**
`const <数据> = useLoaderData()`
```tsx
// 在组件中使用 loader 数据
const user = useLoaderData();
```

---

## Action 表单提交

**基本写法：路由 action 处理表单**
`<Route action={<处理函数>} />`
```tsx
// 提交表单触发 action
<Route path="/login" element={<Login />}
  action={async ({ request }) => submitLogin(await request.formData())} />
```

---

**基本写法：useActionData 读取结果**
`const <数据> = useActionData()`
```tsx
// 获取 action 返回的错误信息
const errors = useActionData();
```

---

## 错误边界

**基本写法：errorElement 处理路由错误**
`<Route errorElement={<错误组件>}>`
```tsx
// 路由抛错时显示
<Route errorElement={<RouteError />}>
  <Route path="/user" element={<User />} />
</Route>
```

---

## 布局路由

**基本写法：无 path 的布局 Route**
`<Route element={<布局>}> <Route path="<子>" /> </Route>`
```tsx
// 共享布局不参与路径匹配
<Route element={<DashboardLayout />}>
  <Route path="stats" element={<Stats />} />
</Route>
```

---

## 索引路由

**基本写法：index 路由匹配父路径**
`<Route index element={<组件>} />`
```tsx
// 父路径默认显示
<Route path="/user" element={<UserLayout />}>
  <Route index element={<UserHome />} />
</Route>
```

---

## 通配路由

**基本写法：兜底 404**
`<Route path="*" element={<NotFound />} />`
```tsx
// 匹配所有未定义路径
<Route path="*" element={<NotFound />} />
```

---

**基本写法：splat 捕获剩余路径**
`<Route path="/files/*" element={<Files />} />`
```tsx
// useSearchParams 读取 splat
const splat = useParams()['*'];
```

---

## 懒加载路由

**基本写法：配合 lazy 与 Suspense**
`const <组件> = lazy(() => import(<路径>))`
```tsx
// 路由按需加载
const Admin = lazy(() => import('./Admin'));
<Suspense fallback={<Spinner />}><Admin /></Suspense>
```

---

## 滚动恢复

**基本写法：路由切换滚动到顶部**
`useEffect(() => window.scrollTo(0, 0), [<loc>.pathname])`
```tsx
// 切换页面重置滚动
const loc = useLocation();
useEffect(() => window.scrollTo(0, 0), [loc.pathname]);
```

---

## createBrowserRouter 数据路由

**基本写法：创建数据路由器**
`const <router> = createBrowserRouter([<路由对象>])`
```tsx
// 推荐 v6.4+ 方式
const router = createBrowserRouter([
  { path: '/', element: <Home />, loader: homeLoader },
]);
```

---

**基本写法：RouterProvider 注入**
`<RouterProvider router={<router>} />`
```tsx
// 渲染数据路由
<RouterProvider router={router} />
```

---

## 嵌套数据路由

**基本写法：children 配置嵌套**
`{ path: '<父>', element: <父>, children: [{ path: '<子>', element: <子> }] }`
```tsx
// 对象式嵌套
{
  path: '/user',
  element: <UserLayout />,
  children: [{ path: 'profile', element: <Profile /> }]
}
```

---

## useRoutes 配置式路由

**基本写法：使用对象配置路由**
`const <元素> = useRoutes([<路由对象>])`
```tsx
// 根据配置渲染
const element = useRoutes([
  { path: '/', element: <Home /> },
  { path: '/about', element: <About /> }
]);
return element;
```

---

## 路由过渡

**基本写法：useNavigation 获取导航状态**
`const <nav> = useNavigation()`
```tsx
// 显示提交中状态
const nav = useNavigation();
{nav.state === 'loading' && <Spinner />}
```
