from pydantic import BaseModel

class CPU(BaseModel):
    name: str
    manufacturer: str
    cores: int
    threads: int


