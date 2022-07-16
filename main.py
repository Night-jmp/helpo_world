#!/usr/bin/env python3

import sys, subprocess
import disassembler
import cgenerator
import compiler
import bigdata

def menu():
    print("\n\n1.) Generate Hello World")
    print("2.) Compile")
    print("3.) Disassemble")
    print("4.) Debug")
    print("5.) Hexdump")
    print("6.) Run")
    print("7.) Big Data")
    print("0.) Exit")
    opt = input("> ")
    print("\n")
    if opt == "0":
        sys.exit(0)
    elif opt == "1":
        print("Who would you like to greet?")
        name = input("> ")
        cgenerator.generate(name)
        print("[+] C code generated successfully!")
    elif opt == "2":
        compiler.compile()
        print("[+] Successfully compiled!")
    elif opt == "3":
        disassembler.disasm("hello")
    elif opt == "4":
        print("[-] Not implemented")
    elif opt == "5":
        subprocess.run(["/usr/bin/xxd", "hello"])
    elif opt == "6":
        subprocess.run(["./hello"])
    elif opt == "7":
        factory = bigdata.bigDataHandlerFactory(bigDataVersion=1)
        handler = factory.generateDataHandler()
        handler.displayData()

    else:
        print("?")

if __name__ == "__main__":
    print("\n\tHelpo world v1.0")
    while True:
        menu()
