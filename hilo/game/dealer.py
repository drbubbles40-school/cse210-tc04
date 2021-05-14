from game.player import Player

class Dealer:
    """A class for the bot who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        player (Player): An instance of the class of objects known as Player.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.keep_playing = True
        self.score = 0
        self.player = Player()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.can_draw()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means revealing the card.

        Args:
            self (Dealer): An instance of Dealer.
        """
        self.player.draw_card()
        print(f"\nThe selected card is: {self.player.current_card}")
        self.player.get_guess()
    

       
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Dealer): An instance of Dealer.
        """
        points = self.player.get_points()
        self.score += points

    def can_draw(self):
        """Checks if score is 0 or below or if all cards have been used.
        This method will set the keep_playing attribute to false, Ending the loop

        Args:
            self (Dealer): An instance of Dealer."""
        if self.score <= 0:
            self.keep_playing = False
        
        if len(self.player.cards) == 0:
            self.keep_playing = False
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dice that were rolled and the score.

        Args:
            self (Dealer): An instance of Dealer.
        """
        print(f"\nThe card is: {self.card}")
        print(f"Your score is: {self.score}")
        if self.player.can_throw():
            choice = input("Keep Playing? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False
