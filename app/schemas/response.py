from pydantic import BaseModel
from .website import Website


class Recommendation(BaseModel):
    website: Website
    score: float
    why: str

class Response(BaseModel):
    query: str
    category: str | None
    confidence: float
    best: Recommendation | None
    alternatives: list[Recommendation] = []