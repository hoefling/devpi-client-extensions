from typing import Any

from pluggy.hooks import HookimplMarker

hookimpl: HookimplMarker

def __getattr__(name: str) -> Any: ...  # incomplete
