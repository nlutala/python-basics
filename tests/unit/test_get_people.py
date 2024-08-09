"""
Tests the get_people() method in create_and_load_data.py
"""

from unittest.mock import Mock

from create_and_load_data import get_people


def test_get_people_returns_a_generator_of_x_people(mocker: Mock):
    """
    The get_people() function should return a generator of a number of people specified
    in the parameters.
    """
    # Create the mock object to consistently return a phone number of "+44 712345678"
    mocker.patch("create_and_load_data.get_phone_number", return_value="+44 712345678")

    num_of_people = 5
    people = [person for person in get_people(num_of_people)]

    assert len(people) == num_of_people

    # Confirm that the mock object has worked and all people generated have the same
    # phone number
    assert people[0].get("phone_number") == "+44 712345678"
    assert people[1].get("phone_number") == "+44 712345678"
    assert people[2].get("phone_number") == "+44 712345678"
    assert people[3].get("phone_number") == "+44 712345678"
    assert people[4].get("phone_number") == "+44 712345678"


def test_get_people_returns_a_generator_of_dictionaries_with_correct_fields(
    mocker: Mock,
):
    """
    The get_people() function should return a generator of dictionaries with the fields:
    \n
    "id",\n
    "full_name",\n
    "first_name",\n
    "last_name",\n
    "email_address",\n
    "phone_number",\n
    "linkedin_profile"
    """
    # Create the mock object to consistently return a phone number of "+44 712345678"
    mocker.patch("create_and_load_data.get_phone_number", return_value="+44 712345678")

    num_of_people = 1
    people = [person for person in get_people(num_of_people)]

    assert str(type(people[0])) == "<class 'dict'>"
    assert list(people[0].keys()) == [
        "id",
        "full_name",
        "first_name",
        "last_name",
        "email_address",
        "phone_number",
        "linkedin_profile",
    ]
    assert people[0].get("id") is not None
    assert people[0].get("full_name") is not None
    assert people[0].get("last_name") is not None
    assert people[0].get("email_address") is not None
    assert people[0].get("phone_number") == "+44 712345678"
    assert people[0].get("linkedin_profile") is not None
