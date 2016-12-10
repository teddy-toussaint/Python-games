'''
Created on 20 juin 2016

@author: ttoussaint
'''
import data
import functions
''' This file contains the hangman game itself '''

print("Welcome to my hangman game !")
player = input("What's your name ? ")

# Checking score with 'scores' file
print("Your score is {0}.".format(functions.checkScore(player)))

print("This time, you'll have {0} chances to find each word, since each of them is maximum {0} letter long.\n".format(data.numChances))

functions.hangman(player, data.words, data.numChances)