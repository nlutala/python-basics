import csv
import os
import sqlite3

from create_and_load_data import get_person, load_people_to_db, write_people_to_csv_file

# Python Basics: Unit testing


def test_load_fake_person_data():
    # Generate fake data
    person = get_person(1)

    # Write this fake data to a file
    write_people_to_csv_file(person, "test_fake_person_data.csv")

    # Create a database called fake_people
    con = sqlite3.connect("fake_people.db")
    cur = con.cursor()

    # Create the table in the fake_people database
    load_people_to_db("test_fake_person_data.csv")

    # Check that there is one row that was inserted into the table
    con = sqlite3.connect("fake_people.db")
    cur = con.cursor()
    query_result = [row for row in cur.execute("SELECT * FROM people")]
    assert len(query_result) == 1

    con.close()
    os.remove("test_fake_person_data.csv")
    os.remove("fake_people.db")
