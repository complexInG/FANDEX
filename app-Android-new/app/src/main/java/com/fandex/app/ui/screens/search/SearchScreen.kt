package com.fandex.app.ui.screens.search

import androidx.compose.animation.Crossfade
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.Search
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.material3.TextFieldDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.fandex.app.ui.common.fandexEntrance
import com.fandex.app.ui.common.tweenNormal
import com.fandex.app.ui.components.DocListItem
import com.fandex.app.ui.components.ThemeQuickToggle
import com.fandex.app.ui.components.TopDock
import com.fandex.app.ui.theme.LocalExtendedColors

/** 搜索结果区阶段（供 Crossfade 切换） */
private enum class SearchPhase { SEARCHING, EMPTY, CONTENT }

/**
 * 搜索页
 *
 * 对齐 Web 端搜索功能：
 * - 搜索框（线框内嵌 Outlined.Search 图标，与语法详情页一致）
 * - 实时搜索文档标题、描述、模块名
 * - 搜索结果列表（条目行层次 + 轻量入场）
 *
 * 动效：搜索中 / 空结果 / 结果列表三态 Crossfade；结果条目首次入场 stagger
 */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SearchScreen(
    onDocClick: (String, String) -> Unit,
    onBack: () -> Unit,
    onOpenDrawer: () -> Unit,
    onHome: () -> Unit = {},
    viewModel: SearchViewModel = viewModel()
) {
    val query by viewModel.query.collectAsState()
    val results by viewModel.results.collectAsState()
    val isSearching by viewModel.isSearching.collectAsState()
    val moduleTitles by viewModel.moduleTitles.collectAsState()
    val extendedColors = LocalExtendedColors.current

    // 入场门控：首批结果就绪后的下一帧置 true，触发首次 stagger 入场
    var hasEntered by remember { mutableStateOf(false) }
    LaunchedEffect(results.isNotEmpty()) {
        if (results.isNotEmpty()) hasEntered = true
    }

    // 结果区阶段归并
    val phase = when {
        isSearching -> SearchPhase.SEARCHING
        results.isEmpty() && query.isNotEmpty() -> SearchPhase.EMPTY
        else -> SearchPhase.CONTENT
    }

    Scaffold(
        topBar = {
            TopDock(
                title = "搜索",
                showBack = true,
                onBack = onBack,
                onOpenDrawer = onOpenDrawer,
                onSyntax = {},
                onLearningPath = {},
                onSearch = {},
                showNavActions = false,
                showHome = true,
                onHome = onHome,
                themeQuickToggle = { ThemeQuickToggle(viewModel = viewModel()) }
            )
        }
    ) { innerPadding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding)
        ) {
            // 搜索框
            TextField(
                value = query,
                onValueChange = { viewModel.updateQuery(it) },
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp),
                placeholder = { Text("输入关键词...") },
                leadingIcon = {
                    // 显式着色：避免 LocalContentColor 默认黑导致深色模式下不可见
                    Icon(
                        Icons.Outlined.Search,
                        contentDescription = null,
                        tint = extendedColors.fgTertiary
                    )
                },
                singleLine = true,
                colors = TextFieldDefaults.colors(
                    focusedContainerColor = extendedColors.bgSecondary,
                    unfocusedContainerColor = extendedColors.bgSecondary
                )
            )

            // 结果区三态切换：120-220ms 淡入淡出
            Crossfade(
                targetState = phase,
                animationSpec = tweenNormal(),
                label = "searchPhaseCrossfade"
            ) { current ->
                when (current) {
                    SearchPhase.SEARCHING -> {
                        Box(
                            modifier = Modifier.fillMaxSize(),
                            contentAlignment = Alignment.Center
                        ) {
                            CircularProgressIndicator()
                        }
                    }
                    SearchPhase.EMPTY -> {
                        Box(
                            modifier = Modifier.fillMaxSize(),
                            contentAlignment = Alignment.Center
                        ) {
                            Text(
                                text = "未找到相关文档",
                                color = extendedColors.fgSecondary
                            )
                        }
                    }
                    SearchPhase.CONTENT -> {
                        LazyColumn(
                            modifier = Modifier.fillMaxSize(),
                            contentPadding = PaddingValues(bottom = 16.dp),
                            verticalArrangement = Arrangement.spacedBy(8.dp)
                        ) {
                            itemsIndexed(
                                results,
                                key = { _, doc -> "${doc.module}/${doc.slug}" }
                            ) { index, doc ->
                                DocListItem(
                                    doc = doc,
                                    onClick = { onDocClick(doc.module, doc.slug) },
                                    // 模块归属标签（标注结果来源）
                                    moduleLabel = moduleTitles[doc.module],
                                    modifier = Modifier
                                        .animateItem()
                                        .fandexEntrance(index = index, visible = hasEntered)
                                )
                            }
                        }
                    }
                }
            }
        }
    }
}
