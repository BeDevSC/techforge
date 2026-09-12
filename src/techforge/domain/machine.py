from pydantic import BaseModel, Field
from techforge.domain.cpu import CPU
from techforge.domain.gpu import GPU
from techforge.domain.memory import Memory
from techforge.domain.storage import Storage
from techforge.domain.motherboard import Motherboard
from techforge.domain.bios import BIOS

class Machine(BaseModel):
    name: str
    motherboard: Motherboard | None = None
    cpu: CPU | None = None
    gpus: list[GPU] = Field(default_factory=list)
    memory: Memory | None = None
    storages: list[Storage] = Field(default_factory=list)
    bios: BIOS | None = None
    windows: str
    windows_build: str
    architecture: str
    tpm_enabled: bool | None = None
    secure_boot_enabled: bool | None = None
