# -*- coding: utf-8 -*-

from vice import Dict
from vice.plugins import Plugin

class Item(Plugin):
    ATTRIBUTES = None

    @classmethod
    def new(cls, name, attributes):
        return type(name, (cls,),
                    dict(NAME=name, ATTRIBUTES=tuple(set(attributes)))

    def __init__(self, *args, **kwargs):
        self.attributes = Dict()

        if hasattr(self.ATTRIBUTES, 'split'):
            attributes = Dict.fromkeys(self.ATTRIBUTES.split())
        elif hasattr(self.ATTRIBUTES, 'index'):
            attributes = Dict.fromkeys(self.ATTRIBUTES)
        else:
            attributes = Dict(self.ATTRIBUTES)

        for key, value in attributes.items():
            setattr(self, key, value)


class Card(Item):
    NAME = "Card"
    ATTRIBUTES = None

class Die(Item):
    NAME = "Die"
    ATTRIBUTES = "sides"
