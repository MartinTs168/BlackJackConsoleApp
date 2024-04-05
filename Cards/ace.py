from Cards.card import Card


class giAce(Card):

    def __init__(self, suit):
        super().__init__(suit)
        self.changed_value = False

    @property
    def name(self):
        return "A"

    @property
    def points(self):
        return 11

    @property
    def changed_value(self):
        return self.__changed_value

    @changed_value.setter
    def changed_value(self, value: bool):
        self.__changed_value = value
