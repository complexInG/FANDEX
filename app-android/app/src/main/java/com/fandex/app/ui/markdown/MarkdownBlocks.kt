package com.fandex.app.ui.markdown

import org.commonmark.ext.gfm.strikethrough.Strikethrough
import org.commonmark.ext.gfm.tables.TableBlock
import org.commonmark.ext.gfm.tables.TableBody
import org.commonmark.ext.gfm.tables.TableCell
import org.commonmark.ext.gfm.tables.TableHead
import org.commonmark.ext.gfm.tables.TableRow
import org.commonmark.ext.task.list.items.TaskListItemMarker
import org.commonmark.node.AbstractVisitor
import org.commonmark.node.BlockQuote
import org.commonmark.node.BulletList
import org.commonmark.node.Code
import org.commonmark.node.CustomBlock
import org.commonmark.node.CustomNode
import org.commonmark.node.Emphasis
import org.commonmark.node.FencedCodeBlock
import org.commonmark.node.HardLineBreak
import org.commonmark.node.Heading
import org.commonmark.node.Image
import org.commonmark.node.IndentedCodeBlock
import org.commonmark.node.Link
import org.commonmark.node.ListBlock
import org.commonmark.node.ListItem
import org.commonmark.node.OrderedList
import org.commonmark.node.Paragraph
import org.commonmark.node.SoftLineBreak
import org.commonmark.node.StrongEmphasis
import org.commonmark.node.Text
import org.commonmark.node.ThematicBreak

/**
 * Markdown 块级元素数据模型
 *
 * 访问器将 commonmark AST 扁平化为本模型，供 Compose 渲染层消费
 */
sealed class MarkdownBlock {
    /** 标题（level 1-6） */
    data class Heading(val level: Int, val text: String) : MarkdownBlock()

    /** 段落（行内片段序列） */
    data class Paragraph(val segments: List<TextSegment>) : MarkdownBlock()

    /** 围栏/缩进代码块 */
    data class CodeBlock(val language: String, val code: String) : MarkdownBlock()

    /** 列表（有序/无序/任务列表统一建模，支持一层以上嵌套） */
    data class ListBlock(
        val ordered: Boolean,
        val startNum: Int,
        val items: List<ListItemNode>
    ) : MarkdownBlock()

    /** 引用块 */
    data class BlockQuote(val paragraphs: List<List<TextSegment>>) : MarkdownBlock()

    /** 告警块（对齐 web 端 remark-admonition：[!NOTE] / [!TIP] 等） */
    data class Admonition(
        val type: String,
        val title: String,
        val paragraphs: List<List<TextSegment>>
    ) : MarkdownBlock()

    /** 表格 */
    data class Table(val headers: List<String>, val rows: List<List<String>>) : MarkdownBlock()

    /** 水平分隔线 */
    object ThematicBreak : MarkdownBlock()
}

/**
 * 列表项节点
 *
 * @param segments 行内内容
 * @param checked 任务列表勾选态；null 表示普通列表项
 * @param children 嵌套子列表项
 */
data class ListItemNode(
    val segments: List<TextSegment>,
    val checked: Boolean? = null,
    val children: List<ListItemNode> = emptyList()
)

/**
 * 行内片段（段落 / 列表项 / 引用内容中的内联元素）
 */
sealed class TextSegment {
    data class Plain(val text: String) : TextSegment()
    data class Bold(val text: String) : TextSegment()
    data class Italic(val text: String) : TextSegment()
    data class Strikethrough(val text: String) : TextSegment()
    data class InlineCode(val text: String) : TextSegment()
    data class Link(val text: String, val url: String) : TextSegment()

    /** 图片（离线场景渲染为占位卡片，展示 alt 与地址） */
    data class Image(val url: String, val alt: String) : TextSegment()

    object SoftBreak : TextSegment()
    object HardBreak : TextSegment()
}

/**
 * 告警块类型定义
 *
 * 对齐 web 端 remark-admonition 支持的类型集合，
 * label 为中文标题，kind 用于主题配色
 */
