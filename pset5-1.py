# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 10:39:04 2017

@author: furrukh
"""

import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

#changing string into a list
lowercase = list(lowercase)
uppercase = list(uppercase)

#print(lowercase)

shift = 3

# converting the lowercase list into a new encrypted one
encryptlowercase = []
encryptuppercase = []

for i in range(0, len(lowercase)):
    #print(lowercase[(i + shift) % 26])
    encryptlowercase.append(lowercase[(i + shift) % 26])
    encryptuppercase.append(uppercase[(i + shift) % 26])
    
#print(encryptlowercase)
#joining all the uppercase and lowercase into a single list
fulllowercase = lowercase + uppercase

#joining all encrypted into a single list
fullencrypted = encryptlowercase + encryptuppercase

outputdict = {}

#adding the 2 dictionaries as key value in dictionary
for i in range(len(fulllowercase)):
    outputdict[fulllowercase[i]] = fullencrypted[i]
    
print (outputdict)

message = "hello World!"

message = list(message)

encryptedlist = []

#if a character from message is found as key in dict, add its value
# to encrptedlist else add the character as it is
for char in message:
    if (char in outputdict):
        encryptedlist.append(outputdict[char])
    else:
        encryptedlist.append(char)
        
print(encryptedlist)
encryptedmessage = "".join(encryptedlist)
print(encryptedmessage)
    
    
    
    