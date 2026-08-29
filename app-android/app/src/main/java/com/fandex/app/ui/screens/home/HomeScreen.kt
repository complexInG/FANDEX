package com.fandex.app.ui.screens.home

import androidx.compose.animation.Crossfade
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
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
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
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
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.fandex.app.data.model.CategoryInfo
import com.fandex.app.ui.common.fandexEntrance
import com.fandex.app.ui.common.pressScale
import com.fandex.app.ui.common.tweenNormal
import com.fandex.app.ui.components.CategoryColor
import com.fandex.app.ui.components.FilterChip
import com.fandex.app.ui.components.ModuleCard
import com.fandex.app.ui.components.ThemeQuickToggle
import com.fandex.app.ui.components.TopDock
import com.fandex.app.ui.theme.LocalExtendedColors

/**
 * 首页
 *
 * 参考旧版 FANDEX-App 主页设计：开门见山直入内容
 * - 顶部 Dock：抽屉菜单 + 品牌名 + 常驻功能按钮
 * - 分类筛选 chips（多彩，选中态高亮）
 * - 模块内容列表（按分类分组）
 *
 * 动效：
 * - Loading / Error / Success 状态切换使用 Crossfade（220ms）
 * - 首次进入成功态时，chips / 最近浏览 / 区块标题 / 模块卡片
 *   以 fandexEntrance 做 stagger 入场（仅首次播放一次）
 */
@Composable
fun HomeScreen(
    onModuleClick: (String) -> Unit,
    onDocClick: (String, String) -> Unit,
    onSyntax: () -> Unit,
    onLearningPath: () -> Unit,
    onSearch: () -> Unit,
    onOpenDrawer: () -> Unit,
    viewModel: HomeViewModel = viewModel()
) {
    val state by viewModel.state.collectAsState()
    val recentDocs by viewModel.recentDocs.collectAsState()

    // 当前筛选分类（null = 全部）
    var selectedCategory by remember { mutableStateOf<String?>(null) }

    // 入场门控：内容就绪后的下一帧置 true，触发首次 stagger 入场
    var hasEntered by remember { mutableStateOf(false) }
    val dataReady = state is HomeUiState.Success
    LaunchedEffect(dataReady) {
        if (dataReady) hasEntered = true
    }

    LaunchedEffect(Unit) {
        viewModel.load()
    }

    Scaffold(
        topBar = {
            TopDock(
                title = "FANDEX",
                showBack = false,
                onBack = {},
                onOpenDrawer = onOpenDrawer,
                onSyntax = onSyntax,
                onLearningPath = onLearningPath,
                onSearch = onSearch,
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
                label = "homeStateCrossfade"
            ) { current ->
                when (current) {
                    is HomeUiState.Loading -> LoadingView()
                    is HomeUiState.Error -> ErrorView(
                        message = current.message,
                        onRetry = { viewModel.load() }
                    )
                    is HomeUiState.Success -> {
                        val data = current
                        // 筛选后的分类列表
                        val visibleCategories = selectedCategory
                            ?.let { id -> data.categories.filter { it.id == id } }
                            ?: data.categories

                        HomeContent(
                            categories = visibleCategories,
                            recentDocs = recentDocs,
                            hasEntered = hasEntered,
                            selectedCategory = selectedCategory,
                            onSelectCategory = { selectedCategory = it },
                            onModuleClick = onModuleClick,
                            onDocClick = onDocClick
                        )
                    }
                }
            }
        }
    }
}

/**
 * 首页内容（成功态）
 *
 * @param entranceBases 各分类区块的入场下标基数（前置区块数累计，保证 stagger 递增）
 */
