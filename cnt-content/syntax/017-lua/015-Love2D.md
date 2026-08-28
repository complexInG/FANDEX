# Lua Love2D 常用命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 命令行

**基本写法：运行游戏**
`love <目录>`
```bash
// 运行指定目录的 Love2D 游戏
love /path/to/game
```

---

**基本写法：打包 love 文件**
`zip -r game.love .`
```bash
// 把游戏目录打包为 .love 文件
zip -r game.love *.lua assets
```

---

**基本写法：生成可执行文件**
`cat love.exe game.love > game.exe`
```bash
// Windows 下合并为单可执行文件
cat love.exe game.love > game.exe
```

---

**基本写法：查看版本**
`love --version`
```bash
// 输出 Love2D 版本号
love --version
```

---

**基本写法：启用控制台**
`love <目录> --console`
```bash
// Windows 启动时附加控制台窗口
love game --console
```

---

## 项目结构

**基本写法：main.lua 入口**
`function love.load() end`
```lua
-- 游戏启动时调用一次
function love.load()
    love.graphics.setBackgroundColor(0.2, 0.2, 0.2)
end
```

---

**基本写法：主回调**
`function love.<回调>() end`
```lua
-- Love2D 内置主回调
-- love.load()      加载时
-- love.update(dt)  每帧更新
-- love.draw()      每帧绘制
-- love.keypressed(key) 按键
-- love.mousemoved(x,y) 鼠标移动
```

---

## 窗口配置

**基本写法：设置窗口**
`love.window.setMode(<宽>, <高>, <设置>)`
```lua
-- 设置窗口大小与属性
love.window.setMode(800, 600, {
    fullscreen = false,
    resizable = true,
    vsync = true
})
```

---

**基本写法：设置标题**
`love.window.setTitle("<标题>")`
```lua
-- 设置窗口标题
love.window.setTitle("My Game")
```

---

**基本写法：获取尺寸**
`local <w>, <h> = love.graphics.getDimensions()`
```lua
-- 获取窗口客户区尺寸
local w, h = love.graphics.getDimensions()
```

---

## 图形绘制

**基本写法：设置颜色**
`love.graphics.setColor(<r>, <g>, <b> [, <a>])`
```lua
-- 设置后续绘制颜色（0-1）
love.graphics.setColor(1, 0, 0)  -- 红色
```

---

**基本写法：绘制矩形**
`love.graphics.rectangle("<模式>", <x>, <y>, <宽>, <高>)`
```lua
-- mode 为 fill 或 line
love.graphics.rectangle("fill", 100, 100, 80, 60)
```

---

**基本写法：绘制圆形**
`love.graphics.circle("<模式>", <x>, <y>, <半径>)`
```lua
-- 绘制填充圆
love.graphics.circle("fill", 200, 200, 30)
```

---

**基本写法：绘制线段**
`love.graphics.line(<x1>, <y1>, <x2>, <y2>)`
```lua
-- 连接多点的线段
love.graphics.line(0, 0, 100, 100)
```

---

**基本写法：绘制文本**
`love.graphics.print("<文本>", <x> [, <y>])`
```lua
-- 在指定位置绘制文本
love.graphics.print("Score: 0", 10, 10)
```

---

**基本写法：设置字体**
`love.graphics.setFont(<字体>)`
```lua
-- 设置当前字体
local font = love.graphics.newFont(20)
love.graphics.setFont(font)
```

---

**基本写法：清屏**
`love.graphics.clear(<r>, <g>, <b>)`
```lua
-- 用指定颜色清空画布
love.graphics.clear(0, 0, 0)
```

---

## 图像与资源

**基本写法：加载图像**
`local <img> = love.graphics.newImage("<路径>")`
```lua
-- 加载图片资源
local img = love.graphics.newImage("assets/player.png")
```

---

**基本写法：绘制图像**
`love.graphics.draw(<图像>, <x>, <y> [, <旋转>])`
```lua
-- 在指定位置绘制图像
love.graphics.draw(img, 100, 100)
```

---

**基本写法：加载字体**
`local <font> = love.graphics.newFont("<路径>", <大小>)`
```lua
-- 加载 TTF 字体文件
local font = love.graphics.newFont("font.ttf", 24)
```

---

**基本写法：加载音频**
`local <snd> = love.audio.newSource("<路径>", <类型>)`
```lua
-- 加载音效或音乐
local bgm = love.audio.newSource("bgm.ogg", "stream")
local sfx = love.audio.newSource("hit.wav", "static")
```

---

## 输入处理

**基本写法：按键回调**
`function love.keypressed(<键>) end`
```lua
-- 按键按下时触发
function love.keypressed(key)
    if key == "escape" then love.event.quit() end
end
```

---

**基本写法：按键状态查询**
`love.keyboard.isDown(<键>)`
```lua
-- 查询按键是否持续按下
if love.keyboard.isDown("right") then
    player.x = player.x + 200 * dt
end
```

---

**基本写法：鼠标按下**
`function love.mousepressed(<x>, <y>, <按钮>) end`
```lua
-- 鼠标按键按下回调
function love.mousepressed(x, y, button)
    if button == 1 then print("左键点击", x, y) end
end
```

---

**基本写法：查询鼠标位置**
`local <x>, <y> = love.mouse.getPosition()`
```lua
-- 获取当前鼠标坐标
local x, y = love.mouse.getPosition()
```

