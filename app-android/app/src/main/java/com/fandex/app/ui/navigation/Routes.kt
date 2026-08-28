package com.fandex.app.ui.navigation

/**
 * 路由定义
 *
 * 单 Activity 架构下所有页面的路由常量
 * （设置收纳于抽屉，无独立路由；底部导航已移除，改为顶部 Dock）
 */
object Routes {
    const val HOME = "home"
    const val MODULE = "module/{moduleId}"
    const val DOCUMENT = "doc/{moduleId}/{docSlug}"
    const val SYNTAX = "syntax"
    const val SYNTAX_DETAIL = "syntax/{moduleId}"
    const val LEARNING_PATH = "learning-path"
    const val LEARNING_PATH_DETAIL = "learning-path/{moduleId}"
    const val SEARCH = "search"

    fun module(moduleId: String) = "module/$moduleId"
    fun document(moduleId: String, docSlug: String) = "doc/$moduleId/$docSlug"
    fun syntaxDetail(moduleId: String) = "syntax/$moduleId"
    fun learningPathDetail(moduleId: String) = "learning-path/$moduleId"
}
