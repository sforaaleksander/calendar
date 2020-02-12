import storage


def print_current_day(count="no"):
    schedule = storage.read_from_file()
    if schedule:
        print("Your schedule for today: ")
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


def print_menu():
    print("Menu:\n"
          "(s) schedule a new meeting\n"
          "(c) cancel an existing meeting\n"
          "(q) quit")


