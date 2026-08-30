/**
 * FANDEX 旧版 App（app-Android-old）内容生成脚本
 *
 * 从 cnt-content/full 与 shd-shared/metadata 生成旧版 App 的离线文档资源，
 * 替代原先随旧仓库维护的 dist-mobile 文档，使旧版 App 与主仓库内容源保持一致。
 *
 * 用法: node scripts/generate-legacy-content.mjs
 *
 * 生成内容:
 * 1. assets/dist-mobile/docs/{moduleId}/{docSlug}.md (从 cnt-content/full 复制并剥离 frontmatter，
 *    旧版渲染器基于 commonmark-java，不识别 YAML frontmatter，保留会产生渲染噪音)
 * 2. assets/dist-mobile/index.json (旧版 ContentIndex 结构：categories / modules / documents，
 *    分类与模块元数据取自 shd-shared/metadata/modules.json，文档标题等取自 frontmatter)
 */

import { readFileSync, writeFileSync, mkdirSync, readdirSync, rmSync, existsSync } from 'fs';
import { join, dirname, relative } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

// 项目根目录（scripts 上一级为 app-Android-old，再上一级为仓库根）
const ROOT = join(__dirname, '..', '..');
const DIST_MOBILE = join(ROOT, 'app-Android-old', 'app', 'src', 'main', 'assets', 'dist-mobile');

// 内容源
const CONTENT_DIR = join(ROOT, 'cnt-content', 'full');
const MODULES_META = join(ROOT, 'shd-shared', 'metadata', 'modules.json');

/**
 * 读取单个文档：返回 { slug, module, frontmatter 摘要, 正文 }，跳过 MERGED 合集
 */
function readDoc(filePath, moduleId, fileName) {
    const slug = fileName.replace(/\.md$/, '');
    if (slug.includes('MERGED')) return null;

    const content = readFileSync(filePath, 'utf-8');
    const fmRegex = /^---\s*\n([\s\S]*?)\n---\s*\n/;
    const fmMatch = content.match(fmRegex);

    let body = content;
    const fm = {};
    if (fmMatch !== null) {
        // 按 frontmatter 实际匹配长度截取正文，避免正文中的分隔线造成误判
        body = content.slice(fmMatch[0].length);
        // 简易逐行解析（键值 + 单层列表），仅取生成索引所需的标量字段
        for (const line of fmMatch[1].split('\n')) {
            const trimmed = line.trim();
            const colonIdx = trimmed.indexOf(':');
            if (colonIdx <= 0) continue;
            const key = trimmed.substring(0, colonIdx).trim();
            const value = trimmed.substring(colonIdx + 1).trim().replace(/^['"]|['"]$/g, '');
            // related / prerequisites 为列表字段，索引不需要，跳过
            if (key === 'related' || key === 'prerequisites') continue;
            if (value !== '') fm[key] = value;
        }
    }

    // 剥离 frontmatter 后去掉正文开头的空行，保持文档头部整洁
    body = body.replace(/^\s*\n/, '');

    return {
        slug,
        module: fm.module || moduleId,
        title: fm.title || slug,
        category: fm.category || '',
        difficulty: fm.difficulty || 'beginner',
        description: fm.description || '',
        order: parseInt(fm.order, 10) || 0,
        body
    };
}

/**
 * 主流程
 */
function main() {
    console.log('=== FANDEX 旧版 App 内容生成 ===');
    console.log(`输出目录: ${DIST_MOBILE}`);
    console.log(`内容源: ${CONTENT_DIR}`);

    const meta = JSON.parse(readFileSync(MODULES_META, 'utf-8'));

    // 清空旧的 docs 目录，避免残留已下线的模块或文档
    const docsDir = join(DIST_MOBILE, 'docs');
    rmSync(docsDir, { recursive: true, force: true });
    mkdirSync(docsDir, { recursive: true });

    const modules = [];
    const moduleOrders = [];
    const documents = [];
    let docCount = 0;

    for (const mod of meta.modules) {
        const moduleDir = join(CONTENT_DIR, mod.id);
        const srcDir = existsSync(moduleDir)
            ? moduleDir
            : join(CONTENT_DIR, mod.folder_order ? `${String(mod.folder_order).padStart(3, '0')}-${mod.id}` : mod.id);

        if (!existsSync(srcDir)) {
            console.log(`  [警告] 模块目录缺失，跳过: ${mod.id}`);
            continue;
        }

        const slugs = [];
        const orderBySlug = {};
        for (const fileName of readdirSync(srcDir).sort()) {
            if (!fileName.endsWith('.md')) continue;
            const doc = readDoc(join(srcDir, fileName), mod.id, fileName);
            if (!doc) continue;

            const destDir = join(docsDir, mod.id);
            if (!existsSync(destDir)) mkdirSync(destDir, { recursive: true });
            writeFileSync(join(destDir, `${doc.slug}.md`), doc.body, 'utf-8');

            slugs.push(doc.slug);
            orderBySlug[doc.slug] = doc.order;
            documents.push({
                slug: doc.slug,
                title: doc.title,
                module: mod.id,
                category: doc.category,
                difficulty: doc.difficulty,
                description: doc.description
            });
            docCount++;
        }

        modules.push({
            id: mod.id,
            title: mod.title,
            category: (mod.categories && mod.categories[0]) || '',
            description: mod.description || '',
            documents: slugs
        });
        moduleOrders.push(orderBySlug);
    }

    // 模块顺序与 modules.json 保持一致（folder_order），
    // 模块内文档按 frontmatter order 排序（与学习顺序一致）
    modules.forEach((m, i) => {
        const orders = moduleOrders[i];
        m.documents.sort((a, b) => (orders[a] || 0) - (orders[b] || 0));
    });

    // 旧版 ContentIndex 结构：分类沿用 modules.json 的语义分类与配色，
    // 仅保留仍有模块归属的分类，避免旧版首页出现空分类组
    const usedCategories = new Set(modules.map(m => m.category));
    const index = {
        version: meta.version || '',
        generatedAt: new Date().toISOString().slice(0, 10),
        categories: meta.categoryOrder
            .filter(id => usedCategories.has(id))
            .map(id => ({
            id,
            label: meta.categoryLabels[id] || id,
            color: meta.categoryColors[id] || '#4f5bd5'
        })),
        modules,
        documents
    };

    writeFileSync(join(DIST_MOBILE, 'index.json'), JSON.stringify(index, null, 4), 'utf-8');

    console.log(`  [完成] ${modules.length} 个模块 / ${docCount} 篇文档`);
    console.log(`  [生成] ${relative(ROOT, join(DIST_MOBILE, 'index.json'))}`);
    console.log('=== 生成结束 ===');
}

main();
