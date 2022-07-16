import subprocess

def compile():
    opts = getopts()
    print("Compiler options have not been implemented. :(")
    subprocess.call("gcc hello.c -o hello", shell=True)

def print_help():
    subprocess.call("man gcc", shell=True)

def getopts():
    try:
        fd = open("user_options", "r")
        lines = fd.read().split("\n")
        x = set(lines)
        if len(x) == 1:
            print("Using recent compiler options")
            return x[0]
    except:
        pass

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

    fd = open("user_options", "a")
    
    for x in opts:
        fd.write(x + ",")
    fd.write("\n")
    fd.close()

    return opts
