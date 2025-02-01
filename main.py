from card import Card
from dealer import Dealer
from game import Game
from player import Player
from text import *

def main():
   
    player_name = input(f"\n{INPUT_NAME}  ")
    player_bank = int(input(f"\n{INPUT_MONEY}  "))
    game = Game(player_name, player_bank )

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    
    print(f"\n{game.player.name}{WELCOME}  ")
    knows_rules = input(f"\n{ASK_RULES} (yes or no) ")
    if knows_rules == "yes":
        print(f"\n{NO_RULES}")
    else:
        print(f"\n{RULES}")
        print(f"\n{AFTER_RULES}")


    while True:
        game.play_round()











if __name__ == "__main__":
    main()