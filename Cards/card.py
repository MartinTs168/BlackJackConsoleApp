from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, suit):
        self.__suit = suit
        self.__name = self.name
        self.__points = self.points

    @property
    @abstractmethod
    def name(self):
        ...

    @property
    @abstractmethod
    def points(self):
        ...

    def __str__(self):
        return f"{self.name}{self.__suit}"

    def __add__(self, other):
        return self.points + other.points

