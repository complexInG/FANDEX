package com.fandex.app.ui.markdown

import android.annotation.SuppressLint
import android.os.Handler
import android.os.Looper
import android.webkit.JavascriptInterface
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.getValue
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.viewinterop.AndroidView
import com.fandex.app.ui.theme.LocalExtendedColors
import kotlinx.serialization.json.Json

/**
 * Mermaid 图表离线渲染组件
 *
 * 基于 WebView + 内置 mermaid.min.js（assets/mermaid/）：
 * - 完全离线渲染，无网络依赖
 * - 主题跟随应用深浅色（dark / neutral）
 * - 渲染完成后由 JS 回报实际高度，WebView 自适应
 * - 渲染失败时回退展示图表源码
 */
@SuppressLint("SetJavaScriptEnabled")
@Composable
fun MermaidDiagram(
    code: String,
    modifier: Modifier = Modifier
) {
    val extendedColors = LocalExtendedColors.current
    val density = LocalDensity.current
    val context = LocalContext.current
    val mainHandler = remember { Handler(Looper.getMainLooper()) }

    // JS 回报的内容高度（px），0 表示尚未渲染
    var contentHeightPx by remember { mutableIntStateOf(0) }
    var renderError by remember { mutableStateOf(false) }
    var pageReady by remember { mutableStateOf(false) }

    val bridge = remember {
        MermaidBridge(
            { px -> mainHandler.post { contentHeightPx = px } },
            { mainHandler.post { renderError = true } }
        )
    }

    val webView = remember {
        WebView(context).apply {
            settings.javaScriptEnabled = true
            settings.domStorageEnabled = true
            setBackgroundColor(android.graphics.Color.TRANSPARENT)
            isVerticalScrollBarEnabled = false
            addJavascriptInterface(bridge, "AndroidBridge")
            webViewClient = object : WebViewClient() {
                override fun onPageFinished(view: WebView?, url: String?) {
                    pageReady = true
                }
            }
            loadUrl("file:///android_asset/mermaid/index.html")
        }
    }

    // 页面就绪后触发渲染；代码或主题变化时在同一 WebView 内重渲染
    LaunchedEffect(webView, code, extendedColors.isDark, pageReady) {
        if (pageReady) {
            val theme = if (extendedColors.isDark) "dark" else "neutral"
            val codeJson = Json.encodeToString(code)
            webView.evaluateJavascript("renderMermaid($codeJson, \"$theme\")", null)
        }
    }

    val height = if (contentHeightPx > 0) {
        with(density) { contentHeightPx.toDp() }.coerceIn(80.dp, 1600.dp)
    } else {
        220.dp
    }

    if (renderError) {
        // 回退：渲染失败展示源码
        Box(
            modifier = modifier
                .fillMaxWidth()
                .clip(RoundedCornerShape(8.dp))
                .background(extendedColors.codeBg)
                .padding(12.dp)
        ) {
            Text(
                text = code,
                style = MaterialTheme.typography.bodySmall,
                color = extendedColors.codeText,
                maxLines = 12,
                overflow = TextOverflow.Ellipsis
            )
        }
        return
    }

    Box(
        modifier = modifier
            .fillMaxWidth()
            .clip(RoundedCornerShape(8.dp))
            .background(extendedColors.codeBg)
    ) {
        AndroidView(
            factory = { webView },
            modifier = Modifier
                .fillMaxWidth()
                .height(height)
        )
    }
}

/**
 * JS 桥：回报渲染高度与错误
 *
 * 回调运行在 WebView 线程，经主线程 Handler 切回后再更新状态
 */
private class MermaidBridge(
    private val onHeightCallback: (Int) -> Unit,
    private val onErrorCallback: (String) -> Unit
) {
    @JavascriptInterface
    fun onHeight(px: Int) = onHeightCallback(px)

    @JavascriptInterface
    fun onError(error: String) = onErrorCallback(error)
}
