import subprocess
from abc import ABC, abstractmethod


class DisassemblerHandler(ABC):

    def __init__(self, *args, **kwargs):
        self.arguments = args

        for key, val in kwargs.items():
            self.__dict__[key] = val

    @abstractmethod
    def disasm(self):
        pass


class DisassemblerHandlerV1(DisassemblerHandler):

    def disasm(filename="hello"):
        subprocess.call("gdb hello -ex='disassemble main' -q -ex='q' ", shell=True)



class disassemblerHandlerFactory:
    def __init__(self, disasmVersion):
        self.disasmVersion = str(disasmVersion)

    def generateDisasmHandler(self) -> DisassemblerHandler:
        return globals()["DisassemblerHandlerV" + self.disasmVersion]()



