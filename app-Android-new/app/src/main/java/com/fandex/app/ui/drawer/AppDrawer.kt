package com.fandex.app.ui.drawer

import android.app.Application
import androidx.compose.animation.animateColorAsState
import androidx.compose.animation.core.tween
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Code
import androidx.compose.material.icons.filled.Explore
import androidx.compose.material.icons.filled.Home
import androidx.compose.material.icons.filled.Search
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import androidx.lifecycle.viewmodel.compose.viewModel
import com.fandex.app.BuildConfig
import com.fandex.app.FandexApp
import com.fandex.app.data.model.CategoryInfo
import com.fandex.app.data.prefs.ThemeMode
import com.fandex.app.ui.common.pressScale
import com.fandex.app.ui.components.CategoryColor
import com.fandex.app.ui.theme.LocalExtendedColors
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

/**
 * 抽屉 ViewModel
 *
 * 提供抽屉所需的站点统计、分类模块导航数据与主题控制
 * （设置收纳进抽屉，参考旧版 FANDEX-App 的抽屉面板设计）
 */
class DrawerViewModel(application: Application) : AndroidViewModel(application) {

    private val container = (application as FandexApp).container

    /** 分类模块数据 */
    private val _categories = MutableStateFlow<List<CategoryInfo>>(emptyList())
    val categories: StateFlow<List<CategoryInfo>> = _categories.asStateFlow()

    /** 站点统计 */
    private val _stats = MutableStateFlow(DrawerStats())
    val stats: StateFlow<DrawerStats> = _stats.asStateFlow()

    /** 模块文档计数（模块导航行展示） */
    private val _moduleCounts = MutableStateFlow<Map<String, Int>>(emptyMap())
    val moduleCounts: StateFlow<Map<String, Int>> = _moduleCounts.asStateFlow()

    val themeMode: StateFlow<ThemeMode> = container.themePreferences.themeMode
        .stateIn(viewModelScope, SharingStarted.Eagerly, ThemeMode.SYSTEM)

    init {
        load()
    }

    fun load() {
        viewModelScope.launch {
            runCatching {
                _categories.value = container.moduleRepository.categories()
                val docStats = container.docRepository.stats()
                _stats.value = DrawerStats(
                    categoryCount = _categories.value.size,
                    moduleCount = docStats.moduleCount,
                    docCount = docStats.docCount
                )
                // 各模块文档计数
                _moduleCounts.value = container.docRepository.docIndex()
                    .groupingBy { it.module }.eachCount()
            }
        }
    }

    fun setThemeMode(mode: ThemeMode) {
        viewModelScope.launch { container.themePreferences.setThemeMode(mode) }
    }
}

/** 抽屉统计信息 */
data class DrawerStats(
    val categoryCount: Int = 0,
    val moduleCount: Int = 0,
    val docCount: Int = 0
)

/** 抽屉导航项 */
private data class DrawerNav(
    val icon: ImageVector,
    val label: String,
    val route: String
)

/**
 * 应用抽屉面板
 *
 * 功能布局参考旧版 FANDEX-App 抽屉，采用固定分区结构：
 * - 固定顶部：品牌头部 + 快捷导航 + 主题三选（不随内容滚动）
 * - 滚动区域：模块快速导航（多彩分类分组 + 计数）
 * - 固定底部：免责声明
 */
