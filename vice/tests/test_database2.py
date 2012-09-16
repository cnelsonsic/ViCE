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

# Data Definition Language
def test_create_table(db):
    db.create_table(
        'cards',
        OrderedDict(
            id_ = integer(primary_key=True),
            name = text(),
            def_ = integer(),
            atk = integer()))

    assert sorted(db.cards.columns) == ['atk', 'def_', 'id_', 'name']

def test_primary_key(db):
    assert db.cards.primary_key == 'id_'
"""
# Data Manipulation Language
def test_insert(db):
    db.cards.insert(
        name = 'Imp',
        atk = 2,
        def_ = 2)

    assert len(db.cards) == 1

def test_select_using_attributes(db):
    db.cards.insert(
        name = 'Foo',
        atk = 4,
        def_ = 1)

    record = db.cards[1]

    assert record.columns == dict(
        name = 'Foo',
        atk = 4,
        def_ = 1)

def test_select(db):
    record = db.cards.select(atk = 2).next()

    assert record == dict(
        name = 'Imp',
        atk = 2,
        def_ = 2)
"""
