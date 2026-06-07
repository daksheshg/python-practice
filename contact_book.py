contacts={}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Added {name}")

def show_contacts():
    print("Contact List")
    for position,(name,phone) in enumerate(contacts.items(),start=1):
        print(f" {position}. {name} - {phone}")


def find_contact(name):
    if name in contacts:
        print(f"{name} - {contacts[name]}")

    else:
        print(f"Contact for {name} not in the directory")

add_contact("John", "1111111111")
add_contact("Sarah", "2222222222")
add_contact("Mike", "3333333333")

show_contacts()

find_contact("Sarah")
find_contact("Emma")