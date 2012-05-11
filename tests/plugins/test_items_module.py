import unittest
from vice.plugins.items import Item


class TestItem(unittest.TestCase):

    def setUp(self):
        class Card(Item):
            ATTRIBUTES = 'name', 'atk', 'def'

        self.card = Card()

    def test_new(self):
        item = Item.new("Dice", ('sides',))

        assert item.__name__ == 'Dice', item.__name__
        assert item.NAME == 'Dice', item.NAME
        assert 'Dice' in Item.plugins(), Item.plugins().keys()


    def test_attributes_created(self):
        assert hasattr(self.card, 'name'), dir(self.card)

    def test_new_atttribute_creation_impossible(self):
        self.card.cost = 4

        assert not hasattr(self.card, 'cost')


if __name__ == '__main__':
    unittest.main()