@Composable
fun AppDrawer(
    currentRoute: String,
    onNavigate: (String) -> Unit,
    onModuleClick: (String) -> Unit,
    viewModel: DrawerViewModel = viewModel()
) {
    val extendedColors = LocalExtendedColors.current
    val categories by viewModel.categories.collectAsState()
    val stats by viewModel.stats.collectAsState()
    val moduleCounts by viewModel.moduleCounts.collectAsState()
    val themeMode by viewModel.themeMode.collectAsState()

    val navItems = listOf(
        DrawerNav(Icons.Filled.Home, "首页", com.fandex.app.ui.navigation.Routes.HOME),
        DrawerNav(Icons.Filled.Code, "语法速览", com.fandex.app.ui.navigation.Routes.SYNTAX),
        DrawerNav(Icons.Filled.Explore, "学习路线", com.fandex.app.ui.navigation.Routes.LEARNING_PATH),
        DrawerNav(Icons.Filled.Search, "搜索", com.fandex.app.ui.navigation.Routes.SEARCH)
    )

    Column(modifier = Modifier.fillMaxWidth()) {
        // ---------------------------------------------------------------
        // 固定顶部：品牌头部
        // ---------------------------------------------------------------
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .background(MaterialTheme.colorScheme.primary.copy(alpha = 0.08f))
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(4.dp)
        ) {
            Text(
                text = "FANDEX",
                style = MaterialTheme.typography.titleLarge,
                color = MaterialTheme.colorScheme.primary,
                fontWeight = FontWeight.ExtraBold
            )
            Text(
                text = "全栈知识速查体系",
                style = MaterialTheme.typography.bodySmall,
                color = extendedColors.fgSecondary
            )
            Text(
                text = "v${BuildConfig.VERSION_NAME} · fanquanpp",
                style = MaterialTheme.typography.labelSmall,
                color = extendedColors.fgTertiary
            )
            Spacer(modifier = Modifier.height(4.dp))
            Row(verticalAlignment = Alignment.CenterVertically) {
                DrawerStat("${stats.categoryCount}", "分类")
                DrawerStatDivider()
                DrawerStat("${stats.moduleCount}", "模块")
                DrawerStatDivider()
                DrawerStat("${stats.docCount}", "文档")
            }
        }

        // 品牌头部与固定分区之间的 1dp 分割线：增强分区层次
        HorizontalDivider(color = extendedColors.borderSubtle)

        // ---------------------------------------------------------------
        // 固定顶部：快捷导航（当前路由高亮，选中底色平滑过渡）
        // ---------------------------------------------------------------
        navItems.forEach { item ->
            val selected = currentRoute == item.route ||
                (item.route != com.fandex.app.ui.navigation.Routes.HOME &&
                    currentRoute.startsWith(item.route))
            // 选中态背景色 180ms 平滑过渡
            val itemBackground by animateColorAsState(
                targetValue = if (selected) MaterialTheme.colorScheme.primary.copy(alpha = 0.10f)
                else Color.Transparent,
                animationSpec = tween(durationMillis = 180),
                label = "drawerNavBg"
            )
            // 图标与文字颜色随选中态过渡
            val itemTint by animateColorAsState(
                targetValue = if (selected) MaterialTheme.colorScheme.primary
                else extendedColors.fgSecondary,
                animationSpec = tween(durationMillis = 180),
                label = "drawerNavTint"
            )
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .clickable { onNavigate(item.route) }
                    .background(itemBackground)
                    .padding(horizontal = 16.dp, vertical = 12.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                Icon(
                    imageVector = item.icon,
                    contentDescription = null,
                    tint = itemTint
                )
                Spacer(modifier = Modifier.width(12.dp))
                Text(
                    text = item.label,
                    style = MaterialTheme.typography.bodyLarge,
                    color = if (selected) MaterialTheme.colorScheme.primary
                    else MaterialTheme.colorScheme.onSurface,
                    fontWeight = if (selected) FontWeight.SemiBold else FontWeight.Normal
                )
            }
        }

        Spacer(modifier = Modifier.height(4.dp))
        HorizontalDivider(color = extendedColors.borderSubtle)

        // ---------------------------------------------------------------
        // 固定顶部：主题三选（紧凑分段）
        // ---------------------------------------------------------------
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = 16.dp, vertical = 10.dp),
            horizontalArrangement = Arrangement.spacedBy(6.dp)
        ) {
            listOf(
                ThemeMode.SYSTEM to "系统",
                ThemeMode.LIGHT to "浅色",
                ThemeMode.DARK to "深色"
            ).forEach { (mode, label) ->
                val selected = themeMode == mode
                Box(
                    modifier = Modifier
                        .weight(1f)
                        .clip(RoundedCornerShape(4.dp))
                        .background(
                            if (selected) MaterialTheme.colorScheme.primary
                            else extendedColors.bgElevated
                        )
                        .border(
                            1.dp,
                            if (selected) MaterialTheme.colorScheme.primary
                            else extendedColors.borderDefault,
                            RoundedCornerShape(4.dp)
                        )
                        .clickable { viewModel.setThemeMode(mode) }
                        .padding(vertical = 8.dp),
                    contentAlignment = Alignment.Center
                ) {
                    Text(
                        text = label,
                        style = MaterialTheme.typography.labelLarge,
                        color = if (selected) {
                            if (MaterialTheme.colorScheme.primary.isLightDrawer()) Color(0xFF0A0A0A)
                            else Color.White
                        } else extendedColors.fgSecondary
                    )
                }
            }
        }

        HorizontalDivider(color = extendedColors.borderSubtle)

        // ---------------------------------------------------------------
        // 滚动区域：模块快速导航（多彩分类）
        // ---------------------------------------------------------------
        Column(
            modifier = Modifier
                .weight(1f)
                .verticalScroll(rememberScrollState())
        ) {
            DrawerSectionTitle("模块导航")
            categories.forEach { category ->
                val color = CategoryColor.parse(category.colorHex)
                // 分类小节标题
                Row(
                    modifier = Modifier.padding(horizontal = 16.dp, vertical = 6.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Box(
                        modifier = Modifier
                            .width(3.dp)
                            .height(12.dp)
                            .clip(RoundedCornerShape(1.dp))
                            .background(color)
                    )
                    Spacer(modifier = Modifier.width(8.dp))
                    Text(
                        text = category.label,
                        style = MaterialTheme.typography.labelLarge,
                        color = extendedColors.fgSecondary,
                        fontWeight = FontWeight.SemiBold
                    )
                }
                // 模块行（点击直达模块页，带分类内序号与计数）
                category.modules.forEachIndexed { index, module ->
                    val interaction = remember { MutableInteractionSource() }
                    Row(
                        modifier = Modifier
                            .fillMaxWidth()
                            .pressScale(interaction)
                            .clickable(
                                interactionSource = interaction,
                                indication = null
                            ) { onModuleClick(module.id) }
                            .padding(horizontal = 24.dp, vertical = 8.dp),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        Text(
                            text = "%02d".format(index + 1),
                            fontFamily = androidx.compose.ui.text.font.FontFamily.Monospace,
                            fontWeight = FontWeight.SemiBold,
                            fontSize = 10.sp,
                            color = color.copy(alpha = 0.85f)
                        )
                        Spacer(modifier = Modifier.width(8.dp))
                        Box(
                            modifier = Modifier
                                .width(3.dp)
                                .height(16.dp)
                                .clip(RoundedCornerShape(1.dp))
                                .background(color)
                        )
                        Spacer(modifier = Modifier.width(10.dp))
                        Text(
                            text = module.title,
                            style = MaterialTheme.typography.bodyMedium,
                            color = MaterialTheme.colorScheme.onSurface,
                            maxLines = 1,
                            modifier = Modifier.weight(1f)
                        )
                        moduleCounts[module.id]?.let { count ->
                            Text(
                                text = "$count",
                                style = MaterialTheme.typography.labelSmall,
                                color = extendedColors.fgTertiary
                            )
                        }
                    }
                }
            }
        }

        // ---------------------------------------------------------------
        // 固定底部：免责声明
        // ---------------------------------------------------------------
        HorizontalDivider(color = extendedColors.borderSubtle)
        Text(
            text = "内容由人工与 AI 共同编写，请结合官方文档独立验证",
            style = MaterialTheme.typography.labelSmall,
            color = extendedColors.fgTertiary,
            modifier = Modifier.padding(16.dp)
        )
    }
}

