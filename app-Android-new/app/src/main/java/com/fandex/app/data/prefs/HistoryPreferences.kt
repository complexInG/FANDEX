package com.fandex.app.data.prefs

import android.content.Context
import androidx.datastore.core.DataStore
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map
import kotlinx.serialization.Serializable
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json

private val Context.historyStore: DataStore<Preferences> by preferencesDataStore(name = "fandex_history")

/**
 * 阅读历史条目
 *
 * 记录最近浏览的文档，供首页"最近浏览"与搜索空态快捷入口使用
 */
@Serializable
data class HistoryEntry(
    val module: String,
    val slug: String,
    val title: String,
    /** 模块中文名（展示用，冗余存储避免每次回查元数据） */
    val moduleTitle: String = "",
    val timestamp: Long = 0
)

/**
 * 阅读历史存储
 *
 * 基于 DataStore 保存 JSON 列表：最新在前、按 module/slug 去重、上限 12 条
 */
class HistoryPreferences(private val context: Context) {

    private val json = Json { ignoreUnknownKeys = true }

    /** 历史列表流（最新在前） */
    val history: Flow<List<HistoryEntry>> = context.historyStore.data.map { prefs ->
        decode(prefs[KEY_HISTORY]).sortedByDescending { it.timestamp }
    }

    /**
     * 记录一次文档访问
     */
    suspend fun record(entry: HistoryEntry) {
        context.historyStore.edit { prefs ->
            val current = decode(prefs[KEY_HISTORY])
                .filterNot { it.module == entry.module && it.slug == entry.slug }
            val next = (listOf(entry) + current).take(MAX_ENTRIES)
            prefs[KEY_HISTORY] = json.encodeToString(next)
        }
    }

    /**
     * 清空历史
     */
    suspend fun clear() {
        context.historyStore.edit { prefs -> prefs.remove(KEY_HISTORY) }
    }

    private fun decode(raw: String?): List<HistoryEntry> {
        if (raw.isNullOrEmpty()) return emptyList()
        return runCatching { json.decodeFromString<List<HistoryEntry>>(raw) }.getOrDefault(emptyList())
    }

    companion object {
        private val KEY_HISTORY = stringPreferencesKey("doc_history")

        /** 历史上限：首页展示取前几条，存储多留余量 */
        const val MAX_ENTRIES = 12
    }
}
