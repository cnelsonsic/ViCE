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

def string(**kwargs):
    kwargs.update({'type_': sqlalchemy.String})

    return kwargs

def integer(**kwargs):
    kwargs.update({'type_': sqlalchemy.Integer})

    return kwargs

class Database(object):
    def __init__(self, URI=None, echo=False):
        self.metadata = sqlalchemy.MetaData()
        if URI:
            self.connect(URI, echo)
        else:
            self.engine = None

    @property
    def tables(self):
        return self.metadata.tables.keys()

    def connect(self, URI, echo=False):
        self.engine = sqlalchemy.create_engine(URI, echo=echo)
        self.metadata.reflect(bind=self.engine)

        for table in self.tables:
            setattr(self, table, self.metadata.tables[table])

    def create_table(self, table_name, column_attrs):
        if table_name in self.tables:
            return

        columns = []

        for attr in column_attrs.keys():
            columns.append(sqlalchemy.Column(attr.rstrip('_'),
                **column_attrs[attr.rstrip('_')]
            ))

        setattr(self, table_name,
            sqlalchemy.Table(table_name, self.metadata, *columns
        ))

        self.metadata.create_all(self.engine)

    def insert(self, table_name, **kwargs):
        values = {key.rstrip('_'): value for key, value in kwargs.items()}
        insert = getattr(self, table_name).insert().values(**values)
        connection = self.engine.connect()

        return connection.execute(insert)

    def select(self, tables, **kwargs):
        kwargs = {key.rstrip('_'): value for key, value in kwargs.items()}

        if hasattr(tables, '__iter__'):
            tables = [getattr(self, table) for table in tables]
        else:
            tables = [getattr(self, tables)]

        select = sqlalchemy.sql.select(tables, **kwargs)
        connection = self.engine.connect()

        return connection.execute(select)
