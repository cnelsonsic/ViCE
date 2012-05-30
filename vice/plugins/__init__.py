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
class PluginMeta(type):

    def __new__(cls, name, bases, attrs):
        if not attrs.get('NAME'):
            attrs['NAME'] = name

        return super(PluginMeta, cls).__new__(cls, name, bases, attrs)


PluginBase = PluginMeta('Plugin', (object, ), {})


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
        """ Returns a plugin's subclasses as a vice.PropertyDict.

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
            subclasses = cls.__subclasses__()

            if subclasses:
                cls._plugins += subclasses

                for subclass in subclasses:
                    find_subclasses(subclass)

        find_subclasses(cls)

        return PropertyDict((plugin.NAME, plugin)
            for plugin in cls._plugins
            if plugin.NAME is not None and plugin.NAME.strip() != ""
        )
