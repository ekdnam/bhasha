# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 21:07:11 2020

@author: vgadi
"""

import re 
"""
gets the keywords (print etc), and the text within thr parentheses


the function extractFromScript() has the following parameters:
    
1) text (string): the code from which the keywords, text has to be extracted

returns: keywords (list of strings), texts (list of strings)
"""
def extractFromScript(text):
    keywords = []
    texts = []
    for line in text:
        try:
            """
            get value before the parentheses
            """
            keyword = re.compile("(.*?)\s*\(")
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

"""
removes the comments from the python script
def comment(text):
    
"""
