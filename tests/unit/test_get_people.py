"""
Tests the get_people() method in create_and_load_data.py
"""

from unittest.mock import Mock

from fake_people.fake_people_records import (
    get_people,
    get_phone_number,
    get_rows_of_people,
)


def test_get_people_returns_a_generator_of_x_people(mocker: Mock):
    """
    The get_people() function should return a generator of a number of people specified
    in the parameters.
    """
    # Create the mock object to consistently return a phone number of "+44 712345678"
    mocker.patch(
        "fake_people.fake_people_records.get_phone_number", return_value="+44 712345678"
    )

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
    mocker.patch(
        "fake_people.fake_people_records.get_phone_number", return_value="+44 712345678"
    )

    people = [person for person in get_people(1)]

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


def test_get_rows_of_people_returns_a_record():
    # Create generic people
    people = iter(
        [
            {
                "id": "mock_person_10",
                "full_name": "Adam Bowman",
                "first_name": "Adam",
                "last_name": "Bowman",
                "email_address": "adam.bowman@example.com",
                "phone_number": "+44 123456789",
                "linkedin_profile": "www.linkedin.com/adam-bowman",
            },
            {
                "id": "mock_person_11",
                "full_name": "Catherine Daniels",
                "first_name": "Catherine",
                "last_name": "Daniels",
                "email_address": "catherine.daniels@example.com",
                "phone_number": "+44 234567891",
                "linkedin_profile": "www.linkedin.com/catherine-daniels",
            },
            {
                "id": "mock_person_12",
                "full_name": "Esther Frank",
                "first_name": "Esther",
                "last_name": "Frank",
                "email_address": "esther.frank@example.com",
                "phone_number": "+44 345678912",
                "linkedin_profile": "www.linkedin.com/esther-frank",
            },
        ]
    )

    rows_of_people = get_rows_of_people(people)

    assert len(rows_of_people) == 3
    assert rows_of_people == [
        [
            "mock_person_10",
            "Adam Bowman",
            "Adam",
            "Bowman",
            "adam.bowman@example.com",
            "+44 123456789",
            "www.linkedin.com/adam-bowman",
        ],
        [
            "mock_person_11",
            "Catherine Daniels",
            "Catherine",
            "Daniels",
            "catherine.daniels@example.com",
            "+44 234567891",
            "www.linkedin.com/catherine-daniels",
        ],
        [
            "mock_person_12",
            "Esther Frank",
            "Esther",
            "Frank",
            "esther.frank@example.com",
            "+44 345678912",
            "www.linkedin.com/esther-frank",
        ],
    ]
