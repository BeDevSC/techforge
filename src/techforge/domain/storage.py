from pydantic import BaseModel

class Storage(BaseModel):
    name: str
    type: str
    capacity: int
    filesystem: str | None = None