# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 08:11:11 2019

@author: asus
"""

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

ps = PorterStemmer()
file1 = open(r"C:\Users\asus\Desktop\IS\nlp.py\test.txt")
line = file1.read()
words = line.split() #tokenize 
file1.close()
stop_words = set(stopwords.words('english'))
file2 = open("append.txt","a+")
for w in words:
    if w not in stop_words:
        file2.write(w+" ")

new_lines = file2.readlines()

for i in range(1):
    new_words1 = new_lines[i]

new_words = new_words1.split()

stem_file=open("stemm.txt","a+")
for w in new_words:
    stemed=ps.stem(w)
    stem_file.write(stemed+" ")

stem_file.close()

#file3 = open("C:\Users\asus\Stemming.txt","a+")
#for w in new_words:
#    stem_words = ps.stem(w)
#
#file3.close()