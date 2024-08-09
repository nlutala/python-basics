"""
Tests the get_phone_number() method in create_and_load_data.py
"""

from create_and_load_data import get_phone_number


def test_get_phone_number_starts_with_plus() -> None:
    """
    All phone numbers generated should start with a "+" followed by a series of numbers.
    """
    phone_number = get_phone_number()

    assert phone_number.startswith("+")


def test_get_phone_number_is_12_digits_long() -> None:
    """
    All phone numbers generated should be 12 digits long (13 characters in total
    including the "+").
    """
    phone_number = get_phone_number()

    assert len(phone_number[1:].replace(" ", "")) == 12
    assert phone_number[1:].replace(" ", "").isnumeric()
