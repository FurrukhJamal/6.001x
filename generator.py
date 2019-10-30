# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:53:05 2017

@author: furrukh
"""

for n in range(2, 10):
    print ("n is", n)
    for x in range(2, n):
         print("x is", x)
         if n % x == 0:
            print (n, 'equals', x, '*', n/x)
            break
    else:
          print (n, 'is a prime number')