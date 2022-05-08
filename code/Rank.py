class Rank:
    name = None
    value = None

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value


class Ace(Rank):
    name = "A"
    value = 11


class King(Rank):
    name = "K"
    value = 10


class Queen(Rank):
    name = "Q"
    value = 10


class Jack(Rank):
    name = "J"
    value = 10


class Ten(Rank):
    name = "10"
    value = 10


class Nine(Rank):
    name = "9"
    value = 9


class Eight(Rank):
    name = "8"
    value = 8


class Seven(Rank):
    name = "7"
    value = 7


class Six(Rank):
    name = "6"
    value = 6


class Five(Rank):
    name = "5"
    value = 5


class Four(Rank):
    name = "4"
    value = 4


class Three(Rank):
    name = "3"
    value = 3


class Two(Rank):
    name = "2"
    value = 2
