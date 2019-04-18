import os
import sys
from urllib.parse import urlparse

# Bruteforcers
import database_functions

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def GOOD_WRITE(TEXT):
    print(color.GREEN+"    [+] "+color.END+TEXT)

def INFO_WRITE(TEXT):
    print(color.BLUE+"    [i] "+color.END+TEXT)

def ERROR_WRITE(TEXT):
    print(color.RED+"    [-] "+color.END+TEXT)

def WARNING_WRITE(TEXT):
    print(color.YELLOW+"    [!] "+color.END+TEXT)

print(color.BOLD)

def BANNER():
    banner = r''' __      _____     ___         _           
 \ \    / / _ \___| _ )_ _ ___| |_____ _ _ 
  \ \/\/ /|  _/___| _ \ '_/ _ \ / / -_) '_|
   \_/\_/ |_|     |___/_| \___/_\_\___|_|  
    |-WordPress Scanner & Exploiter-----|                           
    |-Coded By Ghosty / DeaDHackS Team--|'''+'\n'
    print(banner)

def DATABASE_MAIN_MENU():
    BANNER()
    while True:
        print("\n    [1]: Display Database Content")
        print("    [2]: Clear Database")
        print("\n    [98]: Go back")
        print("    [99]: Exit WP-Broker\n")
        BRUTEFORCE_MENU_CHOICE = input("    [WP-Broker@Database]~[Root] #> ")
        if BRUTEFORCE_MENU_CHOICE == "1":
            database_functions.ReadDB()
        elif BRUTEFORCE_MENU_CHOICE == "2":
            database_functions.ClearDB()
        elif BRUTEFORCE_MENU_CHOICE == "98":
            break
        elif BRUTEFORCE_MENU_CHOICE == "99":
            sys.exit()