# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    # FILL IN YOUR CODE HERE...
    return all(map(lambda c: c in lettersGuessed, secretWord))



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guess = {}
    for i in range(len(secretWord)):
      if secretWord[i] in lettersGuessed:
        guess[i] = secretWord[i]
      else:
        guess[i] = "_"
    return "".join(guess.values())



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    baseString = string.ascii_lowercase
    for char in lettersGuessed:
      baseString.replace(char, "")
    return baseString


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
    # FILL IN YOUR CODE HERE...
    def printLine():
      print('-------------')

    guessTimes = 8
    letterCount = len(secretWord)
    lettersGuessed = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(letterCount) + ' letters long.')
    printLine()
    while guessTimes > 0:
      print('You have ' + str(guessTimes) + ' guesses left.')
      print('Available Letters: ' + getAvailableLetters(lettersGuessed))
      guess = raw_input('Please guess a letter: ').lower()
      informString = 'Good guess: '
      if guess in lettersGuessed:
        informString = "Oops! You've already guessed that letter: "
        print(informString + getGuessedWord(secretWord, lettersGuessed))
        printLine()
        continue
      elif guess not in secretWord:
        informString = 'Oops! That letter is not in my word: '
        guessTimes -= 1

      lettersGuessed.append(guess)
      print(informString + getGuessedWord(secretWord, lettersGuessed))
      printLine()
      if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, you won!')
        return

    print('Sorry, you ran out of guesses. The word was else. ')






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
