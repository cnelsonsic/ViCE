import unittest
from vice.plugins.items import Item


class TestItem(unittest.TestCase):

    def setUp(self):
        class Card(Item):
            ATTRIBUTES = 'name', 'atk', 'def'

        self.card = Card()

    def test_attributes_created(self):
        try:
            self.card.name
        except AttributeError:
            self.fail("Attribute 'name' wasn't created on instantiation")

    def test_new_atttribute_creation_impossible(self):
        self.card.cost = 4

        try:
            self.card.cost
        except AttributeError:
            pass
        else:
            self.fail("Attribute 'cost' was created after instantiation")


if __name__ == '__main__':
    unittest.main()
