"""
The main .py file to run which creates records of fake people, writes them to a .csv
file and then writes these records of fake people from the .csv file to a database.
"""

import csv
import logging
import os
import sqlite3

from fake_people.fake_people_records import get_people, get_rows_of_people

# Python Basics: Python scope and LEGB rule
# Global variables
CSV_FILE_NAME = "fake_person_data.csv"
NUM_OF_PEOPLE_TO_GENERATE = 1000
LOGGER = logging.getLogger(__name__)

"""
Letting the logger know to write all logs at the info level (my logs) and above to a
file called create_and_load_data.log
"""
logging.basicConfig(
    filename="create_and_load_data.log",
    filemode="w",  # To write new content everytime the program is run again
    encoding="utf-8",
    level=logging.INFO,
)


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


def load_people_to_db(csv_file_name: str) -> int:
    """
    Writes data about a fake people from a csv file to a database \n

    :param - csv_file_name (str) - the csv file to read the rows of people from and
    write to the database.\n

    returns the number of rows written to the database
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

    return len(data)


if __name__ == "__main__":
    # Step 1 - Create data about fake people
    person = get_people(NUM_OF_PEOPLE_TO_GENERATE)

    # Step 2 - Write the data about the fake person to a csv file
    people = get_rows_of_people(person)
    LOGGER.info(f"Finished generating {len(people)} rows of people.")

    write_people_to_csv_file(people)
    LOGGER.info(f"Wrote {len(people)} of people to {CSV_FILE_NAME}.")

    # Step 3 - Load the data about the fake people into a database
    num_of_rows = load_people_to_db(CSV_FILE_NAME)
    LOGGER.info(f"Wrote {num_of_rows} number of records to the database.")

    # Step 4 (optional) - Remove the csv file of fake people generated
    os.remove(CSV_FILE_NAME)
