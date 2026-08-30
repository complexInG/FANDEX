package com.fandex.app.ui.screens.syntax

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import com.fandex.app.FandexApp
import com.fandex.app.data.model.SyntaxIndex
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

/**
 * 语法速览 ViewModel
 *
 * 语言列表与统计来自预构建索引（syntax-index.json），顺序与 web 端一致
 */
class SyntaxViewModel(application: Application) : AndroidViewModel(application) {

    private val container = (application as FandexApp).container

    private val _index = MutableStateFlow<SyntaxIndex>(SyntaxIndex())
    val index: StateFlow<SyntaxIndex> = _index.asStateFlow()

    fun load() {
        viewModelScope.launch {
            _index.value = container.syntaxRepository.languages()
        }
    }
}
