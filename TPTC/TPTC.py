""" Tic Tac Toe """

class TPTC():
    
    # ConStructor
    def __init__(self):
        self.currentPlayer = "X"
        self.table = [[" " for x in range(3)] for y in range(3)]

    # Methods
    def add(self, x, y):
        if self.table[x][y] != " ":
            return 0 # Error
        else:
            self.table[x][y] = self.currentPlayer
            if self.currentPlayer == "X":
                self.currentPlayer = "O"
            else:
                self.currentPlayer = "X"
            return 1
                
    def display(self):
        print(" ___________")
        for i in enumerate(self.table):
            print("| ", end="")
            for j in enumerate(self.table[i[0]]):
                print(j[1], "| ", end="")
            print("\n ___________")
        print("\n* * * * * * * * * *\n")
    
monTPTC = TPTC()
player = 'P2';
ordon = absci = 0

while 1:
    """ Game loop """

    monTPTC.display()
    
    """if there is a winner - TO IMPROVE by analyzing only cases where
    the last input is concerned"""
    if (
    ((monTPTC.table[0][0] != " ")
    and (monTPTC.table[0][0] == monTPTC.table[0][1])
    and (monTPTC.table[0][0] == monTPTC.table[0][2]))
    or
    ((monTPTC.table[1][0] != " ")
    and (monTPTC.table[1][0] == monTPTC.table[1][1])
    and (monTPTC.table[1][0] == monTPTC.table[1][2]))
    or
    ((monTPTC.table[2][0] != " ")
    and (monTPTC.table[2][0] == monTPTC.table[2][1])
    and (monTPTC.table[2][0] == monTPTC.table[2][2]))
    
    or
    
    ((monTPTC.table[0][0] != " ")
    and (monTPTC.table[0][0] == monTPTC.table[1][0])
    and (monTPTC.table[0][0] == monTPTC.table[2][0]))
    or
    ((monTPTC.table[0][1] != " ")
    and (monTPTC.table[0][1] == monTPTC.table[1][1])
    and (monTPTC.table[0][1] == monTPTC.table[2][1]))
    or
    ((monTPTC.table[0][2] != " ")
    and (monTPTC.table[0][2] == monTPTC.table[1][2])
    and (monTPTC.table[0][2] == monTPTC.table[2][2]))
    
    or
    
    ((monTPTC.table[0][0] != " ")
    and (monTPTC.table[0][0] == monTPTC.table[1][1])
    and (monTPTC.table[0][0] == monTPTC.table[2][2]))
    or
    ((monTPTC.table[0][2] != " ")
    and (monTPTC.table[0][2] == monTPTC.table[1][1])
    and (monTPTC.table[0][2] == monTPTC.table[2][0])) ):
        print("{0} wins. End of the game.".format(player))
        break
    
    """ Player change """
    if player[len(player)-1] == '1':
        player = "P2"
    elif player[len(player)-1] == '2':
        player = "P1"
    print("{0}'s turn.".format(player))
    
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
        
        if not monTPTC.add(ordon, absci):
            print("Already used. Play somewhere else")
            continue
        else:
            break