from vice.plugins import Plugin

class Action(Plugin):

    @classmethod
    def new(cls, function):
        return type(function.__name__, (cls,),
                    Dict(NAME=function.__name__lower(), __call__=function))

    @classmethod
    def plugins(cls, *args, **kwargs):
        return Dict((plugin_name, plugin(*args, **kwargs)) for plugin_name, plugin
                    in super(Action, cls).plugins().iteritems())

    def __call__(self):
        raise NotImplementedError("All actions should implement __call__!")
