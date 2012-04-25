import unittest
import vice

class TestProperyDict(unittest.TestCase):

    def setUp(self):
        self.pdict = vice.PropertyDict()

    def test_property_access(self):
        self.pdict.foo = 'bar'
        assert self.pdict.foo == self.pdict['foo']

if __name__ == '__main__':
    unittest.main()
