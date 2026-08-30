package com.fandex.app.ui.screens.syntax

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
import com.fandex.app.ui.common.fandexEntrance
import com.fandex.app.ui.common.pressScale
import com.fandex.app.ui.common.tweenNormal
import com.fandex.app.ui.components.CategoryColor
import com.fandex.app.ui.components.ModuleIcon
import com.fandex.app.ui.components.StatsBar
import com.fandex.app.ui.components.ThemeQuickToggle
import com.fandex.app.ui.components.TopDock
import com.fandex.app.ui.theme.LocalExtendedColors

/**
 * 语法速览页
 *
 * 对齐 Web 端 /syntax 页面，并提级至与首页同等级的视觉层次：
 * - 头部统计横幅：语言 / 语法点 / 文档总量一览（StatsBar）
 * - 语言列表：序号 + 几何图标 + 名称 + 语法点与文档双计数药丸（预构建索引，含主题色）
 * - 点击进入具体语言的语法卡片列表
 *
 * 动效：加载 / 内容切换 Crossfade；语言条目轻量入场（仅首次）
 */
@Composable
fun SyntaxScreen(
    onModuleClick: (String) -> Unit,
    onBack: () -> Unit,
    onOpenDrawer: () -> Unit,
    onHome: () -> Unit = {},
    viewModel: SyntaxViewModel = viewModel()
) {
    LaunchedEffect(Unit) {
        viewModel.load()
    }

    val index by viewModel.index.collectAsState()

    // 入场门控：内容就绪后的下一帧置 true，触发首次 stagger 入场
    var hasEntered by remember { mutableStateOf(false) }
    val dataReady = index.languages.isNotEmpty()
    LaunchedEffect(dataReady) {
        if (dataReady) hasEntered = true
    }

    Scaffold(
        topBar = {
            TopDock(
                title = "语法速览",
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
            // 加载 / 内容切换：220ms 淡入淡出
            Crossfade(
                targetState = dataReady,
                animationSpec = tweenNormal(),
                label = "syntaxStateCrossfade"
            ) { loaded ->
                if (!loaded) {
                    Box(
                        modifier = Modifier.fillMaxSize(),
                        contentAlignment = Alignment.Center
                    ) {
                        CircularProgressIndicator()
                    }
                } else {
                    val languages = index.languages
                    // 头部统计：语言数 / 语法点总数 / 文档总数（从预构建索引聚合）
                    val totalPoints = languages.sumOf { it.count }
                    val totalDocs = languages.sumOf { it.docCount }

                    LazyColumn(
                        modifier = Modifier.fillMaxSize(),
                        contentPadding = PaddingValues(16.dp),
                        verticalArrangement = Arrangement.spacedBy(10.dp)
                    ) {
                        // 统计横幅（提级：与首页同级的内容锚点）
                        item(key = "stats") {
                            StatsBar(
                                stats = listOf(
                                    "${languages.size}" to "语言",
                                    "$totalPoints" to "语法点",
                                    "$totalDocs" to "文档"
                                ),
                                modifier = Modifier.fandexEntrance(index = 0, visible = hasEntered)
                            )
                        }
                        itemsIndexed(languages, key = { _, language -> language.id }) { position, language ->
                            SyntaxLanguageItem(
                                language = language,
                                position = position,
                                onClick = { onModuleClick(language.id) },
                                modifier = Modifier
                                    .animateItem()
                                    .fandexEntrance(index = position + 1, visible = hasEntered)
                            )
                        }
                    }
                }
            }
        }
    }
}

/**
 * 语法语言项（提级版）
 *
 * 对齐 web 端语言切换项并增强信息密度：
 * 模块内序号 + 几何图标 + 名称 + 语法点（强调色药丸）与文档数（中性药丸）双计数
 */
@Composable
private fun SyntaxLanguageItem(
    language: com.fandex.app.data.model.SyntaxLanguage,
    position: Int,
    onClick: () -> Unit,
    modifier: Modifier = Modifier
) {
    val extendedColors = LocalExtendedColors.current
    val accent = CategoryColor.parse(language.color)
    val interaction = remember { MutableInteractionSource() }

    Row(
        modifier = modifier
            .fillMaxWidth()
            .pressScale(interaction)
            .clip(RoundedCornerShape(4.dp))
            .background(extendedColors.bgElevated)
            .border(1.dp, extendedColors.borderDefault, RoundedCornerShape(4.dp))
            .clickable(interactionSource = interaction, indication = null, onClick = onClick)
            .padding(horizontal = 12.dp, vertical = 12.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        // 模块内学习顺序序号（等宽字，次级色）
        Text(
            text = "%02d".format(position + 1),
            style = MaterialTheme.typography.labelMedium,
            color = extendedColors.fgTertiary,
            fontFamily = FontFamily.Monospace
        )
        Spacer(modifier = Modifier.width(10.dp))

        // 几何图标（索引提供的 2 字符标识，等宽字体）
        ModuleIcon(
            label = language.icon.ifEmpty { language.title.take(2) },
            color = accent
        )

        Spacer(modifier = Modifier.width(12.dp))

        Column(modifier = Modifier.weight(1f)) {
            Text(
                text = language.title,
                style = MaterialTheme.typography.titleSmall,
                color = MaterialTheme.colorScheme.onSurface,
                fontWeight = FontWeight.SemiBold,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
            Text(
                text = "语法速查",
                style = MaterialTheme.typography.bodySmall,
                color = extendedColors.fgSecondary
            )
        }

        // 语法点计数（强调色药丸）
        Text(
            text = "${language.count} 语法点",
            style = MaterialTheme.typography.labelSmall,
            color = accent,
            modifier = Modifier
                .clip(RoundedCornerShape(4.dp))
                .background(accent.copy(alpha = 0.1f))
                .border(1.dp, accent.copy(alpha = 0.35f), RoundedCornerShape(4.dp))
                .padding(horizontal = 8.dp, vertical = 2.dp)
        )
        Spacer(modifier = Modifier.width(6.dp))
        // 文档数（中性药丸）
        Text(
            text = "${language.docCount} 篇",
            style = MaterialTheme.typography.labelSmall,
            color = extendedColors.fgTertiary,
            modifier = Modifier
                .clip(RoundedCornerShape(4.dp))
                .background(extendedColors.bgSunken)
                .padding(horizontal = 8.dp, vertical = 2.dp)
        )
    }
}
