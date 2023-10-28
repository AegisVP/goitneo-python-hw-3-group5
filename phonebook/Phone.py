import re
from phonebook import Field
from exceptions.Exceptions import IncorrectPhoneFormat


class Phone(Field):
    regex = r"\d{10}"

    @classmethod
    def is_phone(cls, number):
        return re.fullmatch(cls.regex, number)
    # end def

    def __init__(self, number):
        if not self.is_phone(number):
            raise IncorrectPhoneFormat
        # end if
        self.value = number
    # end def
# end class


if __name__ == "__main__":
    exit()
# end if