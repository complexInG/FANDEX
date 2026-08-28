# Lua Neovim 配置

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 配置基础

**基本写法：init.lua 入口**
`~/.config/nvim/init.lua`
```lua
-- Neovim Lua 配置入口
-- 标准初始化
vim.g.mapleader = " "
vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
```

---

**基本写法：vim.opt 选项设置**
`vim.opt.<选项> = <值>`
```lua
-- 设置 Neovim 选项
vim.opt.ignorecase = true       -- 忽略大小写
vim.opt.smartcase = true        -- 智能大小写
vim.opt.wrap = false            -- 不自动换行
vim.opt.scrolloff = 8           -- 光标保留 8 行
vim.opt.termguicolors = true    -- 24 位颜色
vim.opt.splitright = true       -- 垂直分割在右侧
vim.opt.splitbelow = true       -- 水平分割在下方
```

---

## vim 全局对象

**基本写法：vim.g 全局变量**
`vim.g.<变量> = <值>`
```lua
-- 设置 vim 全局变量
vim.g.mapleader = " "
vim.g.loaded_netrw = 1           -- 禁用 netrw
vim.g.netrw_banner = 0
-- 访问
print(vim.g.mapleader)
```

---

**基本写法：vim.b 缓冲区变量**
`vim.b[<缓冲区>].<变量>`
```lua
-- 缓冲区局部变量
vim.b.current_project = "myapp"
print(vim.b.current_project)
-- 当前缓冲区
vim.b[0].custom = true
```

---

**基本写法：vim.w 窗口变量**
`vim.w.<变量>`
```lua
-- 窗口局部变量
vim.w.is_focused = true
```

---

## 键映射

**基本写法：vim.keymap.set**
`vim.keymap.set(<模式>, <键>, <动作>, <选项>)`
```lua
-- 设置键映射
vim.keymap.set("n", "<leader>w", ":w<CR>", { desc = "保存" })
vim.keymap.set("n", "<leader>q", ":q<CR>", { desc = "退出" })
vim.keymap.set("i", "jk", "<ESC>", { desc = "返回普通模式" })
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv", { desc = "移动选中行下" })
-- 模式：n 普通 i 插入 v 可视 c 命令 t 终端
```

---

**基本写法：映射选项**
`{ buffer = <bufnr>, silent = true, ... }`
```lua
-- 映射选项
vim.keymap.set("n", "<leader>f", function()
    vim.lsp.buf.format()
end, {
    desc = "格式化",
    buffer = true,       -- 仅当前缓冲区
    silent = true,       -- 静默
    noremap = true,      -- 非递归
    expr = false,        -- 非表达式
})
```

---

## 命令与自动命令

**基本写法：vim.api.nvim_create_user_command**
`vim.api.nvim_create_user_command(<名>, <回调>, <选项>)`
```lua
-- 创建用户命令
vim.api.nvim_create_user_command("Hello", function(opts)
    print("Hello, " .. opts.args)
end, { nargs = "*", desc = "打招呼" })
-- :Hello world
```

---

**基本写法：自动命令组**
`vim.api.nvim_create_augroup(<名>, <选项>)`
```lua
-- 创建自动命令组
local group = vim.api.nvim_create_augroup("MyConfig", { clear = true })
vim.api.nvim_create_autocmd("TextYankPost", {
    group = group,
    callback = function()
        vim.highlight.on_yank()
    end,
})
vim.api.nvim_create_autocmd("BufWritePre", {
    group = group,
    pattern = "*.lua",
    callback = function()
        vim.lsp.buf.format()
    end,
})
```

---

## 插件管理

**基本写法：lazy.nvim**
`require("lazy").setup(<插件列表>)`
```lua
-- lazy.nvim 插件管理器
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
vim.opt.rtp:prepend(lazypath)
require("lazy").setup({
    { "nvim-treesitter/nvim-treesitter", build = ":TSUpdate" },
    { "nvim-telescope/telescope.nvim", dependencies = { "nvim-lua/plenary.nvim" } },
    { "neovim/nvim-lspconfig" },
}, {
    install = { colorscheme = { "habamax" } },
    checker = { enabled = true },
})
```

---

**基本写法：插件配置**
`config = function() ... end`
```lua
-- 插件配置回调
{
    "nvim-telescope/telescope.nvim",
    dependencies = { "nvim-lua/plenary.nvim" },
    config = function()
        require("telescope").setup({})
        vim.keymap.set("n", "<leader>ff", require("telescope.builtin").find_files)
    end
}
```

---

## API 与函数

**基本写法：vim.fn 调用 vim 函数**
`vim.fn.<函数>(<参数>)`
```lua
-- 调用 vim 内置函数
local cwd = vim.fn.getcwd()
local expand = vim.fn.expand("%:p")
local line = vim.fn.line(".")
vim.fn.mkdir(vim.fn.stdpath("config") .. "/tmp", "p")
```

---

**基本写法：vim.cmd 执行命令**
`vim.cmd("<命令>")`
```lua
-- 执行 Ex 命令
vim.cmd("colorscheme habamax")
vim.cmd("set number")
-- 多行
vim.cmd([[
    augroup MyGroup
        autocmd!
    augroup END
]])
```

---

**基本写法：vim.notify 通知**
`vim.notify(<消息>, <级别>)`
```lua
-- 显示通知
vim.notify("Hello", vim.log.levels.INFO)
vim.notify("警告", vim.log.levels.WARN)
vim.notify("错误", vim.log.levels.ERROR)
```

---

## LSP 配置

**基本写法：lspconfig**
`require("lspconfig").<服务器>.setup(<配置>)`
```lua
-- 配置语言服务器
local lspconfig = require("lspconfig")
lspconfig.lua_ls.setup({
    settings = {
        Lua = {
            diagnostics = { globals = { "vim" } },
            workspace = { checkThirdParty = false },
        }
    }
})
lspconfig.clangd.setup({})
lspconfig.pyright.setup({})
```
