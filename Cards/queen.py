from Cards.card import Card


class Queen(Card):
    @property
    def name(self):
        return "Q"

    @property
    def points(self):
        return 10
