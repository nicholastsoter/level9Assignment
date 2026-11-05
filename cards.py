import random

class cards:

     
    def __init__(self):
        self.starting_cards = []
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
                    value = 14
                elif j > 1 and j < 11:
                    card = str(j) + suit
                    value = j
                elif j == 11:
                    card = "Jack" + suit
                    value = 11
                elif j == 12:
                    card = "Queen" + suit
                    value = 12
                elif j == 13:
                    card = "King" + suit
                    value = 13
                card = (card, value)
                self.starting_cards.append(card)

    def shuffle(self):
        random.shuffle(self.starting_cards)
        return self.starting_cards


class deck:
    # card_hand is the list of card a player currently has
    def __init__ (self, deck):
        self.deck = deck

    def starting_cards(self):
        return self.deck

    def show_card(self):
        self.top_card = cards[0]
        print(self.top_card)
        return self.top_card

    #def draw_card(self):
    #    self.deck.pop(0)
    
    def add_cards(self, new_cards):
        self.deck.extend(new_cards)
