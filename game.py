from player import Player
from dealer import Dealer
from card import Card
import time

class Game:
    def __init__(self, player_name, player_bank):
        self.player = Player(player_name, player_bank)
        self.dealer = Dealer()

    def __give_cards(self):
        if self.player.is_out == False:
        #Give the player it's card if it's not out:
            self.dealer.deal_card(self.player)
        print("-------------------------------------------------------------------------------------")
        print(self.player.print_player_cards_in_row(self.player.current_cards))

        #Give the Dealer it's card
        self.dealer.deal_card(self.dealer)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(self.dealer.print_dealer_cards_in_row(self.dealer.current_cards))

    def __display_menu(self):
        print("\nWhat would you like to do now?")
        #check current bet
        print("1. Check your current bet")
        #check bank
        print("2. Check the total credit left")
        #ask for a new card
        print("3. Get a new card")
        #stand
        if self.player.is_out == False:
            print("4. Stand")
        #double the bet
        print("5. Double my bet, I'am feeling lucky")
        print("6. Check my score")

        menu_choice = input("\nChoose an optin (1-5):")
        time.sleep(1)

        if menu_choice == "1":
            print(f"\n Your current bet is {self.player.current_bet}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif menu_choice == "2":
            self.player.check_bank()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif menu_choice == "3":
            self.__give_cards()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif menu_choice == "4":
            self.player.stand()
            print(f"You won't receive any more cards until the round is over.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif menu_choice == "5":
            self.player.double_bet()
            print(f"Right now, your bet is {self.player.current_bet}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif menu_choice == "6":
            self.player.calculate_score()



    def play_round(self):
         #Place bet
        self.player.bet()
        print(f"\nYou have {self.player.bank} credit left.")

        #Show the deck:
        print("\n Ok, great, let's shuffle the deck.....")
        time.sleep(2)
        print(f"\n Now, that we shuffled the deck, let's see your first card.")
        time.sleep(2)
        #Give player and dealer one card each
        self.__give_cards()
        time.sleep(2)

        #Display the menu after each turn
        while True:
            self.__display_menu()

    def end_round():
        pass