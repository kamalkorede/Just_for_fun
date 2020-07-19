# -*- coding: utf-8 -*-
import io, time, json
import requests
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
import re
from IPython.display import display

from datetime import datetime

import string

"""
Created on Mon Mar 23 18:00:16 2020

@author: KAMALDEEN
"""
"""Python for everybody by charles severance"""

text = "This course will introduce the basics of data science"
match = re.search(r"data science", text)
#print(match.start())

#line = 'please have a nice day'
#print(line.startswith('please'))

data= "kamal96adekola@gmail.com june 10 1996"
atpos=data.find('@')
#print (atpos)
#spos=data.find(".",atpos)
#print(spos)
#host = data[atpos+1 : spos]
#print(host)

# fhand = open('notepad.txt', 'r')
count = 0
#for lines in fhand:
#    count +=1
#print (count)

# fhand = open('notepad.txt')
# input = fhand.read()
#print (len(input))
#print(input[:])

# fhand = open("notepad.txt")
#for line in fhand:
#    line = line.lower()
#    line = line.rstrip()
#    if line.startswith('data'):
#        print(line)

# fname= input("enter file name:")
# fhand = open(fname)
# count = 0
#for line in fhand:
#    count +=1
#print(count)
#
#line = 'first second third'
#thing = line.split()
#print (thing)

# fhand = open('notepad.txt')
# input = fhand.read()
# words = input.split()
count = []
count = dict()
#for word in words:
#    count[word] = count.get(word,0)+1
#        if word not in count:
#        count[word] = 1
#    else:
#        count[word] +=1    
#    if word not in count:count.append(word)
#print(count)
#print(len(count))
#print(len(words))
#
#inp = input('enter filenme:')
#fhand = open(inp)
#fh = fhand.readlines()
#print (fh)
#count = 0
#for line in fh:
#    if line.startswith ('Data'):
#        count +=1
#print (count)
#
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 15
purse['money'] = 10
# print(purse)
#for key in purse:
#    print(key, purse[key])
#for key,value in purse.items():
#    print(key,value)
# purses = purse.items()
#print(purses)

#counts = dict()
#print('Enter a line of text')
#line = input('')
# words = line.split()
#print ('words:', words)

#print ('counting:')
#for word in words:
#    counts[word]=counts.get(word,0)+1
#print('counts', counts)

#inp = input('enter filenme:')
#fhand = open(inp)
#fh = fhand.read()
#words = fh.split()
#
#counts = dict()
#for word in words:
#    counts[word]=counts.get(word,0) + 1
#bigcount = None
#bigword = None
#for word,count in counts.items():
#    if bigcount is None or count > bigcount:
#        bigword = word
#        bigcount = count
#print(bigword,bigcount)

t = tuple()
#print (dir(t))
#(x,y) = (4,'fred')
#print(x)
#d = {'a':10, 'c':22, 'b':1}
#print(sorted(d.items()))
#inp = input('enter filenme:')
#hand = open('mbox-short.txt')
#fhand= hand.readlines()
#for line in fhand:
##    print(line)
#    lines = line.rstrip()
#    if lines.find('from') >= 0:print (lines)
#    if re.search('from',line):print(line)

#x = 'My 2 favourite numbers are 19 and 42'
#y = re.findall('[0-9]+',x)
#print(y)

# w = open('mbox-short.txt')
# x = w.read()
#print(x)
# y = re.findall('\S+@\S+',x)
# y = re.findall('@[^ ]*',x)
#z = []
#for mail in y:
#    if mail in z:
#        continue
#    else:
#        z.append(mail)
#print(z)

# w = open('mbox-short.txt')
# x = w.read()
# y = re.findall('[0-9]+',x)
# y = re.findall('\d+',x)
# z = 0
#for i in y:
#    a = int(i)
#    print(type(a))
#    print(i)
#    z = z + a
#print(z)


""" This is AI Saturday's first assignment"""
def rotate_list(l, n):
    for i in range(n):
        element = l.pop(0)
        l.append(element)
    return l


""" Practicing Zip function"""
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ] 
roll_no = [ 4, 1, 3, 2 ]
marks = [ 40, 50, 60, 70 ]
mapped = zip(name, roll_no, marks)
mapped = list(mapped)
# print ("The zipped result is : ",end="") 
# print (mapped)


"""Practicing with Pandas with Zico Colter CMU"""

df = pd.DataFrame([(1, 'Kolter', 'Zico'),
(2, 'Manek', 'Gaurav'),
(3, 'Rice', 'Leslie'),
(4, 'Peres', 'Filipe'),
(5, 'Gates', 'Bill'),
(6, 'Musk', 'Elon')],
columns=["Person ID", "Last Name", "First Name"])

df.set_index("Person ID", inplace=True)
# print(df)

# df = pd.read_csv(filename) # read CSV file into DataFrame

# print(df.head())  # get first five rows of DataFrame

"""index into a dataframe with df.loc[rows, columns] and df.iloc[row numbers, column numbers] """

