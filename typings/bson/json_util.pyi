from typing import Any

def loads(s: str) -> Any: ...
def dumps(obj: object, *args: Any, **kwargs: Any) -> str: ...
def default(obj: object, json_options: Any = ...) -> Any: ...
