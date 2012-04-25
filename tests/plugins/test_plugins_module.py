from unittest import TestCase, main
from vice.plugins import Plugin, disable

class TestPlugin(TestCase):

    def setUp(self):
        class FooPlugin(Plugin):
            NAME = 'foo'

        self.FooPlugin = FooPlugin

    def test_plugin_enabled(self):
        plugins = Plugin.plugins().keys()

        assert self.FooPlugin.ENABLED
        assert 'foo' in plugins

    def test_plugin_disable(self):
        disable(self.FooPlugin)
        plugins = Plugin.plugins().keys()

        assert not self.FooPlugin.ENABLED
        assert 'foo' not in plugins

    def test_plugin_discovery_nested(self):
        class BarPlugin(self.FooPlugin):
            NAME = 'bar'

        plugins = sorted(Plugin.plugins().keys())

        assert plugins == ['bar', 'foo']


if __name__ == '__main__':
    main()
