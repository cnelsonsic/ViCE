# -*- coding: utf-8 -*-

# Copyright (C) 2011-2012 Edwin Marshall <emarshall85@gmail.com>
#
# This file is part of ViCE.
#
# ViCE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ViCE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with ViCE.  If not, see <http://www.gnu.org/licenses/>.

from vice import PropertyDict


class PluginMeta(type):

    def __new__(cls, name, bases, attrs):
        attrs['NAME'] = attrs.get('NAME') or name

        return super(PluginMeta, cls).__new__(cls, name, bases, attrs)


PluginBase = PluginMeta('PluginBase', (object, ), {})


class Plugin(PluginBase):
    """ Base class for all new plugin types.

        All new plugin types are created by subclassing Plugin. In
        most cases, you will want to inherit from a Plugin subclass
        rather than directly from Plugin itself.

        The NAME attribute is used to identify the plugin during discovery. If
        not specified, the class name is used.
    """

    @classmethod
    def plugins(cls):
        """ Returns a vice.PropertyDict of available plugins.

            This PropertyDict's keys are plugin names and values are the plugin
            classes that correspond with those names. A common idiom is to
            assign the return value to a variable to ease the access to
            available plugins::

                class FooPlugin(Plugin): pass
                plugins = Plugin.plugins()
                foo = plugins.Foo()
        """

        cls._plugins = []

        def find_subclasses(cls):
            """ Recursive function needed to find subclassses of subclasses. """
            subclasses = [subclass for subclass in cls.__subclasses__()
                          if 'Base' not in subclass.__name__]

            if subclasses:
                cls._plugins += subclasses

                for subclass in subclasses:
                    find_subclasses(subclass)

        find_subclasses(cls)

        return PropertyDict((plugin.NAME, plugin) for plugin in cls._plugins)


class ActionMeta(PluginMeta):
    """ Action metaclass.

        This metaclass automatically sets the NAME attribute to an underscore
        version of the class name if one wasn't already provided in the class
        declaration.
    """

    def __new__(cls, name, bases, attrs):
        # convert CamelCase to underscore_case
        head = [name[0].lower()]
        tail = ['_{0}'.format(char.lower()) if char.isupper() else char
                for char in name[1:]]
        attrs['NAME'] = ''.join(head + tail)

        return super(ActionMeta, cls).__new__(cls, name, bases, attrs)


ActionBase = ActionMeta('ActionBase', (Plugin,), {})


