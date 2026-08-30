package com.fandex.app.data.repository

import com.fandex.app.data.asset.AssetStore
import com.fandex.app.data.model.DocFrontmatter
import com.fandex.app.data.model.DocIndexEntry
import com.fandex.app.data.model.FandexDoc
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import kotlinx.serialization.json.Json

/**
 * 文档仓库
 *
 * 对齐 app-web 的 doc-service.ts：
 * - 全量文档索引缓存
 * - 文档正文加载与 frontmatter 解析
 * - 上下篇导航 / 相关文档 / 前置知识解析（跨模块）
 * - 标题、描述与模块名全文搜索
 * - 阅读时长估算（与 lib/reading-time.ts 同一公式）
 */
class DocRepository(private val assetStore: AssetStore) {

    /** 索引缓存 */
    @Volatile
    private var cachedIndex: List<DocIndexEntry>? = null

    private val mutex = Mutex()

    /** JSON 解码器：忽略未知字段，容忍宽松输入 */
    private val decoder = Json {
        ignoreUnknownKeys = true
        coerceInputValues = true
        isLenient = true
    }

    /**
     * 全量文档索引（缓存优先）
     */
    suspend fun docIndex(): List<DocIndexEntry> {
        cachedIndex?.let { return it }
        return mutex.withLock {
            cachedIndex ?: loadIndex().also { cachedIndex = it }
        }
    }

    /**
     * 加载模块下文档列表（按 order 升序，与学习顺序一致）
     */
    suspend fun docsByModule(moduleId: String): List<DocIndexEntry> {
        return docIndex().filter { it.module == moduleId }.sortedBy { it.order }
    }

    /**
     * 模块最新一篇文档（order 最大，供"继续阅读"直达）
     */
    suspend fun latestDocOf(moduleId: String): DocIndexEntry? {
        return docIndex().filter { it.module == moduleId }.maxByOrNull { it.order }
    }

    /**
     * 按索引条目加载单个模块文档
     */
    suspend fun doc(entry: DocIndexEntry): FandexDoc? {
        return doc(entry.module, entry.slug)
    }

    /**
     * 加载单个文档正文并解析 frontmatter
     */
    suspend fun doc(moduleId: String, docSlug: String): FandexDoc? {
        val path = "docs/$moduleId/$docSlug.md"
        val content = assetStore.readText(path) ?: return null
        return parseMarkdown(content, docSlug)
    }

    /**
     * 上下篇导航（对齐 getDocNavigation）
     *
     * 以模块内文档 order 顺序为基准
     */
    suspend fun navigation(moduleId: String, docSlug: String): Pair<DocIndexEntry?, DocIndexEntry?> {
        val moduleDocs = docsByModule(moduleId)
        val index = moduleDocs.indexOfFirst { it.slug == docSlug }
        if (index < 0) return null to null
        val prev = if (index > 0) moduleDocs[index - 1] else null
        val next = if (index < moduleDocs.size - 1) moduleDocs[index + 1] else null
        return prev to next
    }

    /**
     * 相关文档（对齐 getRelatedDocs）
     *
     * frontmatter related 引用格式为 module/文件名 或裸文件名，
     * 在全量索引中解析（支持跨模块引用），保持索引顺序
     */
    suspend fun relatedDocs(moduleId: String, docSlug: String): List<DocIndexEntry> {
        val current = docsByModule(moduleId).find { it.slug == docSlug } ?: return emptyList()
        val doc = doc(current) ?: return emptyList()
        val refs = doc.frontmatter.related
        if (refs.isEmpty()) return emptyList()

        val refSet = refs.toSet()
        return docIndex().filter { entry ->
            val fullRef = "${entry.module}/${entry.slug}"
            refSet.contains(entry.slug) || refSet.contains(fullRef)
        }
    }

    /**
     * 前置知识文档
     *
     * frontmatter prerequisites 引用格式与 related 一致，跨模块解析
     */
    suspend fun prerequisites(moduleId: String, docSlug: String): List<DocIndexEntry> {
        val current = docsByModule(moduleId).find { it.slug == docSlug } ?: return emptyList()
        val doc = doc(current) ?: return emptyList()
        val refs = doc.frontmatter.prerequisites
        if (refs.isEmpty()) return emptyList()

        val refSet = refs.toSet()
        return docIndex().filter { entry ->
            val fullRef = "${entry.module}/${entry.slug}"
            refSet.contains(entry.slug) || refSet.contains(fullRef)
        }
    }

