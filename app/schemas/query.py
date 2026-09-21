from pydantic import BaseModel, Field

class Query(BaseModel):
    q: str = Field(min_length=2, max_length =200)

class Intent(BaseModel):
    category: str | None
    terms: list[str]
    confidence: float = Field (0.0, ge = 0, le = 1)

