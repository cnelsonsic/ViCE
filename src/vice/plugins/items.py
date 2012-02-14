# -*- coding: utf-8 -*-

from vice.plugins import Plugin

class Item(Plugin):
    ATTRIBUTES = None

    @classmethod
    def new(cls, name, attributes):
        return type(name, (cls,),
                    dict(NAME = name.lower(), ATTRIBUTES=attributes))

    def __init__(self, *args, **kwargs):
        self.attributes = Dict()
        if hasattr(self.ATTRIBUTES, 'split'):
            attributes = Dict.fromkeys(self.ATTRIBUTES.split())
        elif hasattr(self.ATTRIBUTES, 'index'):
            attributes = Dict.fromkeys(self.ATTRIBUTES)
        else:
            attributes = Dict(self.ATTRIBUTES)

        for key, value in attributes.iteritems():
            setattr(self, key, value)


class Card(Item):
    ATTRIBUTES = None

class Die(Item):
    ATTRIBUTES = "sides"
