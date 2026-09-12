from pydantic import BaseModel

class BIOS(BaseModel):
    manufacturer: str
    version: str
    mode: str

