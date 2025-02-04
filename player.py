class Player:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.current_cards = []
        self.current_bet = 0
        self.is_out = False
        self.over_limit = False
        self.current_score = 0

    def calculate_score(self):
        for card in self.current_cards:
            if self.current_score < 21:
                if card.rank in ["K", "J", "Q", "A"]:
                    symbol_value = card.get_symbols_value(card.rank)
                    self.current_score += symbol_value
                else:
                    self.current_score += int(card.rank)

        print(f"So far you got {self.current_score} score.")


    def add_to_score(self):
        if self.is_out == False and self.current_score < 21:
            if self.current_cards[len(self.current_cards)-1].rank in ["K", "J", "Q", "A"]:
                symbol_value = self.current_cards[len(self.current_cards)-1].get_symbols_value(self.current_cards[len(self.current_cards)-1].rank)
                self.current_score += symbol_value
            else:
                 self.current_score += int(self.current_cards[len(self.current_cards)-1].rank)
        else:
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