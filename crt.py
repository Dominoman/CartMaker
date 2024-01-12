from PySide6.QtCore import QAbstractTableModel


class CrtException(Exception):
    pass


class Chip:
    TYPE = {0: "ROM", 1: "RAM", 2: "Flash ROM"}
    SIGNATURE = "CHIP"

    def __init__(self) -> None:
        self.type = 2
        self.bank_number = 0
        self.start_address = 0
        self.data = bytes()

    def __str__(self):
        return f"<{self.SIGNATURE}:{self.TYPE[self.type] if self.type in self.TYPE else self.type}:B{self.bank_number}:{hex(self.start_address)}:{hex(len(self.data))}>"

    @staticmethod
    def from_bytes(data: bytes) -> 'Chip':
        chip = Chip()
        chip.type = int.from_bytes(data[0x08:0x0a], "big")
        chip.bank_number = int.from_bytes(data[0x0a:0x0c], "big")
        chip.start_address = int.from_bytes(data[0x0c:0x0e], "big")
        rom_size = int.from_bytes(data[0x0e:0x10], "big")
        chip.data = data[0x10:0x10 + rom_size]
        return chip

    def to_bytes(self) -> bytes:
        result = bytes(self.SIGNATURE, 'ASCII')
        result += (0x10 + len(self.data)).to_bytes(4, "big")
        result += self.type.to_bytes(2, "big")
        result += self.bank_number.to_bytes(2, "big")
        result += self.start_address.to_bytes(2, "big")
        result += len(self.data).to_bytes(2, "big")
        result += self.data
        return result


class Crt:
    chips: list[Chip]
    TYPE = {0: "Normal cartridge", 1: "Action Replay", 2: "KCS Power Cartridge", 3: "Final Cartridge III",
            4: "Simons Basic",
            5: "Ocean type", 6: "Expert Cartridge", 7: "Fun Play, Power Play", 8: "Super Games", 9: "Atomic Power",
            10: "Epyx Fastload", 11: "Westermann Learning", 12: "Rex Utility", 13: "Final Cartridge I",
            14: "Magic Formel",
            15: "C64 Game System, System 3", 16: "WarpSpeed", 17: "Dinamic", 18: "Zaxxon, Super Zaxxon (SEGA)",
            19: "Magic Desk, Domark, HES Australia", 20: "Super Snapshot 5", 21: "Comal-80", 22: "Structured Basic",
            23: "Ross", 24: "Dela EP64", 25: "Dela EP7x8", 26: "Dela EP256", 27: "Rex EP256", 32: "EasyFlash"}
    SIGNATURE = 'C64 CARTRIDGE   '
    HEADER_LENGTH = 0x40

    def __init__(self) -> None:
        self.version_hi = 1
        self.version_low = 0
        self.type = 32
        self.exrom = True
        self.game = False
        self.name = "EasyFlash"
        self.chips = []

    def __str__(self):
        return f"<{self.SIGNATURE}:{self.version_hi}.{self.version_low}:{self.TYPE[self.type] if self.type in self.TYPE else self.type}:{'EXROM' if self.exrom else ''}{'GAME' if self.game else ''}:{self.name}>"

    @staticmethod
    def from_bytes(data: bytes) -> 'Crt':
        crt = Crt()
        signature = data[:0x10].decode('ASCII')
        if signature != Crt.SIGNATURE:
            raise CrtException("Signature error!")
        header_length = int.from_bytes(data[0x10:0x14], "big")
        crt.version_hi = data[0x14]
        crt.version_low = data[0x15]
        crt.type = int.from_bytes(data[0x16:0x18], "big")
        crt.exrom = data[0x18] == 1
        crt.game = data[0x19] == 1
        crt.name = data[0x20:0x40].decode('ASCII').rstrip(' \0x00')
        i = crt.HEADER_LENGTH
        while i < len(data):
            signature = data[i:i + 0x04].decode('ASCII')
            if signature != Chip.SIGNATURE:
                raise CrtException("Signature error!")
            total_length = int.from_bytes(data[i + 0x04:i + 0x08], "big")
            chip = Chip.from_bytes(data[i:i + total_length])
            crt.chips.append(chip)
            i += total_length
        return crt

    def to_bytes(self) -> bytes:
        result = bytes(self.SIGNATURE, 'ASCII')
        result += self.HEADER_LENGTH.to_bytes(4, "big")
        result += self.version_hi.to_bytes(1, "big")
        result += self.version_low.to_bytes(1, "big")
        result += self.type.to_bytes(2, "big")
        result += b'\1' if self.exrom else b'\0'
        result += b'\1' if self.game else b'\0'
        result += b'\0' * 6
        result += bytes(self.name, 'ASCII')
        result += b'\0' * (32 - len(self.name))
        for chip in self.chips:
            result += chip.to_bytes()
        return result

    def get_raw(self) -> bytes:
        result = bytes()
        for chip in self.chips:
            result += chip.data
        return result

    def add_raw(self, data: bytes) -> None:
        data = data.rstrip(b':\xff')
        start_address = [0x8000, 0xa000]
        bank_size = 0x2000
        p = 0
        while p * bank_size < len(data):
            chip = Chip()
            chip.rom_size = bank_size
            chip.bank_number = p // 2
            chip.start_address = start_address[p % 2]
            chip_data = data[p * bank_size:(p + 1) * bank_size]
            if len(chip_data) < bank_size:
                chip_data += b'\xff' * (bank_size - len(chip_data))
            chip.data = chip_data
            chip.rom_size = len(chip.data)
            chip.total_length = 0x10 + chip.rom_size
            self.chips.append(chip)
            p += 1


class EasyFile:
    pass


class EasyFS(QAbstractTableModel):
    files: list[EasyFile]

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.files = []

    def from_bytes(self, data: bytes) -> None:
        pass
