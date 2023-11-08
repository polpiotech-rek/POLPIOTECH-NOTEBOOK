from os import system
from termcolor import cprint
from time import sleep

import getpass


class Logged():

    def __init__(self):
        system("clear")
        self.loading()
        self.login_and_password()

    def login_and_password(self):
        cprint("       POLPIOTECH®       ", "black", "on_white")
        cprint("     [ LOGIN PANEL ]     ", "white", "on_yellow")
        login = getpass.getpass(str("ENTER LOGIN: "))
        password = getpass.getpass(str("ENTER PASSWORD: "))
        if login == "polpiotech" and password == "PLWP-#220193":
            print()
            cprint("LOGIN AND PASSWORD CORRECT!", "white", "on_green")
            sleep(3)
            system("clear")
            system("python3 main.py")
        else:
            print()
            cprint("LOGIN OR PASSWORD INCORRECT!", "white", "on_red")
            sleep(3)
            system("python3 logged.py")

    def loading(self):
        cprint(" █▓▒▓█▀██▀█▄░░▄█▀██▀█▓▒▓█ ", "black", "on_white")
        cprint(" █▓▒░▀▄▄▄▄▄█░░█▄▄▄▄▄▀░▒▓█ ", "black", "on_white")
        cprint(" █▓▓▒░░░░░▒▓░░▓▒░░░░░▒▓▓█ ", "black", "on_white")
        cprint("    [ LOADING SYSTEM ]    ", "white", "on_yellow")
        for i in range(101):
            print("\rLOADING {}%".format(i), end='')
            sleep(0.06)
        system("clear")

 
logged = Logged()