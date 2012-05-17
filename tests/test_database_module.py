import os
import unittest
from vice.database import integer, string, Database

class TestSQLiteDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database('sqlite:///:memory:')
        self.test_table_creation()

    def test_table_creation(self):
        self.db.create_table('cards',
            id = integer(primary_key=True),
            name = string(),
            def_ = integer(),
            atk = integer()
        )

        column_names = [column.name for column in self.db.cards.columns]

        assert 'cards' in self.db.tables, self.db.tables
        assert sorted(column_names) == ['atk', 'def', 'id', 'name'], sorted(column_names)

    def test_simple_table_selection(self):
        self.test_record_creation()
        result = self.db.select('cards')

        assert result, result

    def test_record_creation(self):
        result = self.db.create_record('cards',
            name = 'Imp',
            atk = 2,
            def_ = 2
        )

        assert result, result

if __name__ == '__main__':
    unittest.main()
