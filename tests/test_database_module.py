import os
import unittest
from vice.database import integer, string, Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database('sqlite:///wtactics.sqlite')

    def test_table_creation(self):
        self.db.create_table('cards', {
            'id': integer(primary_key=True),
            'name': string(),
            'def': integer(),
            'atk': integer(),
        })

        column_names = [column.name for column in self.db.cards.columns]

        assert 'cards' in self.db.tables, self.db.tables
        assert sorted(column_names) == ['atk', 'def', 'id', 'name'], sorted(column_names)

    def test_table_insertion(self):
        self.test_table_creation()
        self.db.insert('cards',
            name = 'Imp',
            atk = 4,
            def_ = 4
        )


if __name__ == '__main__':
    unittest.main()
