'''
Created on June 20th 2016

@author: ttoussaint

This file contains the hangman game itself
'''

import data
import functions

print("Welcome to my hangman game !")
player = input("What's your name ? ")

# Checking score with 'scores' file
print("Your score is {0}.".format(functions.checkScore(player)))

print("This time, you'll have {0} chances to find each word, since each of them contains maximum {0} different letters.\n".format(data.numChances))

functions.hangman(player, data.words, data.numChances)