enum class AdmonitionType(val label: String) {
    NOTE("注意"),
    TIP("技巧"),
    WARNING("警告"),
    DANGER("危险"),
    INFO("信息"),
    CAUTION("当心"),
    IMPORTANT("重要"),
    EXAMPLE("示例"),
    SUCCESS("成功"),
    QUOTE("引用"),
    QUESTION("问题"),
    FAILURE("失败"),
    BUG("缺陷"),
    ABSTRACT("摘要"),
    TODO("待办");

    companion object {
        /** 按标记解析类型（大小写不敏感），未匹配时返回 null */
        fun fromMarker(marker: String): AdmonitionType? {
            return entries.find { it.name.equals(marker, ignoreCase = true) }
        }
    }
}

/**
 * commonmark-java AST 访问器
 *
 * 遍历 AST 并提取块级元素数据，供 Compose 组件渲染
 */
class MarkdownComposeVisitor : AbstractVisitor() {

    private val blocks = mutableListOf<MarkdownBlock>()

    /** 当前正在收集的行内片段缓冲 */
    private var currentTextSegments = mutableListOf<TextSegment>()

    /** 引用块 / 告警块内部的段落缓冲 */
    private val quoteParagraphs = mutableListOf<List<TextSegment>>()

    /**
     * 提取块级元素
     */
    fun extractBlocks(document: org.commonmark.node.Node): List<MarkdownBlock> {
        blocks.clear()
        quoteParagraphs.clear()
        currentTextSegments = mutableListOf()
        document.accept(this)
        return blocks.toList()
    }

    // ------------------------------------------------------------------
    // 块级节点
    // ------------------------------------------------------------------

    override fun visit(heading: Heading) {
        flushParagraph()
        blocks.add(MarkdownBlock.Heading(heading.level, inlineText(heading)))
    }

    override fun visit(fencedCodeBlock: FencedCodeBlock) {
        flushParagraph()
        blocks.add(
            MarkdownBlock.CodeBlock(
                language = fencedCodeBlock.info.toString().trim(),
                code = fencedCodeBlock.literal.trimEnd('\n')
            )
        )
    }

    override fun visit(indentedCodeBlock: IndentedCodeBlock) {
        flushParagraph()
        blocks.add(MarkdownBlock.CodeBlock(language = "", code = indentedCodeBlock.literal.trimEnd('\n')))
    }

    override fun visit(bulletList: BulletList) {
        flushParagraph()
        blocks.add(collectList(bulletList, ordered = false, startNum = 1))
    }

    override fun visit(orderedList: OrderedList) {
        flushParagraph()
        blocks.add(collectList(orderedList, ordered = true, startNum = orderedList.markerStartNumber))
    }

    override fun visit(blockQuote: BlockQuote) {
        flushParagraph()
        // 先探测告警块标记：首段落首个 Text 形如 "[!NOTE] ..."
        val marker = detectAdmonitionMarker(blockQuote)
        if (marker != null) {
            val (type, markerLength) = marker
            // 跳过标记文本后收集剩余段落
            collectQuoteParagraphs(blockQuote, skipMarker = markerLength)
            blocks.add(MarkdownBlock.Admonition(type.name, type.label, quoteParagraphs.toList()))
        } else {
            collectQuoteParagraphs(blockQuote)
            blocks.add(MarkdownBlock.BlockQuote(quoteParagraphs.toList()))
        }
        quoteParagraphs.clear()
    }

    override fun visit(thematicBreak: ThematicBreak) {
        flushParagraph()
        blocks.add(MarkdownBlock.ThematicBreak)
    }

    override fun visit(customBlock: CustomBlock) {
        when (customBlock) {
            is TableBlock -> {
                flushParagraph()
                collectTable(customBlock)?.let { blocks.add(it) }
            }
            else -> visitChildren(customBlock)
        }
    }

    // ------------------------------------------------------------------
    // 行内节点
    // ------------------------------------------------------------------

    override fun visit(text: Text) {
        currentTextSegments.add(TextSegment.Plain(text.literal))
    }

    override fun visit(emphasis: Emphasis) {
        currentTextSegments.add(TextSegment.Italic(inlineText(emphasis)))
    }

