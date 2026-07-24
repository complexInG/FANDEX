/**
 * 首页布局交互脚本
 * -----------------------------------------------------------------------------
 * 从 components/HomeLayout.astro 提取的客户端逻辑，负责：
 * - 全屏模式切换（点击按钮进入/退出全屏）
 * - 全屏状态持久化（localStorage 记忆用户偏好）
 * - 页面加载时恢复全屏状态
 *
 * 触发时机：
 * - 脚本首次加载时执行一次
 * - astro:page-load 事件触发时重新绑定（支持 View Transitions 路由切换）
 */

/** localStorage 键名：用于持久化全屏状态 */
const FULLSCREEN_STORAGE_KEY = 'fandex-fullscreen';

/**
 * 初始化首页全屏切换交互
 *
 * 实现要点：
 * - 绑定 #home-fullscreen-btn 的 click 事件
 * - 监听 fullscreenchange 事件，将状态写入/移除 localStorage
 * - 页面加载时检查 localStorage，恢复用户上次的偏好
 * - 所有 localStorage 操作包裹 try-catch，避免隐私模式下抛出异常
 */
function initHomeLayoutInteractions(): void {
  const btn = document.getElementById('home-fullscreen-btn');
  if (!btn) return;

  btn.addEventListener('click', () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      document.exitFullscreen().catch(() => {});
    }
  });

  // 监听全屏状态变化并持久化
  document.addEventListener('fullscreenchange', () => {
    if (document.fullscreenElement) {
      try {
        localStorage.setItem(FULLSCREEN_STORAGE_KEY, 'true');
      } catch {
        /* 隐私模式下 localStorage 不可用，静默处理 */
      }
    } else {
      try {
        localStorage.removeItem(FULLSCREEN_STORAGE_KEY);
      } catch {
        /* 同上 */
      }
    }
  });

  // 恢复全屏状态
  try {
    if (localStorage.getItem(FULLSCREEN_STORAGE_KEY) === 'true' && !document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    }
  } catch {
    /* localStorage 读取失败时静默处理 */
  }
}

// 初始化（首次加载与 View Transitions 后触发）
initHomeLayoutInteractions();
document.addEventListener('astro:page-load', initHomeLayoutInteractions);
