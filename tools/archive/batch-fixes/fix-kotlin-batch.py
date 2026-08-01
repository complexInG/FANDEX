# -*- coding: utf-8 -*-
"""修复 014-kotlin 下 ASCII 图表。"""

from __future__ import annotations

import pathlib

ROOT = pathlib.Path(r"C:\Atian\Project\Trae\FANDEX-pj\FANDEX\cnt-content\full\014-kotlin")


def replace_block(path: pathlib.Path, marker: str, new: str) -> bool:
    text = path.read_text(encoding="utf-8")
    idx = text.find(marker)
    if idx < 0:
        return False
    start = text.rfind("```", 0, idx)
    end = text.find("```", idx)
    if start < 0 or end < 0 or end < start:
        return False
    end += 3
    path.write_text(text[:start] + new + text[end:], encoding="utf-8")
    return True


results = []

p = ROOT / "008-KotlinMultiplatform.md"
new = (
    "```mermaid\nflowchart TD\n"
    "    Shared[Shared Kotlin Code<br/>业务逻辑、数据模型、工具类]\n"
    "    Shared --> A[Android<br/>JVM/ART]\n"
    "    Shared --> I[iOS<br/>Native]\n"
    "    Shared --> W[Web<br/>JS/Wasm]\n"
    "    Shared --> D[Desktop<br/>JVM/Native]\n"
    "```"
)
results.append(("008-kmp", replace_block(p, "Shared Kotlin Code", new)))

p = ROOT / "045-FlowColdSharedState.md"
new2 = (
    "```mermaid\nflowchart TD\n"
    "    UI[UI Layer Compose / View<br/>collectAsStateWithLifecycle()]\n"
    "    VM[ViewModel / Presenter<br/>StateFlow&lt;UiState&gt;<br/>SharedFlow&lt;UiEvent&gt;]\n"
    "    Dom[Domain / UseCase<br/>suspend fun / Flow&lt;T&gt;]\n"
    "    Data[Data / Repository<br/>Flow&lt;T&gt; from DB / Network]\n"
    "    UI --> VM --> Dom --> Data\n"
    "```"
)
results.append(("045-flow", replace_block(p, "UI Layer (Compose", new2)))

p = ROOT / "052-KotlinCrossPlatform.md"
new3 = (
    "```mermaid\nflowchart TD\n"
    "    PUI[Platform UI Layer<br/>Jetpack Compose / SwiftUI / Compose MP]\n"
    "    SUI[Shared UI Layer 可选<br/>Compose Multiplatform]\n"
    "    SP[Shared Presentation Layer<br/>ViewModel / MVI]\n"
    "    SD[Shared Domain Layer<br/>Use Cases / Entities]\n"
    "    SData[Shared Data Layer<br/>Repository / DataSource]\n"
    "    PI[Platform Integration Layer<br/>Network: Ktor / DB: SQLDelight]\n"
    "    PUI --> SUI --> SP --> SD --> SData --> PI\n"
    "```"
)
results.append(("052-layers", replace_block(p, "Platform UI Layer", new3)))

new4 = (
    "```mermaid\nflowchart TD\n"
    "    PUI[平台 UI<br/>Compose Web / Android / iOS]\n"
    "    SUI[Shared UI<br/>Compose Multiplatform]\n"
    "    SVM[Shared VM<br/>MVIKotlin 跨平台 ViewModel]\n"
    "    SD[Shared Domain<br/>Space 业务逻辑]\n"
    "    SData[Shared Data<br/>Ktor + SQLDelight]\n"
    "    PUI --> SUI --> SVM --> SD --> SData\n"
    "```"
)
results.append(("052-arch", replace_block(p, "平台 UI（Compose", new4)))

for name, ok in results:
    print(f"{name}: {ok}")
