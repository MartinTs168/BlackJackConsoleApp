from Cards.card import Card


class King(Card):
    @property
    def name(self):
        return "K"

    @property
    def points(self):
        return 10
