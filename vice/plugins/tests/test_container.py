from vice.plugins import Item, Container


def pytest_funcarg__card(request):
    card = Item.new('Card', ('name', 'types'))()
    card.name = 'SomeCard'
    card.types = 'Land',

    return card

def pytest_funcarg__land_zone(request):
    return request.cached_setup(setup=test_define_from_new, scope='function')

def test_define_from_new():
    LandZone = Container.new('LandZone', lambda cls, item: [
        item.NAME == 'Card',
        len(cls) < 1,
        'Land' in item.types

    ])

    assert 'LandZone' in Container.plugins()
    return LandZone()

def test_container_insertion(land_zone, card):
    assert land_zone.insert(card)

def test_invalid_container_inesertion(land_zone, card):
    land_zone.insert(card)

    # attempt to insert a second card...
    assert not land_zone.insert(card)
