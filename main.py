import sys
import disassembler
import cgenerator

def menu():
    print("\n\n1.) Hello World")
    print("2.) Compile")
    print("3.) Disassemble")
    print("4.) Debug")
    print("0.) Exit")
    opt = input("> ")
    print("\n")
    if opt == "0":
        sys.exit(0)
    elif opt == "1":
        print("Who would you like to greet?")
        name = input("> ")
        cgenerator.generate(name)
    elif opt == "2":
        print("Not implemented")
    elif opt == "3":
        print("Enter the full path to your hello world program")
        path = input("> ")
        disassembler.disasm(path)
    elif opt == "4":
        print("Not implemented")
    elif opt == "9":
        print(open("/bin/ls", "rb").read())
    else:
        print("what lol")

if __name__ == "__main__":
    print("\n\tHelpo world v1.0")
    while True:
        menu()
