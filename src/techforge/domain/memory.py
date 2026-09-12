from pydantic import BaseModel

class Memory(BaseModel):
    capacity: int
    available_capacity: int

