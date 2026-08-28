package com.fandex.app.ui.components

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.BrightnessAuto
import androidx.compose.material.icons.filled.Code
import androidx.compose.material.icons.filled.DarkMode
import androidx.compose.material.icons.filled.Explore
import androidx.compose.material.icons.filled.OpenInNew
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.LightMode
import androidx.compose.material.icons.filled.Menu
import androidx.compose.material.icons.filled.Search
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.platform.LocalUriHandler
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import com.fandex.app.ui.common.pressScale
import com.fandex.app.ui.theme.LocalExtendedColors

/** 源仓库地址（GitHub 按钮跳转目标） */
const val REPO_URL = "https://github.com/fanquanpp/FANDEX"

/**
 * 全局顶部功能 Dock
 *
 * 参考旧版 FANDEX-App 顶栏设计：多页面通用功能常驻
 * - 左侧：抽屉菜单（首页）/ 返回（详情页）
 * - 中部：页面标题（首页为品牌名）
 * - 右侧：常驻功能按钮（语法速览 / 学习路线 / 搜索 / 首页 / 源仓库 / 主题快切）
 *   与页面专属按钮（如文档页的目录）按需组合
 *
 * 图标统一取自共享 Material 图标集与 modules.json 元数据，不单独造图标
 */
@Composable
fun TopDock(
    title: String,
    showBack: Boolean,
    onBack: () -> Unit,
    onOpenDrawer: () -> Unit,
    onSyntax: () -> Unit,
    onLearningPath: () -> Unit,
    onSearch: () -> Unit,
    showNavActions: Boolean = true,
    showHome: Boolean = false,
    onHome: () -> Unit = {},
    themeQuickToggle: @Composable () -> Unit = {},
    pageActions: @Composable () -> Unit = {}
) {
    val extendedColors = LocalExtendedColors.current

    Row(
        modifier = Modifier
            .fillMaxWidth()
            .background(MaterialTheme.colorScheme.surface)
            // 状态栏内边距：自定义 Dock 需自行处理（M3 TopAppBar 默认自带）
            .statusBarsPadding()
            .height(64.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        // 左侧：抽屉 / 返回
        IconButton(onClick = if (showBack) onBack else onOpenDrawer) {
            Icon(
                imageVector = if (showBack) Icons.AutoMirrored.Filled.ArrowBack else Icons.Filled.Menu,
                contentDescription = if (showBack) "返回" else "菜单"
            )
        }

        // 标题
        Text(
            text = title,
            style = MaterialTheme.typography.titleMedium,
            fontWeight = FontWeight.Bold,
            maxLines = 1,
            overflow = TextOverflow.Ellipsis,
            modifier = Modifier.weight(1f)
        )

        // 页面专属按钮（目录 / 分享等）
        pageActions()

        // 常驻功能：语法速览 / 学习路线 / 搜索（详情页收起以保标题空间）
        if (showNavActions) {
            DockIcon(Icons.Filled.Code, "语法速览", onSyntax)
            DockIcon(Icons.Filled.Explore, "学习路线", onLearningPath)
            DockIcon(Icons.Filled.Search, "搜索", onSearch)
        }

        // 首页（非首页时显示，一键回主页）
        if (showHome) {
            DockIcon(Icons.Filled.Home, "首页", onHome)
        }

        // 源仓库（浏览器打开 GitHub 仓库）
        val uriHandler = LocalUriHandler.current
        DockIcon(Icons.Filled.OpenInNew, "源仓库") {
            runCatching { uriHandler.openUri(REPO_URL) }
        }

        // 主题快切（全页面常驻）
        themeQuickToggle()
    }
}

/**
 * Dock 图标按钮
 */
@Composable
private fun DockIcon(
    icon: ImageVector,
    contentDescription: String,
    onClick: () -> Unit
) {
    IconButton(onClick = onClick) {
        Icon(icon, contentDescription = contentDescription)
    }
}

/**
 * 分类筛选 Chip（参考旧版首页筛选行）
 *
 * 选中态：分类色填充 + 反色文字；未选中：边框 + 次级文字
 * 提供明确的点击选择视觉提示
 */
@Composable
fun FilterChip(
    label: String,
    selected: Boolean,
    color: androidx.compose.ui.graphics.Color,
    onClick: () -> Unit
) {
    val extendedColors = LocalExtendedColors.current
    val interaction = remember { MutableInteractionSource() }

    val bg = if (selected) color else extendedColors.bgElevated
    val fg = if (selected) {
        // 依据背景亮度选择可读文字色
        if (color.isLightColor()) androidx.compose.ui.graphics.Color.White
        else androidx.compose.ui.graphics.Color(0xFF0A0A0A)
    } else extendedColors.fgSecondary
    val border = if (selected) color else extendedColors.borderDefault

    Box(
        modifier = Modifier
            .pressScale(interaction)
            .clip(RoundedCornerShape(4.dp))
            .background(bg)
            .border(1.dp, border, RoundedCornerShape(4.dp))
            .clickable(interactionSource = interaction, indication = null, onClick = onClick)
            .padding(horizontal = 14.dp, vertical = 8.dp)
    ) {
        Text(
            text = label,
            style = MaterialTheme.typography.labelLarge,
            color = fg,
            fontWeight = if (selected) FontWeight.SemiBold else FontWeight.Medium
        )
    }
}

/** 亮度粗判（>0.6 视为浅色背景，用深色文字） */
private fun androidx.compose.ui.graphics.Color.isLightColor(): Boolean {
    val lum = 0.299 * red + 0.587 * green + 0.114 * blue
    return lum > 0.6
}

/**
 * 主题快切按钮
 *
 * 参考旧版顶栏主题按钮：跟随系统 -> 浅色 -> 深色 循环
 * 图标随当前模式切换（共享 Material 图标集）
 */
@Composable
fun ThemeQuickToggle(
    viewModel: com.fandex.app.MainViewModel
) {
    val mode by viewModel.themeMode.collectAsState()
    IconButton(onClick = { viewModel.cycleThemeMode() }) {
        Icon(
            imageVector = when (mode) {
                com.fandex.app.data.prefs.ThemeMode.SYSTEM -> Icons.Filled.BrightnessAuto
                com.fandex.app.data.prefs.ThemeMode.LIGHT -> Icons.Filled.LightMode
                com.fandex.app.data.prefs.ThemeMode.DARK -> Icons.Filled.DarkMode
            },
            contentDescription = "切换主题"
        )
    }
}
