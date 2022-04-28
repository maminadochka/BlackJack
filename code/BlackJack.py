from Cards import *
from Player import *
import time


class Blackjack:
    blackjack = 21
    minDeckSize = 7

    dealer = Player("Dealer")
    player = None
    deck = []

    def __init__(self, player, decks):
        self.player = player
        self.deck = self.Cards.merge_decks(decks)  # ???

    def play(self):
        while len(self.deck) > self.minDeckSize:  # ??
            print('\n')
            print("TYPE 'play' TO START NEW ROUND")
            line: str = input().lower()
            if line != "play":
                return
            print('\n')
            self.play_round()
            self.player.reset_hand()
            self.delear.reset_hand()
            self.show_statistics()
            time.sleep(1500)

    def __play_round(self):
        self.dealer.draw_card(self.deck)
        print('\n')
        #
        #
        #
        print("Points:", player.get_points())
        if is_round_not_over_after_players_turn():
            print('\n')
            self.dealers_turn()
        print('\n')
        round_results()

    def __players_turn(self):
        while self.player.get_points() < self.blackjack:
            #
            print('\n')
            time.sleep(1500)
            print("Get a card? (y/n)")
            line = input().lower()
            if ("n" == line):
                return
            #

    def __dealer_turn(self):
        while self.dealer.get_points() < 16:
            self.dealer.draw_card(self.deck)
            self.dealer.show_hand()
            print('\n')

    def __is_round_not_over_after_players_turn(self):
        check = True
        if self.player.get_points() >= self.blackjack:
            check = False
        return check

    def __round_results(self):
        if self.player.get_points() == self.blackjack:
            #
            print("You got blackjack! You won!")
        elif self.dealer.get_points() == self.blackjack:
            #
            print("Dealer got blackjack! Dealer won!")
        elif self.player.get_points() > self.blackjack:
            #
            print("You got too much points! Dealer won!")
        elif self.dealer.get_points() > self.blackjack:
            #
            print("Dealer got too much points! You won!")
        elif self.player.get_points() > self.dealer.get_points() && self.player.get_points() < self.blackjack:
            #
            print("You got more points than dealer! You won!")
        elif self.dealer.get_points() > self.player.get_points() && self.dealer.get_points() < self.blackjack:
            #
            print("Dealer got more points than you! Dealer won!")
        else:
            print("Push!")

    def __show_statistics(self):
        print("")       #
        print("")       #