import random
from vice.plugins import Action

def pytest_funcarg__actions(request):
    return request.cached_setup(setup=test_define_from_new, scope='function')

def test_define_from_new():
    Echo = Action.new('Echo', lambda x: x)

    assert Echo.NAME == 'echo'
    return Action.plugins()

def test_plugin_discovery(actions):
    assert isinstance(actions.echo, Action)

