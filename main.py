from card import Card
from dealer import Dealer
from game import Game
from player import Player
from text import *

def main():
   


    while True:
        player_name = input(f"\n {INPUT_NAME}")
        player_bank = int(input(f"\{INPUT_MONEY}"))
        game = Game(player_name, player_bank )
        print("-----------------------------")
        print(f"{game.player.name}, {WELCOME}")











if __name__ == "__main__":
    main()