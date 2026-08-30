package com.fandex.app.ui.components

import androidx.compose.animation.animateColorAsState
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.interaction.collectIsPressedAsState
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.fandex.app.ui.common.pressScale
import com.fandex.app.ui.common.selectionPulse
import com.fandex.app.ui.common.tweenFast
import com.fandex.app.ui.theme.CategoryColors
import com.fandex.app.ui.theme.LocalExtendedColors

/**
 * 分类色工具
 *
 * 全局唯一的分类色解析入口（模块卡片 / 抽屉导航 / 筛选 chips 共用），
 * 避免各页面自行解析造成色彩不统一
 */
object CategoryColor {
    /** 解析十六进制色值，非法时回退到工具链默认色 */
    fun parse(hex: String): Color {
        val normalized = hex.removePrefix("#")
        return runCatching {
            Color(normalized.toLong(16) or 0xFF000000)
        }.getOrDefault(CategoryColors.Tools)
    }
}

/**
 * 共享小图标按钮
 *
 * 统一顶栏图标按钮的规格：32dp 触达区 + 4dp 直角小圆角 + 透明底；
 * 按下时给出双重反馈：bgHover 底色过渡 + 0.94 按压缩放，
 * 全应用顶栏与页面工具区的裸 IconButton 统一替换为此组件
 * （ModalBottomSheet 内部按钮与 FAB 除外）
 *
 * @param tint 图标着色，传 Color.Unspecified 时跟随 LocalContentColor
 */
@Composable
fun FdxIconButton(
    icon: ImageVector,
    contentDescription: String?,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    tint: Color = Color.Unspecified,
    iconSize: Dp = 20.dp
) {
    val extendedColors = LocalExtendedColors.current
    val interaction = remember { MutableInteractionSource() }
    val pressed by interaction.collectIsPressedAsState()

    // 按下底色过渡：透明 -> bgHover（快速反馈节奏）
    val background by animateColorAsState(
        targetValue = if (pressed) extendedColors.bgHover else Color.Transparent,
        animationSpec = tweenFast(),
        label = "fdxIconButtonBg"
    )

    Box(
        modifier = modifier
            .size(32.dp)
            .pressScale(interaction, pressedScale = 0.94f)
            .clip(RoundedCornerShape(4.dp))
            .background(background)
            .clickable(interactionSource = interaction, indication = null, onClick = onClick),
        contentAlignment = Alignment.Center
    ) {
        Icon(
            imageVector = icon,
            contentDescription = contentDescription,
            tint = tint,
            modifier = Modifier.size(iconSize)
        )
    }
}

/**
 * 区块标题（共享）
 *
 * 3px 分类色竖条 + 粗体标题 + 可选计数药丸，
 * 首页分类区 / 最近浏览 / 语法分组等统一使用
 */
@Composable
fun SectionHeader(
    title: String,
    color: Color = MaterialTheme.colorScheme.primary,
    count: Int? = null,
    modifier: Modifier = Modifier
) {
    val extendedColors = LocalExtendedColors.current

    Row(
        modifier = modifier.fillMaxWidth(),
        verticalAlignment = Alignment.CenterVertically
    ) {
        Box(
            modifier = Modifier
                .width(3.dp)
                .height(14.dp)
                .clip(RoundedCornerShape(1.dp))
                .background(color)
        )
        Spacer(modifier = Modifier.width(8.dp))
        Text(
            text = title,
            style = MaterialTheme.typography.titleMedium,
            color = MaterialTheme.colorScheme.onSurface,
            fontWeight = FontWeight.Bold,
            letterSpacing = 0.04.sp,
            maxLines = 1,
            overflow = TextOverflow.Ellipsis
        )
        if (count != null) {
            Spacer(modifier = Modifier.width(8.dp))
            Text(
                text = "$count",
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
 * 筛选数据模型
 */
data class FilterOption(
    val id: String,
    val label: String,
    val color: Color = Color.Unspecified
)

/**
 * 分类筛选 chips（共享）
 *
 * 对齐旧版首页筛选行：横向滑动 chip 组，
 * 选中态以分类色微透底 + 分类色文字 + 分类色边框高亮（点击选择的视觉提示），
 * 未选中态为线框样式；
 * 选中 / 未选中的底色、边框色、文字色均以 animateColorAsState 平滑过渡，
 * 选中瞬间叠加 springBouncy 缩放脉冲（与按压 pressScale 变换相乘）
 */
@Composable
fun FilterChipRow(
    options: List<FilterOption>,
    selectedId: String,
    onSelect: (String) -> Unit,
    modifier: Modifier = Modifier
) {
    val extendedColors = LocalExtendedColors.current

    androidx.compose.foundation.lazy.LazyRow(
        modifier = modifier,
        horizontalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        items(options.size, key = { options[it].id }) { index ->
            val option = options[index]
            val selected = option.id == selectedId
            val accent = if (option.color == Color.Unspecified) {
                MaterialTheme.colorScheme.primary
            } else option.color
            val interaction = remember { MutableInteractionSource() }

            // 选中 / 未选中三态颜色平滑过渡
            val bg by animateColorAsState(
                targetValue = if (selected) accent.copy(alpha = 0.12f) else extendedColors.bgElevated,
                animationSpec = tweenFast(),
                label = "chipRowBg"
            )
            val borderColor by animateColorAsState(
                targetValue = if (selected) accent.copy(alpha = 0.5f) else extendedColors.borderDefault,
                animationSpec = tweenFast(),
                label = "chipRowBorder"
            )
            val fgColor by animateColorAsState(
                targetValue = if (selected) accent else extendedColors.fgSecondary,
                animationSpec = tweenFast(),
                label = "chipRowFg"
            )

            Row(
                modifier = Modifier
                    .pressScale(interaction)
                    .selectionPulse(selected)
                    .clip(RoundedCornerShape(4.dp))
                    .background(bg)
                    .border(1.dp, borderColor, RoundedCornerShape(4.dp))
                    .clickable(
                        interactionSource = interaction,
                        indication = null
                    ) { onSelect(option.id) }
                    .padding(horizontal = 14.dp, vertical = 8.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                // 选中态左侧色条（几何提示，非圆点）
                if (selected) {
                    Box(
                        modifier = Modifier
                            .width(3.dp)
                            .height(12.dp)
                            .clip(RoundedCornerShape(1.dp))
                            .background(accent)
                    )
                    Spacer(modifier = Modifier.width(6.dp))
                }
                Text(
                    text = option.label,
                    style = MaterialTheme.typography.labelLarge,
                    color = fgColor,
                    fontWeight = if (selected) FontWeight.SemiBold else FontWeight.Medium
                )
            }
        }
    }
}
