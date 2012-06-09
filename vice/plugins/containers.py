from vice.plugins import Plugin, PluginMeta

class ContainerMeta(PluginMeta):
    """ Container metaclass.

        This metaclass automatically adds an items attribute to the container
        to be used by the constraints method.
    """

    def __new__(cls, name, bases, attrs):
        attrs['items'] = []

        return super(ContainerMeta, cls).__new__(cls, name, bases, attrs)


ContainerBase = ContainerMeta('ContainerBase', (Plugin,), {})


class Container(ContainerBase):
    """ Plugin that represents an object that is able to hold other objects.

        A container is any object within a card game that can contain other
        objects, optionally placing arbitrary restrictions on its contents.
        Examples of containers include a decks (container of cards with a
        maximum and minumum count requirement), a questing
        zone (contains only quest cards), or a hand (container of cards).
    """

    def __len__(self):
        return len(self.items)

    @classmethod
    def new(cls, name, function):
        """ Convenience method used to help simplify the creation of new
            containers.

            Simply pass an appropriate container name and a consraints
            function::

                def contraints(self, item):
                    return [
                        item.NAME = 'Card' # container holds cards
                        40 <= len(self) <= 60 # between 40 and 60 cards
                    ]

                Deck = Container.new('Deck', constraints)
        """
        return ContainerMeta(name, (cls,), dict(
            NAME=name,
            consraints=function
        ))


    def constraints(self, item):
        """ Returns a list of constraints to be applied toward items.

            This method should return a list of comparison expressions used to
            validate the item before an action may be committed on it with
            respect to the container. If any of the comparisons evaluates to
            False, the action is aborted.
        """

        raise NotImplementedError(
            'All containers should implement a filters method!'
        )

    def insert(self, item, position=-1):
        """ Insert's an item into the container at position.

            If the item is valid, it is inserted into the container at the
            given position and True is returned to signal success. If the item
            is invalid, nothing is inserted, and False is returned.
        """

        if all(self.constraints(item)):
            self.items.insert(position, item)
            return True
        else:
            return False
