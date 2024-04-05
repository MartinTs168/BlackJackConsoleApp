from Cards.card import Card


class Six(Card):
    @property
    def name(self):
        return "6"

    @property
    def points(self):
        return 6
