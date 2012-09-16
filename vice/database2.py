import sqlite3
from functools import partial

def column(kind, name=None, primary_key=False):
    query = '{name} {kind}'
    if primary_key:
        query += ' PRIMARY KEY'

    if name:
        return query.format(kind=kind, name=name)
    else:
        return partial(query.format, kind=kind)

text = partial(column, kind='text')
integer = partial(column, kind='integer')
real = partial(column, kind='real')
blob = partial(column, kind='blob')
null = partial(column, kind='null')


class Table(object):

    def __init__(self, connection, name, columns):
        self._conn = connection
        self.name = name
        self.columns = columns.keys()

        columns = ', '.join(value(name=key) for key, value in columns.items())
        query = """CREATE TABLE {name}
                ({columns})""".format(name=name, columns=columns)

        self._conn.execute(query)

    def insert(self):
        pass

    def select(self):
        pass


class Database(object):

    text = text
    integer = integer
    real = real
    blob = blob
    null = null

    def __init__(self, location=':memory:'):
        self.location = location
        self._conn = sqlite3.connect(self.location)

    def create_table(self, name, columns):
        setattr(self, name, Table(self._conn, name, columns))




class Record(object):
    pass


