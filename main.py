import re
from datetime import datetime
from pathlib import Path
from variables import *
from phonebook import Record, Phone, Name, Birthday, AddressBook
from exceptions.Exceptions import *


book = dict()


@error_handler
def find_records(*data):
    found = []
    for needle in data:
        res = book.find(needle)
        if res:
            found.append(res)
        # end if
    # end for

    return found
    # end for
# end def


@error_handler
def add_entry(name, *args):
    if len(args) < 1:
        raise InsufficientDataEntered

    record = book.data.get(name, None) or Record(name)

    msg = []
    success = False
    for arg in args:
        if Birthday.is_date_format(arg):
            msg.append(record.set_birthday(arg))
            success = True
        elif Phone.is_phone(arg):
            msg.append(record.add_phone(arg))
            success = True
        else:
            msg.append(f"Запис '{arg}' в невірному форматі. Пропускаю")
        # end if
    # end for

    if success:
        msg.append(book.add_record(record))
    # end if

    if len(msg) == 0:
        msg.append("Нічого не вийшло записати")
    # end if

    return "\n".join(msg)
# end def


@error_handler
def modify_entry(name, *args):
    if len(args) < 1:
        raise InsufficientDataEntered

    record: Record = book.find(name)

    msg = []
    for arg in args:
        if Name.is_name(arg):
            msg.append(book.change_name(name, arg))
        else:
            phonelist = re.split('-|_', arg)

            if len(phonelist) == 2 and Phone.is_phone(phonelist[0]) and Phone.is_phone(phonelist[1]):
                msg.append(record.modify_phone(phonelist[0], phonelist[1]))
            else:
                msg.append(f"Запис '{arg}' в невірному форматі. Пропускаю")
            # end if
        # end if

        if len(args) == 0:
            break
        # end if
    # end while

    if len(msg) == 0:
        msg.append("Нічого не змінено")
    # end if

    return "\n".join(msg)
# end def


@error_handler
def delete_entry(name, phone=None):
    if phone == None:
        return book.delete_record(name)
    # end if

    if Birthday.is_date_format(phone):
        raise IncorrectDataType("Неможливо видалити День народження")
    # end if

    return book.find(name).delete_phone(phone)
# end def


@error_handler
def print_data(data, fields_to_show=["all"]):
    if len(data) == 0:
        raise NoDataFound
    # end if

    msg = []
    data = list(data)
    data.sort
    for record in data:
        if "all" in fields_to_show:
            msg.append(str(record))
            continue
        # end if

        temp_rec = Record(record.name)
        for field in fields_to_show:
            rec_data = record[field]

            if rec_data != None:
                temp_rec[field] = rec_data
            # end if
        # end for
        msg.append(str(temp_rec))
    return "\n".join(msg)
# end def


def get_birthdays_per_week():
    next_birthdays = book.get_upcoming_birthdays()

    msg = []
    for next_workday in Birthday.get_next_workdays():
        if len(next_birthdays[next_workday]):
            bday_str = ", ".join(list(map(
                lambda x: f"{x.name} ({(datetime.now().year - int(x.birthday[6:]))})",
                next_birthdays[next_workday]
            )))
            msg.append(
                f"{Birthday.weekdays_name[next_workday]:>11}: {bday_str}"
            )
        # end if
    # end for

    if len(msg):
        return "\n".join(msg)
    # end if

    return "На наступному тижні немає іменинників"
# end def


def run_bot():
    global book

    try:
        book.load()
    except FileAccessError as e:
        if str(e) == "read":
            print("Була помилка читання файла.")
        else:
            raise Exception("Unknow error")
        # end if
    except Exception as e:
        print(e)
        print("#\n#  Аварійне завершення програми!\n#")
        exit(0)
    # end try

    print(greeting)

    while True:
        try:
            user_input = input(">>> ")
            if len(user_input) == 0:
                continue
            # end if

            command, *data = user_input.strip().split()
            command = command.casefold()

            if command in ["hello", "hi"]:
                print("Чим я можу допомогти?")
            elif command in ["help"]:
                print(help_text)
            elif command in ["add", "new", "add-birthday"]:
                print(add_entry(*data))
            elif command in ["delete", "remove", "rem", "del"]:
                print(delete_entry(*data))
            elif command in ["edit", "change", "modify"]:
                print(modify_entry(*data))
            elif command in ["show", "find"]:
                print(print_data(find_records(*data), ["all"]))
            elif command in ["phone", "phones"]:
                print(print_data(find_records(*data), ["phones"]))
            elif command in ["show-birthday", "birthday", "bday"]:
                print(print_data(find_records(*data), ["birthday"]))
            elif command in ["all", "list", "list-all"]:
                print(print_data(book.data.values()))
            elif command in ["birthdays", "celebrate"]:
                print(get_birthdays_per_week())
            elif command in ["close", "quit", "exit", "bye"]:
                print("До побачення!")
                book.save()
                break

            # ****** remove after testing ******
            elif command in ["save"]:
                book.save()
                print("Данні збережено")
            elif command in ["load"]:
                book.load()
                print("Данні завантажено")
            # **********************************

            else:
                print("Сформулюйте запит відповідно командам в 'help'")
            # end if

        except Exception as e:
            if len(str(e)):
                print(e)
            continue
        # end try
    # end while
# end def


if __name__ == "__main__":
    book = AddressBook(filename=Path(__file__).parent / 'phonebook.bin')
    run_bot()
# end if
