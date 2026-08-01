/**
 * 算法练习测试脚手架生成器
 *
 * 功能概述：
 *   - 根据题目用例与语言，生成追加在用户代码末尾的测试代码
 *   - JS/TS/Python：用例以 Base64 嵌入，运行时解析并逐条断言
 *   - C/C++：直接生成带字面量的 main 测试代码（JSCPP 可解释执行）
 *   - 统一输出约定：[PASS] / [FAIL] 逐条结果 + [RESULT] passed/failed/total 汇总行
 *
 * 设计原则：
 *   - 用例数据通过 Base64 传输，避免引号/换行/Unicode 转义问题
 *   - 失败时输出期望与实际值，便于用户定位问题
 *   - 不修改用户代码内容，仅追加测试代码
 */

import type { Exercise, LabLanguage } from './types';

/** 用例 JSON 的 Base64 编码（UTF-8 安全，浏览器环境可用 btoa） */
function utf8ToBase64(text: string): string {
  const bytes = new TextEncoder().encode(text);
  let binary = '';
  bytes.forEach((b) => {
    binary += String.fromCharCode(b);
  });
  return btoa(binary);
}

/** 生成 JavaScript/TypeScript 测试脚手架 */
function buildJsHarness(exercise: Exercise): string {
  const casesB64 = utf8ToBase64(JSON.stringify(exercise.cases));
  const fnName = exercise.functionName;
  const mutate = exercise.kind === 'mutate';
  return `
/* ===== 测试脚手架（自动生成） ===== */
(function () {
  function __decode(b64) {
    var bin = atob(b64);
    var bytes = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
    return new TextDecoder('utf-8').decode(bytes);
  }
  function __deepEqual(a, b) {
    if (a === b) return true;
    if (typeof a !== typeof b) return false;
    if (Array.isArray(a)) {
      if (!Array.isArray(b) || a.length !== b.length) return false;
      for (var i = 0; i < a.length; i++) {
        if (!__deepEqual(a[i], b[i])) return false;
      }
      return true;
    }
    if (a && b && typeof a === 'object') {
      var ka = Object.keys(a), kb = Object.keys(b);
      if (ka.length !== kb.length) return false;
      for (var j = 0; j < ka.length; j++) {
        if (!__deepEqual(a[ka[j]], b[ka[j]])) return false;
      }
      return true;
    }
    return false;
  }
  function __fmt(v) {
    try { return JSON.stringify(v); } catch (e) { return String(v); }
  }
  var __cases = JSON.parse(__decode(${JSON.stringify(casesB64)}));
  if (typeof ${fnName} !== 'function') {
    console.log('[FAIL] 未找到函数 ${fnName}，请保持函数名与题目要求一致');
    console.log('[RESULT] passed=0 failed=1 total=1');
    return;
  }
  var __pass = 0, __fail = 0;
  for (var i = 0; i < __cases.length; i++) {
    var c = __cases[i];
    try {
      var out;
      ${mutate ? `var args = c.args.slice();\n      ${fnName}(args[0]);\n      out = args[0];` : `out = ${fnName}.apply(null, c.args);`}
      if (__deepEqual(out, c.expected)) {
        __pass++;
        console.log('[PASS] 用例 ' + (i + 1));
      } else {
        __fail++;
        console.log('[FAIL] 用例 ' + (i + 1) + ' 期望 ' + __fmt(c.expected) + ' 实际 ' + __fmt(out));
      }
    } catch (e) {
      __fail++;
      console.log('[FAIL] 用例 ' + (i + 1) + ' 异常: ' + (e && e.message ? e.message : String(e)));
    }
  }
  console.log('[RESULT] passed=' + __pass + ' failed=' + __fail + ' total=' + __cases.length);
})();
`;
}

