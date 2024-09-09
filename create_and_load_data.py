"""
The main .py file to run which creates records of fake people, writes them to a .csv
file and then writes these records of fake people from the .csv file to a database.
"""

import os

from create_and_load.fake_people.fake_people_records import (
    CSV_FILE_NAME,
    get_people,
    get_rows_of_people,
    load_people_to_db,
    write_people_to_csv_file,
)

# Python Basics: Python scope and LEGB rule
# Global variables
NUM_OF_PEOPLE_TO_GENERATE = 1000

if __name__ == "__main__":
    # Step 1 - Create data about fake people
    people = get_people(NUM_OF_PEOPLE_TO_GENERATE)

    # Step 2 - Get the records of people from the generator
    people_records = get_rows_of_people(people)

    # Step 3 - Write the data about the fake person to a csv file
    write_people_to_csv_file(people_records)

    # Step 4 - Load the data about the fake people into a database
    num_of_rows = load_people_to_db(CSV_FILE_NAME)

    # Step 5 (optional) - Remove the csv file of fake people generated
    os.remove(CSV_FILE_NAME)
