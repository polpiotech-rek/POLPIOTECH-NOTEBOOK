from os import system, getcwd, chdir, listdir
from time import sleep, gmtime, strftime
from termcolor import cprint, colored
from sys import exit

import colorama, os

colorama.init


class Main():

    def __init__(self):
        system("clear")
        self.date_and_time()
        print()
        self.path_file()
        print()
        self.write_file()
        system("clear")
        self.process_record()
        self.close_program()

    def date_and_time(self):
        systemDate = strftime("%a, %d %b %Y", gmtime())
        systemTime = strftime("%r")
        print(systemDate, systemTime)

    def path_file(self):
        cprint(" SPECIFY THE FILE SAVE PATH: ", "white", "on_yellow")
        path = str(input("ENTER THE PATH: "))
        print()
        chdir(path)
        path_destination = getcwd()
        cprint(" THE FILE WILL BE SAVED IN: ", "white", "on_yellow")
        print(colored(path_destination, "black", "on_light_green"))
        print()
        cprint(" DIRECTORIES AND FILES IN THE SPECIFIED LOCATION: ", "white", "on_yellow")
        for item in listdir('.'):
            if os.path.isdir(item):
                cprint('{} - [ D ]'.format(item), "white", "on_light_cyan")
            else:
                cprint('{} - [ F ]'.format(item), "black", "on_light_green")

    def write_file(self):
        systemDate_wf = strftime("%a, %d %b %Y", gmtime())
        systemTime_wf = strftime("%r")
        
        cprint(" ENTER NAME TEXT DOCUMENT: ", "white", "on_yellow")
        nameFile = str(input("ENTER THE NAME FILE: ") + ".txt")
        print()
        with open(nameFile, "a") as file:
            if file.writable:
                cprint(" WRITE TEXT IN A TEXT DOCUMENT: ", "white", "on_yellow")
                file.write(systemDate_wf + " " + systemTime_wf + "\n" +(input("ENTER THE TEXT: ") + "\n" + "\n"))
            file.close()
            
    def process_record(self):
        cprint(" SAVING THE FILE... ", "white", "on_yellow")
        for i in range(101):
            print("\rLOADING {}%".format(i), end='')
            sleep(0.03)
        system("clear")

    def close_program(self):
        cprint(" PROGRAM CLOSING ALERT: ", "white", "on_yellow")
        alert = str(input("DO YOU WANT CLOSE PROGRAM? (y/n): "))
        if alert == "y":
            system("clear")
            cprint("     SEE YOU SOON!     ", "white", "on_yellow")
            cprint("░░░░░░░░░░░█           ", "black", "on_white")
            cprint("░░░░░░░░░▄▄█▄▄         ", "black", "on_white")
            cprint("░░░░░▀▀▀██▀▀▀██▀▀▀     ", "black", "on_white")
            cprint("░▄▄▄▄▄▄▄███████▄▄▄▄▄▄▄ ", "black", "on_white")
            cprint("░░░█▄█░░▀██▄██▀░░█▄█   ", "black", "on_white")
            exit()
        else:
            path_program = "/home/rekbod/Pulpit/Projects/Python/POLPIOTECH® NOTEBOOK/Modules/"
            chdir(path_program)
            system("python3 main.py")

        
main = Main()