import random
import unittest
from vice.plugins.actions import Action


class testAction(unittest.TestCase):

    def setUp(self):
        class Move(Action):
            NAME = 'move'

            def __call__(cls, index, source, destination):
                destination.append(source.pop(index))

        self.Move = Move

        random.seed(1)
        self.source = [1, 2, 3]
        self.destination = [7, 8, 9]

    def test_plugins(self):
        actions = Action.plugins()

        assert isinstance(actions.move, self.Move), type(actions.move)
        actions.move(1, self.source, self.destination)
        assert self.source == [1, 3], self.source
        assert self.destination == [7, 8, 9, 2], self.destination

    def test_new(self):
        def shuffle(cls, item):
            random.shuffle(item)

        action = Action.new(shuffle)

        assert action.__name__ == 'Shuffle', action.__name__
        assert action.NAME == 'shuffle', action.NAME
        assert 'shuffle' in Action.plugins(), Action.plugins().keys()


if __name__ == '__main__':
    unittest.main()
