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

from sqlobject import SQLObject
from sqlobject.col import UnicodeCol

from vice.plugins import Plugin

class Item(Plugin):
    ATTRIBUTES = None

    def __init__(self):
        for attribute in self.ATTRIBUTES:
            self.__dict__[attribute] = None

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

    def __setattr__(self, name, value):
        if self.__dict__.get(name):
            self.__dict__[name] = value
