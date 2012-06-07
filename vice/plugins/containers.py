from vice.plugins import Plugin, PluginMeta

class ContainerMeta(PluginMeta):

    def __new__(cls, name, bases, attrs):
        attrs['items'] = []

        return super(ContainerMeta, cls).__new__(cls, name, bases, attrs)


ContainerBase = ContainerMeta('ContainerBase', (Plugin,), {})


class Container(ContainerBase):

    def __len__(self):
        return len(self.items)

    @classmethod
    def new(cls, function):

        class_name = function.__name__.title().replace('_', '')

        return ContainerMeta(class_name, (cls,), dict(
            NAME=class_name,
            consraints=function
        ))


    def constraints(self, item):
        raise NotImplementedError(
            'All containers should implement a filters method!'
        )

    def add(self, item):
        if all(self.constraints(item)):
            self.items.append(item)
            return True
        else:
            return False
