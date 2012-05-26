# -*- coding: utf-8 -*-

# Copyright (C) 2011-2012 Edwin Marshall <emarshall85@gmail.com>
#
# This file is part of ViCE.
#
# ViCE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ViCE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with ViCE.  If not, see <http://www.gnu.org/licenses/>.

from vice.plugins import Plugin

class Item(Plugin):
    """ Plugin that represents a games tangible objects.

        An item is any object within a card game that can be interacted
        with. The most obvious example of this would be the game's cards,
        but things such as tokens and dice would be implemented as items
        as well.

        To create a new item, define a new Item subclass, override the NAME
        attribute (by convention, uppercase for items), and finally override
        ATTRIBUTES with a sequence of strings::

            class Card(Item):
                NAME = 'Card'
                ATTRIBUTES = 'name', 'atk', 'def'

        Alternatively, you may pass an appropriate name and attributes to
        Item.new::

            Dice = Item.new('Dice', ('name', 'atk', 'def'))

        As another alternative, you may pass an appropriate name, valid
        database table and an optional exclude sequence to Item.fromTable::

            db = vice.database.Database('sqlite:///wtactics.sqlite')
            Card = Item.fromTable('Card', db.cards, exclude=['id'])

        On instantiation, the values of ATTRIBUTES are converted to properties
        of the plugin instance. These properties are semi-immutable. That is,
        on instantiating of an item plugin, you may change the value of existing
        attributes, but you may not create new ones. If you wish to do so, you
        should add the new attribute to ATTRIBUTES when defining the class.
    """

    ATTRIBUTES = None

    def __init__(self):
        for attribute in self.ATTRIBUTES:
            self.__dict__[attribute] = None

    @classmethod
    def new(cls, name, attributes):
        """ Convenience method used to help simplify the creation of new items. """
        return type(name, (cls,),
                    dict(NAME=name, ATTRIBUTES=tuple(set(attributes))))

    @classmethod
    def fromTable(cls, name, table, exclude=None):
        """ Convenience method used to create new items from database tables. """
        attributes = [
            column.name for column in table.columns
            if column.name not in exclude
        ]

        return cls.new(name, attributes)

    def __setattr__(self, name, value):
        if name in self.__dict__:
            super(Item, self).__setattr__(name, value)
