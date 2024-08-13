"""
A file that includes functions to help generate records of fake people.
"""

from uuid import uuid4

from faker import Faker  # type: ignore

from phone_numbers.phone_number import get_phone_number


def get_people(num_of_people_to_generate=10):
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
    "linkedin_profile": str
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


def get_rows_of_people(person_iterator) -> list[str]:
    """
    Returns rows of people to add to the database as a list of dictionary values \n

    :param - person_iterator (generator/lazy iterator) a generator storing people to add
    to the database
    """

    people = []

    while True:
        try:
            people.append(list(next(person_iterator).values()))
        except StopIteration:
            return people
