/**
 * 算法练习题目目录（内置数据）
 *
 * 功能概述：
 *   - 提供 8 道经典算法练习题，覆盖入门/进阶/挑战三个难度
 *   - 每道题包含 5 种语言（JS/TS/Python/C/C++）的起始代码模板
 *   - 内置测试用例与 C/C++ 签名元数据，供测试脚手架生成器使用
 *
 * 设计原则：
 *   - 题目为静态数据，随站点构建发布，不占用户本地存储
 *   - 所有语言统一使用相同函数名，降低切换语言的学习成本
 *   - 用例数值范围受限，确保在浏览器沙箱（JSCPP/Pyodide）内可执行
 */

import type { Exercise, ExerciseDifficulty, LabLanguage } from './types';

/** 实验室内可选语言（Go 的浏览器沙箱暂不支持，不进入列表） */
export const LAB_LANGUAGES: LabLanguage[] = ['javascript', 'typescript', 'python', 'c', 'cpp'];

/** 语言显示名称 */
export const LAB_LANGUAGE_LABELS: Record<LabLanguage, string> = {
  javascript: 'JavaScript',
  typescript: 'TypeScript',
  python: 'Python',
  c: 'C',
  cpp: 'C++',
};

/** 难度标签样式类（与主题令牌联动） */
export const DIFFICULTY_CLASS: Record<ExerciseDifficulty, string> = {
  入门: 'pg-badge--easy',
  进阶: 'pg-badge--medium',
  挑战: 'pg-badge--hard',
};

/** 通用 JavaScript 起始代码头部注释 */
const JS_NOTE = `/**
 * 请实现下面的函数并保证签名不变。
 * 测试用例会自动调用该函数并检查返回值。
 */`;

/** 通用 Python 起始代码注释 */
const PY_NOTE = `# 请实现下面的函数并保证签名不变。
# 测试用例会自动调用该函数并检查返回值。`;

