from unittest import TestCase, main
from vice.plugins import Plugin, disable

class TestPlugin(TestCase):

    def setUp(self):
        class FooPlugin(Plugin):
            NAME = 'foo'

        self.FooPlugin = FooPlugin

    def test_plugin_discovery_nested(self):
        class BarPlugin(self.FooPlugin):
            NAME = 'bar'

        plugins = sorted(Plugin.plugins().keys())

        assert plugins == ['bar', 'foo']


if __name__ == '__main__':
    main()
