""" WTactics Plugin Prototype

    This module is an example of how to write a rules plugin for ViCE.
    Currently, it is contained within a single file. However, as plugins are
    really just python files, the different bits could be extracted into
    separate modules (actions, containers, items, etc) and packaged as a single
    python package.
"""
from vice.plugins import Item, Container, Action
from vice.database import Database

# opens a local db file
db = Database('sqlite:///wtactics.db')

# Items
Item.from_table('Card', db.cards, exclude=(
    'border_color', 'footer'
))

Item.new('Token', attributes=(
    'owner', 'type_', 'target' # target is which card it is placed on
))

# Containers
Zone = Container.new('Zone', lambda cls, item: [
    item.NAME == 'Card',
])

for zone in 'Questing', 'Offensive', 'Defensive':
    Zone.new('{0}Zone'.format(zone), lambda cls, item:
        Zone.constraints(cls, item) + [
           zone.lower() in item.types
    ])

HeroZone = Zone.new('HeroZone', lambda cls, item:
    Zone.constraints(cls, item) + [
        len(cls) == 1
])

# register the plugins
actions = Action.plugins()
containers = Container.plugins()
items = Item.plugins()
