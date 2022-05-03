from Player import *
from BlackJack import *


class Play:
    player = Player(input("Your name: "))
    decks = int(input("Number of decks: "))

    bj = Blackjack(player, decks)
    bj.play()
