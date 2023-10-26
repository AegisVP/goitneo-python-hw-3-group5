from exceptions.Exceptions import *


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Значення не правильне")
            raise
        except KeyError:
            print("Значення не знайдене")
            raise
        except IndexError as e:
            print(e)
            raise
        except NoDataEntered:
            print("Недостатньо данних введено")
            raise
        except PhoneNotEntered as e:
            print(
                f"Введіть {e}{(' ' if e.args.__len__ else '')}номер телефона")
            raise
        except PhoneNotFound:
            print("Номер телефона не знайдено")
            raise
        except IncorrectPhoneFormat:
            print("Введіть 10 цифр як номер телефона")
            raise
        except NoDataFound:
            print("Нічого не знайдено")
            raise
        except UserNotFound:
            print("Користувача не знайдено")
            raise
        except IncorrectDataType:
            print("Некорректний тип данних")
            raise
        except IncorrectNameFormat:
            print("Імʼя має починатись з літери та містити лише літери, цифри, _ та -")
            raise
        except DuplicateEntry as e:
            print(f"{(e if e.args.__len__ else 'Запис')} вже існує")
            raise

        except Exception as e:
            print(e)
            raise
        # end try
    return inner
# end def
