package com.fandex.app.ui.components

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
import com.fandex.app.data.model.DocIndexEntry
import com.fandex.app.ui.common.pressScale
import com.fandex.app.ui.theme.LocalExtendedColors

/**
 * 文档列表项
 *
 * 对齐 Web 端 DocumentListItem 组件设计，并做"条目行"层次化处理：
 * - bgElevated 底 + 1dp borderSubtle 边框 + 4dp 直角小圆角（与页面背景分层）
 * - 左侧 3dp 分类色竖条保留（多彩点缀）
 * - 编号 / 标题 / 描述 / 难度标签 / 更新日期
 * - 按压缩放反馈；条目间距由调用方 LazyColumn spacedBy(8.dp) 控制
 *
 * @param moduleLabel 模块归属标签（搜索结果展示来源，普通列表不展示）
 */
@Composable
fun DocListItem(
    doc: DocIndexEntry,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    moduleLabel: String? = null,
    accent: Color = MaterialTheme.colorScheme.primary,
    /** 序号标签（如 "01"，体现文档阅读顺序） */
    indexLabel: String? = null
) {
    val extendedColors = LocalExtendedColors.current
    val interaction = remember { MutableInteractionSource() }

    // 条目行：外层 16dp 屏幕边距 + 卡片化条目本体
    Row(
        modifier = modifier
            .fillMaxWidth()
            .padding(horizontal = 16.dp)
            .pressScale(interaction)
            .clip(RoundedCornerShape(4.dp))
            .background(extendedColors.bgElevated)
            .border(1.dp, extendedColors.borderSubtle, RoundedCornerShape(4.dp))
            .clickable(interactionSource = interaction, indication = null, onClick = onClick)
            .padding(horizontal = 12.dp, vertical = 10.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        // 阅读顺序编号
        if (indexLabel != null) {
            Text(
                text = indexLabel,
                fontFamily = FontFamily.Monospace,
                fontWeight = FontWeight.SemiBold,
                fontSize = 11.sp,
                color = accent.copy(alpha = 0.85f)
            )
            Spacer(modifier = Modifier.width(8.dp))
        }

        // 编号竖条（多彩分类色）
        Box(
            modifier = Modifier
                .width(3.dp)
                .height(40.dp)
                .clip(RoundedCornerShape(2.dp))
                .background(accent.copy(alpha = 0.7f))
        )

        Spacer(modifier = Modifier.width(12.dp))

        Column(
            modifier = Modifier.weight(1f),
            verticalArrangement = Arrangement.spacedBy(2.dp)
        ) {
            // 模块归属标签（搜索场景）
            if (!moduleLabel.isNullOrEmpty()) {
                Text(
                    text = moduleLabel,
                    style = MaterialTheme.typography.labelSmall,
                    color = MaterialTheme.colorScheme.primary
                )
            }
            Text(
                text = doc.title,
                style = MaterialTheme.typography.titleSmall,
                color = MaterialTheme.colorScheme.onSurface,
                fontWeight = FontWeight.SemiBold,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
            if (doc.description.isNotEmpty()) {
                Text(
                    text = doc.description,
                    style = MaterialTheme.typography.bodySmall,
                    color = extendedColors.fgSecondary,
                    maxLines = 1,
                    overflow = TextOverflow.Ellipsis
                )
            }
            Row(
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                // 难度标签
                DifficultyBadge(difficulty = doc.difficulty)

                // 更新日期
                if (doc.updated.isNotEmpty()) {
                    Text(
                        text = doc.updated,
                        style = MaterialTheme.typography.labelSmall,
                        color = extendedColors.fgTertiary
                    )
                }
            }
        }
    }
}

/**
 * 难度标签
 *
 * 公共组件：文档列表项与文档详情页共用
 */
@Composable
fun DifficultyBadge(difficulty: String) {
    val (label, color) = when (difficulty) {
        "beginner" -> "入门" to MaterialTheme.colorScheme.primary
        "intermediate" -> "进阶" to (LocalExtendedColors.current.warning)
        "advanced" -> "高级" to MaterialTheme.colorScheme.error
        else -> difficulty to (LocalExtendedColors.current.fgSecondary)
    }

    Box(
        modifier = Modifier
            .clip(RoundedCornerShape(4.dp))
            .background(color.copy(alpha = 0.12f))
            .padding(horizontal = 6.dp, vertical = 2.dp)
    ) {
        Text(
            text = label,
            style = MaterialTheme.typography.labelSmall,
            color = color,
            fontWeight = FontWeight.Medium
        )
    }
}
