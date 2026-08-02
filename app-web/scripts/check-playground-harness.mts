/**
 * Playground 测试脚手架校验脚本（开发用）
 *
 * 功能概述：
 *   - 对每道题目生成 JS 与 Python 测试脚手架，并附上正确实现后实际执行
 *   - 校验 [RESULT] 汇总行是否全部通过（passed === total）
 *   - 需本机安装 Python 3（py 命令）时才会执行 Python 校验
 *
 * 运行方式：
 *   pnpm exec tsx app-web/scripts/check-playground-harness.mts
 */

import { spawnSync } from 'node:child_process';
import { mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { EXERCISES } from '../src/islands/playground/exercises.ts';
import { buildHarness, parseRunSummary } from '../src/islands/playground/pg-harness.ts';

/** 各题目的正确实现（仅用于校验脚手架本身） */
const SOLUTIONS: Record<string, { js: string; py: string }> = {
  fibonacci: {
    js: 'function fibonacci(n) { if (n < 2) return n; return fibonacci(n - 1) + fibonacci(n - 2); }',
    py: 'def fibonacci(n):\n    if n < 2:\n        return n\n    return fibonacci(n - 1) + fibonacci(n - 2)',
  },
  'is-prime': {
    js: 'function isPrime(n) { if (n <= 1) return false; for (let i = 2; i * i <= n; i++) if (n % i === 0) return false; return true; }',
    py: 'def isPrime(n):\n    if n <= 1:\n        return False\n    i = 2\n    while i * i <= n:\n        if n % i == 0:\n            return False\n        i += 1\n    return True',
  },
  gcd: {
    js: 'function gcd(a, b) { while (b) { const t = b; b = a % b; a = t; } return a; }',
    py: 'def gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a',
  },
  factorial: {
    js: 'function factorial(n) { let r = 1; for (let i = 2; i <= n; i++) r *= i; return r; }',
    py: 'def factorial(n):\n    r = 1\n    for i in range(2, n + 1):\n        r *= i\n    return r',
  },
  'max-subarray-sum': {
    js: 'function maxSubarraySum(arr) { let best = -Infinity, cur = 0; for (const v of arr) { cur = Math.max(v, cur + v); best = Math.max(best, cur); } return best === -Infinity ? 0 : best; }',
    py: 'def maxSubarraySum(arr):\n    best = None\n    cur = 0\n    for v in arr:\n        cur = max(v, cur + v)\n        best = cur if best is None else max(best, cur)\n    return 0 if best is None else best',
  },
  'reverse-array': {
    js: 'function reverseArray(arr) { let i = 0, j = arr.length - 1; while (i < j) { const t = arr[i]; arr[i] = arr[j]; arr[j] = t; i++; j--; } }',
    py: 'def reverseArray(arr):\n    i, j = 0, len(arr) - 1\n    while i < j:\n        arr[i], arr[j] = arr[j], arr[i]\n        i += 1\n        j -= 1',
  },
  'valid-parentheses': {
    js: 'function isValid(s) { const stack = []; const map = { ")": "(", "]": "[", "}": "{" }; for (const ch of s) { if (ch === "(" || ch === "[" || ch === "{") { stack.push(ch); } else if (stack.pop() !== map[ch]) { return false; } } return stack.length === 0; }',
    py: 'def isValid(s):\n    stack = []\n    pairs = {")": "(", "]": "[", "}": "{"}\n    for ch in s:\n        if ch in "([{":\n            stack.append(ch)\n        elif not stack or stack.pop() != pairs[ch]:\n            return False\n    return len(stack) == 0',
  },
  'binary-search': {
    js: 'function binarySearch(arr, target) { let lo = 0, hi = arr.length - 1; while (lo <= hi) { const mid = (lo + hi) >> 1; if (arr[mid] === target) return mid; if (arr[mid] < target) lo = mid + 1; else hi = mid - 1; } return -1; }',
    py: 'def binarySearch(arr, target):\n    lo, hi = 0, len(arr) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if arr[mid] == target:\n            return mid\n        if arr[mid] < target:\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return -1',
  },
};

/** 在 Node 内执行 JS 脚手架 */
function checkJs(exerciseId: string): boolean {
  const exercise = EXERCISES.find((e) => e.id === exerciseId);
  if (!exercise) throw new Error(`题目不存在: ${exerciseId}`);
  const solution = SOLUTIONS[exerciseId];
  if (!solution) throw new Error(`缺少 JS 正确实现: ${exerciseId}`);

  const logs: string[] = [];
  const originalLog = console.log;
  console.log = (...args: unknown[]) => logs.push(args.map(String).join(' '));
  try {
    const fn = new Function(`${solution.js}\n${buildHarness(exercise, 'javascript')}`);
    fn();
  } finally {
    console.log = originalLog;
  }

  const summary = parseRunSummary(logs.join('\n'));
  if (!summary) {
    console.error(`[JS] ${exerciseId}: 未找到 [RESULT] 汇总行`);
    return false;
  }
  const ok = summary.failed === 0 && summary.passed === summary.total;
  console.log(`[JS] ${exerciseId}: passed=${summary.passed} failed=${summary.failed} total=${summary.total} ${ok ? 'OK' : 'FAIL'}`);
  return ok;
}

/** 调用本机 Python 执行脚手架 */
function checkPython(exerciseId: string): boolean {
  const exercise = EXERCISES.find((e) => e.id === exerciseId);
  if (!exercise) throw new Error(`题目不存在: ${exerciseId}`);
  const solution = SOLUTIONS[exerciseId];
  if (!solution) throw new Error(`缺少 Python 正确实现: ${exerciseId}`);

  const dir = mkdtempSync(join(tmpdir(), 'pg-harness-'));
  const file = join(dir, 'test.py');
  writeFileSync(file, `${solution.py}\n${buildHarness(exercise, 'python')}`, 'utf8');
  const result = spawnSync('py', [file], { encoding: 'utf8', timeout: 30000 });
  rmSync(dir, { recursive: true, force: true });

  if (result.error) {
    console.log(`[PY] ${exerciseId}: 跳过（本机未安装 Python: ${result.error.message}）`);
    return true;
  }
  if (result.status !== 0) {
    console.error(`[PY] ${exerciseId}: 执行失败\n${result.stdout}\n${result.stderr}`);
    return false;
  }
  const summary = parseRunSummary(result.stdout);
  if (!summary) {
    console.error(`[PY] ${exerciseId}: 未找到 [RESULT] 汇总行\n${result.stdout}`);
    return false;
  }
  const ok = summary.failed === 0 && summary.passed === summary.total;
  console.log(`[PY] ${exerciseId}: passed=${summary.passed} failed=${summary.failed} total=${summary.total} ${ok ? 'OK' : 'FAIL'}`);
  return ok;
}

/** 运行全部校验 */
function main(): void {
  let failed = false;
  for (const exercise of EXERCISES) {
    failed = !checkJs(exercise.id) || failed;
    failed = !checkPython(exercise.id) || failed;
  }
  if (failed) {
    console.error('校验未通过');
    process.exit(1);
  }
  console.log('全部脚手架校验通过');
}

main();
