import ui
import storage
import os
import datetime

NOW = datetime.date.today()
NOW = NOW.strftime("%d-%m-%Y")


def main():
    os.system("clear")
    ui.print_todays_date(NOW)
    ui.print_current_day_events(NOW)
    start_menu()


def start_menu():
    ui.print_menu()
    current_day = NOW
    user_choice = ui.gather_input(["s", "c", "d", "q"])
    dictionary_choice = {"s": schedule, "c": cancel}
    dictionary_choice2 = {"d": go_to_date, "q": quit}
    if user_choice in dictionary_choice.keys():
        dictionary_choice[user_choice](current_day)
    else:
        dictionary_choice2[user_choice]()


def schedule(current_day):
    os.system("clear")
    ui.print_current_day_events(current_day)
    plan_name = ui.gather_input(title="What is your plan? ")
    start_time = ui.gather_hours(title="When does it start? [hh:mm]")
    end_time = ui.gather_hours(title="When does it end? [hh:mm] ")
    if not ui.check_event_conflicts(start_time, end_time, current_day):
        user_revolve = input("Time conflict found. Do you want to schedule event anyways? [Y/N]")
        if user_revolve.lower() != "y":
            schedule(current_day)
    hours = f"{str(start_time)} - {str(end_time)}"
    full_entry = f"{hours} ⸻    {plan_name}\n"
    storage.write_to_file(full_entry, current_day)
    if current_day == NOW:
        main()
    else:
        other_day_menu(current_day)


def cancel(current_day):
    os.system("clear")
    ui.print_current_day_events(current_day, count="yes")
    meeting_no = ui.gather_input(input_type=int, title="Which event you want to cancel? Type the number: ")
    plans = storage.read_from_file(current_day)
    del plans[meeting_no-1]
    storage.update_file(plans, current_day)
    if current_day == NOW:
        main()
    else:
        other_day_menu(current_day)


def go_to_date():
    user_date = ui.gather_date("Which date do you want to go to? [dd-mm-yyyy]")
    os.system("clear")
    other_day_menu(user_date)


def other_day_menu(current_day):
    os.system("clear")
    ui.print_todays_date(NOW)
    ui.print_other_date(current_day)
    ui.print_current_day_events(current_day)
    ui.print_menu_other_date()
    user_choice = ui.gather_input(["s", "c", "d", "q"])
    dictionary_choice = {"s": schedule, "c": cancel}
    dictionary_choice2 = {"d": main, "q": quit}
    if user_choice in dictionary_choice.keys():
        dictionary_choice[user_choice](current_day)
    else:
        dictionary_choice2[user_choice]()


def go_to_todays_date():
    main()


main()
