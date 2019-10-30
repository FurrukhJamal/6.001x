# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 12:09:51 2017

@author: furrukh
"""

s = "azcbobobegghakl"
count = 0
for eachchar in s:
    if (eachchar == "a" or eachchar == "e" or eachchar == "i" or eachchar == "o" or eachchar == "u"):
        count += 1
        
print("Number of Vowels : " +  str(count))