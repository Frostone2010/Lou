#This File is used to run the code if deleted, code can not be executed.

from sys import *

def open_file(filename):
    data = open(filename, 'r').read()
    return data
    
def parse(filecontents):
    fl = ""
    if "print " in filecontents:
        fl = filecontents.replace("print ", "")
        fl = fl.replace("\n", "")
        fl = fl.replace("\"", "")
        if ";" in fl:
            fl - fl[:-1]
            if "; " in fl:
                fl = fl.replace("; ", "\n")
            else:
                fl = fl.replace(";", "\n")
    
    if fl is not None:
        return fl
    else:
        return ""
        
def run():
    data = open_file(argv[1])
    print(parse(data))

run()
