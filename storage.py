def write_to_file(entry, file_name="plans.txt"):
    with open(file_name, "a") as f:
        f.write(entry)
    print("Plan added.")


def read_from_file(file_name="plans.txt"):
    with open(file_name, "r") as f:
        return f.readlines()


def update_file(updated_plans, file_name="plans.txt"):
    with open(file_name, "w") as f:
        f.write("".join(updated_plans))
