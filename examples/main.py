import sys
sys.path.insert(0, "/home/edwin/projects/python/vice/src")

from vice import database
from vice.plugins import Item
from vice.plugins.schemes import FlatFileScheme
from wtactics import WTacticsCard as Card
from wtactics import WtCard as Card2

"""
# create flat-file database cwd
db = database.connect('flat-file')

# create a table called cards with fields name, attack, and defense
#db.create_table('cards', 'name', 'attack', 'defense')
#db.create_table("cards", *Card.ATTRIBUTES)

# add a record to the databse
db.create_record('cards',
    name = 'foo',
    attack = 5,
    defense = 6
)
"""

# test two styles of creating an item plugin
items = Item.plugins().keys()
cards = Card.plugins().keys()

print items
print cards
