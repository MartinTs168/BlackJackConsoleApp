from abc import ABC, abstractmethod

from Cards.ace import Ace
from create_deck import CardDeck


class BasePlayer(ABC):
    __BUST_CAP = 21

    def __init__(self, name):
        self.name = name
        self._hand = []  # list of Card object
        self.__points = 0
        self._is_bust = False

    @property
    def hand(self):
        return self._hand

    def _setHand(self, value):
        self._hand = [value]

    @property
    def points(self):
        return self.__points

    @property
    def is_bust(self):
        return self._is_bust

    @points.setter
    def points(self, value):
        if value < 0:
            raise ValueError("Invalid value for points")
        self.__points = value

    @abstractmethod
    def hit(self, deck: CardDeck):
        ...

    def check_is_pl_bust(self):
        if self.points > self.__BUST_CAP:
            if not self.check_for_ace():
                self._is_bust = True

    @abstractmethod
    def set_board(self, deck):
        ...

    def check_for_blackjack(self):
        if self.points == self.__BUST_CAP:
            return True

        return False

    def check_for_ace(self):
        for card in self.hand:
            if isinstance(card, Ace) and not card.changed_value:
                card.changed_value = True
                self.points -= 10
                return True

        return False

    @abstractmethod
    def reset(self):
        ...
