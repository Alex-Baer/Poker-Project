# This class models a playing card in a deck.
# Attributes includes the suit of the card (string: suit name)
# and the value of the card when playing poker (number between 2 and 14 inclusive).
class Card:
    def __init__(self, suit: str, value: int):
        self.suit = suit
        self.value = value

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def get_name(self):
        names = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
        return f'{names[self.value - 2]} of {self.suit}'

    def image_file_name(self):
        file_cards = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace")
        return f'cards/{file_cards[self.value - 2]}_of_{self.suit}.png'



