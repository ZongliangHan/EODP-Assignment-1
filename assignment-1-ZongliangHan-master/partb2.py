# Part B Task 2
import re
import os
import sys

#This is the function for pre_processing
def prepocessing (string):
    pattern = r'[^a-zA-Z]'
    string = re.sub(pattern, r' ', string)
    string = re.sub(r' +', r' ', string)
    string = string.lower()
    return string

#pre_processing the the given article
txt = sys.argv[1]
f=open('cricket/'+txt[7:], 'r')
string = f.read()
string = prepocessing (string)
print (string)

        
