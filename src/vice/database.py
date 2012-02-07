from plugins import Scheme

def connect(scheme, location="."):
    schemes = Scheme.plugins()
    if scheme.lower() not in schemes.keys():
        print "{0} is an invalid scheme type. Valid schemes:\n\t{1}".format(scheme, schemes.keys())
    else:
        return schemes[scheme](location)

def from_plugin(plugin):
    return (plugin.NAME, plugin.ATTRIBUTES)
