from Cards.card import Card


class Ten(Card):
    @property
    def name(self):
        return "10"

    @property
    def points(self):
        return 10
