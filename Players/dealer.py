from Players.base_player import BasePlayer
from create_deck import CardDeck


class Dealer(BasePlayer):
    __SOFT_CAP = 17

    def __init__(self):
        super().__init__("Dealer")
        self.__reached_soft_cap = False

    @property
    def reached_soft_cap(self):
        return self.__reached_soft_cap

    def set_board(self, deck: CardDeck):
        first_card = deck.draw()
        second_card = deck.draw()
        self.hand.extend([first_card, second_card])
        self.points += first_card + second_card
        if self.points > 21:
            self.check_for_ace()
        self.check_has_reached_soft_cap()
        if not self.check_for_blackjack():
            return f"Dealers hand: ? {second_card}"

        return f"Dealer has blackjack: {first_card} {second_card}"

    def check_has_reached_soft_cap(self):
        if self.points >= 17:
            self.__reached_soft_cap = True

    def hit(self, deck: CardDeck):
        drawn_card = deck.draw()
        self.hand.append(drawn_card)
        self.points += drawn_card.points
        self.check_is_pl_bust()
        self.check_has_reached_soft_cap()
        return f"Dealer drew a {drawn_card}. {self.__repr__()}"

    def reset(self):
        self.points = 0
        self._hand = []
        self._is_bust = False
        self.__reached_soft_cap = False

    def __repr__(self):
        return f"Dealer's hand is {' '.join(str(c) for c in self.hand)} - {self.points} points"