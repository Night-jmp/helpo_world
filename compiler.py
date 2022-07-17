import subprocess


def compile():
    opts = getopts()
    print("[-] Compiler options have not been implemented. :(")
    subprocess.call("gcc hello.c -o hello", shell=True)

def print_help():
    subprocess.call("man gcc", shell=True)

def getopts():
    
    opts = []
    try:
        # Take previously used options and reuse them
        # Machine learning ???
        fd = open("user_options", "r")
        lines = fd.read().split("\n")[-4:]
        
        if len(lines) >= 4:
            for i in lines:
                if i not in opts:
                    opts.append(i)
            if len(opts) == 2:
                print("[+] Using recent compiler options")
                return opts[0].split(",")
    except:
        pass

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
