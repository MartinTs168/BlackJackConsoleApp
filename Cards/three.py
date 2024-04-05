from Cards.card import Card


class Three(Card):
    @property
    def name(self):
        return "3"

    @property
    def points(self):
        return 3