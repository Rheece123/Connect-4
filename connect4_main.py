import tkinter
import random
import time

from sys import exit
from tkinter import messagebox
from connect4_board import GameBoard
from connect4_player import Player 
from connect4_player import HumanPlayer
from connect4_player import ComputerPlayer

class GameGUI:

    # This class creates all of the GUI elements for the game. This has also replaced
    # the play function within the Player class as the GUI code is now responsilbe for placing
    # the player's symbol onto the game board

    # Attributes:
        # X_widget: This method creates the button which allows the human player to choose X as their symbol
        # choose_symbol_X: This function is used by the button within X_widget function
        # O_widget: This method creates the button which allows the human player to choose O as their symbol
        # choose_symbol_O: This function is used by the button within O_widget function
        # restart_btn: Creates the button which allows the game to be restarted
        # restart_game: Allows the game to be restarted as the main window is destroyed and the main() function is called
        # quit_btn: Allows the player to quit the game as the the main window is destroyed
        # clicked_btn: Replaces the play method within Player class and places the player symbols onto the board
        # intialise_dynamic: Creates the button within the 7x6 gameboard and places the symbol onto the gameboard 
       

    def __init__(self):

        self.mw = tkinter.Tk()

        # The size of self.mw 
        self.mw.geometry("1280x720")

        # The top frame holds the 6x7 grid where counters are dropped
        self.top_frame = tkinter.Frame(self.mw)
        self.top_frame.pack()

        # The bottom frame has the restart and quit buttons 
        self.bottom_frame = tkinter.Frame(self.mw)
        self.bottom_frame.pack()

        self.mw.title("Connect 4")

        # Iterates through the buttons 7 times to create a gameboard
        self.size = 7
        self.buttons_2d_list = []
        for i in range (self.size):
            self.row = [" "] * self.size
            self.buttons_2d_list.append(self.row)


        # Creates a gameboard with 6 rows and 7 columns
        self.gboard = GameBoard(6, 7)
        
        self.winner = False

        
        # This has been set to False so that the only button which appears at the start
        # of the game are the ones asking the player to pick a game mode
        self.symbol_choose = False
        

        # Below are all of the different game modes the player can select. These are all set
        # to false as no game mode has been chosen at the start of the game

        self.choose_game_mode = False

        self.Human_VS_Human_mode = False

        self.Computer_VS_Computer_mode = False

        self.Human_VS_Computer_mode = False


    def game_modes(self):
        # Creates all of the buttons which allow the player to choose a game mode

        # If no game mode has been chosen, create the 3 buttons
        if self.choose_game_mode == False:

            # Human vs Human mode button
            self.Human_VS_Human_button = tkinter.Button(self.bottom_frame, text = "Human VS Human", font = 20, command = self.Human_VS_Human, height = 10, width = 20)
            self.Human_VS_Human_button.pack(side = "top")

            # Computer vs Computer mode button
            self.Computer_VS_Computer_button = tkinter.Button(self.bottom_frame, text = "Computer VS Computer", font = 20, command = self.Computer_VS_Computer, height = 10, width = 20)
            self.Computer_VS_Computer_button.pack(side = "top")

            
            # Human vs Computer mode button
            self.Human_VS_Computer_button = tkinter.Button(self.bottom_frame, text = "Human VS Computer", font = 20, command = self.Human_VS_Computer, height = 10, width = 20)
            self.Human_VS_Computer_button.pack(side = "top")

            # The first message at the start of the game
            start_game_message = messagebox.showinfo("Game Info ", "Welcome to Connect 4" "\n\nPlease choose a game mode")


    def Human_VS_Human(self):
        # Command used for the Human_VS_Human_button

        # If the Human_VS_Human_button has been clicked on, a game mode has
        # been chosen
        self.choose_game_mode = True

        self.symbol_choose = False

        # If the Human_VS_Human_button has been clicked on, the game mode chosen
        # is Human against another Human  
        self.Human_VS_Human_mode = True


        # Once the game mode has been chosen, create the symbol buttons
        # and destroy the game mode buttons
        if self.choose_game_mode == True:

            self.Red_button()
            self.Yellow_button()

            self.Human_VS_Human_button.destroy()
            
            self.Computer_VS_Computer_button.destroy()
            
            self.Human_VS_Computer_button.destroy()

            # Once the player has chosen the game mode, this message tells them to
            # choose a coloured symbol
            chosen_mode_message = messagebox.showinfo("Game Info", "Please choose a coloured symbol for Human Player 1")


    def Computer_VS_Computer(self):
        # Command used for the Computer_VS_Computer_button

        # If the Computer_VS_Computer_button has been clicked on, a game mode has
        # been chosen
        self.choose_game_mode = True

        # If the Computer_VS_Computer_button has been clicked on, the game mode chosen
        # is Computer against another Computer player 
        self.Computer_VS_Computer_mode = True
        

        # Once the game mode has been chosen, create the symbol buttons
        # and destroy the game mode buttons
        if self.choose_game_mode == True:

            self.Red_button()
            self.Yellow_button()

            self.Computer_VS_Computer_button.destroy()

            self.Human_VS_Human_button.destroy()

            self.Human_VS_Computer_button.destroy()


            # Once the player has chosen the game mode, this message tells them to
            # choose a coloured symbol for Computer Player 1  
            chosen_mode_message = messagebox.showinfo("Game Info", "Please choose a coloured symbol for Computer Player 1")



    def Human_VS_Computer(self):
        # Command used for the Human_VS_Computer_button

        # If the Human_VS_Computer_button has been clicked on, a game mode has
        # been chosen
        self.choose_game_mode = True

        # If the Human_VS_Computer_button has been clicked on, the game mode chosen
        # is Human against a Computer player
        self.Human_VS_Computer_mode = True
        

        # Once the game mode has been chosen, create the symbol buttons
        # and destroy the game mode buttons
        if self.choose_game_mode == True:

            self.Red_button()
            self.Yellow_button()
    
            self.Human_VS_Computer_button.destroy()

            self.Computer_VS_Computer_button.destroy()

            self.Human_VS_Human_button.destroy()

            # Once the player has chosen the game mode, this message tells them to
            # choose a coloured symbol for Human Player 
            chosen_mode_message = messagebox.showinfo("Game Info", "Please choose a coloured symbol")
            
            
    def Red_button(self):
        # Creates the button which allows the player to choose Red as their symbol
  
        # The red button is called once the player has selected their game 
        
        self.choose_Red_button = tkinter.Button(self.bottom_frame, text = "Red", font = 20, command = self.choose_symbol_Red, height = 10, width = 20, fg = "Red")
        self.choose_Red_button.pack(side = "top")


    def choose_symbol_Red(self):
        # This is the method used by the Red button

        # allows the game to start once the player has chosen their symbol/colour
        self.symbol_choose = True

        # If the chosen game mode is Human against another human player and if the red
        # button is clicked on, Human Player 1 symbol = Red, Human Player 2 symbol = Yellow
        if self.Human_VS_Human_mode == True:

            hp1_symbol = ("R")
            hp2_symbol = "Y"

            p1 = HumanPlayer(hp1_symbol)
            p2 = HumanPlayer(hp2_symbol)

       # Place players 1 and 2 in the tuple for turn based game 
            self.players_lst = (p1, p2)
            self.current_player_index = 0

            # Message telling players which symbol they are
            chosen_symbol_message = messagebox.showinfo("Game Info", "Player 1 symbol is Red\n\nPlayer 2 symbol is Yellow")
        
        # testing purposes 
            print("Human player 1 symbol is", hp1_symbol)
            print("Human player 2 symbol is", hp2_symbol)

            

        # If the chosen game mode is Computer against another Computer player and if the red
        # button is clicked on, Human Computer Player 1 symbol = Red, Computer Player 2 symbol = Yellow
        if self.Computer_VS_Computer_mode == True:

            cp1_symbol = "R"
            cp2_symbol = "Y"

            p1 = ComputerPlayer(cp1_symbol)
            p2 = ComputerPlayer(cp2_symbol)

       # Place players 1 and 2 in the tuple for turn based game 
            self.players_lst = (p1, p2)
            self.current_player_index = 0

            chosen_symbol_message = messagebox.showinfo("Game Info", "Computer Player 1 symbol is Red\n\nComputer Player 2 symbol is Yellow")
        
        # testing purposes 
            print("Computer player 1 symbol is", cp1_symbol)
            print("Computer player 2 symbol is", cp2_symbol)



        # If the chosen game mode is Human against a Computer player and if the red
        # button is clicked on, Human Computer Player symbol = Red, Computer Player symbol = Yellow
        if self.Human_VS_Computer_mode == True:
        
            hp_symbol= "R"
            cp_symbol = "Y"

            p1 = HumanPlayer(hp_symbol)
            p2 = ComputerPlayer(cp_symbol)

       # Place players 1 and 2 in the tuple for turn based game 
            self.players_lst = (p1, p2)
            self.current_player_index = 0

            # Message telling players which symbol they are
            chosen_symbol_message = messagebox.showinfo("Game Info", "Your chosen symbol is Red\n\nThe computer symbol is Yellow")
        
        # testing purposes 
            print("The human player symbol is", hp_symbol)
            print("The computer player symbol is", cp_symbol)

        
        # executes all of the other functions needed within the game once the symbols have been
        # chosen for the current game
        if self.symbol_choose == True:

            # Buttons destroyed as not needed during the game
            self.choose_Red_button.destroy()
            self.choose_Yellow_button.destroy()

            # Grid is created
            self.intialise_dynamic()

            # Restart and quit buttons are created
            self.restart_btn()
            self.quit_btn()


    def Yellow_button(self):
        # Creates the button which allows the player to choose Yellow as their symbol

        # The yellow button is called once the player has selected their game 
         
        self.choose_Yellow_button = tkinter.Button(self.bottom_frame, text = "Yellow", font = 20, command = self.choose_symbol_Yellow, height = 10, width = 20, fg = "Yellow")
        self.choose_Yellow_button.pack(side = "top")
             

    def choose_symbol_Yellow(self):
        # This is the method used by the Yellow button. If the choose_Yellow_button is clicked
        # the human player symbol is Yellow, computer player symbol is Red

        # allows the game to start once the player has chosen their symbol/colour
        self.symbol_choose = True

        # If the chosen game mode is Human against another human player and if the yellow
        # button is clicked on, Human Player 1 symbol = Yellow, Human Player 2 symbol = Red
        if self.Human_VS_Human_mode == True:

           hp1_symbol = "Y"
           hp2_symbol = "R"

           p1 = HumanPlayer(hp1_symbol)
           p2 = HumanPlayer(hp2_symbol)

           # Place players 1 and 2 in the tuple for turn based game
           self.players_lst = (p1, p2)
           self.current_player_index = 0

           # Message telling players which symbol they are
           chosen_symbol_message = messagebox.showinfo("Game Info", "Player 1 symbol is Yellow\n\nPlayer 2 symbol is Red")

           # testing purposes
           print("Human player 1 symbol is", hp1_symbol)
           print("Human player 2 symbol is", hp2_symbol)


          
        # If the chosen game mode is Computer against another Computer player and if the yellow
        # button is clicked on, Computer Player 1 symbol = Yellow, Computer Player 2 symbol = Red
        if self.Computer_VS_Computer_mode == True:

            cp1_symbol = "Y"
            cp2_symbol = "R"

            p1 = ComputerPlayer(cp1_symbol)
            p2 = ComputerPlayer(cp2_symbol)

       # Place players 1 and 2 in the tuple for turn based game 
            self.players_lst = (p1, p2)
            self.current_player_index = 0

            # Message telling players which symbol they are
            chosen_symbol_message = messagebox.showinfo("Game Info", "Computer Player 1 symbol is Yellow\n\nComputer Player 2 symbol is Red")
        
        # testing purposes 
            print("Computer player 1 symbol is", cp1_symbol)
            print("Computer player 2 symbol is", cp2_symbol)


        # If the chosen game mode is Human against a Computer player and if the yellow
        # button is clicked on, Human Player symbol = Yellow, Computer Player symbol = Red
        if self.Human_VS_Computer_mode == True:
        
            hp_symbol= "Y"
            cp_symbol = "R"

            p1 = HumanPlayer(hp_symbol)
            p2 = ComputerPlayer(cp_symbol)

       # Place players 1 and 2 in the tuple for turn based game 
            self.players_lst = (p1, p2)
            self.current_player_index = 0

            # Message telling players which symbol they are
            chosen_symbol_message = messagebox.showinfo("Game Info", "Your chosen symbol is Yellow\n\nThe computer symbol is Red")

            # testing purposes 
            print("Human player symbol is", hp_symbol)
            print("Computer player symbol is", cp_symbol)

            
        
        # executes all of the other functions needed within the game once the symbols have been
        # chosen for the current game
        if self.symbol_choose == True:
            # Buttons destroyed as not needed during the game          
            self.choose_Yellow_button.destroy()
            self.choose_Red_button.destroy()
            
            # Grid is created       
            self.intialise_dynamic()
            
            # Restart and quit buttons are created
            self.restart_btn()
            self.quit_btn()


    def restart_btn(self):
        # Creates the restart button
        
        # Only create this button once the player has chosen their symbol
        if self.symbol_choose == True:
            self.restart_button = tkinter.Button(self.bottom_frame, text = "Restart", command = self.restart_game)
            self.restart_button.pack(side = "left")

            
    def restart_game(self):
        # This is the function used by the restart_button within the restart_btn method
        
        # Closes the current window
            self.mw.destroy()

        # Creates a new windows and runs all of the main functions within game
            main()
        
        # Lets player know that the game has been restarted
            restart_message = messagebox.showinfo("Game Info", "The game has been restarted")

            # For testing purposes
            print("\n\nThe game has been restarted, new game is created")

            
    def quit_btn(self):
        # Creates the quit button

        # Only create this button once the player has chosen their symbol
        if self.symbol_choose == True:
            self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit", command = self.mw.destroy)
            self.quit_button.pack(side = "right")


    def clicked_btn(self,x, y):
        # This method replaces the play method within the Player class. This allows players
        # to take turns and check if they are winner by calling the winner method

        # Uses player indexes to keep track of who's turn it is
        p = self.players_lst[self.current_player_index]
        
        # Get the button instance from the list
        button = self.buttons_2d_list[x][y] 

        # Human Player. i is the row number and allows the player symbol to fall
        # from the top of the grid. This only occurs if there is space on the grid

        # This is used to check if there is a space in the grid
        allow_counter_drop = True

        # This only runs if the game mode is Human VS Human or Human VS Computer 
        # as these are the only two game modes which requires a Human Player
        if self.Human_VS_Human_mode or self.Human_VS_Computer_mode == True:
        
            for i in range(6-1, -1, -1):
                free = self.gboard.is_space_free(i,y)

            # if there is no free space on the top row, ask player to pick a empty column   
                if not free and i == 0:
                    messagebox.showinfo("This column is full", "Please choose another column")
                    allow_counter_drop = False
                    
                # If there is a space on the gameboard grid
                if free == True:
                    self.gboard.make_move(i, y, p.get_player_symbol())
                    button = self.buttons_2d_list[i][y]
                    button["text"] = p.get_player_symbol()
                    break
                

        # Shows the board in text format on IDLE
            self.gboard.show_board_dynamic()
        
            
        # Allows the player to have a turn by changing index to 0
            if self.current_player_index == 1:
                self.current_player_index = 0
                
            else:
                self.current_player_index+=1 # increment index by 1

        
            winner = self.gboard.check_winner() # The board will check after each move if any player has won the game

            is_full = self.gboard.is_board_full()

            if winner == True:
                    # Show current player's symbol as Winner and terminate the game

                    win_message = ("Player %s is the Winner!" %p.get_player_symbol())
                    messagebox.showinfo("Winner Info ",win_message)
                    self.mw.destroy()
                    exit()

            
            elif is_full == True:
                # If the gameboard is full, the game ends in a draw
                
                messagebox.showinfo("Winner Info", "The game ended in a draw!")
                self.mw.destroy()
                exit()

            
            else:
            # Once the HumanPlayer has placed their counter, wait 2 seconds
            # then allow the computer player to have their turn

                # This only runs when game mode is Computer VS Computer or
                # Human VS Computer
                if self.Computer_VS_Computer_mode or self.Human_VS_Computer_mode == True:
                    root = self.mw
                    root.update()
                    time.sleep(2) # 2 seconds = computer thinking time
                    pass

            # Go to the next players turn
            p = self.players_lst[self.current_player_index]
            p.play()

            
        # Computer Player

        # This only runs if the game mode is Computer VS Computer or Human VS Computer 
        # as these are the only two game modes which requires a Computer Player
        if self.Computer_VS_Computer_mode or self.Human_VS_Computer_mode == True:


        # If the human player has placed their counter into a empty column, the computer player can have a turn
            if allow_counter_drop:

                # Picks a random column to place counter within
                y = random.randint(0,6)

            # If the computer player is looking for a empty columns, run of the below
                find_another_column = True

                # If the column chosen intially is full, find another empty column            
                while find_another_column:
                    for i in range(6-1, -1, -1):
                        free = self.gboard.is_space_free(i,y)
                        find_another_column = False

                    # If there is no space on the top row, the computer player must search for another empty column
                        if not free and i == 0:
                            print("This column is full, choose another one")
                            y = random.randint(0,6)
                            find_another_column = True

                    # if there is a free space in a column, get the player symbol 
                        if free == True:
                            self.gboard.make_move(i, y, p.get_player_symbol())
                            print("\nColumn", y)
                            button = self.buttons_2d_list[i][y]
                            button["text"] = p.get_player_symbol()
                            break             


        # Allows the player to have a turn by changing index to 0
            if self.current_player_index == 1:
                self.current_player_index = 0
                
            else:
                self.current_player_index+=1 # increment index by 1

    
            winner = self.gboard.check_winner() # The board will check after each move, if any player has won the game

            is_full = self.gboard.is_board_full()

            if winner == True:
                # Show current player's symbol as Winner and terminate the game

                    win_message = ("Player %s is the Winner!" %p.get_player_symbol())
                    messagebox.showinfo("Winner Info ",win_message)
                    self.mw.destroy()
                    exit()

            
            elif is_full == True:
                # If the gameboard is full, the game ends in a draw
                
                messagebox.showinfo("Winner Info", "The game ended in a draw!")
                self.mw.destroy()
                exit()


            else:
                pass

            self.gboard.show_board_dynamic()

            

    def intialise_dynamic(self):
        # This method creates the gameboard grid buttons which holds the player symbols within

        # The grid is only created once the coloured symbols have been chosen
        if self.symbol_choose == True:

            # Creates 6 rows and 7 columns 
            for x in range(6):
                for y in range(7):

                    self.button = tkinter.Button(self.top_frame, text = " ", font = ('Arial 30 bold'), command = lambda i = x, j = y: self.clicked_btn(i, j),height = 1, width = 4)
                    self.button.grid(row = x, column = y)
                    self.buttons_2d_list[x][y] = self.button


def main():
    # the main function instantiates an instance of b_gui from the GameGUI class. The init creates the 7x6 board using the
    # GameBoard class. The human player p1 and the computer player p2 is also created along with their symbol/colour. The players
    # are then placed into the list which ask each player to take a turn at placing their symbol/colour onto the game board
    
    b_gui = GameGUI()
    
    b_gui.game_modes()
    
    b_gui.intialise_dynamic()
    
    b_gui.restart_btn()
    b_gui.quit_btn()
    
    gui = b_gui

main()

	
                  

            


