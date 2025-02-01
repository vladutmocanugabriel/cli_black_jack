class Player:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.current_cards = []
        
        self.current_bet = 0

    def bet(self):
        bet_amount = int(input(f"\nPlease place your bet:"))
        if bet_amount > self.bank:
            print(f"\n You don't have enough credit.")
            return
        else:
            self.bank -= bet_amount

    def ask_for_card(self):
        pass

    def check_bank(self):
        print(f"\n{self.name}, you have {self.bank} RON left.")

    def get_win_money(self, amount):
        self.bank+= amount

    def print_player_cards_in_row(self, cards):
        # Split each card representation into lines
        card_lines = [card.draw_card().split("\n") for card in cards]

        # Print each row by combining corresponding lines of all cards
        for lines in zip(*card_lines):
            print("  ".join(lines))  # Join lines with spacing