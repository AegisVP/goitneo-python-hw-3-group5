class InsufficientDataEntered(Exception): pass
class NoDataFound(Exception): pass
class IncorrectDataType(Exception): pass
class IncorrectNameFormat(Exception): pass
class IncorrectPhoneFormat(Exception): pass
class IncorrectDateFormat(Exception): pass
class DuplicateEntry(Exception): pass
class InvalidDate(Exception): pass
class FileAccessError(Exception): pass

def error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InsufficientDataEntered as e:
            print("Введені некоректні дані")
            if len(e): print(e)
            raise
        except NoDataFound as e:
            print("Данні не знайдено")
            if len(e): print(e)
            raise
        except IncorrectDataType as e:
            print("Некорректний тип данних")
            if len(e): print(e)
            raise
        except IncorrectNameFormat as e:
            print("Імʼя має починатись з літери та містити лише літери, цифри, _ та -")
            if len(e): print(e)
            raise
        except IncorrectPhoneFormat as e:
            print("Введіть 10 цифр без символів як номер телефона")
            if len(e): print(e)
            raise
        except IncorrectDateFormat as e:
            print("Дата має бути в форматі DD.MM.YYYY")
            if len(e): print(e)
            raise
        except DuplicateEntry as e:
            print(f"{(str(e) if len(e.args) > 0 else 'Запис')} вже існує")
            raise
        except InvalidDate as e:
            print("Дата не існує")
            if len(e): print(e)
            raise
        except FileAccessError as e:
            print(f"Неможливо {({'read': 'прочитати файл', 'write': 'записати в файл'}[str(e)])}")
            raise
        except ValueError as e:
            print(e)
            raise
        except KeyError as e:
            print(e)
            raise
        except IndexError as e:
            print(e)
            raise
        except Exception as e:
            print(e)
            raise
        # end try
    return inner
# end def