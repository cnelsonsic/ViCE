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

import sqlalchemy

class PropertyDict(dict):
    """ A dict subclass that allows values to be retrieved by accessing their
        keys as properties.

        PropertyDict provides a dictionary whose key:value pairs may be
        assigned in the conventional brace notation (foo['bar'] = 'baz'),
        or in the more elegant object:property notation (foo.bar = 'baz').
        Beyond this subtle addition, they behave identically to regular
        dictionaries.
    """

    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

    def __getattr__(self, name):
        return self.get(name, None)

class Database(object):
    def __init__(self, URI=None, verbose=False):
        self.metadata = sqlalchemy.MetaData()
        if URI:
            self.engine = self.connect(URI, verbose)
        else:
            self.engine = None

    @property
    def tables(self):
        return self.metadata.tables.keys()

    def connect(self, URI, verbose=False):
        return sqlalchemy.create_engine(URI, echo=verbose)

    def create_table(self, name, column_names, column_attrs):
        column_names = list(column_names)
        columns = []

        for attr in column_attrs.keys():
            columns.append(sqlalchemy.Column(attr, **column_attrs[attr]))

        for column in column_names:
            if column not in column_attrs.keys():
                columns.append(sqlalchemy.Column(name, sqlalchemy.String))

        self.setattr(self, name, sqlalchemy.Table(name, self.metadata, *columns))
        self.metadata.create_all(self.engine)

    def insert(name, **kwargs):
        insert = getattr(self, name).insert().values(**kwargs)
        connection = engine.connect()
        return connection.execute(insert)

    def string(self, **kwargs):
        kwargs.update({'type_': sqlalchemy.String})

        return kwargs

    def integer(self, **kwargs):
        kwargs.update({'type_': sqlalchemy.Integer})

        return kwargs
