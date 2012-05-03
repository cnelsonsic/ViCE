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

class PropertyDict(dict):
    """ A dict subclass that allows values to be retrieved by accessing their
        keys as properties.

        PropertyDict provides a dictionary whose key:value pairs may be
        assigned in the conventional brace notation (foo['bar'] = 'baz'),
        or in the more elegant object:property notation (foo.bar = 'baz').
        Beyond this subtle addition, they behave identically to regular
        dictionaries.
    """

    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

    def __getattr__(self, name):
        return self.get(name, None)
