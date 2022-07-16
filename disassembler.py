from capstone import *

def disasm(filename):

    CODE = open(filename, "rb").read()
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    for i in md.disasm(CODE, 0):
        print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))
