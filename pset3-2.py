# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 12:53:41 2017

@author: furrukh
"""

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

#for the test if lettersguessed was empty
if (len(lettersGuessed) == 0):
    clone = []
    for i in range(len(secretWord)):
        clone.append("_")
        
    string = " ".join(clone)
    print(string)
    
else:

    wordaslist = list(secretWord)

    #cloning the above list so that original copy be kept
    clone = wordaslist[:]

    # index to keep track of position of char in wordaslist so that it
    # can be referenced back to clone later on
    index = 0

    for eachchar in wordaslist:
        for char in lettersGuessed:
            if (eachchar == char):
            
                # if the char from wordaslist matches from guessed list 
                #than replace the element in clone at that index with that
                #char and break the loop so that it doesnot changes back
                # to '_'
                clone[index] = eachchar
                break
                
            else:
                # replace that char from clone with _
                clone[index] = "_"
                
    
     
        index = index + 1       

    #to ouput string as it is desired with _ and guessed alphabets
    string = " ".join(clone)
    print(string)           