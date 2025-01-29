from card import Card

def main():

    def print_cards_in_row(*cards):
        # Split each card representation into lines
        card_lines = [card.draw_card().split("\n") for card in cards]

        # Print each row by combining corresponding lines of all cards
        for lines in zip(*card_lines):
            print("  ".join(lines))  # Join lines with spacing


    card_one = Card("spade", "black", "A")
    card_two = Card("heart", "red", "10")
    card_three = Card("diamond", "red", "K")

    player_one = Card("spade", "black", "A")
    player_two = Card("heart", "red", "10")
    player_three = Card("diamond", "red", "K")

    print_cards_in_row(card_one, card_two, card_three)
    print_cards_in_row(player_one, player_two, player_three)










if __name__ == "__main__":
    main()