# COP1030 - Module A7 - Jason Kee
#
# Design, code, and test a program that reads the text file below as an input file. (First save
# this file to your system, and put it in a folder where your program can find it or make sure
# you tell your program exactly where it can be found.)

# Importing re
import re

# Read the file
read = open("cr.txt","r")

# (1) Strip out all punctuation (including periods, apostrophes, quotation marks, commas, etc.).
string = "" 
for i in read: 
    i = re.sub(r'[^\w\s]','',i) 
    if re.search("\n",i): 
        string =string +i[0:-1]+" " 
    else: 
        string =string +i

# (2) Count the words.
words = string.split()
totalWords = len(words)

# (3) Add up the total length of all the words.
sum =0 
for k in words: 
    l = len(k) 
    sum = sum +l

# (4) Calculate the average word length.
average = sum/totalWords

# (5) Output the values you calculated in steps 2,3,4 above.
print("Total words in the file is:", totalWords)
print("Total length of all of the words in the file is:", sum)
print("Average length of all of the words in the file is:", average)
