import unittest
from vice import PropertyDict

class TestProperyDict(unittest.TestCase):

    def setUp(self):
        self.fields = PropertyDict()

    def test_property_access(self):
        self.fields.name = "Joe"
        self.assertEqual(self.fields.name, self.fields['name'])


if __name__ == '__main__':
    unittest.main()
