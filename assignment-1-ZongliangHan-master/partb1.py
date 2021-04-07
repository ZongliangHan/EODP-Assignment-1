## Part B Task 1
import re
import pandas as pd
import os

ID = []
filename = []
i=0

#reading in the text and find the ID
for file in os.listdir('cricket'):
    f=open('cricket/'+file, 'r')
    string = f.read()  
    pattern = r'[A-Z]{4}-\d{3}\w?.?'         #pattern of ID
    if re.search(pattern, string) :
        filename.append(file)
        id = re.findall(pattern, string)
        ID.append(id)
    else :
        print (file)
        print("Not found")
    f.close()

#make a list of modified ID
good_id = []
for id in ID:                   #check if the id has last letter
    if id[0][-1].isdigit():
        id = id[0]
        good_id.append(id)
    elif id[0][-1].isupper():
        id = id[0][0:9]
        good_id.append(id)
    else:
        id = id[0][0:8]
        good_id.append(id)

#put filename and id into dataframe
file_id = pd.Series(good_id)
file_name = pd.Series(filename)
cricket = pd.DataFrame({'file name':file_name, 'file ID':file_id})  
cricket = cricket.set_index('file name')
cricket = cricket.sort_values(by='file name', ascending=True)
print (cricket)

#make a csv file to store those data
cricket.to_csv(r'partb1.csv', header = True, index = True)

