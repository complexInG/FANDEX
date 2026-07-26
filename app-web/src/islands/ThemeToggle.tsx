/**
 * 主题切换组件 (ThemeToggle)
 * ========================
 * 功能概述：
 * - 在亮色(light)和暗色(dark)模式之间切换
 * - 主题状态持久化到 localStorage（键名: fandex-theme），刷新页面后保持用户选择
 * - 首次访问时跟随系统偏好（prefers-color-scheme）
 * - SSR 阶段渲染不可见占位按钮（保留布局空间避免 CLS），
 *   客户端挂载后填充实际图标，避免水合后布局偏移
 *
 * 动效体系（Motion React + View Transitions API）：
 * - MotionProvider 包裹，reducedMotion="user" 自动降级
 * - motion.button：whileTap 按压回弹、whileHover 轻微放大（ark 微交互）
 * - AnimatePresence + motion.svg：日/月图标旋转交叉淡入淡出
 * - View Transitions API：主题切换时圆形扩散动画，从按钮位置向外展开
 *   不支持 VT 或 prefers-reduced-motion 时降级为直接切换
 *
 * 数据流：
 * - 挂载时从 localStorage 读取已保存的主题，无保存值时检测系统偏好
 * - 切换时同步更新：theme(state) → document.documentElement data-theme 属性 → localStorage
 * - 通过 data-theme 属性驱动全局 CSS 变量切换（在全局样式中定义）
 *
 * 使用场景：
 * - 放置在页面顶部导航栏，作为全局主题控制入口
 * - 配合 Astro 群岛架构，仅客户端交互
 */
import { useState, useEffect, useCallback, useRef } from 'react';
import { flushSync } from 'react-dom';
import { motion, AnimatePresence } from 'motion/react';
import { MotionProvider } from '@/motion';
import { getSavedTheme, prefersDarkMode, setTheme as persistTheme, type Theme } from '@/lib/theme';
import '@/styles/islands/ThemeToggle.css';

/**
 * View Transitions API 类型补充
 * 标准 DOM 类型库可能未包含此接口，此处声明用到的子集
 */
interface ViewTransition {
  readonly ready: Promise<void>;
  readonly finished: Promise<void>;
  readonly updateCallbackDone: Promise<void>;
  skipTransition: () => void;
}

interface ViewTransitionDocument {
  startViewTransition: (callback: () => void) => ViewTransition;
}

/**
 * 组件 props 接口
 * ThemeToggle 无外部 props，定义空接口以保持组件接口一致性
 */
interface ThemeToggleProps {}

/**
 * 主题切换组件
 * 在亮色与暗色模式间切换，状态持久化到 localStorage
 * 支持 View Transitions API 圆形扩散过渡动画
 */
