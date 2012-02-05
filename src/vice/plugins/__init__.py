class Dict(dict):

    def __getattr__(self, attr):
        return self.get(attr, None)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class Plugin(object):

    active = True

    @classmethod
    def plugins(cls, *args, **kwargs):
        return Dict((subclass.name, subclass(*args, **kwargs))
                    for subclass in cls.__subclasses__()
                    if subclass.active)


class Action(Plugin):

    def __call__(self):
        raise NotImplementedError("All actions should implement __call__!")


class Item(Plugin):

    stored = False

class Test(Action):
    pass

def deactivate(*classes):
    for cls in classes:
        cls.active = False
