import os
from collections import OrderedDict
import pytest
from vice.database import Database, integer, text, gt

@pytest.fixture(scope='module')
def db(request):
    db = Database('wtactics.db')

    def fin():
        os.remove(db.location)

    request.addfinalizer(fin)

    return db

def test_create_table(db):
    db.create_table(
        'cards', {
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
    db.cards.insert({
        'name': 'Imp',
        'atk': 2,
        'def': 2})

    assert len(db.cards) == 1

def test_select(db):
    for n, a, d in [
        ['Runt', 2, 1],
        ['Air', 0, 0],
        ['God', 10, 10]]:
        db.cards.insert({'def': d}, name=n, atk=a)

    rows = db.cards.select(atk=2).fetchall()

    assert len(rows) == 2

def test_operator_select(db):
    rows = db.cards.select(**{
        'def': gt(0)}).fetchall()

    assert len(rows) == 3

def test_drop(db):
    db.drop('cards')

    assert not db.tables

def test_rename_table(db):
    test_create_table(db)
    db.rename_table('cards', 'dogs')

    assert 'dogs' in db.tables
    assert 'cards' not in db.tables
