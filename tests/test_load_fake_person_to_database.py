import csv
import os
import sqlite3

from create_and_load_data import (
    create_fake_person_data,
    write_fake_person_data_to_csv_file,
)

# Python Basics: Unit testing


def test_load_fake_person_data():
    # Generate fake data
    fake_person_generator = create_fake_person_data()
    fake_person = next(fake_person_generator)

    # Write this fake data to a file
    write_fake_person_data_to_csv_file(fake_person, 0, "test_fake_person_data.csv")

    # Create a database called fake_people
    con = sqlite3.connect("test_fake_people.db")
    cur = con.cursor()

    # Create the table in the fake_people database
    cur.execute(
        """
        CREATE TABLE test_people(
            id,
            full_name,
            first_name,
            last_name,
            email_address,
            phone_number,
            linkedin_profile
        )
        """
    )

    # Insert the data about the fake people from the csv into the table
    file = open("test_fake_person_data.csv", "r", newline="\n")
    reader = csv.reader(file, delimiter=",")
    data = [(row) for row in reader]
    cur.executemany("INSERT INTO test_people VALUES(?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()

    # Check that there is one row that was inserted into the table
    query_result = [row for row in cur.execute("SELECT * FROM test_people")]
    assert len(query_result) == 1

    # Check the contents of the fields
    assert query_result[0][0] == str(fake_person.get("id"))
    assert query_result[0][1] == fake_person.get("full_name")
    assert query_result[0][2] == fake_person.get("first_name")
    assert query_result[0][3] == fake_person.get("last_name")
    assert query_result[0][4] == fake_person.get("email_address")
    assert query_result[0][5] == fake_person.get("phone_number")
    assert query_result[0][6] == fake_person.get("linkedin_profile")

    con.close()
    os.remove("test_fake_person_data.csv")
    os.remove("test_fake_people.db")
