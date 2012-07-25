import unittest
from collections import OrderedDict
from sqlalchemy.exc import OperationalError
from vice.database import integer, string, Database

class TestSQLiteDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database('sqlite:///:memory:')
        self.test_table_creation()

    def test_table_creation(self):
        self.db.create_table('cards', OrderedDict(
            id = integer(primary_key=True),
            name = string(),
            def_ = integer(),
            atk = integer()
        ))

        column_names = [column.name for column in self.db.cards.columns]

        assert 'cards' in self.db.tables
        assert sorted(column_names) == ['atk', 'def', 'id', 'name']

    def test_simple_table_selection(self):
        self.test_record_creation()
        result = self.db.select('cards')

        assert result is not None

    def test_record_creation(self):
        result = self.db.create_record('cards', dict(
            name = 'Imp',
            atk = 2,
            def_ = 2
        ))

        assert result is not None

    def test_table_renaming(self):
        self.db.rename_table('cards', 'items')

        assert 'cards' not in self.db.tables
        assert 'items' in self.db.tables

    def test_invalid_table_renaming(self):
        try:
            self.db.rename_table('items', 'cards')
        except OperationalError:
            pass
        else:
            raise AssertionError("'items' table doesn't exist")


    def test_table_dropping(self):
        self.db.drop_table('cards')

        assert 'cards' not in self.db.tables

    def test_invalid_table_dropping(self):
        try:
            self.db.drop_table('items')
        except AttributeError as e:
            pass
        else:
            raise AssertionError("'items' table doesn't exist")


if __name__ == '__main__':
    unittest.main()
