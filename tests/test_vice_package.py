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

    def test_table_creation_from_item(self):
        Card = Item.new('Card', ('name', 'atk', 'def_'))
        self.db.create_table('cards', Card.ATTRIBUTES, {
            'id': self.db.integer(primary_key=True),
            'atk': self.db.integer(),
            'def': self.db.integer(),
        })

        assert 'cards' in self.db.tables, self.db.tables

    def test_table_insertion(self):
        self.test_table_creation_from_item()
        self.db.insert('cards',
            name = 'Imp',
            atk = 4,
            def_ = 4
        )


if __name__ == '__main__':
    unittest.main()
