import random
import unittest
from collections import OrderedDict
from vice.plugins import Plugin, Action, Item, Container
from vice.database import Database, integer, string


class TestItem(unittest.TestCase):

    def setUp(self):
        class Counter(Item):
            ATTRIBUTES = 'value',

        self.counter = Counter()

    def test_creation_from_new(self):
        item = Item.new('Dice', ('sides',))

        assert item.__name__ == 'Dice'
        assert 'Dice' in Item.plugins()

    def test_creation_from_db(self):
        db = Database('sqlite:///:memory:')
        db.create_table(
            'cards', OrderedDict(
                id = integer(primary_key=True),
                name = string(),
                atk = integer(),
                def_ = integer()))

        Card = Item.from_table('Card', db.cards, exclude=['id'])

        assert all(hasattr(Card, attr) for attr in ('atk', 'def', 'name'))

    def test_attributes_created(self):
        assert hasattr(self.counter, 'value')

    def test_new_atttribute_creation_impossible(self):
        self.counter.owner = 'me'

        assert not hasattr(self.counter, 'owner')

    def test_attribute_assignable(self):
        self.counter.value  = 7

        assert self.counter.value == 7


if __name__ == '__main__':
    unittest.main()
