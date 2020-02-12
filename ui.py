import storage


def print_todays_date(NOW):
    print(f"Today's date: {NOW}")
    print()


def print_other_date(user_date):
    print(f"You are now editing date: {user_date}")
    print()


def print_menu():
    print("Menu:\n"
          "(s) schedule a new meeting\n"
          "(c) cancel an existing meeting\n"
          "(d) date change\n"
          "(q) quit")


def print_menu_other_date():
    print("Menu:\n"
          "(s) schedule a new meeting\n"
          "(c) cancel an existing meeting\n"
          "(d) back to today's date\n"
          "(q) quit")


def print_current_day_events(count="no"):
    schedule = storage.read_from_file()
    if schedule:
        print("Your schedule for the day: ")
    schedule = [x.strip() for x in schedule]
    if count == "yes":
        for i in range(len(schedule)):
            print(f"{i+1}.   {schedule[i]}")
        print()
    else:
        for element in schedule:
            print(element)
        print()


def gather_input(possible="all", input_type="all", title=""):
    user_input = input(title)
    valid = False
    while not valid:
        if input_type == int:
            try:
                user_input = int(user_input)
            except ValueError:
                print("Input must be a number.")
                user_input = input(title)
            else:
                return user_input
        elif possible != "all" and user_input not in possible:
            print("Type a correct value.")
            user_input = input(title)
        else:
            return user_input


def gather_hours(title=""):
    user_input = input(title)
    hours_lst = user_input.split(":")
    while len(hours_lst) != 2:
        user_input = input("Pass a correct hour format.")
        hours_lst = user_input.split(":")

    for num in hours_lst:
        valid = False
        while not valid:
            try:
                num = int(num)
                valid = True
            except ValueError:
                print("Invalid hour type.")
                user_input = input(title)
    return user_input


def gather_date(title=""):
    user_input = input(title)
    dates_lst = user_input.split("/")
    while len(dates_lst) != 3 or not check_date_format(dates_lst):
        user_input = input("Pass a correct date format. [dd/mm/yyyy]")
        dates_lst = user_input.split("/")
    for num in dates_lst:
        valid = False
        while not valid:
            try:
                num = int(num)
                valid = True
            except ValueError:
                print("Invalid date type.")     # works only if first input is correct
                gather_date(title)              # does not work when first "aa/aa/ssss"
    return user_input                           # and second is correct


def check_date_format(dates_lst):
    date_format = [2, 2, 4]
    for user_date, expected_format in zip(dates_lst, date_format):
        if len(user_date) != expected_format:
            return False
    return True
