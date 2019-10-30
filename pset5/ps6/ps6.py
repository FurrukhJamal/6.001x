import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase

        #changing string into a list
        lowercase = list(lowercase)
        uppercase = list(uppercase)

        # converting the lowercase list into a new encrypted one
        encryptlowercase = []
        encryptuppercase = []

        for i in range(0, len(lowercase)):
            encryptlowercase.append(lowercase[(i + shift) % 26])
            encryptuppercase.append(uppercase[(i + shift) % 26])
    

        #joining all the uppercase and lowercase into a single list
        fulllowercase = lowercase + uppercase

        #joining all encrypted into a single list
        fullencrypted = encryptlowercase + encryptuppercase

        outputdict = {}

        #adding the 2 dictionaries as key value in dictionary
        for i in range(len(fulllowercase)):
            outputdict[fulllowercase[i]] = fullencrypted[i]
            
        return outputdict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # calling the getter method to get the message
        message = self.get_message_text()
        
        #calling the method to get the encrypted dict
        outputdict = self.build_shift_dict(shift)
        
        message = list(message)

        encryptedlist = []

        #if a character from message is found as key in dict, add its value
        # to encrptedlist else add the character as it is
        for char in message:
            if (char in outputdict):
                encryptedlist.append(outputdict[char])
            else:
                encryptedlist.append(char)
        
        #joining the list as a string
        encryptedmessage = "".join(encryptedlist)
        return encryptedmessage

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        #Message.__init__(self, text)
        
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self,self.shift)
        self.message_text_encrypted = Message.apply_shift(self,self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        copy = self.encrypting_dict.copy()
        return copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self,self.shift)
        self.message_text_encrypted = Message.apply_shift(self,self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        #Message.__init__(self, text)
        self.valid_words = load_words(WORDLIST_FILENAME)
       

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        maxwords = 0
        keyformaxwords = -1
        
        #converting text into list of words
        listofwords = self.message_text.split(" ")
        
        #to note down max correctwords in each shift value
        count = 0
        
        validwords = self.get_valid_words()
        
        for x in range(27):
            for word in listofwords:
                decryptedword = Message(word).apply_shift(26 - x)
                
                if (is_word(validwords, decryptedword)):
                    count += 1
#==============================================================================
#                 if decryptedword in validwords:
#                     count += 1
#==============================================================================
                    
                
                    
            # at the end checking the max number of correct words
            # and what key was used to decrypt that message
            if (count >= maxwords):
                maxwords = count
                keyformaxwords = 26 - x
                count = 0
            else:
                count = 0
                
        # now that we have the key, use it to make a list of decrypted words
        decryptedwords = []
        
        for word in listofwords:
            decryptedword = Message(word).apply_shift(keyformaxwords)
            decryptedwords.append(decryptedword)
            
        # making it a string 
        string = " ".join(decryptedwords)
        
        tupletoreturn = (keyformaxwords, string)
        
        return tupletoreturn

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())


def decrypt_story(storystring):
    sstring = storystring
    newchiper = CiphertextMessage(sstring)
    return newchiper.decrypt_message()
    

story = get_story_string()
print(decrypt_story(story))
