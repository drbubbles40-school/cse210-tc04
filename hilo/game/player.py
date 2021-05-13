import random

class Player:
    """A class for the player. This class of objects is responsible for
    keeping track of the points and turns.
    
    Attributes:
        draw_card (number): returns a card number and removes it from the list of values.
        player (Player): An instance of the class of objects known as Player.
    """
    
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        
        self.cards = []
        for i in range (1, 14):
            self.cards.append(i)

    def draw_card(self):
        new_card = random.self.cards
        self.cards.remove(new_card)
            