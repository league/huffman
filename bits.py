
class BitInstream:
    def __init__(self, buf):
        self.buf = buf
        self.byte = 0
        self.bits = 0

    def read1(self):
        if not self.bits:
            bs = self.buf.read(1)
            if not bs:
                self.buf.close()
                raise EOFError()
            self.byte = bs[0]
            self.bits = 8
        mask = 1 << (self.bits - 1)
        self.bits -= 1;
        return bool(self.byte & mask)

class BitOutstream:
    def __init__(self, buf):
        self.buf = buf
        self.byte = 0
        self.bits = 0

    def write1(self, val):
        self.byte <<= 1
        self.byte |= 1 if val else 0
        self.bits += 1
        if self.bits == 8:
            self.buf.write(bytes([self.byte]))
            self.byte = 0
            self.bits = 0

    def close(self):
        if self.bits:
            self.byte <<= (8 - self.bits)
            self.buf.write(bytes([self.byte]))
        self.buf.close()
