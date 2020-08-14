import usr_data as ud
import data_conversion_primitives as dcp
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
                passphrase_a = dcp.OS2IP(dcp.nochunk_PT2OS(passphrase_a))
                passphrase_a = pow(passphrase_a, 65537, 206013970136021274755909796996044923643)
                break
            else:
                print("Passphrases do not match. Try again.")
        except (ValueError, TypeError):
            print("Enter a valid passphrase.")
    return [user, passphrase_a]

def signup_pqned(data, pqned):
    data.extend(pqned)
    ud.add_data(data)
    print(ud.read_table())

def login():
    while True:
        try:
            user = str(input("Enter your username:\n> "))
            if ud.search_column('username', user):
                break
            else:
                print("Username doesn't exist.")
        except (TypeError, ValueError):
            print("Enter a valid username.")
    while True:
        try:
            passphrase = getpass(prompt = "Passphrase: ")
            passphrase = dcp.OS2IP(dcp.nochunk_PT2OS(passphrase))
            passphrase = pow(passphrase, 65537, 206013970136021274755909796996044923643)
            if passphrase == ud.get_field(user, 'password'):
                break
            else:
                print("Incorrect passphrase. Try again.")
        except (TypeError, ValueError):
            print("Enter a valid passphrase.")
    return user

def message_loc_get():
    while True:
        try:
            location = int(input("\n[1] File or \n[2] String\n[3] Delete account\n> "))
            if location not in (1, 2, 3):
                print("ERR: Enter a valid choice.")
            else:
                return location
        except (TypeError, ValueError):
            print("ERR: Enter a valid choice.")


def get_input_file():
    while True:
        filename = input("File A?\n> ")
        try:
            with open(filename):
                return filename
        except FileNotFoundError:
            print("Incorrect file or path.")

def get_output_file():
    filename = input("File B?\n> ")
    return filename
def encrpyt_or_decrypt():
    while True:
        try:
            state = int(input("[1] Encrypt file\n[2] Decrypt file\n> "))
            if state not in (1, 2):
                print("ERR: Enter a valid choice.")
            else:
                return state
        except (TypeError, ValueError):
            print("ERR: Enter a valid choice.")


def get_encrypt_list(user):
    bits = ud.get_field(user, 'bits')
    e = ud.get_field(user, 'e')
    n = ud.get_field(user, 'n')
    return [bits, e, n]
def get_decrypt_list(user):
    bits = ud.get_field(user, 'bits')
    d = ud.get_field(user, 'd')
    p = ud.get_field(user, 'p')
    q = ud.get_field(user, 'q')
    return [bits, d, p, q]
def del_user():
    user = login()
    ud.drop_row(user)