series_lastnames = df.loc[:, "Last Name"] # Series of all last names
# print(type(series_lastnames))
# print(series_lastnames)

df_lastname = df.loc[:, ["Last Name"]]
# print(type(df_lastname))
# print(df_lastname) # DataFrame with one column

df_id = df.loc[[1,2], :] # DataFrame with only ids 1,2
# print(df_id)

df.loc[1,"Last Name"] = "Kilter" # Set an entry in a DataFrame
# print(df)

df.loc[7,:] = ("Moore", "Andrew") # Add a new entry with index=7
# print(df)
# print(df.iloc[1,0])



"""Practicing with Pandas with data camp"""

cities = ['Austin', 'Dallas', 'Austin', 'Dallas']
signups = [7, 12, 3, 5]
visitors = [139, 237, 326, 456]
weekdays = ['Sun', 'Sun', 'Mon', 'Mon']
list_labels = ['city', 'signups', 'visitors', 'weekday']
list_cols = [cities, signups, visitors, weekdays]
zipped = list(zip(list_labels, list_cols))
# print(zipped)
data = dict(zipped)
users = pd.DataFrame(data)
# print(users)
users['fees'] = 0 # Broadcasts to entire column
# print(users)


heights = [ 59.0, 65.2, 62.9, 65.4, 63.7, 65.7, 64.1 ]
data = {'height': heights, 'sex': 'F'}
results = pd.DataFrame(data)
# display(results)
results.columns = ['height (in)', 'gender']
results.index = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# print(results)


filepath = 'kpit_weather.csv'
sunspots = pd.read_csv(filepath, parse_dates = [0,1])
# sunspots = pd.read_csv(filepath, parse_dates = [[0,1]])
sunspots.index = sunspots['ZTime']
sunspots.index.name = 'date'
# print(sunspots.iloc[10:20,:])
# sunspots.info()

"""List comprehensions practice"""
# print([n for n in range(10) if n % 2])

"""datetime in python"""
# print(datetime(1970, 1, 1).strftime('%Y-%d-%B'))

"""Hacker rank challenge"""
# class Mynumbers:
#     def __init__(self, n):
#         self.n = n
        
#     def multiple(self):
#         for i in range(1,11):
#             mult = self.n*i
#             print("n x i = ", mult )
#             print("{} x {} = {}".format(N, i, (N*i)))
#         return None
# n = int(input('Enter: '))

"""Udacity AWS intro to ML"""
# label_list = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality']
# print(label_list)
# for i in label_list:
#     i = i.replace(' ','_')
#     print(i)
  
"""MIT 6.001 EDX - Problem set 1  - problem 1"""
  
# s=input()
# counter = 0
# for i in s:
#     if i == "a":
#         counter+=1
#     elif i == "e":
#         counter+=1
#     elif i == "o":
#         counter+=1
#     elif i=="i":
#         counter+=1
#     elif i== "u":
#         counter+=1

# print(counter)

"""MIT 6.001 EDX - Problem set 1  - problem 2"""

# s = "abcabcdef"
s = 'azcbobobegghakl'
# s = 'zyxwvutsrqponmlkjihgfedcba'
# print(s[:-1])
# print(s[s.index("a")+2])
# lst = []
# count=0
# for i in range(len(s)):
#     lst.append(s[i:i+3])
# for bob in lst:
#     if bob == 'bob':
#         count+=1
# print("Number of times bob occurs is: ",count)

"""MIT 6.001 EDX - Problem set 1  - problem 3"""
# lst = []
# wordlist=[]
# word = ""
# for a in string.ascii_lowercase:
#     lst.append(a)
# for i,j in enumerate(s[0:-1]):
#     # # print(lst.index(s[i+1]))
#     # print(lst.index(j))
#     # print(s[i+1])
#     if lst.index(s[i])<=lst.index(s[i+1]):
#         if len(word) == 0:
#             word = s[i] + s[i+1]
#             wordlist.append(word)
#         elif len(word) > 0:
#             word = word+s[i+1]
#             wordlist.append(word)                
#     else:
#         word=""
# if len(wordlist)<1:
#     wordlist.append(s[0])
# # wordlist = ['az', 'bo', 'bo', 'be', 'beg', 'begg', 'beggh', 'ak', 'akl']
# # print(max(wordlist,key=len))
# count=0           
# for each in wordlist:
#     if len(each)>count:
#         count = len(each)
#         word=each
# print(word)


"""MIT 6.001 EDX - Problem set 3  - problem 1"""
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    lst = []
    for letters in secretWord:
        if letters in lettersGuessed:
            lst.append(True)
        else:
            lst.append(False)
    return False not in lst


# print(isWordGuessed('areaswe', ['a', 'e', 'i', 'k', 'p', 'r', 's']))


def is_prime(number):
    if number <= 1:
        return False
    for factor in range(2, int(number/2)):
        if number % factor == 0:
            return False

        
    return True
# print(is_prime(4))


