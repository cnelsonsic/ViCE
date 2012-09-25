import os
from collections import OrderedDict
from vice.database2 import Database, integer, text


def pytest_funcarg__db(request):

    def setup():
        db = Database('wtactics.db')

        assert os.path.exists('wtactics.db')
        return db

    def teardown(db):
        os.remove(db.location)

        assert not os.path.exists(db.location)
        del db

    return request.cached_setup(
        setup=setup, teardown=teardown, scope='module')

def test_create_table(db):
    db.create_table(
        'cards', **{
            'id': integer(primary_key=True),
            'name': text(),
            'def': integer(),
            'atk': integer()})

    assert sorted(db.cards.columns) == ['atk', 'def', 'id', 'name']

def test_tables(db):
    assert db.tables == ['cards']

def test_primary_key(db):
    assert db.cards.primary_key == 'id'

def test_insert(db):
    db.cards.insert(2, 2, name='Imp')

    assert len(db.cards) == 1

def test_select(db):
    db.cards.insert(2, 1, 'Runt')
    db.cards.insert(0, 0, 'Air')
    db.cards.insert(10, 10, 'God')
    rows = db.cards.select(atk=2)

    assert len(rows.fetchall()) == 2

def test_operator_select(db):
    pass

def test_drop(db):
    pass

def test_rename_table(db):
    pass
