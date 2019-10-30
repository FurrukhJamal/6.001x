# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:07:08 2017

@author: furrukh
"""

secretword = "apple"
lettersguessed = ['e', 'i', 'k', 'p', 'r', 's', 'a', 'l']

#lenght of secret word
length = len(secretword)

#counter to use as a flag that will determine if the word
# is indeed in the guessed word

count = 0

for eachchar in secretword:
    for chars in lettersguessed:
        # comparing each char with that of in lettersguessed
        if (eachchar == chars):
            count += 1
            break
            

#checking if numbers of matched chars equal to length of secretword
if (count == length):
    print("True")
else:
    print("not guessed")