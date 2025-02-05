from card import Card
import random
from visuals import *

class Player:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.current_cards = []
        self.current_bet = 0
        self.is_out = False
        self.over_limit = False
        self.win_condition = False

    def calculate_score(self):
        current_score = 0
        for card in self.current_cards:
            if current_score < 21:
                if card.rank in ["K", "J", "Q"]:
                    symbol_value = card.get_symbols_value(card.rank)
                    current_score += symbol_value
                elif card.rank == "A":
                    print("You got an ACE, it can be 1 or 11.")
                    choice = input("Type your choice (1 or 11):")
                    current_score += int[choice]
                else:
                    current_score += int(card.rank)
            elif current_score > 21:
                self.is_out == True
                self.over_limit == True
            elif current_score == 21:
                self.win_condition = True

        return current_score
    
    def deal_card(self):
        new_card = Card(random.choice(list(SUITS.keys())), random.choice(RANK))
        if new_card.rank in ["K", "J", "Q"]:
            future_score = new_card.get_symbols_value(new_card.rank) + self.calculate_score()
        elif new_card.rank == "A":
            print("You just received an ACE, it can be 1 or 11.")
            choice = input("Type your choice (1 or 11):")
            future_score = int(choice) + self.calculate_score()
        else:
            future_score = int(new_card.rank) + self.calculate_score()

        if self.is_out == False and future_score <= 21 :
            self.current_cards.append(new_card)
        else:
            self.is_out = True
            self.over_limit = True

    def bet(self):
        bet_amount = int(input(f"\nPlease place your bet:"))
        self.current_bet = bet_amount
        if bet_amount > self.bank:
            print(f"\n You don't have enough credit.")
            return
        else:
            self.bank -= bet_amount

    def double_bet(self):
        if  self.bank -  self.current_bet*2 > 0:
            self.bank -= self.current_bet
            self.current_bet*= 2
        else:
            print("You don't have enough money to double your bet.")

    def stand(self):
        self.is_out = True

    def check_bank(self):
        print(f"\n{self.name}, you have {self.bank} CREDIT left.")

    def get_win_money(self, amount):
        self.bank+= amount

    def print_player_cards_in_row(self, cards):
        # Split each card representation into lines
        card_lines = [card.draw_card().split("\n") for card in cards]

        # Print each row by combining corresponding lines of all cards
        for lines in zip(*card_lines):
            print("  ".join(lines))  # Join lines with spacing

        return "\nYour cards ⬆"