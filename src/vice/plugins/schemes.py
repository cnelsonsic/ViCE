import io, os

from vice import Dict
from vice.plugins import Plugin

#TODO: returning True/False seems confusing. Raise exceptions instead?

class SchemeError(Exception):
    def __init__(self, value):
        self.value = value

        def __str__(self):
            return repr(self.value)


class Scheme(Plugin):
    FILENAME = 'database'
    NAME = None

    def __init__(self, path="."):
        path = os.path.join(path, self.FILENAME)
        self.absolutePath = os.path.abspath(path)
        self.tables = []

    def createTable(name, fields):
        raise NotImplementedError("All Scheme plugins must implement a "
                                  "createTable method!")

    def createRecord(**fields):
        raise NotImplementedError("All Scheme plugins must implement a "
                                  "createRecord method!")

    def updateRecord(**fields):
        raise NotImplementedError("All Scheme plugins must implement a "
                                  "updateRecord method")


class FlatFileScheme(Scheme):
    NAME = 'flat-file'

    def __init__(self, location="."):
        super(FlatFileScheme, self).__init__(location)

        if not os.path.exists(self.absolutePath):
            os.makedirs(self.absolutePath)
        else:
            #TODO: actually read contents of flat-file database
            pass

    def createTable(self, name, *fields):
        tableLocation = os.path.join(self.absolutePath, name)
        if os.path.exists(tableLocation):
            return False
        else:
            try:
                io.open(tableLocation, "w").write("")
            except IOError:
                print("table {0} already exists.")
                return False

            self.tables.append(name)
            setattr(self, name,
                Dict(
                    fields = fields,
                    location = tableLocation,
                    records = []
                )
            )

            return True

    def createRecord(self, table, **fields):
        try:
            currentTable = getattr(self, table)
        except AttributeError:
            return False

        try:
            with io.open(getattr(self, table).location, "a") as f:
                f.write(" ".join([str(field)
                        for field in sorted(fields.values())]))
        except IOError:
            return False

        currentTable.records.append(fields)

        return True
