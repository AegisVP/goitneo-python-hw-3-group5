import re
from phonebook.Field import Field
from exceptions.Exceptions import IncorrectDateFormat


class Birthday(Field):
    regex = r"\d{2}[. /\\\-]\d{2}[. /\\\-]\d{4}"

    @classmethod
    def is_birthday(cls, birthday):
        return re.fullmatch(cls.regex, birthday)
    # end def

    def __init__(self, birthday):
        if not self.is_birthday(birthday):
            raise IncorrectDateFormat
        # end if
        self.value = re.sub(r"[/\\ \-]", ".", birthday)
    # end def
# end class
