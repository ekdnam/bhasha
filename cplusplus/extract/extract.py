# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 21:07:11 2020

@author: vgadi
"""

import re 
import scriptIO

""" stable """
"""
gets the keywords (print etc), and the text within thr parentheses


the function extractFromScript() has the following parameters:
    
1) text (string): the code from which the keywords, text has to be extracted

returns: keywords (list of strings), texts (list of strings)
"""
def clean_raw_code(text):
    keywords = []
    texts = []
    
    for line in text:
        try:
            
            if str(line)[0] == '':
                continue
            """
            get value before the parentheses
            """
            keyword = re.compile("(.*?)\s*\(")
            flag = re.search("(.*?)\s*\(", line)
            if flag is None:
                continue
            else:
                keyword = keyword.match(line)
                keyword = keyword.group(1)
                keywords.append(keyword)
            
                """
                get value in the parentheses
                """
                text = re.compile(".*?\((.*?)\)")
                text = text.match(line)
                text = text.group(1)
                texts.append(text)
            
        except:
            keywords, texts = -1, -1
            print("An error occurred while applying regular expressions")
            raise
            
    return keywords, texts

""" stable """
# returns whether comment exists or not and if yes the column number also
def comment_exists(text):
    col = text.find('#')
    if(col != -1):
        return 1, col
    else:
        return 0, -1


""" stable """
""" returns the indices of the rows where code and / or comments are present"""

def get_indices(script):
    
    codeRowIndices, commentRowIndices = [], []
    row = 0
    flag, col = 0, 0
    
    for line in script:
        row += 1
        flag, col = comment_exists(line)
    
    # check whether comment exists on the line
        if(flag):
            # add the row number to commentIndices
            commentRowIndices.append(row)
            if (col > 0):
                codeRowIndices.append(row)
        
        # if line has an empty line
        elif line == '':
            continue
        
        else:
            codeRowIndices.append(row)
        
    return commentRowIndices, codeRowIndices
            

""" stable """          
"""
removes the single line comments from the python script
"""
def strip_comments(script):
    """ 
    initializing empty lists to get the comments, 
    and an empty string to store the comments
    """
    comments = []
    comment = ''
    row = 0
    
    # iterate over the script line by line
    for line in script:
        
        row += 1
        # get single line comments
        
        if line.find('#') != -1:
        
            # get where the comment begins in the line
            ind = line.find('#')
            
            
            
            # isolate commment from the line
            comment = (str(line))[ind:]
            
            # append comment to the list of comments
            comments.append(comment)
            
            
    # replacing the comments in script with an empty string
    def replaceCharacters(s, unwanted, input_char = ''):
    # Iterate over the strings to be replaced
        for elem in unwanted:
        # Replace the string, does not do anything if `elem` not in `s`
            s = s.replace(elem, input_char)
        return s
    
    # call the function
    script_new = [replaceCharacters(x, comments) for x in script]
    
    
    # remove all the empty strings in the script_new 
    raw_code = list(filter(None, script_new))
    
    return raw_code, comments


""" the code below is the proof of concept for converting python comments to cpp comments """

"""
filename = 'temp.py'
script = scriptIO.readScript(filename)
script = list(filter(None, script))
commentRowIndices, codeRowIndices = get_indices(script)
commentRowIndices.append(-1)
codeRowIndices.append(-1)
raw_code, comments = stripComments(script)
keywords, texts = clean_raw_code(raw_code)
print(texts[0])
print(str(comments[0])[1:])
#
def POC(keywords, texts, comments, commentRowIndices, codeRowIndices):
    codeIterator, commentIterator = 0, 0
    
    len_code = len(keywords)
    
    len_comments = len(comments)
    
    while(codeIterator < len_code and commentIterator < len_comments):
        if(codeRowIndices[codeIterator] == commentRowIndices[commentIterator]):
            
            print('print ' + str(texts[codeIterator]) + ' // ' + str(comments[commentIterator])[1:] + '\n')
            codeIterator += 1
            commentIterator += 1
        
        elif (codeRowIndices[codeIterator] > commentRowIndices[commentIterator]):
            
            print('// ' + str(comments[commentIterator])[1:] + '\n')
            commentIterator += 1
        
        elif (codeRowIndices[codeIterator] < commentRowIndices[commentIterator]):
            
            if keywords[codeIterator] == 'print':
                print('print ' + str(texts[codeIterator]) + '\n')
            codeIterator += 1
            
        
    while(commentIterator < len_comments):
        print('// ' + str(comments[commentIterator])[1:] + '\n')
        commentIterator += 1
    
    while(codeIterator < len_code):
        if keywords[codeIterator] == 'print':
            print('print ' + str(texts[codeIterator]) + '\n')
        codeIterator += 1
    


POC(keywords, texts, comments, commentRowIndices, codeRowIndices)

"""
