# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:24:32 2017

@author: furrukh
"""

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

n = 7

word = "waybill"

length = len(word)

wordsum = 0

# getting each alphabet in word and getting its subsequent score from
# dictionary
for char in word:
    wordsum = wordsum + SCRABBLE_LETTER_VALUES[str(char)]
    
score = 0
if (length == n):
    score = wordsum * length + 50
else:
    score = wordsum * length
    
print (score)
    
    

