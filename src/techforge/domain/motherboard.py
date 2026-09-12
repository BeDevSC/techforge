from pydantic import BaseModel

class Motherboard(BaseModel):
    name: str
    manufacturer: str
    model: str
    socket: str

