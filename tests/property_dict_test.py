from vice import PropertyDict

class TestPropertyDict:

    def setup_class(self):
        self.pdict = PropertyDict()

    def test_property_access(self):
        self.pdict['foo'] = 'bar'

        assert self.pdict.foo == self.pdict['foo']

    def test_property_assignment(self):
        self.pdict.foo = 'bar'

        assert self.pdict['foo'] == 'bar'
