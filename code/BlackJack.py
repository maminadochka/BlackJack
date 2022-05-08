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

        dc = DeckCreator()
        self.deck = dc.merge_decks(decks)

    def play(self):
        if len(self.deck) > self.minDeckSize:
            while True:
                print('\n')
                print("TYPE 'play' TO START NEW ROUND OR 'exit' TO END THE GAME")
                line: str = input().lower()
                if line == "exit":
                    quit()
                if line != "play":
                    return
                print('\n')

                self.__play_round()
                self.player.reset_hand()
                self.dealer.reset_hand()
                self.__show_statistics()
                time.sleep(2)
        else:
            print("Too few cards in the deck to start new round!")
            quit()

    def __play_round(self):
        self.dealer.draw_card(self.deck)
        print('\n')
        self.player.draw_card(self.deck)
        self.player.draw_card(self.deck)
        self.__players_turn()
        if self.__is_round_not_over_after_players_turn():
            print('\n')
            self.__dealer_turn()
        print('\n')
        self.__round_results()

    def __players_turn(self):
        while self.player.points < self.blackjack:
            self.player.show_hand()
            print('\n')
            time.sleep(2)
            print("Get a card? (y/n)")
            line = input().lower()
            if "n" == line:
                self.player.show_hand()
                return
            self.player.draw_card(self.deck)

    def __dealer_turn(self):
        while self.dealer.points < 16:
            self.dealer.draw_card(self.deck)
            self.dealer.show_hand()
            print('\n')

    def __is_round_not_over_after_players_turn(self):
        check = True
        if self.player.points >= self.blackjack:
            check = False
        return check

    def __round_results(self):
        if self.player.points == self.blackjack:
            self.player.add_victory()
            print("You got blackjack! You won!")
        elif self.dealer.points == self.blackjack:
            self.dealer.add_victory()
            print("Dealer got blackjack! Dealer won!")
        elif self.player.points > self.blackjack:
            self.dealer.add_victory()
            print("You got too much points! Dealer won!")
        elif self.dealer.points > self.blackjack:
            self.player.add_victory()
            print("Dealer got too much points! You won!")
        elif (self.player.points > self.dealer.points) and (self.player.points < self.blackjack):
            self.player.add_victory()
            print("You got more points than dealer! You won!")
        elif (self.dealer.points > self.player.points) and (self.dealer.points < self.blackjack):
            self.dealer.add_victory()
            print("Dealer got more points than you! Dealer won!")
        else:
            print("Push!")

    def __show_statistics(self):
        print(str(self.player.get_name()) + " : " + str(self.player.get_victories()))
        print("Dealer: " + str(self.dealer.get_victories()))
