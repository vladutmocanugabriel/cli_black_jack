from player import Player
from dealer import Dealer
from card import Card

class Game:
    def __init__(self, player_name, player_bank):
        self.player = Player(player_name, player_bank)
        self.dealer = Dealer()

    def end_round():
        pass

    def give_cards(self):
        #Give the player it's card
        self.dealer.deal_card(self.player)
        print("-------------------------------------------------------------------------------------")
        print(f"\nThe dealer is giving the player a card:")
        print(self.player.print_player_cards_in_row(self.player.current_cards))

        #Give the Dealer it's card
        self.dealer.deal_card(self.dealer)
        print("-------------------------------------------------------------------------------------")
        print(f"\nThe dealer is getting a card:")
        print(self.dealer.print_dealer_cards_in_row(self.dealer.current_cards))

        #Place bet
        self.player.bet()
        print(f"\nYou have {self.player.bank} credit left.")

        #Show the deck:
        print("\n Ok, great, let's shuffle the deck...")
        deck = Card("diamond", 5)
        print(f"{deck.draw_deck()}")
        print(f"\n Now, that we shuffled the deck, let's see your first card.")

    def play_round(self):
        self.give_cards()