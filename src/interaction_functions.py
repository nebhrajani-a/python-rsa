import usr_data as ud
from getpass import getpass

def login_or_signup():
    while True:
        try:
            state = int(input("[1] Create account\n[2] Sign in\n> "))
            if state not in (1, 2):
                print("ERR: Enter a valid choice.")
            else:
                return state
        except (TypeError, ValueError):
            print("ERR: Enter a valid choice.")

def signup_core():
    while True:
        try:
            user = str(input("Enter a username:\n> "))
            if ud.search_column('username', user):
                print("Username taken, try another.")
            else:
                break
        except (TypeError, ValueError):
            print("Enter a valid username.")
    while True:
        try:
            passphrase_a = getpass(prompt = "Passphrase: ")
            passphrase_b = getpass(prompt = "Repeat passphrase: ")
            if passphrase_a == passphrase_b:
                break
            else:
                print("Passphrases do not match. Try again.")
        except GetPassWarning:
            print("Use teletype at /dev/tty or PTY-compliant device. Passphrase will be echoed: insecure.")
    return [user, passphrase_a]

def signup_pqned(data, pqned):
    data.extend(pqned)
    ud.add_data(data)
    print(ud.usr_data)

def message_loc_get():
    while True:
        try:
            location = int(input("Encrypt? \n[1] File or \n[2] String\n> "))
            if location not in (1, 2):
                print("ERR: Enter a valid choice.")
            else:
                return location
        except (TypeError, ValueError):
            print("ERR: Enter a valid choice.")


def get_input_file():
    while True:
        filename = input("Enter filename to be encrypted: ")
        try:
            with open(filename) as f:
                return filename
        except FileNotFoundError:
            print("Incorrect file or path.")

def get_output_file():
    filename = input("Enter filename to print to: ")
    return filename
