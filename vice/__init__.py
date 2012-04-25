# -*- coding: utf-8 -*-

class PropertyDict(dict):

    """ dict subclass that allows values to be retrieved by accessing their
        keys as properties.

        Example:
        >>> pdict = PropertyDict()
        >>> pdict['foo'] = 'bar'
        >>> pdict.foo
        'bar'
    """
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

    def __getattr__(self, name):
        return self.get(name, None)
