import os
import sqlite3

from create_and_load_data import (
    get_person,
    get_rows_of_people,
    load_people_to_db,
    write_people_to_csv_file,
)

# Python Basics: Unit testing


def test_first_name_is_one_word_long():
    person = get_person(1)
    someone = list(get_rows_of_people(person)[0])
    first_name = someone[2]

    assert "." not in first_name
    assert " " not in first_name


def test_last_name_is_one_word_long():
    person = get_person(1)
    someone = list(get_rows_of_people(person)[0])
    last_name = someone[3]

    assert "." not in last_name
    assert " " not in last_name


def test_email_address_has_domain_at_example_dot_com():
    person = get_person(1)
    someone = list(get_rows_of_people(person)[0])
    email = someone[4]

    assert email.endswith("@example.com")


def test_phone_number_does_not_contain_letters():
    person = get_person(1)
    someone = list(get_rows_of_people(person)[0])
    phone_number = someone[5]

    # Get rid of the "+" character
    # and remove the spaces from the phone_number
    assert phone_number[1:].replace(" ", "").isnumeric()


def test_linkedin_profile_contains_first_name_and_last_name():
    person = get_person(1)
    someone = list(get_rows_of_people(person)[0])
    first_name = someone[2]
    last_name = someone[3]
    linkedin_profile = someone[6]

    assert first_name.lower() in linkedin_profile
    assert last_name.lower() in linkedin_profile


def test_load_fake_person_data():
    # Generate fake data
    person = get_person(1)

    # Write this fake data to a file
    rows = get_rows_of_people(person)
    write_people_to_csv_file(rows, "test_fake_person_data.csv")

    # Create the table in the fake_people database
    load_people_to_db("test_fake_person_data.csv")

    # Check that there is one row that was inserted into the table
    con = sqlite3.connect("fake_people.db")
    cur = con.cursor()
    query_result = [row for row in cur.execute("SELECT * FROM people")]
    assert len(query_result) == 1

    con.close()

    rows = list(rows[0])

    assert query_result[0][0] == rows[0]
    assert query_result[0][1] == rows[1]
    assert query_result[0][2] == rows[2]
    assert query_result[0][3] == rows[3]
    assert query_result[0][4] == rows[4]
    assert query_result[0][5] == rows[5]
    assert query_result[0][6] == rows[6]

    os.remove("test_fake_person_data.csv")
    os.remove("fake_people.db")


def test_create_fake_person_data_loads_fake_person_data_into_a_csv_file():
    person = get_person(1)
    rows = get_rows_of_people(person)
    write_people_to_csv_file(rows, "test_fake_person_data.csv")

    assert "test_fake_person_data.csv" in os.listdir()
    os.remove("test_fake_person_data.csv")
