'''
Created on Dec 11th 2016

@author: ttoussaint
'''

import tic_tac_toe

# Initialization
myTTT = tic_tac_toe.TicTacToe()
print("Welcome to my Tic Tac Toe game.\n\n")

while 1:
    pvp = input("How many players will play ? (1 or 2) ")
    if ((pvp != "1") and (pvp != "2")):
        print("\nPlease, write \"1\" or \"2\" exactly.")
        continue
    else:
        try:
            pvp =int(pvp)-1 # 'pvp' will be True in case of 2 players
            break
        except TypeError:
            print("\nPlease, write \"1\" or \"2\" exactly.")

player = "AI";
ordon = absci = -1

# Game loop
while 1:

    myTTT.display()
    
    # Potential end of he game
    if myTTT.there_is_a_winner():
        print("{0} ({1}) wins. End of the game.".format(player, myTTT.currentPlayer))
        break
    if myTTT.is_full():
        print("There is no winner, it's a tie. End of the game.")
        break
    
    # Player change
    if (player == "P2") or (player == "AI"):
        player = "P1"
    elif pvp:
        player = "P2"
    else:
        player = "AI"
    if myTTT.currentPlayer == "X":
        myTTT.currentPlayer = "O"
    else:
        myTTT.currentPlayer = "X"
    print("{0}'s ({1}) turn.".format(player, myTTT.currentPlayer))
    
    # Turn loop
    if player == "AI":
        myTTT.ai_turn()
    else:
        while 1:
            try:
                ordon = int(input("{0}, Please enter the ordinate of where you\nwant to play : ".format(player)))-1
                absci = int(input("And the abscissa : "))-1
            except ValueError:
                print("The coordinates must be integer numbers.")
                continue
            
            if (0 <= ordon) and (ordon <= 2) and (0 <= absci) and (absci <= 2):
                pass
            else:
                print("The coordinates must be between 1 and 3.")
                continue
            
            if not myTTT.add(ordon, absci):
                print("Already used. Play somewhere else")
                continue
            else:
                break