
import re
from phonebook.Field import Field
from exceptions.Exceptions import IncorrectNameFormat


class Name(Field):
    def __init__(self, name):
        if re.fullmatch(r"[A-Za-z]+[_\-\w]*", name):
            self.value = name
        else:
            raise IncorrectNameFormat
        # end if
    # end def
# end class
