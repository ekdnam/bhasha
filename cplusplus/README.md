# cplusplus

A library that that transforms python code into cpp code.

The 'temp.py' file gets metamorphosed into 'temp.cpp'.

## Libraries created

* stroustrup

Creates a CPP class, which does all the heavy handed work of generating code.

* scriptIO

Taking the input and producing output of a script.

* extract

Extracting text from the code. We get two lists of strings, one is a list of keywords ('print' etc), 
and a list of texts (the text enclosed in parentheses).

Currently, the code is being tested for bugs.