@Composable
private fun HomeContent(
    categories: List<CategoryInfo>,
    recentDocs: List<com.fandex.app.data.prefs.HistoryEntry>,
    hasEntered: Boolean,
    selectedCategory: String?,
    onSelectCategory: (String?) -> Unit,
    onModuleClick: (String) -> Unit,
    onDocClick: (String, String) -> Unit
) {
    // 入场下标基数：chips 占 0；最近浏览标题占 1、卡片占 2..n+1；
    // 各分类区块按（标题 + 模块数）累计，保证 stagger 下标全局递增
    val entranceBases = remember(categories, recentDocs) {
        var acc = recentDocs.size + 2
        categories.map { category ->
            val base = acc
            acc += category.modules.size + 1
            base
        }
    }

    LazyColumn(
        modifier = Modifier.fillMaxSize(),
        contentPadding = PaddingValues(bottom = 16.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        // 分类筛选 chips（横滑，多彩，选中态高亮；逐个 stagger 入场）
        item(key = "filters") {
            LazyRow(
                contentPadding = PaddingValues(horizontal = 16.dp),
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                item {
                    FilterChip(
                        label = "全部",
                        selected = selectedCategory == null,
                        color = MaterialTheme.colorScheme.primary,
                        onClick = { onSelectCategory(null) },
                        modifier = Modifier.fandexEntrance(index = 0, visible = hasEntered)
                    )
                }
                itemsIndexed(
                    items = categories,
                    key = { _, category -> category.id }
                ) { chipIndex, category ->
                    FilterChip(
                        label = category.label,
                        selected = selectedCategory == category.id,
                        color = CategoryColor.parse(category.colorHex),
                        onClick = {
                            onSelectCategory(
                                if (selectedCategory == category.id) null else category.id
                            )
                        },
                        modifier = Modifier.fandexEntrance(
                            index = chipIndex + 1,
                            visible = hasEntered
                        )
                    )
                }
            }
        }

        // 最近浏览（有历史时展示，紧凑单行）
        if (recentDocs.isNotEmpty()) {
            item(key = "recent") {
                RecentDocsSection(
                    docs = recentDocs,
                    hasEntered = hasEntered,
                    onDocClick = onDocClick
                )
            }
        }

        // 分类模块内容（筛选切换时对位置变化做重排动画）
        itemsIndexed(
            items = categories,
            key = { _, category -> category.id }
        ) { index, category ->
            CategorySection(
                category = category,
                entranceBase = entranceBases[index],
                hasEntered = hasEntered,
                onModuleClick = onModuleClick,
                modifier = Modifier.animateItem()
            )
        }
    }
}

/**
 * 最近浏览区块（紧凑横滑，直达文档）
 */
@Composable
private fun RecentDocsSection(
    docs: List<com.fandex.app.data.prefs.HistoryEntry>,
    hasEntered: Boolean,
    onDocClick: (String, String) -> Unit
) {
    val extendedColors = LocalExtendedColors.current

    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
        // 区块标题
        SectionHeader(
            label = "最近浏览",
            modifier = Modifier
                .padding(horizontal = 16.dp)
                .fandexEntrance(index = 1, visible = hasEntered)
        )
        androidx.compose.foundation.lazy.LazyRow(
            contentPadding = PaddingValues(horizontal = 16.dp),
            horizontalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            items(docs.size, key = { "${docs[it].module}/${docs[it].slug}" }) { index ->
                val doc = docs[index]
                val interaction = remember { MutableInteractionSource() }
                Column(
                    modifier = Modifier
                        .width(168.dp)
                        .fandexEntrance(index = index + 2, visible = hasEntered)
                        .pressScale(interaction)
                        .clip(RoundedCornerShape(4.dp))
                        .background(extendedColors.bgElevated)
                        .border(1.dp, extendedColors.borderDefault, RoundedCornerShape(4.dp))
                        .clickable(
                            interactionSource = interaction,
                            indication = null
                        ) { onDocClick(doc.module, doc.slug) }
                        .padding(12.dp),
                    verticalArrangement = Arrangement.spacedBy(4.dp)
                ) {
                    Text(
                        text = doc.moduleTitle.ifEmpty { doc.module },
                        style = MaterialTheme.typography.labelSmall,
                        color = MaterialTheme.colorScheme.primary
                    )
                    Text(
                        text = doc.title,
                        style = MaterialTheme.typography.bodyMedium,
                        color = MaterialTheme.colorScheme.onSurface,
                        fontWeight = FontWeight.Medium,
                        maxLines = 2,
                        overflow = TextOverflow.Ellipsis,
                        minLines = 2
                    )
                }
            }
        }
    }
}

