import json

# Function that verify if the every element of phone number is digit and if the lenght of the number is == 10
def verify_phone_number(phone_number):
    for digit in phone_number:
        if not digit.isdigit():
            return False

    return len(phone_number) == 10

# Verify email function
def verify_email_address(email):
    if "@" not in email: # Check if the "@" element is in the "email"
        return False

    split_email = email.split("@") # split the "email"
    identifier = "".join(split_email[:-1])
    domain = split_email[-1]

    if len(identifier) < 1:
        return False

    if "." not in domain:
        return False

    split_domain = domain.split(".")

    for section in split_domain:
        if len(section) == 0:
            return False

    return True

# Function that check if in the contact object exist the contacts based on the first and last name parameters
def get_contact_by_name(first_name, last_name, contacts):
    for contact in contacts:
        if contact["First Name"] == first_name and contact["Last Name"] == last_name:
            return contact

    return None

# Read contact file based on path that we provide
def read_contacts(file_path):
    try:
        with open(file_path, 'r') as f:
            contacts = json.load(f)['contacts']
    except FileNotFoundError:
        contacts = []

    return contacts

# Write new contact in our JSON file
def write_contacts(file_path, contacts):
    with open(file_path, 'w') as f:
        contacts = {"contacts": contacts}
        json.dump(contacts, f)
