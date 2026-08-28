package com.fandex.app

import android.app.Application
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.viewModels
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import androidx.lifecycle.viewmodel.compose.viewModel
import com.fandex.app.data.prefs.ThemeMode
import com.fandex.app.ui.navigation.AppRoot
import com.fandex.app.ui.theme.FandexTheme
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

/**
 * 主 Activity
 *
 * 单 Activity 架构，所有页面通过 Navigation Compose 导航
 * 启用沉浸式状态栏与导航栏；主题模式由用户设置驱动，
 * 字号跟随系统设置（不做应用内缩放）
 */
class MainActivity : ComponentActivity() {

    private val mainViewModel: MainViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            val themeMode by mainViewModel.themeMode.collectAsState()
            RootTheme(themeMode = themeMode) {
                AppRoot()
            }
        }
    }
}

/**
 * 根主题包装
 *
 * 根据用户选择的主题模式决定深浅色：
 * SYSTEM 跟随系统，LIGHT / DARK 强制指定
 */
@Composable
private fun RootTheme(themeMode: ThemeMode, content: @Composable () -> Unit) {
    val darkTheme = when (themeMode) {
        ThemeMode.SYSTEM -> isSystemInDarkTheme()
        ThemeMode.LIGHT -> false
        ThemeMode.DARK -> true
    }
    FandexTheme(darkTheme = darkTheme, content = content)
}

/**
 * 主界面 ViewModel
 *
 * 为顶部 Dock 与抽屉提供主题模式状态；页面级状态由各自 ViewModel 管理
 */
class MainViewModel(application: Application) : AndroidViewModel(application) {

    private val prefs = (application as FandexApp).container.themePreferences

    /** 当前主题模式 */
    val themeMode: StateFlow<ThemeMode> = prefs.themeMode
        .stateIn(viewModelScope, SharingStarted.Eagerly, ThemeMode.SYSTEM)

    /**
     * 循环切换主题模式：跟随系统 -> 浅色 -> 深色 -> 跟随系统
     */
    fun cycleThemeMode() {
        viewModelScope.launch {
            val next = when (themeMode.value) {
                ThemeMode.SYSTEM -> ThemeMode.LIGHT
                ThemeMode.LIGHT -> ThemeMode.DARK
                ThemeMode.DARK -> ThemeMode.SYSTEM
            }
            prefs.setThemeMode(next)
        }
    }
}
