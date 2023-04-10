from typing import Callable, TypeVar, overload

from _typeshed import Incomplete

_F = TypeVar("_F", bound=Callable[..., object])

class HookimplMarker:
    project_name: str
    def __init__(self, project_name: str) -> None: ...
    @overload
    def __call__(
        self,
        function: _F,
        hookwrapper: bool = ...,
        optionalhook: bool = ...,
        tryfirst: bool = ...,
        trylast: bool = ...,
        specname: str | None = ...,
    ) -> _F: ...
    @overload
    def __call__(
        self,
        function: None = ...,
        hookwrapper: bool = ...,
        optionalhook: bool = ...,
        tryfirst: bool = ...,
        trylast: bool = ...,
        specname: str | None = ...,
    ) -> Callable[[_F], _F]: ...
