"""
A file that includes functions to help generate records of fake people.
"""

import csv
import os
import sqlite3
from uuid import uuid4

from faker import Faker

from create_and_load.phone_numbers.phone_number import get_phone_number
from decorators import log_activity

CSV_FILE_NAME = "fake_person_data.csv"


def get_people(num_of_people_to_generate=10):
    """
    Yields a list containing the fake person's fake data as a dictionary

    :param - num_of_people_to_generate (int)

    Returns a generator of people as key, value pairs: \n
    "id": str, \n
    "full_name": str, \n
    "first_name": str, \n
    "last_name": str, \n
    "email_address": str, \n
    "phone_number": str, \n
    "linkedin_profile": str
    """

    for i in range(num_of_people_to_generate):
        full_name = Faker().name()

        if "." in full_name.split(" ")[0]:
            first_name = full_name.split(" ")[1]
            last_name = full_name.split(" ")[2]
        else:
            first_name = full_name.split(" ")[0]
            last_name = full_name.split(" ")[1]

        email_address = f"{first_name.lower()}.{last_name.lower()}@example.com"
        phone_number = get_phone_number()
        linkedin_profile = f"""
                wwww.linkedin.com/{first_name.lower()}-{last_name.lower()}
        """.strip()

        person = {
            "id": str(uuid4()),
            "full_name": full_name,
            "first_name": first_name,
            "last_name": last_name,
            "email_address": email_address,
            "phone_number": phone_number,
            "linkedin_profile": linkedin_profile,
        }

        yield person


def get_rows_of_people(person_iterator) -> list[list[str]]:
    """
    Returns rows of people to add to the database as a list of dictionary values \n

    :param - person_iterator (generator/lazy iterator) a generator storing people to add
    to the database

    Returns a list of a list of records for each person
    """

    people = []

    while True:
        try:
            people.append(list(next(person_iterator).values()))
        except StopIteration:
            return people


@log_activity
def write_people_to_csv_file(
    people: list[list[str]], csv_file_name=CSV_FILE_NAME
) -> None:
    """
    Writes data about a fake person to a csv file (or creates it if it doesn't exist)\n

    :param - people (list of a list of strings) - rows of people to add to the
    database\n
    :param - csv_file_name (str) - the name of the csv file you want to create
    (including the .csv extension)
    """

    with open(csv_file_name, "a", newline="\n") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerows(people)


@log_activity
def load_people_to_db(csv_file_name: str) -> int:
    """
    Writes data about a fake people from a csv file to a database \n

    :param - csv_file_name (str) - the csv file to read the rows of people from and
    write to the database.\n

    returns the number of rows written to the database
    """

    # Set initially to False as we will then check if the fake_people.db already exists
    parent_dir = os.path.dirname(__file__).partition("create_and_load")[0]
    path_to_db = os.path.join(parent_dir, "fake_people.db")
    only_insert = True if "fake_people.db" in os.listdir(parent_dir) else False

    # Create a database called fake_people
    con = sqlite3.connect(path_to_db)
    cur = con.cursor()

    if only_insert is False:
        # Create the table in the fake_people database
        cur.execute(
            """
            CREATE TABLE people(
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
    with open(csv_file_name, "r", newline="\n") as file:
        reader = csv.reader(file, delimiter=",")
        data = [(row) for row in reader]

    cur.executemany("INSERT INTO people VALUES(?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()
    con.close()

    return len(data)
