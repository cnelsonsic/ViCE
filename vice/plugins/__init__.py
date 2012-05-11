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

import os

from vice import PropertyDict

class Plugin(object):
    """ Base class for all new plugin types.

        All new plugin types are created by subclassing Plugin. In
        most cases, you will want to inherit from a Plugin subclass
        rather than directly from Plugin iteself.

        All new plugins must have a NAME class attribute, which is used mainly
        for plugin discovery.
    """

    NAME = None

    @classmethod
    def plugins(cls):
        """ Returns a plugin's subclasses as a vice.PropertyDict.

            This PropertyDict's keys are plugin names and values are the plugin
            classes that correspond with those names. A common idiom is to
            assign the return value to a variable to ease the access to
            available plugins::

                foo_plugins = Foo.plugins()
                baz = foo_plugins.Baz(x, y)
        """

        cls._plugins = []

        def find_subclasses(cls):
            """ Recursive function needed to find subclassses of subclasses. """
            subclasses = cls.__subclasses__()

            if subclasses:
                cls._plugins += subclasses

                for subclass in subclasses:
                    find_subclasses(subclass)

        find_subclasses(cls)

        return PropertyDict((plugin.NAME, plugin)
                    for plugin in cls._plugins if plugin.NAME is not None)
