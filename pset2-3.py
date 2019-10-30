# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 13:31:47 2017

@author: furrukh
"""

balance = 999999
annualInterestRate = 0.18

# incase of floats we dont compare it to 0 instead we imagine a small value
epsilon = 0.01
monthlyinterest = annualInterestRate/12.0

lowerbound = balance/12
upperbound = (balance * (1 + monthlyinterest)**12) / 12.0

guess = (lowerbound + upperbound)/2

while True:

    balanceforloop = balance
    
    for i in range(12):
        ub0 = balanceforloop - guess
        balanceforloop = ub0 + ub0 * (annualInterestRate/12)


    #balance = round(balance , 2)
    
    #check if debt been paid at the end of yr if not increase x by 10
    if(upperbound - lowerbound < epsilon):
        break
    elif(balanceforloop > 0):
        lowerbound = guess
        guess = (lowerbound + upperbound)/2
    elif(balanceforloop < 0):
        upperbound = guess
        guess = (lowerbound + upperbound)/2
        
        
        

guess = round(guess, 2)
print("Lowest Payment = ", guess)