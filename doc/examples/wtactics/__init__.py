import os, sys
sys.path..insert(0, os.path.join(os.path.abspath("..", ",,", "src")))

from vice import database
from vice.plugins.items import Item
from vice.plugins.schemes import FlatFileScheme

from wtactics.items import WtCard

# create flat-file database cwd
db = database.connect('flat-file')

# create a table called cards with fields name, attack, and defense
#db.create_table('cards', 'name', 'attack', 'defense')
db.create_table("cards", *WtCard.ATTRIBUTES)

# add a record to the databse
db.create_record('cards',
    name = 'foo',
    attack = 5,
    defense = 6
)
