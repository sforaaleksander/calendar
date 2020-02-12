import ui
import storage
import os
import datetime

NOW = datetime.date.today()
NOW = NOW.strftime("%d/%m/%Y")


def main():
    os.system("clear")
    ui.print_todays_date(NOW)
    ui.print_current_day_events()
    start_menu()


def start_menu():
    ui.print_menu()
    user_choice = ui.gather_input(["s", "c", "d", "q"])
    dictionary_choice = {"s": schedule, "c": cancel, "d": go_to_date, "q": quit}
    if user_choice in dictionary_choice.keys():
        dictionary_choice[user_choice]()


def schedule():
    os.system("clear")
    ui.print_current_day_events()
    plan_name = ui.gather_input(title="What is your plan? ")
    start_time = ui.gather_hours(title="When does it start? [hh:mm]")
    end_time = ui.gather_hours(title="When does it end? [hh:mm] ")

    hours = f"{str(start_time)} - {str(end_time)}"
    full_entry = f"{hours} : {plan_name}\n"
    storage.write_to_file(full_entry)
    main()


def cancel():
    os.system("clear")
    ui.print_current_day_events(count="yes")
    meeting_no = ui.gather_input(input_type=int, title="Which event you want to cancel? Type the number: ")
    plans = storage.read_from_file()
    print(plans)
    del plans[meeting_no-1]
    storage.update_file(plans)
    main()


def go_to_date():
    editing_date = ui.gather_date("Which date do you want to go to? [dd/mm/yyyy]")
    ui.print_todays_date(NOW)
    ui.print_other_date(editing_date)
    ui.print_current_day_events()


def go_to_todays_date():
    main()


main()
