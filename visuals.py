SUITS = {
        "diamond": "♦",
        "heart": "♥",
        "spade": "♠",
        "club": "♣"
    }

COLORS = {
        "black": "black",
        "red": "red"
    }

RANK = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]

    # ASCII art for card faces and backs
FACE_TEMPLATE = [
        "┌─────────┐",
        "│{rank}{spacing}│",
        "│         │",
        "│         │",
        "│    {suit}    │",
        "│         │",
        "│         │",
        "│{spacing}{rank}│",
        "└─────────┘"
    ]

BACK_TEMPLATE = [
        "┌─────────┐", 
        "│▓▓▓▓▓▓▓▓▓│",
        "│▓▓▓▓▓▓▓▓▓│",
        "│▓░▓▓▓▓▓░▓│", 
        "│▓▓░▓▓▓░▓▓│", 
        "│▓▓▓░░░▓▓▓│", 
        "│▓▓░▓▓▓░▓▓│", 
        "│▓░▓▓▓▓▓░▓│", 
        "│▓▓▓▓▓▓▓▓▓│",
        "└─────────┘",
    ]