import json
from functools import lru_cache
from pathlib import Path
from urllib.parse import urlparse

from app.schemas import Website

DB_DIR = Path(__file__).resolve().parent.parent / "database"

def _load(name: str):
    return json.loads((DB_DIR / name).read_text(encoding= "utf-8"))

@lru_cache(maxsize=1)
def load_db()-> dict:
    return{
        "website": [Website(**w) for w in _load("websites.json")],
        "categories": _load("catagories.json"),
        "aliases": _load("aliases.json"),
        "blacklist": _load("blacklist.json")["domains"],
    }

def domain_of(url:str) -> str:
    return urlparse(url).netloc.lower().removeprefix("www.")
