# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:28:45 2017

@author: furrukh
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#ub0 = balance - (balance * monthlyPaymentRate)

for i in range(12):
    ub0 = balance - (balance * monthlyPaymentRate)
    balance = ub0 + ub0 * (annualInterestRate/12)

    #balance = round(balance , 2)
    #print(balance)

balance = round(balance , 2)

print("Balance Remaining = ", balance)