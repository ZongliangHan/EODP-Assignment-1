## Part B Task 3
import re
import sys
import pandas as pd
import nltk
import os

#This function is for pre-processing, deleting all non alphabatic character and coverting to lower case.  
def prepocessing (string):
    pattern = r'[^a-zA-Z]'
    string = re.sub(pattern, r' ', string)
    string = re.sub(r' +', r' ', string)
    string = string.lower()
    return string

#finding the matched articles by checking if key words are in the article
txt = list(sys.argv)[1:]
txt_lower = []  #convert the key words into lower case first
for i in txt:
    i = i.lower()
    txt_lower.append(i)
file_name = []

for file in os.listdir('cricket'):  #check if the key words is in article
    f=open('cricket/'+file, 'r')
    string = f.read()
    string = prepocessing (string)
    list = string.split()
    if all(elem in list for elem in txt_lower):
        file_name.append(file)

#reading the ID using partb3.csv        
file_id = pd.read_csv('partb1.csv', encoding = 'ISO-8859-1') 
file_id = file_id.set_index('file name')
file_id = file_id.squeeze()
id = []
for elem in file_name:
    id1 = file_id[elem]
    id.append(id1)  

#print out results
if id == []:
    print ('No file matched!')
else:
    print ('There are', len(id), 'results in total')
    print ('')
    for i in id:
        print (i)
