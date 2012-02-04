class Dict(dict):

    def __getattr__(self, attr):
        return self.get(attr, None)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class Plugin(object):

    @classmethod
    def plugins(cls, *args, **kwargs):
        return Dict((subclass.name, subclass(*args, **kwargs))
                       for subclass in cls.__subclasses__())


class Action(Plugin):

    def __call__(self):
        raise NotImplementedError()


class Item(Plugin):

    isStored = False
    fields = Dict()
