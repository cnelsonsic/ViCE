from vice import Dict
from vice.plugins import Plugin

class Action(Plugin):

    @classmethod
    def new(cls, function):
        return type(function.__name__, (cls,),
                    Dict(NAME=function.__name__, __call__=function))

    @classmethod
    def plugins(cls, *args, **kwargs):
        return Dict((pluginName, plugin(*args, **kwargs)) for pluginName, plugin
                    in super(Action, cls).plugins().items())

    def __call__(self):
        raise NotImplementedError('All actions should implement __call__!')
