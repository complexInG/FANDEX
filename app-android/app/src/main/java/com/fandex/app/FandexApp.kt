package com.fandex.app

import android.app.Application

/**
 * FANDEX 应用入口
 *
 * 持有全局依赖容器 AppContainer，供 ViewModel 获取数据仓库
 */
class FandexApp : Application() {

    /** 依赖容器（应用生命周期内单例） */
    lateinit var container: AppContainer
        private set

    override fun onCreate() {
        super.onCreate()
        container = AppContainer(this)
    }
}
