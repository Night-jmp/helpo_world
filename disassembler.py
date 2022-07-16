import rzpipe
def disasm(filename):
    rz = rzpipe.open("hello")
    rz.cmd('aa')
    rz.cmd('s sym.main')
    print(rz.cmd('pdf'))
