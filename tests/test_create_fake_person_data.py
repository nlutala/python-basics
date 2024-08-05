from create_and_load_data import get_person

# Python Basics: Unit testing


def test_first_name_is_one_word_long():
    person = get_person(1)
    someone = next(person)
    first_name = [data for data in someone][2]

    assert "." not in first_name
    assert " " not in first_name


def test_last_name_is_one_word_long():
    person = get_person(1)
    someone = next(person)
    last_name = [data for data in someone][3]

    assert "." not in last_name
    assert " " not in last_name


def test_email_address_has_domain_at_example_dot_com():
    person = get_person(1)
    someone = next(person)
    email = [data for data in someone][4]

    assert email.endswith("@example.com")


def test_phone_number_does_not_contain_letters():
    person = get_person(1)
    someone = next(person)
    phone_number = [data for data in someone][5]
    # Get rid of the "+" character
    # and remove the spaces from the phone_number
    assert phone_number[1:].replace(" ", "").isnumeric()


def test_linkedin_profile_contains_first_name_and_last_name():
    person = get_person(1)
    someone = next(person)
    first_name = [data for data in someone][2]
    last_name = [data for data in someone][3]
    linkedin_profile = [data for data in someone][6]

    assert first_name.lower() in linkedin_profile
    assert last_name.lower() in linkedin_profile
