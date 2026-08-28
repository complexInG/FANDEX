package com.fandex.app.ui.components

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.fandex.app.data.model.Module
import com.fandex.app.ui.common.pressScale
import com.fandex.app.ui.theme.LocalExtendedColors

/**
 * 模块卡片
 *
 * 对齐 Web 端 ModuleCard.astro（ark-ui 设计语言）：
 * - 纵向布局：图标 + 标题同行，描述在下（两行省略）
 * - 几何图标：分类色微透底(8%) + 分类色细边框(38%) + 等宽大写字符
 * - 卡片：1px 边框 + 4px 直角小圆角，克制阴影
 * - 不使用点状元素，遵循仓库规则
 */
@Composable
fun ModuleCard(
    module: Module,
    categoryColor: Color,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    /** 序号标签（如 "01"，体现模块学习顺序） */
    indexLabel: String? = null
) {
    val extendedColors = LocalExtendedColors.current
    val interaction = remember { MutableInteractionSource() }

    Column(
        modifier = modifier
            .fillMaxWidth()
            .pressScale(interaction)
            .clip(RoundedCornerShape(4.dp))
            .background(extendedColors.bgElevated)
            .border(1.dp, extendedColors.borderDefault, RoundedCornerShape(4.dp))
            .clickable(interactionSource = interaction, indication = null, onClick = onClick)
            .padding(horizontal = 12.dp, vertical = 8.dp),
        verticalArrangement = Arrangement.spacedBy(4.dp)
    ) {
        // 头部：序号 + 几何图标 + 标题同行
        Row(
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            if (indexLabel != null) {
                Text(
                    text = indexLabel,
                    fontFamily = FontFamily.Monospace,
                    fontWeight = FontWeight.SemiBold,
                    fontSize = 11.sp,
                    color = categoryColor.copy(alpha = 0.85f)
                )
            }
            ModuleIcon(
                label = module.icon.ifEmpty { module.title.take(2) },
                color = categoryColor
            )
            Text(
                text = module.title,
                style = MaterialTheme.typography.titleSmall,
                color = MaterialTheme.colorScheme.onSurface,
                fontWeight = FontWeight.SemiBold,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
        }
        // 描述（最多两行）
        if (module.description.isNotEmpty()) {
            Text(
                text = module.description,
                style = MaterialTheme.typography.bodySmall,
                color = extendedColors.fgSecondary,
                maxLines = 2,
                overflow = TextOverflow.Ellipsis,
                lineHeight = 18.sp
            )
        }
    }
}

/**
 * 模块几何图标
 *
 * 对齐 Web 端 .card-icon：透明底 + 分类色细边框 + 等宽字体字符
 */
@Composable
fun ModuleIcon(
    label: String,
    color: Color,
    modifier: Modifier = Modifier
) {
    Box(
        modifier = modifier
            .size(22.dp)
            .clip(RoundedCornerShape(3.dp))
            .background(color.copy(alpha = 0.08f))
            .border(1.dp, color.copy(alpha = 0.38f), RoundedCornerShape(3.dp)),
        contentAlignment = Alignment.Center
    ) {
        Text(
            text = label.take(2).uppercase(),
            fontFamily = FontFamily.Monospace,
            fontWeight = FontWeight.SemiBold,
            fontSize = 9.sp,
            lineHeight = 9.sp,
            letterSpacing = 0.sp,
            color = color
        )
    }
}

/**
 * 紧凑型模块卡片
 *
 * 用于首页分类网格，更紧凑的布局
 */
@Composable
fun ModuleCardCompact(
    module: Module,
    categoryColorHex: String,
    onClick: () -> Unit,
    modifier: Modifier = Modifier
) {
    ModuleCard(
        module = module,
        categoryColor = parseHexColor(categoryColorHex),
        onClick = onClick,
        modifier = modifier
    )
}

/**
 * 解析十六进制颜色
 */
private fun parseHexColor(hex: String): Color {
    val normalized = hex.removePrefix("#")
    return runCatching {
        Color(normalized.toLong(16) or 0xFF000000)
    }.getOrDefault(Color(0xFF4E5E6B))
}
