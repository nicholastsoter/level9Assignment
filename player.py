from cards import cards, deck, deck1, deck2

class player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def draw_card(self, deck):
        card = self.deck.pop(0)
        return card
    
    def collect_cards(self, won_cards):
        self.deck.extend(won_cards)
    
    def card_count(self):
        return len(self.deck)
