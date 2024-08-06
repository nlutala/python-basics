import csv
import os
import sqlite3
from random import choice, randint
from uuid import uuid4

from faker import Faker  # type: ignore

from country_codes import country_codes

# Python Basics: Python scope and LEGB rule
# Global variable
CSV_FILE_NAME = "fake_person_data.csv"
NUM_OF_PEOPLE_TO_GENERATE = 1000


def get_phone_number() -> str:
    """
    Returns a phone number with an area code as a string
    """

    area_code = choice(country_codes).get("dial_code")
    area_code = "" if area_code is None else area_code
    numbers_to_generate = (13 + area_code.count(" ")) - len(area_code)
    phone_number = f"""{area_code} {
        ''.join(
            [str(randint(0,9)) for i in range(numbers_to_generate)]
        )
    }""".strip()
    return phone_number


def get_person(num_of_people_to_generate=NUM_OF_PEOPLE_TO_GENERATE):
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
    "linkedin_profile": str, \n
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


def get_rows_of_people(person_iterator) -> list:
    """
    Returns rows of people to add to the database \n

    :param - person_iterator (generator/lazy iterator) a generator storing people to add
    to the database
    """

    people = []

    while True:
        try:
            people.append(next(person_iterator).values())
        except StopIteration:
            return people


def write_people_to_csv_file(people: list, csv_file_name=CSV_FILE_NAME) -> None:
    """
    Writes data about a fake person to a csv file (or creates it if it doesn't exist) \n

    :param - people (list) - rows of people to add to the database \n
    :param - csv_file_name (str) - the name of the csv file you want to create
    (including the .csv extension)
    """

    with open(csv_file_name, "a", newline="\n") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerows(people)


def load_people_to_db(csv_file_name: str) -> None:
    """
    Writes data about a fake people from a csv file to a database \n

    :param - csv_file_name (str) - the csv file to read the rows of people from and
    write to the database.
    """

    # Create a database called fake_people
    con = sqlite3.connect("fake_people.db")
    cur = con.cursor()

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


if __name__ == "__main__":
    # Step 1 - Create data about fake people
    person = get_person(NUM_OF_PEOPLE_TO_GENERATE)

    # Step 2 - Write the data about the fake person to a csv file
    people = get_rows_of_people(person)
    write_people_to_csv_file(people)

    # Step 3 - Load the data about the fake people into a database
    load_people_to_db(CSV_FILE_NAME)

    # Step 4 (optional) - Remove the csv file of fake people generated
    # os.remove(CSV_FILE_NAME)
