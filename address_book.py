from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not all(c.isdigit() for c in value):
            raise ValueError("Phone number must be 10 digits long")
        self.value = value

class Birthday(Field):
    def __init__(self, value):
        day, month, year = map(int, value.split("."))
        if day < 1 or day > 31 or month < 1 or month > 12 or year > datetime.now().year:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        self.value = datetime(day=day, month=month, year=year)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value.date() if self.birthday else None}"

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value

class AddressBook(UserDict):
    def __str__(self):
        for record in self.data.values():
            print(record)
        return ""

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name]

    def delete(self, name):
        del self.data[name]
