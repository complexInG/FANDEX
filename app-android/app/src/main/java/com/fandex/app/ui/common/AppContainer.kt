package com.fandex.app.ui.common

import androidx.compose.runtime.Composable
import androidx.compose.ui.platform.LocalContext
import com.fandex.app.AppContainer
import com.fandex.app.FandexApp

/**
 * 获取应用级依赖容器
 *
 * Compose 界面层访问数据仓库的统一入口，
 * 与 app-web services 统一出口的设计对齐
 */
@Composable
fun rememberAppContainer(): AppContainer {
    return (LocalContext.current.applicationContext as FandexApp).container
}
