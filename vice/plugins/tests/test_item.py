import pytest
from vice.database import Database, integer, text
from vice.plugins import Item

@pytest.fixture(scope='function')
def counter():
    class Counter(Item):
        ATTRIBUTES = ('value', )

    return Counter()

def test_creation_from_new():
    item = Item.new('Dice', ('sides', ))

    assert item.__name__ in Item.plugins()

def test_creation_from_db():
    db = Database()
    db.create_table(
        'cards', {
            'id': integer(primary_key=True),
            'name': text(),
            'atk': integer(),
            'def': integer()})

    Card = Item.from_table('Card', db.cards, exclude=['id'])

    assert all(hasattr(Card, attr) for attr in ('atk', 'def', 'name'))

def test_attributes_created(counter):
    assert hasattr(counter, 'value')

def test_new_attributes_not_created(counter):
    # should I raise an exception here instead of failing silently?
    counter.owner = 'me'

    assert not hasattr(counter, 'owner')

def test_attribute_assignable(counter):
    counter.value = 7

    assert counter.value == 7

