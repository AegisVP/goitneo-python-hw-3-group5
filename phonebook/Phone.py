import re
from phonebook.Field import Field
from exceptions.Exceptions import IncorrectPhoneFormat


class Phone(Field):
    def __init__(self, number):
        if re.fullmatch(r"\d{10}", number):
            self.value = number
        else:
            raise IncorrectPhoneFormat
    # end def
# end class
