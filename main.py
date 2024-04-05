import sys
import time

from Cards.ace import Ace
from Players.dealer import Dealer
from Players.player import Player
from create_deck import CardDeck


def dealer_plays():
    print(dealer)
    while True:
        if dealer.is_bust or dealer.reached_soft_cap:
            break
        print(dealer.hit(deck))
        time.sleep(3)


def check_can_bet(try_bet):
    if budget < try_bet:
        print("You can't bet more money than you have try again!")
        return False
    return True


def check_result(cur_player):
    global budget
    cur_bet = bet
    if cur_player.has_doubled_down:
        cur_bet *= 2
        budget -= bet
    if dealer.is_bust:
        message = f"Dealer busted!\n{cur_player.name} wins ${cur_bet}"
        budget += cur_bet * 2
    elif dealer.points == cur_player.points:
        message = f"{cur_player.name} and Dealer are tied"
        budget += cur_bet
    elif dealer.points > cur_player.points:
        message = f"Dealer wins!"
    else:
        message = f"{cur_player.name} you win ${cur_bet}"
        budget += cur_bet * 2

    return message


def reset_table():
    dealer.reset()
    player.reset()


budget = 5000
deck = CardDeck()
dealer = Dealer()
player = Player(input("Please enter your name: "))
valid_commands = ['stand', 'hit', 'double down', 'split']
while True:
    while True:
        print(f"{player.name} you have ${budget:.2f}")
        print("If you want to stand up write 'stand up' in the bet section!")
        try:
            bet = input("Enter your bet: ")
            bet = int(bet)
        except ValueError:
            if bet.lower() == "stand up":
                raise sys.exit()

        if not check_can_bet(bet):
            continue
        budget -= bet

        print(dealer.set_board(deck))
        player_board = player.set_board(deck)

        if dealer.check_for_blackjack() and not player.check_for_blackjack():
            print(player_board)
            print(f"You lost ${bet}")
            reset_table()
            break

        elif dealer.check_for_blackjack() and player.check_for_blackjack():
            print(player_board)
            print(f"{player.name} and Dealer are tied!")
            budget += bet
            break

        elif player.check_for_blackjack():
            winnings = bet * 1.25
            print(player_board)
            print(f"You won ${winnings:.2f}")
            budget += winnings + bet
            reset_table()
            break

        hands = [player]  # wil contain the hands aka the player objects to play each hand
        for player in hands:
            while True:
                print(f"{player.name}'s hand: {' '.join(str(c) for c in player.hand)} - you have {player.points}")
                print("Make a choice: 'Stand'  'Hit'  'Double down'  'Split'")
                command = input().lower()
                if command not in valid_commands:
                    print(f"{command} is an invalid command!")
                    continue

                if command == 'stand':
                    break
                elif command == 'hit':
                    print(player.hit(deck))
                    if player.is_bust:
                        print(f"{player.name} busted!\nDealer wins!")
                        break
                elif command == 'double down':
                    if check_can_bet(bet):
                        print(player.hit(deck))
                        if player.is_bust:
                            print(f"{player.name} busted!\nDealer wins!")
                            budget -= bet
                        player.has_doubled_down = True
                        break
                    else:
                        continue
                elif command == 'split':
                    if len(player.hand) == 2 and player.hand[0].points == player.hand[1].points:
                        if check_can_bet(bet):
                            budget -= bet
                            hands.append(Player.create_player_to_play_split_hand(player))
                            if isinstance(player.hand[0], Ace) and player.hand[0].changed_value:
                                player.points += 10
                            print(player.hit(deck))
                            print(hands[-1].hit(deck))
                            continue
                    else:
                        print("Can't split these cards! Try again")
                    continue

        if not player.is_bust:
            dealer_plays()
            for cur_player in hands:
                print(check_result(cur_player))

        if budget <= 0:
            print("You lost all of your money!")
            raise sys.exit()
        reset_table()
