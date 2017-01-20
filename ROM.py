class ROM(romFile):
    sNES = "NES" # 3 bytes
    idFormat = 0x1A # 1 byte
    num16ROMBanks = 0x00 # 1 byte
    num8ROMBanks = 0x00 # 1 byte
    ctrl1 = 0x00 # 1 byte
    ctrl2 = 0x00 # 1 byte
    num8RAMBanks = 0x00 # 1 byte
    reserved = 0x00 # 7 byte

    trainer512 = 0x00 # 512 bytes, if present

    def __init__(self, romFile):
        if  (romFile.read(3) == self.sNES):
            print 'lul'
        else:
            raise Exception("It is not a iNES game.")


fp = open()