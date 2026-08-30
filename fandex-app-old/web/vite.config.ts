import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// FANDEX-App 下载页 Vite 配置
// 部署于 GitHub Pages 子路径 /FANDEX-App/，构建产物输出到仓库根 docs/ 目录
export default defineConfig({
  plugins: [react(), tailwindcss()],
  base: '/FANDEX-App/',
  build: {
    outDir: '../docs',
    emptyOutDir: true,
    target: 'es2022',
    cssMinify: 'lightningcss',
    rollupOptions: {
      output: {
        chunkFileNames: 'assets/[name]-[hash].js',
        entryFileNames: 'assets/[name]-[hash].js',
        assetFileNames: 'assets/[name]-[hash][extname]',
      },
    },
  },
})
