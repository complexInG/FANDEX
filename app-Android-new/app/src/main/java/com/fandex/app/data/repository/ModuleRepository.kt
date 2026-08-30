package com.fandex.app.data.repository

import com.fandex.app.data.asset.AssetStore
import com.fandex.app.data.model.CategoryInfo
import com.fandex.app.data.model.Module
import com.fandex.app.data.model.ModulesMetadata
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import kotlinx.serialization.json.Json

/**
 * 模块仓库
 *
 * 对齐 app-web 的 module-service.ts：
 * 提供模块元数据与按分类组织的视图，元数据进程内单份缓存
 */
class ModuleRepository(private val assetStore: AssetStore) {

    /** 元数据缓存 */
    @Volatile
    private var cachedMetadata: ModulesMetadata? = null

    private val mutex = Mutex()

    /**
     * 加载模块元数据（缓存优先）
     */
    suspend fun metadata(): ModulesMetadata {
        cachedMetadata?.let { return it }
        return mutex.withLock {
            cachedMetadata ?: loadMetadata().also { cachedMetadata = it }
        }
    }

    /**
     * 获取分类列表
     *
     * 按 categoryOrder 排序，每个分类包含其下模块列表（按 folderOrder 排序）
     */
    suspend fun categories(): List<CategoryInfo> {
        val metadata = metadata()
        return metadata.categoryOrder.map { categoryId ->
            CategoryInfo(
                id = categoryId,
                label = metadata.categoryLabels[categoryId] ?: categoryId,
                colorHex = metadata.categoryColors[categoryId] ?: DEFAULT_COLOR,
                modules = metadata.modules
                    .filter { it.categories.contains(categoryId) }
                    .sortedBy { it.folderOrder }
            )
        }.filter { it.modules.isNotEmpty() }
    }

    /**
     * 获取单个模块
     */
    suspend fun module(moduleId: String): Module? {
        return metadata().modules.find { it.id == moduleId }
    }

    /**
     * 模块主分类色（categories 第一个分类对应的十六进制色值）
     *
     * 供子级页面的辅助装饰使用多彩分类色
     */
    suspend fun categoryColorHex(moduleId: String): String? {
        val metadata = metadata()
        val module = metadata.modules.find { it.id == moduleId } ?: return null
        val primaryCategory = module.categories.firstOrNull() ?: return null
        return metadata.categoryColors[primaryCategory]
    }

    /**
     * 从 assets 加载并解析元数据
     */
    private suspend fun loadMetadata(): ModulesMetadata {
        val json = assetStore.readTextOrThrow("metadata/modules.json")
        return decoder.decodeFromString(json)
    }

    companion object {
        /** 分类默认色（元数据缺失时兜底） */
        private const val DEFAULT_COLOR = "#4E5E6B"
    }

    /** JSON 解码器：忽略未知字段，容忍宽松输入 */
    private val decoder = Json {
        ignoreUnknownKeys = true
        coerceInputValues = true
        isLenient = true
    }
}
