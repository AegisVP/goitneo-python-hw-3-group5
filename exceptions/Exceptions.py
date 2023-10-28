class InsufficientDataEntered(Exception):
    pass


class NoDataFound(Exception):
    pass


class IncorrectDataType(Exception):
    pass


class IncorrectNameFormat(Exception):
    pass


class IncorrectPhoneFormat(Exception):
    pass


class IncorrectDateFormat(Exception):
    pass


class DuplicateEntry(Exception):
    pass


class InvalidDate(Exception):
    pass


class FileAccessError(Exception):
    pass


def error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InsufficientDataEntered as e:
            print(f"{e if len(str(e)) else 'Введені некоректні дані'}")
            raise InsufficientDataEntered
        except NoDataFound as e:
            print(f"{e if len(str(e)) else 'Данні не знайдено'}")
            raise NoDataFound
        except IncorrectDataType as e:
            print(f"{e if len(str(e)) else 'Некорректний тип данних'}")
            raise IncorrectDataType
        except IncorrectNameFormat as e:
            print(
                f"{e if len(str(e)) else 'Імʼя починається з літери та містить лише літери, цифри, _ та -'}")
            raise IncorrectNameFormat
        except IncorrectPhoneFormat as e:
            print(
                f"{e if len(str(e)) else 'Введіть 10 цифр без символів як номер телефона'}")
            raise IncorrectPhoneFormat
        except IncorrectDateFormat as e:
            print(f"{e if len(str(e)) else 'Дата має бути в форматі DD.MM.YYYY'}")
            raise IncorrectDateFormat
        except DuplicateEntry as e:
            print(f"{(str(e) if len(e.args) > 0 else 'Запис')} вже існує")
            raise DuplicateEntry
        except InvalidDate as e:
            print(f"{e if len(str(e)) else 'Дата не існує'}")
            raise InvalidDate
        except FileAccessError as e:
            print(
                f"Неможливо {({'read': 'прочитати файл', 'write': 'записати в файл'}[str(e)])}")
            raise FileAccessError
        except ValueError as e:
            print(e)
            raise ValueError
        except KeyError as e:
            print(e)
            raise KeyError
        except IndexError as e:
            print(e)
            raise IndexError
        except Exception as e:
            print(e)
            raise Exception
        # end try
    return inner
# end def
