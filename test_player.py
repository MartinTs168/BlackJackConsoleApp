import unittest

from Cards.ace import Ace
from Players.player import Player
from create_deck import CardDeck


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.p = Player("Marti")
        card = Ace("♥")
        card1 = Ace("♥")
        self.p.hand.append(card)
        self.p.hand.append(card1)
        self.p.points = 22
        self.deck = CardDeck()

    def test_check_for_ace_with_two_aces_should_return_true_and_change_player_points(self):
        self.assertTrue(self.p.check_for_ace())
        self.assertEqual(12, self.p.points)
        self.p.check_for_ace()
        self.assertEqual(2, self.p.points)

    def test_the_splitting(self):
        new_p = Player.create_player_to_play_split_hand(self.p)
        self.assertEqual(11, new_p.points)
        self.assertEqual(11, self.p.points)
        print(new_p.hit(self.deck))
        print(self.p.hit(self.deck))


if __name__ == "__main__":
    unittest.main()
