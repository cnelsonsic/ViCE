import sqlite3
from functools import partial

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

class Row(object):
    def __init__(self, connection, table, **kwargs):
        self._conn = connection
        self._table = table

        query = """INSERT INTO {table}
                   ({columns})
                   VALUES ({values})""".format(
            table=self._table,
            columns=', '.join(repr(key) for key in kwargs.keys()),
            values=', '.join(repr(value) for value in kwargs.values()))

        self._conn.execute(query)


class Table(object):
    def __init__(self, connection, name, columns=None):
        self._conn = connection
        self.name = name

        if columns:
            self.create_columns(columns)

    def __len__(self):
        cursor = self._conn.execute("""SELECT count(*) from {name}""".format(
            name=self.name))

        return len(cursor.fetchall())

    def create_columns(self, columns):
        columns = ', '.join(value(name=key) for key, value in columns.items())
        query = """CREATE TABLE if not exists {0}
                   ({1})""".format(self.name, columns)

        self._conn.execute(query)

    def insert(self, **kwargs):
        return Row(self._conn, self.name, **kwargs)
        #TODO: add attribute by primary key

    def select(self):
        pass

    @property
    def info(self):
        # name, type, null, default, primary_key
        columns = self._conn.execute(
            "PRAGMA table_info({0})".format(self.name)).fetchall()

        return dict(
            (column[1], {
                'index': column[0],
                'type': column[2], 'null_allowed': bool(column[3]),
                'default': column[4], 'primary_key': bool(column[5])})
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

    def __getattr__(self, name):
        if name in self.tables:
            return Table(self._conn, name)

    def create_table(self, name, columns):
        return Table(self._conn, name, columns)

    @property
    def tables(self):
        cursor = self._conn.execute("""SELECT name from sqlite_master
                                        WHERE type = 'table'""")

        return [row[0] for row in cursor]
