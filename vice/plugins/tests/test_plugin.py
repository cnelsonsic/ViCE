from vice.plugins import Plugin

def test_plugin_discovery():
    class FooPlugin(Plugin):
        NAME = 'foo'

    class BarPlugin(FooPlugin):
        NAME = 'bar'

    plugin_names = Plugin.plugins().keys()

    assert sorted(plugin_names) == ['bar', 'foo']
