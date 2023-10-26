import re
from phonebook.Field import Field
from exceptions.Exceptions import IncorrectDateFormat
from datetime import datetime


class Birthday(Field):
    regex = r"\d{2}[./\\\-]\d{2}[./\\\-]\d{4}"
    weekdays_name = {
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "Пʼятниця"
    }

    @classmethod
    def is_birthday(cls, birthday):
        return re.fullmatch(cls.regex, birthday)
    # end def

    @classmethod
    def get_next_workdays(cls, start_date=None):
        if start_date == None or type(start_date) != datetime.date:
            start_date = datetime.now().date()
        # end if

        next_work_days = list()
        for i in range(6+1):
            next_week_day = int(start_date.strftime("%w")) + i
            if next_week_day > 6:
                next_week_day -= 7
            # end if

            if next_week_day != 0 and next_week_day != 6:
                next_work_days.append(next_week_day)
            # end if
        # end for
        return next_work_days
    # end def

    def __init__(self, birthday):
        if not self.is_birthday(birthday):
            raise IncorrectDateFormat
        # end if

        try:
            bday = re.sub(r"[/\\\-]", ".", birthday)
            bday = datetime.strptime(bday, "%d.%m.%Y")
            self.value = datetime.strftime(bday, "%d.%m.%Y")
        except Exception as e:
            raise Exception("Not a valid date")
        # end try
    # end def
# end class
