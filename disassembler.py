#from capstone import *
from pwn import *
#def disasm():

#    CODE = open("hello", "rb").read()
#    md = Cs(CS_ARCH_X86, CS_MODE_64)
#    for i in md.disasm(CODE, 0): 
#        print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))

def disasm():
    e = ELF("hello")
    addr = e.symbols['main']


if __name__ == "__main__":
    disasm()
