# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 16:07:14 2017

@author: furrukh
"""

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

import string

alphalist = list(string.ascii_lowercase)

for char in lettersGuessed:
    for alpha in alphalist:
        if (alpha == char):
            alphalist.remove(alpha)
            
string = "".join(alphalist)
print(string)
