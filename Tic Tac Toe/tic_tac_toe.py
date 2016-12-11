'''
Created on Dec 11th 2016

@author: ttoussaint
'''

class TicTacToe():
    
    # Constructor
    def __init__(self):
        self.currentPlayer = "X"
        self.table = [[" " for x in range(3)] for y in range(3)]

    # Adds a cross or a circle
    def add(self, x, y):
        if self.table[x][y] != " ":
            return 0 # Error, case already used
        else:
            self.table[x][y] = self.currentPlayer
            return 1
    
    # Displays the table
    def display(self):
        print(" ___________")
        for i in enumerate(self.table):
            print("| ", end="")
            for j in enumerate(self.table[i[0]]):
                print(j[1], "| ", end="")
            print("\n ___________")
        print("\n* * * * * * * *\n")
    
    # Checks if 3 given cases are filled with the same symbol    
    def are_filled_and_equal(self, case1, case2, case3):
        # 'casei' contains the coordinates of the i'th case to compare
        if self.table[case1[0]][case1[1]] != " ":
            if((self.table[case1[0]][case1[1]] == self.table[case2[0]][case2[1]]) and
               (self.table[case1[0]][case1[1]] == self.table[case3[0]][case3[1]])):
                return True
            else:
                return False
        else:
            return False
    # Checks if there is a winner    
    def there_is_a_winner(self):
        if (
        (self.are_filled_and_equal((0,0), (0,1), (0,2))) or
        (self.are_filled_and_equal((1,0), (1,1), (1,2))) or
        (self.are_filled_and_equal((2,0), (2,1), (2,2))) or
        (self.are_filled_and_equal((0,0), (1,0), (2,0))) or
        (self.are_filled_and_equal((0,1), (1,1), (2,1))) or
        (self.are_filled_and_equal((0,2), (1,2), (2,2))) or
        (self.are_filled_and_equal((0,0), (1,1), (2,2))) or
        (self.are_filled_and_equal((0,2), (1,1), (2,0))) ):
            return True
        else:
            return False
    # Checks if the table is full
    def is_full(self):
        res = True
        for y in range(3):
            for x in range(3):
                if self.table[y][x] != " ":
                    pass
                else:
                    res = False
                    break
        return res
    
    # AI plays
    def ai_turn(self):
        """ This will take some time... """