import calendar
from datetime import datetime
from exceptions.Exceptions import *
from phonebook import Name, Phone, Birthday


class Record:
    fields = {
        "name": "Контакт",
        "phones": "Телефони",
        "birthday": "День народження"
    }

    def __init__(self, name):
        self.name = str(Name(name))
        self.phones = list()
        self.birthday = None
    # end def

    def __str__(self):
        str = f"{self.name:>15}:   "
        if self.birthday != None:
            str += f"{self.fields['birthday']}: {self.birthday:<14}"
        if len(self.phones) > 0:
            str += f"{self.fields['phones']}: {'; '.join(self.phones)}"
        # end if
        return str
    # end def

    def __getitem__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        # end if
    # end def

    def __setitem__(self, key, value):
        if key in self.__dict__:
            self.__dict__[key] = value
        # end if
    # end def

    def add_phone(self, phone):
        if phone in self.phones:
            raise DuplicateEntry("Телефон")
        # end if

        self.phones.append(str(Phone(phone)))
        return "Телефон доданий успішно"
    # end def

    def set_birthday(self, birthday):
        self.birthday = str(Birthday(birthday))
        return "День народження записаний"
    # end def

    def delete_phone(self, phone):
        try:
            self.phones.remove(str(Phone(phone)))
        except ValueError:
            raise NoDataFound
        # end try

        return "Телефон видалений успішно"
    # end def

    def modify_phone(self, old_phone=None, new_phone=None):
        try:
            idx = self.phones.index(old_phone)
        except ValueError:
            raise NoDataFound
        # end try

        self.phones[idx] = str(Phone(new_phone))
        return "Телефон змінений успішно"
    # end def

    def get_celebrate_date(self, celebrate_year):
        if self.birthday == None:
            return
        # end if

        is_leap = calendar.isleap(celebrate_year)
        bday = datetime.strptime(self.birthday, "%d.%m.%Y")
        month = bday.month
        day = bday.day
        if (month == 2 and day == 29 and not is_leap):
            day = 28

        return datetime(
            year=celebrate_year,
            month=month,
            day=day
        ).date()
    # end def
# end class