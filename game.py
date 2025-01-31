from player import Player
from dealer import Dealer

class Game:
    def __init__(self, player_name, player_bank):
        self.player = Player(player_name, player_bank)
        self.dealer = Dealer()

    def end_round():
        pass

    def print_player_cards_in_row(*cards):
        # Split each card representation into lines
        card_lines = [card.draw_card().split("\n") for card in cards]

        # Print each row by combining corresponding lines of all cards
        for lines in zip(*card_lines):
            print("  ".join(lines))  # Join lines with spacing

    def print_dealer_cards_in_row(*cards):
        # Split each card representation into lines
        card_lines = [card.draw_card().split("\n") for card in cards]

        # Print each row by combining corresponding lines of all cards
        for lines in zip(*card_lines):
            print("  ".join(lines))  # Join lines with spacing

    