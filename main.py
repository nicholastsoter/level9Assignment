from player import player
from cards import (deck, cards)

def play_round(player1, player2):

    cards_in_play = []

    while True:
        card1 = player1.draw_card()
        card2 = player2.draw_card()
        

        cards_in_play.append(card1)
        cards_in_play.append(card2)

        print(player1.name, 'drew the', card1[0])
        print(player2.name, 'drew the', card2[0])

        if card1[1] > card2[1]:
            print(player1.name, 'wins the round!')
            player1.collect_cards(cards_in_play)
            return player1

        elif card1[1] < card2[1]:
            print(player2.name, 'wins the round!')
            player2.collect_cards(cards_in_play)
            return player2

        else:
            print('War!')
            #If someone has no card left to play in the war, the other player wins everything
            if not player1.has_cards() or not player2.has_cards():
                if player1.card_count() == 104:
                    winner = 'Player 1'
                elif player2.card_count() == 104:
                    winner = 'Player 2'
                #winner = player1 if player1.has_cards() else player2
                print(f'{winner} wins the war because the other player ran out of cards!')
                winner.collect_cards(cards_in_play)
                return winner

def main():
    print('Welcome to the game of war!')

    #make and shuffle the decks before the game begins
    deck1 = cards()
    deck2 = cards()
    deck1.shuffle()
    deck2.shuffle()

    

    player1 = player('Player 1', deck1)
    player2 = player('Player 2', deck2)

    while player1.has_cards() and player2.has_cards():
        play_round(player1, player2)
 
        print(player1.name, 'has', player1.card_count(), 'cards.')
        print(player2.name, 'has', player2.card_count(), 'cards.')

        if player1.has_cards() and player2.has_cards():
            input('Press enter to play the next round')
            print()
        else:
            if player1.has_cards():
                winner = 'Player 1'
            if player2.has_cards():
                winner = 'Player 2'
            print(f'{winner} wins the war because the other player ran out of cards!')

main()