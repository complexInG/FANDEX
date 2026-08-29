package com.fandex.app.ui.screens.syntax

import com.fandex.app.ui.components.CategoryColor
import androidx.compose.animation.Crossfade
import androidx.compose.animation.animateColorAsState
import androidx.compose.animation.core.tween
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.interaction.collectIsFocusedAsState
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
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.outlined.ContentCopy
import androidx.compose.material.icons.outlined.Search
import androidx.compose.material3.CircularProgressIndicator
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
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalClipboardManager
import androidx.compose.ui.text.AnnotatedString
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.fandex.app.data.model.SyntaxCard
import com.fandex.app.ui.components.FdxIconButton
import com.fandex.app.ui.common.fandexEntrance
import com.fandex.app.ui.common.tweenNormal
import com.fandex.app.ui.components.ThemeQuickToggle
import com.fandex.app.ui.components.TopDock
import com.fandex.app.ui.markdown.rememberHighlightedCode
import com.fandex.app.ui.theme.CodeTextStyle
import com.fandex.app.ui.theme.LocalExtendedColors

/**
 * 语法速览详情页
 *
 * 对齐 Web 端 SyntaxExplorer 交互：
 * - 顶部搜索框（按名称 / 公式 / 代码过滤；焦点态边框颜色 150ms 过渡）
 * - 按 section 分组展示卡片
 * - 卡片含公式、高亮代码、复制与跳转原文入口
 *
 * 动效：状态切换 Crossfade；分组卡片首次入场 stagger
 */
