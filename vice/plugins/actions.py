# -*- coding: utf-8 -*-

# This file is part of ViCE.

# ViCE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# ViCE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with ViCE.  If not, see <http://www.gnu.org/licenses/>.

from vice import PropertyDict
from vice.plugins import Plugin

class Action(Plugin):

    @classmethod
    def new(cls, function):
        return type(function.__name__, (cls,),
                    PropertyDict(NAME=function.__name__, __call__=function))

    @classmethod
    def plugins(cls, *args, **kwargs):
        return PropertyDict(
            (pluginName, plugin(*args, **kwargs))
            for pluginName, plugin in super(Action, cls).plugins().items()
        )

    def __call__(self):
        raise NotImplementedError('All actions should implement __call__!')
