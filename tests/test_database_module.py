import os
import unittest
from vice import database
from vice.plugins.items import Item

@unittest.skip("Feature on hold")
class TestDatabase(unittest.TestCase):

    def setUp(self):
        class Card(Item):
            ATTRIBUTES = 'name', 'atk', 'def_'

        self.Card = Card
        self.test_connection()

    def test_connection(self):
        self.db = database.connect('sqlite:/foo.sqlite')

        assert os.path.exists("foo.db"), os.listdir

    def test_table_creation(self):
        self.db.create_table('cards', self.Card.ATTRIBUTES, {
            IntCol: ['atk', 'def']
        })

        assert hasattr(self.db, 'cards'), dir(self.db)

    def test_record_creation_with_args(self):
        self.db.cards.create_record("Imp", 1, 2)

        assert len(self.db.cards) > 0, len(self.db.cards)

    def test_record_creation_with_kwargs(self):
        self.db.cards.create_record(
            name = dwarf,
            atk = 5,
            def_ = 2
        )

        assert len(self.db.cards) > 0, len(self.db.cards)


if __name__ == '__main__':
    unittest.main()
