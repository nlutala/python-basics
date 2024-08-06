import csv
import os
import sqlite3

from create_and_load_data import (
    get_person,
    get_rows_of_people,
    load_people_to_db,
    write_people_to_csv_file,
)

# Python Basics: Unit testing


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
