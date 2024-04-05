from Players.base_player import BasePlayer
from create_deck import CardDeck


class Player(BasePlayer):

    def __init__(self, name):
        super().__init__(name)
        self.has_doubled_down = False

    @classmethod
    def create_player_to_play_split_hand(cls, player):
        new_player = cls(player.name)
        card = player.hand.pop()
        new_player._setHand(card)
        player.points -= card.points
        new_player.points += card.points
        return new_player

    def hit(self, deck: CardDeck):
        drawn_card = deck.draw()
        self.hand.append(drawn_card)
        self.points += drawn_card.points
        self.check_is_pl_bust()
        return f"{self.name} drew a {drawn_card} - you have {self.points}"

    def set_board(self, deck: CardDeck):
        first_card = deck.draw()
        second_card = deck.draw()
        self.hand.extend([first_card, second_card])
        self.points += first_card + second_card
        if self.points > 21:
            self.check_for_ace()
        if not self.check_for_blackjack():
            return f"{self.name}'s hand: {first_card} {second_card} - you have {self.points}"

        return f"{self.name} has blackjack: {first_card} {second_card}"

    def split_hand(self):
        card = self.hand.pop()
        self.points -= card.points
        return card

    def reset(self):
        self.points = 0
        self._hand = []
        self._is_bust = False
        self.has_doubled_down = False
