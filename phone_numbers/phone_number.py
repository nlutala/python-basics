"""
A class that generates phone numbers
"""

from random import choice, randint

from phone_numbers.country_codes import country_codes


def get_phone_number() -> str:
    """
    Returns a phone number with an area code as a string
    """

    area_code = choice(country_codes).get("dial_code")
    area_code = "+1" if area_code is None else area_code
    numbers_to_generate = (13 + area_code.count(" ")) - len(area_code)
    phone_number = f"""{area_code} {
        ''.join(
            [str(randint(0,9)) for i in range(numbers_to_generate)]
        )
    }""".strip()
    return phone_number
