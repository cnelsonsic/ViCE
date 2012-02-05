class Dict(dict):

    def __getattr__(self, attr):
        return self.get(attr, None)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class Plugin(object):

    ACTIVE = True

    @classmethod
    def plugins(cls, *args, **kwargs):
        return Dict((subclass.NAME, subclass)
                    for subclass in cls.__subclasses__()
                    if subclass.ACTIVE)


class Action(Plugin):

    def __call__(self):
        raise NotImplementedError("All actions should implement __call__!")


class Item(Plugin):
    ATTRIBUTES = None

    def __init__(self, *args, **kwargs):
        self.attributes = Dict()
        if hasattr(self.ATTRIBUTES, 'split'):
            attributes = Dict.fromkeys(self.ATTRIBUTES.split())
        elif hasattr(self.ATTRIBUTES, 'index'):
            attributes = Dict.fromkeys(self.ATTRIBUTES)
        else:
            attributes = Dict(self.ATTRIBUTES)

        for key, value in attributes.iteritems():
            setattr(self, key, value)


def deactivate(*classes):
    for cls in classes:
        cls.ACTIVE = False