/** 抽屉分区标题 */
@Composable
private fun DrawerSectionTitle(title: String) {
    Row(
        modifier = Modifier.padding(horizontal = 16.dp, vertical = 6.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        Box(
            modifier = Modifier
                .width(3.dp)
                .height(12.dp)
                .clip(RoundedCornerShape(1.dp))
                .background(MaterialTheme.colorScheme.primary)
        )
        Spacer(modifier = Modifier.width(8.dp))
        Text(
            text = title,
            style = MaterialTheme.typography.labelLarge,
            color = LocalExtendedColors.current.fgTertiary,
            fontWeight = FontWeight.SemiBold
        )
    }
}

/** 抽屉统计项 */
@Composable
private fun DrawerStat(value: String, label: String) {
    val extendedColors = LocalExtendedColors.current
    Row(verticalAlignment = Alignment.Bottom) {
        Text(
            text = value,
            style = MaterialTheme.typography.titleMedium,
            color = MaterialTheme.colorScheme.primary,
            fontWeight = FontWeight.Bold
        )
        Spacer(modifier = Modifier.width(2.dp))
        Text(
            text = label,
            style = MaterialTheme.typography.labelSmall,
            color = extendedColors.fgTertiary
        )
    }
}

/** 统计项分割竖线 */
@Composable
private fun DrawerStatDivider() {
    Box(
        modifier = Modifier
            .padding(horizontal = 12.dp)
            .width(1.dp)
            .height(14.dp)
            .background(LocalExtendedColors.current.borderSubtle)
    )
}

/** Color 亮度粗判 */
private fun Color.isLightDrawer(): Boolean {
    val lum = 0.299 * red + 0.587 * green + 0.114 * blue
    return lum > 0.6
}
