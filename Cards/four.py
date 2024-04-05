from Cards.card import Card


class Four(Card):
    @property
    def name(self):
        return "4"

    @property
    def points(self):
        return 4