from visuals import *
from text import *

class Card:
    def __init__(self, suit, color, rank):
        self.suit = suit
        self.color = color
        self.rank = rank



    def get_symbols_value(symbol):
        if symbol=="K":
            return 10
        elif symbol == "J":
            return 10
        elif symbol == "Q":
            return 10
        elif symbol == "A":
            choice = input(f"\n{ACE_INFO} (1 or 11)")
            if choice == "1":
                return 1
            elif choice == "11":
                return 11


    def draw_card(self, height=0):
        suit_icon = self._get_suit_icon()
        spacing = " " * (len(FACE_TEMPLATE[0]) - len(self.rank) - 2)

        return self._build_card_string(FACE_TEMPLATE, height)\
            .replace("{suit}", suit_icon)\
            .replace("{rank}", self.rank)\
            .replace("{spacing}", spacing)

    def draw_deck(self, height=0):
        return self._build_card_string(BACK_TEMPLATE, height)

    def _get_suit_icon(self):
        if self.suit == "diamond":
            return "♦" if self.color == "black" else "♢"
        elif self.suit == "heart":
            return "♥" if self.color == "black" else "♡"
        elif self.suit == "spade":
            return "♠" if self.color == "black" else "♤"
        elif self.suit == "club":
            return "♣" if self.color == "black" else "♧"
        else:
            return self.suit[0]  # Default: first character of suit name

    def _build_card_string(self, template, height):
        result = []
        for row in template:
            if height > 0:
                prefix = row[0] * height
                result.append(f"{prefix}{row}")
            elif height < 0:
                postfix = row[-1] * abs(height)
                result.append(f"{row}{postfix}")
            else:
                result.append(row)
        return "\n".join(result)
