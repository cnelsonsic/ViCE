import unittest
from vice.plugins import Plugin

class TestPlugin(unittest.TestCase):

    def setUp(self):
        class FooPlugin(Plugin):
            NAME = 'foo'

        self.FooPlugin = FooPlugin

    def test_plugin_discovery_nested(self):
        class BarPlugin(self.FooPlugin):
            NAME = 'bar'

        plugins = Plugin.plugins().keys()

        assert 'foo' in plugins and 'bar' in plugins


if __name__ == '__main__':
    unittest.main()
