class Player:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.current_cards = []
        self.current_bet = 0
        

    def bet(self, amount):
        self.bank -= amount

    def ask_for_card(self):
        pass

    def check_bank(self):
        print(f"\n{self.name}, you have {self.bank} RON left.")

    def get_win_money(self, amount):
        self.bank+= amount

    