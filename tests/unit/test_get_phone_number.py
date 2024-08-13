"""
Tests the get_phone_number() method in create_and_load_data.py
"""

from phone_numbers.phone_number import PhoneNumber


def test_get_phone_number() -> None:
    """
    This test validates all phone numbers that are generated and given to the fake
    people in the application.\n

    All phone numbers generated should:\n
    - start with a "+"\n
    - be 13 characters long (without the "+", it should be 12 characters long)
    - all characters after the "+" should be numbers
    """
    phone_number = PhoneNumber().get_phone_number()

    assert phone_number.startswith("+")
    assert len(phone_number[1:].replace(" ", "")) == 12
    assert phone_number[1:].replace(" ", "").isnumeric()