/** 题目目录（顺序即默认展示顺序） */
export const EXERCISES: Exercise[] = [
  {
    id: 'fibonacci',
    title: '斐波那契数列',
    difficulty: '入门',
    tags: ['递归', '动态规划'],
    description:
      '计算第 n 个斐波那契数，其中 fibonacci(0) = 0，fibonacci(1) = 1，\nfibonacci(n) = fibonacci(n-1) + fibonacci(n-2)（n >= 2）。',
    example: '输入: n = 6\n输出: 8（序列: 0, 1, 1, 2, 3, 5, 8）',
    functionName: 'fibonacci',
    kind: 'call',
    cSignature: { returnType: 'int', argTypes: ['int'] },
    cases: [
      { args: [0], expected: 0 },
      { args: [1], expected: 1 },
      { args: [2], expected: 1 },
      { args: [5], expected: 5 },
      { args: [10], expected: 55 },
      { args: [20], expected: 6765 },
    ],
    hints: ['递归写法最简单，但 n 较大时会重复计算，可尝试循环或记忆化。'],
    starters: {
      javascript: `${JS_NOTE}\nfunction fibonacci(n) {\n  // 在此编写你的实现\n  return n;\n}`,
      typescript: `${JS_NOTE}\nfunction fibonacci(n) {\n  // 在此编写你的实现（浏览器内使用 JavaScript 兼容语法）\n  return n;\n}`,
      python: `${PY_NOTE}\ndef fibonacci(n: int) -> int:\n    # 在此编写你的实现\n    return n`,
      c: `#include <stdbool.h>\n\nint fibonacci(int n) {\n    // 在此编写你的实现\n    return n;\n}`,
      cpp: `int fibonacci(int n) {\n    // 在此编写你的实现\n    return n;\n}`,
    },
  },
  {
    id: 'is-prime',
    title: '素数判断',
    difficulty: '入门',
    tags: ['数学'],
    description: '判断一个整数 n 是否为素数。素数是大于 1 且只能被 1 和自身整除的自然数。',
    example: '输入: n = 17\n输出: true（17 只能被 1 和 17 整除）',
    functionName: 'isPrime',
    kind: 'call',
    cSignature: { returnType: 'bool', argTypes: ['int'] },
    cases: [
      { args: [2], expected: true },
      { args: [3], expected: true },
      { args: [4], expected: false },
      { args: [1], expected: false },
      { args: [17], expected: true },
      { args: [97], expected: true },
      { args: [100], expected: false },
    ],
    hints: ['只需检查 2 到 sqrt(n) 之间的整数即可；注意 n <= 1 直接返回 false。'],
    starters: {
      javascript: `${JS_NOTE}\nfunction isPrime(n) {\n  // 在此编写你的实现\n  return false;\n}`,
      typescript: `${JS_NOTE}\nfunction isPrime(n) {\n  // 在此编写你的实现（浏览器内使用 JavaScript 兼容语法）\n  return false;\n}`,
      python: `${PY_NOTE}\ndef isPrime(n: int) -> bool:\n    # 在此编写你的实现\n    return False`,
      c: `#include <stdbool.h>\n\nbool isPrime(int n) {\n    // 在此编写你的实现\n    return false;\n}`,
      cpp: `bool isPrime(int n) {\n    // 在此编写你的实现\n    return false;\n}`,
    },
  },
  {
    id: 'gcd',
    title: '最大公约数',
    difficulty: '入门',
    tags: ['数学', '欧几里得算法'],
    description: '计算两个非负整数 a 和 b 的最大公约数（GCD）。',
    example: '输入: a = 12, b = 18\n输出: 6',
    functionName: 'gcd',
    kind: 'call',
    cSignature: { returnType: 'int', argTypes: ['int', 'int'] },
    cases: [
      { args: [12, 18], expected: 6 },
      { args: [7, 13], expected: 1 },
      { args: [100, 10], expected: 10 },
      { args: [1, 1], expected: 1 },
      { args: [0, 5], expected: 5 },
    ],
    hints: ['使用辗转相除法：gcd(a, b) = gcd(b, a % b)，当 b 为 0 时返回 a。'],
    starters: {
      javascript: `${JS_NOTE}\nfunction gcd(a, b) {\n  // 在此编写你的实现\n  return a;\n}`,
      typescript: `${JS_NOTE}\nfunction gcd(a, b) {\n  // 在此编写你的实现（浏览器内使用 JavaScript 兼容语法）\n  return a;\n}`,
      python: `${PY_NOTE}\ndef gcd(a: int, b: int) -> int:\n    # 在此编写你的实现\n    return a`,
      c: `int gcd(int a, int b) {\n    // 在此编写你的实现\n    return a;\n}`,
      cpp: `int gcd(int a, int b) {\n    // 在此编写你的实现\n    return a;\n}`,
    },
  },
  {
    id: 'factorial',
    title: '阶乘',
    difficulty: '入门',
    tags: ['递归'],
    description: '计算 n 的阶乘 n!，其中 n! = 1 * 2 * ... * n，且 0! = 1。n 的取值范围为 0 到 12。',
    example: '输入: n = 5\n输出: 120',
    functionName: 'factorial',
    kind: 'call',
    cSignature: { returnType: 'int', argTypes: ['int'] },
    cases: [
      { args: [0], expected: 1 },
      { args: [1], expected: 1 },
      { args: [5], expected: 120 },
      { args: [10], expected: 3628800 },
      { args: [12], expected: 479001600 },
    ],
    hints: ['n 较小，递归或循环均可；注意 0! = 1 的边界。'],
    starters: {
      javascript: `${JS_NOTE}\nfunction factorial(n) {\n  // 在此编写你的实现\n  return 1;\n}`,
      typescript: `${JS_NOTE}\nfunction factorial(n) {\n  // 在此编写你的实现（浏览器内使用 JavaScript 兼容语法）\n  return 1;\n}`,
      python: `${PY_NOTE}\ndef factorial(n: int) -> int:\n    # 在此编写你的实现\n    return 1`,
      c: `int factorial(int n) {\n    // 在此编写你的实现\n    return 1;\n}`,
      cpp: `int factorial(int n) {\n    // 在此编写你的实现\n    return 1;\n}`,
    },
  },
  {
    id: 'max-subarray-sum',
    title: '最大子数组和',
    difficulty: '进阶',
    tags: ['动态规划', 'Kadane 算法'],
    description:
      '给定一个整数数组 arr（可能包含负数），找出和最大的连续子数组并返回其和。\n空数组返回 0。',
    example: '输入: arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]\n输出: 6（子数组 [4, -1, 2, 1]）',
    functionName: 'maxSubarraySum',
    kind: 'call',
    cSignature: { returnType: 'int', argTypes: ['int[]'] },
    cases: [
      { args: [[-2, 1, -3, 4, -1, 2, 1, -5, 4]], expected: 6 },
      { args: [[1]], expected: 1 },
      { args: [[-1, -2, -3]], expected: -1 },
      { args: [[5, -2, 3]], expected: 6 },
      { args: [[]], expected: 0 },
    ],
    hints: ['Kadane 算法：遍历时维护当前子数组和，若为负则重新开始。'],
    starters: {
      javascript: `${JS_NOTE}\nfunction maxSubarraySum(arr) {\n  // 在此编写你的实现\n  return 0;\n}`,
      typescript: `${JS_NOTE}\nfunction maxSubarraySum(arr) {\n  // 在此编写你的实现（浏览器内使用 JavaScript 兼容语法）\n  return 0;\n}`,
      python: `${PY_NOTE}\ndef maxSubarraySum(arr: list) -> int:\n    # 在此编写你的实现\n    return 0`,
      c: `int maxSubarraySum(int arr[], int n) {\n    // 在此编写你的实现（n 为数组长度）\n    return 0;\n}`,
      cpp: `int maxSubarraySum(int arr[], int n) {\n    // 在此编写你的实现（n 为数组长度）\n    return 0;\n}`,
    },
  },
  {
    id: 'reverse-array',
    title: '数组反转',
    difficulty: '入门',
    tags: ['数组', '双指针'],
    description: '原地反转整数数组 arr，函数不返回新数组，直接修改传入的数组。',
    example: '输入: arr = [1, 2, 3]\n修改后: [3, 2, 1]',
    functionName: 'reverseArray',
    kind: 'mutate',
    cSignature: { returnType: 'void', argTypes: ['int[]'] },
    cases: [
      { args: [[1, 2, 3]], expected: [3, 2, 1] },
      { args: [[5]], expected: [5] },
      { args: [[-1, 0, 4, 9]], expected: [9, 4, 0, -1] },
      { args: [[]], expected: [] },
    ],
    hints: ['使用双指针：交换首尾元素并向中间移动。'],
    starters: {
      javascript: `${JS_NOTE}\nfunction reverseArray(arr) {\n  // 在此编写你的实现（原地反转，直接修改 arr）\n}`,
      typescript: `${JS_NOTE}\nfunction reverseArray(arr) {\n  // 在此编写你的实现（原地反转，直接修改 arr）\n}`,
      python: `${PY_NOTE}\ndef reverseArray(arr: list) -> None:\n    # 在此编写你的实现（原地反转，直接修改 arr）\n    pass`,
      c: `void reverseArray(int arr[], int n) {\n    // 在此编写你的实现（原地反转，直接修改 arr）\n}`,
      cpp: `void reverseArray(int arr[], int n) {\n    // 在此编写你的实现（原地反转，直接修改 arr）\n}`,
    },
  },
  {
    id: 'valid-parentheses',
    title: '有效括号',
    difficulty: '进阶',
    tags: ['栈', '字符串'],
    description:
      '给定只包含字符 ( ) [ ] { } 的字符串 s，判断括号是否有效。\n有效规则：左括号必须由同类型右括号闭合，且闭合顺序正确。',
    example: '输入: s = "()[]{}"\n输出: true\n输入: s = "([)]"\n输出: false',
    functionName: 'isValid',
    kind: 'call',
    cSignature: { returnType: 'bool', argTypes: ['str'] },
    cases: [
      { args: ['()'], expected: true },
      { args: ['()[]{}'], expected: true },
      { args: ['(]'], expected: false },
      { args: ['([)]'], expected: false },
      { args: ['{[]}'], expected: true },
      { args: [''], expected: true },
      { args: ['((()))'], expected: true },
    ],
    hints: ['遍历字符串，遇到左括号入栈，遇到右括号检查栈顶是否匹配。'],
    starters: {
      javascript: `${JS_NOTE}\nfunction isValid(s) {\n  // 在此编写你的实现\n  return false;\n}`,
      typescript: `${JS_NOTE}\nfunction isValid(s) {\n  // 在此编写你的实现（浏览器内使用 JavaScript 兼容语法）\n  return false;\n}`,
      python: `${PY_NOTE}\ndef isValid(s: str) -> bool:\n    # 在此编写你的实现\n    return False`,
      c: `#include <stdbool.h>\n\nbool isValid(const char* s) {\n    // 在此编写你的实现\n    return false;\n}`,
      cpp: `bool isValid(const char* s) {\n    // 在此编写你的实现\n    return false;\n}`,
    },
  },
  {
    id: 'binary-search',
    title: '二分查找',
    difficulty: '进阶',
    tags: ['数组', '二分查找'],
    description: '在升序整数数组 arr 中查找目标值 target，返回其下标；不存在时返回 -1。',
    example: '输入: arr = [1, 3, 5, 7, 9], target = 5\n输出: 2',
    functionName: 'binarySearch',
    kind: 'call',
    cSignature: { returnType: 'int', argTypes: ['int[]', 'int'] },
    cases: [
      { args: [[1, 3, 5, 7, 9], 5], expected: 2 },
      { args: [[1, 3, 5, 7, 9], 4], expected: -1 },
      { args: [[1], 1], expected: 0 },
      { args: [[], 5], expected: -1 },
      { args: [[-2, 0, 2], 0], expected: 1 },
    ],
    hints: ['维护左右边界，每次比较中间元素后缩小一半区间。'],
    starters: {
      javascript: `${JS_NOTE}\nfunction binarySearch(arr, target) {\n  // 在此编写你的实现\n  return -1;\n}`,
      typescript: `${JS_NOTE}\nfunction binarySearch(arr, target) {\n  // 在此编写你的实现（浏览器内使用 JavaScript 兼容语法）\n  return -1;\n}`,
      python: `${PY_NOTE}\ndef binarySearch(arr: list, target: int) -> int:\n    # 在此编写你的实现\n    return -1`,
      c: `int binarySearch(int arr[], int n, int target) {\n    // 在此编写你的实现（n 为数组长度）\n    return -1;\n}`,
      cpp: `int binarySearch(int arr[], int n, int target) {\n    // 在此编写你的实现（n 为数组长度）\n    return -1;\n}`,
    },
  },
];

/**
 * 按 ID 查找题目
 * @param id - 题目 ID
 * @returns 题目；不存在时返回第一个题目（保证页面始终可用）
 */
export function getExercise(id: string): Exercise {
  return EXERCISES.find((e) => e.id === id) ?? EXERCISES[0]!;
}

/**
 * 获取题目在指定语言下的起始代码
 * @param exercise - 题目
 * @param language - 语言
 * @returns 起始代码（无模板时回退到 JavaScript 模板）
 */
export function getStarter(exercise: Exercise, language: LabLanguage): string {
  const starter = exercise.starters[language];
  if (starter) return starter;
  return exercise.starters.javascript ?? '';
}
