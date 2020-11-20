from typing import Any, Optional

def __getattr__(name: str) -> Any: ...  # incomplete
def get_password(service_name: str, username: str) -> Optional[str]: ...
