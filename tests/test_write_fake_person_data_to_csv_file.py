import csv
import os
from random import choice

from faker import Faker  # type: ignore

# Python Basics: Unit testing


def test_create_fake_person_data_loads_fake_person_data_into_a_csv_file():
    full_name = Faker().name()

    if "." in full_name.split(" ")[0]:
        first_name = full_name.split(" ")[1]
        last_name = full_name.split(" ")[2]
    else:
        first_name = full_name.split(" ")[0]
        last_name = full_name.split(" ")[1]

    email_address = email = (
        f"""
        {first_name.lower()}.{last_name.lower()}@example.com
        """.strip()
    )

    phone_number = "".join(
        [choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]) for i in range(12)]
    )

    linkedin_profile = f"wwww.linkedin.com/{first_name.lower()}-{last_name.lower()}"

    with open("test_fake_person_data.csv", "w", newline="\n") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(
            [
                0,
                full_name,
                first_name,
                last_name,
                email_address,
                phone_number,
                linkedin_profile,
            ]
        )

    assert "test_fake_person_data.csv" in os.listdir()
    os.remove("test_fake_person_data.csv")
