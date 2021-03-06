
def unsignedLEB128(n):
    BUFFER = bytearray()
    while True:
        byte = n & 0x7f
        n >>= 7
        if (n !=0):
            byte |= 0x80
        BUFFER.append(byte)
        if (n==0):
            break
    return BUFFER

        
        