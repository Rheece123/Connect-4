class GameBoard:

    # This class is responsible for the controlling all of the gameboard parameters
    # within the game and is responsible for checking when a player has won

    # Attributes:
        # make_move: Allows the row and column values to be inserted onto the grid
        # check_winner: Uses two functions to check winner vertically and horizontally
        # is_board_full: Ends the game if all rows and columns in gameboard is full
        # is_space_free: Prevents players from putting symbol in row/column already occupied
        # show_board_dynamic: Responsible for printing the board


    def __init__(self, r, c):
        # Grid is created as a 2D list and self.__board is the outer list while the
        # inner lists are created using the for loop below
        self.__space = " "
        self.__rows = r
        self.__cols = c
        self.__board = []

        
        # This iterates through the 2D list 6 times to create the board
        # 6 is used for the number of columns
        for i in range (self.__rows):
            row = [" "] * self.__cols
            self.__board.append(row)
            

    def make_move(self, row, col, element):
        # Takes row and column values from players and uses these values to insert
        # player symbol onto the game grid
        self.__board[row][col] = element
        

    def check_winner(self):
        # check_vt checks for player symbol vertically and check_hz checks for player
        # symbol horizontal. If 4 player symbols are in a row, winner is returned
        winner =(self.check_hz() or self.check_vt() or

        # Below checks for diagonal. The first number is X and the second one is Y within self.__board

        # Check across the top row [0]
        (self.__board[0][0] == self.__board[1][1] and self.__board[1][1] == self.__board[2][2] and self.__board[2][2] == self.__board[3][3] != self.__space) or
        (self.__board[0][1] == self.__board[1][2] and self.__board[1][2] == self.__board[2][3] and self.__board[2][3] == self.__board[3][4] != self.__space) or
        (self.__board[0][2] == self.__board[1][3] and self.__board[1][3] == self.__board[2][4] and self.__board[2][4] == self.__board[3][5] != self.__space) or
        (self.__board[0][3] == self.__board[1][4] and self.__board[1][4] == self.__board[2][5] and self.__board[2][5] == self.__board[3][6] != self.__space) or

        # Check across the second row [1]
        (self.__board[1][0] == self.__board[2][1] and self.__board[2][1] == self.__board[3][2] and self.__board[3][2] == self.__board[4][3] != self.__space) or        
        (self.__board[1][1] == self.__board[2][2] and self.__board[2][2] == self.__board[3][3] and self.__board[3][3] == self.__board[4][4] != self.__space) or
        (self.__board[1][2] == self.__board[2][3] and self.__board[2][3] == self.__board[3][4] and self.__board[3][4] == self.__board[4][5] != self.__space) or
        (self.__board[1][3] == self.__board[2][4] and self.__board[2][4] == self.__board[3][5] and self.__board[3][5] == self.__board[4][6] != self.__space) or
          
        # Check across the thrid row [2]
        (self.__board[2][0] == self.__board[3][1] and self.__board[3][1] == self.__board[4][2] and self.__board[4][2] == self.__board[5][3] != self.__space) or
        (self.__board[2][1] == self.__board[3][2] and self.__board[3][2] == self.__board[4][3] and self.__board[4][3] == self.__board[5][4] != self.__space) or
        (self.__board[2][2] == self.__board[3][3] and self.__board[3][3] == self.__board[4][4] and self.__board[4][4] == self.__board[5][5] != self.__space) or
        (self.__board[2][3] == self.__board[3][4] and self.__board[3][4] == self.__board[4][5] and self.__board[4][5] == self.__board[5][6] != self.__space) or

        # Checks across the fourth row [3]
        (self.__board[3][0] == self.__board[3][1] and self.__board[3][1] == self.__board[3][2] and self.__board[3][2] == self.__board[3][3] != self.__space) or
        (self.__board[3][1] == self.__board[3][2] and self.__board[3][2] == self.__board[3][3] and self.__board[3][3] == self.__board[3][4] != self.__space) or
        (self.__board[3][2] == self.__board[3][3] and self.__board[3][3] == self.__board[3][4] and self.__board[3][4] == self.__board[3][5] != self.__space) or
        (self.__board[3][3] == self.__board[3][4] and self.__board[2][4] == self.__board[3][5] and self.__board[3][5] == self.__board[3][6] != self.__space) or

        # Checks across the fourth row [4]
        (self.__board[4][0] == self.__board[3][1] and self.__board[3][1] == self.__board[2][2] and self.__board[2][2] == self.__board[1][3] != self.__space) or
        (self.__board[4][1] == self.__board[3][2] and self.__board[3][2] == self.__board[2][3] and self.__board[2][3] == self.__board[1][4] != self.__space) or
        (self.__board[4][2] == self.__board[3][3] and self.__board[3][3] == self.__board[2][4] and self.__board[2][4] == self.__board[1][5] != self.__space) or
        (self.__board[4][3] == self.__board[3][4] and self.__board[3][4] == self.__board[2][5] and self.__board[2][5] == self.__board[1][6] != self.__space) or

        # Checks across the bottom row [5]
        (self.__board[5][0] == self.__board[4][1] and self.__board[4][1] == self.__board[3][2] and self.__board[3][2] == self.__board[2][3] != self.__space) or
        (self.__board[5][1] == self.__board[4][2] and self.__board[4][2] == self.__board[3][3] and self.__board[3][3] == self.__board[2][4] != self.__space) or
        (self.__board[5][2] == self.__board[4][3] and self.__board[4][3] == self.__board[3][4] and self.__board[3][4] == self.__board[2][5] != self.__space) or
        (self.__board[5][3] == self.__board[4][4] and self.__board[4][4] == self.__board[3][5] and self.__board[3][5] == self.__board[2][6] != self.__space))
        
        return winner
    
                 
    def check_hz(self):
        # At each iteration the outer for-loop increments x by 1, then the inner for-loop
        # will iterate 6 times while incrementing the value y by 1, which allows access to
        # all columns inside each row
        row = ""
        for x in range(6):
            for y in range(7):
                row += self.__board[x][y]

            # If winning combination is found, return winner == True
            # else return false and carry on checking for a winner
            if "RRRR" in row or "YYYY" in row:
                return True

            row = ""
        return False


    def check_vt(self):
        # At each iteration the outer for-loop increments y by 1, then the inner for-loop
        # will iterate 7 times while incrementing the value x by 1, which allows access to
        # all rows inside each column
        col = ""
        for y in range(7):
            for x in range(6):
                col += self.__board[x][y]
                
            # If winning combination is found, return winner == True
            # else return false and carry on checking for a winner
            if "RRRR" in col or "YYYY" in col:
                return True

            col = ""
        return False

    def is_board_full(self):
        # Checks each row and column to see if it is filled with a player symbol, if it is
        # True is returned else False is returned and the row is empty
        row = ""
        for x in range(6):
            for y in range(7):
                row += self.__board[x][y]

            if " " in row:
                return False
            row = ""
        return True
    
        
    def is_space_free(self, row, col):
        # if statement checks if the value inside the cell with the given index row and col is empty.
        # If True, then the cell is free for the player to place their symbol, otherwise the cell is
        # not usable and the player should try to place their symbol somewhere else inside the gird
        if self.__board[row][col] == " ":
            return True
        
        return False
    

    def show_board_dynamic(self):
        # This prints the board each time a player places their symbol on the grid
        print()
        print("---------------")
        for i in range(len(self.__board)):
            for j in range(self.__cols):
                print ("|", end = "")
                print (self.__board[i][j], end=""),
            print ("|")
            print("---------------")
        print()
        
