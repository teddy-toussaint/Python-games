'''
Created on June 20th 2016

@author: ttoussaint

This file contains all the functions of the program
'''

import pickle
import random

def checkScore(player):
    try:
        file = open("scores", "r")
    except FileNotFoundError:
        file = open("scores", "w")
        file = open("scores", "r")
    
    # The file didn't exist
    if file.read() == "":
        scores = {player: 0}        
        with open("scores", "wb") as file:
            myPickler = pickle.Pickler(file)    
            myPickler.dump(scores)
    
    # The file existed already => the 'scores' object too
    else:
        file = open("scores", "rb")
        myUnpickler = pickle.Unpickler(file)
        scores = myUnpickler.load()
        
        # The player does not exist yet
        if player not in scores:            
            scores[player] = 0
            with open("scores", "wb") as file:
                myPickler = pickle.Pickler(file)
                myPickler.dump(scores)
    
    return scores[player]

def pickRandWord(aList):
    rdm = random.randrange(len(aList))
    return aList[rdm]

def updateScore(player, score):
    file = open("scores", "rb")
    myUnpickler = pickle.Unpickler(file)
    scores = myUnpickler.load()
    
    # Update
    scores[player] += score
    with open("scores", "wb") as file:
        myPickler = pickle.Pickler(file)
        myPickler.dump(scores)
        

def askEndOfGame():
    while 1:
        yn = input("Do you want to continue to play (Y/N) ? ")
        if yn.lower() != "y" and yn.lower() != "n":
            print("Please type 'Y' or 'N'.\n")
            continue
        else:
            break
        
    if yn.lower() == "y":
        return 0
    else:
        print("End of game. Thanks for playing !")
        return 1
    
def hangman(player, words, chances):
    dataChances = chances;
    usedLetters = []
    gameWords = []
    for w in words:
        gameWords.append(w)
    # Game loop starts
    while 1:
        print("Here's a new word. Try to guess the letters composing it :")
        word = pickRandWord(gameWords)
        alreadyGiven = 1
        score = 0
        # Word loop starts
        while chances:
            for j in word:
                if j in usedLetters:
                    print("{}".format(j), end="")
                else:
                    print("*", end="")
            print()
            while alreadyGiven:
                a = input("Type a letter : ")
                if a in usedLetters:
                    print("You've already given this letter.")
                elif (len(a) > 1) or not (a.isalpha()):
                    print("Please type a letter.")
                else:
                    alreadyGiven = 0
            alreadyGiven = 1
            usedLetters.append(a)
            if a in word:
                print("Congrats, you chose a good letter.")
                count = 0
                for j in word:
                    if j not in usedLetters:
                        count += 1 #counts the non-found letters
                if count == 0:
                    break
            else:
                print("Too bad, you chose a wrong letter.")
                chances -= 1
            
            if chances:
                score = chances
                print("You have {0} chances left.".format(score))
            else:
                print("You have used all your {0} chances.".format(chances))
                
            print()
        
        # Potential end of game loop
        for i in word:
            if i not in usedLetters:
                print("You didn't manage to find the word... It was '{0}'.".format(word))
                print("Your score is still {0}.".format(checkScore(player)))
                break
            else:
                if i == word[len(word)-1]:
                    print("Well done ! You found the word '{0}', and won {1} points.".format(word, score))
                    updateScore(player, score)
                    print("Your score is now {0}.".format(checkScore(player)))
        
        # Reinitialization
        chances = dataChances
        usedLetters = []
        
        if askEndOfGame():
            break
        else:  
            gameWords.remove(word)
            print()
            continue