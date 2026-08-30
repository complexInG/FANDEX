package com.fandex.app.ui.screens.module

import com.fandex.app.ui.components.CategoryColor
import androidx.compose.animation.Crossfade
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.fandex.app.data.model.DocIndexEntry
import com.fandex.app.data.model.Module
import com.fandex.app.ui.common.fandexEntrance
import com.fandex.app.ui.common.tweenNormal
import com.fandex.app.ui.components.DocListItem
import com.fandex.app.ui.components.ThemeQuickToggle
import com.fandex.app.ui.components.TopDock
import com.fandex.app.ui.theme.LocalExtendedColors

/**
 * 模块详情页
 *
 * 对齐 Web 端模块列表页：
 * - 顶部栏（模块标题 + 返回 + 模块色竖条装饰）
 * - 模块描述
 * - 文档列表（条目行层次 + stagger 入场）
 *
 * 动效：Loading / Error / Success 切换 Crossfade；列表项轻量入场（仅首次）
 */
@Composable
fun ModuleScreen(
    moduleId: String,
    onDocClick: (String) -> Unit,
    onBack: () -> Unit,
    onOpenDrawer: () -> Unit,
    onHome: () -> Unit = {},
    viewModel: ModuleViewModel = viewModel()
) {
    LaunchedEffect(moduleId) {
        viewModel.loadModule(moduleId)
    }

    val state by viewModel.state.collectAsState()

    // 入场门控：内容就绪后的下一帧置 true，触发首次 stagger 入场
    var hasEntered by remember { mutableStateOf(false) }
    val dataReady = state is ModuleUiState.Success
    LaunchedEffect(dataReady) {
        if (dataReady) hasEntered = true
    }

    Scaffold(
        topBar = {
            TopDock(
                title = (state as? ModuleUiState.Success)?.module?.title ?: "加载中",
                showBack = true,
                onBack = onBack,
                onOpenDrawer = onOpenDrawer,
                onSyntax = {},
                onLearningPath = {},
                onSearch = {},
                showNavActions = false,
                showHome = true,
                onHome = onHome,
                // 模块色竖条装饰
                accentHex = (state as? ModuleUiState.Success)?.accentHex,
                themeQuickToggle = { ThemeQuickToggle(viewModel = viewModel()) }
            )
        }
    ) { innerPadding ->
        Box(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding)
        ) {
            // 状态切换：220ms 淡入淡出
            Crossfade(
                targetState = state,
                animationSpec = tweenNormal(),
                label = "moduleStateCrossfade"
            ) { current ->
                when (current) {
                    is ModuleUiState.Loading -> {
                        Box(
                            modifier = Modifier.fillMaxSize(),
                            contentAlignment = Alignment.Center
                        ) {
                            CircularProgressIndicator()
                        }
                    }
                    is ModuleUiState.Error -> {
                        Box(
                            modifier = Modifier.fillMaxSize(),
                            contentAlignment = Alignment.Center
                        ) {
                            Text(text = current.message, color = LocalExtendedColors.current.fgSecondary)
                        }
                    }
                    is ModuleUiState.Success -> {
                        ModuleContent(
                            module = current.module,
                            docs = current.docs,
                            accentHex = current.accentHex,
                            hasEntered = hasEntered,
                            onDocClick = onDocClick
                        )
                    }
                }
            }
        }
    }
}

/**
 * 模块内容
 */
@Composable
private fun ModuleContent(
    module: Module,
    docs: List<DocIndexEntry>,
    accentHex: String,
    hasEntered: Boolean,
    onDocClick: (String) -> Unit
) {
    val extendedColors = LocalExtendedColors.current
    val accent = CategoryColor.parse(accentHex)

    LazyColumn(
        modifier = Modifier.fillMaxSize(),
        contentPadding = PaddingValues(top = 8.dp, bottom = 16.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        // 模块描述（多彩分类色竖条点缀 + 入场动效）
        item(key = "description") {
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp)
                    .fandexEntrance(index = 0, visible = hasEntered)
            ) {
                Box(
                    modifier = Modifier
                        .width(3.dp)
                        .height(40.dp)
                        .clip(RoundedCornerShape(2.dp))
                        .background(accent.copy(alpha = 0.8f))
                )
                Spacer(modifier = Modifier.width(12.dp))
                Column {
                    Text(
                        text = module.description,
                        style = MaterialTheme.typography.bodyMedium,
                        color = extendedColors.fgSecondary
                    )
                    Spacer(modifier = Modifier.height(4.dp))
                    Text(
                        text = "${docs.size} 篇文档",
                        style = MaterialTheme.typography.labelMedium,
                        color = extendedColors.fgTertiary
                    )
                }
            }
        }

        // 文档列表（条目行 + 入场动效 + 重排动画）
        itemsIndexed(
            items = docs,
            key = { _, doc -> doc.slug }
        ) { index, doc ->
            DocListItem(
                doc = doc,
                onClick = { onDocClick(doc.slug) },
                accent = accent,
                indexLabel = "%02d".format(index + 1),
                modifier = Modifier
                    .animateItem()
                    .fandexEntrance(index = index + 1, visible = hasEntered)
            )
        }
    }
}
