import os, sys
sys.path.insert(0, os.path.abspath(os.path.join("..", "..", "src")))

from vice.plugins.items import Card

class WtCard(Card):
    NAME = "WtCard"
    ATTRIBUTES = (
        "art", "border_color", "cost", "faction", "footer",
        "loyalty", "name", "text", "types", "stats"
    )
