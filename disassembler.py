import r2pipe
def disasm(filename = "hello"):
    rz = r2pipe.open("hello")
    rz.cmd('aa')
    rz.cmd('s sym.main')
    print(rz.cmd('pdf'))
