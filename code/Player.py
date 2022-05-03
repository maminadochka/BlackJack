from Cards import *


class Player:
    name = None
    victories = 0
    hand = []

    def __init__(self, name):
        self.name = name

    def draw_card(self, deck):
        if len(deck) < 1:
            print("No more card in the desk")
            return
        card = deck.pop(0)
        self.hand.append(card)
        print(self.name + " got " + card.get_name())

    def reset_hand(self):
        self.hand.clear()

    def add_victory(self):
        self.victories += 1

    def get_points(self):
        points = 0
        for card in self.hand:
            if points > 10 and str(card.get_rank()) == 'A':
                points += 1
            else:
                points += card.get_rank().get_value()
        return points

    def get_name(self): return self.name

    def get_victories(self): return self.victories

    def show_hand(self):
        print(self.name + ": " + self.hand)
        print("Points: " + str(self.get_points()))
