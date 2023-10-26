from variables import help_text
from phonebook.Record import Record
from phonebook.Phone import Phone
from phonebook.Name import Name
from phonebook.Birthday import Birthday
from phonebook.AddressBook import AddressBook
from datetime import datetime


book = AddressBook()


def find_records(*data):
    found = []
    for needle in data:
        res = book.find(needle)
        if res:
            found.append(res)
        # end if
    # end for

    return found if len(found) > 0 else "Нічого не знайдено"
    # end for
# end def


def add_entry(name, *args):
    if len(args) < 1:
        raise Exception("Не можу додати пустий запис")

    record = book.data.get(name, None) or Record(name)

    msg = []
    for arg in args:
        try:
            if Birthday.is_birthday(arg):
                msg.append(record.set_birthday(arg))
            elif Phone.is_phone(arg):
                msg.append(record.add_phone(arg))
            else:
                raise Exception(f"Невідомий запис {arg}. Пропускаю")
            # end if
            book.add_record(record)
        except Exception as e:
            if str(e) != "":
                msg.append(str(e))
        # end try
    # end for

    if len(msg) == 0:
        msg.append("Нічого не вийшло записати")
    # end if

    return "\n".join(msg)
# end def


def delete_entry(name, phone=None, *_):
    if phone == None:
        return book.delete_record(name)
    # end if

    return delete_phone(name, phone)
# end def


def modify_entry(name, *args):
    if len(args) < 1:
        raise Exception("Недостатньо аргументів")

    record = book.find(name)
    args = list(args)

    msg = []
    while True:
        arg = args.pop(0)

        try:
            if Birthday.is_birthday(arg):
                msg.append(record.set_birthday(arg))
            elif Name.is_name(arg):
                msg.append(book.change_name(name, arg))
            elif Phone.is_phone(arg):
                msg.append(record.modify_phone(arg, args.pop(0)))
            else:
                raise Exception(f"Невідомий запис {arg}. Пропускаю")
            # end if
        except Exception as e:
            if str(e) != "":
                msg.append(str(e))
            # end if
        # end try

        if len(args) == 0:
            break
        # end if
    # end while

    if len(msg) == 0:
        msg.append("Нічого не вийшло змінити")
    # end if

    return "\n".join(msg)
# end def


def delete_phone(name, phone):
    record = book.find(name)
    record.delete_phone(phone)
    return book.modify_record(record)
# end def


def print_data(data, fields_to_show=["all"]):
    if len(data) == 0:
        return "Записна книжка пуста"
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

    output = []
    for next_workday in Birthday.get_next_workdays():
        if len(next_birthdays[next_workday]):
            bday_str = ", ".join(list(map(
                lambda x: f"{x.name} ({(datetime.now().year - int(x.birthday[6:]))})",
                next_birthdays[next_workday]
            )))
            output.append(
                f"{Birthday.weekdays_name[next_workday]:>11}: {bday_str}"
            )
        # end if
    # end for
    return "\n".join(output)
# end def


def run_bot():
    global book
    print("Вітаю!")

    while True:
        try:
            user_input = input(">>> ")
            if len(user_input) == 0:
                continue
            # end if

            command, *data = user_input.strip().split()
            command = command.casefold()

            if command in ["hello", "hi"]:
                print("Чим можу допомогті?")
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
            elif command in ["help"]:
                print(help_text)
            elif command in ["close", "quit", "exit", "bye"]:
                print("До побачення!")
                break
            else:
                print("Сформулюйте запит відповідно командам в 'help'")
            # end if
        except Exception as e:
            print(e)
            continue
        # end try
    # end while
# end def


if __name__ == "__main__":
    run_bot()
# end if
