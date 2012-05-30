import random
import unittest
from vice.plugins.actions import Action


class TestAction(unittest.TestCase):

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

        self.assertIsInstance(actions.move, self.Move)

        actions.move(1, self.source, self.destination)
        self.assertSequenceEqual(self.source, [1, 3])
        self.assertSequenceEqual(self.destination, [7, 8, 9, 2])


    def test_creation_from_new(self):
        def shuffle(cls, item):
            random.shuffle(item)

        action = Action.new(shuffle)

        self.assertEqual(action.__name__, 'Shuffle')
        self.assertEqual(action.NAME, 'shuffle')
        self.assertIn('shuffle', Action.plugins())


if __name__ == '__main__':
    unittest.main()
