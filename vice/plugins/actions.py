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

    def __new__(cls, name, bases, attrs):
        if not attrs.get('NAME'):
            # find the indicies of all capital letters
            caps = [i for i in range(len(name)) if name[i].isupper()]
            # create list of words based on those indicies
            words = [name[caps[i]:caps[i+1]] for i in range(len(caps)-1)]
            # add last word to list
            words.append(name[caps[-1]:])
            # convert list of words to underscored string
            attrs['NAME'] = '_'.join([word.lower() for word in words])

        return super(ActionMeta, cls).__new__(cls, name, bases, attrs)


ActionBase = ActionMeta('ActionBase', (Plugin,), {})


class Action(ActionBase):
    """ Callable plugin that provides general operations for Item plugins.

        An action is a class which acts like a generic function that operates
        on Item plugins. This approach is more flexible, extensible, and less
        repetitious than implementing methods directly within a subclass.

        To create a new action, define an Action subclass, override NAME (by
        convention, lowercase for actions), and finally override __call__::

            class Foo(Action):
                NAME = 'foo'

                def __call__(cls):
                    return 'bar'

        Alternatively, you may define a simple function and pass that to
        Action.new::

            def foo(cls):
                return 'bar'

            Action.new(foo)
    """

    @classmethod
    def new(cls, function):
        """ Convenience method used to help simply creation of new actions.

            The function's name is converted to title case and used as the name
            of the class, and it's original form is used as the Plugin's NAME.

            When defining the function, make sure the first argument is cls,
            since this will be used as the class's __call__ special method
        """

        class_name = function.__name__.title().replace('_', '')

        return type(class_name, (cls,),
                    PropertyDict(NAME=function.__name__, __call__=function))

    @classmethod
    def plugins(cls, *args, **kwargs):
        """ Acts similarly to Plugin.plugins(), except that it returns
            instances of the plugin classes, rather than the classes
            themselves.
        """

        return PropertyDict(
            (pluginName, plugin(*args, **kwargs))
            for pluginName, plugin in super(Action, cls).plugins().items()
        )

    def __call__(self):
        raise NotImplementedError('All actions should implement a __call__ method!')