class Action(ActionBase):
    """ Callable plugin that provides general operations for Item plugins.

        An action is a class which acts like a generic function that operates
        on Item plugins. This approach is more flexible, extensible, and less
        repetitious than implementing methods directly within a subclass.

        To create a new action, define an Action subclass and override the
        __call__ method::

            class Foo(Action):
                def __call__(cls):
                    return 'bar'

        The NAME attribute, if not specified, is set to be the underscored
        version of the camel-case class name (eg.FooBar-> foo_bar)
    """

    @classmethod
    def new(cls, name, call=None):
        """ Convenience method used to help simply creation of new actions.

            The function's name is converted to title case and used as the name
            of the class, and it's original form is used as the Plugin's NAME.

            When defining the function, make sure the first argument is cls,
            since this will be used as the class's __call__ special method::

                def foo(cls):
                    return 'bar'

                Action.new('foo', foo)

            Alternatively, you may use a lambda instead::

                Action.new('foo', lambda cls: 'bar')
        """

        if name is None:
            name = call.__name__

        return ActionMeta(name, (cls,), PropertyDict(
            NAME=name,
            __call__=call
        ))

    @classmethod
    def plugins(cls, *args, **kwargs):
        """ Returns a vice.PropertyDict of available action plugins

            Acts similarly to Plugin.plugins(), except that it returns
            instances of the plugin classes, rather than the classes
            themselves::

                actions = Action.plugins()
                foo = actions.foo_action()
        """

        return PropertyDict(
            (pluginName, plugin(*args, **kwargs))
            for pluginName, plugin in super(Action, cls).plugins().items())

    def __call__(self):
        raise NotImplementedError(
            'All actions should implement a __call__ method!')


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

        To create a new container, define a Container subclass and override the
        constraints method::

            class Foo(Action):
                def contraints(self, item):
                    return [
                        item.NAME == 'Card', # container holds cards
                        40 <= len(self) <= 60 # between 40 and 60 cards]

        .. note:: self refers to container.

        The NAME attribute, if not specified, is set to be the underscored
        version of the camel-case class name (eg.FooBar-> foo_bar)
    """

    def __len__(self):
        return len(self.items)

    @classmethod
    def new(cls, name, constraints):
        """ Convenience method used to help simplify the creation of new
            containers.

            Simply pass an appropriate container name and a constraints
            function::

                def contraints(self, item):
                    return [
                        item.NAME == 'Card',
                        40 <= len(self) <= 60]

                Deck = Container.new('Deck', constraints)

            Alternatively, you may pass a lambda instead::

                Deck = Container.new(
                    'Deck', lambda self, item: [
                        item.NAME == 'Card',
                        40 <= len(self) <= 60])
        """

        return ContainerMeta(
            name, (cls,), dict(NAME=name, constraints=constraints))


    def constraints(self, item):
        """ Returns a list of constraints to be applied toward items.

            This method should return a list of comparison expressions used to
            validate the item before an action may be committed on it with
            respect to the container. If any of the comparisons evaluates to
            False, the action is aborted.
       """

        raise NotImplementedError(
            'All containers should implement a constraints method!')

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


class ItemMeta(PluginMeta):
    """ Item metaclass.

        This metaclass automatically creates class attributes for
        each attribute defined in ATTRIBUTES.
    """

    def __new__(cls, name, bases, attrs):
        if attrs.get('ATTRIBUTES'):
            attrs.update(dict.fromkeys(attrs['ATTRIBUTES']))

        return super(ItemMeta, cls).__new__(cls, name, bases, attrs)


ItemBase = ItemMeta('ItemBase', (Plugin,), {})


class Item(ItemBase):
    """ Plugin that represents a games tangible objects.

        An item is any object within a card game that can be interacted
        with. The most obvious example of this would be the game's cards,
        but things such as tokens and dice would be implemented as items
        as well.

        To create a new item, define a new Item subclass and override
        ATTRIBUTES with a sequence of strings::

            class Card(Item):
                ATTRIBUTES = 'name', 'atk', 'def'

        The values of ATTRIBUTES are converted to class attributes. These
        attributes are semi-immutable. That is, on instantiating of an item
        plugin, you may change the value of existing attributes, but you may
        not create new ones. If you wish to do so, you should add the new
        attribute to ATTRIBUTES when defining the class.
    """

    ATTRIBUTES = ()

    @classmethod
    def new(cls, name, attributes):
        """ Convenience method used to help simplify the creation of new items.

            Simply pass an appropriate item name and a sequence of attribute
            names::

                Dice = Item.new('Dice', ('name', 'atk', 'def'))
        """

        return ItemMeta(
            name, (cls,), dict(
                NAME=name,
                ATTRIBUTES=tuple(set(attributes))))

    @classmethod
    def from_table(cls, name, table, exclude=None):
        """ Convenience method used to create new items from database tables.

            Simply pass an appropriate name, valid database table and an optional
            exclude sequence to Item.from_table::

                db = vice.database.Database('sqlite:///wtactics.sqlite')
                Card = Item.from_table('Card', db.cards, exclude=['id'])

           Any columns that match those in the exclude sequence will be ignored.
        """

        exclude = exclude or []

        attributes = [
            column.name for column in table.columns
            if column.name not in exclude]

        return cls.new(name, attributes)

    def __setattr__(self, name, value):
        if hasattr(self, name):
            super(Item, self).__setattr__(name, value)
