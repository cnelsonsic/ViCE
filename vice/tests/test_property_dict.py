from vice import PropertyDict

def test_assignment_and_access():
    fields = PropertyDict()
    fields.name = "Joe"

    assert fields.name == fields['name']
