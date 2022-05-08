class Suit:
    name = None

    def get_name(self):
        return self.name


class Cross(Suit):
    name = "Cross"


class Diamond(Suit):
    name = "Diamond"


class Heart(Suit):
    name = "Heart"


class Spade(Suit):
    name = "Spade"
