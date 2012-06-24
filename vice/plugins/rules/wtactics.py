""" WTactics Plugin Prototype

    This module is an example of how to write a rules plugin for ViCE.
    Currently, it is contained within a single file. However, as plugins are
    really just python files, the different bits could be extracted into
    separate modules (actions, containers, items, etc) and packaged as a single
    python package.
"""
from vice.plugins import Item, Container, Action
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
class Zone(Container):
    def constraints(self, item):
        return [
            item.NAME = 'Card'
        ]
