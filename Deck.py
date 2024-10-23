import random
import Card


# The Deck class models a deck 52 unique player cards from the Card class.
# The only attribute is deck which is a list with Card objects
# The deck constructor makes a 52 player card deck list by incorperating a nested loop that goes through a list of suits
# and range of values making 52 unique Card objects. The deck is in order, and uses the
# shuffle() method to randomize the deck order and eventually game outcomes.
# The deal card method stores the last card of the deck by using the len() method.
# The print_deck() method uses list comprehension that makes and prints a list using loops through the deck
# printing the list self.deck using the variable x for each individual object.
class Deck:
    def __init__(self):
        suits = ("diamonds", "clubs", "spades", "hearts")
        self.deck = []
        for i in suits:
            # the_suit = i
            for f in range(13):
                self.deck.append(Card.Card(i, f + 2))
        self.shuffle()

    def get_deck(self):
        return self.deck

    def print_deck(self):
        print([x for x in self.deck])

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        removed = self.deck[len(self.deck) - 1]
        self.deck.pop()
        return removed


