from card import Card
from visuals import *
import random
class Dealer:
    def __init__(self):
        self.current_cards = []
        self.is_out = False
        
    def deal_card(self):
        new_card = Card(random.choice(list(SUITS.keys())), random.choice(RANK))
        
        if new_card.rank in ["K", "J", "Q", "A"]:
            future_score = new_card.get_symbols_value(new_card.rank) + self.calculate_score()
        else:
            future_score = int(new_card.rank) + self.calculate_score()
        

        if self.is_out == False and future_score <= 17:
            self.current_cards.append(new_card)
        else:
            self.is_out = True 

    def print_dealer_cards_in_row(self, cards):
        # Split each card representation into lines
        card_lines = [card.draw_card().split("\n") for card in cards]

        # Print each row by combining corresponding lines of all cards
        for lines in zip(*card_lines):
            print("  ".join(lines))  # Join lines with spacing

        return "\nDealer's cards ⬆"
    
    def print_dealer_cards_hidden_in_row(self, cards):
        # Split each card representation into lines
        if len(self.current_cards) > 1:
            card_lines = [self.current_cards[0].draw_card().split("\n")] + [card.draw_deck().split("\n") for card in cards[1:]]
        else:
             card_lines = [card.draw_card().split("\n") for card in cards]

        # Print each row by combining corresponding lines of all cards
        for lines in zip(*card_lines):
            print("  ".join(lines))  # Join lines with spacing

        return "\nDealer's cards ⬆"

    
    def calculate_score(self):
        current_score = 0
        for card in self.current_cards:
            if current_score <= 17:
                if card.rank in ["K", "J", "Q"]:
                    symbol_value = card.get_symbols_value(card.rank)
                    current_score += symbol_value
                elif card.rank == "A":
                    future_score = current_score + 11
                    if future_score <= 17:
                        current_score += 11
                    else:
                        current_score += 1
                else:
                    current_score += int(card.rank)
            elif current_score > 17:
                self.is_out = True

        return current_score
        