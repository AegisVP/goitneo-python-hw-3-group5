import re
from phonebook import Field
from exceptions.Exceptions import IncorrectDateFormat, InvalidDate
from datetime import datetime


class Birthday(Field):
    regex = r"\d{2}[./\\\-]\d{2}[./\\\-]\d{4}"
    replace_regex = r"[/\\\-]"
    replace_with = "."
    str_format = "%d.%m.%Y"
    weekdays_name = {
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "Пʼятниця"
    }

    @classmethod
    def is_date_format(cls, date):
        return re.fullmatch(cls.regex, date)
    # end def

    @classmethod
    def is_date_valid(cls, date):
        date = datetime.strptime(
            re.sub(cls.replace_regex, cls.replace_with, date), cls.str_format)
        return type(datetime.strftime(date, cls.str_format)) == datetime.datetime
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
        if not self.is_date_format(birthday):
            raise IncorrectDateFormat
        # end if

        try:
            self.value = datetime.strftime(
                datetime.strptime(
                    re.sub(self.replace_regex, self.replace_with, birthday),
                    self.str_format
                ),
                self.str_format
            )
        except Exception as e:
            raise InvalidDate
        # end try
    # end def
# end class
