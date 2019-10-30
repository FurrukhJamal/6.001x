# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 13:07:31 2017

@author: furrukh
"""

s = "nbooboboobobbbotr"

#counter to know what position char is been read
count = 0

vowels = 0

# going through each alphabets one at a time
for chars in s:
    
    # if a char is b then check the next 2 chars are "ob" or not and check word does not end
    if (chars == "b" and (count + 1 <= len(s) - 1 and count + 2 <= len(s) - 1)):
        if (s[count + 1] == "o" and s[count + 2] == "b"):
            
            
            
            # add the number of vowels
            vowels += 1
    
    # incrementting the counter
    count = count + 1        

print("Number of times bob occur is : " + str(vowels))            