    override fun visit(strongEmphasis: StrongEmphasis) {
        currentTextSegments.add(TextSegment.Bold(inlineText(strongEmphasis)))
    }

    override fun visit(code: Code) {
        currentTextSegments.add(TextSegment.InlineCode(code.literal))
    }

    override fun visit(link: Link) {
        currentTextSegments.add(TextSegment.Link(inlineText(link), link.destination))
    }

    override fun visit(image: Image) {
        currentTextSegments.add(TextSegment.Image(image.destination, inlineText(image)))
    }

    override fun visit(softLineBreak: SoftLineBreak) {
        currentTextSegments.add(TextSegment.SoftBreak)
    }

    override fun visit(hardLineBreak: HardLineBreak) {
        currentTextSegments.add(TextSegment.HardBreak)
    }

    override fun visit(customNode: CustomNode) {
        when (customNode) {
            is Strikethrough -> {
                currentTextSegments.add(TextSegment.Strikethrough(inlineText(customNode)))
            }
            // 任务列表勾选标记：由 collectList 在列表项层面处理，行内不输出
            is TaskListItemMarker -> Unit
            else -> visitChildren(customNode)
        }
    }

    // ------------------------------------------------------------------
    // 收集逻辑
    // ------------------------------------------------------------------

    /**
     * 收集列表为 ListBlock（递归支持嵌套）
     */
    private fun collectList(listBlock: ListBlock, ordered: Boolean, startNum: Int): MarkdownBlock.ListBlock {
        val items = mutableListOf<ListItemNode>()
        var child = listBlock.firstChild
        while (child != null) {
            if (child is ListItem) {
                items.add(collectListItem(child))
            }
            child = child.next
        }
        return MarkdownBlock.ListBlock(ordered, startNum, items)
    }

    /**
     * 收集单个列表项：段落片段 + 任务勾选态 + 嵌套子列表
     */
    private fun collectListItem(item: ListItem): ListItemNode {
        val segments = mutableListOf<TextSegment>()
        var checked: Boolean? = null
        val children = mutableListOf<ListItemNode>()

        var child = item.firstChild
        while (child != null) {
            when (child) {
                is Paragraph -> {
                    // 任务列表标记位于首段落开头，提出后记录勾选态
                    val first = child.firstChild
                    if (first is TaskListItemMarker) {
                        checked = first.isChecked
                        // 剩余内容作为片段收集
                        val marker = first
                        currentTextSegments = mutableListOf()
                        var node = marker.next
                        while (node != null) {
                            node.accept(this)
                            node = node.next
                        }
                        segments.addAll(currentTextSegments)
                        restoreSegmentBuffer()
                    } else {
                        segments.addAll(inlineSegments(child))
                    }
                }
                is BulletList -> {
                    children.add(collectListItemChildren(child, ordered = false))
                }
                is OrderedList -> {
                    children.add(collectListItemChildren(child, ordered = true))
                }
            }
            child = child.next
        }
        return ListItemNode(segments, checked, children)
    }

    /** 嵌套列表项：ListBlock -> 单元素列表项链（简化渲染层） */
    private fun collectListItemChildren(listBlock: ListBlock, ordered: Boolean): ListItemNode {
        val subItems = mutableListOf<ListItemNode>()
        var child = listBlock.firstChild
        while (child != null) {
            if (child is ListItem) {
                subItems.add(collectListItem(child))
            }
            child = child.next
        }
        // 嵌套列表以合成列表项承载，segments 为空，children 为子项
        return ListItemNode(segments = emptyList(), checked = null, children = subItems)
    }

    /**
     * 引用块 / 告警块段落收集
     *
     * @param skipMarkerInFirstText 需要从首个 Text 中剔除的标记文本长度
     */
    private fun collectQuoteParagraphs(quote: BlockQuote, skipMarker: Int = 0) {
        quoteParagraphs.clear()
        var child = quote.firstChild
        while (child != null) {
            if (child is Paragraph) {
                val paragraphSegments = inlineSegments(child)
                // 剔除已消费的标记文本与空片段
                val cleaned = if (skipMarker > 0 && paragraphSegments.isNotEmpty()) {
                    val first = paragraphSegments.first()
                    val rest = when (first) {
                        is TextSegment.Plain -> first.text.drop(skipMarker)
                        else -> null
                    }
                    if (rest != null) {
                        (listOf(TextSegment.Plain(rest)) + paragraphSegments.drop(1))
                            .filterNot { it is TextSegment.Plain && it.text.isEmpty() }
                    } else {
                        paragraphSegments
                    }
                } else {
                    paragraphSegments
                }
                if (cleaned.any { it !is TextSegment.SoftBreak }) {
                    quoteParagraphs.add(cleaned)
                }
            }
            child = child.next
        }
    }

