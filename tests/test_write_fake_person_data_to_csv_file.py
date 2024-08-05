import csv
import os
from random import choice

from create_and_load_data import get_person, write_people_to_csv_file

# Python Basics: Unit testing


def test_create_fake_person_data_loads_fake_person_data_into_a_csv_file():
    person = get_person(1)
    write_people_to_csv_file(person, "test_fake_person_data.csv")

    assert "test_fake_person_data.csv" in os.listdir()
    os.remove("test_fake_person_data.csv")
