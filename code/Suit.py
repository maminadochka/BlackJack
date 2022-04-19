class Suit:
    name = None

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Cross(Suit):
    name = "Cross"

    def __init__(self, name):
        super(Cross, self).__init__(name)


class Diamond(Suit):
    name = "Diamond"

    def __init__(self, name):
        super(Diamond, self).__init__(name)


class Heart(Suit):
    name = "Heart"

    def __init__(self, name):
        super(Heart, self).__init__(name)


class Spade(Suit):
    name = "Spade"

    def __init__(self, name):
        super(Spade, self).__init__(name)
