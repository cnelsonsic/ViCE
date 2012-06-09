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
from vice.plugins import Plugin, PluginMeta

class ActionMeta(PluginMeta):
    """ Action metaclass.

        This metaclass automatically sets the NAME attribute to an underscore
        version of the class name if one wasn't already provided in the class
        declaration.
    """

    def __new__(cls, name, bases, attrs):
        if not attrs.get('NAME'):
            # convert camel-case to underscores
            caps = [i for i in range(len(name)) if name[i].isupper()]
            words = [name[caps[i]:caps[i+1]] for i in range(len(caps)-1)]
            words.append(name[caps[-1]:])
            attrs['NAME'] = '_'.join((word.lower() for word in words))

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
    def new(cls, function):
        """ Convenience method used to help simply creation of new actions.

            The function's name is converted to title case and used as the name
            of the class, and it's original form is used as the Plugin's NAME.

            When defining the function, make sure the first argument is cls,
            since this will be used as the class's __call__ special method::

                def foo(cls):
                    return 'bar'

                Action.new(foo)
        """

        class_name = function.__name__.title().replace('_', '')

        return ActionMeta(class_name, (cls,), PropertyDict(
            NAME=function.__name__,
            __call__=function
        ))

    @classmethod
    def plugins(cls, *args, **kwargs):
        """ Returns a vice.PropertyDict of available action plugins

            Acts similarly to Plugin.plugins(), except that it returns
            instances of the plugin classes, rather than the classes
            themselves::

                class FooAction(Action): pass
                actions = Action.plugins()
                foo = actions.foo_action()
        """

        return PropertyDict(
            (pluginName, plugin(*args, **kwargs))
            for pluginName, plugin in super(Action, cls).plugins().items()
        )

    def __call__(self):
        raise NotImplementedError(
            'All actions should implement a __call__ method!'
        )
