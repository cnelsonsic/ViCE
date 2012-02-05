from . import Item, Dict

class Card(Item):
    stored = True
    fields = Dict(
        title = "Title",
        cost = "Cost",
        types = "Card Types",
        expansion = "Card Set",
        text = "Card Text",
        uid = "Card Number"
    )
