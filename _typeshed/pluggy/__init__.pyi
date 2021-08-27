from typing import Any

from .hooks import HookimplMarker as HookimplMarker

def __getattr__(name: str) -> Any: ...  # incomplete
