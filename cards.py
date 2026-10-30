import random

class cards:


    starting_cards = [] 
    def __init__(self):
        for i in range(1,5):
            if i == 1:
                suit = " of hearts"
            if i == 2:
                suit = " of clubs"
            if i == 3:
                suit = " of spades"
            if i == 4:
                suit = " of dimonds"
            for j in range(1,14):
                card = ("")
                if j == 1:
                    card = "Ace" + suit
                elif j > 1 and j < 11:
                    card = str(j) + suit
                elif j == 11:
                    card = "Jack" + suit
                elif j == 12:
                    card = "Queen" + suit
                elif j == 13:
                    card = "King" + suit
                
                self.starting_cards.append(card)

    def shuffle(self):
        random.shuffle(self.starting_cards)


class deck:

    def __init__(self):
        deck_hand = cards
        



deck1 = cards()
print(deck1)