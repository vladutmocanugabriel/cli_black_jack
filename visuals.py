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