# -*- coding: utf-8 -*-

from copy import deepcopy
from sqlobject import SQLObject
from sqlobject.col import UnicodeCol
from vice.plugins import Plugin

class Item(Plugin):
    ATTRIBUTES = None

    @classmethod
    def new(cls, name, attributes):
        return type(name, (cls,),
                    dict(NAME=name, ATTRIBUTES=tuple(set(attributes))))

    @classmethod
    def toSQLObject(cls, *col_list, **col_dict):
        attrs = deepcopy(cls.__dict__['ATTRIBUTES'])
        col_list = list(col_list)

        for attr in attrs:
            if not col_dict.get(attr):
                try:
                    col_dict[attr] = col_list.pop(0)
                except IndexError:
                    col_dict[attr] = UnicodeCol()


        return type(cls.__name__, (SQLObject,), col_dict)

class Die(Item):
    NAME = 'die'
    ATTRIBUTES = ['sides']