/**
 * 分类区块
 *
 * @param entranceBase 区块内元素入场的下标基数（标题在前，卡片依次递增）
 */
@Composable
private fun CategorySection(
    category: CategoryInfo,
    entranceBase: Int,
    hasEntered: Boolean,
    onModuleClick: (String) -> Unit,
    modifier: Modifier = Modifier
) {
    val categoryColor = CategoryColor.parse(category.colorHex)

    Column(
        modifier = modifier,
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        // 分类标题栏
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = 16.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            SectionHeader(
                label = category.label,
                color = categoryColor,
                trailing = "${category.modules.size}",
                modifier = Modifier.fandexEntrance(index = entranceBase, visible = hasEntered)
            )
        }

        // 模块卡片列表（带分类内学习顺序编号 + stagger 入场）
        Column(
            modifier = Modifier.padding(horizontal = 16.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            category.modules.forEachIndexed { index, module ->
                ModuleCard(
                    module = module,
                    categoryColor = categoryColor,
                    onClick = { onModuleClick(module.id) },
                    indexLabel = "%02d".format(index + 1),
                    modifier = Modifier.fandexEntrance(
                        index = entranceBase + 1 + index,
                        visible = hasEntered
                    )
                )
            }
        }
    }
}

/**
 * 区块标题（竖条 + 标签 + 可选计数）
 */
@Composable
private fun SectionHeader(
    label: String,
    color: Color = MaterialTheme.colorScheme.primary,
    trailing: String? = null,
    modifier: Modifier = Modifier
) {
    val extendedColors = LocalExtendedColors.current
    Row(
        modifier = modifier,
        verticalAlignment = Alignment.CenterVertically
    ) {
        Box(
            modifier = Modifier
                .width(3.dp)
                .height(14.dp)
                .clip(RoundedCornerShape(2.dp))
                .background(color)
        )
        Spacer(modifier = Modifier.width(8.dp))
        Text(
            text = label,
            style = MaterialTheme.typography.titleMedium,
            color = MaterialTheme.colorScheme.onSurface,
            fontWeight = FontWeight.Bold
        )
        if (trailing != null) {
            Spacer(modifier = Modifier.width(8.dp))
            Text(
                text = trailing,
                style = MaterialTheme.typography.labelSmall,
                color = extendedColors.fgTertiary,
                modifier = Modifier
                    .clip(RoundedCornerShape(4.dp))
                    .background(extendedColors.bgElevated)
                    .border(1.dp, extendedColors.borderSubtle, RoundedCornerShape(4.dp))
                    .padding(horizontal = 8.dp, vertical = 1.dp)
            )
        }
    }
}

/**
 * 加载中视图
 */
@Composable
private fun LoadingView() {
    Box(
        modifier = Modifier.fillMaxSize(),
        contentAlignment = Alignment.Center
    ) {
        CircularProgressIndicator()
    }
}

/**
 * 错误视图
 */
@Composable
private fun ErrorView(message: String, onRetry: () -> Unit) {
    val extendedColors = LocalExtendedColors.current
    Box(
        modifier = Modifier
            .fillMaxSize()
            .padding(32.dp),
        contentAlignment = Alignment.Center
    ) {
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            Text(
                text = message,
                style = MaterialTheme.typography.bodyLarge,
                color = extendedColors.fgSecondary
            )
            Text(
                text = "点击重试",
                style = MaterialTheme.typography.labelLarge,
                color = MaterialTheme.colorScheme.primary,
                modifier = Modifier.clickable { onRetry() }
            )
        }
    }
}
