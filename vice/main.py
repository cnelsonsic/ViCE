#!/usr/bin/env python2

from importlib import import_module

# load configuration
try:
    import config
except ImportError:
    config = {
        'ui': 'vice.ui.command'
    }

ui = import_module(config['ui'])
ui.main()
