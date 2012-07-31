from collections import OrderedDict
import pytest
from sqlalchemy.exc import OperationalError
from vice.database import integer, string, Database

def pytest_funcarg__db(request):
    return request.cached_setup(setup=test_table_creation, scope='function')

def test_table_creation():
    db = Database('sqlite:///:memory:')
    db.create_table('cards', OrderedDict(
        id = integer(primary_key=True),
        name = string(),
        def_ = integer(),
        atk = integer()))

    columns = (column.name for column in db.cards.columns)

    assert sorted(columns) == ['atk', 'def', 'id', 'name']
    return db

def test_record_creation(db):
    result = db.create_record('cards', dict(
        nme = 'Imp',
        atk = 2,
        def_ = 2))

    assert result

def test_simple_table_selection(db):
    result = db.select('cards')

    assert result is not None

def test_table_renaming(db):
    db.rename_table('cards', 'items')

    assert 'cards' not in db.tables
    assert 'items' in db.tables

def test_invalid_table_renaming(db):
    with pytest.raises(OperationalError):
        db.rename_table('items', 'cards')

def test_table_dropping(db):
    db.drop_table('cards')

    assert 'cards' not in db.tables

def test_invalid_table_dropping(db):
    with pytest.raises(AttributeError):
        db.drop_table('items')
