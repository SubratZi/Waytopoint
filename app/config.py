import os
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Settings:
    cache_ttl: int = int(os.getenv("WAYTOPOINT_CACHE_TTL","3600"))
    log_level: str = os.getenv("WAYPOINT_LOG_LEVEL", "INFO")
    max_alternatives: int = 3 
    weights: dict = field(default_factory= lambda: {
        "curated": 0.5,
        "tag_match": 0.35,
        "pricing": 0.15,
    })

settings = Settings()
