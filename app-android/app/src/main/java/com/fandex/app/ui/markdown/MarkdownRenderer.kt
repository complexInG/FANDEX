package com.fandex.app.ui.markdown

import androidx.compose.foundation.background
import androidx.compose.foundation.gestures.detectTapGestures
import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.CheckBox
import androidx.compose.material.icons.filled.CheckBoxOutlineBlank
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material.icons.filled.InsertDriveFile
import androidx.compose.material.icons.outlined.ContentCopy
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.toArgb
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.platform.LocalClipboardManager
import androidx.compose.ui.platform.LocalConfiguration
import androidx.compose.ui.platform.LocalUriHandler
import androidx.compose.ui.text.AnnotatedString
import androidx.compose.ui.text.SpanStyle
import androidx.compose.ui.text.TextLayoutResult
import androidx.compose.ui.text.buildAnnotatedString
import androidx.compose.ui.text.font.FontStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.text.withStyle
import androidx.compose.ui.unit.dp
import com.fandex.app.ui.theme.CodeTextStyle
import com.fandex.app.ui.theme.FandexExtendedColors
import com.fandex.app.ui.theme.InlineCodeStyle
import com.fandex.app.ui.theme.LocalExtendedColors
import org.commonmark.ext.gfm.strikethrough.StrikethroughExtension
import org.commonmark.ext.gfm.tables.TablesExtension
import org.commonmark.ext.task.list.items.TaskListItemsExtension
import org.commonmark.parser.Parser

/** 链接点击注解标签 */
private const val URL_TAG = "URL"

/**
 * Markdown 渲染引擎
 *
 * 使用 commonmark-java 解析 Markdown 为 AST，
 * 再将块级模型映射到 Jetpack Compose 组件：
 * - 标题 / 段落 / 加粗 / 斜体 / 删除线 / 内联代码
 * - 代码块（语法高亮 + 复制按钮 + 语言标签）
 * - 有序 / 无序 / 任务 / 嵌套列表
 * - 引用块与告警块（[!NOTE] 等）
 * - 表格 / 分隔线 / 链接点击 / 图片占位
 */
class MarkdownRenderer {

    private val parser: Parser = Parser.builder()
        .extensions(
            listOf(
                TablesExtension.create(),
                StrikethroughExtension.create(),
                TaskListItemsExtension.create()
            )
        )
        .build()

    /**
     * 解析 Markdown 为块级列表
     *
     * 供文档页 LazyColumn 分块渲染与目录提取使用
     */
    fun parse(markdown: String): List<MarkdownBlock> {
        val document = parser.parse(markdown)
        return MarkdownComposeVisitor().extractBlocks(document)
    }

    /**
     * 整体渲染（Column 顺序排列全部块）
     *
     * 适用于内容较短的页面；长文档请配合 parse + LazyColumn 使用
     */
    @Composable
    fun Render(markdown: String) {
        val blocks = remember(markdown) { parse(markdown) }
        Column(
            modifier = Modifier.fillMaxWidth(),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            blocks.forEach { block ->
                Block(block)
            }
        }
    }

    /**
     * 渲染单个块级元素（公开供文档页逐块渲染）
     */
    @Composable
    fun Block(block: MarkdownBlock) {
        when (block) {
            is MarkdownBlock.Heading -> HeadingBlock(block)
            is MarkdownBlock.Paragraph -> ParagraphBlock(block)
            is MarkdownBlock.CodeBlock -> CodeBlockView(block)
            is MarkdownBlock.ListBlock -> ListBlockView(block, depth = 0)
            is MarkdownBlock.BlockQuote -> BlockQuoteView(block)
            is MarkdownBlock.Admonition -> AdmonitionView(block)
            is MarkdownBlock.Table -> TableView(block)
            MarkdownBlock.ThematicBreak -> ThematicBreakView()
        }
    }
}

// ---------------------------------------------------------------------------
// 块级视图
// ---------------------------------------------------------------------------

/**
 * 标题块
 */
