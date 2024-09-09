"""
Tests the get_contacts() method in
./create_and_load/fake_contacts/fake_contact_records.py
"""

from unittest.mock import Mock

from create_and_load.fake_contacts.fake_contact_records import get_contacts
from pytest_mock import mocker


def test_get_contacts_returns_a_generator_of_x_people(mocker: Mock):
    """
    The get_contacts() function should return a generator of a number of contacts
    specified in the parameters.
    """

    # Create the mock object to consistently return a phone number of "+44 7123456789"
    mocker.patch(
        "create_and_load.fake_contacts.fake_contact_records.get_phone_number",
        return_value="+44 7123456789",
    )

    num_of_contacts = 5
    contacts = [contact for contact in get_contacts(num_of_contacts)]

    assert len(contacts) == num_of_contacts

    for contact in contacts:
        # Confirm that the length of each record in the contact is 3
        assert len(contact) == 3

        # Confirm that the mock object has worked and all people generated have the same
        # phone number
        assert contact[2] == "+44 7123456789"
