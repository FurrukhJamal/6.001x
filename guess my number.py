# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 10:36:24 2017

@author: furrukh
"""

high = 100
low = 0

print("Please think of a number between 0 and 100!")

guess = (high + low)//2


answer = ""
while (answer != "c"):
    print("Is your secret number", guess, "?")
    #print("Enter 'h' to indicate the guess is too high.", end = " ")
    #print("Enter 'l' to indicate the guess is too low.", end = " ")
    #print("Enter 'c' to indicate I guessed correctly.")
    
    answer = input("Enter 'h' to indicate the guess is too high."\
                   + " Enter 'l' to indicate the guess is too low."\
                   + " Enter 'c' to indicate I guessed correctly. ")
    
    while (answer != "c" and answer != "h" and answer != "l"):
        print("Sorry, I did not understand your input.")
        print("Is your secret number", guess, "?")
        #print("Enter 'h' to indicate the guess is too high.", end = " ")
        #print("Enter 'l' to indicate the guess is too low.", end = " ")
        #print("Enter 'c' to indicate I guessed correctly.")
    
        answer = input("Enter 'h' to indicate the guess is too high."\
                   + " Enter 'l' to indicate the guess is too low."\
                   + " Enter 'c' to indicate I guessed correctly. ")
        
    if (answer == "h"):
         
        high = guess
        guess = (high + low)//2
        
    elif (answer == "l"):
        
        low = guess
        guess = (high + low)//2
        
print("Game over. Your secret number was: ", guess)        