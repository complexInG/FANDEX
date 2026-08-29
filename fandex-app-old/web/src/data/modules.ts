/**
 * FANDEX-App 模块矩阵数据
 * 数据源：android/app/src/main/assets/dist-mobile/index.json (v3.5.0)
 * 统计：22 唯一模块 / 313 篇文档 / modules 数组 24 条（含 HTML5+SVG 跨分类副本）
 */

export interface FandexModule {
  id: string;
  title: string;
  category: string;
  docCount: number;
}

export interface FandexCategory {
  id: string;
  label: string;
  color: string;
  modules: FandexModule[];
}

/** 模块原始数据（22 唯一模块，去重跨分类副本） */
const moduleData: FandexModule[] = [
  { id: 'c', title: 'C语言', category: 'languages', docCount: 15 },
  { id: 'cpp', title: 'C++', category: 'languages', docCount: 15 },
  { id: 'csharp', title: 'C#', category: 'languages', docCount: 8 },
  { id: 'go', title: 'Go', category: 'languages', docCount: 10 },
  { id: 'java', title: 'Java', category: 'languages', docCount: 15 },
  { id: 'javascript', title: 'JavaScript', category: 'languages', docCount: 15 },
  { id: 'kotlin', title: 'Kotlin', category: 'languages', docCount: 13 },
  { id: 'lua', title: 'Lua', category: 'languages', docCount: 10 },
  { id: 'python', title: 'Python', category: 'languages', docCount: 16 },
  { id: 'typescript', title: 'TypeScript', category: 'languages', docCount: 12 },
  { id: 'harmonyos', title: 'HarmonyOS', category: 'languages', docCount: 20 },
  { id: 'css', title: 'CSS', category: 'frontend', docCount: 16 },
  { id: 'html5', title: 'HTML5', category: 'markup', docCount: 29, },
  { id: 'html5-fe', title: 'HTML5', category: 'frontend', docCount: 29 },
  { id: 'svg', title: 'SVG', category: 'markup', docCount: 18 },
  { id: 'svg-fe', title: 'SVG', category: 'frontend', docCount: 18 },
  { id: 'react', title: 'React', category: 'frontend', docCount: 15 },
  { id: 'vue3', title: 'Vue3', category: 'frontend', docCount: 20 },
  { id: 'mysql', title: 'MySQL', category: 'database', docCount: 10 },
  { id: 'postgresql', title: 'PostgreSQL', category: 'database', docCount: 8 },
  { id: 'redis', title: 'Redis', category: 'database', docCount: 10 },
  { id: 'sql', title: 'SQL', category: 'database', docCount: 15 },
  { id: 'git', title: 'Git', category: 'tools', docCount: 10 },
  { id: 'markdown', title: 'Markdown', category: 'markup', docCount: 12 },
];

/** 分类元信息 */
const categoryMeta: Record<string, { label: string; color: string }> = {
  languages: { label: '编程语言', color: '#4f5bd5' },
  frontend: { label: '前端技术', color: '#d63031' },
  database: { label: '数据库', color: '#00b894' },
  tools: { label: '工具链', color: '#8854d0' },
  markup: { label: '标记语言', color: '#6c5ce7' },
};

/** 按分类组织的模块矩阵 */
export const categories: FandexCategory[] = Object.entries(categoryMeta).map(
  ([id, meta]) => ({
    id,
    label: meta.label,
    color: meta.color,
    modules: moduleData.filter((m) => m.category === id),
  }),
);

/** 统计汇总 */
export const stats = {
  /** 唯一模块数（去重跨分类副本） */
  uniqueModuleCount: 22,
  /** modules 数组总条目数（含跨分类副本） */
  moduleEntries: 24,
  /** 文档总数（按唯一模块统计） */
  totalDocuments: 313,
  /** 分类数 */
  categoryCount: 5,
};
