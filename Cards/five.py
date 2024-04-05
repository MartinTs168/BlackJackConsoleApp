from Cards.card import Card


class Five(Card):
    @property
    def name(self):
        return "5"

    @property
    def points(self):
        return 5
