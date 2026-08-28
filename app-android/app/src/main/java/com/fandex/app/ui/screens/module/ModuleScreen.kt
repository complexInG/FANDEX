package com.fandex.app.ui.screens.module

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
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.fandex.app.data.model.DocIndexEntry
import com.fandex.app.data.model.Module
import com.fandex.app.ui.components.DocListItem
import com.fandex.app.ui.components.ThemeQuickToggle
import com.fandex.app.ui.components.TopDock
import com.fandex.app.ui.theme.LocalExtendedColors
import androidx.compose.ui.graphics.Color

/**
 * 模块详情页
 *
 * 对齐 Web 端模块列表页：
 * - 顶部栏（模块标题 + 返回）
 * - 模块描述
 * - 文档列表
 */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ModuleScreen(
    moduleId: String,
    onDocClick: (String) -> Unit,
    onBack: () -> Unit,
    onOpenDrawer: () -> Unit,
    onHome: () -> Unit = {},
    viewModel: ModuleViewModel = viewModel()
) {    LaunchedEffect(moduleId) {
        viewModel.loadModule(moduleId)
    }

    val state by viewModel.state.collectAsState()

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
                themeQuickToggle = { ThemeQuickToggle(viewModel = viewModel()) }
            )
        }
    ) { innerPadding ->
        Box(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding)
        ) {
            when (state) {
                is ModuleUiState.Loading -> {
                    Box(
                        modifier = Modifier.fillMaxSize(),
                        contentAlignment = Alignment.Center
                    ) {
                        CircularProgressIndicator()
                    }
                }
                is ModuleUiState.Error -> {
                    val msg = (state as ModuleUiState.Error).message
                    Box(
                        modifier = Modifier.fillMaxSize(),
                        contentAlignment = Alignment.Center
                    ) {
                        Text(text = msg, color = LocalExtendedColors.current.fgSecondary)
                    }
                }
                is ModuleUiState.Success -> {
                    val data = state as ModuleUiState.Success
                    ModuleContent(
                        module = data.module,
                        docs = data.docs,
                        accentHex = data.accentHex,
                        onDocClick = onDocClick
                    )
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
    onDocClick: (String) -> Unit
) {
    val extendedColors = LocalExtendedColors.current
    val accent = parseAccentColor(accentHex)

    LazyColumn(
        modifier = Modifier.fillMaxSize(),
        contentPadding = PaddingValues(bottom = 16.dp),
        verticalArrangement = Arrangement.spacedBy(0.dp)
    ) {
        // 模块描述（多彩分类色竖条点缀）
        item {
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp)
            ) {
                Box(
                    modifier = Modifier
                        .width(3.dp)
                        .height(40.dp)
                        .clip(androidx.compose.foundation.shape.RoundedCornerShape(2.dp))
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

        // 文档列表（多彩竖条 + 阅读顺序编号，条目带位移动画）
        itemsIndexed(
            items = docs,
            key = { _, doc -> doc.slug }
        ) { index, doc ->
            DocListItem(
                doc = doc,
                onClick = { onDocClick(doc.slug) },
                accent = accent,
                indexLabel = "%02d".format(index + 1),
                modifier = Modifier.animateItem()
            )
        }
    }
}


/**
 * 解析十六进制颜色
 */
private fun parseAccentColor(hex: String): Color {
    val normalized = hex.removePrefix("#")
    return runCatching {
        Color(normalized.toLong(16) or 0xFF000000)
    }.getOrDefault(Color(0xFF4F5BD5))
}
