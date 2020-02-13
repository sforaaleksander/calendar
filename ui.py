import storage
import datetime


def print_todays_date(NOW):
    print(f"Today's date: {NOW}")
    print()


def print_other_date(user_date):
    print(f"You are now in date: {user_date}")
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


def print_current_day_events(current_day, count="no"):
    schedule = storage.read_from_file(current_day)
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
    else:
        print("No plans for the day.")
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


# def check_if_hour_not_smaller(start_hour, end_hour):


def gather_hours(title=""):
    user_input = input(title)
    hours_lst = user_input.split(":")
    while len(hours_lst) != 2:
        user_input = input("Pass a correct hour format.")
        hours_lst = user_input.split(":")
    while int(hours_lst[1]) < 0 > int(hours_lst[0]) or int(hours_lst[0]) > 24\
            or 0 > int(hours_lst[1]) > 59:
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
    dates_lst = user_input.split("-")
    while len(dates_lst) != 3 or not check_date_format(dates_lst):
        user_input = input("Pass a correct date format. [dd-mm-yyyy]")
        dates_lst = user_input.split("-")
    for num in dates_lst:
        valid = False
        while not valid:
            try:
                num = int(num)
                valid = True
            except ValueError:
                print("Invalid date type.")     # works only if first input is correct
                gather_date(title)              # does not work when first "aa-aa-ssss"
    return user_input                           # and second is correct


def check_date_format(dates_lst):
    date_format = [2, 2, 4]
    for user_date, expected_format in zip(dates_lst, date_format):
        if len(user_date) != expected_format:
            return False
    return True


def check_event_conflicts(start_hour, end_hour, current_day):
    data = storage.read_from_file(current_day)
    data = [x.split("⸻") for x in data]
    data = [x[0] for x in data]
    data = [x.split("-") for x in data]
    data = [[hour.strip() for hour in hours] for hours in data]
    start_hour = datetime.datetime.strptime(start_hour, "%H:%M").time()
    end_hour = datetime.datetime.strptime(end_hour, "%H:%M").time()

    for event in data:
        start_event = datetime.datetime.strptime(event[0], "%H:%M").time()
        end_event = datetime.datetime.strptime(event[1], "%H:%M").time()
        if start_event < start_hour < end_event or start_event < end_hour < end_event:
            user_resolve = input("Time conflict found. Do you want to schedule event anyways? [Y/N] ")
            if user_resolve.lower() != "y":
                return False
    return True


    # if not ui.check_event_conflicts(start_time, end_time, current_day):


def sort_events(current_day):
    data = storage.read_from_file(current_day)
    data = [x.split("⸻") for x in data]
    for event in data:
        event[0] = event[0].split("-")

    for event in data:
        event[0][0] = datetime.datetime.strptime(event[0][0].strip(), "%H:%M").time()
        event[0][1] = datetime.datetime.strptime(event[0][1].strip(), "%H:%M").time()
        event[1] = event[1].strip(" ")

    data = sorted(data, key=lambda x: x[0][1])
    data = sorted(data, key=lambda x: x[0][0])

    for event in data:
        event[0][0] = (event[0][0].strftime("%H:%M")).zfill(2)
        event[0][1] = event[0][1].strftime("%H:%M").zfill(2)
        print(event[0][0])

        event[0] = " - ".join(event[0])
    data = [" ⸻    ".join(e) for e in data]

    storage.update_file(data, current_day)


# sort_events("13-02-2020")


# timeStr = dateTimeObj.strftime("%H:%M:%S.%f")
# print('Current Timestamp : ', timeStr)
