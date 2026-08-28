package com.fandex.app.ui.screens.search

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import com.fandex.app.FandexApp
import com.fandex.app.data.model.DocIndexEntry
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

/**
 * 搜索 ViewModel
 *
 * 输入防抖 300ms 后在文档索引中检索，
 * 匹配范围：文档标题 / 描述 / 模块 ID / 模块中文标题
 */
class SearchViewModel(application: Application) : AndroidViewModel(application) {

    private val container = (application as FandexApp).container

    private val _query = MutableStateFlow("")
    val query: StateFlow<String> = _query.asStateFlow()

    private val _results = MutableStateFlow<List<DocIndexEntry>>(emptyList())
    val results: StateFlow<List<DocIndexEntry>> = _results.asStateFlow()

    private val _isSearching = MutableStateFlow(false)
    val isSearching: StateFlow<Boolean> = _isSearching.asStateFlow()

    /** 模块 ID -> 中文名（搜索结果归属标签） */
    private val _moduleTitles = MutableStateFlow<Map<String, String>>(emptyMap())
    val moduleTitles: StateFlow<Map<String, String>> = _moduleTitles.asStateFlow()

    private var searchJob: Job? = null

    init {
        // 模块标题表预加载（模块元数据带内存缓存，开销可忽略）
        viewModelScope.launch {
            _moduleTitles.value = container.moduleRepository.metadata()
                .modules.associate { it.id to it.title }
        }
    }

    fun updateQuery(newQuery: String) {
        _query.value = newQuery
        searchJob?.cancel()
        if (newQuery.isBlank()) {
            _results.value = emptyList()
            _isSearching.value = false
            return
        }
        searchJob = viewModelScope.launch {
            // 输入防抖，避免高频 keystroke 触发检索
            delay(300)
            _isSearching.value = true
            try {
                _results.value = container.docRepository.search(newQuery, _moduleTitles.value)
            } finally {
                _isSearching.value = false
            }
        }
    }
}
