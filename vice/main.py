#!/usr/bin/env python2

from importlib import import_module
from vice import PropertyDict

# load configuration
try:
    import config
except ImportError:
    config = PropertyDict(
        ui='vice.ui.cli')

ui = import_module(config.ui)
ui.main()
