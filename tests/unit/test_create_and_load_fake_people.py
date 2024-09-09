"""
Tests the get_people() method in create_and_load_data.py
"""

import os
import sqlite3
from unittest.mock import Mock

from create_and_load.fake_people.fake_people_records import (
    get_people,
    get_phone_number,
    get_rows_of_people,
    load_people_to_db,
)
from pytest_mock import mocker


def test_get_people_returns_a_generator_of_x_people(mocker: Mock):
    """
    The get_people() function should return a generator of a number of people specified
    in the parameters.
    """

    # Create the mock object to consistently return a phone number of "+44 7123456789"
    mocker.patch(
        "create_and_load.fake_people.fake_people_records.get_phone_number",
        return_value="+44 7123456789",
    )

    num_of_people = 5
    people = [person for person in get_people(num_of_people)]

    assert len(people) == num_of_people

    # Confirm that the mock object has worked and all people generated have the same
    # phone number
    assert people[0].get("phone_number") == "+44 7123456789"
    assert people[1].get("phone_number") == "+44 7123456789"
    assert people[2].get("phone_number") == "+44 7123456789"
    assert people[3].get("phone_number") == "+44 7123456789"
    assert people[4].get("phone_number") == "+44 7123456789"


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
    # Create the mock object to consistently return a phone number of "+44 7123456789"
    mocker.patch(
        "create_and_load.fake_people.fake_people_records.get_phone_number",
        return_value="+44 7123456789",
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
    assert people[0].get("phone_number") == "+44 7123456789"
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
                "phone_number": "+44 1234567891",
                "linkedin_profile": "www.linkedin.com/adam-bowman",
            },
            {
                "id": "mock_person_11",
                "full_name": "Catherine Daniels",
                "first_name": "Catherine",
                "last_name": "Daniels",
                "email_address": "catherine.daniels@example.com",
                "phone_number": "+44 2345678912",
                "linkedin_profile": "www.linkedin.com/catherine-daniels",
            },
            {
                "id": "mock_person_12",
                "full_name": "Esther Frank",
                "first_name": "Esther",
                "last_name": "Frank",
                "email_address": "esther.frank@example.com",
                "phone_number": "+44 3456789123",
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
            "+44 1234567891",
            "www.linkedin.com/adam-bowman",
        ],
        [
            "mock_person_11",
            "Catherine Daniels",
            "Catherine",
            "Daniels",
            "catherine.daniels@example.com",
            "+44 2345678912",
            "www.linkedin.com/catherine-daniels",
        ],
        [
            "mock_person_12",
            "Esther Frank",
            "Esther",
            "Frank",
            "esther.frank@example.com",
            "+44 3456789123",
            "www.linkedin.com/esther-frank",
        ],
    ]


def test_load_people_to_db_on_predefined_file():
    """
    There should be the same amount of records in the csv file that is loaded into the
    database.
    """
    current_dir = os.path.dirname(__file__)
    test_files_dir = os.path.join(current_dir, "test_files")

    # Get the amount of records before loading people to the db
    parent_dir = current_dir.partition("tests")[0]
    path_to_db = os.path.join(parent_dir, "fake_people.db")
    con = sqlite3.connect(path_to_db)
    cur = con.cursor()
    records_before = [row for row in cur.execute("SELECT * FROM people")]
    con.close()

    num_of_records = load_people_to_db(
        os.path.join(test_files_dir, "fake_person_data.csv")
    )

    con = sqlite3.connect(path_to_db)
    cur = con.cursor()
    records_after = [row for row in cur.execute("SELECT * FROM people")]
    con.close()

    assert num_of_records == len(records_after) - len(records_before)
