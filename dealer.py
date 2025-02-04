from card import Card
from visuals import *
import random
class Dealer:
    def __init__(self):
        self.current_cards = []
        self.current_score = 0
        self.is_out = False
        
    def deal_card(self, player):
        if player.is_out == False:
            new_card = Card(random.choice(list(SUITS.keys())), random.choice(RANK))
            player.current_cards.append(new_card)
        else:
            return 

    def print_dealer_cards_in_row(self, cards):
        # Split each card representation into lines
        card_lines = [card.draw_card().split("\n") for card in cards]

        # Print each row by combining corresponding lines of all cards
        for lines in zip(*card_lines):
            print("  ".join(lines))  # Join lines with spacing

        return "\nDealer's cards ⬆"
    
    def add_to_score(self):
        if self.is_out == False and self.current_score < 21:
            if self.current_cards[len(self.current_cards)-1].rank in ["K", "J", "Q", "A"]:
                symbol_value = self.current_cards[len(self.current_cards)-1].get_symbols_value(self.current_cards[len(self.current_cards)-1].rank)
                self.current_score += symbol_value
            else:
                 self.current_score += int(self.current_cards[len(self.current_cards)-1].rank)
        else:
            self.over_limit = True
        