from datetime import datetime
from collections import UserDict, defaultdict
from phonebook import Record, Name
from exceptions.Exceptions import *
from writers.FileWriter import FileWriter


def saver(func):
    def inner(self, *args, **kwargs):
        msg = func(self, *args, **kwargs)
        self.save()
        return msg
    # end def
    return inner
# end def


class AddressBook(UserDict):
    def __init__(self, **config):
        filename = config.get("filename")
        self.data = UserDict()
        self.database_connector = FileWriter(filename)
    # end def

    @error_handler
    def save(self):
        self.database_connector.save(self.data)
    # end def

    @error_handler
    def load(self):
        self.data = UserDict(self.database_connector.load())
    # end def

    def find(self, needle):
        res = self.data.get(needle, None)

        if res == None:
            raise NoDataFound("Контакт не знайдений")
        # end if

        return res
    # end def

    @saver
    def add_record(self, record):
        if type(record) != Record:
            raise IncorrectDataType
        # end if

        if record.name in self.data.keys():
            record.phones.extend(self.data[record.name].phones)
            record.phones = list(set(record.phones))
            return self.modify_record(record)
        # end if

        self.data[record.name] = record
        return "Контакт доданий успішно"
    # end def

    @saver
    def change_name(self, old_name, new_name=None):
        if new_name == None:
            raise InsufficientDataEntered("Введіть нове імʼя")
        if old_name == new_name:
            return "Нічого не міняю"
        if new_name in self.data.keys():
            raise DuplicateEntry(new_name)
        # end if

        self.data[old_name].name = str(Name(new_name))
        self.data[new_name] = self.data.pop(old_name)
        return f"Імʼя {old_name} змінено на {new_name}"
    # end def

    @saver
    def modify_record(self, record):
        if type(record) != Record:
            raise IncorrectDataType
        # end if

        self.data[record.name] = record
        return "Контакт змінений успішно"
    # end def

    @saver
    def delete_record(self, name):
        if name not in self.data:
            raise NoDataFound("Контакт не знайдений")
        # end if

        self.data.pop(name)
        return "Контакт видалений успішно"
    # end def

    def get_upcoming_birthdays(self, current_date=None):
        if current_date == None or type(current_date) != datetime.date:
            current_date = datetime.now().date()
        # end if

        next_birthdays = defaultdict(list)
        for record in list(self.data.values()):
            if record.birthday == None:
                continue
            # end if

            celebrate_day = record.get_celebrate_date(current_date.year)
            if celebrate_day == None:
                continue

            if (celebrate_day > current_date and (celebrate_day - current_date).days <= 7):
                weekday: int = int(celebrate_day.strftime("%w"))
                if weekday == 0 or weekday == 6:
                    weekday = 1
                # end if
                next_birthdays[weekday].append(record)
            # end if
        # end for
        return next_birthdays
    # end def
# end class
