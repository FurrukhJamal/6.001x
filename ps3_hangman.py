# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "E:/Python/6.00.1x/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    #lenght of secret word
    length = len(secretWord)

    #counter to use as a flag that will determine if the word
    # is indeed in the guessed word

    count = 0

    for eachchar in secretWord:
        for chars in lettersGuessed:
            # comparing each char with that of in lettersguessed
            if (eachchar == chars):
                count += 1
                break
            

    #checking if numbers of matched chars equal to length of secretword
    if (count == length):
        return True
    else:
        return False




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    #for the test if lettersguessed was empty
    if (len(lettersGuessed) == 0):
        clone = []
        for i in range(len(secretWord)):
            clone.append("_")
        
        string = " ".join(clone)
        return string
    
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
        return string           



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string

    alphalist = list(string.ascii_lowercase)

    for char in lettersGuessed:
        for alpha in alphalist:
            if (alpha == char):
                alphalist.remove(alpha)
            
    string = "".join(alphalist)
    return string
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    def correctness(secretWord, guess):
        """
        secretWord: the secret word to guess
        guess: The users guess
        Returns true if the guess alphabet is in the secret word 
        otherwise false
        """
        for i in secretWord:
            if (guess == i):
                return True
            #else:
        return False
    
    
    
    guesslist = []
    
    
    print("Welcome to the game, Hangman!")
    
    countforword = len(secretWord)
    print("I am thinking of a word that is " + str(countforword)\
          + " letters long")
    
    # to track number of turns left
    guessnum = 8
    
    flagforlossing = False
    
    while(isWordGuessed(secretWord, guesslist) != True):
        print("-----------")
        print("You have "+ str(guessnum) + " guesses left.")
        print("Available letters: ",getAvailableLetters(guesslist) )
        guess = input("Please guess a letter: ")
    
        guess = guess.lower()
        
        # To check if letter already checked
        if guess in guesslist:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, guesslist) )
            continue
        
        # adding to the list the entered letter
        guesslist.append(guess)
        
        
        if (correctness(secretWord, guess) == True):
            print("Good guess: ",getGuessedWord(secretWord, guesslist) )
       
        else:
            print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, guesslist))
            guessnum -= 1
            
        #to see if player ran out of guesses
        if (guessnum == 0):
            flagforlossing = True
            break
    
    #checking if the player won or lost
    if (flagforlossing == True):
        print("-----------")
        print("Sorry, you ran out of guesses. The word was " + str(secretWord))
    else:
        print("-----------")
        print("Congratulations, you won!")
    
        
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
# for test use secretWord = "apple"
hangman(secretWord)
