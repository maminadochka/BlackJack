class Player:
    name = None
    victories = 0
    points = 0

    def __init__(self, name):
        self.name = name
        self._connection = None

    def draw_card(self, deck):
        if len(deck) < 1:
            return
        card = deck.pop(0)
        str1 = self.name + " got " + str(card.get_name())
        if self.points > 10 and str(card.get_rank()) == 'A':
            self.points += 1
        else:
            self.points += card.get_rank().get_value()
        return str1

    def reset_hand(self):
        self.points = 0

    def add_victory(self):
        self.victories += 1

    def get_name(self):
        return self.name

    def get_victories(self):
        return self.victories

    def show_hand(self):
        point = str(self.points)
        return point.encode()

    def set_connection(self, connection):
        self.connection = connection
