from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Дата має бути у форматі ДД.ММ.РРРР")


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        self.phones = []
        if phone:
            self.add_phone(phone)
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def __str__(self):
        phones = ", ".join(p.value for p in self.phones)
        return f"{self.name.value}: {phones}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def __str__(self):
        return "\n".join(str(rec) for rec in self.data.values())
