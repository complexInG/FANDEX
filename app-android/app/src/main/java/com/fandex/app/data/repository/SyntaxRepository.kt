package com.fandex.app.data.repository

import com.fandex.app.data.asset.AssetStore
import com.fandex.app.data.model.SyntaxIndex
import com.fandex.app.data.model.SyntaxModule
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import kotlinx.serialization.json.Json

/**
 * 语法速查仓库
 *
 * 对齐 app-web 的 syntax-service.ts：
 * - 语言索引（syntax-index.json）提供语言元数据与统计，缓存常驻
 * - 各语言卡片数据（syntax-data/{moduleId}.json）按需加载，不常驻内存
 */
class SyntaxRepository(private val assetStore: AssetStore) {

    /** 语言索引缓存 */
    @Volatile
    private var cachedIndex: SyntaxIndex? = null

    /** 卡片数据缓存（体量有限，语言切换频繁，可常驻） */
    @Volatile
    private var cachedModules: MutableMap<String, SyntaxModule>? = null

    private val indexMutex = Mutex()
    private val moduleMutex = Mutex()

    /** JSON 解码器：忽略未知字段，容忍宽松输入 */
    private val decoder = Json {
        ignoreUnknownKeys = true
        coerceInputValues = true
        isLenient = true
    }

    /**
     * 语言索引（缓存优先），语言顺序与 web 端构建顺序一致
     */
    suspend fun languages(): SyntaxIndex {
        cachedIndex?.let { return it }
        return indexMutex.withLock {
            cachedIndex ?: loadIndex().also { cachedIndex = it }
        }
    }

    /**
     * 加载单语言语法卡片数据（缓存优先）
     */
    suspend fun module(moduleId: String): SyntaxModule? {
        cachedModules?.get(moduleId)?.let { return it }
        return moduleMutex.withLock {
            val cache = cachedModules ?: mutableMapOf<String, SyntaxModule>().also { cachedModules = it }
            cache[moduleId] ?: loadModule(moduleId)?.also { cache[moduleId] = it }
        }
    }

    /**
     * 语法点卡片总数统计
     */
    suspend fun totalCards(): Int {
        return languages().languages.sumOf { it.count }
    }

    /**
     * 从 assets 加载语言索引
     */
    private suspend fun loadIndex(): SyntaxIndex {
        val json = assetStore.readText("metadata/syntax-index.json")
            ?: return SyntaxIndex()
        return runCatching { decoder.decodeFromString<SyntaxIndex>(json) }
            .getOrDefault(SyntaxIndex())
    }

    /**
     * 从 assets 加载单语言卡片数据
     */
    private suspend fun loadModule(moduleId: String): SyntaxModule? {
        val json = assetStore.readText("syntax-data/$moduleId.json") ?: return null
        return runCatching { decoder.decodeFromString<SyntaxModule>(json) }.getOrNull()
    }
}
