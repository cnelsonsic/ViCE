import os
from vice import Dict

class Plugin(object):

    ACTIVE = True

    @classmethod
    def plugins(cls):
        cls._plugins = []

        def findSubclasses(cls):
            subclasses = cls.__subclasses__()

            if subclasses:
                cls._plugins += subclasses

                for subclass in subclasses:
                    findSubclasses(subclass)

        findSubclasses(cls)

        return Dict((plugin.NAME, plugin)
                    for plugin in cls._plugins if plugin.ACTIVE)


def deactivate(*classes):
    for cls in classes:
        cls.ACTIVE = False