from Deck import Deck
from Card import Card


# The hand class represents five playing cards out of a deck given to a player.
# The only attribute is a list of five Card objects called hand
# For the rank method I broke the algorithm into multiple functions in a process called method decomposition, and
# I used loops to compare values and suits of cards determining the rank of the card.
# The Algorithm starts by running the algorithms that check the higher ranks first with the rank being checked
# incrementing down each time. The compare function uses the rank method to compare the rank of the card to each other,
# and in the case of a rank tie compare uses method decomposition, loops, and nested loops to compare the
# card values and suits of both of the hands to each other and the rank method to help specify the type of tie
# and resolve the rank tie.


class Hand:

    def __init__(self):
        self.hand = []

    def get_hand(self):
        return self.hand

    def print_hand(self):
        [print(i.get_name()) for i in self.hand]

    def add_card(self, card: Card):
        # check with teacher to make sure this works
        self.hand.insert(len(self.hand) - 1, card)
        self.hand.sort(key=self.sort_order)
        self.hand.reverse()

    @staticmethod
    def sort_order(elem):
        return elem.get_value()

    def is_flush(self):
        for i in self.hand:
            if not (i.suit == self.hand[0].suit):
                return False
        return True

    def is_royal_flush(self):
        t = 14
        for i in self.hand:
            if not (i.get_value() == t):
                return False
            t = t - 1
        if not (self.is_flush()):
            return False
        return True

    # change it so ace can be one
    # fix is_straight so it doesn't try and find 5 of the same card
    def is_straight(self):
        is_false = True
        t = self.get_hand()[0].get_value()
        comparison = []
        for i in self.get_hand():
            comparison.append(i.get_value())
        if comparison == [14, 5, 4, 3, 2]:
            return True
        for i in self.get_hand():
            if not (i.get_value() == (t - self.get_hand().index(i))):
                return False
        return True

    def is_straight_flush(self):
        if not (self.is_straight() and self.is_flush()):
            return False
        return True

    def is_multi_kind(self):
        # try using sum()
        multi = []
        original = 0
        finding = 0
        streak = 0
        while finding < len(self.hand):
            if self.hand[original].get_value() == self.hand[finding].get_value():
                streak = streak + 1
            elif streak >= 2:
                multi.append(streak)
                streak = 0
                original = finding
                finding = finding - 1
            else:
                streak = 0
                original = finding
                finding = finding - 1
            if streak >= 2 and finding == 4:
                multi.append(streak)
            finding = finding + 1
        return multi

    def rank(self):
        multi = self.is_multi_kind()
        if self.is_royal_flush():
            return 9
        if self.is_straight_flush():
            return 8
        if multi == [4]:
            return 7
        if multi == [2, 3] or multi == [3, 2]:
            return 6
        if self.is_flush():
            return 5
        if self.is_straight():
            return 4
        if multi == [3]:
            return 3
        if multi == [2, 2]:
            return 2
        if multi == [2]:
            return 1
        return 0

    def compare(self, other_hand):
        rank1 = self.rank()
        rank2 = other_hand.rank()
        compare1 = 0
        compare2 = 0
        if rank1 > rank2:
            return 1
        if rank2 > rank1:
            return -1
        if rank1 == 9:
            return 0
        if rank1 == 8 or rank1 == 4:
            if self.hand[0].get_value() == 14 and self.hand[4].value == 2:
                compare1 = self.hand[3].get_value()
            else:
                compare1 = self.hand[2].get_value()
            if other_hand.hand[0].get_value() == 14 and other_hand.hand[4].get_value() == 2:
                compare2 = other_hand.hand[3].get_value()
            else:
                compare2 = other_hand.hand[2].get_value()
        if rank1 == 8:
            if compare1 > compare2:
                return 1
            if compare1 < compare2:
                return -1
            else:
                return 0
        if rank1 == 7:
            return self.compare_middle(other_hand)
        if rank1 == 6:
            return self.compare_middle(other_hand)
        if rank1 == 5:
            return self.compare_high_card(other_hand)
        if rank1 == 4:
            if compare1 > compare2:
                return 1
            elif compare2 > compare1:
                return -1
            else:
                return 0
        if rank1 == 3:
            return self.compare_middle(other_hand)
        if rank1 == 2:
            if self.value_of_pair()[0] > other_hand.value_of_pair()[0]:
                return 1
            if self.value_of_pair()[0] < other_hand.value_of_pair()[0]:
                return -1
            if self.value_of_pair()[1] > other_hand.value_of_pair()[1]:
                return 1
            if self.value_of_pair()[1] < other_hand.value_of_pair()[1]:
                return -1
            return self.compare_high_card(other_hand)
        if rank1 == 1:
            if self.value_of_pair()[0] > other_hand.value_of_pair()[0]:
                return 1
            if self.value_of_pair()[0] < other_hand.value_of_pair()[0]:
                return -1
            return self.compare_high_card(other_hand)
        if rank1 == 0:
            return self.compare_high_card(other_hand)

    def compare_middle(self, other_hand):
        if self.hand[2].get_value() > other_hand.hand[2].get_value():
            return 1
        if self.hand[2].get_value() < other_hand.hand[2].get_value():
            return -1

    def compare_high_card(self, other_hand):
        for i in range(5):
            if self.hand[i].get_value() > other_hand.hand[i].get_value():
                return 1
            if self.hand[i].get_value() < other_hand.hand[i].get_value():
                return -1
        return 0

    def value_of_pair(self):
        count = []
        values = []
        i = 0
        for j in self.get_hand():
            values.append(j.get_value())
        while i < len(values):
            if values.count(values[i]) == 2:
                count.append(values[i])
            i = i + 2
        print(count)
        return count

    def get_hand_type(self):
        ranking = ["High Card", "One Pair", "Two Pair", "Three-of-a-kind", "Straight", "Flush", "Full House", "Four-of-a-kind", "Straight Flush", "Royal Flush"]
        return ranking[self.rank()]

    def __repr__(self):
        return f'{self.hand[0].get_name()} - {self.hand[1].get_name()} - {self.hand[2].get_name()} - \
               {self.hand[3].get_name()} - {self.hand[4].get_name()}'


if __name__ == '__main__':
    hand1 = Hand()
    hand2 = Hand()
    card1 = Card("clubs", 13)
    print(card1.get_suit())
    print(card1.get_value())
    print(card1.image_file_name())
    print(card1.get_name())
    card2 = Card("diamonds", 13)
    card3 = Card("diamonds", 10)
    card4 = Card("diamonds", 10)
    card5 = Card("diamonds", 9)
    my_hand = [card1, card2, card3, card4, card5]
    for i in my_hand:
        hand1.add_card(i)
    card6 = Card("diamonds", 13)
    # print(card1.get_suit())
    # print(card1.get_value())
    # print(card1.image_file_name())
    # print(card1.get_name())
    card7 = Card("diamonds", 13)
    card8 = Card("clubs", 12)
    card9 = Card("diamonds", 12)
    card10 = Card("diamonds", 9)
    my_hand_two = [card6, card7, card8, card9, card10]
    for i in my_hand_two:
        hand2.add_card(i)
    print(hand1.rank())
    print(hand2.rank())
    print(hand1.compare(hand2))


















