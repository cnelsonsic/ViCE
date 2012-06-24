import unittest
from vice.plugins import Item, Container

class TestContainer(unittest.TestCase):
    def setUp(self):

        class Card(Item):
            ATTRIBUTES = 'name', 'types'

        class LandZone(Container):
            def constraints(self, item):
                return [
                    len(self) < 1,
                    'Land' in item.types
                ]

        self.LandZone = LandZone
        self.card = Card()
        self.card.name = 'SomeCard'
        self.card.types = 'Land',

    def test_creation_from_new(self):
        def constraints(self, item):
            return [
                item.NAME == 'Card',
                40 <= len(self) <= 60,
            ]

        Deck = Container.new('Deck', constraints)

        self.assertNotEqual(Deck, None)

    def test_container_insert_true(self):
        land_zone = self.LandZone()
        self.assertTrue(land_zone.insert(self.card))

    def test_container_insert_false(self):
        land_zone = self.LandZone()
        land_zone.insert(self.card)
        self.assertFalse(land_zone.insert(self.card))


if __name__ == '__main__':
    unittest.main()
