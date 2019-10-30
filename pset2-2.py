# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 12:33:51 2017

@author: furrukh
"""

balance = 3926
annualInterestRate = 0.2


# let x be the minimum amount to be paid in order to pay off debt
x = 10
while True:

    balanceforloop = balance
    
    for i in range(12):
        ub0 = balanceforloop - x
        balanceforloop = ub0 + ub0 * (annualInterestRate/12)


    #balance = round(balance , 2)
    
    #check if debt been paid at the end of yr if not increase x by 10
    if(balanceforloop <= 0):
        break
    else:
        x = x + 10

print("Lowest Payment = ", x)