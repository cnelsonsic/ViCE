import os, sys
sys.path.insert(0, os.path.abspath(os.path.join('..')))

from vice import database
from vice.plugins.items import Item
from vice.plugins.schemes import FlatFileScheme

from wtactics.items import WtCard
