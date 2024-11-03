import cli_methods as cli
import address_book

def help():
    return """
    Available commands:
    help - Show available commands.
    hello - Greet the bot.
    add <name> <phone> - Add a new contact.
    change <name> <old_phone> <new_phone> - Change the phone number of a contact.
    phone <name> - Get the phone number of a contact.
    add-birthday <name> <birthday> - Add a birthday to a contact.
    show-birthday <name> - Show the birthday of a contact.
    birthdays - Show upcoming birthdays.
    all - Get all contacts.
    close - Close the bot.
    exit - Close the bot.
    """

def main():
    contacts = address_book.AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = cli.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(cli.add_contact(args, contacts))
        elif command == "change":
            print(cli.change_contact(args, contacts))
        elif command == "phone":
            print(cli.get_phone(args, contacts))
        elif command == "all":
            print(cli.get_contacts(contacts))
        elif command == "add-birthday":
            print(cli.add_birthday(args, contacts))
        elif command == "show-birthday":
            print(cli.get_birthday(args, contacts))
        elif command == "birthdays":
            print(cli.get_upcoming_birthdays(contacts))
        elif command == "help":
            print(help())
        else:
            print("Invalid command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
