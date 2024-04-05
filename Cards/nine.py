from Cards.card import Card


class Nine(Card):
    @property
    def name(self):
        return "9"

    @property
    def points(self):
        return 9
