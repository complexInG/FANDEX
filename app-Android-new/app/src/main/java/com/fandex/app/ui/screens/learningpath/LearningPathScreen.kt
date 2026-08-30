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
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.fandex.app.data.model.LearningPathSummary
import com.fandex.app.ui.common.fandexEntrance
import com.fandex.app.ui.common.pressScale
import com.fandex.app.ui.common.tweenNormal
import com.fandex.app.ui.components.CategoryColor
import com.fandex.app.ui.components.StatsBar
import com.fandex.app.ui.components.ThemeQuickToggle
import com.fandex.app.ui.components.TopDock
import com.fandex.app.ui.theme.LocalExtendedColors

/** 阶段刻度条的最大刻度数，超出部分以「+N」提示 */
private const val MAX_STAGE_TICKS = 8

/**
 * 学习路线页
 *
 * 对齐 Web 端 /learning-path 页面，并提级至与首页同等级的视觉层次：
 * - 头部统计横幅：路径 / 阶段总量一览（StatsBar）
 * - 路径列表：序号徽标 + 分类色 + 阶段刻度条（几何刻度线，直读进度感）
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
                        // 头部统计：路径数 / 阶段总数
                        val totalStages = paths.sumOf { it.stageCount }

                        LazyColumn(
                            modifier = Modifier.fillMaxSize(),
                            contentPadding = PaddingValues(16.dp),
                            verticalArrangement = Arrangement.spacedBy(10.dp)
                        ) {
                            // 统计横幅（提级：与首页同级的内容锚点）
                            item(key = "stats") {
                                StatsBar(
                                    stats = listOf(
                                        "${paths.size}" to "学习路线",
                                        "$totalStages" to "阶段"
                                    ),
                                    modifier = Modifier.fandexEntrance(index = 0, visible = hasEntered)
                                )
                            }
                            itemsIndexed(paths, key = { _, entry -> entry.moduleId }) { index, entry ->
                                LearningPathItem(
                                    entry = entry,
                                    position = index,
                                    onClick = { onPathClick(entry.moduleId) },
                                    modifier = Modifier
                                        .animateItem()
                                        .fandexEntrance(index = index + 1, visible = hasEntered)
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
 * 学习路径项（提级版）
 *
 * 序号徽标 + 标题/描述 + 阶段刻度条（几何刻度线，直读学习跨度）+ 阶段计数药丸
 */
@Composable
private fun LearningPathItem(
    entry: LearningPathSummary,
    position: Int,
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
            .padding(14.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        // 序号徽标：分类色描边小方块 + 等宽序号（替代单调色条，信息量与视觉层级更高）
        Box(
            modifier = Modifier
                .clip(RoundedCornerShape(3.dp))
                .background(accent.copy(alpha = 0.08f))
                .border(1.dp, accent.copy(alpha = 0.38f), RoundedCornerShape(3.dp))
                .padding(horizontal = 8.dp, vertical = 6.dp),
            contentAlignment = Alignment.Center
        ) {
            Text(
                text = "%02d".format(position + 1),
                style = MaterialTheme.typography.labelMedium,
                color = accent,
                fontFamily = FontFamily.Monospace,
                fontWeight = FontWeight.SemiBold
            )
        }
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
            // 阶段刻度条：每阶段一根 2dp 竖条（几何刻度线，非点状），超出上限以「+N」提示
            if (entry.stageCount > 0) {
                Spacer(modifier = Modifier.height(6.dp))
                Row(verticalAlignment = Alignment.CenterVertically) {
                    repeat(minOf(entry.stageCount, MAX_STAGE_TICKS)) { tick ->
                        Box(
                            modifier = Modifier
                                .padding(end = 3.dp)
                                .width(2.dp)
                                .height(10.dp)
                                .clip(RoundedCornerShape(1.dp))
                                .background(accent.copy(alpha = 0.25f + 0.75f * (tick + 1) / minOf(entry.stageCount, MAX_STAGE_TICKS)))
                        )
                    }
                    if (entry.stageCount > MAX_STAGE_TICKS) {
                        Spacer(modifier = Modifier.width(4.dp))
                        Text(
                            text = "+${entry.stageCount - MAX_STAGE_TICKS}",
                            style = MaterialTheme.typography.labelSmall,
                            color = extendedColors.fgTertiary
                        )
                    }
                }
            }
        }

        // 阶段计数药丸
        if (entry.stageCount > 0) {
            Spacer(modifier = Modifier.width(8.dp))
            Text(
                text = "${entry.stageCount} 阶段",
                style = MaterialTheme.typography.labelSmall,
                color = accent,
                modifier = Modifier
                    .clip(RoundedCornerShape(4.dp))
                    .background(accent.copy(alpha = 0.1f))
                    .border(1.dp, accent.copy(alpha = 0.35f), RoundedCornerShape(4.dp))
                    .padding(horizontal = 8.dp, vertical = 2.dp)
            )
        }
    }
}
