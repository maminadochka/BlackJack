class Rank:
    name = None
    value = None

    #def __init__(self, name, value):
     #   self.name = name
     #  self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value


class Ace(Rank):
    name = "A"
    value = 11

    #def __init__(self, name, value):
     #   super(Ace, self).__init__(name, value)


class King(Rank):
    name = "K"
    value = 10

    #def __init__(self, name, value):
        #super(King, self).__init__(name, value)


class Queen(Rank):
    name = "Q"
    value = 10

    #def __init__(self, name, value):
        #super(Queen, self).__init__(name, value)


class Jack(Rank):
    name = "J"
    value = 10

    #def __init__(self, name, value):
        #super(Jack, self).__init__(name, value)


class Ten(Rank):
    name = "10"
    value = 10

    #def __init__(self, name, value):
        #super(Ten, self).__init__(name, value)


class Nine(Rank):
    name = "9"
    value = 9

    #def __init__(self, name, value):
        #super(Nine, self).__init__(name, value)


class Eight(Rank):
    name = "8"
    value = 8

    #def __init__(self, name, value):
        #super(Eight, self).__init__(name, value)


class Seven(Rank):
    name = "7"
    value = 7

    #def __init__(self, name, value):
        #super(Seven, self).__init__(name, value)


class Six(Rank):
    name = "6"
    value = 6

    #def __init__(self, name, value):
        #super(Six, self).__init__(name, value)


class Five(Rank):
    name = "5"
    value = 5

    #def __init__(self, name, value):
        #super(Five, self).__init__(name, value)


class Four(Rank):
    name = "4"
    value = 4

    #def __init__(self, name, value):
        #super(Four, self).__init__(name, value)


class Three(Rank):
    name = "3"
    value = 3

    #def __init__(self, name, value):
        #super(Three, self).__init__(name, value)


class Two(Rank):
    name = "2"
    value = 2

    #def __init__(self, name, value):
        #super(Two, self).__init__(name, value)
