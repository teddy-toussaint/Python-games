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

while 1:
    """ Game loop """

    monTPTC.display()
    
    """if endOfGame"""
    
    """ Player change """
    if player[len(player)-1] == '1':
        player = "P2"
    else:
        player = "P1"
    
    print("{0}'s turn.".format(player))
    if player[0] == 'P':
        while 1:
            try:
                ordon = int(input("{0}, Please enter the ordinate of where you\nwant to play : ".format(player)))
                absci = int(input("And the abscissa : "))
            except ValueError:
                print("The coordinates must be integer numbers.")
                continue
            
            if (0 <= ordon) and (ordon <= 2) and (0 <= absci) and (absci <= 2):
                pass
            else:
                print("The coordinates must be between 0 and 2.")
                print("{0}, {1}".format(ordon, absci))
            
            if not monTPTC.add(ordon, absci):
                print("Already used. Play somewhere else")
                continue
            else:
                break
        
        
        