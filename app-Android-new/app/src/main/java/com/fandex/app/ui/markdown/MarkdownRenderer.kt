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
import androidx.compose.foundation.text.InlineTextContent
import androidx.compose.foundation.text.appendInlineContent
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
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.platform.LocalUriHandler
import androidx.compose.ui.text.AnnotatedString
import androidx.compose.ui.text.Placeholder
import androidx.compose.ui.text.PlaceholderVerticalAlign
import androidx.compose.ui.text.SpanStyle
import androidx.compose.ui.text.TextLayoutResult
import androidx.compose.ui.text.buildAnnotatedString
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.text.withStyle
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
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

/** 行内公式内嵌内容标签前缀 */
private const val MATH_TAG = "math-"

/**
 * Markdown 渲染引擎
 *
 * 使用 commonmark-java 解析 Markdown 为 AST，
 * 再将块级模型映射到 Jetpack Compose 组件：
 * - 标题 / 段落 / 加粗（模块色）/ 斜体 / 删除线 / 内联代码
 * - 代码块（语法高亮 + 复制按钮 + 语言标签）
 * - 块级数学公式（$$...$$，JLatexMath）与行内公式（$...$）
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
     * 块级公式（$$...$$）在进入 commonmark 之前先提取（避免被解析为普通段落），
     * 其余文本按原逻辑解析；供文档页 LazyColumn 分块渲染与目录提取使用
     */
    fun parse(markdown: String): List<MarkdownBlock> {
        val blocks = mutableListOf<MarkdownBlock>()
        for (segment in splitMathSegments(markdown)) {
            if (segment.isMath) {
                blocks.add(MarkdownBlock.MathBlock(segment.text.trim()))
            } else {
                val document = parser.parse(segment.text)
                blocks.addAll(MarkdownComposeVisitor().extractBlocks(document))
            }
        }
        return blocks
    }

    /**
     * 整体渲染（Column 顺序排列全部块）
     *
     * 适用于内容较短的页面；长文档请配合 parse + LazyColumn 使用
     */
    @Composable
    fun Render(markdown: String, accentColor: Color? = null) {
        val blocks = remember(markdown) { parse(markdown) }
        Column(
            modifier = Modifier.fillMaxWidth(),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            blocks.forEach { block ->
                Block(block, accentColor)
            }
        }
    }

    /**
     * 渲染单个块级元素（公开供文档页逐块渲染）
     *
     * @param accentColor 模块分类色，用于加粗文字着色（对齐 web 端 .prose strong）
     */
    @Composable
    fun Block(block: MarkdownBlock, accentColor: Color? = null) {
        when (block) {
            is MarkdownBlock.Heading -> HeadingBlock(block)
            is MarkdownBlock.Paragraph -> ParagraphBlock(block, accentColor)
            is MarkdownBlock.CodeBlock -> CodeBlockView(block)
            is MarkdownBlock.MathBlock -> MathBlockView(block.latex)
            is MarkdownBlock.ListBlock -> ListBlockView(block, accentColor, depth = 0)
            is MarkdownBlock.BlockQuote -> BlockQuoteView(block, accentColor)
            is MarkdownBlock.Admonition -> AdmonitionView(block, accentColor)
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
 * 段落块（支持链接点击、图片占位、行内公式与模块色加粗）
 */
@Composable
private fun ParagraphBlock(block: MarkdownBlock.Paragraph, accentColor: Color?) {
    // 段落仅含图片时渲染为图片占位卡
    val images = block.segments.filterIsInstance<TextSegment.Image>()
    if (images.size == 1 && block.segments.size == 1) {
        ImagePlaceholder(images.first())
        return
    }

    val uriHandler = LocalUriHandler.current
    val extendedColors = LocalExtendedColors.current
    val primaryColor = MaterialTheme.colorScheme.primary
    val markdown = rememberAnnotatedMarkdown(block.segments, extendedColors, primaryColor, accentColor)
    val layoutResult = remember { mutableStateOf<TextLayoutResult?>(null) }

    Text(
        text = markdown.annotated,
        inlineContent = markdown.inlineContent,
        style = MaterialTheme.typography.bodyLarge,
        color = MaterialTheme.colorScheme.onSurface,
        onTextLayout = { layoutResult.value = it },
        modifier = Modifier
            .fillMaxWidth()
            .pointerInput(markdown) {
                detectTapGestures { position ->
                    layoutResult.value?.let { layout ->
                        val offset = layout.getOffsetForPosition(position)
                        markdown.annotated.getStringAnnotations(URL_TAG, offset, offset)
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
private fun ListBlockView(block: MarkdownBlock.ListBlock, accentColor: Color?, depth: Int) {
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
                    MarkdownText(
                        segments = item.segments,
                        accentColor = accentColor,
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
                            MarkdownText(
                                segments = child.segments,
                                accentColor = accentColor,
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
private fun BlockQuoteView(block: MarkdownBlock.BlockQuote, accentColor: Color?) {
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
                MarkdownText(
                    segments = paragraph,
                    accentColor = accentColor,
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
private fun AdmonitionView(block: MarkdownBlock.Admonition, accentColor: Color?) {
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
                MarkdownText(
                    segments = paragraph,
                    accentColor = accentColor,
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

/** 组合内带行内公式的富文本结果 */
private data class AnnotatedMarkdown(
    val annotated: AnnotatedString,
    val inlineContent: Map<String, InlineTextContent>
)

/**
 * 组合内构建富文本（带主题色缓存键与行内公式位图）
 */
@Composable
private fun MarkdownText(
    segments: List<TextSegment>,
    accentColor: Color?,
    style: androidx.compose.ui.text.TextStyle,
    color: Color
) {
    val extendedColors = LocalExtendedColors.current
    val primaryColor = MaterialTheme.colorScheme.primary
    val markdown = rememberAnnotatedMarkdown(segments, extendedColors, primaryColor, accentColor)
    Text(
        text = markdown.annotated,
        inlineContent = markdown.inlineContent,
        style = style,
        color = color
    )
}

/**
 * 构建带行内公式的富文本
 *
 * 行内公式从 Plain 片段中以 $...$ 提取（与 web 端 remark-mask 相同的启发式：
 * 定界符内侧不留空白），位图同步渲染（行内公式规模小，耗时可忽略）
 */
@Composable
private fun rememberAnnotatedMarkdown(
    segments: List<TextSegment>,
    extendedColors: FandexExtendedColors,
    primaryColor: Color,
    accentColor: Color?
): AnnotatedMarkdown {
    val density = LocalDensity.current
    val onSurface = MaterialTheme.colorScheme.onSurface
    val mathKeys = remember(segments) { extractInlineMath(segments) }
    val textSizePx = inlineMathTextSizePx(density)
    val bitmaps = remember(mathKeys, onSurface, textSizePx) {
        mathKeys.associateWith { latex -> renderMathBitmap(latex, onSurface.toArgb(), textSizePx) }
    }
    // InlineTextContent 为 @Composable 构造，需在组合上下文完成
    val mathIds = remember(mathKeys) { mathKeys.mapIndexed { i, _ -> "$MATH_TAG$i" } }
    val mathContents = remember(bitmaps, mathIds) {
        mutableMapOf<String, InlineTextContent>().apply {
            mathKeys.forEachIndexed { i, latex ->
                val bitmap = bitmaps[latex] ?: return@forEachIndexed
                val (wSp, hSp) = inlineMathPlaceholder(bitmap.width, bitmap.height)
                put(
                    mathIds[i],
                    InlineTextContent(Placeholder(wSp.sp, hSp.sp, PlaceholderVerticalAlign.TextCenter)) {
                        androidx.compose.foundation.Image(
                            bitmap = bitmap,
                            contentDescription = null,
                            modifier = Modifier.fillMaxWidth()
                        )
                    }
                )
            }
        }.toMap()
    }
    return remember(segments, extendedColors, primaryColor, accentColor, mathIds, mathContents) {
        buildAnnotatedMarkdown(segments, extendedColors, primaryColor, accentColor, mathIds, mathContents)
    }
}

/**
 * 将行内片段序列构建为富文本（非组合函数，可在 remember 计算中使用）
 *
 * - 链接以 URL_TAG 注解承载地址，供点击手势解析
 * - 加粗文字使用模块分类色（对齐 web 端 .prose strong 的 --module-color）
 * - 行内公式以内嵌内容承载，未渲染成功的回退为等宽源文本
 */
private fun buildAnnotatedMarkdown(
    segments: List<TextSegment>,
    extendedColors: FandexExtendedColors,
    primaryColor: Color,
    accentColor: Color?,
    mathIds: List<String>,
    mathContents: Map<String, InlineTextContent>
): AnnotatedMarkdown {
    val codeBgColor = extendedColors.codeBg
    val boldColor = accentColor ?: Color.Unspecified
    var mathIndex = 0

    val annotated = buildAnnotatedString {
        segments.forEach { segment ->
            when (segment) {
                is TextSegment.Plain -> {
                    // 拆分行内公式
                    var rest = segment.text
                    while (rest.isNotEmpty()) {
                        val match = INLINE_MATH_RE.find(rest)
                        if (match == null) {
                            append(rest)
                            break
                        }
                        append(rest.substring(0, match.range.first))
                        val latex = match.groupValues[1]
                        val id = mathIds.getOrNull(mathIndex)
                        if (id != null && mathContents.containsKey(id)) {
                            appendInlineContent(id, "［公式］")
                        } else {
                            // 回退：等宽源文本
                            withStyle(
                                SpanStyle(fontFamily = FontFamily.Monospace, color = primaryColor)
                            ) { append(latex) }
                        }
                        mathIndex++
                        rest = rest.substring(match.range.last + 1)
                    }
                }
                is TextSegment.Bold -> withStyle(
                    SpanStyle(fontWeight = FontWeight.Bold, color = boldColor)
                ) {
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
                        // 亮色浅底深字 / 暗色深底浅字（对齐 web 端行内代码观感）
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
    return AnnotatedMarkdown(annotated, mathContents)
}

/**
 * 行内公式正则：$...$，内容不含 $ 与换行、且定界符内侧不留空白
 * （"价格 $5 和 $10" 这类货币写法不会误判）
 */
private val INLINE_MATH_RE = Regex("\\$([^\\$\n\\s][^$\n]*[^$\n\\s]|[^$\n\\s])\\$")

/** 从片段集合中提取全部行内公式（作为位图缓存键） */
private fun extractInlineMath(segments: List<TextSegment>): List<String> {
    val keys = mutableListOf<String>()
    segments.forEach { segment ->
        if (segment is TextSegment.Plain) {
            INLINE_MATH_RE.findAll(segment.text).forEach { keys.add(it.groupValues[1]) }
        }
    }
    return keys.distinct()
}

// ---------------------------------------------------------------------------
// 块级公式预提取
// ---------------------------------------------------------------------------

/** 解析分段：isMath 为 true 时 text 为公式体 */
private data class ParsedSegment(val isMath: Boolean, val text: String)

/**
 * 围栏感知的 $$...$$ 预提取
 *
 * 代码围栏（``` / ~~~）内出现的 $$ 视为普通文本不参与提取；
 * 跨行公式块被切出后，剩余文本保持行结构供 commonmark 正常解析
 */
private fun splitMathSegments(markdown: String): List<ParsedSegment> {
    val segments = mutableListOf<ParsedSegment>()
    val lines = markdown.split('\n')
    val buf = StringBuilder()
    var inFence = false
    var fenceMark = "```"

    fun flush() {
        if (buf.isNotBlank()) segments.add(ParsedSegment(false, buf.toString()))
        buf.clear()
    }

    var i = 0
    while (i < lines.size) {
        val line = lines[i]
        val trimmed = line.trimStart()
        if (!inFence && (trimmed.startsWith("```") || trimmed.startsWith("~~~"))) {
            inFence = true
            fenceMark = trimmed.take(3)
            buf.append(line).append('\n')
            i++
            continue
        }
        if (inFence) {
            buf.append(line).append('\n')
            if (trimmed.startsWith(fenceMark)) inFence = false
            i++
            continue
        }
        if (trimmed.startsWith("$$")) {
            val rest = trimmed.removePrefix("$$")
            val inlineClose = rest.indexOf("$$")
            if (inlineClose >= 0) {
                // 单行 $$...$$
                flush()
                segments.add(ParsedSegment(true, rest.take(inlineClose)))
                buf.append(rest.substring(inlineClose + 2)).append('\n')
                i++
                continue
            }
            // 跨行块：向后查找闭合 $$
            val mathLines = mutableListOf<String>()
            if (rest.isNotBlank()) mathLines.add(rest)
            var j = i + 1
            var closed = false
            while (j < lines.size) {
                val closeIdx = lines[j].indexOf("$$")
                if (closeIdx >= 0) {
                    val before = lines[j].take(closeIdx)
                    if (before.isNotBlank()) mathLines.add(before)
                    closed = true
                    break
                }
                mathLines.add(lines[j])
                j++
            }
            if (closed) {
                flush()
                segments.add(ParsedSegment(true, mathLines.joinToString("\n").trim()))
                i = j + 1
                continue
            }
            // 未闭合：按普通文本处理
            buf.append(line).append('\n')
            i++
            continue
        }
        buf.append(line).append('\n')
        i++
    }
    flush()
    return segments
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
