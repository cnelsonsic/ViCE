import random
import unittest
from collections import OrderedDict
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

        plugins = Plugin.plugins()

        assert 'bar' in plugins


class TestAction(unittest.TestCase):

    def setUp(self):
        class Move(Action):
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

        assert self.source == [1, 3]
        assert self.destination ==  [7, 8, 9, 2]


    def test_creation_from_new(self):
        action = Action.new('shuffle', lambda cls, item:
            random.shuffle(item)
        )

        assert action.__name__ == 'Shuffle'
        assert 'shuffle' in Action.plugins()


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
        Deck = Container.new('Deck', lambda cls, item: [
            item.NAME == 'Card',
            40 <= len(cls) <= 60
        ])

        assert Deck is not None

    def test_container_insertion(self):
        land_zone = self.LandZone()
        assert land_zone.insert(self.card)

    def test_invalid_container_insertion(self):
        land_zone = self.LandZone()
        land_zone.insert(self.card)
        assert not land_zone.insert(self.card)


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
        db.create_table('cards', OrderedDict(
            id = integer(primary_key=True),
            name = string(),
            atk = integer(),
            def_ = integer()
        ))

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
