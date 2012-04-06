from vice import Dict
from vice.plugins import Plugin


# should table be a separate object?

class Storage(Plugin):

    def __init__(self, location):
        self.location = location

    def createTable(self):
        pass

    def insert(self):
        pass

    def remove(self):
        pass

    def find(self):
        pass


def connect(uri):
    dbType, dbLocation = uri.split("://")
    databases = Database.plugins()

    return databases[dbType](dbLocation)


if __name__ == "__main__":
    # define a new item to test the databse API
    from vice.plugins.items import Card

    Card.new("WtCard", (
        "art", "border_color", "cost", "faction", "footer",
        "loyalty", "name", "text", "types", "stats"
    ))

    # Initialize a new database
    db = Database("sqlite://vice.db")
    # Create a new table, using a class as a template
    db.createTable("cards", WtCard.ATTRIBUTES)
    # Insert a new card into the database
    # Ideally, this would be automated, perhaps by converting an sql dump or web scrape
    db.cards.insert(
        art="foo.png",
        border_color="blue"
        #etc...
    )
    # Query the table
    results = db.cards.find(border_color="green")
    # Delete all cards with a border color of green
    db.cards.remove(border_color="green")
    # or perhaps it should be a two part step, where-by a query is passed to the delete?
    db.cards.remove(results)
