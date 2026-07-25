/**
 * 统一存储抽象层（web 端）
 * =============================================================================
 * 职责：
 *   1. 提供 SSR 安全的 localStorage / sessionStorage 访问（Astro SSR 场景下 window 不存在）
 *   2. 统一 try-catch 包裹，避免隐私模式或配额超限导致运行时崩溃
 *   3. 提供 JSON 序列化/反序列化便捷方法
 *   4. 提供防抖写入，减少高频写入对性能的影响
 *   5. 提供 storage 事件跨标签页同步能力
 *
 * 设计原则：
 *   - 所有方法在 SSR 环境（无 window）下安全降级，返回 null/undefined 而非抛错
 *   - 读取方法不抛错，写入方法静默吞掉异常（存储失败不应阻断业务逻辑）
 *   - 类型安全：泛型支持确保序列化/反序列化的类型一致性
 *
 * 使用场景：
 *   - 主题偏好持久化（fandex-theme）
 *   - 侧边栏状态持久化（fandex-sidebar-*）
 *   - 全屏模式状态（fandex-fullscreen）
 *   - 任何需要跨刷新保持的客户端状态
 *
 * 偏差报备（ProgressToggle 功能删除）：
 *   - 原：包含阅读进度持久化（fandex-progress-*）
 *   - 新：ProgressToggle（已读/未读）功能已删除，fandex-progress-* 不再使用
 *   - 依据：用户明确要求删除 ProgressToggle 及其相关的一切功能
 * =============================================================================
 */

/** SSR 环境检测：window 或 localStorage 不存在时返回 false */
const isClientSide = typeof window !== 'undefined' && typeof window.localStorage !== 'undefined';

/** 防抖写入的定时器映射（按 key 去重） */
const debounceTimers = new Map<string, ReturnType<typeof setTimeout>>();

/**
 * 安全读取 localStorage 字符串值
 * SSR 环境或异常时返回 null，不抛错
 *
 * @param key - 存储 key
 * @returns 存储的字符串值；不存在或异常时返回 null
 */
export function getItem(key: string): string | null {
  if (!isClientSide) return null;
  try {
    return window.localStorage.getItem(key);
  } catch {
    // 隐私模式、配额超限或安全策略阻止访问时降级
    return null;
  }
}

/**
 * 安全写入 localStorage 字符串值
 * 异常时静默吞掉，不阻断业务逻辑
 *
 * @param key - 存储 key
 * @param value - 要存储的字符串值
 */
export function setItem(key: string, value: string): void {
  if (!isClientSide) return;
  try {
    window.localStorage.setItem(key, value);
  } catch {
    // 写入失败静默降级（隐私模式或配额超限）
  }
}

/**
 * 安全移除 localStorage 项
 *
 * @param key - 要移除的存储 key
 */
export function removeItem(key: string): void {
  if (!isClientSide) return;
  try {
    window.localStorage.removeItem(key);
  } catch {
    // 移除失败静默降级
  }
}

/**
 * 安全读取并 JSON 反序列化 localStorage 值
 * 泛型 T 确保返回类型与预期一致
 *
 * @param key - 存储 key
 * @returns 反序列化后的值；不存在、解析失败或异常时返回 null
 */
export function getJSON<T>(key: string): T | null {
  const raw = getItem(key);
  if (raw === null) return null;
  try {
    return JSON.parse(raw) as T;
  } catch {
    // JSON 解析失败（数据格式变更或损坏）时返回 null
    return null;
  }
}

/**
 * 安全 JSON 序列化并写入 localStorage
 *
 * @param key - 存储 key
 * @param value - 要序列化存储的值
 */
export function setJSON<T>(key: string, value: T): void {
  try {
    setItem(key, JSON.stringify(value));
  } catch {
    // 序列化失败（循环引用等）静默降级
  }
}

/**
 * 防抖写入 localStorage
 * 在指定延迟内多次写入同一 key 时，仅最后一次生效
 * 适用于高频更新场景（如滚动位置、实时进度）
 *
 * @param key - 存储 key
 * @param value - 要存储的字符串值
 * @param delay - 防抖延迟（毫秒），默认 300ms
 */
export function setItemDebounced(key: string, value: string, delay = 300): void {
  if (!isClientSide) return;
  // 清除已有的防抖定时器
  const existingTimer = debounceTimers.get(key);
  if (existingTimer) {
    clearTimeout(existingTimer);
  }
  // 设置新的防抖定时器
  const timer = setTimeout(() => {
    setItem(key, value);
    debounceTimers.delete(key);
  }, delay);
  debounceTimers.set(key, timer);
}

/**
 * 监听跨标签页 storage 事件
 * 当其他标签页修改 localStorage 时触发回调
 * 用于主题切换、进度同步等多标签页同步场景
 *
 * @param key - 要监听的存储 key
 * @param callback - 值变化时的回调函数
 * @returns 取消监听的函数（用于清理）
 */
export function onStorageChange(
  key: string,
  callback: (newValue: string | null, oldValue: string | null) => void,
): () => void {
  if (!isClientSide) return () => {};
  const handler = (e: StorageEvent) => {
    if (e.key === key) {
      callback(e.newValue, e.oldValue);
    }
  };
  window.addEventListener('storage', handler);
  return () => {
    window.removeEventListener('storage', handler);
  };
}

/**
 * 批量清理指定前缀的 localStorage 项
 * 用于重置或清理功能
 *
 * @param prefix - 存储 key 前缀
 */
export function clearByPrefix(prefix: string): void {
  if (!isClientSide) return;
  try {
    const keysToRemove: string[] = [];
    for (let i = 0; i < window.localStorage.length; i++) {
      const key = window.localStorage.key(i);
      if (key && key.startsWith(prefix)) {
        keysToRemove.push(key);
      }
    }
    keysToRemove.forEach((k) => window.localStorage.removeItem(k));
  } catch {
    // 清理失败静默降级
  }
}
