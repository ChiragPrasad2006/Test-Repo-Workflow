import json

def save(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def load():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

contacts = load()

while True:
    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter the contact name: ")
        phone = input("Enter the phone number: ")
        contacts[name] = phone
        save(contacts)
        print("Contact saved.")
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            for name, phone in contacts.items():
                print(name + ": " + phone)
    elif choice == "3":
        print("Exit")
        break
    else:
        print("Invalid choice.")