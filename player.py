import random
from cards import cards
class player:
    def __init__(self, name, deck):
        self.name = name
        #Take all the cards out of the deck object and keep them as this player's pile
        self.cards = deck

    def draw_card(self):
        card = self.cards.starting_cards.pop(0)
        return card
    
    def collect_cards(self, won_cards):
        #Adds cards to the bottom of the deck and shuffles them to avoid repeats
        random.shuffle(won_cards)
        self.cards.starting_cards.extend(won_cards)

    def has_cards(self):
        if len(self.cards.starting_cards) > 0:
            return True
    
    def card_count(self):
        return len(self.cards.starting_cards)
