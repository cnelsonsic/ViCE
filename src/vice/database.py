from vice.plugins import Scheme

class SchemeError(Exception):
    def __init__(self, value):
        self.value = value

        def __str__(self):
            return repr(self.value)


def connect(scheme, location="."):
    schemes = Scheme.plugins()
    if scheme.lower() not in schemes.keys():
        if schemes:
            raise SchemeError("{scheme} is an invalid scheme type. Valid Scheme types (case-insensitive):\n"
                                 "\t{schemes}".format(scheme=scheme, schemes=schemes.keys()))
        else:
            raise SchemeError("No valid schemes have been imported or defined, cannot connect to a database.")
    else:
        return schemes[scheme](location)

def from_plugin(plugin):
    return (plugin.NAME, plugin.ATTRIBUTES)
