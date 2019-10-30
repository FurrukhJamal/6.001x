# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:52:40 2017

@author: furrukh
"""
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()  



hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
displayHand(hand)

word = "quail"  

copyofhand = hand.copy()

#print (copyofhand)  

#dictionary for count of alphabets in word
wordcount = {}

for char in word:
    wordcount[char] = wordcount.get(char, 0) + 1

# updating the value of keys in copyofhand/ cuz of python error
# had to linear search instead of refrencing the same key to both
# dictionaries
for char in copyofhand.keys():
    for i in wordcount.keys():
        if (i == char):
            
            copyofhand[char] = int(copyofhand[char]) - int(wordcount[i])
            break

displayHand(copyofhand)        