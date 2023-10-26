from exceptions.Exceptions import *


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            raise Exception(
                "Значення не правильне"
            )
        except KeyError:
            raise Exception(
                "Значення не знайдене"
            )
        except IndexError as e:
            raise Exception(
                e
            )
        except NoDataEntered:
            raise Exception(
                "Недостатньо данних введено"
            )
        except PhoneNotEntered as e:
            raise Exception(
                f"Введіть {((str(e) + ' ') if (len(e.args) > 0) else '')}номер телефона"
            )
        except PhoneNotFound:
            raise Exception(
                "Номер телефона не знайдено"
            )
        except IncorrectPhoneFormat:
            raise Exception(
                "Введіть 10 цифр як номер телефона"
            )
        except NoDataFound:
            raise Exception(
                "Нічого не знайдено"
            )
        except UserNotFound:
            raise Exception(
                "Користувача не знайдено"
            )
        except IncorrectDataType:
            raise Exception(
                "Некорректний тип данних"
            )
        except IncorrectNameFormat:
            raise Exception(
                "Імʼя має починатись з літери та містити лише літери, цифри, _ та -")
        except IncorrectDateFormat:
            raise Exception(
                "Дата має бути в форматі DD.MM.YYYY"
            )
        except DuplicateEntry as e:
            raise Exception(
                f"{(str(e) if len(e.args) > 0 else 'Запис')} вже існує"
            )
        except Exception as e:
            raise Exception(
                e
            )
        # end try
    return inner
# end def
