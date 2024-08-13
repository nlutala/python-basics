"""
A file to test the integration
"""

import csv
import os
import sqlite3

from create_and_load_data import load_people_to_db, write_people_to_csv_file
from fake_people.fake_people_records import get_people, get_rows_of_people


def test_step_1_and_step_2():
    """
    Test that you can create a generator of people (i.e. step 1) and get the records of
    people from the generator (step 2)
    """

    # Step 1
    people = get_people(5)

    # Step 2
    people_records = get_rows_of_people(people)

    assert len(people_records) == 5

    for i, person in enumerate(people):
        assert person.get("id") == people_records[i][0]
        assert person.get("full_name") == people_records[i][1]
        assert person.get("first_name") == people_records[i][2]
        assert person.get("last_name") == people_records[i][3]
        assert person.get("email_address") == people_records[i][4]
        assert person.get("phone_number") == people_records[i][5]
        assert person.get("linkedin_profile") == people_records[i][6]


def test_step_2_and_step_3():
    """
    Test that you can get the rows of people from the generator (step 2) and write
    the rows of people to a csv file (step 3)
    """
    people = get_people(4)

    # Step 2
    people_records = get_rows_of_people(people)

    # Step 3
    test_files_dir = os.path.dirname(__file__)
    test_file = os.path.join(test_files_dir, "fake_people_data_step_2_to_3.csv")

    write_people_to_csv_file(people_records, test_file)

    with open(test_file, "r", newline="\n") as file:
        reader = csv.reader(file, delimiter=",")
        rows = [row for row in reader]

    assert len(rows) == len(people_records)

    for i, row in enumerate(rows):
        assert row[0] == people_records[i][0]
        assert row[1] == people_records[i][1]
        assert row[2] == people_records[i][2]
        assert row[3] == people_records[i][3]
        assert row[4] == people_records[i][4]
        assert row[5] == people_records[i][5]
        assert row[6] == people_records[i][6]

    os.remove(test_file)


def test_step_3_and_step_4():
    """
    Test that you can write the rows of people to a csv file (step 3) and load the rows
    of people as records to a database (step 4)
    """
    people = get_people(2)
    people_records = get_rows_of_people(people)

    # Step 3
    test_files_dir = os.path.dirname(__file__)
    test_file = os.path.join(test_files_dir, "fake_people_data_step_3_to_4.csv")

    write_people_to_csv_file(people_records, test_file)

    with open(test_file, "r", newline="\n") as file:
        reader = csv.reader(file, delimiter=",")
        rows_in_csv = [row for row in reader]

    # Step 4
    load_people_to_db(test_file)

    con = sqlite3.connect("fake_people.db")
    cur = con.cursor()
    records_in_db = [row for row in cur.execute("SELECT * FROM people")]
    con.close()

    assert len(rows_in_csv) == len(records_in_db)

    for i, row in enumerate(rows_in_csv):
        assert row[0] == records_in_db[i][0]
        assert row[1] == records_in_db[i][1]
        assert row[2] == records_in_db[i][2]
        assert row[3] == records_in_db[i][3]
        assert row[4] == records_in_db[i][4]
        assert row[5] == records_in_db[i][5]
        assert row[6] == records_in_db[i][6]

    os.remove(test_file)
    os.remove("fake_people.db")
