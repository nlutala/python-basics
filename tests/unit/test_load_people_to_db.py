"""
Tests the load_people_to_db() function in create_and_load_data.py
"""

import os
import sqlite3

from create_and_load.fake_people.fake_people_records import load_people_to_db


def test_load_people_to_db_on_predefined_file():
    """
    There should be the same amount of records in the csv file that is loaded into the
    database.
    """
    test_files_dir = os.path.dirname(__file__)
    test_files_dir = os.path.join(test_files_dir, "test_files")

    con = sqlite3.connect("fake_people.db")
    cur = con.cursor()
    people_before_load = [row for row in cur.execute("SELECT * FROM people")]
    con.close()

    num_of_records = load_people_to_db(
        os.path.join(test_files_dir, "fake_person_data.csv")
    )

    con = sqlite3.connect("fake_people.db")
    cur = con.cursor()
    people_after_load = [row for row in cur.execute("SELECT * FROM people")]
    con.close()

    assert len(people_after_load) - len(people_before_load) == num_of_records

    os.remove("fake_people.db")