/** 生成 Python 测试脚手架 */
function buildPythonHarness(exercise: Exercise): string {
  const casesB64 = utf8ToBase64(JSON.stringify(exercise.cases));
  const fnName = exercise.functionName;
  const mutate = exercise.kind === 'mutate';
  const callLine = mutate
    ? `            __args = list(__c['args'])\n            ${fnName}(__args[0])\n            __out = __args[0]`
    : `            __out = ${fnName}(*__c['args'])`;
  return `
# ===== 测试脚手架（自动生成） =====
import base64
import json


def __decode(b64: str) -> str:
    return base64.b64decode(b64).decode('utf-8')


def __deep_equal(a, b) -> bool:
    if a == b:
        return True
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False
        return all(__deep_equal(x, y) for x, y in zip(a, b))
    return False


def __fmt(v) -> str:
    try:
        return json.dumps(v, ensure_ascii=False)
    except Exception:
        return str(v)


__cases = json.loads(__decode(${JSON.stringify(casesB64)}))

if not callable(globals().get('${fnName}')):
    print('[FAIL] 未找到函数 ${fnName}，请保持函数名与题目要求一致')
    print('[RESULT] passed=0 failed=1 total=1')
else:
    __pass = 0
    __fail = 0
    for __i, __c in enumerate(__cases):
        try:
${callLine}
            if __deep_equal(__out, __c['expected']):
                __pass += 1
                print('[PASS] 用例 ' + str(__i + 1))
            else:
                __fail += 1
                print('[FAIL] 用例 ' + str(__i + 1) + ' 期望 ' + __fmt(__c['expected']) + ' 实际 ' + __fmt(__out))
        except Exception as __e:
            __fail += 1
            print('[FAIL] 用例 ' + str(__i + 1) + ' 异常: ' + str(__e))
    print('[RESULT] passed=%d failed=%d total=%d' % (__pass, __fail, len(__cases)))
`;
}

/** 转义 C 字符串字面量 */
function cStringLiteral(value: string): string {
  return `"${value.replace(/\\/g, '\\\\').replace(/"/g, '\\"').replace(/\n/g, '\\n')}"`;
}

/** 生成 C 整型数组字面量（空数组补 {0}，长度由调用处传入） */
function cArrayLiteral(values: unknown): string {
  const arr = Array.isArray(values) ? (values as unknown[]) : [];
  if (arr.length === 0) return '{0}';
  return `{${arr.map((v) => String(v)).join(', ')}}`;
}