@Composable
fun SyntaxDetailScreen(
    moduleId: String,
    onBack: () -> Unit,
    onDocClick: (String, String) -> Unit,
    onOpenDrawer: () -> Unit,
    onHome: () -> Unit = {},
    viewModel: SyntaxDetailViewModel = viewModel()
) {
    LaunchedEffect(moduleId) {
        viewModel.loadModule(moduleId)
    }

    val state by viewModel.state.collectAsState()
    val query by viewModel.query.collectAsState()
    val title by viewModel.title.collectAsState()
    val accentHex by viewModel.accentHex.collectAsState()
    val accent = CategoryColor.parse(accentHex)
    val extendedColors = LocalExtendedColors.current

    // 入场门控：内容就绪后的下一帧置 true，触发首次 stagger 入场
    var hasEntered by remember { mutableStateOf(false) }
    val dataReady = state is SyntaxDetailUiState.Success
    LaunchedEffect(dataReady) {
        if (dataReady) hasEntered = true
    }

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
                accentHex = accentHex,
                themeQuickToggle = { ThemeQuickToggle(viewModel = viewModel()) }
            )
        }
    ) { innerPadding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding)
        ) {
            // 搜索框：容器边框随焦点态 150ms 颜色过渡（对齐 web 端输入框减速过渡）
            SyntaxSearchField(
                query = query,
                onQueryChange = { viewModel.updateQuery(it) }
            )

            // 状态切换：220ms 淡入淡出
            Crossfade(
                targetState = state,
                animationSpec = tweenNormal(),
                label = "syntaxDetailStateCrossfade"
            ) { current ->
                when (current) {
                    is SyntaxDetailUiState.Loading -> {
                        Box(
                            modifier = Modifier.fillMaxSize(),
                            contentAlignment = Alignment.Center
                        ) {
                            CircularProgressIndicator()
                        }
                    }
                    is SyntaxDetailUiState.Error -> {
                        Box(
                            modifier = Modifier.fillMaxSize(),
                            contentAlignment = Alignment.Center
                        ) {
                            Text(
                                text = current.message,
                                color = extendedColors.fgSecondary
                            )
                        }
                    }
                    is SyntaxDetailUiState.Success -> {
                        val s = current
                        val filtered = remember(s.cards, query) {
                            val q = query.trim()
                            if (q.isEmpty()) s.cards
                            else s.cards.filter { card ->
                                card.name.contains(q, ignoreCase = true) ||
                                    card.formula.contains(q, ignoreCase = true) ||
                                    card.code.contains(q, ignoreCase = true) ||
                                    card.section.contains(q, ignoreCase = true)
                            }
                        }
                        // 按 section 分组并保留首次出现顺序
                        val grouped = remember(filtered) {
                            filtered.groupBy { it.section.ifEmpty { "其他" } }
                        }

                        if (filtered.isEmpty()) {
                            Box(
                                modifier = Modifier.fillMaxSize(),
                                contentAlignment = Alignment.Center
                            ) {
                                Text(
                                    text = "未找到匹配的语法点",
                                    color = extendedColors.fgSecondary
                                )
                            }
                        } else {
                            LazyColumn(
                                modifier = Modifier.fillMaxSize(),
                                contentPadding = PaddingValues(16.dp),
                                verticalArrangement = Arrangement.spacedBy(12.dp)
                            ) {
                                // 在 builder 阶段确定性分配全局入场下标（跨分组连续递增）
                                var runningIndex = 0
                                grouped.forEach { (section, cards) ->
                                    val headerIndex = runningIndex
                                    runningIndex += 1
                                    // 分组标题
                                    item(key = "section-$section") {
                                        SectionHeader(
                                            section = section,
                                            accent = accent,
                                            modifier = Modifier
                                                .animateItem()
                                                .fandexEntrance(
                                                    index = headerIndex,
                                                    visible = hasEntered
                                                )
                                        )
                                    }
                                    val cardStart = runningIndex
                                    runningIndex += cards.size
                                    items(cards.size, key = { cards[it].id.ifEmpty { "$section-$it" } }) { index ->
                                        SyntaxCardItem(
                                            card = cards[index],
                                            moduleId = moduleId,
                                            docSlug = s.docTitleToSlug[cards[index].docTitle],
                                            onDocClick = onDocClick,
                                            modifier = Modifier
                                                .animateItem()
                                                .fandexEntrance(
                                                    index = cardStart + index,
                                                    visible = hasEntered
                                                )
                                        )
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

/**
 * 语法搜索框
 *
 * 容器边框颜色随焦点态过渡：未聚焦 borderDefault -> 聚焦 borderFocus（150ms）
 */
@Composable
private fun SyntaxSearchField(
    query: String,
    onQueryChange: (String) -> Unit
) {
    val extendedColors = LocalExtendedColors.current
    val interaction = remember { MutableInteractionSource() }
    val focused by interaction.collectIsFocusedAsState()

    val borderColor by animateColorAsState(
        targetValue = if (focused) extendedColors.borderFocus else extendedColors.borderDefault,
        animationSpec = tween(durationMillis = 150),
        label = "syntaxSearchBorder"
    )

    Box(
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 16.dp, vertical = 8.dp)
            .clip(RoundedCornerShape(4.dp))
            .border(1.dp, borderColor, RoundedCornerShape(4.dp))
    ) {
        TextField(
            value = query,
            onValueChange = onQueryChange,
            modifier = Modifier.fillMaxWidth(),
            interactionSource = interaction,
            placeholder = { Text("搜索语法点...") },
            leadingIcon = {
                Icon(Icons.Outlined.Search, contentDescription = null)
            },
            singleLine = true,
            shape = RoundedCornerShape(4.dp),
            // 隐藏默认下划线指示器，由容器边框承担焦点反馈
            colors = TextFieldDefaults.colors(
                focusedContainerColor = extendedColors.bgSecondary,
                unfocusedContainerColor = extendedColors.bgSecondary,
                focusedIndicatorColor = Color.Transparent,
                unfocusedIndicatorColor = Color.Transparent,
                disabledIndicatorColor = Color.Transparent,
                errorIndicatorColor = Color.Transparent
            )
        )
    }
}

/**
 * 分组标题
 */
@Composable
private fun SectionHeader(
    section: String,
    accent: Color,
    modifier: Modifier = Modifier
) {
    Row(
        modifier = modifier,
        verticalAlignment = Alignment.CenterVertically
    ) {
        Box(
            modifier = Modifier
                .width(3.dp)
                .height(14.dp)
                .clip(RoundedCornerShape(2.dp))
                .background(accent)
        )
        Spacer(modifier = Modifier.width(8.dp))
        Text(
            text = section,
            style = MaterialTheme.typography.titleSmall,
            fontWeight = FontWeight.SemiBold,
            color = MaterialTheme.colorScheme.onSurface
        )
    }
}

/**
 * 语法速查卡片
 *
 * @param moduleId 当前语法模块 ID（跳转原文时的文档模块）
 */
@Composable
private fun SyntaxCardItem(
    card: SyntaxCard,
    moduleId: String,
    docSlug: String?,
    onDocClick: (String, String) -> Unit,
    modifier: Modifier = Modifier
) {
    val extendedColors = LocalExtendedColors.current
    val clipboard = LocalClipboardManager.current
    var copied by remember { mutableStateOf(false) }

    Column(
        modifier = modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(4.dp))
            .background(extendedColors.bgElevated)
            .border(1.dp, extendedColors.borderDefault, RoundedCornerShape(4.dp))
            .padding(12.dp),
        verticalArrangement = Arrangement.spacedBy(6.dp)
    ) {
        // 名称
        Text(
            text = card.name,
            style = MaterialTheme.typography.titleSmall,
            color = MaterialTheme.colorScheme.onSurface,
            fontWeight = FontWeight.SemiBold
        )

        // 公式
        if (card.formula.isNotEmpty()) {
            val scrollState = rememberScrollState()
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .clip(RoundedCornerShape(4.dp))
                    .background(extendedColors.bgSunken)
                    .padding(8.dp)
            ) {
                Text(
                    text = card.formula,
                    style = CodeTextStyle,
                    color = extendedColors.codeText,
                    modifier = Modifier.horizontalScroll(scrollState)
                )
            }
        }

        // 代码示例（语法高亮 + 复制按钮）
        if (card.code.isNotEmpty()) {
            val scrollState = rememberScrollState()
            val highlighted = rememberHighlightedCode(card.code, card.lang)
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .clip(RoundedCornerShape(4.dp))
                    .background(extendedColors.codeBg)
            ) {
                Text(
                    text = highlighted,
                    style = CodeTextStyle,
                    color = extendedColors.codeText,
                    modifier = Modifier
                        .padding(8.dp)
                        .horizontalScroll(scrollState)
                )
                // 复制按钮悬浮右上（复制成功切换成功色图标）
                FdxIconButton(
                    icon = if (copied) Icons.Filled.CheckCircle else Icons.Outlined.ContentCopy,
                    contentDescription = if (copied) "已复制" else "复制",
                    onClick = {
                        clipboard.setText(AnnotatedString(card.code))
                        copied = true
                    },
                    tint = if (copied) extendedColors.success else extendedColors.fgTertiary,
                    modifier = Modifier.align(Alignment.TopEnd)
                )
            }
        }

        // 跳转来源文档
        if (docSlug != null) {
            Text(
                text = "查看文档：${card.docTitle}",
                style = MaterialTheme.typography.labelMedium,
                color = MaterialTheme.colorScheme.primary,
                modifier = Modifier.clickable { onDocClick(moduleId, docSlug) }
            )
        }
    }
}
