import os
from vice import PropertyDict

class Plugin(object):

    ACTIVE = True

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
                    for plugin in cls._plugins if plugin.ACTIVE)


def deactivate(*classes):
    for cls in classes:
        cls.ACTIVE = False
