""" WTactics Items """
from vice.plugins.items import Item
from vice.plugins.containers import Container
from vice.plugins
from vice.database import Database

db = Database('wtactics.db')

# Items
Card = Item.fromTable('Card', 'cards', exclude=(
    'border_color', 'footer'
))
Token = Item.new('Token', attributes=(
    'owner', 'type_', 'target' # target is which card it is placed on
))

# Containers
class Zone(Container)
