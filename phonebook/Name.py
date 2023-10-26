import re
from phonebook.Field import Field
from exceptions.Exceptions import IncorrectNameFormat


class Name(Field):
    regex = r"[A-Za-z]+[_\-\w]*"

    @staticmethod
    def is_name(cls, number):
        return re.fullmatch(cls.regex, number)
    # end def

    def __init__(self, name):
        if not self.is_name(name):
            raise IncorrectNameFormat
        # end if
        self.value = name
    # end def
# end class
