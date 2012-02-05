# -*- coding: utf-8 -*-

class Dict(dict):

    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

    def __getattr__(self, name):
        return self.get(name, None)
