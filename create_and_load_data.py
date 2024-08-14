"""
The main .py file to run which creates records of fake people, writes them to a .csv
file and then writes these records of fake people from the .csv file to a database.
"""

import logging
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


if __name__ == "__main__":
    # Step 1 - Create data about fake people
    people = get_people(NUM_OF_PEOPLE_TO_GENERATE)

    # Step 2 - Get the records of people from the generator
    people_records = get_rows_of_people(people)
    LOGGER.info(f"Finished generating {len(people_records)} rows of people.")

    # Step 3 - Write the data about the fake person to a csv file
    write_people_to_csv_file(people_records)
    LOGGER.info(f"Wrote {len(people_records)} of people to {CSV_FILE_NAME}.")

    # Step 4 - Load the data about the fake people into a database
    num_of_rows = load_people_to_db(CSV_FILE_NAME)
    LOGGER.info(f"Wrote {num_of_rows} number of records to the database.")

    # Step 5 (optional) - Remove the csv file of fake people generated
    os.remove(CSV_FILE_NAME)
