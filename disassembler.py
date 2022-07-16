import subprocess
def disasm(filename = "hello"):
    subprocess.call("gdb hello -ex='disassemble main' -q -ex='q' ",shell=True)
