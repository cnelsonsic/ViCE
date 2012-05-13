import os
import unittest
from vice.database import integer, string, Database

class TestSQLiteDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database('sqlite:///wtactics.sqlite')
        self.test_table_creation()

    def test_table_creation(self):
        result = self.db.create_table('cards', {
            'id': integer(primary_key=True),
            'name': string(),
            'def': integer(),
            'atk': integer(),
        })

        column_names = [column.name for column in self.db.cards.columns]

        assert 'cards' in self.db.tables, self.db.tables
        assert sorted(column_names) == ['atk', 'def', 'id', 'name'], sorted(column_names)

    def test_table_insertion(self):
        self.db.insert('cards',
            name = 'Imp',
            atk = 4,
            def_ = 4
        )

    def test_simple_table_selection(self):
        self.test_table_insertion()
        results = self.db.select('cards')

        assert results, results


if __name__ == '__main__':
    unittest.main()
