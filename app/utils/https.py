import httpx

from app.utils.logger import get_logger

log = get_logger(__name__)
_HEADERS = {"User-Agent": "Waytopoint/0.1"}

def get_json(url:str, params:dict | None = None, timeout:float = 5.0) -> dict|list| None:
    try:
        r = httpx.get(url, params = params, headers = _HEADERS, timeout= timeout)
        r.raise_for_status()
        return r.json()
    except Exception as exc:
        log.warning("GET %s failed: %s", url, exc)
        return None

def is_alive(url: str, timeout: float = 4.0) -> bool:
    try:
        return httpx.head(url, headers = _HEADERS, timeout = timeout, follow_redirects = True).status_code < 400
    except Exception:
        return False