    /**
     * 搜索文档
     *
     * 匹配标题、描述、模块 ID 与模块中文标题（模块名匹配需传入模块标题表）
     */
    suspend fun search(query: String, moduleTitles: Map<String, String> = emptyMap()): List<DocIndexEntry> {
        val lowerQuery = query.lowercase().trim()
        if (lowerQuery.isEmpty()) return emptyList()
        return docIndex().filter { entry ->
            entry.title.lowercase().contains(lowerQuery) ||
                entry.description.lowercase().contains(lowerQuery) ||
                entry.module.lowercase().contains(lowerQuery) ||
                moduleTitles[entry.module]?.lowercase()?.contains(lowerQuery) == true
        }
    }

    /**
     * 站点统计（首页展示）
     */
    suspend fun stats(): DocStats {
        val index = docIndex()
        return DocStats(
            docCount = index.size,
            moduleCount = index.map { it.module }.distinct().size
        )
    }

    /**
     * 从 assets 加载索引
     */
    private suspend fun loadIndex(): List<DocIndexEntry> {
        val json = assetStore.readTextOrThrow("metadata/doc-index.json")
        return decoder.decodeFromString<List<DocIndexEntry>>(json)
            .sortedWith(compareBy({ it.module }, { it.order }))
    }

    /**
     * 解析 Markdown：分离 frontmatter（YAML）与正文
     */
    private fun parseMarkdown(content: String, slug: String): FandexDoc {
        val frontmatterRegex = Regex("""^---\s*\n(.*?)\n---\s*\n""", RegexOption.DOT_MATCHES_ALL)
        val match = frontmatterRegex.find(content)

        if (match == null) {
            return FandexDoc(
                slug = slug,
                frontmatter = DocFrontmatter(title = slug),
                content = content
            )
        }

        val body = content.substring(match.range.last + 1).trim()
        return FandexDoc(
            slug = slug,
            frontmatter = parseFrontmatter(match.groupValues[1], slug),
            content = body
        )
    }

    /**
     * 简易 YAML frontmatter 解析
     *
     * 覆盖 FANDEX 标准 10 字段：order, title, module, category, difficulty,
     * description, author, updated, related, prerequisites
     */
    private fun parseFrontmatter(yaml: String, slug: String): DocFrontmatter {
        var order = 0
        var title = slug
        var module = ""
        var category = ""
        var difficulty = "beginner"
        var description = ""
        var author = "fanquanpp"
        var updated = ""
        val related = mutableListOf<String>()
        val prerequisites = mutableListOf<String>()

        var currentList: MutableList<String>? = null

        for (rawLine in yaml.split("\n")) {
            val trimmed = rawLine.trim()
            if (trimmed.isEmpty()) continue

            // 处理列表项（related / prerequisites 的 "- 'module/文件名'" 行）
            if (currentList != null && trimmed.startsWith("- ")) {
                currentList.add(trimmed.removePrefix("- ").trim().trim('\'', '"'))
                continue
            }
            currentList = null

            val colonIndex = trimmed.indexOf(':')
            if (colonIndex <= 0) continue

            val key = trimmed.substring(0, colonIndex).trim()
            val value = trimmed.substring(colonIndex + 1).trim().trim('\'', '"')

            when (key) {
                "order" -> order = value.toIntOrNull() ?: 0
                "title" -> title = value
                "module" -> module = value
                "category" -> category = value
                "difficulty" -> difficulty = value
                "description" -> description = value
                "author" -> author = value
                "updated" -> updated = value
                "related" -> if (value.isEmpty()) currentList = related
                "prerequisites" -> if (value.isEmpty()) currentList = prerequisites
            }
        }

        return DocFrontmatter(
            order = order,
            title = title,
            module = module,
            category = category,
            difficulty = difficulty,
            description = description,
            author = author,
            updated = updated,
            related = related,
            prerequisites = prerequisites
        )
    }
}

/**
 * 站点统计信息
 */
data class DocStats(
    val docCount: Int,
    val moduleCount: Int
)

/**
 * 阅读时长估算
 *
 * 与 app-web lib/reading-time.ts 保持同一公式：
 * 去除代码块与 Markdown 标记后，按非空白字符数 / 300 估算分钟数
 */
object ReadingTime {

    /**
     * 计算预计阅读时长（分钟，最少 1 分钟）
     *
     * @param body Markdown 正文
     */
    fun compute(body: String): Int {
        val stripped = body
            .replace(Regex("```[\\s\\S]*?```"), "")
            .replace(Regex("[#*`~\\[\\]()>_\\-!|]"), "")
        val chars = stripped.replace(Regex("\\s"), "").length
        return maxOf(1, ceilDiv(chars, 300))
    }

    /** 正整数向上取整除法（避免浮点） */
    private fun ceilDiv(a: Int, b: Int): Int = (a + b - 1) / b
}
