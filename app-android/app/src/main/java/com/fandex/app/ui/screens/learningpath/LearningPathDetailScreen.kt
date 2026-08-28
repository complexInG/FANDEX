package com.fandex.app.ui.screens.learningpath

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
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
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
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
import com.fandex.app.data.model.LearningPathStage
import com.fandex.app.ui.components.DifficultyBadge
import com.fandex.app.ui.components.ThemeQuickToggle
import com.fandex.app.ui.components.TopDock
import com.fandex.app.ui.theme.LocalExtendedColors

/**
 * 学习路径详情页
 *
 * 展示某技术的学习路径：阶段（标题 + 副标题）与节点
 * 节点带难度标签与摘要，点击跳转对应文档
 */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun LearningPathDetailScreen(
    moduleId: String,
    onBack: () -> Unit,
    onDocClick: (String, String) -> Unit,
    onOpenDrawer: () -> Unit,
    onHome: () -> Unit = {},
    viewModel: LearningPathDetailViewModel = viewModel()
) {
    LaunchedEffect(moduleId) {
        viewModel.loadPath(moduleId)
    }

    val state by viewModel.state.collectAsState()
    val title by viewModel.title.collectAsState()
    val accentHex by viewModel.accentHex.collectAsState()
    val accent = parseLpAccent(accentHex)

    Scaffold(
        topBar = {
            TopDock(
                title = title.ifEmpty { moduleId },
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
                is LearningPathDetailUiState.Loading -> {
                    Box(
                        modifier = Modifier.fillMaxSize(),
                        contentAlignment = Alignment.Center
                    ) {
                        CircularProgressIndicator()
                    }
                }
                is LearningPathDetailUiState.Error -> {
                    Box(
                        modifier = Modifier.fillMaxSize(),
                        contentAlignment = Alignment.Center
                    ) {
                        Text(
                            text = (state as LearningPathDetailUiState.Error).message,
                            color = LocalExtendedColors.current.fgSecondary
                        )
                    }
                }
                is LearningPathDetailUiState.Success -> {
                    val path = (state as LearningPathDetailUiState.Success).path
                    LazyColumn(
                        modifier = Modifier.fillMaxSize(),
                        contentPadding = PaddingValues(16.dp),
                        verticalArrangement = Arrangement.spacedBy(16.dp)
                    ) {
                        // 摘要
                        if (path.summary.isNotEmpty()) {
                            item(key = "summary") {
                                Text(
                                    text = path.summary,
                                    style = MaterialTheme.typography.bodyMedium,
                                    color = LocalExtendedColors.current.fgSecondary
                                )
                            }
                        }
                        // 阶段
                        items(path.stages, key = { it.id.ifEmpty { it.title } }) { stage ->
                            StageItem(
                                moduleId = path.module,
                                stage = stage,
                                accent = accent,
                                onDocClick = onDocClick
                            )
                        }
                    }
                }
            }
        }
    }
}

/**
 * 阶段项
 */
@Composable
private fun StageItem(
    moduleId: String,
    stage: LearningPathStage,
    accent: androidx.compose.ui.graphics.Color,
    onDocClick: (String, String) -> Unit
) {
    val extendedColors = LocalExtendedColors.current

    Column(
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(4.dp))
            .background(extendedColors.bgElevated)
            .border(1.dp, extendedColors.borderDefault, RoundedCornerShape(4.dp))
            .padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        // 阶段标题与副标题（多彩分类色）
        Text(
            text = stage.title,
            style = MaterialTheme.typography.titleMedium,
            color = accent,
            fontWeight = FontWeight.SemiBold
        )
        if (stage.subtitle.isNotEmpty()) {
            Text(
                text = stage.subtitle,
                style = MaterialTheme.typography.bodySmall,
                color = extendedColors.fgSecondary
            )
        }
        // 节点列表
        stage.nodes.forEach { node ->
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .clickable(enabled = node.doc.isNotEmpty()) {
                        onDocClick(moduleId, node.doc)
                    }
                    .padding(vertical = 4.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                Box(
                    modifier = Modifier
                        .width(3.dp)
                        .height(28.dp)
                        .clip(RoundedCornerShape(2.dp))
                        .background(accent.copy(alpha = 0.7f))
                )
                Spacer(modifier = Modifier.width(10.dp))
                Column(modifier = Modifier.weight(1f)) {
                    Text(
                        text = node.title,
                        style = MaterialTheme.typography.bodyMedium,
                        color = MaterialTheme.colorScheme.onSurface,
                        maxLines = 1,
                        overflow = TextOverflow.Ellipsis
                    )
                    if (node.desc.isNotEmpty()) {
                        Text(
                            text = node.desc,
                            style = MaterialTheme.typography.bodySmall,
                            color = extendedColors.fgTertiary,
                            maxLines = 1,
                            overflow = TextOverflow.Ellipsis
                        )
                    }
                }
                if (node.doc.isNotEmpty()) {
                    Spacer(modifier = Modifier.width(8.dp))
                    DifficultyBadge(difficulty = node.difficulty)
                }
            }
        }
    }
}


/**
 * 解析十六进制颜色
 */
private fun parseLpAccent(hex: String): androidx.compose.ui.graphics.Color {
    val normalized = hex.removePrefix("#")
    return runCatching {
        androidx.compose.ui.graphics.Color(normalized.toLong(16) or 0xFF000000)
    }.getOrDefault(androidx.compose.ui.graphics.Color(0xFF4F5BD5))
}
