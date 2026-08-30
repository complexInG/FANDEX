## 0. 你现在在哪里（先读这里）

> 学习目标：对照进阶路线，明确接下来三站要学什么、为什么按这个顺序学、每站学到什么程度算过关。

前五篇文档带你完成了 Angular 的入门闭环：认识框架与工具链（001）、
组件与模板（002）、Signals 信号体系（003）、依赖注入与服务（004）、
路由与表单（005）。到这里，你已经能搭出一个多页面、有表单、有服务层的
Angular 应用骨架。

本篇是通往精通阶段的路线图：把剩余的核心能力拆成三站。每一站给出
"要解决的问题 → 核心 API 清单 → 最小示例 → 常见陷阱 → 过关自检"，
后续版本会把每一站展开为独立文档（编号紧接本篇）。

## 1. 进阶路线总览

| 站点 | 主题 | 解决的问题 | 核心能力 |
| --- | --- | --- | --- |
| 第六站 | 指令与管道 | 模板怎么复用：行为复用与数据格式化 | 属性/结构指令、@if/@for、自定义管道 |
| 第七站 | HttpClient 与状态管理 | 数据怎么流：接口调用与信号化状态 | 拦截器、resource、computed、toSignal |
| 第八站 | 测试与 SSR 水合 | 质量与首屏：自动化测试与服务端渲染 | TestBed、@angular/ssr、水合 |

三站的关系：第六站解决"模板层的复用"，第七站解决"数据层的组织"，
第八站解决"交付质量"。顺序不可跳：指令与管道是模板写法的基础，
状态管理依赖信号（003 已学），SSR 则建立在完整应用之上。

## 2. 第六站：指令与管道

Angular 的模板复用分两条路：指令复用"行为"，管道复用"格式化"。

### 2.1 指令三分法

| 类型 | 装饰器 | 作用 | 例 |
| --- | --- | --- | --- |
| 组件 | @Component | 带模板的指令 | 页面、卡片 |
| 属性指令 | @Directive | 改变元素外观或行为 | 高亮、tooltip |
| 结构指令 | @Directive | 增删 DOM 改变布局 | *ngIf 的替代者 |

### 2.2 属性指令最小示例

```ts
@Directive({ selector: "[appHighlight]" })
export class HighlightDirective {
  // host 绑定：把宿主元素的颜色绑定到信号
  color = signal("transparent");
  host = { "[style.backgroundColor]": "color()" };

  constructor(private el: ElementRef) {}
  @HostListener("mouseenter") enter() { this.color.set("#39C5BB"); }
  @HostListener("mouseleave") leave() { this.color.set("transparent"); }
}
```

```html
<p appHighlight>鼠标移过来试试</p>
```

### 2.3 结构指令的原理

```ts
@Directive({ selector: "[appUnless]" })
export class UnlessDirective {
  private tpl = inject(TemplateRef);
  private vcr = inject(ViewContainerRef);

  @Input() set appUnless(cond: boolean) {
    if (!cond) this.vcr.createEmbeddedView(this.tpl);   // 条件成立才渲染
    else this.vcr.clear();
  }
}
```

**讲解：** 结构指令的本质是"拿到模板 + 手动决定挂不挂"——
理解了 TemplateRef/ViewContainerRef，`@if` 的新控制流语法就不再神秘。

### 2.4 新控制流与管道

- 控制流：`@if (cond) {...} @for (item of list; track item.id) {...}` 已是
  Angular 17+ 的推荐写法，`track` 决定列表 diff 的效率（对照 *ngIf/*ngFor 迁移）。
- 管道：内置 date/currency/number/json 等速查；自定义管道实现
  `transform()`；默认纯管道（输入引用不变则不重算），非纯管道要慎用。

### 2.5 常见陷阱

- @for 忘写 track 或用 index 当 track：列表更新错乱或性能差。
- 在模板里调用方法做过滤排序（每次变更检测都执行），应改用 computed 或管道。
- 非纯管道里做重计算，拖垮整个变更检测。

### 2.6 过关自检

1. 能写一个属性指令和一个结构指令。
2. 新控制流 @if/@for 的 track 规则能说清楚。
3. 能解释"管道 vs 方法调用 vs computed"的性能取舍。

## 3. 第七站：HttpClient 与状态管理

这一站把"接口数据"变成"界面状态"，全程信号化。

### 3.1 拦截器：统一关注点

```ts
// 认证拦截器：函数式写法，自动附加 token
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const token = inject(AuthService).token();
  const authReq = token
    ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })
    : req;
  return next(authReq);
};

// app.config.ts
provideHttpClient(withInterceptors([authInterceptor]))
```

### 3.2 resource：把请求变成三态信号

```ts
@Component({ /* ... */ })
export class UserList {
  private http = inject(HttpClient);
  keyword = signal("");

