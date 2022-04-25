from Cards import *

class Blackjack:
    blackjack = 21
    minDeckSize = 7

    dealer = Player("Dealer")
    player = None
    deck = []

    def __init__(self, player, decks):
        self.player = player
        self.deck = self.merge_decks(decks) # ???

    def play(self):
        while len(self.deck) > self.minDeckSize: #??
            print('\n')
            print("TYPE 'play' TO START NEW ROUND")
            line: str = input().lower()
            if (line != "play"):
                return
            print('\n')
            self.play_round()
            self.player.reset_hand()
            self.delear.reset_hand()
            self.show_statistics()
            #sleep

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
            #sleep
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

    #def __round_results

    #def __show_statistics
