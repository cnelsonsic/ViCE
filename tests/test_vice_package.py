import os
import unittest
from vice import Database, PropertyDict
from vice.plugins.items import Item

class TestProperyDict(unittest.TestCase):

    def setUp(self):
        self.fields = PropertyDict()

    def test_property_access(self):
        self.fields.name = "Joe"
        assert self.fields.name == self.fields['name'], self.fields.name


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database('sqlite:///wtactics.sqlite')

    def tearDown(self):
        if os.path.exists('wtactics.sqlite'):
            os.remove('wtactics.sqlite')

    def test_table_creation_from_item(self):
        Card = Item.new('Card', ('name', 'atk', 'def', 'set'))

        self.db.create_table('cards', Card.ATTRIBUTES, {
            'atk': self.db.integer(),
            'def': self.db.integer(),
            'set': self.db.string(primary_key=True),
        })

        assert 'cards' in self.db.tables, self.db.tables


if __name__ == '__main__':
    unittest.main()
