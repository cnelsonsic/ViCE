from unittest import TestCase, main
from vice.plugins.actions import Action

class testAction(TestCase):

    def setUp(self):
        class FooAction(Action):
            NAME = 'foo'

            def __call__(cls):
                return 'bar'

        self.FooAction = FooAction

    def test_plugins(self):
        actions = Action.plugins()

        assert isinstance(actions.foo, self.FooAction)
        assert actions.foo() == 'bar'

    def test_new(self):
        def foo_action2(cls):
            return 'bar'

        new_action = Action.new(foo_action2)

        assert new_action.__name__ == 'FooAction2'
        assert new_action.NAME == 'foo_action2'
        assert 'foo_action2' in Action.plugins()


if __name__ == '__main__':
    main()
