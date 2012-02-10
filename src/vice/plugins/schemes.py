import io
import os

from vice import Dict
from vice.plugins import Scheme

#TODO: returning True/False seems confusing. Raise exceptions instead?

class FlatFileScheme(Scheme):
    NAME = 'flat-file'

    def __init__(self, location="."):
        super(FlatFileScheme, self).__init__(location)

        if not os.path.exists(self.absolute_path):
            os.makedirs(self.absolute_path)
        else:
            #TODO: actually read contents of flat-file database
            pass

    def create_table(self, name, *fields):
        table_location = os.path.join(self.absolute_path, name)
        if os.path.exists(table_location):
            return False
        else:
            try:
                io.open(table_location, "w").write("")
            except IOError:
                print("table {0} already exists.")
                return False

            self.tables.append(name)
            setattr(self, name,
                Dict(
                    fields = fields,
                    location = table_location,
                    records = []
                )
            )

            return True

    def create_record(self, table, **fields):
        try:
            current_table = getattr(self, table)
        except AttributeError:
            return False

        try:
            with io.open(getattr(self, table).location, "a") as f:
                f.write(" ".join([str(field)
                        for field in sorted(fields.values())]))
        except IOError:
            return False

        current_table.records.append(fields)

        return True

