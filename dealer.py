from card import Card
from visuals import *
import random
class Dealer:
    def __init__(self):
        self.current_cards = []
        
    def deal_card(self, player):
        new_card = Card(random.choice(list(SUITS.keys())), random.choice(RANK))
        player.current_cards.append(new_card)

    def print_dealer_cards_in_row(self, cards):
        # Split each card representation into lines
        card_lines = [card.draw_card().split("\n") for card in cards]

        # Print each row by combining corresponding lines of all cards
        for lines in zip(*card_lines):
            print("  ".join(lines))  # Join lines with spacing

        return "\nDealer's cards ⬆"