---

## 更新循环

**基本写法：update 回调**
`function love.update(<dt>) end`
```lua
-- 每帧调用，dt 是距上一帧秒数
function love.update(dt)
    player.x = player.x + speed * dt
end
```

---

**基本写法：基于时间的移动**
`<位置> = <位置> + <速度> * <dt>`
```lua
-- 用 dt 保证不同帧率下速度一致
player.x = player.x + 200 * dt
```

---

**基本写法：定时器**
`local <计时> = 0`
```lua
-- 用 dt 累积实现计时
local timer = 0
function love.update(dt)
    timer = timer + dt
    if timer >= 2 then
        timer = 0
        -- 每 2 秒触发一次
    end
end
```

---

## 绘制回调

**基本写法：draw 回调**
`function love.draw() end`
```lua
-- 每帧绘制内容
function love.draw()
    love.graphics.print("Hello Love2D", 100, 100)
end
```

---

**基本写法：批量绘制**
`love.graphics.rectangle(...)`
```lua
-- 在 draw 中批量调用绘制
function love.draw()
    for _, e in ipairs(enemies) do
        love.graphics.circle("fill", e.x, e.y, e.r)
    end
end
```

---

## 数学与随机

**基本写法：Love2D 随机数**
`love.math.random([<最小> [, <最大>]])`
```lua
-- 使用 Love2D 的随机数（独立于 math.random）
local n = love.math.random(1, 100)
```

---

**基本写法：设置随机种子**
`love.math.setRandomSeed(<种子>)`
```lua
-- 设置随机种子保证可复现
love.math.setRandomSeed(os.time())
```

---

**基本写法：角度与弧度**
`math.rad(<角度>) | math.deg(<弧度>)`
```lua
-- Love2D 三角函数用弧度
local rad = math.rad(90)
local sin = math.sin(rad)
```

---

## 音频播放

**基本写法：播放音效**
`<source>:play()`
```lua
-- 播放音效源
local sfx = love.audio.newSource("hit.wav", "static")
sfx:play()
```

---

**基本写法：循环播放背景音乐**
`<source>:setLooping(true)`
```lua
-- 设置循环播放
local bgm = love.audio.newSource("bgm.ogg", "stream")
bgm:setLooping(true)
bgm:play()
```

---

**基本写法：设置音量**
`<source>:setVolume(<0-1>)`
```lua
-- 设置音量
bgm:setVolume(0.5)
```

---

**基本写法：停止播放**
`<source>:stop()`
```lua
-- 停止播放并回到开头
bgm:stop()
```

---

## 画布与变换

**基本写法：创建画布**
`local <canvas> = love.graphics.newCanvas(<宽>, <高>)`
```lua
-- 离屏渲染画布
local canvas = love.graphics.newCanvas(800, 600)
```

---

**基本写法：渲染到画布**
`love.graphics.setCanvas(<canvas>)`
```lua
-- 切换渲染目标到画布
love.graphics.setCanvas(canvas)
love.graphics.circle("fill", 100, 100, 50)
love.graphics.setCanvas()  -- 恢复主屏
```

---

**基本写法：坐标变换**
`love.graphics.push() | love.graphics.pop()`
```lua
-- 保存与恢复变换状态
love.graphics.push()
love.graphics.translate(100, 100)
love.graphics.rotate(math.rad(45))
love.graphics.draw(img, 0, 0)
love.graphics.pop()
```

---

## 文件系统

**基本写法：读取文件**
`local <内容> = love.filesystem.read("<路径>")`
```lua
-- 在保存目录与源中读取
local content = love.filesystem.read("config.txt")
```

---

**基本写法：写入文件**
`love.filesystem.write("<路径>", <内容>)`
```lua
-- 写入到保存目录
love.filesystem.write("save.txt", "progress=5")
```

---

**基本写法：追加写入**
`love.filesystem.append("<路径>", <内容>)`
```lua
-- 追加内容到文件
love.filesystem.append("log.txt", "new line\n")
```

---

**基本写法：列举目录**
`local <文件表> = love.filesystem.getDirectoryItems("<目录>")`
```lua
-- 列出目录下所有文件
local files = love.filesystem.getDirectoryItems("levels")
for _, f in ipairs(files) do
    print(f)
end
```

---

## 状态管理

**基本写法：游戏状态切换**
`love.event.quit("restart")`
```lua
-- 重启游戏
love.event.quit("restart")
```

---

**基本写法：退出游戏**
`love.event.quit()`
```lua
-- 退出应用
love.event.quit()
```

---

**基本写法：获取帧率**
`love.timer.getFPS()`
```lua
-- 获取当前帧率
local fps = love.timer.getFPS()
love.graphics.print("FPS: " .. fps, 10, 10)
```

---

## 配置 conf.lua

**基本写法：配置窗口与模块**
`function love.conf(<t>) end`
```lua
-- 项目根目录 conf.lua 设置
function love.conf(t)
    t.window.width = 1024
    t.window.height = 768
    t.window.title = "My Game"
    t.modules.joystick = false  -- 禁用未用模块
end
```

---

**基本写法：设置版本兼容**
`t.version = "<版本>"`
```lua
-- 声明目标 Love2D 版本
function love.conf(t)
    t.version = "11.5"
end
```
