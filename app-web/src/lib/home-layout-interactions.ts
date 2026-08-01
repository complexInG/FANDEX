/**
 * 首页布局交互脚本
 * -----------------------------------------------------------------------------
 * 负责：
 * - 全屏模式切换（点击按钮进入/退出全屏）
 * - 全屏状态持久化（localStorage 记忆用户偏好）
 * - 页面加载时恢复全屏状态
 *
 * 触发时机：
 * - 脚本首次加载时执行一次
 * - astro:page-load 事件触发时重新绑定（支持 View Transitions 路由切换）
 *
 * 修复说明：
 * - 原实现每次 astro:page-load 都重复注册 fullscreenchange 监听器，导致累积
 * - 现使用模块级 fullscreenHandler 守卫，仅注册一次；click 通过 dataset.bound 去重
 */

/** localStorage 键名：用于持久化全屏状态 */
const FULLSCREEN_STORAGE_KEY = 'fandex-fullscreen';

/** fullscreenchange 回调（模块级单例，仅注册一次，防止累积） */
let fullscreenHandler: (() => void) | null = null;

/**
 * 初始化首页全屏切换交互
 */
function initHomeLayoutInteractions(): void {
  const btn = document.getElementById('home-fullscreen-btn');
  if (!btn) return;

  // click 监听通过 dataset.bound 去重，防止 View Transitions 后重复绑定
  if (btn.dataset.bound !== 'true') {
    btn.dataset.bound = 'true';
    btn.addEventListener('click', () => {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        document.exitFullscreen().catch(() => {});
      }
    });
  }

  // fullscreenchange 监听仅注册一次（document 持久存在，无需重复绑定）
  if (fullscreenHandler === null) {
    fullscreenHandler = () => {
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
    };
    document.addEventListener('fullscreenchange', fullscreenHandler);
  }

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
