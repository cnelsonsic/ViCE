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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with ViCE. If not, see <http://www.gnu.org/licenses/>.

import sqlite3
from functools import partial
from vice import PropertyDict

def property_dict_factory(cursor, row):
    """ Returns the cursor's row as a property dict."""

    return PropertyDict(
        (col[0], row[idx]) for idx, col in enumerate(cursor.description))


def column(name=None, kind='text', primary_key=False):
    """ Returns a string to be used as a column declaration for
        an SQL query with the given column name and type (kind).
    """

    query = '{name} {kind}'
    if primary_key:
        query += ' PRIMARY KEY'

    if name:
        return query.format(name=name, kind=kind)
    else:
        return partial(query.format, kind=kind)

""" Column Shortcuts """
text = partial(column, kind='text')
integer = partial(column, kind='integer')
real = partial(column, kind='real')
blob = partial(column, kind='blob')
null = partial(column, kind='null')

def comparison(value=None, column=None, operator='='):
    """ Returns a string to be used as a comparison declaration for an SQL
        query with the given value, column, and operator.
    """

    query = '{column} {operator} {value}'

    if column:
        return query.format(column=column, operator=operator, value=repr(value))
    else:
        return partial(query.format, operator=operator, value=repr(value))

""" Operator Shortcuts """
lt = partial(comparison, operator='<')
le = partial(comparison, operator='<=')
eq = partial(comparison, operator='=')
ge = partial(comparison, operator='>=')
gt = partial(comparison, operator='>')
ne = partial(comparison, operator='!=')

class Table(object):
    """ Abstraction layer on top of python's sqlite3 API.

        This class wraps python's sqlite3 API, providing a simple to use Table class.
    """
    def __init__(self, connection, table_name, columns=None, **kwargs):

        self._conn = connection
        self.name = table_name

        kwargs.update(columns or {})
        if kwargs:
            self._create_columns(kwargs)

    def __len__(self):
        cursor = self.execute("""SELECT count(*) from {name}""".format(
            name=self.name))

        return len(cursor.fetchall())

    def _create_columns(self, columns):
        columns = ', '.join(value(name=key) for key, value in columns.items())
        query = """CREATE TABLE if not exists {0}
                   ({1})""".format(self.name, columns)

        return self.execute(query)

    def insert(self, columns, **kwargs):
        """ Insert a new row into the database.

            Keyword arguemnts are understood to be key value  pairs
            representing the columns and their values respectively.
        """
        kwargs.update(columns or {})
        kwargs.update((key, value) for key, value in columns.items()
            if key not in kwargs)

        query = """INSERT INTO {table}
                ({columns})
                VALUES ({values})""".format(
            table=self.name,
            columns=', '.join(str(key) for key in kwargs.keys()),
            values=', '.join(repr(value) for value in kwargs.values()))

        return self.execute(query)

    def select(self, comparisons=None, **kwargs):
        """ Select rows from the database.

            If no arguments are given, every row is returned. Positional
            arguemnts are understood to be column names (in alphabetical order),
            where as keyword arguemnts are
            understood to be key value  pairs representing the columns and their
            values respectively.

            Comparison functions (lt, le, eq, gt, ge, ne) pay be passed as
            keyword values in order to broaden query results::

                db.cards.select({
                    'def': gt(2),
                    'atk': ge(3),
                    'type': 'Elf'})
        """
        kwargs.update(comparisons or {})

        if not kwargs:
            query = """SELECT *
                       FROM {table}""".format(table=self.name)
        else:
            kwargs.update(
                dict((key, eq(value)) for key, value in kwargs.items()
                    if not callable(value)))

            comparisons = ' AND '.join(
                value(column=key) for key, value in kwargs.items())

            query = """SELECT *
                    FROM {table}
                    WHERE {comparisons}""".format(
                        table=self.name, comparisons=comparisons)

        return self.execute(query)

    def execute(self, query, *args, **kwargs):
        return self._conn.execute(query, *args, **kwargs)

    @property
    def info(self):
        """ Returns a dictionary of columns and their attributes.

            Each column holds the following attributes:

                index
                    The column's index

                type
                    The column's type (text, integer, real, blob, null)

                null_allowed
                    Whether or not a null (None) value is allowed in the column

                default
                    The default value of the column, if there is one

                primary_key
                    Whether or not the column is a primary key
        """

        # name, type, null, default, primary_key
        columns = self.execute(
            "PRAGMA table_info({0})".format(self.name)).fetchall()

        return dict(
            (column.name, {
                'index': column.cid,
                'type': column.type,
                'null_allowed': bool(column.notnull),
                'default': column.dflt_value,
                'primary_key': bool(column.pk)})
            for column in columns)

    @property
    def columns(self):
        """ Returns a list of column names """
        return self.info.keys()

    @property
    def primary_key(self):
        """ Returns the table's primary key """

        for key, value in self.info.items():
            if value['primary_key']:
                return key


class Database(object):
    """ Abstraction layer on top of python's sqlite3 API.

        This class wraps python's sqlite3 API, providing a simple to use Database class.
    """

    def __init__(self, location=':memory:'):
        self.location = location
        self._conn = sqlite3.connect(self.location)
        self._conn.isolation_level = None # autocommit mode
        self._conn.row_factory = property_dict_factory #sqlite3.Row

    def __getattr__(self, name):
        if name in self.tables:
            return Table(self._conn, name)
        else:
            raise AttributeError(
                "'Database' object has no attribute '{0}'".format(name))

    def create_table(self, table_name, columns=None, **kwargs):
        """ Create a table in the database named table_name with columns whose
            name and value correspond to the keys and values of kwargs.

            table_name may be anything you wish, but if you wish to use names
            that collide with reserved words in Python (eg. 'def' or 'id'),
            simply pass a dictionary instead::
                db.create_table('cards', {
                    'id': integer(primary_key=True),
                    'name': text(),
                    'atk': integer(),
                    'def': integer()})
        """

        kwargs.update(columns or {})

        return Table(self._conn, table_name, **kwargs)

    def rename_table(self, old_name, new_name):
        """ Renames a table """
        query = """ALTER TABLE {old_name}
                   RENAME TO {new_name}""".format(
                        old_name=str(old_name), new_name=repr(new_name))

        return self.execute(query)

    def drop(self, table_name):
        """ Removes an existing table from the database. """
        query = """DROP TABLE {table}""".format(table=table_name)

        return self.execute(query)

    def execute(self, query, *args, **kwargs):
        """ Provides low-level access to Python's sqlite3 API.

            Functions identically to the sqlite3.Connection.execute() and uses
            the Connection object instatiated when the Database object was
            first created.
        """

        return self._conn.execute(query, *args, **kwargs)

    @property
    def tables(self):
        """ Returns a list of the database's table names. """
        cursor = self.execute("""SELECT name from sqlite_master
                                        WHERE type = 'table'""")

        return [row.name for row in cursor]
