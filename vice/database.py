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
    """ Returns a kwargs dictionary suitable for creating an SQLAlchemy
        String column.
    """

    kwargs.update({'type_': sqlalchemy.String})

    return kwargs

def integer(**kwargs):
    """ Returns a kwargs dictionary suitable for creating an SQLAlchemy
        Integer column.
    """

    kwargs.update({'type_': sqlalchemy.Integer})

    return kwargs

class Database(object):
    """ Abstraction layer on top of SQLAlchemy's interface.

        While SQLAlchemy abstracts the particulars of different
        database backends and the subtle ways SQL may differ within them,
        this Database class abstracts the SQLAlchemy API into something more
        simple, meanwhile adding facilities that make it integrate better with
        ViCE's plugin architecture.
    """

    def __init__(self, URI=None, echo=False):
        """ Instantiate a new database object, calling connect if a valid URI
            is given.
        """

        self.metadata = sqlalchemy.MetaData()
        if URI:
            self.connect(URI, echo)
        else:
            self.engine = None

    @property
    def tables(self):
        """ Returns a list of table names for the current database object. """
        return self.metadata.tables.keys()

    def connect(self, URI, echo=False):
        """ Connects to an existing database, or creates a new one if one
            isn't found.

            URI may be any URI recognized by SQLAlchemy, and generally follows
            the form::

                "<protocol>:///<location>"

            For example::

                "sqlite:///wtactics.db"

            echo determines whether or not SQL statements are echoed to stdout
            after each operation.
        """

        self.engine = sqlalchemy.create_engine(URI, echo=echo)
        self.metadata.reflect(bind=self.engine)

        for table in self.tables:
            setattr(self, table, self.metadata.tables[table])

    def create_table(self, table_name, column_attrs):
        """ Creates a table in the database named table_name, with columns
            whose attributes match column_attrs.

            table_name may be anything you wish, but if it so happens to be a
            reserved word in Python (eg. 'def'), then you must suffix it with
            an underscore ('_'). You needn't worry, however, since the
            trailing underscore is removed inside the actual database.

            All remaining keyword arguments will be processed as column
            attributes where the keys should be valid column names, and the values
            should be arguments to column types.

            Valid column types are currently:
                * string() -- Represents an string column.
                * integer() -- Represents an integer column .

            Arguments may be passed to these column types to further specify
            restrictions on data or relationships.

            Valid arguments are currently:
                primary_key=True -- Marks the column as the primary key.

            Example::

                db.create_table('cards', dict(
                    id = integer(primary_key=True),
                    name = string(),
                    atk = integer(),
                    def_ = integer() # notice the trailing underscore
                ))

            .. note::
                Since column_attrs is a dictionary, definition order is
                arbitrary, and thus the order in which the columns is
                specified may differ from what you expect when examining the
                resulting database. If column order is important, pass
                column_attrs as a `collections.OrderedDict` instead.
        """
        if table_name in self.tables:
            return

        columns = (sqlalchemy.Column(attr.rstrip('_'), **column_attrs[attr])
                   for attr in column_attrs.keys())

        setattr(self, table_name,
            sqlalchemy.Table(table_name.rstrip('_'), self.metadata, *columns
        ))

        self.metadata.create_all(self.engine)

    def create_record(self, table_name, parameters):
        """ Creates a record in table_name, using parameters.

            Example::

                db.create_record('cards', dict(
                    # note that id is auto-incremented, so isn't specified
                    name = 'Imp',
                    atk = 2,
                    def_ = 2
                ))
        """
        parameters = {key.rstrip('_'): value
                      for key, value in parameters.items()}
        insert = getattr(self, table_name).insert().values(**parameters)
        connection = self.engine.connect()

        return connection.execute(insert)

    def select(self, tables, **kwargs):
        """ Selects all records of the given tables.

            tables is a list of table names.

            .. warning::
                The interface is mostly ported directly from SQLAlchemy. In
                the future, a simpler interface will be implemented, most
                probably named "find", and this one will be deprecated for
                immediate removal.
        """

        kwargs = {key.rstrip('_'): value for key, value in kwargs.items()}

        if not hasattr(tables, 'join'):
            tables = [getattr(self, table) for table in tables]
        else:
            tables = [getattr(self, tables)]

        select = sqlalchemy.sql.select(tables, **kwargs)
        connection = self.engine.connect()

        return connection.execute(select)

    def drop_table(self, table_name):
        """ Drops the given table from the database.

            If the table doesn't exist in the database, an AttributeError is
            raised.

            Example::

                db.drop('cards')
        """

        if table_name not in self.tables:
            raise AttributeError(u"Table '{0}' does not exist".format(table_name))

        # Drop the table.
        getattr(self, table_name).drop(self.engine)
        self.metadata.clear()
        self.metadata.reflect(self.engine)
        
    def rename_table(self, old_name, new_name):
        """ Changes the name of a table.
        
            Example::
            
                db.rename_table('cards', 'items')
        """
        if old_name == new_name:
            return
        if old_name not in self.tables:
            raise AttributeError(u'No “{0}” table found'.format(old_name))
        if new_name in self.tables:
            raise AttributeError(u'Table “{0}” already exists'.format(new_name))
        
        connection = self.engine.connect()
        sentence = u'ALTER TABLE {0} RENAME TO {1}'.format(old_name, new_name)
        connection.execute(sentence)
        self.metadata.clear()
        self.metadata.reflect(self.engine)
