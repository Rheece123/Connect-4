class Player:

    # this the superclass for both the human and computer player. It uses a getter
    # method to return the symbol for both the human and computer player

    def __init__(self, letter):
        self.symbol = letter
       
    def get_player_symbol(self):
        return self.symbol
    

class HumanPlayer(Player):

    # this a is a subclass of the Player class. The play method is passed as the
    # GUI buttons are used instead of input
    def __init__(self, letter):
        Player.__init__(self, letter)

    def play(self):
        # do nothing as the play is done at the Button_GUI
        pass

class ComputerPlayer(Player):

    # this is a subclass of the Player class

    def __init__(self, letter):
        Player.__init__(self, letter)

    def play(self):
        # do nothing as the play is done at the Button_GUI
        pass
       
            



         
        


