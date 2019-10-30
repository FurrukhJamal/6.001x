# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:12:06 2017

@author: furrukh
"""

hand = {'h': 1, 'e' : 1, 'l' : 3, 'o' : 1, 'z' : 2}
wordList = ["hello", "zebra", "coin"]
word = "hello"

#creating copy of hand
copyofhand = hand.copy()

# creating a dictionar like that of hand for word
listforword = {}

for char in word:
    listforword[char] = listforword.get(char, 0) + 1

#number of different alphabets in word so that it cud b used to test
# by the count flag that all alphabets in word matched the test
wordnum = len(listforword)

print("hand as list", copyofhand)
print("word as list",listforword, "length", wordnum)

#flag to check if word can be formed with available letters in word
flagforword = False

#to track the number of true tests that should be equal to lenght of word
count = 0

if (word in wordList):
    for char in copyofhand.keys():
        for letter in listforword.keys():
            print(char , letter)
            if (letter == char):
                print (copyofhand[char])
                if (copyofhand[char] - listforword[letter] >= 0):
                    # that means word can not be formed
                    flagforword = True
                    count += 1
                    break
        
            
                    
    if (flagforword == True and count == wordnum):
        print("Success")
    else:
        print("Failed")
else:
    print("word not in the list")
    
    