@Composable
private fun HeadingBlock(block: MarkdownBlock.Heading) {
    val style = when (block.level) {
        1 -> MaterialTheme.typography.headlineLarge
        2 -> MaterialTheme.typography.headlineMedium
        3 -> MaterialTheme.typography.headlineSmall
        4 -> MaterialTheme.typography.titleLarge
        else -> MaterialTheme.typography.titleMedium
    }
    Text(
        text = block.text,
        style = style,
        color = MaterialTheme.colorScheme.onSurface,
        fontWeight = FontWeight.SemiBold,
        modifier = Modifier
            .fillMaxWidth()
            .padding(top = if (block.level <= 2) 16.dp else 8.dp, bottom = 2.dp)
    )
}

/**
 * 段落块（支持链接点击与图片占位）
 */
@Composable
private fun ParagraphBlock(block: MarkdownBlock.Paragraph) {
    // 段落仅含图片时渲染为图片占位卡
    val images = block.segments.filterIsInstance<TextSegment.Image>()
    if (images.size == 1 && block.segments.size == 1) {
        ImagePlaceholder(images.first())
        return
    }

    val uriHandler = LocalUriHandler.current
    val extendedColors = LocalExtendedColors.current
    val primaryColor = MaterialTheme.colorScheme.primary
    val annotated = remember(block.segments, extendedColors, primaryColor) {
        buildAnnotatedStringFromSegments(block.segments, extendedColors, primaryColor)
    }
    val layoutResult = remember { mutableStateOf<TextLayoutResult?>(null) }

    Text(
        text = annotated,
        style = MaterialTheme.typography.bodyLarge,
        color = MaterialTheme.colorScheme.onSurface,
        onTextLayout = { layoutResult.value = it },
        modifier = Modifier
            .fillMaxWidth()
            .pointerInput(annotated) {
                detectTapGestures { position ->
                    layoutResult.value?.let { layout ->
                        val offset = layout.getOffsetForPosition(position)
                        annotated.getStringAnnotations(URL_TAG, offset, offset)
                            .firstOrNull()
                            ?.let { annotation ->
                                runCatching { uriHandler.openUri(annotation.item) }
                            }
                    }
                }
            }
    )
    // 与文本混排的内嵌图片：段落后补占位卡
    images.forEach { image ->
        ImagePlaceholder(image)
    }
}

/**
 * 代码块（语言标签 + 复制 + 语法高亮）
 *
 * mermaid 块走离线图表渲染（WebView + 内置 mermaid.min.js）
 */
@Composable
private fun CodeBlockView(block: MarkdownBlock.CodeBlock) {
    if (block.language.lowercase().trim() == "mermaid") {
        MermaidDiagram(code = block.code)
        return
    }
    val extendedColors = LocalExtendedColors.current
    val clipboard = LocalClipboardManager.current
    var copied by remember { mutableStateOf(false) }
    val scrollState = rememberScrollState()
    val highlighted = rememberHighlightedCode(block.code, block.language)

    Column(
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(8.dp))
            .background(extendedColors.codeBg)
    ) {
        // 头部：语言标签 + 复制按钮
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(start = 12.dp, end = 4.dp, top = 4.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            Text(
                text = block.language.ifEmpty { "text" },
                style = MaterialTheme.typography.labelSmall,
                color = extendedColors.fgTertiary
            )
            Spacer(modifier = Modifier.weight(1f))
            IconButton(onClick = {
                clipboard.setText(AnnotatedString(block.code))
                copied = true
            }) {
                Icon(
                    imageVector = if (copied) Icons.Filled.CheckCircle else Icons.Outlined.ContentCopy,
                    contentDescription = if (copied) "已复制" else "复制代码",
                    tint = if (copied) extendedColors.success else extendedColors.fgTertiary,
                    modifier = Modifier.size(16.dp)
                )
            }
        }
        Text(
            text = highlighted,
            style = CodeTextStyle,
            color = extendedColors.codeText,
            modifier = Modifier
                .fillMaxWidth()
                .padding(start = 12.dp, end = 12.dp, bottom = 12.dp)
                .horizontalScroll(scrollState)
        )
    }
}

/**
 * 列表块（含任务列表与嵌套渲染）
 */
