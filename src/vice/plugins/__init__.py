import os

class Dict(dict):

    def __getattr__(self, attr):
        return self.get(attr, None)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class Plugin(object):

    ACTIVE = True

    @classmethod
    def plugins(cls, *args, **kwargs):
        cls._plugins = []

        def find_subclasses(cls):
            subclasses = cls.__subclasses__()

            if subclasses:
                cls._plugins += subclasses

                for subclass in subclasses:
                    find_subclasses(subclass)

        find_subclasses(cls)

        return Dict((plugin.NAME, plugin)
                    for plugin in cls._plugins if plugin.ACTIVE)


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


class Scheme(Plugin):
    FILENAME = 'database'
    NAME = None

    def __init__(self, path="."):
        path = os.path.join(path, self.FILENAME)
        self.absolute_path = os.path.abspath(path)
        self.tables = []

    def create_table(name, *fields):
        raise NotImplementedError("All Scheme plugins must implement a "
                                  "create_table method!")

    def create_record(**fields):
        raise NotImplementedError("All Scheme plugins must implement a "
                                  "create_record method!")

    def update_record(**fields):
        raise NotImplementedError("All Scheme plugins must implement a "
                                  "update_record method")

def deactivate(*classes):
    for cls in classes:
        cls.ACTIVE = False

def newItem(name, attributes, base=Item):
    return type(name, (base,), dict(NAME = name.lower(), ATTRIBUTES=attributes))
