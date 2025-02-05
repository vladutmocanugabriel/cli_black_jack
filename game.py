from player import Player
from dealer import Dealer
from card import Card
import time

class Game:
    def __init__(self, player_name, player_bank):
        self.player = Player(player_name, player_bank)
        self.dealer = Dealer()
        self.round_finished = False

    def __give_cards(self):
        #Give the player it's card if it's not out:
        self.player.deal_card()
        print("-------------------------------------------------------------------------------------")
        print(self.player.print_player_cards_in_row(self.player.current_cards))

        #Give the Dealer it's card and start counting score
        self.dealer.deal_card()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if (self.player.is_out == False and self.player.over_limit == False) and len(self.dealer.current_cards)>1:
            print(self.dealer.print_dealer_cards_hidden_in_row(self.dealer.current_cards))
        else:
            print(self.dealer.print_dealer_cards_in_row(self.dealer.current_cards))

        print("####")
        print(f"Player: {self.player.calculate_score()}")
        print(f"Dealer: {self.dealer.calculate_score()}")
        print("####")

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
            self.player.calculate_score()
            self.dealer.calculate_score()
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
            print(f"Your score at the moment is: {self.player.calculate_score()}")

    def end_roud_check(self):
        if (self.player.is_out and self.player.over_limit) or self.player.win_condition:
            self.round_finished = True

    def check_win_condition(self):
        if self.player.win_condition == True:
            self.round_finished = True


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
                if self.round_finished == False and self.player.win_condition == False:
                    print(f"Round is finished is: {self.round_finished}")
                    print(f"Player is out is: {self.player.is_out}")
                    print(f"Player is over the limit is: {self.player.over_limit}")
                    print(f"Dealer is out: {self.dealer.is_out}")
                    print(f"Win condition is: {self.player.win_condition}")
                    self.__display_menu()
                    self.check_win_condition
                    self.end_roud_check()
                else:
                    break
        if self.player.win_condition:
            print(f"{self.player.name} got THE BLACK JACK with 21")
        else:
            print("The game ENDED! WEll done everyone!")