export function ThemeToggle({}: ThemeToggleProps = {}) {
  /**
   * 当前主题状态：'light' 亮色 | 'dark' 暗色
   * 初始值为 'light'，在 useEffect 中根据 localStorage 或系统偏好修正
   */
  const [theme, setTheme] = useState<'light' | 'dark'>('light');

  /**
   * 是否已完成客户端挂载
   * 用于控制图标的可见性：
   * - SSR 阶段渲染透明占位按钮（保留 32x32 布局空间，CLS=0）
   * - 客户端挂载后通过 opacity 平滑显示图标
   */
  const [mounted, setMounted] = useState(false);

  /**
   * 按钮元素引用
   * 用于获取按钮位置，作为 View Transition 圆形扩散动画的起点
   */
  const buttonRef = useRef<HTMLButtonElement>(null);

  /**
   * 组件挂载后的初始化逻辑
   * 1. 标记已挂载，触发图标淡入
   * 2. 从 localStorage 读取用户保存的主题偏好
   * 3. 如果没有保存值，则检测系统暗色模式偏好
   * 4. 根据结果设置 theme 值，并同步刷新 data-theme 属性与 colorScheme
   *    （作为 BaseLayout 初始化脚本的二次保险：当组件被重新挂载、
   *    或初始化脚本因故未执行时，确保 data-theme 始终处于显式声明状态，
   *    避免 tokens.css 的 :root:not([data-theme]) 兜底逻辑误覆盖用户选择）
   */
  useEffect(() => {
    // 通过统一主题模块读取已保存的主题偏好，无保存值时跟随系统
    const saved = getSavedTheme();
    const initial: Theme = saved ?? (prefersDarkMode() ? 'dark' : 'light');
    setTheme(initial);
    // 同步显式声明 data-theme，消除"无属性"中间态
    // 作为 BaseLayout 内联脚本的二次保险（FOUC 四层防护 · 第四层）
    document.documentElement.setAttribute('data-theme', initial);
    document.documentElement.style.colorScheme = initial;
    // 下一帧标记挂载完成，触发 opacity 过渡（避免初始渲染闪烁）
    const rafId = requestAnimationFrame(() => {
      setMounted(true);
    });
    return () => {
      cancelAnimationFrame(rafId);
    };
  }, []);

  /**
   * 切换主题并持久化到 localStorage
   *
   * View Transitions 过渡动画流程：
   * 1. 检测浏览器支持 startViewTransition 且用户未启用 prefers-reduced-motion
   * 2. 获取按钮位置作为圆形扩散起点
   * 3. 启动 View Transition，在回调中同步更新 DOM 与 React 状态
   *    （flushSync 确保 React 状态同步刷新，使图标变化被 VT 捕获）
   * 4. transition.ready 后对 ::view-transition-new(root) 执行 clipPath 圆形展开动画
   * 5. 动画完成后移除过渡标记类
   *
   * 降级策略：
   * - 不支持 View Transitions API：直接切换 DOM 与状态，无过渡动画
   * - prefers-reduced-motion: reduce：直接切换，避免触发动画
   */
  const toggle = useCallback(async () => {
    const next: Theme = theme === 'dark' ? 'light' : 'dark';

    /**
     * 应用主题到 DOM 与 localStorage
     * 使用统一主题模块确保 meta theme-color 同步更新
     */
    const applyThemeFn = () => {
      persistTheme(next);
    };

    // 检测 View Transitions API 支持与用户动效偏好
    const vtDocument = document as Document & Partial<ViewTransitionDocument>;
    const supportsVT = typeof vtDocument.startViewTransition === 'function';
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // 不支持 VT 或用户偏好减少动效：直接切换，无过渡
    if (!supportsVT || reduceMotion) {
      applyThemeFn();
      setTheme(next);
      return;
    }

    // 获取按钮位置作为圆形扩散动画起点
    const button = buttonRef.current;
    let cx = window.innerWidth / 2;
    let cy = window.innerHeight / 2;
    if (button) {
      const rect = button.getBoundingClientRect();
      cx = rect.left + rect.width / 2;
      cy = rect.top + rect.height / 2;
    }

    // 计算圆形展开最大半径（到屏幕最远角的距离，确保完全覆盖视口）
    const maxRadius = Math.hypot(
      Math.max(cx, window.innerWidth - cx),
      Math.max(cy, window.innerHeight - cy),
    );

    // 添加过渡标记类，使 CSS 中 ::view-transition-* 规则生效
    document.documentElement.classList.add('theme-vt');

    const transition = vtDocument.startViewTransition(() => {
      applyThemeFn();
      // flushSync 确保 React 状态同步更新，图标变化被 VT 捕获
      flushSync(() => {
        setTheme(next);
      });
    });

    try {
      // 等待 VT 伪元素就绪后执行自定义圆形展开动画
      await transition.ready;

      document.documentElement.animate(
        {
          clipPath: [
            `circle(0px at ${cx}px ${cy}px)`,
            `circle(${maxRadius}px at ${cx}px ${cy}px)`,
          ],
        },
        {
          // duration 从 380ms 调至 250ms，提升主题切换响应感
          // 380ms 偏长导致切换迟缓，250ms 接近 --motion-duration-normal，手感更跟手
          duration: 250,
          easing: 'cubic-bezier(0.4, 0, 0.2, 1)',
          pseudoElement: '::view-transition-new(root)',
        },
      );

      await transition.finished;
    } catch {
      // 过渡被跳过或中断（如用户快速连续点击），安全降级
      // 此时 DOM 已在回调中更新完毕，无需额外处理
    } finally {
      // 移除过渡标记类，恢复默认 VT 行为（避免影响 Astro 页面导航过渡）
      document.documentElement.classList.remove('theme-vt');
    }
  }, [theme]);

  return (
    /*
     * MotionProvider 包裹：统一 reduced-motion 降级策略
     * 始终渲染按钮以保留布局空间（避免水合后 CLS）：
     * - SSR 阶段：按钮透明不可点击（mounted=false）
     * - 客户端挂载后：opacity 过渡到 1，pointer-events 启用
     * - whileTap/whileHover 由 Motion 驱动微交互（ark: 直接交互 150ms）
     */
    <MotionProvider>
      <motion.button
        ref={buttonRef}
        className={`fndx-theme-toggle${mounted ? ' fndx-theme-toggle--ready' : ''}`}
        onClick={mounted ? toggle : undefined}
        data-tooltip={theme === 'dark' ? '亮色模式' : '暗色模式'}
        data-tooltip-pos="bottom"
        aria-label={theme === 'dark' ? '切换到亮色模式' : '切换到暗色模式'}
        tabIndex={mounted ? 0 : -1}
        aria-hidden={!mounted}
        whileTap={{ scale: 0.85 }}
        whileHover={{ scale: 1.08 }}
      >
        {/*
          AnimatePresence mode="wait"：日/月图标依次旋转交叉切换
          - 旧图标先旋转淡出，再淡入新图标，避免叠加错位
          - initial={false}：首挂载不播放入场（由容器 CSS opacity 接管淡入）
        */}
        <AnimatePresence mode="wait" initial={false}>
          {/* 暗色模式下显示太阳图标（提示用户可切换到亮色） */}
          {mounted && theme === 'dark' && (
            <motion.svg
              key="sun"
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2.5"
              initial={{ opacity: 0, rotate: -90, scale: 0.5 }}
              animate={{ opacity: 1, rotate: 0, scale: 1 }}
              exit={{ opacity: 0, rotate: 90, scale: 0.5 }}
              transition={{ duration: 0.2, ease: [0, 0, 0.2, 1] }}
            >
              <circle cx="12" cy="12" r="5" />
              <line x1="12" y1="1" x2="12" y2="3" />
              <line x1="12" y1="21" x2="12" y2="23" />
              <line x1="4.22" y1="4.22" x2="5.64" y2="5.64" />
              <line x1="18.36" y1="18.36" x2="19.78" y2="19.78" />
              <line x1="1" y1="12" x2="3" y2="12" />
              <line x1="21" y1="12" x2="23" y2="12" />
              <line x1="4.22" y1="19.78" x2="5.64" y2="18.36" />
              <line x1="18.36" y1="5.64" x2="19.78" y2="4.22" />
            </motion.svg>
          )}
          {/* 亮色模式下显示月亮图标（提示用户可切换到暗色） */}
          {mounted && theme === 'light' && (
            <motion.svg
              key="moon"
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2.5"
              initial={{ opacity: 0, rotate: 90, scale: 0.5 }}
              animate={{ opacity: 1, rotate: 0, scale: 1 }}
              exit={{ opacity: 0, rotate: -90, scale: 0.5 }}
              transition={{ duration: 0.2, ease: [0, 0, 0.2, 1] }}
            >
              <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
            </motion.svg>
          )}
        </AnimatePresence>
      </motion.button>
    </MotionProvider>
  );
}

export default ThemeToggle;