  users = resource({
    request: this.keyword,                       // 信号变化自动重新请求
    loader: ({ request }) =>
      this.http.get<User[]>(`/api/users?q=${request}`),
  });

  // 模板里用 users.value() / users.isLoading() / users.error()
}
```

**讲解：** resource 把 loading/value/error 三态装进一个信号资源，
配合 computed 派生筛选视图，组件不再手写"请求 → 存结果 → 翻状态"的样板。

### 3.3 服务化状态与 RxJS 桥接

- 领域状态收进 service：`signal` 存数据、`computed` 派生视图模型、
  方法内做变更，组件只读不写。
- 既有 RxJS 代码用 `toSignal()` 接入信号世界，反向用 `toObservable()`；
  两者并存期注意订阅生命周期。

### 3.4 常见陷阱

- 拦截器里做重业务逻辑（它只该管横切关注点）。
- effect 里再改被它依赖的信号，造成循环触发。
- toSignal 在非注入上下文调用报错（要传 injectionContext 或在构造器里）。

### 3.5 过关自检

1. 会写函数式拦截器处理 token 与 401。
2. 会用 resource/rxResource 表达"请求即状态"。
3. 能把一个"满地手写状态同步"的组件重构成 signal + computed。

## 4. 第八站：测试与 SSR 水合

交付质量的两大支柱。

### 4.1 组件测试骨架

```ts
describe("CounterComponent", () => {
  it("点击加一", async () => {
    await TestBed.compileComponents();          // 准备
    const fixture = TestBed.createComponent(Counter);
    fixture.componentInstance.count.set(1);     // 执行
    await fixture.whenStable();
    expect(fixture.componentInstance.count()).toBe(2);   // 断言
  });
});
```

服务测试用 `provideHttpClientTesting` 把后端换成 mock，专测服务逻辑。

### 4.2 SSR 与水合

```bash
ng add @angular/ssr        # 一条命令接入服务端渲染
```

```ts
// app.config.ts —— 客户端水合：接管服务端 HTML 而非重绘
provideClientHydration(),
```

**讲解：** SSR 让首屏由服务端直出 HTML（快 + 利于 SEO），
水合让客户端"接上"这份 HTML 继续交互。水合错误的根源是
"服务端与客户端渲染出不同结果"——渲染路径里别直接碰 window/localStorage，
需要浏览器的逻辑放 afterNextRender。

### 4.3 常见陷阱

- 测试里没有 await fixture.whenStable 就断言，时序失败。
- SSR 下使用 window/document 直接访问导致服务器报错。
- 服务端与客户端渲染不一致（如依赖 Date.now 的随机内容），水合告警。

### 4.4 过关自检

1. 能为核心组件写 AAA 结构的测试并接入 CI。
2. 能解释 SSR 渲染流程与水合的关系。
3. 知道三类水合错误的典型成因与规避手段。

## 5. 学习建议

1. 顺序学，不跳站：第六站的模板 idioms 会在第七、八站反复出现。
2. 每站一个产出：给现有应用加"权限高亮"指令、把列表页改造成 resource + computed、
   为核心组件写测试并开启 SSR。
3. 版本跟进：Angular 半年一个大版本，升级走官方 update guide；
   zoneless 持续推进，新项目留意实验选项。

## 小结与延伸

- 进阶三站：模板复用 → 数据与状态 → 质量与首屏，对应从"会搭"到"能交付"的跨越。
- 每一站的展开文档将陆续补充在本模块中，编号紧接本篇（007 起）。
- 官方资源：angular.dev（新文档站）、angular.dev/guide/signals、
  angular.dev/guide/ssr。
