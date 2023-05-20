from ..deck import FullDeck
from ..player import Player

player1, player2 = Player('CPU 1'), Player('CPU 2')
new_deck = FullDeck()
new_deck.shuffle_deck()
player1.add_cards(new_deck.deck[0:26])
player2.add_cards(new_deck.deck[26:52])

round_counter = 0
game_on = True
while game_on:
    round_counter += 1
    if len(player1.hand) == 0:
        print(f'Player {player1.name} Wins')
        game_on = False
        break

    if len(player2.hand) == 0:
        print(f'Player {player2.name} Wins')
        game_on = False
        break

    player1_card = []
    player1_card.append(player1.remove_card())
    player2_card = []
    player2_card.append(player2.remove_card())

    war = True
    while war:
        if player1_card[-1].value > player2_card[-1].value:
            player1.add_cards(player1_card), player1.add_cards(player2_card)
            war = False
        elif player1_card[-1].value < player2_card[-1].value:
            player2.add_cards(player1_card), player2.add_cards(player2_card)
            war = False
        else:
            if len(player1.hand) < 5:
                print(f'Player {player2.name} Wins')
                game_on = False
                break
            elif len(player2.hand) < 5:
                print(f'Player {player1.name} Wins')
                game_on = False
                break
            else:
                for i in range(5):
                    player1_card.append(player1.remove_card())
                    player2_card.append(player2.remove_card())
print(f'Whole war took {round_counter} rounds')