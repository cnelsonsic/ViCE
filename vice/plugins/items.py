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

from copy import deepcopy
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

            class Dice(Item):
                NAME = 'Dice'
                ATTRIBUTES = 'sides',

        Alternatively, you may pass an appropriate name and attributes to
        Item.new::

            Item.new("Dice", ('sides',))

        On instantiation, the values of ATTRIBUTES are converted to properties
        of the plugin instance. These properties are semi-immutable. That is,
        on instantiating of an item plugin, you may change the value of existing
        attributes, but you may not create new ones. If you whish to do so, you
        should add the new attribute to ATTRIBUTES when defining the class.
    """

    ATTRIBUTES = None

    def __init__(self):
        for attribute in self.ATTRIBUTES:
            self.__dict__[attribute] = None

    @classmethod
    def new(cls, name, attributes):
        """ Convenience method used to help simplify the creation of new items."""
        return type(name, (cls,),
                    dict(NAME=name, ATTRIBUTES=tuple(set(attributes))))

    def __setattr__(self, name, value):
        if self.__dict__.get(name):
            self.__dict__[name] = value
