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
        print(self.starting_cards)
        return self.starting_cards

deck1 = cards.shuffle


class deck:
    # card_hand is the list of card a player currently has
    def __init__ (self, deck):
        self.deck = deck

    # Working on it
    def show_card(self):
        self.top_card = cards[0]
        print(self.top_card)
        return self.top_card

    def draw_card(self):
        self.deck.pop(0)
    
    def add_cards(self, new_cards):
        self.deck.extend(new_cards)

    def if_lose():
        pass

    def if_won():
        pass

    def if_war(self):
        return self.draw_card()

#deck1 = cards()
#print(deck1)
#deck.show_card(cards.shuffle)

deck1 = cards()
deck1.shuffle()
print(deck1)
cards_before_war = deck(deck1)
top_card = deck.show_card
print()