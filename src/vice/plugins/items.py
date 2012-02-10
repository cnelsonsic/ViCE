# -*- coding: utf-8 -*-

from vice.plugins import Item, Dict

class Card(Item):
    NAME = 'card'
    ATTRIBUTES = "title cost types expansion text uid"

class Card(Item):
    ATTRIBUTES = "title", "cost", "types", "expansions", "text", "uid"

class Die(Item):
    ATTRIBUTES = "sides"
