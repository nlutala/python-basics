from random import choice

from faker import Faker  # type: ignore

# Python Basics: Unit testing


def test_first_name_is_one_word_long():
    full_name = Faker().name()

    if "." in full_name.split(" ")[0]:
        first_name = full_name.split(" ")[1]
    else:
        first_name = full_name.split(" ")[0]

    assert "." not in first_name
    assert " " not in first_name


def test_last_name_is_one_word_long():
    full_name = Faker().name()

    if "." in full_name.split(" ")[0]:
        last_name = full_name.split(" ")[2]
    else:
        last_name = full_name.split(" ")[1]

    assert " " not in last_name


def test_email_address_has_domain_at_example_dot_com():
    # Python Basics: Exception Handling
    full_name = Faker().name()

    if "." in full_name.split(" ")[0]:
        first_name = full_name.split(" ")[1]
        last_name = full_name.split(" ")[2]
    else:
        first_name = full_name.split(" ")[0]
        last_name = full_name.split(" ")[1]

    email = f"{first_name.lower()}.{last_name.lower()}@example.com"

    assert email.endswith("@example.com")


def test_phone_number_does_not_contain_letters():
    phone_number = "".join(
        [choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]) for i in range(12)]
    )
    assert phone_number.isnumeric()


def test_linkedin_profile_contains_first_name_and_last_name():
    full_name = Faker().name()

    if "." in full_name.split(" ")[0]:
        first_name = full_name.split(" ")[1]
        last_name = full_name.split(" ")[2]
    else:
        first_name = full_name.split(" ")[0]
        last_name = full_name.split(" ")[1]

    linkedin_profile = f"wwww.linkedin.com/{first_name.lower()}-{last_name.lower()}"
    assert first_name.lower() in linkedin_profile
    assert last_name.lower() in linkedin_profile
