from pydantic import BaseModel,Field

class Website(BaseModel):
    name:str
    url: str
    categories: list[str]
    tags: list[str] = []
    description: str = ""
    quality: float = Field(0.5, ge =0 , le=1)
    free: bool = True

class Signal(BaseModel):
    site: str
    source: str
    strength: float = Field(ge = 0, le=1)
