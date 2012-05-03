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
from vice.plugins import Plugin

class Action(Plugin):
    """ Callable plugin intended to provide general operations for Item plugins.

        An action is a class which acts like a generic function that operates
        on Item plugins. This approach is more flexible, extensible, and less
        repetitious than implementing methods directly within a subclass.

        To create a new action, simply define an Action subclass, ovewrite the
        NAME class attribute (by convention, lower-case), and finally overwrite
        the __call__ special method::

        class Foo(Action):
            NAME = 'foo'

            def __call__(cls):
                return 'bar'

        Alternatively, you can define a simple  function and pass that to the
        Action.new class method::

        def foo(cls):
            return 'bar'

        Action.foo(foo)
    """

    @classmethod
    def new(cls, function):
        """ Convenience method used to help simply creation of new Actions.

            The function's name is converted to title case and used as the name
            of the class, and it's original form is used as the Plugin's NAME.

            When defining the function, make sure the first argument is cls,
            since this will be used as the class's __call__ special method
        """

        return type(function.__name__.title(), (cls,),
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
        raise NotImplementedError('All actions should implement __call__!')
