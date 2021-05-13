import random


class Player:
    """A class for the player. This class of objects is responsible for
    keeping track of the points and turns.

    Attributes:
        self.cards (list): List of cards the dealer will show.
        self.guess (string): The Player's guess if the next card is higher or lower.
        self.new_card ():
        self.current_card ():

    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Player): an instance of Player.
        """

        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.hilo = True
        self.guess = 0
        self.new_card
        self.current_card

    def guess(self):
        pass

    def get_points(self):
        """Calculates the total number of points for the current round. Player starts off with 300 points. The Player gets 100 ponts if guessed correctly and loses 75 points if guessed incorrectly. If Player reaches 0 points the game is over. 

        Args: 
            self (Player): An instance of Player.

        Returns:
            number: The total points for the current round.
        """
        # I'm might be wrong, please let me know if I am
        if self.guess == 'h':
            if self.new_card > self.current_card:
                return 100
        elif self.guess == 'l':
            if self.new_card < self.current_card:
                return -75
        else:
            return ("Not valid guess!")

    def draw_card(self):
        self.new_card = random.self.cards
        self.cards.remove(new_card)
        # I think this should go down here, I could be wrong lol
        # for i in range (1, 14):
        #    self.cards.append(i)
