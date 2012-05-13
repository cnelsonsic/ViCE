import unittest
from vice.plugins.items import Item
from vice.database import Database, string, integer


class TestItem(unittest.TestCase):

    def setUp(self):
        class Counter(Item):
            ATTRIBUTES = 'value',

        self.counter = Counter()

    def test_creation_from_new(self):
        item = Item.new("Dice", ('sides',))

        assert item.__name__ == 'Dice', item.__name__
        assert item.NAME == 'Dice', item.NAME
        assert 'Dice' in Item.plugins(), Item.plugins().keys()

    def test_creation_from_db(self):
        db = Database('sqlite:///wtactics.sqlite')
        db.create_table('cards', {
            'id': integer(primary_key=True),
            'name': string(),
            'atk': integer(),
            'def': integer()
        })
        Card = Item.fromTable('Card', db.cards, exclude=['id'])

        assert  Card.ATTRIBUTES == ('atk', 'def', 'name'), Card.ATTRIBUTES

    def test_attributes_created(self):
        assert hasattr(self.counter, 'value'), dir(self.counter)

    def test_new_atttribute_creation_impossible(self):
        self.counter.owner = 'me'

        assert not hasattr(self.counter, 'me'), self.counter.cost


if __name__ == '__main__':
    unittest.main()
