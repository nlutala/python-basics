"""
Tests the load_people_to_db() function in create_and_load_data.py
"""

import os
import sqlite3

from create_and_load_data import load_people_to_db


def test_load_people_to_db_on_predefined_file():
    num_of_records = load_people_to_db("fake_person_data.csv")
    con = sqlite3.connect("fake_people.db")
    cur = con.cursor()
    num_of_records_in_db = [row for row in cur.execute("SELECT * FROM people")]
    con.close()

    assert num_of_records == len(num_of_records_in_db)

    os.remove("fake_people.db")
