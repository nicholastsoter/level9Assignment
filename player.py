import random

class player:
    def __init__(self, name, deck):
        self.name = name
        #Take all the cards out of the deck object and keep them as this player's pile
        self.cards = deck.deal_all()

    def draw_card(self):
        card = self.cards.pop(0)
        return card
    
    def collect_cards(self, won_cards):
        #Adds cards to the bottom of the deck and shuffles them to avoid repeats
        random.shuffle(won_cards)
        self.deck.extend(won_cards)

    def has_cards(self):
        return len(self.cards) > 0
    
    def card_count(self):
        return len(self.cards)
