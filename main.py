from player import player, player1, player2
from cards import deck, cards

def play_round(player1, player2):

    cards_in_play = []

    while True:
        card1 = player1.draw_card()
        card2 = player2.draw_card()

        cards_in_play.append(card1)
        cards_in_play.append(card2)

        print(player1.name, 'drew', card1)
        print(player2.name, 'drew', card2)

        if card1.value > card2.value:
            print(player1.name, 'wins the round!')
            player1.collect_cards(cards_in_play)
            break

        elif card1.value < card2.value:
            print(player2.name, 'wins the round!')
            player1.collect_cards(cards_in_play)
            break

        else:
            print("War!")
            print("Both players draw again!")
            continue

print('Welcome to the game of War!')

while player1.card_count() > 0 and player2.card_count() > 0:

    play_round(player1, player2)

    print(player1.name, 'has', player1.card_count, 'cards')
    print(player2.name, 'has', player2.card_count, 'cards')

    if player1.card_count() > 0 and player2.card_count() > 0:
        input('Press enter to play the next round.')

if player1.card_count() > 0:
    print(player1.name, 'wins the game!')
else:
    print(player2.name, 'wins the game!')