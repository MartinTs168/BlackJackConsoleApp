from Cards.card import Card


class Seven(Card):
    @property
    def name(self):
        return "7"

    @property
    def points(self):
        return 7
