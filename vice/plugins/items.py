# -*- coding: utf-8 -*-

from copy import deepcopy
from sqlobject import SQLObject
from sqlobject.col import UnicodeCol
from vice import Dict
from vice.plugins import Plugin

class Item(Plugin):
    ATTRIBUTES = None

    @classmethod
    def new(cls, name, attributes):
        return type(name, (cls,),
                    dict(NAME=name, ATTRIBUTES=tuple(set(attributes))))

    @classmethod
    def toSQLObject(cls, *colList, **colDict):
        attrs = deepcopy(cls.__dict__['ATTRIBUTES'])
        colList = list(colList)

        for attr in attrs:
            if not colDict.get(attr):
                try:
                    colDict[attr] = colList.pop(0)
                except IndexError:
                    colDict[attr] = UnicodeCol()


        return type(cls.__name__, (SQLObject,), colDict)

class Die(Item):
    NAME = 'die'
    ATTRIBUTES = ['sides']
