#This File is used to run the code if deleted, code can not be executed.

def open_file(filename):
    filename = 'main.lou'
    data = open(filename, 'r').read()
    return data
    
def parse(filecontents):
    fl = ""
    if "print " in filecontents:
        fl = filecontents.replace("print ", "")
        fl = fl.replace("\n", "")
        fl = fl.replace("\"", "")
        if ";" in fl:
            fl = fl[:-1]
            if "; " in fl:
                fl = fl.replace("; ", "\n")
            else:
                fl = fl.replace(";", "\n")
    
    if fl is not None:
        return fl
    else:
        return ""
        
def run():
    data = open_file('main.lou')
    print(parse(data))

run()
