import os
import sqlite3
from typing import Generator

import pytest  # type: ignore

from create_and_load_data import (
    get_people,
    get_rows_of_people,
    load_people_to_db,
    write_people_to_csv_file,
)


# Python Basics: Unit testing
@pytest.fixture
def people() -> Generator:
    return get_people(1)


@pytest.fixture
def people_list(people: Generator) -> list:
    return get_rows_of_people(people)


def test_person_phone_number_returns_12_digits(people: Generator) -> None:
    phone_number = next(people).get("phone_number")

    # Get rid of the "+" character
    # and remove the spaces from the phone_number
    # Assert there are 12 digits in the phone number
    assert len(phone_number[1:].replace(" ", "")) == 12
    assert phone_number[1:].replace(" ", "").isnumeric()


def test_next_people_returns_a_dictionary_with_table_fields(people: Generator) -> None:
    person = next(people)

    assert str(type(person)) == "<class 'dict'>"
    assert list(person.keys()) == [
        "id",
        "full_name",
        "first_name",
        "last_name",
        "email_address",
        "phone_number",
        "linkedin_profile",
    ]


def test_write_people_to_csv_file(people_list: list) -> None:
    write_people_to_csv_file(people_list, "test_fake_person_data_2.csv")

    assert "test_fake_person_data_2.csv" in os.listdir()

    with open("test_fake_person_data_2.csv", "r") as file:
        file_rows = [row.strip() for row in file]

    assert people_list[0] == file_rows[0].split(",")

    os.remove("test_fake_person_data_2.csv")


def test_load_fake_person_data(people: Generator) -> None:
    # Get the row of a person to write to the csv file
    people_rows = get_rows_of_people(people)

    # Write the row of the person to write to the csv file
    write_people_to_csv_file(people_rows, "test_fake_person_data_2.csv")

    # Create the table in the fake_people database
    load_people_to_db("test_fake_person_data_2.csv")

    # Check that there is one row that was inserted into the table
    con = sqlite3.connect("fake_people.db")
    cur = con.cursor()
    query_result = [row for row in cur.execute("SELECT * FROM people")]
    con.close()

    first_person_record = people_rows[0]  # Get the first row

    assert len(query_result) == 1
    assert query_result[0][0] == first_person_record[0]
    assert query_result[0][1] == first_person_record[1]
    assert query_result[0][2] == first_person_record[2]
    assert query_result[0][3] == first_person_record[3]
    assert query_result[0][4] == first_person_record[4]
    assert query_result[0][5] == first_person_record[5]
    assert query_result[0][6] == first_person_record[6]

    os.remove("test_fake_person_data_2.csv")
    os.remove("fake_people.db")