@Composable
private fun ListBlockView(block: MarkdownBlock.ListBlock, depth: Int) {
    val extendedColors = LocalExtendedColors.current

    Column(
        modifier = Modifier
            .fillMaxWidth()
            .padding(start = if (depth > 0) 16.dp else 0.dp),
        verticalArrangement = Arrangement.spacedBy(4.dp)
    ) {
        block.items.forEachIndexed { index, item ->
            Row(verticalAlignment = Alignment.Top) {
                // 任务项渲染勾选框，普通项渲染序号 / 符号
                when {
                    item.checked != null -> {
                        Icon(
                            imageVector = if (item.checked) Icons.Filled.CheckBox else Icons.Filled.CheckBoxOutlineBlank,
                            contentDescription = null,
                            tint = if (item.checked) MaterialTheme.colorScheme.primary else extendedColors.fgTertiary,
                            modifier = Modifier
                                .size(18.dp)
                                .padding(top = 2.dp)
                        )
                        Spacer(modifier = Modifier.width(8.dp))
                    }
                    block.ordered -> {
                        Text(
                            text = "${block.startNum + index}. ",
                            style = MaterialTheme.typography.bodyLarge,
                            color = MaterialTheme.colorScheme.primary
                        )
                    }
                    else -> {
                        Text(
                            text = "- ",
                            style = MaterialTheme.typography.bodyLarge,
                            color = MaterialTheme.colorScheme.primary
                        )
                    }
                }
                Column(modifier = Modifier.weight(1f)) {
                    Text(
                        text = annotatedOf(item.segments),
                        style = MaterialTheme.typography.bodyLarge,
                        color = MaterialTheme.colorScheme.onSurface
                    )
                    // 嵌套子列表项
                    item.children.forEach { child ->
                        Row(verticalAlignment = Alignment.Top) {
                            Text(
                                text = "  - ",
                                style = MaterialTheme.typography.bodyLarge,
                                color = MaterialTheme.colorScheme.primary
                            )
                            Text(
                                text = annotatedOf(child.segments),
                                style = MaterialTheme.typography.bodyLarge,
                                color = MaterialTheme.colorScheme.onSurface
                            )
                        }
                    }
                }
            }
        }
    }
}

/**
 * 引用块
 */
@Composable
private fun BlockQuoteView(block: MarkdownBlock.BlockQuote) {
    val extendedColors = LocalExtendedColors.current

    Row(
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(0.dp, 8.dp, 8.dp, 0.dp))
            .background(extendedColors.bgSecondary)
    ) {
        Box(
            modifier = Modifier
                .width(3.dp)
                .fillMaxHeight()
                .background(MaterialTheme.colorScheme.primary.copy(alpha = 0.5f))
        )
        Column(
            modifier = Modifier
                .weight(1f)
                .padding(horizontal = 12.dp, vertical = 8.dp),
            verticalArrangement = Arrangement.spacedBy(6.dp)
        ) {
            block.paragraphs.forEach { paragraph ->
                Text(
                    text = annotatedOf(paragraph),
                    style = MaterialTheme.typography.bodyMedium,
                    color = extendedColors.fgSecondary
                )
            }
        }
    }
}

/**
 * 告警块（[!NOTE] / [!TIP] 等）
 *
 * 左侧主题色竖条 + 类型标题 + 内容段落
 */
@Composable
private fun AdmonitionView(block: MarkdownBlock.Admonition) {
    val extendedColors = LocalExtendedColors.current
    val accent = when (block.type) {
        "TIP", "SUCCESS" -> extendedColors.success
        "WARNING", "CAUTION" -> extendedColors.warning
        "DANGER", "FAILURE", "BUG" -> MaterialTheme.colorScheme.error
        "NOTE", "INFO" -> extendedColors.info
        else -> MaterialTheme.colorScheme.primary
    }

    Row(
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(0.dp, 8.dp, 8.dp, 0.dp))
            .background(accent.copy(alpha = 0.08f))
    ) {
        Box(
            modifier = Modifier
                .width(3.dp)
                .fillMaxHeight()
                .background(accent)
        )
        Column(
            modifier = Modifier
                .weight(1f)
                .padding(horizontal = 12.dp, vertical = 8.dp),
            verticalArrangement = Arrangement.spacedBy(6.dp)
        ) {
            Text(
                text = block.title,
                style = MaterialTheme.typography.labelLarge,
                color = accent,
                fontWeight = FontWeight.SemiBold
            )
            block.paragraphs.forEach { paragraph ->
                Text(
                    text = annotatedOf(paragraph),
                    style = MaterialTheme.typography.bodyMedium,
                    color = extendedColors.fgSecondary
                )
            }
        }
    }
}

