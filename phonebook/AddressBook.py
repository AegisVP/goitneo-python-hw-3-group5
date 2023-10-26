import re
from phonebook.Record import Record
from phonebook.Name import Name
from writers.FileWriter import FileWriter
from utils.InputError import input_error
from exceptions.Exceptions import *
from collections import UserDict


def save(func):
    def inner(self, *args, **kwargs):
        func(self, *args, **kwargs)
        self.database.save(self.data)
    # end def
    return inner
# end def


class AddressBook(UserDict):
    def __init__(self, **config):
        filename = config.get("filename", "phonebook.json")
        self.database = FileWriter(filename)
        self.data = UserDict(self.database.load())
    # end def

    def __del__(self):
        self.database.save(self.data)
    # end def

    @input_error
    def find(self, needle):
        res = self.data.get(needle, None)

        if res == None:
            raise UserNotFound
        # end if

        return res
    # end def

    @input_error
    # @save
    def add_record(self, record):
        if type(record) != Record:
            raise IncorrectDataType
        # end if

        if record.name in self.data.keys():
            if len(record.phones) > 0:
                record.phones.extend(self.data[record.name].phones)
                record.phones = list(set(record.phones))
                return self.modify_record(record)
            else:
                raise DuplicateEntry("Контакт")
            # end if
        # end if

        self.data[record.name] = record
        return "Контакт доданий успішно"
    # end def

    @input_error
    def change_name(self, old_name, new_name=None):
        if new_name == None:
            raise NoDataEntered
        if old_name == new_name:
            raise DuplicateEntry
        if new_name in self.data:
            raise DuplicateEntry
        # end if

        self.data[old_name].name = str(Name(new_name))
        self.data[new_name] = self.data.pop(old_name)
        return f"Імʼя {old_name} змінено на {new_name}"

    @input_error
    def modify_record(self, record):
        if type(record) != Record:
            raise IncorrectDataType
        # end if

        self.data[record.name] = record
        return "Контакт змінений успішно"
    # end def

    @input_error
    def delete_record(self, name):
        self.data.pop(name)
        return "Контакт видалений успішно"
    # end def

    def return_phonebook(self):
        for record in self.data.values():
            yield record
        # end for
    # end def
