from techforge.domain.cpu import CPU
from techforge.domain.gpu import GPU
from techforge.domain.memory import Memory
from techforge.domain.storage import Storage
from techforge.domain.motherboard import Motherboard
from techforge.domain.bios import BIOS
from techforge.domain.machine import Machine

def test_machine_creation():
    machine = Machine(
        name="TECH-PC",
        motherboard=Motherboard(
            name="ROG STRIX Z890-A GAMING WIFI",
            manufacturer="ASUS",
            model="ROG STRIX Z890-A GAMING WIFI",
            socket="LGA1700"
        ),
        cpu=CPU(
            name="AMD Ryzen 9 7950X",
            manufacturer="AMD",
            cores=16,
            threads=32
        ),
        gpus=[
            GPU(
                name="NVIDIA GeForce RTX 4090",
                manufacturer="NVIDIA",
                memory=24
            )
        ],
        memory=Memory(
            capacity=32,
            available_capacity=32
        ),
        storages=[
            Storage(
                name="Samsung 990 PRO 1TB",
                type="SSD",
                capacity=1000,
                filesystem="NTFS"
            )
        ],
        bios=BIOS(
            manufacturer="ASUS",
            version="1.0",
            mode="UEFI"
        ),
        windows="Windows 11",
        windows_build="22H2",
        architecture="x64",
        tpm_enabled=True,
        secure_boot_enabled=True
    )
    assert machine is not None
    assert machine.name == "TECH-PC"
    assert machine.motherboard.name == "ROG STRIX Z890-A GAMING WIFI"
    assert machine.cpu.name == "AMD Ryzen 9 7950X"
    assert machine.gpus[0].name == "NVIDIA GeForce RTX 4090"
    assert machine.memory.capacity == 32
    assert machine.memory.available_capacity == 32
    assert machine.storages[0].name == "Samsung 990 PRO 1TB"
    assert machine.storages[0].type == "SSD"
    assert machine.storages[0].capacity == 1000
    assert machine.storages[0].filesystem == "NTFS"
    assert machine.bios.manufacturer == "ASUS"
    assert machine.bios.version == "1.0"
    assert machine.bios.mode == "UEFI"
    assert machine.windows == "Windows 11"
    assert machine.windows_build == "22H2"
    assert machine.architecture == "x64"
    assert machine.tpm_enabled == True
    assert machine.secure_boot_enabled == True

