package com.fandex.app.data.prefs

import android.content.Context
import androidx.datastore.core.DataStore
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.core.booleanPreferencesKey
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.floatPreferencesKey
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

/**
 * 主题模式
 *
 * 对齐 web 端 ThemeToggle 的三态切换
 */
enum class ThemeMode {
    /** 跟随系统 */
    SYSTEM,

    /** 强制浅色 */
    LIGHT,

    /** 强制深色 */
    DARK
}

private val Context.dataStore: DataStore<Preferences> by preferencesDataStore(name = "fandex_prefs")

/**
 * 主题偏好存储
 *
 * 基于 DataStore Preferences 持久化主题模式选择
 * （字号跟随系统设置，不做应用内缩放）
 */
class ThemePreferences(private val context: Context) {

    /**
     * 主题模式流（默认跟随系统）
     */
    val themeMode: Flow<ThemeMode> = context.dataStore.data.map { prefs ->
        when (prefs[KEY_THEME_MODE]) {
            ThemeMode.LIGHT.name -> ThemeMode.LIGHT
            ThemeMode.DARK.name -> ThemeMode.DARK
            else -> ThemeMode.SYSTEM
        }
    }

    /**
     * 写入主题模式
     */
    suspend fun setThemeMode(mode: ThemeMode) {
        context.dataStore.edit { prefs ->
            prefs[KEY_THEME_MODE] = mode.name
        }
    }

    companion object {
        private val KEY_THEME_MODE = stringPreferencesKey("theme_mode")
    }
}
