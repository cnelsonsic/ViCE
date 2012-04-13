from vice import Dict
from vice.plugins import Plugin
from vice.plugins.items import Card

class Container(Plugin, list):

    CONTAINS = None

class Hand(Container, list):
    # keys are item types
    # values is a dictionary of attribute: restriction pairs
    CONTAINS = Dict(
        Card = Dict(
            types = ["foo", "bar"]
        )
    )
