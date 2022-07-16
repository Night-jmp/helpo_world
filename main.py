#!/usr/bin/env python3

import sys, subprocess
import disassembler
import cgenerator
import compiler

def menu():
    print("\n\n1.) Generate Hello World")
    print("2.) Compile")
    print("3.) Disassemble")
    print("4.) Debug")
    print("5.) Hexdump")
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
        disassembler.disasm()
    elif opt == "4":
        print("[-] Not implemented")
    elif opt == "5":
        subprocess.run(["/usr/bin/xxd", "hello"])
    else:
        print("?")

if __name__ == "__main__":
    print("\n\tHelpo world v1.0")
    while True:
        menu()
