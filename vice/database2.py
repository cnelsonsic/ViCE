import sqlite3
from collections import OrderedDict
from functools import partial
from vice import PropertyDict


def property_dict_factory(cursor, row):
    pd = PropertyDict()
    for idx, col in enumerate(cursor.description):
        pd[col[0]] = row[idx]

    return pd


def column(kind='text', name=None, primary_key=False):
    query = '{name} {kind}'
    if primary_key:
        query += ' PRIMARY KEY'

    if name:
        return query.format(name=name, kind=kind)
    else:
        return partial(query.format, kind=kind)

text = partial(column, kind='text')
integer = partial(column, kind='integer')
real = partial(column, kind='real')
blob = partial(column, kind='blob')
null = partial(column, kind='null')


class Table(object):
    def __init__(self, connection, table_name, **kwargs):
        self._conn = connection
        self.name = table_name

        if kwargs.get('columns'):
            self._create_columns(kwargs['columns'])
        elif kwargs:
            self._create_columns(kwargs)

    def __len__(self):
        cursor = self._conn.execute("""SELECT count(*) from {name}""".format(
            name=self.name))

        return len(cursor.fetchall())

    def _create_columns(self, columns):
        columns = ', '.join(value(name=key) for key, value in columns.items())
        query = """CREATE TABLE if not exists {0}
                   ({1})""".format(self.name, columns)

        return self._conn.execute(query)

    def insert(self, *args, **kwargs):
        columns = dict(zip(self.columns, args))
        kwargs.update((key, value) for key, value in columns.items()
            if key not in kwargs)

        query = """INSERT INTO {table}
                ({columns})
                VALUES ({values})""".format(
            table=self.name,
            columns=', '.join(str(key) for key in kwargs.keys()),
            values=', '.join(repr(value) for value in kwargs.values()))

        return self._conn.execute(query)

    def select(self, *args, **kwargs):
        if not args and not kwargs:
            query = """SELECT *
                       FROM {table}""".format(table=self.name)
        else:
            columns = OrderedDict(zip(self.columns, args))
            kwargs.update((key, value) for key, value in columns.items()
                if key not in kwargs)

            columns = ", ".join(["{key} = {value}".format(key=key, value=value)
                for key, value in kwargs.items()])

            query = """SELECT *
                       FROM {table}
                       WHERE {columns}""".format(table=self.name, columns=columns)

        return self._conn.execute(query)

    @property
    def info(self):
        # name, type, null, default, primary_key
        columns = self._conn.execute(
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
        return self.info.keys()

    @property
    def primary_key(self):
        for key, value in self.info.items():
            if value['primary_key']:
                return key


class Database(object):

    text = text
    integer = integer
    real = real
    blob = blob
    null = null

    def __init__(self, location=':memory:'):
        self.location = location
        self._conn = sqlite3.connect(self.location)
        self._conn.isolation_level = None # autocommit mode
        self._conn.row_factory = property_dict_factory #sqlite3.Row

    def __getattr__(self, name):
        if name in self.tables:
            return Table(self._conn, name)

    def create_table(self, table_name, **kwargs):
        return Table(self._conn, table_name, **kwargs)

    @property
    def tables(self):
        cursor = self._conn.execute("""SELECT name from sqlite_master
                                        WHERE type = 'table'""")

        return [row.name for row in cursor]
