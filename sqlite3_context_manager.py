"""
A module used to extract all the rows of the tables in the database

Author: nlutala (Nathan Lutala)
"""

import csv
import os
import sqlite3


class DBContextManager:
    def __init__(self, path_to_db: str):
        """
        The object constructor\ns
        :param - path_to_db (str) - the complete path to the sqlite3 databases
        """
        self.path_to_db: str = path_to_db

    def __enter__(self) -> dict[str, list[list[str]]]:
        # Get all the tables in this database
        # table_contents is made up of a dictionary of table_name and table_contents
        # {name_of_table: [headers + rows]}
        table_contents: dict[str, list[list[str]]] = {}

        # 1. Check whether the sqlite3 database exists in the directory
        temp: list[str] = self.path_to_db.replace("\\", "/").split("/")
        parent_dir: str = "/".join(temp[: len(temp) - 2])
        parent_dir: str = None if parent_dir == "" else parent_dir
        db: str = temp[-1]

        if db not in os.listdir(parent_dir):
            if parent_dir is None:
                raise FileNotFoundError(f"Database ({db}) does not exist.")
            else:
                raise FileNotFoundError(
                    f"Database ({db}) does not exist in {parent_dir}."
                )

        # 2. Get all the tables that exist in the database
        tables: list[str] = self._get_list_of_tables_in_db()

        # 3. Get all the headers and rows for each table in the database
        con: sqlite3.Connection = sqlite3.connect(self.path_to_db)
        cur: sqlite3.Cursor = con.cursor()

        for table in tables:
            res: sqlite3.Cursor = cur.execute(f"SELECT * FROM {table}")
            headers: list[str] = [[header[0] for header in res.description]]
            rows: list[str] = [list(row) for row in res]
            # Add this to the table_contents dictionary
            table_contents[table] = headers + rows

        con.close()

        return table_contents

    def _get_list_of_tables_in_db(self) -> list[str]:
        """
        Return a list of all the tables in the database
        """
        con: sqlite3.Connection = sqlite3.connect(self.path_to_db)
        cur: sqlite3.Cursor = con.cursor()
        tables: list[str] = [
            table[0]
            for table in cur.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            )
        ]
        con.close()

        return tables

    def __exit__(self, exc_type, exc_value, exc_tb) -> tuple:
        return exc_type, exc_value, exc_tb
