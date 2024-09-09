"""
A module that generates fake contact data (or records rather)
"""

from uuid import uuid4

from create_and_load.phone_numbers.phone_number import get_phone_number
from faker import Faker


def get_contacts(number_of_contacts: int) -> iter(list[str]):  # type: ignore
    """
    Returns a lazy generator of contacts.\n

    :param - number_of_contacts (int) - How many contacts that should be generated.

    yields a list [id, name, phone_number]
    """
    for i in range(number_of_contacts):
        id = str(uuid4())
        name = Faker().name()
        phone_number = get_phone_number()

        yield [id, name, phone_number]
