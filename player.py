from cards import cards, deck, deck1, deck2

class player:
    def __init__(self, name, deck):
        self.name()
        self.deck()

    def draw_card(self, deck):
        card = self.deck.pop(0)
        return card
    
    def collect_cards(self, won_cards):
        self.deck.extend(won_cards)
    
    def card_count(self):
        return len(self.deck)
    
player1 = player('Player 1', deck1.starting_cards)
player2 = player('Player 2', deck2.starting_cards)
