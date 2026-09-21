import time
from typing import Any

class TTLCache:

    def __init__ (self, ttl:int):
        self.ttl = ttl
        self._data: dict[str, tuple[float, Any]] = {}

    def get(self, key:str) -> Any | None:
        item = self._data.get(key)
        if not item:
            return None
        expires, value = item
        if expires < time.time():
            del self._data[key]
            return None
        return value

    def set(self, key:str, value: Any) -> None:
        self._data[key] = (time.time() + self.ttl, value)

    def clear(self) -> None:
        self._data.clear()