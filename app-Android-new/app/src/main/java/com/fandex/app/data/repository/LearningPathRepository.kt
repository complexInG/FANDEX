package com.fandex.app.data.repository

import com.fandex.app.data.asset.AssetStore
import com.fandex.app.data.model.LearningPath
import com.fandex.app.data.model.LearningPathIndex
import com.fandex.app.data.model.LearningPathSummary
import kotlinx.coroutines.async
import kotlinx.coroutines.awaitAll
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import kotlinx.serialization.json.Json
import java.util.concurrent.ConcurrentHashMap

/**
 * 学习路径仓库
 *
 * 对齐 app-web /learning-path 数据源：
 * - index.json 的 order 数组给出路径顺序
 * - 路径标题、描述由模块元数据补充（单一路径文件不含展示字段）
 *
 * 性能：路径列表页需要全量路径的阶段数，此处以并发方式批量加载缺失的
 * 路径 JSON（约 40 个文件），避免逐个串行读取造成列表长时间转圈
 */
class LearningPathRepository(
    private val assetStore: AssetStore,
    private val moduleRepository: ModuleRepository
) {

    /** 索引缓存 */
    @Volatile
    private var cachedIndex: LearningPathIndex? = null

    /** 路径详情缓存（并发安全；单个条目加载由 pathMutex 串行去重） */
    private val pathCache = ConcurrentHashMap<String, LearningPath>()

    /** 同一路径的并发加载去重 */
    private val pathMutex = Mutex()

    private val indexMutex = Mutex()

    /** JSON 解码器：忽略未知字段，容忍宽松输入 */
    private val decoder = Json {
        ignoreUnknownKeys = true
        coerceInputValues = true
        isLenient = true
    }

    /**
     * 学习路径列表
     *
     * 按 index.json 的 order 顺序组合模块元数据；索引缺失时回退为模块全量列表。
     * 阶段数统计所需的路径文件在此处并发预加载（各自独立文件，直接并发读取
     * 后写入 ConcurrentHashMap，不经过单条互斥锁以免串行化）
     */
    suspend fun paths(): List<LearningPathSummary> = coroutineScope {
        val metadata = moduleRepository.metadata()
        val byId = metadata.modules.associateBy { it.id }
        val index = indexPath()
        val orderedIds = index.order.ifEmpty { byId.keys.toList() }

        // 并发补齐缺失的路径详情
        orderedIds.filter { !pathCache.containsKey(it) }
            .map { id -> async { id to loadPath(id) } }
            .awaitAll()
            .forEach { (id, path) -> if (path != null) pathCache[id] = path }

        orderedIds.mapNotNull { moduleId ->
            byId[moduleId]?.let { module ->
                val accent = module.categories.firstOrNull()
                    ?.let { metadata.categoryColors[it] } ?: "#4F5BD5"
                LearningPathSummary(
                    moduleId = module.id,
                    title = module.title,
                    description = module.description,
                    stageCount = pathCache[moduleId]?.stages?.size ?: 0,
                    colorHex = accent
                )
            }
        }
    }

    /**
     * 单条学习路径详情（缓存优先）
     */
    suspend fun path(moduleId: String): LearningPath? = loadPathCached(moduleId)

    /**
     * 带并发去重的路径加载
     */
    private suspend fun loadPathCached(moduleId: String): LearningPath? {
        pathCache[moduleId]?.let { return it }
        return pathMutex.withLock {
            pathCache[moduleId] ?: loadPath(moduleId)?.also { pathCache[moduleId] = it }
        }
    }

    /**
     * 从 assets 加载路径索引
     */
    private suspend fun indexPath(): LearningPathIndex {
        cachedIndex?.let { return it }
        return indexMutex.withLock {
            cachedIndex ?: loadIndex().also { cachedIndex = it }
        }
    }

    private suspend fun loadIndex(): LearningPathIndex {
        val json = assetStore.readText("metadata/learning-path/index.json")
            ?: return LearningPathIndex()
        return runCatching { decoder.decodeFromString<LearningPathIndex>(json) }
            .getOrDefault(LearningPathIndex())
    }

    private suspend fun loadPath(moduleId: String): LearningPath? {
        val json = assetStore.readText("metadata/learning-path/$moduleId.json") ?: return null
        return runCatching { decoder.decodeFromString<LearningPath>(json) }.getOrNull()
    }
}
