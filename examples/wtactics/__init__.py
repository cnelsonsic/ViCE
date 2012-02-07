import os
import sys

sys.path.insert(0, "/home/edwin/projects/python/vice/src")

from vice import database, Dict
from vice.plugins import Item

#TODO: separate plugins into separate files

class WTacticsCard(Item):
    ATTRIBUTES = ["title", "attack", "defense", "cost"]
