import unittest
from vice.plugins.items import Item
from vice.database import Database, string, integer


class TestItem(unittest.TestCase):

    def setUp(self):
        class Counter(Item):
            ATTRIBUTES = 'value',

        self.counter = Counter()

    def test_creation_from_new(self):
        item = Item.new('Dice', ('sides',))

        self.assertEqual(item.__name__, 'Dice')
        self.assertEqual(item.NAME, 'Dice')
        self.assertTrue('Dice' in Item.plugins())

    def test_creation_from_db(self):
        db = Database('sqlite:///:memory:')
        db.create_table('cards',
            id = integer(primary_key=True),
            name = string(),
            atk = integer(),
            def_ = integer()
        )

        Card = Item.fromTable('Card', db.cards, exclude=['id'])

        self.assertEqual(Card.ATTRIBUTES, ('atk', 'def', 'name'))

    def test_attributes_created(self):
        self.assertTrue(hasattr(self.counter, 'value'))

    def test_new_atttribute_creation_impossible(self):
        self.counter.owner = 'me'

        self.assertFalse(hasattr(self.counter, 'owner'))

    def test_attribute_assignable(self):
        self.counter.value  = 7
        self.assertEqual(self.counter.value, 7)


if __name__ == '__main__':
    unittest.main()
