import csv
import os
import sqlite3
from random import choice, randint

from faker import Faker  # type: ignore

from country_codes import country_codes

# Python Basics: Python scope and LEGB rule
# Global variable
CSV_FILE_NAME = "fake_person_data.csv"
NUM_OF_FAKE_PEOPLE_TO_GENERATE = 1000


def generate_random_phone_number() -> str:
    """
    Creates a random phone number

    returns a phone number with an area code as a string
    """
    area_code = choice(country_codes).get("dial_code")
    area_code = "" if area_code is None else area_code
    numbers_to_generate = (13 + area_code.count(" ")) - len(area_code)
    phone_number = f"""{area_code} {
        ''.join(
            [str(randint(0,9)) for i in range(numbers_to_generate)]
        )
    }"""
    return phone_number


def create_fake_person_data():
    """
    Creates a fake profile for a person to later write to a table.

    returns a dictionary containing the fake person's fake data as key, value pairs:
    id,
    full_name,
    first_name,
    last_name,
    email_address,
    phone_number,
    linkedin_profile
    """
    while True:
        full_name = Faker().name()

        if "." in full_name.split(" ")[0]:
            first_name = full_name.split(" ")[1]
            last_name = full_name.split(" ")[2]
        else:
            first_name = full_name.split(" ")[0]
            last_name = full_name.split(" ")[1]

        email_address = f"{first_name.lower()}.{last_name.lower()}@example.com"
        phone_number = generate_random_phone_number()
        linkedin_profile = f"""
                wwww.linkedin.com/{first_name.lower()}-{last_name.lower()}
        """.strip()

        person = {
            "id": None,
            "full_name": full_name,
            "first_name": first_name,
            "last_name": last_name,
            "email_address": email_address,
            "phone_number": phone_number,
            "linkedin_profile": linkedin_profile,
        }

        yield person


def write_fake_person_data_to_csv_file(
    fake_person_data: dict, csv_file_name=CSV_FILE_NAME
) -> None:
    """
    Writes data about a fake person to a csv file (or creates it if it doesn't exist)

    :param - fake_person_data (list) as returned by creater_fake_person_data()
    :param - the name of the csv file you want to create (including the extension)
    """

    with open(csv_file_name, "a", newline="\n") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(list((fake_person_data).values()))


def load_fake_person_data(file_name: str) -> None:
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
    file = open(file_name, "r", newline="\n")
    reader = csv.reader(file, delimiter=",")
    data = [(row) for row in reader]
    file.close()

    cur.executemany("INSERT INTO people VALUES(?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()
    con.close()


# Intermediate Python: Generators
def id_generator(row_count=0):
    """
    Yields the next id based on the number of rows currently in the
    fake_person_data.csv file.

    :param - row_count (int) - the starting id number (optional - if this is not given
    the starting id will be 0)
    """
    num = row_count
    while num <= NUM_OF_FAKE_PEOPLE_TO_GENERATE + num:
        yield num
        num += 1


if __name__ == "__main__":
    try:
        file = open(CSV_FILE_NAME, "r", newline="\n")
        reader = csv.reader(file, delimiter=",")
        row_count = sum([1 for _ in reader])
        file.close()
    except FileNotFoundError:
        row_count = 0

    id = id_generator(row_count)
    person_generator = create_fake_person_data()

    # Python Basics: Control Flow and Functions
    for i in range(NUM_OF_FAKE_PEOPLE_TO_GENERATE):
        # Step 1 - Create data about a fake person
        # Step 2 - Write the data about the fake person to a csv file
        person = next(person_generator)
        person["id"] = next(id)
        write_fake_person_data_to_csv_file(person)

    # Step 3 - Load the data about the fake people into a database
    load_fake_person_data(CSV_FILE_NAME)

    os.remove(CSV_FILE_NAME)
