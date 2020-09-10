# Game setup
from player import Player
from deck import Deck


if __name__ == "__main__":
    player_one = Player('One')
    player_two = Player('Two')

    deck = Deck()
    deck.shuffle()

    # Split the deck. Set player's hand
    player_one.add_cards(deck.all_cards[:26])
    player_two.add_cards(deck.all_cards[26:])

    # Game on
    round_num = 0
    game_on = True

    while game_on:
        round_num += 1
        print("Round {}".format(round_num))

        if len(player_one.all_cards) == 0:
            print("Player one is out of cards. Player two wins")
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print("Player two is out of cards. Player one wins")
            game_on = False
            break

        # Start a new round
        player_one_cards, player_two_cards = [], []
        player_one_cards.append(player_one.remove_one())
        player_two_cards.append(player_two.remove_one())

        war = True

        while war:
            # Compare the cards
            print("{} vs {}".format(player_one_cards[-1],player_two_cards[-1]))
            if player_one_cards[-1].value > player_two_cards[-1].value:
                print("Player one add cards")
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                war = False
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                print("Player two add cards")
                player_two.add_cards(player_two_cards)
                player_two.add_cards(player_one_cards)
                war = False
            else:
                print("War!")
                # Check if players have enough cards
                if len(player_one.all_cards) < 5:
                    print("Player one unable to declare war")
                    print("Player two wins!")
                    game_on = False
                    break
                elif len(player_two.all_cards) < 5:
                    print("Player two unable to declare war")
                    print("Player one wins!")
                    game_on = False
                    break
                else:
                    for num in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

            print("End of round. Player one has {} cards and player two has {}".format(len(player_one.all_cards), len(player_two.all_cards)))