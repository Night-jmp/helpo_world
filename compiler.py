import subprocess

def compile():
    opts = getopts()
    print("Compiler options have not been implemented. :(")
    subprocess.call("gcc hello.c -o hello", shell=True)

def print_help():
    subprocess.call("man gcc", shell=True)

def getopts():
    opts = []
    print("Add -c? (y/n/h)")
    opt = input("> ")
    if opt == "y":
        opts.append("-c")
    elif opt == "h":
        print_help()
    print("Add -S? (y/n/h)") 
    opt = input("> ")
    if opt == "y":
        opts.append("-S")
    elif opt == "h":
        print_help()
    print("Add -E? (y/n/h)") 
    opt = input("> ")
    if opt == "y":
        opts.append("-E")
    elif opt == "h":
        print_help()
    print("Add -g? (y/n/h)") 
    opt = input("> ")
    if opt == "y":
        opts.append("-g")
    elif opt == "h":
        print_help()
    print("Add -O? (y/n/h)")
    opt = input("> ")
    if opt == "y":
        print("What level?")
        lvl = input("> ")
        opts.append(f"-O{lvl}")
    elif opt == "h":
        print_help()

    return opts
