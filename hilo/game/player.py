import random


class Player:
    """A class for the player. This class of objects is responsible for
    keeping track of the points and turns.

    Attributes:
        draw_card (number): returns a card number and removes it from the list of values.
        self.cards (list): List of cards the dealer will show.
        self.hilo (boolean): Determines if the guess is correct.
        self.guess (number): The number of the guessed card.

    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Player): an instance of Player.
        """

        self.cards = []
        self.hilo = True
        self.guess = 0

    def get_points(self):
        """Calculates the total number of points for the current round. Player starts off with 300 points. The Player gets 100 ponts if guessed correctly and loses 75 points if guessed incorrectly. If Player reaches 0 points the game is over. 

        Args: 
            self (Player): An instance of Player.

        Returns:
            number: The total points for the current round.
        """
        # I'm might be wrong, please let me know if I am
        points = 300
        if self.hilo.choice("h"):
            if self.guess > self.cards:
                return points + 100
        elif self.hilo.choice("l"):
            if self.guess < self.cards:
                return points - 75

    def draw_card(self):
        new_card = random.self.cards
        self.cards.remove(new_card)
        # I think this should go down here, I could be wrong lol
        # for i in range (1, 14):
        #    self.cards.append(i)
