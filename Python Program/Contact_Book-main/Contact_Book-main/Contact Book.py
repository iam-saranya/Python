class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        self.contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

    def search_contact(self, name):
        if name in self.contacts:
            details = self.contacts[name]
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
        else:
            print(f"Contact {name} not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_book.add_contact(name, phone, email)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)

        elif choice == '4':
            print("Exiting the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


#This program is a simple implementation of a contact book using a Python class called ContactBook. The contact book allows users to perform basic operations such as adding contacts, viewing all contacts, searching for a specific contact, and exiting the program.
