package com.fandex.app.ui.screens.syntax

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.horizontalScroll
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
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.outlined.ContentCopy
import androidx.compose.material.icons.outlined.Search
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.outlined.ContentCopy
import androidx.compose.material.icons.outlined.Search
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
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
import androidx.compose.ui.platform.LocalClipboardManager
import androidx.compose.ui.text.AnnotatedString
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.fandex.app.data.model.SyntaxCard
import com.fandex.app.ui.markdown.rememberHighlightedCode
import com.fandex.app.ui.components.ThemeQuickToggle
import com.fandex.app.ui.components.TopDock
import com.fandex.app.ui.theme.CodeTextStyle
import com.fandex.app.ui.theme.LocalExtendedColors

/**
 * 语法速览详情页
 *
 * 对齐 Web 端 SyntaxExplorer 交互：
 * - 顶部搜索框（按名称 / 公式 / 代码过滤）
 * - 按 section 分组展示卡片
 * - 卡片含公式、高亮代码、复制与跳转原文入口
 */
@OptIn(ExperimentalMaterial3Api::class)
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
    val accent = parseSyntaxAccent(accentHex)

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
                    .padding(horizontal = 16.dp, vertical = 8.dp),
                placeholder = { Text("搜索语法点...") },
                leadingIcon = {
                    Icon(Icons.Outlined.Search, contentDescription = null)
                },
                singleLine = true,
                colors = TextFieldDefaults.colors(
                    focusedContainerColor = LocalExtendedColors.current.bgSecondary,
                    unfocusedContainerColor = LocalExtendedColors.current.bgSecondary
                )
            )

            when (val s = state) {
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
                            text = s.message,
                            color = LocalExtendedColors.current.fgSecondary
                        )
                    }
                }
                is SyntaxDetailUiState.Success -> {
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
                                color = LocalExtendedColors.current.fgSecondary
                            )
                        }
                    } else {
                        LazyColumn(
                            modifier = Modifier.fillMaxSize(),
                            contentPadding = PaddingValues(16.dp),
                            verticalArrangement = Arrangement.spacedBy(12.dp)
                        ) {
                            grouped.forEach { (section, cards) ->
                                // 分组标题
                                item(key = "section-$section") {
                                    SectionHeader(section, accent)
                                }
                                items(cards.size, key = { cards[it].id.ifEmpty { "$section-$it" } }) { index ->
                                    SyntaxCardItem(
                                        card = cards[index],
                                        moduleId = moduleId,
                                        docSlug = s.docTitleToSlug[cards[index].docTitle],
                                        onDocClick = onDocClick
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

/**
 * 分组标题
 */
@Composable
private fun SectionHeader(section: String, accent: androidx.compose.ui.graphics.Color) {
    Row(verticalAlignment = Alignment.CenterVertically) {
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
    onDocClick: (String, String) -> Unit
) {
    val extendedColors = LocalExtendedColors.current
    val clipboard = LocalClipboardManager.current
    var copied by remember { mutableStateOf(false) }

    Column(
        modifier = Modifier
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
                // 复制按钮悬浮右上
                Row(
                    modifier = Modifier
                        .align(Alignment.TopEnd)
                        .padding(4.dp)
                        .background(extendedColors.codeBg.copy(alpha = 0.9f))
                ) {
                    IconButton(
                        onClick = {
                            clipboard.setText(AnnotatedString(card.code))
                            copied = true
                        },
                        modifier = Modifier.width(28.dp)
                    ) {
                        Icon(
                            imageVector = if (copied) Icons.Filled.CheckCircle else Icons.Outlined.ContentCopy,
                            contentDescription = if (copied) "已复制" else "复制",
                            tint = if (copied) extendedColors.success else extendedColors.fgTertiary
                        )
                    }
                }
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


/**
 * 解析十六进制颜色
 */
private fun parseSyntaxAccent(hex: String): androidx.compose.ui.graphics.Color {
    val normalized = hex.removePrefix("#")
    return runCatching {
        androidx.compose.ui.graphics.Color(normalized.toLong(16) or 0xFF000000)
    }.getOrDefault(androidx.compose.ui.graphics.Color(0xFF4F5BD5))
}
