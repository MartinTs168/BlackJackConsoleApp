from Cards.card import Card


class Two(Card):
    @property
    def name(self):
        return "2"

    @property
    def points(self):
        return 2
