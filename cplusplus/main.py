""" a homage to bjarne stroustrup, the creator of the c++ language"""
from stroustrup import CPP

def __main__():
    lang = CPP()
    lang.generateCode()
    lang.write2File()
    
if __name__ == '__main__':
    __main__()
