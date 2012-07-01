import random
import unittest
from vice.plugins import Plugin, Action, Item, Container
from vice.database import Database, integer, string

class TestPlugin(unittest.TestCase):

    def setUp(self):
        class FooPlugin(Plugin):
            NAME = 'foo'

        self.FooPlugin = FooPlugin

    def test_plugin_discovery_nested(self):
        class BarPlugin(self.FooPlugin):
            NAME = 'bar'

        plugins = Plugin.plugins().keys()

        self.assertIn('foo', plugins)
        self.assertIn('bar', plugins)


class TestAction(unittest.TestCase):

    def setUp(self):
        class Move(Action):
            NAME = 'move'

            def __call__(cls, index, source, destination):
                destination.append(source.pop(index))

        self.Move = Move

        random.seed(1)
        self.source = [1, 2, 3]
        self.destination = [7, 8, 9]

    def test_plugins(self):
        actions = Action.plugins()

        self.assertIsInstance(actions.move, self.Move)

        actions.move(1, self.source, self.destination)
        self.assertSequenceEqual(self.source, [1, 3])
        self.assertSequenceEqual(self.destination, [7, 8, 9, 2])


    def test_creation_from_new(self):
        def shuffle(cls, item):
            random.shuffle(item)

        action = Action.new(shuffle)

        self.assertEqual(action.__name__, 'Shuffle')
        self.assertEqual(action.NAME, 'shuffle')
        self.assertIn('shuffle', Action.plugins())


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

        Card = Item.from_table('Card', db.cards, exclude=['id'])

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
