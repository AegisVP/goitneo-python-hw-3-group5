from exceptions.Exceptions import *
from utils.InputError import input_error
from phonebook.Name import Name
from phonebook.Phone import Phone
from phonebook.Birthday import Birthday


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
        if self.birthday:
            str += f"{self.fields['birthday']}: {self.birthday:<14}"
        if self.phones:
            str += f"{self.fields['phones']}: {'; '.join(self.phones)}"
        return str
    # end def

    def __getitem__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]

    def __setitem__(self, key, value):
        if key in self.__dict__:
            self.__dict__[key] = value

    @input_error
    def add_phone(self, phone):
        if phone in self.phones:
            raise DuplicateEntry('Телефон')
        # end if

        self.phones.append(str(Phone(phone)))
        return "Номер телефона додано успішно"
    # end def

    @input_error
    def set_birthday(self, birthday):
        self.birthday = str(Birthday(birthday))
        return "День народження записано успішно"
    # end def

    @input_error
    def delete_phone(self, phone):
        try:
            self.phones.remove(str(Phone(phone)))
        except ValueError:
            raise PhoneNotFound
        # end try

        return "Номер телефона видалено успішно"
    # end def

    @input_error
    def modify_phone(self, old_phone=None, new_phone=None, *args):
        if len(args) > 0:
            raise Exception('Забагато аргументів')
        if old_phone == None:
            raise PhoneNotEntered
        if new_phone == None:
            raise PhoneNotEntered('новий')
        # end if

        try:
            idx = self.phones.index(old_phone)
        except ValueError:
            raise PhoneNotFound
        # end try

        self.phones[idx] = str(Phone(new_phone))
        return "Номер телефона змінено успішно"
    # end def

    @input_error
    def find(self, needle):
        if needle not in self.phones:
            raise PhoneNotFound
        return needle
    # end def
