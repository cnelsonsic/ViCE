import random
import pytest
from vice.plugins import Action

@pytest.fixture(scope='function')
def actions():
    Echo = Action.new('Echo', lambda x: x)

    assert Echo.NAME == 'echo'
    return Action.plugins()

def test_plugin_discovery(actions):
    assert isinstance(actions.echo, Action)