/** 生成 C/C++ 测试脚手架 */
function buildCHarness(exercise: Exercise): string {
  const { returnType, argTypes } = exercise.cSignature;
  const fnName = exercise.functionName;
  const mutate = exercise.kind === 'mutate';
  const lines: string[] = [];

  lines.push('/* ===== 测试脚手架（自动生成） ===== */');
  lines.push('#include <stdio.h>');
  lines.push('#include <string.h>');
  lines.push('');
  lines.push('static int __pg_pass = 0;');
  lines.push('static int __pg_fail = 0;');
  lines.push('');
  lines.push('static int __pg_eq_int(int a, int b) { return a == b; }');
  lines.push('static int __pg_eq_bool(int a, int b) { return (a != 0) == (b != 0); }');
  lines.push('static int __pg_eq_str(const char* a, const char* b) { return strcmp(a, b) == 0; }');
  lines.push('static int __pg_eq_arr(const int* a, const int* b, int n) {');
  lines.push('  int i;');
  lines.push('  for (i = 0; i < n; i++) { if (a[i] != b[i]) return 0; }');
  lines.push('  return 1;');
  lines.push('}');
  lines.push('');
  lines.push('int main(void) {');

  exercise.cases.forEach((c, index) => {
    const caseNo = index + 1;
    const args = c.args;
    const callArgs: string[] = [];
    const arrayVars: string[] = [];

    // 为 int[] 参数生成数组变量
    argTypes.forEach((type, ai) => {
      if (type === 'int[]') {
        const value = args[ai];
        arrayVars.push(`    int __a${ai}[] = ${cArrayLiteral(value)};`);
      }
    });
    // 组装调用参数：数组参数附带长度，字符串参数使用字面量
    argTypes.forEach((type, ai) => {
      if (type === 'int[]') {
        const length = Array.isArray(args[ai]) ? (args[ai] as unknown[]).length : 0;
        callArgs.push(`__a${ai}, ${length}`);
      } else if (type === 'str') {
        callArgs.push(cStringLiteral(String(args[ai])));
      } else {
        callArgs.push(String(args[ai]));
      }
    });

    lines.push('  { /* 用例 ' + caseNo + ' */');
    arrayVars.forEach((v) => lines.push(v));

    if (mutate) {
      // 原地修改型：调用后比较参数数组
      const expectedArr = Array.isArray(c.expected) ? (c.expected as unknown[]) : [];
      const expectedLen = expectedArr.length;
      lines.push(`    int __e${caseNo}[] = ${cArrayLiteral(c.expected)};`);
      lines.push(`    ${fnName}(${callArgs.join(', ')});`);
      lines.push(`    if (__pg_eq_arr(__a0, __e${caseNo}, ${expectedLen})) {`);
      lines.push('      __pg_pass++;');
      lines.push(`      printf("[PASS] 用例 ${caseNo}\\n");`);
      lines.push('    } else {');
      lines.push('      __pg_fail++;');
      lines.push(`      printf("[FAIL] 用例 ${caseNo}\\n");`);
      lines.push('    }');
    } else {
      const exp = c.expected;
      let comparison: string;
      let extraPrint = '';
      if (returnType === 'bool') {
        comparison = `__pg_eq_bool(${fnName}(${callArgs.join(', ')}), ${exp ? 1 : 0})`;
      } else if (returnType === 'int') {
        comparison = `__pg_eq_int(${fnName}(${callArgs.join(', ')}), ${String(exp)})`;
        extraPrint = `      printf("  期望 ${String(exp)} 实际 %d\\n", ${fnName}(${callArgs.join(', ')}));`;
      } else {
        comparison = '__pg_eq_str(0, 0)';
      }
      lines.push(`    if (${comparison}) {`);
      lines.push('      __pg_pass++;');
      lines.push(`      printf("[PASS] 用例 ${caseNo}\\n");`);
      lines.push('    } else {');
      lines.push('      __pg_fail++;');
      lines.push(`      printf("[FAIL] 用例 ${caseNo}\\n");`);
      if (extraPrint) lines.push(extraPrint);
      lines.push('    }');
    }
    lines.push('  }');
  });

  lines.push(`  printf("[RESULT] passed=%d failed=%d total=%d\\n", __pg_pass, __pg_fail, ${exercise.cases.length});`);
  lines.push('  return 0;');
  lines.push('}');
  return '\n' + lines.join('\n') + '\n';
}

/**
 * 生成指定语言的测试脚手架代码
 * @param exercise - 题目
 * @param language - 语言
 * @returns 追加到用户代码末尾的测试代码
 */
export function buildHarness(exercise: Exercise, language: LabLanguage): string {
  if (language === 'javascript' || language === 'typescript') {
    return buildJsHarness(exercise);
  }
  if (language === 'python') {
    return buildPythonHarness(exercise);
  }
  return buildCHarness(exercise);
}

/** 解析运行输出中的汇总行 */
export interface RunSummary {
  /** 通过用例数 */
  passed: number;
  /** 失败用例数 */
  failed: number;
  /** 总用例数 */
  total: number;
}

/**
 * 从运行输出中解析 [RESULT] 汇总
 * @param stdout - 运行标准输出
 * @returns 汇总信息；未找到汇总行时返回 null
 */
export function parseRunSummary(stdout: string): RunSummary | null {
  const match = stdout.match(/\[RESULT\]\s+passed=(\d+)\s+failed=(\d+)\s+total=(\d+)/);
  if (!match) return null;
  return {
    passed: Number(match[1]),
    failed: Number(match[2]),
    total: Number(match[3]),
  };
}
