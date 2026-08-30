package com.fandex.app.ui.screens.learningpath

import androidx.compose.animation.Crossfade
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
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.foundation.interaction.MutableInteractionSource
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
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.fandex.app.data.model.LearningPathSummary
import com.fandex.app.ui.common.fandexEntrance
import com.fandex.app.ui.common.pressScale
import com.fandex.app.ui.common.tweenNormal
import com.fandex.app.ui.components.CategoryColor
import com.fandex.app.ui.components.ThemeQuickToggle
import com.fandex.app.ui.components.TopDock
import com.fandex.app.ui.theme.LocalExtendedColors

/**
 * 学习路线页
 *
 * 对齐 Web 端 /learning-path 页面：
 * - 展示所有可用学习路径（顺序与 web 端索引一致）
 * - 点击进入具体路径的阶段与节点
 *
 * 动效：状态切换 Crossfade；路径条目轻量入场（仅首次）
 */
@Composable
fun LearningPathScreen(
    onPathClick: (String) -> Unit,
    onBack: () -> Unit,
    onOpenDrawer: () -> Unit,
    onHome: () -> Unit = {},
    viewModel: LearningPathViewModel = viewModel()
) {
    LaunchedEffect(Unit) {
        viewModel.load()
    }

    val state by viewModel.state.collectAsState()

    // 入场门控：内容就绪后的下一帧置 true，触发首次 stagger 入场
    var hasEntered by remember { mutableStateOf(false) }
    val dataReady = state is LearningPathUiState.Success
    LaunchedEffect(dataReady) {
        if (dataReady) hasEntered = true
    }

    Scaffold(
        topBar = {
            TopDock(
                title = "学习路线",
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
            // 状态切换：220ms 淡入淡出
            Crossfade(
                targetState = state,
                animationSpec = tweenNormal(),
                label = "learningPathStateCrossfade"
            ) { current ->
                when (current) {
                    is LearningPathUiState.Loading -> {
                        Box(
                            modifier = Modifier.fillMaxSize(),
                            contentAlignment = Alignment.Center
                        ) {
                            CircularProgressIndicator()
                        }
                    }
                    is LearningPathUiState.Error -> {
                        Box(
                            modifier = Modifier.fillMaxSize(),
                            contentAlignment = Alignment.Center
                        ) {
                            Text(
                                text = current.message,
                                color = LocalExtendedColors.current.fgSecondary
                            )
                        }
                    }
                    is LearningPathUiState.Success -> {
                        val paths = current.paths
                        LazyColumn(
                            modifier = Modifier.fillMaxSize(),
                            contentPadding = PaddingValues(16.dp),
                            verticalArrangement = Arrangement.spacedBy(8.dp)
                        ) {
                            itemsIndexed(paths, key = { _, entry -> entry.moduleId }) { index, entry ->
                                LearningPathItem(
                                    entry = entry,
                                    onClick = { onPathClick(entry.moduleId) },
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

/**
 * 学习路径项
 */
@Composable
private fun LearningPathItem(
    entry: LearningPathSummary,
    onClick: () -> Unit,
    modifier: Modifier = Modifier
) {
    val extendedColors = LocalExtendedColors.current
    val interaction = remember { MutableInteractionSource() }
    val accent = CategoryColor.parse(entry.colorHex)

    Row(
        modifier = modifier
            .fillMaxWidth()
            .pressScale(interaction)
            .clip(RoundedCornerShape(4.dp))
            .background(extendedColors.bgElevated)
            .border(1.dp, extendedColors.borderDefault, RoundedCornerShape(4.dp))
            .clickable(interactionSource = interaction, indication = null, onClick = onClick)
            .padding(16.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        Box(
            modifier = Modifier
                .width(3.dp)
                .height(40.dp)
                .clip(RoundedCornerShape(2.dp))
                .background(accent)
        )
        Spacer(modifier = Modifier.width(12.dp))
        Column(modifier = Modifier.weight(1f)) {
            Text(
                text = entry.title,
                style = MaterialTheme.typography.titleMedium,
                color = MaterialTheme.colorScheme.onSurface,
                fontWeight = FontWeight.SemiBold,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
            if (entry.description.isNotEmpty()) {
                Text(
                    text = entry.description,
                    style = MaterialTheme.typography.bodySmall,
                    color = extendedColors.fgSecondary,
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )
            }
        }
        if (entry.stageCount > 0) {
            Text(
                text = "${entry.stageCount} 阶段",
                style = MaterialTheme.typography.labelMedium,
                color = extendedColors.fgTertiary
            )
        }
    }
}
