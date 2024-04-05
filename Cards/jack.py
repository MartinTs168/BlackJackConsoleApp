from Cards.card import Card


class Jack(Card):
    @property
    def name(self):
        return "J"

    @property
    def points(self):
        return 10
