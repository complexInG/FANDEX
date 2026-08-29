/**
 * FANDEX-App 下载页根组件
 * 技术栈:React 19 + Vite 8 + TypeScript 6 + Tailwind CSS v4
 * 美术风格:对齐 FANDEX-Web 设计系统(Sky 天蓝 + Teal 蓝绿 + Amber 琥珀 + Slate 石板灰)
 * 部署:GitHub Pages 子路径 /FANDEX-App/,构建产物输出到仓库根 docs/ 目录
 */
import { useState, useEffect, useCallback } from 'react';
import { Navbar } from './components/Navbar';
import { Hero } from './components/Hero';
import { DownloadSection } from './components/DownloadSection';
import { ModuleMatrix } from './components/ModuleMatrix';
import { Footer } from './components/Footer';
import { NoticeModal } from './components/NoticeModal';
import { useTheme } from './hooks/useTheme';

const NOTICE_STORAGE_KEY = 'fandex-notice-ack';

function App() {
  const { theme, toggle } = useTheme();
  const [noticeOpen, setNoticeOpen] = useState(false);

  // 首次进入自动弹出:同会话已确认则不再自动弹出
  // 铃铛点击不受此限制,可随时再次唤起
  useEffect(() => {
    let autoShow = true;
    try {
      if (sessionStorage.getItem(NOTICE_STORAGE_KEY) === '1') autoShow = false;
    } catch {
      // 隐私模式或存储禁用:默认自动弹出
    }
    if (autoShow) {
      const timer = window.setTimeout(() => setNoticeOpen(true), 500);
      return () => window.clearTimeout(timer);
    }
    return undefined;
  }, []);

  const handleOpenNotice = useCallback(() => setNoticeOpen(true), []);
  const handleCloseNotice = useCallback(() => {
    setNoticeOpen(false);
    try {
      sessionStorage.setItem(NOTICE_STORAGE_KEY, '1');
    } catch {
      // 忽略存储禁用场景
    }
  }, []);

  return (
    <>
      <Navbar
        theme={theme}
        onToggleTheme={toggle}
        onOpenNotice={handleOpenNotice}
      />
      <main className="flex-1">
        <Hero />
        <DownloadSection />
        <ModuleMatrix />
      </main>
      <Footer />
      <NoticeModal open={noticeOpen} onClose={handleCloseNotice} />
    </>
  );
}

export default App;
