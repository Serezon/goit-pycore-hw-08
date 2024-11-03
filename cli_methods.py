from functools import wraps
import address_book

def input_error_factory(default_message="Invalid input", value_error_message=None, index_error_message=None):
    if value_error_message is None:
        value_error_message = default_message
    if index_error_message is None:
        index_error_message = default_message

    def input_error(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return value_error_message
            except IndexError:
                return index_error_message
            except Exception:
                return default_message

        return inner
    
    return input_error

def parse_input(user_input):
    if not user_input:
        return None, None
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error_factory(value_error_message="Please provide a name and a phone number.")
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name].add_phone(phone)
        return "Phone added to existing contact."

    record = address_book.Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return "Contact added."

@input_error_factory(value_error_message="Please provide a name and a phone number.")
def change_contact(args, contacts):
    name, old_phone, phone = args
    if name in contacts:
        contacts[name].edit_phone(old_phone, phone)
        return "Phone number changed."
    else:
        return "Contact not found."

@input_error_factory(index_error_message="Please provide a name.")
def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        phones = contacts[name].phones
        if len(phones) > 0:
            print(f"Phone numbers for {name}:")
            for phone in phones:
                print(phone)
        else:
            return "No phone numbers found."
                
    else:
        return "Contact not found."

@input_error_factory(value_error_message="Please provide a name.")
def get_birthday(args, contacts):
    name = args[0]
    if name in contacts:
        birthday = contacts[name].birthday
        if birthday:
            return f"{name} birthday: {birthday}"
        else:
            return "No birthday found."
    else:
        return "Contact not found."

@input_error_factory(value_error_message="Please provide a name and a birthday.")
def add_birthday(args, contacts):
    name, birthday = args
    if name in contacts:
        contacts[name].add_birthday(birthday)
        return "Birthday added."
    else:
        return "Contact not found."

def get_upcoming_birthdays(contacts):
    def print_birthday(contact):
        return f"{contact.name.value} has a birthday on {contact.birthday.value.date()}"

    return "\n".join([print_birthday(contact) for contact in address_book.get_upcoming_birthdays(contacts)])

def get_contacts(contacts):
    return contacts