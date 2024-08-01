import csv
import os
import sqlite3
from random import choice

from faker import Faker  # type: ignore

# Python Basics: Python scope and LEGB rule
# Global variable
CSV_FILE_NAME = "fake_person_data.csv"


def create_fake_person_data() -> dict[str, str]:
    """
    Creates a fake profile for a person to later write to a table.

    returns a dictionary containing the fake person's fake data as key, value pairs:
    full_name,
    first_name,
    last_name,
    email_address,
    phone_number,
    linkedin_profile
    """
    full_name = Faker().name()

    if "." in full_name.split(" ")[0]:
        first_name = full_name.split(" ")[1]
        last_name = full_name.split(" ")[2]
    else:
        first_name = full_name.split(" ")[0]
        last_name = full_name.split(" ")[1]

    email_address = f"{first_name.lower()}.{last_name.lower()}@example.com"
    phone_number = "".join([choice([str(i) for i in range(10)]) for j in range(12)])
    linkedin_profile = f"wwww.linkedin.com/{first_name.lower()}-{last_name.lower()}"
    return {
        "id": None,
        "full_name": full_name,
        "first_name": first_name,
        "last_name": last_name,
        "email_address": email_address,
        "phone_number": phone_number,
        "linkedin_profile": linkedin_profile,
    }


def write_fake_person_data_to_csv_file(
    fake_person_data: dict, id: int, csv_file_name=CSV_FILE_NAME
) -> None:
    """
    Writes data about a fake person to a csv file (or creates it if it doesn't exist)

    :param - fake_person_data (list) as returned by creater_fake_person_data()
    :param - id (int) a unique identifier for this fake person
    :param - the name of the csv file you want to create (including the extension)
    """
    fake_person_data["id"] = id

    write_mode = "a" if csv_file_name in os.listdir() else "w"

    with open(csv_file_name, write_mode, newline="\n") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(list((fake_person_data).values()))


def load_fake_person_data(file_name: str):
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
    cur.executemany("INSERT INTO people VALUES(?, ?, ?, ?, ?, ?, ?)", data)
    con.commit()
    con.close()
    file.close()


if __name__ == "__main__":
    # Python Basics: Control Flow and Functions
    for i in range(1000):
        # Step 1 - Create data about a fake person
        person_data = create_fake_person_data()
        # Step 2 - Write the data about the fake person to a csv file
        write_fake_person_data_to_csv_file(person_data, i)

    # Step 3 - Load the data about the fake people into a database
    load_fake_person_data(CSV_FILE_NAME)

    os.remove(CSV_FILE_NAME)
