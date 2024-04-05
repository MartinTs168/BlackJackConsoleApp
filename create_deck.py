import random

from Cards.ace import Ace
from Cards.eight import Eight
from Cards.five import Five
from Cards.four import Four
from Cards.jack import Jack
from Cards.king import King
from Cards.nine import Nine
from Cards.queen import Queen
from Cards.seven import Seven
from Cards.six import Six
from Cards.ten import Ten
from Cards.three import Three
from Cards.two import Two


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CardDeck(metaclass=SingletonMeta):
    __SUITS = ["♥", "♦", "♣", "♠"]

    def __init__(self):
        self.__cards_in_play = []
        self.__cards_out_of_play = []
        self.__fill_deck()
        self.shuffle_deck()

    def __fill_deck(self):
        for i in range(8):
            for j in range(4):
                ace = Ace(self.__SUITS[j])
                two = Two(self.__SUITS[j])
                three = Three(self.__SUITS[j])
                four = Four(self.__SUITS[j])
                five = Five(self.__SUITS[j])
                six = Six(self.__SUITS[j])
                seven = Seven(self.__SUITS[j])
                eight = Eight(self.__SUITS[j])
                nine = Nine(self.__SUITS[j])
                ten = Ten(self.__SUITS[j])
                jack = Jack(self.__SUITS[j])
                queen = Queen(self.__SUITS[j])
                king = King(self.__SUITS[j])

                self.__cards_in_play.extend([ace, two, three, four, five, six, seven,
                                             eight, nine, ten, jack, queen, king])

    def shuffle_deck(self):
        self.__cards_in_play.extend(self.__cards_out_of_play)
        random.shuffle(self.__cards_in_play)
        self.__insert_cut_card()

    def __insert_cut_card(self):
        random_pos = random.randint(157, 315)
        self.__cards_in_play.insert(random_pos, "cut_card")

    def draw(self):
        drawn_card = self.__cards_in_play.pop()
        if drawn_card == "cut_card":
            self.shuffle_deck()
            print("Wait a moment we need to shuffle the cards")
            drawn_card = self.__cards_in_play.pop()
        self.__cards_out_of_play.append(drawn_card)
        return drawn_card


if __name__ == '__main__':  # testing the shuffle
    deck = CardDeck()
    print(deck._CardDeck__cards_in_play)
    deck1 = CardDeck()
    print(deck1 == deck)  # check if singleton works
