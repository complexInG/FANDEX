package com.fandex.app.ui.screens.syntax

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
import androidx.compose.foundation.layout.size
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
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.fandex.app.ui.common.pressScale
import com.fandex.app.ui.components.ThemeQuickToggle
import com.fandex.app.ui.components.TopDock
import com.fandex.app.ui.theme.LocalExtendedColors

/**
 * 语法速览页
 *
 * 对齐 Web 端 /syntax 页面：
 * - 语言列表（预构建索引，含语法点统计与主题色）
 * - 点击进入具体语言的语法卡片列表
 */
@OptIn(ExperimentalMaterial3Api::class)
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
            if (index.languages.isEmpty()) {
                Box(
                    modifier = Modifier.fillMaxSize(),
                    contentAlignment = Alignment.Center
                ) {
                    CircularProgressIndicator()
                }
            } else {
                LazyColumn(
                    modifier = Modifier.fillMaxSize(),
                    contentPadding = PaddingValues(16.dp),
                    verticalArrangement = Arrangement.spacedBy(8.dp)
                ) {
                    items(index.languages, key = { it.id }) { language ->
                        SyntaxLanguageItem(
                            language = language,
                            onClick = { onModuleClick(language.id) }
                        )
                    }
                }
            }
        }
    }
}

/**
 * 语法语言项
 *
 * 对齐 web 端语言切换项：几何图标 + 名称 + 语法点统计
 */
@Composable
private fun SyntaxLanguageItem(
    language: com.fandex.app.data.model.SyntaxLanguage,
    onClick: () -> Unit
) {
    val extendedColors = LocalExtendedColors.current
    val accent = parseAccent(language.color, fallback = MaterialTheme.colorScheme.primary)
    val interaction = remember { MutableInteractionSource() }

    Row(
        modifier = Modifier
            .fillMaxWidth()
            .pressScale(interaction)
            .clip(RoundedCornerShape(4.dp))
            .background(extendedColors.bgElevated)
            .border(1.dp, extendedColors.borderDefault, RoundedCornerShape(4.dp))
            .clickable(interactionSource = interaction, indication = null, onClick = onClick)
            .padding(horizontal = 12.dp, vertical = 12.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        // 几何图标（索引提供的 2 字符标识，等宽字体）
        com.fandex.app.ui.components.ModuleIcon(
            label = language.icon.ifEmpty { language.title.take(2) },
            color = accent
        )

        Spacer(modifier = Modifier.width(12.dp))

        Column(modifier = Modifier.weight(1f)) {
            Text(
                text = language.title,
                style = MaterialTheme.typography.titleSmall,
                color = MaterialTheme.colorScheme.onSurface,
                fontWeight = FontWeight.SemiBold
            )
            Text(
                text = "${language.count} 个语法点 / ${language.docCount} 篇文档",
                style = MaterialTheme.typography.bodySmall,
                color = extendedColors.fgSecondary
            )
        }
    }
}

/**
 * 解析索引中的十六进制主题色
 */
private fun parseAccent(hex: String, fallback: Color): Color {
    val normalized = hex.removePrefix("#")
    return runCatching {
        Color(normalized.toLong(16) or 0xFF000000)
    }.getOrDefault(fallback)
}
