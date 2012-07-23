import unittest
from collections import OrderedDict
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

        self.assertIn('cards', self.db.tables)
        self.assertEqual(sorted(column_names), ['atk', 'def', 'id', 'name'])

    def test_simple_table_selection(self):
        self.test_record_creation()
        result = self.db.select('cards')

        self.assertIsNotNone(result)

    def test_record_creation(self):
        result = self.db.create_record('cards', dict(
            name = 'Imp',
            atk = 2,
            def_ = 2
        ))

        self.assertIsNotNone(result)

    def test_table_dropping(self):
        self.db.drop_table('cards')
        self.assertNotIn('cards', self.db.tables)

        with self.assertRaises(AttributeError):
            self.db.drop_table('cards')


if __name__ == '__main__':
    unittest.main()
