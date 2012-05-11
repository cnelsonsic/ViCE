from unittest import main, TestCase
from vice.plugins.items import Item

class FooItem(Item):
    ATTRIBUTES = 'bar', 'biz', 'baz'

class TestItem(TestCase):

    def setUp(self):
        self.foo = FooItem()

    def test_attributes_created(self):
        try:
            self.foo.bar
        except AttributeError:
            self.fail("Attribute 'bar' wasn't created on instantiation")

    def test_new_atttribute_creation_impossible(self):
        self.foo.buz = None

        try:
            self.foo.buz
        except AttributeError:
            pass
        else:
            self.fail("Attribute 'buz' was created after instantiation")


if __name__ == '__main__':
    main()
