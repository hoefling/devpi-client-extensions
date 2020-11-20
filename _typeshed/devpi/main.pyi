from typing import Any, Callable, overload

def __getattr__(name: str) -> Any: ...  # incomplete

AnyFunc = Callable[..., Any]
@overload
def hookimpl(function: AnyFunc) -> AnyFunc: ...
@overload
def hookimpl(
    hookwrapper: bool = False,
    optionalhook: bool = False,
    tryfirst: bool = False,
    trylast: bool = False,
) -> Callable[[AnyFunc], AnyFunc]: ...
