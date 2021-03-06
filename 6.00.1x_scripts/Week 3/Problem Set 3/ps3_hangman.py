# 
# Hangman game
#
# Here are the requirements for your game:
#
# The computer must select a word at random from the list of available words that was provided in words.txt.
# The functions for loading the word list and selecting a random word have already been provided for you in ps3_hangman.py.
#
# The game must be interactive; the flow of the game should go as follows:
#
# At the start of the game, let the user know how many letters the computer's word contains.
# Ask the user to supply one guess (i.e. letter) per round.
# The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.
# After each round, you should also display to the user the partially guessed word so far, as well as letters that the user has not yet guessed.
#
# Some additional rules of the game:
#
# A user is allowed 8 guesses. Make sure to remind the user of how many guesses s/he has left after each round.
# Assume that players will only ever submit one character at a time (A-Z).
# A user loses a guess only when s/he guesses incorrectly.
# If the user guesses the same letter twice, do not take away a guess - instead,
# print a message letting them know they've already guessed that letter and ask them to try again.
#
# The game should end when the user constructs the full word or runs out of guesses.
# If the player runs out of guesses (s/he "loses"), reveal the word to the user when the game ends.

import random
import string

# Path to the list of words for the game
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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if secretWord[0] in lettersGuessed:
        if len(secretWord) == 1:
            return True
        else:
            return isWordGuessed(secretWord[1:], lettersGuessed)
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if secretWord[0] in lettersGuessed:
        if len(secretWord) == 1:
            return secretWord[0]
        else:
            return secretWord[0] + getGuessedWord(secretWord[1:], lettersGuessed)
    else:
        if len(secretWord) == 1:
            return "_ "
        else:
            return "_ " + getGuessedWord(secretWord[1:], lettersGuessed)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    result = ""
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            result += letter
    return result
    
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
    guessesLeft = 8
    lettersGuessed = []
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %s letters long." % len( secretWord )
    print "-------------"
    while guessesLeft > 0:
        print "You have %s guesses left." % guessesLeft
        print "Available letters: %s" % getAvailableLetters( lettersGuessed )
        guess = raw_input("Please guess a letter: ")
        guess = guess.lower()
        if guess in lettersGuessed:
            print "Oops! You've already guessed that letter: %s" % getGuessedWord ( secretWord , lettersGuessed )
        else:
            lettersGuessed.append( guess )
            if guess in secretWord:
                print "Good guess: %s" % getGuessedWord ( secretWord , lettersGuessed )
            else:
                guessesLeft -= 1
                print "Oops! That letter is not in my word: %s" % getGuessedWord ( secretWord , lettersGuessed )
        print "------------"
        if isWordGuessed ( secretWord , lettersGuessed ):
            print "Congratulations, you won!"
            break
    if guessesLeft == 0:
        print "Sorry, you ran out of guesses. The word was %s," % secretWord

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
