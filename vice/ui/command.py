from cmd import Cmd

plugin_template = """\
import os
import sys
from vice.databse import Database
from vice.plugins import Action, Container, Item

DB_FILE = {db_file}
DB_DRIVER = 'sqlite'

# DO NOT EDIT BELOW THIS LINE!
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), DB_FILE))

if DB_DRIVER == 'sqlite':
    db = Database('sqlite:////' + db_path)
else:
    print(DB_DRIVER + "driver not implemented, sorry!")
    sys.exit(1)

"""

item_template = """\
{item_name} = Item.new('{item_name}', attributes=(
    {item_attrs}
))
"""

class ViceConsole(Cmd):

    def do_generate(self, line):
        with open('foo.py', 'w') as f:
            plugin_template.format(
                db_file='foo.db'
            )
            f.write(plugin_template)


if __name__ == '__main__':
    ViceConsole().cmdloop()
