from pydantic import BaseModel

class GPU(BaseModel):
    name: str
    manufacturer: str
    memory: int | None = None

