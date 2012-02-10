import os
import sys

sys.path.insert(0, "/home/edwin/projects/python/vice/src")

from vice import database, Dict
from vice.plugins import Item

#TODO: separate plugins into separate files

class WTacticsCard(Item):
    NAME = 'WTacticsCard'
    ATTRIBUTES = ["title", "attack", "defense", "cost"]

WtCard = WTacticsCard.new('WtCard', ['title', 'attack', 'defense', 'cost'])
