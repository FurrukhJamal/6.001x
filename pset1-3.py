# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 18:42:21 2017

@author: furrukh
"""

s = "azcbobobegghakl"

current_substring = ""
max_substring = ""

for i in range(len(s) - 1):
    
    # checking if ith alphabet is lesser than the next alphabet
    if (s[i] <= s[i + 1] ):
        current_substring += s[i]
        
    else:
        current_substring += s[i]
        
        #checking if this current substring is longest than the current max string
        if (len(current_substring) > len(max_substring)):
            max_substring = current_substring
        current_substring = ""
            
if(len(max_substring) < len(current_substring)):
    max_substring = current_substring + s[len(s) - 1]

print("Longest substring in alphabetical order is: " + max_substring)            
        
            