/**
 * 图片占位卡
 *
 * 离线场景不加载网络位图，展示替代文本与来源
 */
@Composable
private fun ImagePlaceholder(image: TextSegment.Image) {
    val extendedColors = LocalExtendedColors.current

    Column(
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(8.dp))
            .background(extendedColors.bgSecondary)
            .padding(12.dp),
        verticalArrangement = Arrangement.spacedBy(4.dp)
    ) {
        Row(verticalAlignment = Alignment.CenterVertically) {
            Icon(
                imageVector = Icons.Filled.InsertDriveFile,
                contentDescription = null,
                tint = extendedColors.fgTertiary,
                modifier = Modifier.size(16.dp)
            )
            Spacer(modifier = Modifier.width(8.dp))
            Text(
                text = if (image.alt.isNotEmpty()) image.alt else "图片",
                style = MaterialTheme.typography.labelLarge,
                color = extendedColors.fgSecondary
            )
        }
        if (image.url.isNotEmpty()) {
            Text(
                text = image.url,
                style = MaterialTheme.typography.labelSmall,
                color = extendedColors.fgTertiary,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
        }
    }
}

/**
 * 表格
 *
 * 手机屏适配策略：
 * - 按各列最大内容长度占比分配列宽（设最小列宽兜底），保证列对齐
 * - 总宽超出屏幕时横向滚动（不使用 weight，避免滚动容器内权重宽度归零）
 */
@Composable
private fun TableView(block: MarkdownBlock.Table) {
    val extendedColors = LocalExtendedColors.current
    val scrollState = rememberScrollState()
    val screenWidthDp = LocalConfiguration.current.screenWidthDp.dp

    // 各列内容最大字符数（截断到 40，防止个别长列独占宽度）
    val columnCount = block.headers.size
    val columnChars = remember(block) {
        List(columnCount) { c ->
            val headerLen = block.headers.getOrNull(c)?.length ?: 0
            val bodyLen = block.rows.maxOfOrNull { row -> row.getOrNull(c)?.length ?: 0 } ?: 0
            maxOf(headerLen, bodyLen).coerceAtMost(40).coerceAtLeast(4)
        }
    }
    val totalChars = columnChars.sum().coerceAtLeast(1)
    // 可用宽度按 390dp 基准估算，列宽下限 88dp 保证可读
    val baseWidth = minOf(screenWidthDp, 390.dp) - 16.dp
    val columnWidths = columnChars.map { len ->
        maxOf(baseWidth * len / totalChars, 88.dp)
    }
    val tableWidth = columnWidths.reduce { acc, width -> acc + width }

    Column(
        modifier = Modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(8.dp))
            .background(extendedColors.bgSecondary)
            .horizontalScroll(scrollState)
    ) {
        // 表头
        Row {
            block.headers.forEachIndexed { c, header ->
                Text(
                    text = header,
                    style = MaterialTheme.typography.labelLarge,
                    color = MaterialTheme.colorScheme.onSurface,
                    fontWeight = FontWeight.SemiBold,
                    modifier = Modifier
                        .width(columnWidths[c])
                        .padding(8.dp)
                )
            }
        }
        // 表头分隔线（滚动容器内需显式宽度）
        Box(
            modifier = Modifier
                .width(tableWidth)
                .height(1.dp)
                .background(extendedColors.borderSubtle)
        )
        // 表数据
        block.rows.forEachIndexed { rowIndex, row ->
            Row {
                row.forEachIndexed { c, cell ->
                    Text(
                        text = cell,
                        style = MaterialTheme.typography.bodyMedium,
                        color = MaterialTheme.colorScheme.onSurface,
                        modifier = Modifier
                            .width(columnWidths.getOrElse(c) { 88.dp })
                            .padding(8.dp)
                    )
                }
            }
            if (rowIndex < block.rows.size - 1) {
                Box(
                    modifier = Modifier
                        .width(tableWidth)
                        .height(1.dp)
                        .background(extendedColors.borderSubtle.copy(alpha = 0.5f))
                )
            }
        }
    }
}

