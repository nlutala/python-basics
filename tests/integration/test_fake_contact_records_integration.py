from create_and_load.fake_contacts.fake_contact_records import get_contacts


def test_get_contacts_returns_contacts():
    """
    create_and_load.fake_contacts.fake_contact_records.get_contacts() should return a
    lazy iterator of lists with a length of 3 elements, signifying a contact's id, name
    and phone_number (respectively)
    """
    contacts = get_contacts(3)

    assert str(type(contacts)) == "<class 'generator'>"

    for contact in contacts:
        assert contact != []
        assert contact[2].startswith("+")
        assert len(contact[2][1:].replace(" ", "")) == 12
        assert contact[2][1:].replace(" ", "").isnumeric()
