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
    def new(cls, name, function):

        return ContainerMeta(name, (cls,), dict(
            NAME=name,
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
