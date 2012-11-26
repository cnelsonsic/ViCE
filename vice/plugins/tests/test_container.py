import pytest
from vice.plugins import Item, Container

@pytest.fixture(scope='function')
def card(request):
    card = Item.new('Card', ('name', 'types'))()
    card.name = 'SomeCard'
    card.types = ('Land', )

    return card

@pytest.fixture(scope='function')
def land_zone(request):
    LandZone = Container.new(
        'LandZone', lambda cls, item: [
            item.NAME == 'Card',
            len(cls) < 1,
            'Land' in item.types])

    assert 'LandZone' in Container.plugins()
    return LandZone()

def test_container_insertion(land_zone, card):
    assert land_zone.insert(card)

def test_invalid_container_inesertion(land_zone, card):
    land_zone.insert(card)

    # attempt to insert a second card...
    assert not land_zone.insert(card)
