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

        self.assertIn('foo', plugins)
        self.assertIn('bar', plugins)


if __name__ == '__main__':
    unittest.main()
