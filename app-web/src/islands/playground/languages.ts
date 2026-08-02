/**
 * 在线编程沙箱语言目录（内置数据）
 *
 * 功能概述：
 *   - 提供站点全部主流语言的编辑/高亮支持（JS/TS/Python/C/C++/Go/Java/Kotlin/
 *     Rust/C#/Lua/SQL/Shell）
 *   - 每种语言提供独立起始模板与运行能力标记：
 *     - runnable=true：浏览器沙箱内可直接运行（JS/TS/Python/C/C++/Lua）
 *     - runnable=false：仅提供编辑、高亮与本地保存，运行提示使用本地工具链
 *
 * 设计原则：
 *   - 语言为静态数据，随站点构建发布，不占用户本地存储
 *   - 编辑能力覆盖全部语言；运行能力受浏览器 WASM/JS 运行时限制，如实标注
 */

import type { EditorLanguage } from './CodeMirrorBox';
import type { LabLanguage } from './types';

/** 沙箱可选语言顺序（常用语言在前，便于工具栏快速切换） */
export const LAB_LANGUAGES: readonly LabLanguage[] = [
  'javascript',
  'typescript',
  'python',
  'c',
  'cpp',
  'go',
  'java',
  'kotlin',
  'rust',
  'csharp',
  'lua',
  'sql',
  'shell',
];

/** 语言显示名称 */
export const LAB_LANGUAGE_LABELS: Record<LabLanguage, string> = {
  javascript: 'JavaScript',
  typescript: 'TypeScript',
  python: 'Python',
  c: 'C',
  cpp: 'C++',
  go: 'Go',
  java: 'Java',
  kotlin: 'Kotlin',
  rust: 'Rust',
  csharp: 'C#',
  lua: 'Lua',
  sql: 'SQL',
  shell: 'Shell',
};

/** 语言文件扩展名（编辑器标题展示） */
export const LAB_LANGUAGE_EXT: Record<LabLanguage, string> = {
  javascript: 'js',
  typescript: 'ts',
  python: 'py',
  c: 'c',
  cpp: 'cpp',
  go: 'go',
  java: 'java',
  kotlin: 'kt',
  rust: 'rs',
  csharp: 'cs',
  lua: 'lua',
  sql: 'sql',
  shell: 'sh',
};

/**
 * 语言运行能力
 * - true：浏览器沙箱内可直接运行
 * - false：暂不支持浏览器运行，编辑器仍可正常使用
 */
export const LAB_LANGUAGE_RUNNABLE: Record<LabLanguage, boolean> = {
  javascript: true,
  typescript: true,
  python: true,
  c: true,
  cpp: true,
  go: false,
  java: false,
  kotlin: false,
  rust: false,
  csharp: false,
  lua: true,
  sql: false,
  shell: false,
};

/** 不支持运行时提示模板 */
const LOCAL_TOOLCHAIN_NOTE =
  '该语言暂不支持浏览器内运行。编辑器已提供语法高亮与本地保存，请在本地安装对应工具链后执行代码。';

/** 各语言起始模板（Hello World 级别的可运行示例） */
export const LAB_STARTERS: Record<LabLanguage, string> = {
  javascript: `// JavaScript 在线沙箱
console.log('Hello, FANDEX!');

function add(a, b) {
  return a + b;
}

console.log('1 + 2 =', add(1, 2));`,

  typescript: `// TypeScript 在线沙箱（浏览器内按 JavaScript 执行，不做类型检查）
const greet = (name: string): string => \`Hello, \${name}!\`;

console.log(greet('FANDEX'));`,

  python: `# Python 在线沙箱
def greet(name: str) -> str:
    return f"Hello, {name}!"


print(greet("FANDEX"))`,

  c: `#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main(void) {
    printf("Hello, FANDEX!\\n");
    printf("1 + 2 = %d\\n", add(1, 2));
    return 0;
}`,

  cpp: `#include <iostream>

int add(int a, int b) {
    return a + b;
}

int main() {
    std::cout << "Hello, FANDEX!" << std::endl;
    std::cout << "1 + 2 = " << add(1, 2) << std::endl;
    return 0;
}`,

  go: `// Go 在线沙箱（编辑模式；运行需本地 Go 工具链）
package main

import "fmt"

func main() {
	fmt.Println("Hello, FANDEX!")
}`,

  java: `// Java 在线沙箱（编辑模式；运行需本地 JDK）
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, FANDEX!");
    }
}`,

  kotlin: `// Kotlin 在线沙箱（编辑模式；运行需本地 Kotlin 工具链）
fun main() {
    println("Hello, FANDEX!")
}`,

  rust: `// Rust 在线沙箱（编辑模式；运行需本地 cargo）
fn main() {
    println!("Hello, FANDEX!");
}`,

  csharp: `// C# 在线沙箱（编辑模式；运行需本地 .NET SDK）
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, FANDEX!");
    }
}`,

  lua: `-- Lua 在线沙箱
local function add(a, b)
    return a + b
end

print("Hello, FANDEX!")
print("1 + 2 =", add(1, 2))`,

  sql: `-- SQL 在线沙箱（编辑模式；运行需本地数据库或在线 SQL 环境）
SELECT 'Hello, FANDEX!' AS greeting;`,

  shell: `#!/usr/bin/env bash
# Shell 在线沙箱（编辑模式；运行需本地终端）
echo "Hello, FANDEX!"`,
};

/**
 * 获取指定语言的起始模板
 * @param language - 语言
 * @returns 起始代码
 */
export function getStarter(language: LabLanguage): string {
  return LAB_STARTERS[language];
}

/**
 * 获取语言对应的 CodeMirror 语法标识
 * @param language - 沙箱语言
 * @returns CodeMirror 语言名
 */
export function toEditorLanguage(
  language: LabLanguage,
): EditorLanguage {
  // 沙箱语言名与 CodeMirror 语言名一一对应（c/cpp 共用 cpp 高亮，由 CodeMirrorBox 内部处理）
  return language;
}

/**
 * 获取不支持运行时的提示文案
 * @param language - 语言
 * @returns 提示文本
 */
export function getUnsupportedRunMessage(language: LabLanguage): string {
  return `${LAB_LANGUAGE_LABELS[language]}：${LOCAL_TOOLCHAIN_NOTE}`;
}