    /**
     * 表格收集
     */
    private fun collectTable(tableBlock: TableBlock): MarkdownBlock.Table? {
        val headers = mutableListOf<String>()
        val rows = mutableListOf<List<String>>()

        var child = tableBlock.firstChild
        while (child != null) {
            when (child) {
                is TableHead -> {
                    var row = child.firstChild
                    while (row != null) {
                        if (row is TableRow) {
                            var cell = row.firstChild
                            while (cell != null) {
                                if (cell is TableCell) {
                                    headers.add(inlineText(cell).trim())
                                }
                                cell = cell.next
                            }
                        }
                        row = row.next
                    }
                }
                is TableBody -> {
                    var row = child.firstChild
                    while (row != null) {
                        if (row is TableRow) {
                            val rowData = mutableListOf<String>()
                            var cell = row.firstChild
                            while (cell != null) {
                                if (cell is TableCell) {
                                    rowData.add(inlineText(cell).trim())
                                }
                                cell = cell.next
                            }
                            if (rowData.isNotEmpty()) rows.add(rowData)
                        }
                        row = row.next
                    }
                }
            }
            child = child.next
        }
        return if (headers.isNotEmpty()) MarkdownBlock.Table(headers, rows) else null
    }

    // ------------------------------------------------------------------
    // 行内工具
    // ------------------------------------------------------------------

    /**
     * 收集节点的全部行内片段（进入子树访问并取回缓冲）
     *
     * 注意保存 / 恢复外层缓冲：行内收集可能嵌套发生（如链接内含图片）
     */
    private fun inlineSegments(parent: org.commonmark.node.Node): List<TextSegment> {
        val outer = currentTextSegments
        currentTextSegments = mutableListOf()
        visitChildren(parent)
        val result = currentTextSegments.toList()
        currentTextSegments = outer
        return result
    }

    /**
     * 收集节点的拼接纯文本（标题 / 表格单元格）
     */
    private fun inlineText(node: org.commonmark.node.Node): String {
        return inlineSegments(node).mapNotNull { segment ->
            when (segment) {
                is TextSegment.Plain -> segment.text
                is TextSegment.Bold -> segment.text
                is TextSegment.Italic -> segment.text
                is TextSegment.Strikethrough -> segment.text
                is TextSegment.InlineCode -> segment.text
                is TextSegment.Link -> segment.text
                is TextSegment.Image -> segment.alt
                is TextSegment.SoftBreak -> " "
                is TextSegment.HardBreak -> " "
            }
        }.joinToString("").trim()
    }

    private fun restoreSegmentBuffer() {
        currentTextSegments = mutableListOf()
    }

    private fun flushParagraph() {
        if (currentTextSegments.isNotEmpty()) {
            blocks.add(MarkdownBlock.Paragraph(currentTextSegments.toList()))
            currentTextSegments = mutableListOf()
        }
    }

    /**
     * 探测引用块是否为告警块
     *
     * 返回告警类型与标记文本长度（"[!NOTE] "），非告警块返回 null
     */
    private fun detectAdmonitionMarker(quote: BlockQuote): Pair<AdmonitionType, Int>? {
        val firstParagraph = quote.firstChild as? Paragraph ?: return null
        val firstText = firstParagraph.firstChild as? Text ?: return null
        val match = Regex("""^\[!(\w+)\]\s*""", RegexOption.IGNORE_CASE).find(firstText.literal)
            ?: return null
        val type = AdmonitionType.fromMarker(match.groupValues[1]) ?: return null
        return type to match.value.length
    }
}
