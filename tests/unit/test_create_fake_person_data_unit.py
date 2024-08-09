import os

from create_and_load_data import write_people_to_csv_file


def test_write_people_to_csv_file():
    # Using mock (fake) for phone_number
    person = {
        "id": "mock_id_1",
        "full_name": "John Doe",
        "first_name": "John",
        "last_name": "Doe",
        "email_address": "john.doe@example.com",
        "phone_number": "+44 7512334567",
        "linkedin_profile": "wwww.linkedin.com/john-doe",
    }

    row = [list(person.values())]
    write_people_to_csv_file(row, "test_fake_person_data.csv")

    assert "test_fake_person_data.csv" in os.listdir()
    os.remove("test_fake_person_data.csv")
