# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 19:18:49 2020

@author: vgadi
"""

""" a homage to bjarne stroustrup, the creator of the c++ language"""

import sys

""" 
as the scriptIO library and the extract library are not in the original directory, we add the folders to the system path, so
that the interpreter can search for the files there
"""

sys.path.append('scriptIO')
sys.path.append('extract')

""" 
importing the required libraries
"""

import scriptIO
import extract

""" 
imported to iterate over two lists simulateneously
"""
import itertools


class CPP:

    # default constructor
    def __init__(self, userLibraries = ['iostream'], filename = 'temp.py'):
        """ the filename from where the python code is to be read """
        self.filename = filename
        
        """ the list of c++ libraries to be included """
        self.libraries = userLibraries
        
        """ an empty string for initializing cpp code """
        self.generatedCode = ''
        
        """ the extension of the file to be generated """
        self.extension = '.cpp'
        
        """ to add new lines """
        self.newline = '\n'
        
        """ an empty string for initializing the cpp libraries """
        self.libCode = ''
        """ 
        the boilerplate syntax for a .cpp file 
        """
        
        # int main()
        self.int_main = 'int main(void){'
        
        """
        as there is a difference in syntax between python and cpp, we have to
        write some minor syntax by ourselves
        """
        self.semicolon = ' ; '
        self.cout = 'cout << '
        self.starterCode = ''
        self.endCode = 'return 0; \n}'
        self.coutNewline = "cout << endl;"
        
        """ generating the code for including the libraries """
        self.__createLibraries__()
        
        """ including the libraries and also the int main(void) part """
        self.__createStarterCode__()

    
    """ creates the required include library syntax """
    def __createLibraries__(self):
        includes = []
        text = ''
        # creates the syntax for each library that has to be included to be
        # appends that to a list
        for library in self.libraries:
            """
            creating for example '#include<iostream>'
            """
            text = '#include<' + str(library) + '>'
            includes.append(text)
        
        # adds the library syntax to the actual cpp code
        for include in includes:
            self.libCode += str(include)
            
        self.libCode += self.newline


    """
    creates the initial code for the cpp file
    """
    def __createStarterCode__(self):
        """
        adding 'using namespace std; ' and 'int main(void){' to the code
        """
        self.libCode = self.libCode + self.newline + 'using namespace std;'
        self.libCode += self.newline + self.int_main
        self.starterCode = self.libCode + self.newline
        self.generatedCode = self.starterCode
        


    """
    generates the required cpp code, currently supports only print statements
    """
    def generateCode(self):
        
        # reading the code written in the script
        text = scriptIO.readScript(self.filename)
        
        # extracting the keywords, and the texts from the code
        keywords, texts = extract.extractFromScript(text)
        
        # zipping the two lists so as to iterate over them simultaneously
        for (keyword, text) in zip(keywords, texts):
            # currently only support for print()
            if str(keyword) == 'print':
                
                # add 'cout << ', the 'text' extracted, and the semicolon
                self.generatedCode += self.cout + str(text) + self.semicolon
                # add a newline both in the output of file, as per the .py file
                # add a '\n' to increase the readibility the '.cpp' code
                self.generatedCode += str(self.coutNewline) + self.newline
            
            # add a '\n' to increase the readibility the '.cpp' code
            self.generatedCode + self.newline
            
    """
    write the generated code to a .cpp file
    """
    def write2File(self):
        
        # to the generated code, add the ending lines of a .cpp file
        self.generatedCode += self.endCode
        
        # create the required '.cpp' file from the generated code
        scriptIO.createScript(extension = '.cpp', code = self.generatedCode, filename = 'temp')
