KBsize = 1024

class ROM:
    sNES = "NES" # 3 byte

    def __init__(self, romFile):
        if  (romFile.read(3) == self.sNES):
            _ = romFile.read(1)
            self.num16ROMBanks = int(romFile.read(1).encode('hex'), 16)
            self.num8ROMBanks = int(romFile.read(1).encode('hex'), 16)
            self.ctrl1 = romFile.read(1).encode('hex')
            self.ctrl2 = romFile.read(1).encode('hex')
            self.num8RAMBanks = int(romFile.read(1).encode('hex'), 16)
            self.reserved = romFile.read(7).encode('hex')

            self.data = romFile.read(self.num16ROMBanks*16*KBsize + self.num8ROMBanks*8*KBsize)

        else:
            raise Exception("It is not a iNES game.")

    def get_memory(self):
        return self.data

    def get(self, position, size):
        assert size > 0, "Not a valid size."
        return self.data[position:position+size]
