def get_phonebook_from_file():
    phonebook = {}
    try:
        with open("phonebook.txt", "r") as f:
            data = f.read()
            if data != "":
                lines = data.split("\n")
                for line in lines:
                    line = line.split(":")
                    phonebook.update({line[0].strip(): line[1].strip()})
            else:
                print(
                    "\33[90m"
                    + "[INFO]: Phonebook file found, but it's empty for now."
                    + "\x1b[0m"
                )

    except FileNotFoundError:
        print(
            "\33[90m"
            + "[INFO]: Phonebook file not found, but don't worry, I'll create a new one for you."
            + "\x1b[0m"
        )
    return phonebook


def save_to_file(data):
    output = ""
    for k, v in data.items():
        output += f"{k}: {v}\n"
    output = output.removesuffix("\n")
    with open("phonebook.txt", "w") as f:
        f.write(output)


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
    except:
        return "Wrong arguments count, pls use \033[96madd [username] [phone]\x1b[0m."
    if name in contacts:
        while True:
            user_input = str(
                input(
                    f"Contact \033[96m{name}\x1b[0m already have \33[96m{contacts[name]}\x1b[0m number, it will be replaced\nAre you shure? \33[96mY/N\x1b[0m: "
                )
            )
            if user_input in ["Y", "y"]:
                return change_contact(args, contacts)
            elif user_input in ["N", "n"]:
                return "Contact not changed."
            else:
                print("Invalid command.")
    else:
        contacts[name] = phone
        return "Contact added."


def change_contact(args, contacts):
    try:
        name, phone = args
    except:
        return (
            "Wrong arguments count, pls use \033[96mchange [username] [phone]\x1b[0m."
        )
    if name in contacts:
        contacts.update({name: phone})
        return "Contact updated."
    else:
        print(f"Contact \033[96m{name}\x1b[0m does not exist, it will be created.")
        return add_contact(args, contacts)


def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return f"\033[96m{name}'s\x1b[0m phone is: \033[96m{contacts[name]}\x1b[0m"
        else:
            return f"Contact \033[96m{name}\x1b[0m does not exist. Check your spelling."
    except:
        return "Wrong arguments count, pls use'\033[96mphone [username]\x1b[0m."


def show_all(contacts: dict):
    phonebook = ""
    for name in contacts.keys():
        phonebook += f"{name}: {contacts[name]}\n"
    phonebook = phonebook.removesuffix("\n")
    if phonebook == "":
        return "Phonebook is empty."
    else:
        return phonebook


def show_help():
    help = (
        "\nAvailable commands:\n"
        "\033[96mhelp\x1b[0m, \033[96m?\x1b[0m - this help\n"
        "\033[96mclose\x1b[0m, \033[96mexit\x1b[0m, \033[96mquit\x1b[0m, \033[96mbye\x1b[0m - close application\n"
        "\033[96madd [username] [phone]\x1b[0m - adding contact to the phonebook\n"
        "\033[96mchange [username] [phone]\x1b[0m - changing contact in the phonebook\n"
        "\033[96mphone [username]\x1b[0m - show phone of the contact\n"
        "\033[96mall\x1b[0m - show all contacts in phonebook\n"
        "\033[96mhello\x1b[0m, \033[96mhi\x1b[0m - just a greeting"
    )
    return help


def main():
    print("\nWelcome to the assistant bot!")
    contacts = get_phonebook_from_file()
    dirty = False
    while True:
        user_input = input("\nEnter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit", "bye"]:
            if dirty:
                save_to_file(contacts)
            print("Good bye!")
            break
        elif command in ["hello", "hi"]:
            print("How can I help you?")
        elif command == "add":
            dirty = True
            print(add_contact(args, contacts))
        elif command == "change":
            dirty = True
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command in ["help", "?"]:
            print(show_help())
        else:
            print(
                "Invalid command. Use \033[96mhelp\x1b[0m or \033[96m?\x1b[0m to see all available commands."
            )


if __name__ == "__main__":
    main()
