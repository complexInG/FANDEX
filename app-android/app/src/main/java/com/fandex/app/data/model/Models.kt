package com.fandex.app.data.model

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 模块元数据根对象
 *
 * 对应 assets/metadata/modules.json（源自 shd-shared/metadata/modules.json）顶层结构
 */
@Serializable
data class ModulesMetadata(
    val version: String = "",
    @SerialName("categoryLabels") val categoryLabels: Map<String, String> = emptyMap(),
    @SerialName("categoryColors") val categoryColors: Map<String, String> = emptyMap(),
    @SerialName("categoryOrder") val categoryOrder: List<String> = emptyList(),
    val modules: List<Module> = emptyList()
)

/**
 * 模块定义
 *
 * 对应 modules.json 中单个模块对象
 */
@Serializable
data class Module(
    val id: String,
    val title: String,
    val icon: String = "",
    val description: String = "",
    val categories: List<String> = emptyList(),
    @SerialName("folder_order") val folderOrder: Int = 0,
    @SerialName("updatePriority") val updatePriority: Boolean = false,
    @SerialName("updateNote") val updateNote: String? = null,
    @SerialName("officialDocs") val officialDocs: List<OfficialDoc> = emptyList()
)

/**
 * 官方文档链接
 */
@Serializable
data class OfficialDoc(
    val label: String,
    val url: String,
    val type: String = "docs"
)

/**
 * 文档 frontmatter 模型
 *
 * 对应 cnt-content/full 下 Markdown 文件的标准 10 字段 frontmatter
 */
@Serializable
data class DocFrontmatter(
    val order: Int = 0,
    val title: String,
    val module: String = "",
    val category: String = "",
    val difficulty: String = "beginner",
    val description: String = "",
    val author: String = "fanquanpp",
    val updated: String = "",
    val related: List<String> = emptyList(),
    val prerequisites: List<String> = emptyList()
)

/**
 * 文档完整信息
 *
 * 包含 frontmatter 与正文内容
 */
data class FandexDoc(
    val slug: String,
    val frontmatter: DocFrontmatter,
    val content: String
)

/**
 * 文档索引条目
 *
 * 用于快速检索文档列表，避免加载全部内容
 * 对应 assets/metadata/doc-index.json 中的单个条目
 */
@Serializable
data class DocIndexEntry(
    val slug: String,
    val title: String,
    val module: String,
    val category: String = "",
    val difficulty: String = "beginner",
    val description: String = "",
    val order: Int = 0,
    val updated: String = ""
)

/**
 * 分类信息（组合视图）
 *
 * 按 modules.json 的 categoryOrder 组织的模块分组
 */
data class CategoryInfo(
    val id: String,
    val label: String,
    val colorHex: String,
    val modules: List<Module>
)

// ---------------------------------------------------------------------------
// 语法速查
// ---------------------------------------------------------------------------

/**
 * 语法速查语言元数据
 *
 * 对应 assets/metadata/syntax-index.json（源自 app-web 预构建索引）
 */
@Serializable
data class SyntaxLanguage(
    val id: String,
    val title: String,
    val icon: String = "",
    val color: String = "",
    val count: Int = 0,
    @SerialName("docCount") val docCount: Int = 0
)

/**
 * 语法语言索引根对象
 */
@Serializable
data class SyntaxIndex(
    val version: Int = 1,
    @SerialName("generatedAt") val generatedAt: String = "",
    val languages: List<SyntaxLanguage> = emptyList()
)

/**
 * 语法速查卡片
 *
 * 对应 assets/syntax-data/{moduleId}.json 中的单个卡片
 */
@Serializable
data class SyntaxCard(
    val id: String = "",
    @SerialName("docTitle") val docTitle: String = "",
    val section: String = "",
    val name: String = "",
    val formula: String = "",
    val code: String = "",
    val lang: String = "",
    val truncated: Boolean = false
)

/**
 * 语法速查模块（单语言全部卡片）
 */
@Serializable
data class SyntaxModule(
    val module: String = "",
    val cards: List<SyntaxCard> = emptyList()
)

// ---------------------------------------------------------------------------
// 学习路径
//
// 数据结构与真实 JSON 严格对齐：
// - index.json: { version, order: [moduleId, ...] }
// - {moduleId}.json: { version, module, summary, stages: [...] }
// ---------------------------------------------------------------------------

/**
 * 学习路径索引
 *
 * order 数组给出路径展示顺序，标题等展示信息由模块元数据补充
 */
@Serializable
data class LearningPathIndex(
    val version: String = "",
    val order: List<String> = emptyList()
)

/**
 * 学习路径阶段
 *
 * 对应 {moduleId}.json stages 数组中的单个阶段
 */
@Serializable
data class LearningPathStage(
    val id: String = "",
    val title: String = "",
    val subtitle: String = "",
    val nodes: List<LearningPathNode> = emptyList()
)

/**
 * 学习路径节点
 *
 * doc 字段为模块内文档 slug，用于跳转正文
 */
@Serializable
data class LearningPathNode(
    val id: String = "",
    val title: String = "",
    val doc: String = "",
    val desc: String = "",
    val difficulty: String = "beginner"
)

/**
 * 学习路径详情
 */
@Serializable
data class LearningPath(
    val version: String = "",
    val module: String = "",
    val summary: String = "",
    val stages: List<LearningPathStage> = emptyList()
)

/**
 * 学习路径列表项（组合视图）
 *
 * 由索引 order 与模块元数据组合而成，供列表页直接展示
 */
data class LearningPathSummary(
    val moduleId: String,
    val title: String,
    val description: String,
    val stageCount: Int,
    /** 模块主分类色（十六进制），供多彩装饰 */
    val colorHex: String = "#4F5BD5"
)
