from Cards import *


class Player:
    name = None
    victories = 0
    hand = []

    def __init__(self, name):
        self.name = name

    def draw_card(self, deck):
        if deck.size < 1:
            print("No more card in the desk")
            return
        card: Card = deck.remove(0)
        self.hand.add(card)
        print(self.name + "got" + card.tostring())

    def reset_hand(self):
        self.hand.clear()

    def add_victory(self):
        self.victories += 1

    def get_points(self):
        points = 0
        # for (card : self.hand):
        #
        #
        #
        #
        return points

    def get_name(self): return self.name

    def get_victories(self): return self.victories

    def show_hand(self):
        print(self.name + ": " + self.hand)
        print("Points: " + self.get_points())