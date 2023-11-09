from os import system
from termcolor import cprint
from time import sleep

import getpass, colorama

colorama.init

class Logged():

    def __init__(self):
        system("clear")
        self.loading()
        self.login_and_password()

    def login_and_password(self):
        cprint("        POLPIOTECH®       ", "black", "on_white")
        cprint("      [ LOGIN PANEL ]     ", "white", "on_yellow")
        cprint("  ─────█─▄▀█──█▀▄─█─────  ", "black", "on_white")
        cprint("  ────▐▌──────────▐▌────  ", "black", "on_white")
        cprint("  ────█▌▀▄──▄▄──▄▀▐█────  ", "black", "on_white")
        cprint("  ───▐██──▀▀──▀▀──██▌───  ", "black", "on_white")
        cprint("  ──▄████▄──▐▌──▄████▄──  ", "black", "on_white")
        cprint("                          ", "white", "on_yellow")
        print()
        cprint(" [ Q ] -- EXIT THE PROGRAM")
        print()
        login = getpass.getpass(str("ENTER LOGIN: "))
        if login == "q":
            print()
            cprint("ARE YOU SURE, THAT YOU WANT TO CLOSE THE PROGRAM?", "white", "on_red")
            answerStop = str(input("YOUR CHOICE: "))
            if answerStop == "y":
                system("clear")
                cprint("        SEE YOU SOON!         ", "white", "on_yellow")
                cprint("░░░░░░░░░░░░░░█               ", "black", "on_white")
                cprint("░░░░░░░░░░░░▄▄█▄▄             ", "black", "on_white")
                cprint("░░░░░░░░▀▀▀██▀▀▀██▀▀▀         ", "black", "on_white")
                cprint("░░░░▄▄▄▄▄▄▄███████▄▄▄▄▄▄▄     ", "black", "on_white")
                cprint("░░░░░░█▄█░░▀██▄██▀░░█▄█       ", "black", "on_white")
                cprint("  YOU CAN CLOSE THE CONSOLE.  ", "white", "on_yellow")
                exit()
            elif answerStop == "n":
                system("clear")
                self.login_and_password()
            else:
                print()
                cprint("AN INCORRECT OPTION HAS BEEN SELECTED!", "white", "on_red")
                sleep(3)
                system("clear")
                self.login_and_password()
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
            system("clear")
            self.login_and_password()

    def loading(self):
        cprint("         WELCOME!        ", "white", "on_yellow")
        cprint("░░░░░░░░░░░░█            ", "black", "on_white")
        cprint("░░░░░░░░░░▄▄█▄▄          ", "black", "on_white")
        cprint("░░░░░░▀▀▀██▀▀▀██▀▀▀      ", "black", "on_white")
        cprint("░░▄▄▄▄▄▄▄███████▄▄▄▄▄▄▄  ", "black", "on_white")
        cprint("░░░░█▄█░░▀██▄██▀░░█▄█    ", "black", "on_white")
        cprint("   [ LOADING SYSTEM ]    ", "white", "on_yellow")
        for i in range(101):
            print("\rLOADING {}%".format(i), end='')
            sleep(0.06)
        system("clear")


logged = Logged()