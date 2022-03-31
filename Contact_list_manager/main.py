import json
from functions import verify_phone_number, verify_email_address, read_contacts, write_contacts, get_contact_by_name


CONTACT_FILE_PATH = "contacte.json"

def write_contacts(file_path, contacts):
    with open(file_path, 'w') as f:
        contacts = {"contacts": contacts}
        json.dump(contacts, f)


def add_contact(contacts: list):
    first_name = input("First Name: ").lower().strip()
    last_name = input("Last Name: ").lower().strip()
    mobile = input("Mobile Phone Number: ").strip()
    home = input("Home Phone Number: ").strip()
    email = input("Email Address: ").strip()
    address = input("Address: ").strip()

    if not first_name or not last_name:
        print("Contact must have a first and last name.")
    elif mobile and not verify_phone_number(mobile):
        print("Invalid mobile phone number.")
    elif home and not verify_phone_number(home):
        print("Invalid home phone number.")
    elif email and not verify_email_address(email):
        print("Invalid email address.")
    elif get_contact_by_name(first_name, last_name, contacts):
        print("A contact with this name already exists.")
    else:
        Data = {'First Name': first_name,'Last Name': last_name, "Mobile": mobile, "Home": home, "Email": email, "Address": address}
        contacts.append(Data)
        print("Contact added")
    return
    print("You entered invalid information. This contact is not added")


def del_contact_by_name(contacts):
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    
    contact = get_contact_by_name(first_name, last_name, contacts)
    if not contact:
        print("There is no person with this name in list!")
    else:
        confirm = input("Are you sure you would like to delete this contact (y/n)? ").lower()
        if confirm == "y": 
            contacts.remove(contact)
            print("Contact deleted!")


def get_contact_string(contact):
    string = f'{contact["First Name"].capitalize()} {contact["Last Name"].capitalize()}'

    for field in ["Mobile", "Home", "Email", "Address"]:
        value = contact[field]
        if not value:
            continue

        string += f"\n\t{field}: {value}"

    return string


def list_contacts(contacts):
    sorted_contacts = sorted(contacts, key=lambda x: x['First Name'])

    for i, contact in enumerate(sorted_contacts):
        print(f"\n{i + 1}. {get_contact_string(contact)}")


def main(contacts_path):
    print("Welcome to your contact  list!")
    print("""The following is a list of useable commands: 
    add": Adds a contact.
    "delete": Deletes a contact.
    "list": Lists all contacts.
    "search": Searches for a contact by name.
    "q": Quits the program and saves the contact list.""")


contacts = read_contacts("contacte.json")
while True:
    inpt = input("\nType a comman: ")
    if inpt == "q":
        write_contacts("contacte.json", contacts)
        print("Contacts were succesfully saved!")
        break
    elif inpt == "add":
        add_contact(contacts)
    elif inpt == "lst":
        list_contacts(contacts)
    elif inpt == "del":
        del_contact_by_name(contacts)
