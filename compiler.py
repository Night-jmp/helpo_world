import subprocess

def compile():
    subprocess.call("gcc hello.c -o hello", shell=True)
