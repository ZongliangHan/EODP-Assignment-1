## Part B Task 5
import re
import os
import sys
import pandas as pd
from nltk import PorterStemmer
from sklearn.feature_extraction.text import TfidfTransformer
import math
from numpy import dot
from numpy.linalg import norm

#This function is for calculating cosine similarity
def cosine_sim(v1, v2):
    return round (dot(v1, v2)/(norm(1)*norm(v2)), 4)

ps = PorterStemmer()
#This function is for pre-processing, deleting all non alphabatic character and coverting to lower case.  
def prepocessing (pre_string):
    pattern = r'[^a-zA-Z]'
    pre_string = re.sub(pattern, r' ', pre_string)
    pre_string = re.sub(r' +', r' ', pre_string)
    pre_string = pre_string.lower()
    return pre_string

#This function is for temming
def stemming (stem_string):
    ps = PorterStemmer()
    stem_list = []
    convert_list = stem_string.split()
    for elem in convert_list:
        elem1 = ps.stem(elem)
        stem_list.append(elem1)
    return stem_list

#finding the matched articles by checking if key words are in the article
txt = list(sys.argv)[1:]
txt_lower = []  #convert the key words into lower case first and stem them
for i in txt:
    i = i.lower()
    i = ps.stem(i)
    txt_lower.append(i) 
file_name = []


term_count = []
for file in os.listdir('cricket'):  #check if the key words is in article
    f=open('cricket/'+file, 'r')
    string = f.read()
    string = prepocessing (string)
    list = stemming (string)
    count = []
    if all(elem in list for elem in txt_lower):
        file_name.append(file)
        for key in txt_lower:  #make a list of term frequency
            i = 0
            for word in list:
                if key == word:
                    i+=1
            count.append(i)            
        term_count.append(count)
        
#check if there is no file matched, exit the program
if file_name == []:
    sys.exit('No file matched')

# making a list of tf-idf
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(term_count)
doc_tfidf = tfidf.toarray()

#calculating the cosine similarity (comparing the text with key words)
vector = []        #get a vector of 1, since query is key words itself
for elem in txt_lower:
    vector.append(1)
unit_vector = [x/math.sqrt(len(vector)) for x in vector]
sims = [cosine_sim(unit_vector, doc_tfidf[d_id]) for d_id in range (doc_tfidf.shape[0]) ]

#reading the ID using partb3.csv        
file_id = pd.read_csv('partb1.csv', encoding = 'ISO-8859-1') 
file_id = file_id.set_index('file name')
file_id = file_id.squeeze()
id = []
for elem in file_name:
    id1 = file_id[elem]
    id.append(id1)  

#matching the similarity with its file id
result = pd.DataFrame({'name':id, 'score':sims})
result = result.set_index('name')
result = result.sort_values(by = 'score', ascending = False)

#print out results
print ('There are', len(result.index), 'results in total')
print ('')
print (result)    
