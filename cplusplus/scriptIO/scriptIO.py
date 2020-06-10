# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:49:09 2020

@author: vgadi
"""

import sys

"""
reads a .py script

function readScript() has the following parameters:

1) filename (string): the name of the file from which text to be extracted

returns: list of strings new lines split with '\n'
"""
def readScript(filename):
    try:
        # open file to read
        script = open(filename, 'r')
        # read the file
        script = script.read()
        # convert the newlines into '\n'
        script = script.split('\n')
        return script
    except OSError as err:
        print("OS error: {0}".format(err))
        raise
    except:
        print("Unexpected error: ", sys.exc_info()[0])
        raise


"""
creating the required file

function createScript() has the following parameters:
    
1) extension (string): the extension of the file to be created
2) code (string): the code to be added to the file
3) filename (string): the name of the file to be created. default: 'helloWorld'
    
returns: nothing
"""
def createScript(extension, code, filename = 'helloWorld'):
    try:
        filename = filename + extension
        writeFile = open(filename, 'w')
    
        writeFile = writeFile.write(code)
    except:
        print("\nAn error occrred while writing to file.")
