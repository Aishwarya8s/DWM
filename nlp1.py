# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 08:11:11 2019

@author: asus
"""

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

ps = PorterStemmer() #initialize stemmer

file1 = open(r"C:\Users\asus\Desktop\IS\nlp.py\test.txt")
line = file1.read()
words = line.split() #tokenize 
file1.close()


stop_words = set(stopwords.words('english')) #store the stopwords
file2 = open("notstop.txt","a+") #a+ used for reading and appending.
for w in words:
    if w not in stop_words:
        file2.write(w+" ")
        
testfile = open("notstop.txt","r") #reading file for wildcard query
print("Enter A Query")
pattern = input()

compiled = re.compile(pattern) #we can compile pattern into pattern objects, which have methods for various operations such as searching for pattern matches
ms = compiled.search(testfile.read()) #searching the query
print(ms)   #printing if query is found
testfile.close()

new_lines = file2.readlines() #storing the document in a list

for i in range(1):  #convert the list into string
    new_words1 = new_lines[i]

new_words = new_words1.split() #splitting string to make indivisual words

stem_file=open("poststem.txt","a")
for w in new_words:
    stem_file.seek(0)
    stemed=ps.stem(w)
    stem_file.write(stemed+" ")
    
stem_file.close()

    
    
    
    
    