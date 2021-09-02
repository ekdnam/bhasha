# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 19:18:49 2020
@author: vgadi
"""
import sys

sys.path.append('scriptIO')
sys.path.append('extract')
import scriptIO
import extract
import itertools


class CPP:

    # default constructor
    def __init__(self, user_libraries = ['iostream'], filename = 'temp.py'):
        try:
            """ empty string which will contain the script read from the python file """
            self.script = ''
            """ the filename from where the python code is to be read """
            self.filename = filename
        
            """ the list of c++ libraries to be included """
            self.libraries = user_libraries
            
            """ an empty string for initializing cpp code """
            self.generated_code = ''
            
            """ the extension of the file to be generated """
            self.extension = '.cpp'
            
            """ to add new lines """
            self.newline = '\n'
            
            """ comments in python file """
            self.comments = ''
            
            """ an empty string for initializing the cpp libraries """
            self.lib_code = ''
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
            self.starter_code = ''
            self.end_code = 'return 0; \n}'
            self.cout_newline = "cout << endl;"
        
        except:
            print('An unexpected error occurred while creating the class object.')
            raise
        try:
            """ generating the code for including the libraries """
            self.__create_libraries__()
        except:
            print("An unexpected error occurred while creating the libraries")
            raise
            
        try:
            """ including the libraries and also the int main(void) part """
            self.__create_starter_code__()
        except:
            print("An unexpected error occurred while creating the starter code.")

    
    """ stable """
    """ creates the required include library syntax """
    def __create_libraries__(self):
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
            self.lib_code += str(include)
            
        self.lib_code += self.newline

    """ stable """
    """
    creates the initial code for the cpp file
    """
    def __create_starter_code__(self):
        """
        adding 'using namespace std; ' and 'int main(void){' to the code
        """
        self.lib_code = self.lib_code + self.newline + 'using namespace std;'
        self.lib_code += self.newline + self.int_main
        self.starter_code = self.lib_code + self.newline
        self.generated_code = self.starter_code
        

    """ stable """
    """
    generates the required cpp code, including comments transformed from python to c++ format
    currently supports only print statements
    """
    def generate_code(self):
        
        # reading the code written in the script
        self.script = scriptIO.readScript(self.filename)
        
        # extracting the comment and the code row indices
        comment_row_indices, code_row_indices = extract.get_indices(self.script)
        # stripping the script of comments
        self.script, self.comments = extract.strip_comments(self.script)
        # extracting the keywords, and the texts from the code
        keywords, texts = extract.clean_raw_code(self.script)
        #def POC(self, keywords, texts, comments, comment_row_indices, code_row_indices):
        code_iterator, comment_iterator = 0, 0
        #print(code_row_indices)
        #print(comment_row_indices)
        # length of the list containing the keyords
        len_code = len(keywords)
        #print(len_code)
        # length of the list containing the comments
        len_comments = len(self.comments)
        #print(len_comments)
        # add comments and code
        while(code_iterator < len_code and comment_iterator < len_comments):
            
            # if the comment is going to be before the code
            if  (comment_row_indices[comment_iterator] < code_row_indices[code_iterator]):
                # add comment to the generated code    
                self.generated_code += '//' + str(self.comments[comment_iterator])[1:]
                # increment comment iterator
                comment_iterator += 1
        
            # if the code is going to before the comment
            elif (code_row_indices[code_iterator] < comment_row_indices[comment_iterator]):
                # if keyword is print
                if keywords[code_iterator] == 'print':
                    # add code to the line
                    self.generated_code += self.cout + ' ' + str(texts[code_iterator]) + str(self.semicolon)
                    # increment code iterator  
                code_iterator += 1
            
           
            # if the code and comment is on the same line
            elif(code_row_indices[code_iterator] == comment_row_indices[comment_iterator]):
                if (keywords[code_iterator] == 'print'):
                    # add code and comments to the generated code
                    self.generated_code += self.cout + ' ' + str(texts[code_iterator]) + str(self.semicolon) + ' //' +  str(self.comments[comment_iterator])[1:]
                # increment code and comment iterator
                code_iterator += 1
                comment_iterator += 1
            
            
            # add a newline to the generated code for readibility
            self.generated_code += str(self.newline)
        
        # if code list is completed, add comments
        while(comment_iterator < len_comments):
            # add comments to the generated code
            self.generated_code += '// ' + str(self.comments[comment_iterator])[1:]
            # increment comment iterator
            comment_iterator += 1
            # add newline to code for readability
            self.generated_code += self.newline
                
        while(code_iterator < len_code):
            if keywords[code_iterator] == 'print':
                 # add code to generated code      
                self.generated_code += self.cout + ' ' + str(texts[code_iterator]) + str(self.semicolon)
            # increment code iterator      
            code_iterator += 1
            # add newline to code for readability   
            self.generated_code += str(self.newline)
        

    """ stable """
    """
    write the generated code to a .cpp file
    """
    def write2File(self):
        try:
            # to the generated code, add the ending lines of a .cpp file
            self.generated_code += self.end_code
        
            # create the required '.cpp' file from the generated code
            scriptIO.createScript(extension = '.cpp', code = self.generated_code)
            
            print("\n.cpp file sucessfully generated!")
            
        except:
            
            print("\nThere was an error while creating the file :(")