/**
 * 水平分隔线
 */
@Composable
private fun ThematicBreakView() {
    val extendedColors = LocalExtendedColors.current
    Box(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 4.dp)
            .height(1.dp)
            .background(extendedColors.borderSubtle)
    )
}

// ---------------------------------------------------------------------------
// 行内片段构建
// ---------------------------------------------------------------------------

/**
 * 组合内解析行内片段为 AnnotatedString（带主题色缓存键）
 */
@Composable
private fun annotatedOf(segments: List<TextSegment>): AnnotatedString {
    val extendedColors = LocalExtendedColors.current
    val primaryColor = MaterialTheme.colorScheme.primary
    return remember(segments, extendedColors, primaryColor) {
        buildAnnotatedStringFromSegments(segments, extendedColors, primaryColor)
    }
}

/**
 * 将行内片段序列构建为 AnnotatedString（非组合函数，可在 remember 计算中使用）
 *
 * 链接以 URL_TAG 注解承载地址，供点击手势解析
 */
private fun buildAnnotatedStringFromSegments(
    segments: List<TextSegment>,
    extendedColors: com.fandex.app.ui.theme.FandexExtendedColors,
    primaryColor: Color
): AnnotatedString {
    val codeBgColor = extendedColors.codeBg

    return buildAnnotatedString {
        segments.forEach { segment ->
            when (segment) {
                is TextSegment.Plain -> append(segment.text)
                is TextSegment.Bold -> withStyle(SpanStyle(fontWeight = FontWeight.Bold)) {
                    append(segment.text)
                }
                is TextSegment.Italic -> withStyle(SpanStyle(fontStyle = FontStyle.Italic)) {
                    append(segment.text)
                }
                is TextSegment.Strikethrough -> withStyle(
                    SpanStyle(textDecoration = TextDecoration.LineThrough)
                ) {
                    append(segment.text)
                }
                is TextSegment.InlineCode -> withStyle(
                    SpanStyle(
                        fontFamily = InlineCodeStyle.fontFamily,
                        // web 端内联代码使用深色底浅色字（双主题一致）
                        background = codeBgColor,
                        color = extendedColors.codeText
                    )
                ) {
                    append(segment.text)
                }
                is TextSegment.Link -> {
                    pushStringAnnotation(tag = URL_TAG, annotation = segment.url)
                    withStyle(
                        SpanStyle(color = primaryColor, textDecoration = TextDecoration.Underline)
                    ) {
                        append(segment.text)
                    }
                    pop()
                }
                is TextSegment.Image -> withStyle(
                    SpanStyle(color = extendedColors.fgTertiary, fontStyle = FontStyle.Italic)
                ) {
                    append(if (segment.alt.isNotEmpty()) "[图] ${segment.alt}" else "[图片]")
                }
                is TextSegment.SoftBreak -> append(" ")
                is TextSegment.HardBreak -> append("\n")
            }
        }
    }
}

/**
 * 目录条目
 *
 * @param level 标题级别（2-4）
 * @param title 标题文本
 * @param blockIndex 对应块在块列表中的下标（用于滚动定位）
 */
data class TocEntry(
    val level: Int,
    val title: String,
    val blockIndex: Int
)

/**
 * 从块列表提取目录（H2-H4）
 */
fun extractToc(blocks: List<MarkdownBlock>): List<TocEntry> {
    return blocks.mapIndexed { index, block ->
        if (block is MarkdownBlock.Heading && block.level in 2..4) {
            TocEntry(block.level, block.text, index)
        } else null
    }.filterNotNull()
}
