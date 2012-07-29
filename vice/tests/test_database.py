from collections import OrderedDict
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
    result = self.db.create_record('cards', dict(
        nme = 'Imp',
        atk = 2,
        def_ = 2))

    assert result
