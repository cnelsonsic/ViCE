# -*- coding: utf-8 -*-

import sys

from plugins import Scheme

class Dict(dict):

    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

    def __getattr__(self, name):
        return self.get(name, None)
