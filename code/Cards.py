from Rank import *
from Suit import *
import random


# card's  generating
class Card:
    suit: Suit
    rank: Rank

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_name(self):
        return self.rank.get_name() + self.suit.get_name()


# deck's creator
class DeckCreator:
    ranks = [
        Two(),
        Three(),
        Four(),
        Five(),
        Six(),
        Seven(),
        Eight(),
        Nine(),
        Ten(),
        Jack(),
        Queen(),
        King(),
        Ace()
    ]

    suits = [
        Heart(),
        Diamond(),
        Spade(),
        Cross()
    ]

    def create_deck(self):
        deck = []
        for suit in self.suits:
            for rank in self.ranks:
                deck.append(Card(suit, rank))
        random.shuffle(deck)
        return deck

    def merge_decks(self, decks):
        if decks < 2:
            return self.create_deck()
        deck = []
        for i in range(decks):
            deck.extend(self.create_deck())
        random.shuffle(deck)
        return deck








