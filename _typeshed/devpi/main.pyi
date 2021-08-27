from typing import Any, Callable, TypeVar, overload

from pluggy.hooks import HookimplMarker

hookimpl: HookimplMarker

def __getattr__(name: str) -> Any: ...  # incomplete
