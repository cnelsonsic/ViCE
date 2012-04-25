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

    ENABLED = True

    @classmethod
    def plugins(cls):
        cls._plugins = []

        def find_subclasses(cls):
            subclasses = cls.__subclasses__()

            if subclasses:
                cls._plugins += subclasses

                for subclass in subclasses:
                    find_subclasses(subclass)

        find_subclasses(cls)

        return PropertyDict((plugin.NAME, plugin)
                    for plugin in cls._plugins if plugin.ENABLED)


def disable(*classes):
    for cls in classes:
        cls.ENABLED = False
