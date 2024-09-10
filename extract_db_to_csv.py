"""
A script used to extract all the rows of tables in a database to csv file(s)

Author: nlutala (Nathan Lutala)
"""

import csv

from sqlite3_context_manager import DBContextManager

if __name__ == "__main__":
    with DBContextManager("fake_people.db") as cm:
        for key in cm.keys():
            with open(f"{key}.csv", "w") as csv_file:
                writer: csv._writer = csv.writer(csv_file, delimiter=",")
                writer.writerows(cm.get(key))
