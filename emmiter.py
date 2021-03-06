import subprocess
import encoding

MAGICMODULEHEADER = [0x00, 0x61, 0x73, 0x6d]
MODULEVERSION = [0x01, 0x00, 0x00, 0x00]
emitterOut="ptest.wasm"

def emitter():
    with open(emitterOut,'wb') as bytewriter:
        bytewriter.write(bytes(MAGICMODULEHEADER+MODULEVERSION))

emitter()

subprocess.run(["wasmtime", emitterOut])
