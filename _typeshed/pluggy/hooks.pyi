from typing import Any, Callable

C = Callable[..., Any]

class HookimplMarker:
    project_name: str = ...
    def __init__(self, project_name: str) -> None: ...
    def __call__(
        self,
        function: C | None = ...,
        hookwrapper: bool = ...,
        optionalhook: bool = ...,
        tryfirst: bool = ...,
        trylast: bool = ...,
    ) -> Callable[..., C]: ...
