import re
from phonebook.Field import Field
from exceptions.Exceptions import IncorrectNameFormat


class Name(Field):
    regex = r"[A-Za-z]+[_\-\w]*"

    @classmethod
    def is_name(cls, name):
        return re.fullmatch(cls.regex, name)
    # end def

    def __init__(self, name):
        if not self.is_name(name):
            raise IncorrectNameFormat
        # end if
        self.value = name
    # end def
# end class
